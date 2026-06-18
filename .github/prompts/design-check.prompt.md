---
mode: agent
description: Compare the Figma design to the codebase and write figma-code-audit.html
tools: ['codebase', 'editFiles', 'search', 'usages', 'figma']
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
   `fileKey: "i3MTtBKiPbLq7bEIJqL4yc"`. Start at the top-level page node
   (`0-1`) to discover frames, then drill into each component frame by its
   `nodeId`. Never fetch the whole file without a `nodeId`.
5. Compare the three groups defined in AGENTS.md:
   - implemented vs. missing components,
   - matching component design (tokens, colors, spacing, radius, typography, sizes),
   - matching layout (structure, order, alignment, gaps — ignore text wording).
6. Write the result to `figma-code-audit.html` at the repo root, using
   exactly the format from AGENTS.md. Overwrite any existing report.
7. Do not modify any other files.

When done, reply with a one-line summary and a link to the report.
