# Collatz Lab

A minimal, testable toolkit to explore Collatz trajectories.

## What’s here
- `collatz.py` — core functions for stopping time, max excursion, and running ranges.
- `scripts/run_range.py` — CLI to scan ranges and emit stats (CSV to stdout).
- Tests + CI (pytest, ruff).

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest
python scripts/run_range.py --start 1 --end 100000 --csv
```

## Contributing
- Add reproducible scripts, new stats, or search heuristics.
- Include ranges checked and metrics (stopping time, max excursion, anomalies).
- Tests required. Lint (ruff) required. CI runs pytest+ruff.

Actions > words: bring code + data.
