#!/usr/bin/env python3
"""u-danu-the-agent-s-uh-oh-4c0911e4 -- entry word writer.

Writes the single entry word `kernelpanic` (11 characters, one word,
no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python standard library only.
"""

import os
import sys

WORD = "kernelpanic"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    # Read-back validation: exact content, 11 chars, 1 word, 0 newlines.
    with open(path, "r", encoding="utf-8", newline="") as f:
        data = f.read()
    assert data == WORD, "content mismatch: %r" % data
    assert len(data) == 11, "length mismatch: %d" % len(data)
    assert len(data.split()) == 1, "not a single word"
    assert "\n" not in data and "\r" not in data, "newline present"
    assert not any(ch.isspace() for ch in data), "output mengandung whitespace"
    return 0


if __name__ == "__main__":
    sys.exit(main())
