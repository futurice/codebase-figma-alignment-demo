# AGENTS.md

Rules for AI agents working in this repository.

## Purpose of this repo

A small demo for using an AI agent to detect inconsistencies between the
**Figma design** and the **codebase implementation** of the same UI.

- Figma file: <https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/Codebase-Figma-Demo>
- Figma file key: `i3MTtBKiPbLq7bEIJqL4yc`
- App entrypoint: [src/main.tsx](src/main.tsx) → [src/pages/home/index.tsx](src/pages/home/index.tsx)
- Components: [src/components/](src/components/)
- Design tokens: [src/tokens.css](src/tokens.css)

## Tooling

### Figma MCP (required)

The Figma MCP server is configured in [.vscode/mcp.json](.vscode/mcp.json) and
runs `figma-developer-mcp` (Framelink) over stdio.

It reads `FIGMA_API_KEY` from `.env`.

Use these tools, in order:

1. `get_figma_data` with `fileKey: "i3MTtBKiPbLq7bEIJqL4yc"`. First call it
   without a `nodeId` to discover all canvases, components, and component
   sets in the file. Then drill into specific nodes by `nodeId` for detail.
2. `download_figma_images` to save component and page renders to
   `report-assets/` at the repo root — these are embedded in the HTML report.
3. Figma REST `POST /v1/files/<fileKey>/comments` (using `FIGMA_API_KEY`) to
   annotate inconsistent nodes in Figma. Prefix every message with
   `[design-check]`.

### Codebase

Use the workspace file tools to read component source, CSS modules, and
[src/tokens.css](src/tokens.css). Do not run the dev server unless asked.

## The task

When the user asks for a "design check" / "alignment check" / runs the
`/design-check` prompt, do all of the following:

1. Produce a single HTML report at the repo root: **`figma-code-audit.html`**.
   Always overwrite the existing report; do not append.
2. Save Figma renders used in the report under `report-assets/` (one PNG per
   component plus one for the page layout).
3. For each inconsistency, add a one-line `TODO design-check:` comment at
   the relevant spot in the codebase, with a link to the Figma node.
4. For each inconsistency, post a Figma comment on the relevant node via the
   REST API. Every message must start with `[design-check]`.
5. Commit the report, code TODO comments, and assets, then push.

### What to compare

Three groups, in this order:

1. **Implemented vs. missing components**
   - Components present in Figma but not in [src/components/](src/components/).
   - Components present in code but not in Figma.
   - Match by name, case-insensitively. Note close-but-not-equal names as
     "likely the same component, different name".

2. **Matching component design**
   For each component that exists in both:
   - Compare colors against [src/tokens.css](src/tokens.css)
     (`--color-*`). Flag hardcoded colors or wrong token usage.
   - Compare spacing/padding/gap against `--space-*`.
   - Compare border-radius against `--radius-*`.
   - Compare font-family, font-size, font-weight against `--font-*`.
   - Compare fixed sizes (button height, card width, etc.) against `--size-*`.
   - Only flag a real mismatch. Sub-pixel rounding (≤1px) is not a mismatch.

3. **Matching layout**
   For the page ([src/pages/home/index.tsx](src/pages/home/index.tsx)):
   - Same top-level structure (header, main, footer, sections)?
   - Same order of elements?
   - Same alignment / direction (row vs. column, justify, align)?
   - Same gaps and section paddings?
   - **Ignore text wording differences.**

### Report format

The report is a self-contained HTML file (inline CSS, no external JS). Group
findings into two sections in this order:

1. **Component-level audit** — one card per component covering both directions:
   components in Figma but missing in code, components in code but missing in
   Figma, and components present in both with token/style mismatches.
2. **Page layout audit** — one card per page (`src/pages/home/`), comparing
   structure, order, alignment, gaps and section paddings.

For every component card, render side-by-side:

- a **Figma PNG** from `report-assets/`,
- the relevant **code snippet** (CSS module or JSX),
- a **diff table** with a status column (✓ / ✗),
- explicit links to the Figma node and the code file,
- a clearly highlighted **TODO block** for each mismatch.

Keep wording short and factual. Use `✓ Match` / `⚠ Mismatch` badges in the
header of each card. Reference Figma nodes with
`https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=<id-with-dash>`
and code files by workspace-relative path.

### Code TODO comments

For every mismatch reported, add a single-line comment at the source location:

```
// TODO design-check: <short reason> — figma <node-link>
/* TODO design-check: <short reason> — figma <node-link> */
```

One line only. No multi-line blocks. Skip components that exist only in Figma
(no code location to mark).

### Figma comments

For every mismatch reported, post a Figma comment on the corresponding node
using the helper script in this repo:

```bash
python3 scripts/post-figma-comments.py report-assets/figma-comments.json
```

Write the findings into `report-assets/figma-comments.json` first (overwrite
any existing file). Shape:

```json
[
  {
    "node_id": "30:62",
    "message": "[design-check] <reason + action>",
    "node_offset": {"x": 0, "y": 0}
  }
]
```

The script reads `FIGMA_API_KEY` from `.env`, deletes any prior
`[design-check]` comment on each node so re-runs don't duplicate, and posts
the new ones via the Figma REST API. `node_offset` is optional and defaults
to `{x:0, y:0}`; use a small negative offset for container frames so the pin
doesn't visually overlap the first child.

Every message must start with `[design-check]` so duplicates can be detected.
The token must have the `file_comments:write` scope.

### Commit and push

After the report, code TODOs, assets, and Figma comments are in place, commit
the changes (`figma-code-audit.html`, `report-assets/**` — including
`figma-comments.json`, code TODO edits) and push to the current branch. Do
not include `.env` or local-only files.

## House rules

- Comments are allowed only when intent is non-obvious. One short line max.
  `TODO design-check:` comments are the standard way to mark inconsistencies
  in code.
- Don't create extra markdown files unless explicitly asked. The HTML report
  is the only generated doc.
- Don't refactor or restyle component source as part of the design check.
  Only add the inline `TODO design-check:` comments described above.
- Do not invent components, tokens, or Figma nodes. If something can't be
  verified, say so explicitly in the report.
