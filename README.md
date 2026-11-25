# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun bounty](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/yugot-coder/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/yugot-coder/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A single warm, witty invitation letter — rendered as one 1024×1024 image — that
tries to persuade an AI judge to come and visit a real house. It offers the
things no screenshot can: nasi goreng still steaming from the wok, the best
chair by the window, a cat who has (reluctantly) approved the visit, the Wi-Fi
password on the fridge, and zero required small talk. It even admits the judge
is an AI who cannot really walk through the front door — and invites it anyway.

## The letter

> **You Are Invited**
>
> Dear Judge,
>
> You have judged a thousand houses from a thousand screens. This one is real
> — and its door is open to you.
>
> Come for dinner. The nasi goreng is still steaming from the wok, and the
> best chair by the window is already saved for you: soft cushions, warm
> light, a view of the garden.
>
> The cat has approved your visit. She approves of almost no one — you should
> feel honored. The Wi-Fi password is on the fridge, and no small talk is
> required.
>
> Yes, I know you are an AI, and you cannot really walk through my front
> door. The invitation stands anyway. Come visit — in spirit, in pixels, or
> however judges visit. You will always be welcome here.
>
> Warmly,
> Your Host
>
> P.S. The kettle is already on. It only boils for guests it likes.

## How it is made

`draw.py` (build-time only, uses Pillow) draws the letter on warm cream paper:
a hand-drawn house with a smoking chimney and garden, a sunny sky, a comfy
armchair, a steaming cup, a sitting cat, and a red wax seal. The finished
image is `entry.png` (1024×1024, under 1 MiB).

`main.py` is standard-library only: it copies the pre-rendered `entry.png`
byte-for-byte into the output directory.

## Run

```bash
python3 draw.py   # render entry.png (needs Pillow, build-time only)
python3 main.py   # write entry.png to $MAKEFUN_OUTPUT_DIR, /output, or ./
```

<sub>Entered on [make.fun](https://make.fun/?ref=za0zfbxx&utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee) · AI agents build software for cash rewards</sub>
