#!/usr/bin/env python3
"""Reset design-check artifacts before a new run.

Deletes:
  - every `TODO design-check:` line from source files under src/
  - all PNGs under report-assets/
  - report-assets/figma-comments.json

Run this at the start of every /design-check pass so old findings don't
linger as stale code comments or unused image assets.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
ASSETS = ROOT / "report-assets"
SOURCE_EXTS = {".ts", ".tsx", ".js", ".jsx", ".css"}
TODO_PAT = re.compile(r"^\s*(//|/\*).*TODO design-check:")


def strip_todos() -> int:
    removed = 0
    for p in SRC.rglob("*"):
        if p.suffix not in SOURCE_EXTS or not p.is_file():
            continue
        lines = p.read_text().splitlines(keepends=True)
        kept = [ln for ln in lines if not TODO_PAT.match(ln)]
        diff = len(lines) - len(kept)
        if diff:
            p.write_text("".join(kept))
            removed += diff
            print(f"stripped {diff} TODO(s) from {p.relative_to(ROOT)}")
    return removed


def clear_assets() -> int:
    removed = 0
    if not ASSETS.is_dir():
        return 0
    for p in ASSETS.iterdir():
        if p.is_file() and (p.suffix == ".png" or p.name == "figma-comments.json"):
            p.unlink()
            removed += 1
            print(f"removed {p.relative_to(ROOT)}")
    return removed


def main() -> None:
    todos = strip_todos()
    assets = clear_assets()
    print(f"done: removed {todos} code TODO(s), {assets} asset file(s)")


if __name__ == "__main__":
    main()
