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

1. `get_figma_data` with `fileKey: "i3MTtBKiPbLq7bEIJqL4yc"` and a specific
   `nodeId` to fetch a simplified node tree with resolved styles and variables.
   Always pass a `nodeId` — never fetch the whole file.
2. `download_figma_images` only when you need a visual check; save to a temp
   path, not into the repo.

### Codebase

Use the workspace file tools to read component source, CSS modules, and
[src/tokens.css](src/tokens.css). Do not run the dev server unless asked.

## The task

When the user asks for a "design check" / "alignment check" / runs the
`/design-check` prompt, produce a single report file:

**`figma-code-audit.html`** at the repo root.

Always overwrite the existing report; do not append.

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

Use exactly this structure. Keep statements short, simple, clear — one line
each. Link to files and components using workspace-relative paths.

```markdown
# Design Alignment Report

_Generated: <ISO date>_
_Figma: <link to file>_

## 1. Implemented vs. missing components

- [ ] `<ComponentName>` exists in Figma but is missing in code.
- [ ] `<ComponentName>` exists in code ([path](path)) but is missing in Figma.
- [x] All components match. <!-- only if nothing to report -->

<details>
<summary>Details</summary>

For each item above: one short paragraph on what was checked, the Figma node
id, and the code path. Link the Figma node with
`https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=<id>`.

</details>

## 2. Matching component design

- [ ] `Button` uses `#1a2b4d` in code but Figma uses `--color-navy` (`#1b2a4e`). See [src/components/button/Button.module.css](src/components/button/Button.module.css).
- [x] `Card` matches.

<details>
<summary>Details</summary>

One short block per component. Format:

**`ComponentName`** — [code](path) · [figma](node-link)
- Colors: ...
- Spacing: ...
- Radius: ...
- Typography: ...
- Sizes: ...
- Verdict: match / mismatch (list specific diffs).

</details>

## 3. Matching layout

- [ ] Home page footer is below the cards in Figma but above in code. See [src/pages/home/index.tsx](src/pages/home/index.tsx).
- [x] Layout matches.

<details>
<summary>Details</summary>

Per page or major section: what was compared (structure, order, alignment,
gaps) and the specific diff, with code + Figma links.

</details>
```

### Rules for the report

- Use `- [x]` for an OK finding and `- [ ]` for a mismatch.
- If a section has no mismatches, keep a single `- [x] All <foo> match.` line
  and still include the `<details>` block summarising what was checked.
- Link every code reference. Use workspace-relative paths, no backticks
  around file links.
- Do not invent components, tokens, or Figma nodes. If something can't be
  verified through MCP, say so explicitly in the Details block.
- Keep the top-level bullets terse. Put reasoning in `<details>`.

## House rules

- Don't add comments to code unless intent is non-obvious. One short line max.
- Don't create extra markdown files unless explicitly asked. The report is
  the only generated doc.
- Don't modify component source code as part of the design check — the
  output is the report only.
