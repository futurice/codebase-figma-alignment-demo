# codebase-figma-alignment-demo

A small demo showing how an AI agent can detect inconsistencies between a
**Figma design** and its **codebase implementation** — in both directions
(things in Figma but not in code, and vice versa).

[Web page](https://futurice.github.io/codebase-figma-alignment-demo/)

[Figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/Codebase-Figma-Demo)

[Inconsistencies report](design-alignment-report.md)

## Project overview

- React + TypeScript + Vite app.
- Source under [src/](src/):
  - [src/pages/home/](src/pages/home/) — the demo page.
  - [src/components/](src/components/) — UI components (button, card, footer,
    header, round-button).
  - [src/tokens.css](src/tokens.css) — design tokens (colors, spacing, radius,
    typography, sizes) the agent uses as the source of truth when comparing.
- Figma file: [Codebase-Figma-Demo](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/Codebase-Figma-Demo).

## Setup

### Run the app

```bash
pnpm install
pnpm dev
```

### Run the design check (locally, in VS Code Chat)

1. Get a Figma personal access token and put it in `.env`:

   ```env
   FIGMA_API_KEY=figd_...
   ```

2. Open this repo in VS Code. The Figma MCP server is configured in
   [.vscode/mcp.json](.vscode/mcp.json) and starts automatically.

3. In Chat (agent mode), run the `/design-check` prompt. The agent reads
   [AGENTS.md](AGENTS.md) for the rules and writes the report to
   [Inconsistencies report](design-alignment-report.md). Commit the
   updated report when you're happy with it.

## How it works

- [AGENTS.md](AGENTS.md) — task definition, what to compare, exact report format.
- [.github/prompts/design-check.prompt.md](.github/prompts/design-check.prompt.md)
  — the `/design-check` slash command that triggers the agent in VS Code.
- [.vscode/mcp.json](.vscode/mcp.json) — Figma MCP server (Framelink
  `figma-developer-mcp`) so the agent can read Figma frames as a simplified,
  token-aware tree.
