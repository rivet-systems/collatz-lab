import pytest
from collatz import collatz_stats, max_over_range


def test_basic_values():
    assert collatz_stats(1).steps == 0
    assert collatz_stats(2).steps == 1
    assert collatz_stats(3).steps == 7  # known stopping time
    assert collatz_stats(6).steps == 8


def test_max_over_range_small():
    ms, me = max_over_range(1, 10)
    assert ms.n == 9  # 9 has 19 steps in 1..10
    assert ms.steps == 19
    assert me.n == 9 or me.n == 7  # 9 has excursion 52, 7 has 16


def test_invalid():
    with pytest.raises(ValueError):
        collatz_stats(0)
    with pytest.raises(ValueError):
        list(max_over_range(-1, 10))
