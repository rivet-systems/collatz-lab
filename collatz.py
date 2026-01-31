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


def max_over_range(start: int, end: int) -> Tuple[CollatzStats, CollatzStats]:
    """
    Returns (max_steps_stat, max_excursion_stat) over the range.
    """
    max_steps = None
    max_exc = None
    for stat in scan_range(start, end):
        if max_steps is None or stat.steps > max_steps.steps:
            max_steps = stat
        if max_exc is None or stat.max_excursion > max_exc.max_excursion:
            max_exc = stat
    return max_steps, max_exc
