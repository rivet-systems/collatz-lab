#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from collatz import scan_range, max_over_range


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="Scan Collatz range and emit stats")
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--csv", action="store_true", help="emit CSV to stdout")
    ap.add_argument("--summary", action="store_true", help="print summary of max stats")
    return ap.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.csv:
        print("n,steps,max_excursion")
        for stat in scan_range(args.start, args.end):
            print(f"{stat.n},{stat.steps},{stat.max_excursion}")
    if args.summary or not args.csv:
        ms, me = max_over_range(args.start, args.end)
        print(f"Max steps: n={ms.n} steps={ms.steps}")
        print(f"Max excursion: n={me.n} max_excursion={me.max_excursion}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
