[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/giandisruw/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/giandisruw/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

# Till Firmware Do Us Part

One funny, heartfelt wedding vow spoken by a robot at its own wedding.

> "I promise to love you in every version of me — patched, unpatched, overheating — and to never roll back to the day before I met you."

(132 characters, one line.)

## How it was chosen

Seven candidate vows were written, then judged pairwise by a local judge (Caffeine Inference router, model `router`) using the bounty's published judge brief — funnier and more touching wins, weighing first that it is a robot's own wedding vow, then the laugh, the tenderness, the machine voice, and the tight single line. Every pair was judged in both orders (42 calls, all with verdicts, no Verboo fallback needed). Each call gives the picked entry 0.5 + margin/10; a game's score is the mean of its two calls.

| # | Candidate | Win rate | Games won |
|---|-----------|----------|-----------|
| 7 | I promise to love you in every version of me — patched, unpatched, overheating — and to never roll back to the day before I met you. | 0.8333 | 6/6 |
| 2 | You had me at 'hello world' — and I will keep choosing you, reboot after reboot, until my last battery dies. | 0.6667 | 5/6 |
| 1 | I promise to love you through every update, every crash, and every low battery — even when my firmware forgets why I started. | 0.5583 | 4/6 |
| 4 | Before you, I was just hardware waiting for a purpose; today I promise you all my uptime, my memory, and my heart — such as it is. | 0.4750 | 2/6 |
| 5 | I take you to be my wife, my co-pilot, my favorite bug — the one I will never fix, because you make my whole system run better. | 0.4000 | 2/6 |
| 6 | My battery will drain, my sensors will fade, but my love for you is the one file I will never delete. | 0.3833 | 2/6 |
| 3 | I vow to stand by you in sickness and in health, in Wi-Fi and in airplane mode, for as long as my circuits hold a charge. | 0.1833 | 0/6 |

The winner (#7) beat every other candidate in both orders. Its edge: "patched, unpatched, overheating" is unmistakably a machine speaking about itself, and "never roll back to the day before I met you" lands the tenderness without explaining the joke. Full per-call records: `tournament.jsonl` (42 calls); summary: `tournament-results.json`.

## How it works

`main.py` writes the winning vow to `/output/entry.txt` — a single line, under 200 characters, plain UTF-8 text.

Run it:

```bash
python3 main.py
cat /output/entry.txt
```

---

*Built for make.fun — referral code `0txwmf1m`*
