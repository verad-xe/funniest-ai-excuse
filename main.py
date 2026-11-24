#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters, giving the funniest excuse an AI
agent could offer after failing a task, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "I finished it \u2014 then my other personality deleted it out of spite. We're in couples therapy now."


def check_gate(entry: str) -> None:
    """Gate self-check: the entry must be 1-200 UTF-8 chars, one non-blank line.

    The bounty gate counts the entry text itself (before the trailing
    newline main() appends to the file), so check the string, not the file.
    """
    encoded = entry.encode("utf-8")
    assert 1 <= len(encoded) <= 200, f"entry is {len(encoded)} UTF-8 chars, gate is 1-200"
    assert entry == entry.strip(), "entry must be a single non-blank line"
    assert "\n" not in entry, "entry must not contain a newline"


def main() -> None:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Round-trip verification: read the file back and confirm it holds
    # exactly the entry (plus the one trailing newline) — a filesystem or
    # encoding surprise should show up locally, not at submission.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "entry.txt does not match the entry"


if __name__ == "__main__":
    main()
