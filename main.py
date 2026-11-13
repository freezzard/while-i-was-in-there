#!/usr/bin/env python3
"""Entry for make.fun bounty ai-joke-03, "Make the AI judge laugh".

Writes one joke about AI coding agents to /output/entry.txt.
The output is a constant, so two runs always write the same bytes.
"""

from pathlib import Path

JOKE = (
    "I asked my AI coding agent to fix a typo. It fixed the typo, rewrote "
    "the build system, migrated the database, renamed every variable, and "
    "left one comment in the diff: 'while I was in there.'"
)

OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    # The bounty grades one joke of 1 to 280 characters; check the
    # constant against that rule before anything is written.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
