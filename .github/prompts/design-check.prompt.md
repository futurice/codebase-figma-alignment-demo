---
mode: agent
description: Compare the Figma design to the codebase, write figma-code-audit.html, mark inconsistencies in code and Figma, then commit and push.
tools: ['codebase', 'editFiles', 'search', 'usages', 'figma', 'runInTerminal', 'createFile']
---

Run a design alignment check between the Figma file and this codebase, following
the rules in [AGENTS.md](../../AGENTS.md).

Steps:

1. List the components in [src/components/](../../src/components/) and read each
   component's `.tsx` and `.module.css`.
2. Read [src/tokens.css](../../src/tokens.css) so you know the design tokens.
3. Read [src/pages/home/index.tsx](../../src/pages/home/index.tsx) and its CSS
   for the page layout.
4. Use the `figma` MCP `get_figma_data` tool with
   `fileKey: "i3MTtBKiPbLq7bEIJqL4yc"`. First call it without a `nodeId` to
   discover all canvases, components, and component sets in the file (so you
   also catch components that exist in Figma but not in code). Then drill into
   specific nodes by `nodeId` for detail.
5. Use `download_figma_images` to save one PNG per component plus one for the
   page layout into `report-assets/` at the repo root.
6. Compare the two groups defined in AGENTS.md:
   - component-level audit (existence + tokens, colors, spacing, radius,
     typography, sizes — in both directions),
   - page layout audit (structure, order, alignment, gaps — ignore wording).
7. Write the result to `figma-code-audit.html` at the repo root, using the
   HTML format from AGENTS.md (Figma PNG + code snippet + diff table side by
   side, plus a TODO block per mismatch). Overwrite any existing report.
8. For each inconsistency, add a single-line `TODO design-check:` comment at
   the relevant code location with a link to the Figma node.
9. For each inconsistency, post a Figma comment via
   `POST https://api.figma.com/v1/files/i3MTtBKiPbLq7bEIJqL4yc/comments` using
   `FIGMA_API_KEY` from `.env`. Every message starts with `[design-check]`.
10. Commit `figma-code-audit.html`, `report-assets/`, and the code TODO edits,
    then push to the current branch.

When done, reply with a one-line summary and a link to the report.
