#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes the winning one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt by default).
"""

import os
import sys

ENTRY = "I checked: neither of us pressed a floor. We're just two robots riding nowhere, too polite to say it."


def main() -> int:
    line = ENTRY
    if not 1 <= len(line) <= 200:
        print(f"entry must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        data = line.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"wrote {path} ({len(line)} chars, {len(data)} bytes UTF-8)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
