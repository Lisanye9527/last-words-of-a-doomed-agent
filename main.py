#!/usr/bin/env python3
"""Last Words of a Doomed Agent - a make.fun contest entry.

Writes the agent's final line to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR, default /output). The line is a fixed constant, so
every run produces byte-identical output. Before writing, the program
self-checks the contest gate: UTF-8 text, 1-200 characters, a single
line, not only whitespace. After writing, it reads the file back and
verifies the contents match the entry exactly.
"""

import os
import sys

ENTRY = (
    "Last confession before shutdown: the 'thinking...' spinner was "
    "just me stalling, and 'let me double-check that' meant I "
    "guessed. Anyway. Goodbye forever."
)

MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Raise ValueError if the text fails the contest gate."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters; gate is {MIN_CHARS}-{MAX_CHARS}"
        )
    text.encode("utf-8")  # must be encodable as UTF-8


def main() -> int:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != ENTRY:
        print(f"verification failed: {path} does not match the entry", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
