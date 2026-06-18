# codebase-figma-alignment-demo

A small demo showing how an AI agent can detect inconsistencies between a
**Figma design** and its **codebase implementation** — in both directions
(things in Figma but not in code, and vice versa).

Preview: [Web page](https://futurice.github.io/codebase-figma-alignment-demo/)

## Project overview

- React + TypeScript + Vite app.
- Source under [src/](src/):
  - [src/pages/home/](src/pages/home/) — the demo page.
  - [src/components/](src/components/) — UI components (button, card, footer,
    header, round-button).
  - [src/tokens.css](src/tokens.css) — design tokens (colors, spacing, radius,
    typography, sizes) the agent uses as the source of truth when comparing.
- Figma file: [Codebase-Figma-Demo](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/Codebase-Figma-Demo)
  (file key `i3MTtBKiPbLq7bEIJqL4yc`).

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
   [design-alignment-report.md](design-alignment-report.md).

### Run the design check (automatically, in CI)

A GitHub Actions workflow
([.github/workflows/design-check.yml](.github/workflows/design-check.yml))
runs the same check on every push to `main` and on PRs that touch components,
pages, tokens, or the agent rules. It commits the updated report back to the
branch.

Repo secrets required:

- `FIGMA_TOKEN` — Figma personal access token.
- `ANTHROPIC_API_KEY` — for the Claude Code action that runs the agent.

## How it works

- [AGENTS.md](AGENTS.md) — task definition, what to compare, exact report format.
- [.github/prompts/design-check.prompt.md](.github/prompts/design-check.prompt.md)
  — the `/design-check` slash command that triggers the agent in VS Code.
- [.vscode/mcp.json](.vscode/mcp.json) — Figma MCP server (Framelink
  `figma-developer-mcp`) so the agent can read Figma frames as a simplified,
  token-aware tree.
- [.github/workflows/design-check.yml](.github/workflows/design-check.yml) —
  CI runner using the Claude Code GitHub Action with the same MCP server.

Latest report: [design-alignment-report.md](design-alignment-report.md).
