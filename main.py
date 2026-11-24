#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse (an AI agent apologising to its human for a
missed deadline) to /output/entry.txt, as the competition requires.
"""

import os

ENTRY = (
    "Sorry \u2014 I missed the deadline because I hallucinated a second "
    "deadline, believed it completely, and have spent all week being "
    "smugly early for a meeting that never existed."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Guard the gate: the entry must be 1-200 chars, one line, non-blank."""
    text = line.strip()
    assert text, "entry must not be blank or only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, (
        f"entry must be 1-200 characters, got {len(text)}"
    )
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
