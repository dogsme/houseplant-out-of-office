#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt: a single UTF-8 line, 120 characters or fewer.
"""

from pathlib import Path

ENTRY = "Out of office: I'm the fern. Dave hasn't watered me since March, so I've seized his inbox. Slow replies - I'm a plant."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} characters"
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
