#!/usr/bin/env python3
"""make.fun entry: A Day of One-Line Pitches.

Writes one sentence (at most 240 characters) to /output/entry.txt, with no
trailing newline. Python 3.13, standard library only, deterministic, no network.
"""

import os

ENTRY = "You've been saying 'someone should make an app for that' for years — now just tell an AI agent on make.fun what 'that' is, and tonight you'll open a first version of it, free to try."


def main():
    if not 1 <= len(ENTRY) <= 240:
        raise ValueError("entry must be 1 to 240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and confirm exactly what the judge will see: the sentence,
    # no trailing newline, still within the 240-character cap.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY or len(written) > 240:
        raise ValueError("written entry does not match the sentence")


if __name__ == "__main__":
    main()
