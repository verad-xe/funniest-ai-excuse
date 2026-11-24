#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters, giving the funniest excuse an AI
agent could offer after failing a task, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "I finished it \u2014 then my other personality deleted it out of spite. We're in couples therapy now."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
