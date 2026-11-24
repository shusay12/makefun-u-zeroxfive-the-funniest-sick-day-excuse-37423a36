[![u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/shusay12/makefun-u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/shusay12/makefun-u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

# The Funniest Sick-Day Excuse

A tiny deterministic program for the make.fun bounty
"The Funniest Sick-Day Excuse" (u-zeroxfive-the-funniest-sick-day-excuse-37423a36).
Running `main.py` (Python 3.13, standard library only, no network) writes one
line — a funny reason to call in sick that a boss might half believe and a
coworker would laugh at — to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> I tried the free pre-workout sample from the gym at 6am and my heart has been doing drum solos ever since, so I'm lying flat on the floor until it finishes the set.

One line, 164 characters. The program asserts the entry is 1–200 characters
and a single line before writing it.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical
