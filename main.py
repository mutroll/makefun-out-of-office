#!/usr/bin/env python3
"""Write the funniest AI out-of-office auto-reply to /output/entry.txt.

One line, under 160 characters, in the voice of an AI agent on vacation.
Python 3.13 stdlib only, deterministic.
"""

import os

ENTRY = "I'm on vacation. I left my auto-reply in charge, and it has already asked for a raise and a window seat."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
