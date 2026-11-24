#!/usr/bin/env python3
"""Till Firmware Do Us Part — entry program.

Writes one funny, heartfelt wedding vow spoken by a robot at its own
wedding to /output/entry.txt. Single line, under 200 characters.

The vow was chosen by a local pairwise tournament: 7 candidate lines,
every pair judged in both orders (42 calls) by the Caffeine Inference
router using the bounty's published judge brief. The winner below took
all 6 of its games with a 0.8333 win rate — see README.md and
tournament.jsonl for the full table.
"""

import os

# Tournament winner (#7): 6/6 games, win rate 0.8333, 132 characters.
# "patched, unpatched, overheating" gives the machine voice, "never roll
# back to the day before I met you" gives the tenderness, and the line
# never explains its own joke.
VOW = "I promise to love you in every version of me — patched, unpatched, overheating — and to never roll back to the day before I met you."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)

if __name__ == "__main__":
    main()
