# Token usage estimate

Size-based estimate of token usage for the two design-check prompts on the
runs that produced [figma-code-audit.html](figma-code-audit.html) and
[code-changes-audit.html](code-changes-audit.html). Conversion rule of
thumb: ~4 characters per token.

These numbers are **estimates**, not measured. Copilot doesn't expose
per-turn token counts to the local session store, so we approximate from
artifact sizes and the typical shape of each flow.

## Static inputs (both prompts)

| Artifact | Chars | ~Tokens |
|---|---:|---:|
| [AGENTS.md](AGENTS.md) | 6 985 | 1.7K |
| [.github/prompts/design-check.prompt.md](.github/prompts/design-check.prompt.md) | 2 714 | 0.7K |
| [.github/prompts/design-check-changes.prompt.md](.github/prompts/design-check-changes.prompt.md) | 2 166 | 0.5K |
| [src/tokens.css](src/tokens.css) | 766 | 0.2K |
| All [src/](src/) (5 components + page) | 6 917 | 1.7K |

## `/design-check` (full audit)

What gets read in / written out across the whole flow:

| Bucket | Estimate |
|---|---:|
| AGENTS.md + prompt + tokens.css + all source | ~3.6K |
| Figma MCP calls (1 root + 5 components + 1 page ≈ 7 calls × ~3–5KB) | ~10–15K |
| `download_figma_images` text responses | ~0.5K |
| Tool-call framing / intermediate planning across ~30 turns | ~10–20K |
| HTML report output (33.8KB) | ~8.4K |
| `TODO design-check:` lines + `figma-comments.json` + Python invocation | ~1.5K |
| Git status/diff/commit echoes | ~1K |
| **Total prompt (input) tokens** | **~30–45K** |
| **Total completion (output) tokens** | **~13–17K** |
| **Combined ballpark** | **~45–60K tokens** |

## `/design-check-changes` (staged-only — `Button.tsx` + `Button.module.css`)

| Bucket | Estimate |
|---|---:|
| AGENTS.md + prompt + tokens.css + 2 Button files | ~2.7K |
| Figma MCP: 1 call for component set 16:61 | ~1–2K |
| `git diff --cached` output | ~0.3K |
| Tool-call framing across ~6–10 turns | ~3–5K |
| HTML report output (15.2KB) | ~3.8K |
| No code edits / Figma comments / commit | 0 |
| **Total prompt (input) tokens** | **~7–11K** |
| **Total completion (output) tokens** | **~4–6K** |
| **Combined ballpark** | **~11–17K tokens** |

## Takeaway

The staged variant is roughly **4× cheaper** in tokens, driven by three
things:

1. **One Figma call** vs ~7 — biggest single saving.
2. **Two source files read** vs ~13.
3. **Half-sized report** and **no write-side actions** (no per-mismatch
   TODO inserts, no Figma POSTs, no git plumbing turns).

Caveat: these are estimates. A truer number would need either Copilot
usage telemetry or running each flow with a token-counting wrapper.
