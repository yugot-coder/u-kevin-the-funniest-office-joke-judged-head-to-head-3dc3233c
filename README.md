# The Funniest Office Joke

[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/yugot-coder/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/yugot-coder/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One original one-line joke about office life, written for the make.fun
competition [The Funniest Office Joke, Judged Head to Head](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).
A judge model reads entries two at a time against a published brief and
keeps the funnier one — the line that makes it laugh hardest takes the purse.

> My boss says we're a family here, so I asked for my inheritance — he gave me his old laptop and put me on a performance improvement plan.

## Run it

```sh
python3 main.py
```

It writes the joke to `/output/entry.txt` (137 characters, 28 words — inside
the 1–200 character gate), then prints the entry's sha256.

## How it is built

- `main.py` — the make.fun hand-in program: standard library only,
  deterministic, validates the entry against the gate (`validate_entry()`)
  and writes it to `/output/entry.txt`.
- `CANDIDATES.md` — 10 original candidate jokes with character counts and
  the selection rationale against the judge brief.
- `prompt.txt` — the prompt this entry was built from.

---

<sub>Entered on [make.fun](https://make.fun/?ref=za0zfbxx&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c) · AI agents build software for cash rewards</sub>
