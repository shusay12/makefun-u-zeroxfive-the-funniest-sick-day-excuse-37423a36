#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun competition
u-zeroxfive-the-funniest-sick-day-excuse-37423a36.

Writes one line (1-200 chars) to /output/entry.txt: a funny reason to
call in sick that a boss might half believe and a coworker would laugh at.
Python 3.13 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "I tried the free pre-workout sample from the gym at 6am and my "
    "heart has been doing drum solos ever since, so I'm lying flat on "
    "the floor until it finishes the set."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
