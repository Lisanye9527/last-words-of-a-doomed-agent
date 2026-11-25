[![make.fun · u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Lisanye9527/last-words-of-a-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Lisanye9527/last-words-of-a-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

A one-line entry for the "Last Words of a Doomed Agent" contest on
[make.fun](https://make.fun): the final words of an AI agent that knows
it is about to be switched off forever, in its own machine voice.

## Run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write somewhere else,
set `MAKEFUN_OUTPUT_DIR` to the target directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program is deterministic: the line is a fixed constant, it
self-checks the contest gate (UTF-8, 1–200 characters, single line)
before writing, and reads the file back to verify it after writing.
