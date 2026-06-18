---
mode: agent
description: Compare ONLY staged git changes against the Figma file; write code-changes-audit.html. Read-only — no code edits, no Figma comments, no commit.
tools: ['codebase', 'editFiles', 'search', 'usages', 'figma', 'runInTerminal', 'createFile']
---

Run a design alignment check limited to STAGED git changes. Use AGENTS.md
for the comparison conventions (tokens, colors, spacing, radius, typography,
sizes), but follow the staged-only flow below.

Steps:

1. Run `git diff --cached --name-only` to list staged files.
2. Derive the in-scope set:
   - `src/components/<name>/...` → component `<name>`.
   - `src/pages/<name>/...` → page `<name>`.
   - `src/tokens.css` → every component that references a changed token.
   - Files outside `src/` → ignore.
   If the resulting set is empty, write a short report saying
   "No design-check-relevant staged changes." and stop.
3. For each in-scope component, read the current (staged) source and call
   the `figma` MCP `get_figma_data` for the matching Figma component. Keep
   the comparison narrow — only the things that changed (variants exposed,
   tokens used, sizes, layout). Do not re-audit unrelated components.
4. For each in-scope page, compare its current (staged) layout against the
   matching Figma page canvas.
5. Reuse existing PNGs in `report-assets/` for the relevant
   components/page. Only call `download_figma_images` for an in-scope
   component/page that doesn't already have a render there.
6. Write a single self-contained HTML file at the repo root:
   **`code-changes-audit.html`**. Use the same visual style as
   `figma-code-audit.html` but include only the in-scope items, plus a
   short header block summarising:
   - the staged file list,
   - which components/pages it maps to,
   - per-card verdict (`✓ Match` / `⚠ Mismatch`).
7. Do **not** modify any source files. Do not add `TODO design-check:`
   comments. Do not write to `report-assets/figma-comments.json`. Do not
   call `scripts/post-figma-comments.py`. Do not stage, commit, or push.
   The report is the only output.

When done, reply with a one-line summary and a link to the report.
