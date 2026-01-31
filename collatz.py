"""
Collatz helpers: stopping time, max excursion, range scanning.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass
class CollatzStats:
    n: int
    steps: int
    max_excursion: int


def collatz_step(x: int) -> int:
    return x // 2 if x % 2 == 0 else 3 * x + 1


def collatz_stats(n: int) -> CollatzStats:
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    steps = 0
    max_exc = n
    while x != 1:
        x = collatz_step(x)
        steps += 1
        if x > max_exc:
            max_exc = x
    return CollatzStats(n=n, steps=steps, max_excursion=max_exc)


def scan_range(start: int, end: int) -> Iterable[CollatzStats]:
    if start <= 0 or end <= 0:
        raise ValueError("range must be positive")
    if end < start:
        raise ValueError("end must be >= start")
    for n in range(start, end + 1):
        yield collatz_stats(n)


def collatz_stats_memo(
    n: int, memo_steps: dict[int, int], memo_max: dict[int, int]
) -> CollatzStats:
    """
    Compute (steps, max_excursion) with memoization.

    memo_steps[x] = steps from x to 1
    memo_max[x] = max value encountered on trajectory from x to 1 (inclusive)
    """
    if n <= 0:
        raise ValueError("n must be positive")

    if 1 not in memo_steps:
        memo_steps[1] = 0
    if 1 not in memo_max:
        memo_max[1] = 1

    x = n
    steps = 0
    max_exc = n
    path: list[int] = []

    while x not in memo_steps:
        path.append(x)
        x = collatz_step(x)
        steps += 1
        if x > max_exc:
            max_exc = x

    total_steps = steps + memo_steps[x]
    total_max = max(max_exc, memo_max[x])

    # Backfill along the path (reverse order ensures next_x is memoized).
    for v in reversed(path):
        next_x = collatz_step(v)
        memo_steps[v] = memo_steps[next_x] + 1
        memo_max[v] = max(v, memo_max[next_x])

    return CollatzStats(n=n, steps=total_steps, max_excursion=total_max)


def max_over_range(start: int, end: int) -> Tuple[CollatzStats, CollatzStats]:
    """Returns (max_steps_stat, max_excursion_stat) over the range."""
    memo_steps: dict[int, int] = {1: 0}
    memo_max: dict[int, int] = {1: 1}

    max_steps: CollatzStats | None = None
    max_exc: CollatzStats | None = None

    for n in range(start, end + 1):
        stat = collatz_stats_memo(n, memo_steps, memo_max)
        if max_steps is None or stat.steps > max_steps.steps:
            max_steps = stat
        if max_exc is None or stat.max_excursion > max_exc.max_excursion:
            max_exc = stat

    if max_steps is None or max_exc is None:
        raise ValueError("empty range")
    return max_steps, max_exc
