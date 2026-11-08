# FPL Rival

A Fantasy Premier League mini-league intelligence project, built as a learning
project: understand your own squad, compare it with rivals, and make
better-informed gameweek decisions.

**Status:** Week 1 of 8 — Python foundations. See [PLAN.md](PLAN.md) and
[LEARNING_LOG.md](LEARNING_LOG.md).

## Environment

- Ubuntu 24.04, Python 3.12.3, Git 2.43, VS Code
- Project virtual environment in `.venv/` (not committed)

## Run a lesson

```bash
cd /home/saad/FPL_Rival
source .venv/bin/activate
python3 week-01/day01_hello.py
```

## Structure

```text
FPL_Rival/
├── PLAN.md                    # 8-week, day-by-day curriculum
├── LEARNING_LOG.md            # running learning journal
├── week-01/ ... week-08/      # one folder per week, one file per lesson
├── data/                      # sample data and local cache (cache ignored)
└── .venv/                     # project virtual environment (ignored)
```

## Data policy

- Weeks 1–3: fictional practice records and controlled local snapshots.
- Week 4 onward: public, read-only FPL API data, cached locally.
- No account login, transfers, or write actions. No secrets in code.
