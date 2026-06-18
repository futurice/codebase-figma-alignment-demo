---
mode: agent
description: Compare the Figma design to the codebase, write figma-code-audit.html, mark inconsistencies in code and Figma, then commit (do not push).
tools: ['codebase', 'editFiles', 'search', 'usages', 'figma', 'runInTerminal', 'createFile']
---

Run a design alignment check between the Figma file and this codebase, following
the rules in [AGENTS.md](../../AGENTS.md).

Steps:

1. Run `python3 scripts/clean-design-check.py` to strip every prior
   `TODO design-check:` line in `src/` and clear `report-assets/*.png` and
   `report-assets/figma-comments.json`, so this run starts from a clean slate.
2. List the components in [src/components/](../../src/components/) and read each
   component's `.tsx` and `.module.css`.
3. Read [src/tokens.css](../../src/tokens.css) so you know the design tokens.
4. Read [src/pages/home/index.tsx](../../src/pages/home/index.tsx) and its CSS
   for the page layout.
5. Use the `figma` MCP `get_figma_data` tool with
   `fileKey: "i3MTtBKiPbLq7bEIJqL4yc"`. First call it without a `nodeId` to
   discover all canvases, components, and component sets in the file (so you
   also catch components that exist in Figma but not in code). Then drill into
   specific nodes by `nodeId` for detail.
6. Use `download_figma_images` to save one PNG per component plus one for the
   page layout into `report-assets/` at the repo root.
7. Compare the two groups defined in AGENTS.md:
   - component-level audit (existence + tokens, colors, spacing, radius,
     typography, sizes — in both directions),
   - page layout audit (structure, order, alignment, gaps — ignore wording).
8. Write the result to `figma-code-audit.html` at the repo root, using the
   HTML format from AGENTS.md (Figma PNG + code snippet + diff table side by
   side, plus a TODO block per mismatch). Overwrite any existing report.
9. For each inconsistency, add a single-line `TODO design-check:` comment at
   the relevant code location with a link to the Figma node.
10. For each inconsistency, write a finding to
    `report-assets/figma-comments.json` (overwriting any existing file) with
    shape `[{"node_id":"...","message":"[design-check] ...","node_offset":{"x":0,"y":0}}]`.
    Then post the comments with
    `python3 scripts/post-figma-comments.py report-assets/figma-comments.json`.
    The script reads `FIGMA_API_KEY` from `.env`, deletes every prior
    `[design-check]` comment in the file, and posts the new ones.
11. Commit `figma-code-audit.html`, `report-assets/` (PNGs and
    `figma-comments.json`), and the code TODO edits **locally**. Do not
    push — the human pushes after reviewing the diff.

When done, reply with a one-line summary and a link to the report.
