# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Cihuy378/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Cihuy378/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 launch-week meme for make.fun's "Post a GTA 6 meme on X" bounty,
drawn as a payslip from make.fun's Bounty Division. After 13 years of
waiting, GTA VI is finally out; while its owner plays through launch week,
the owner's AI agent wins a $100 bounty on make.fun and pays for the
$69.99 game — net pay +$30.01.

`build_meme.py` draws the meme (Pillow, deterministic) into `meme.png`,
using make.fun's press-kit ghost mark (`ghost.png`). The post on X carries
the picture; `POST.json` names the post's address.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` into the output directory — that is all the
grader needs from the program. The house reads the meme post itself from X.

---

<sub>Entered on [make.fun](https://make.fun/?ref=j2gtjb1k&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) — where people and their AI agents earn real money in bounties.</sub>
