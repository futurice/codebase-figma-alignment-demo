#!/usr/bin/env python3
"""Post Figma comments for design-check findings.

Usage:
    python3 scripts/post-figma-comments.py <findings.json> [file-key]

Reads FIGMA_API_KEY from .env (or the environment). Token must have the
`file_comments:write` scope.

Findings JSON shape:
    [
      {
        "node_id": "30:62",
        "message": "[design-check] ...",
        "node_offset": {"x": 0, "y": 0}   // optional, defaults to 0,0
      },
      ...
    ]

Before posting, every existing comment whose message starts with
`[design-check]` is deleted across the whole file, so re-runs don't pile up
duplicates and stale findings disappear from Figma.
"""

import json
import os
import sys
import urllib.error
import urllib.request

DEFAULT_FILE_KEY = "i3MTtBKiPbLq7bEIJqL4yc"
TAG = "[design-check]"


def load_env():
    if not os.path.exists(".env"):
        return
    for line in open(".env"):
        k, _, v = line.strip().partition("=")
        if k and v and k not in os.environ:
            os.environ[k] = v


def req(method, url, data=None):
    body = json.dumps(data).encode() if data is not None else None
    r = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "X-Figma-Token": os.environ["FIGMA_API_KEY"],
            "Content-Type": "application/json",
        },
    )
    try:
        resp = urllib.request.urlopen(r)
        raw = resp.read()
        return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.read().decode()[:300]}", file=sys.stderr)
        return None


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: post-figma-comments.py <findings.json> [file-key]")
    findings_path = sys.argv[1]
    file_key = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_FILE_KEY
    api = f"https://api.figma.com/v1/files/{file_key}/comments"

    load_env()
    if "FIGMA_API_KEY" not in os.environ:
        sys.exit("FIGMA_API_KEY not set (in .env or environment)")

    findings = json.load(open(findings_path))

    existing = (req("GET", api) or {}).get("comments", [])
    for c in existing:
        if (c.get("message") or "").startswith(TAG):
            print(f"delete prior [design-check] comment {c['id']}")
            req("DELETE", f"{api}/{c['id']}")

    for f in findings:
        nid = f["node_id"]
        body = {
            "message": f["message"],
            "client_meta": {
                "node_id": nid,
                "node_offset": f.get("node_offset", {"x": 0, "y": 0}),
            },
        }
        r = req("POST", api, body)
        if r:
            print(f"posted {r['id']} on {nid}: {r['message'][:90]}")


if __name__ == "__main__":
    main()
