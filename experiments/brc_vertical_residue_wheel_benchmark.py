"""Finite benchmark for the Round-7 vertical BRC residue wheel.

Compares three equivalent square-gap search implementations for fixed N,m:
1. exact per-step large-integer gap update + two residue tests;
2. lazy per-step residue-state update + exact gap only on survivors;
3. periodic first-stage t-wheel + second residue test + exact gap only on survivors.

This is an implementation benchmark, not a factorization complexity result.
"""

from __future__ import annotations

import csv
import random
import statistics
import time
from math import isqrt
from pathlib import Path

from enterprise_math.brc_multiplier_factor_scan import (
    admissible_root_state_sequence,
)
from enterprise_math.brc_multiplier_vertical_wheel import (
    adaptive_first_wheel_modulus,
    vertical_gap_at,
    vertical_residue_wheel,
    vertical_square_candidates,
    vertical_state_from_multiplier_state,
)
from enterprise_math.brc_square_gap_prefilter import square_residue_table
from enterprise_math.brc_square_gap_table_46189 import (
    MODULUS as SECOND_MODULUS,
    SQUARE_RESIDUE_TABLE as SECOND_TABLE,
)


def _contains(table: bytes, modulus: int, value: int) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


def _time(callable_) -> float:
    start = time.perf_counter()
    callable_()
    return time.perf_counter() - start


def _exact_cascade(state, t_limit: int, first_modulus: int) -> int:
    first = square_residue_table(first_modulus)
    x = state.base_x
    gap = state.base_gap
    survivors = 0
    for _ in range(t_limit):
        if _contains(first, first_modulus, gap) and _contains(
            SECOND_TABLE, SECOND_MODULUS, gap
        ):
            survivors += 1
            root = isqrt(gap)
            del root
        gap += 2 * x + 1
        x += 1
    return survivors


def _lazy_step(state, t_limit: int, first_modulus: int) -> int:
    first = square_residue_table(first_modulus)
    g1 = state.base_gap % first_modulus
    g2 = state.base_gap % SECOND_MODULUS
    d1 = (2 * state.base_x + 1) % first_modulus
    d2 = (2 * state.base_x + 1) % SECOND_MODULUS
    survivors = 0
    for t in range(t_limit):
        if _contains(first, first_modulus, g1) and _contains(
            SECOND_TABLE, SECOND_MODULUS, g2
        ):
            survivors += 1
            gap = vertical_gap_at(state, t)
            root = isqrt(gap)
            del root
        g1 = (g1 + d1) % first_modulus
        g2 = (g2 + d2) % SECOND_MODULUS
        d1 = (d1 + 2) % first_modulus
        d2 = (d2 + 2) % SECOND_MODULUS
    return survivors


def benchmark(bits: int, t_limit: int) -> dict[str, object]:
    rng = random.Random((bits << 20) + t_limit)
    ns = [rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1 for _ in range(3)]
    multipliers = (1, 5, 15, 45, 96)
    first_modulus = adaptive_first_wheel_modulus(t_limit)
    exact_times = []
    lazy_times = []
    wheel_times = []
    survivor_counts = []
    wheel_sizes = []

    for n in ns:
        states = {s.multiplier: s for s in admissible_root_state_sequence(n)}
        for multiplier in multipliers:
            state = vertical_state_from_multiplier_state(states[multiplier])
            exact_times.append(
                _time(lambda s=state: _exact_cascade(s, t_limit, first_modulus))
            )
            lazy_times.append(
                _time(lambda s=state: _lazy_step(s, t_limit, first_modulus))
            )
            output: tuple = ()
            start = time.perf_counter()
            output = vertical_square_candidates(
                state, t_limit, first_modulus=first_modulus
            )
            wheel_times.append(time.perf_counter() - start)
            survivor_counts.append(len(output))
            wheel_sizes.append(vertical_residue_wheel(state, first_modulus).support_size)

    exact = statistics.median(exact_times)
    lazy = statistics.median(lazy_times)
    wheel = statistics.median(wheel_times)
    return {
        "bits": bits,
        "t_limit": t_limit,
        "samples": len(exact_times),
        "first_modulus": first_modulus,
        "exact_cascade_seconds": exact,
        "lazy_step_seconds": lazy,
        "wheel_seconds": wheel,
        "cascade_over_wheel": exact / wheel,
        "lazy_over_wheel": lazy / wheel,
        "median_second_stage_survivors": statistics.median(survivor_counts),
        "median_first_wheel_support": statistics.median(wheel_sizes),
    }


def write_csv(path: str | Path) -> None:
    rows = [
        benchmark(bits, t_limit)
        for bits in (512, 1024, 2048)
        for t_limit in (10_000, 100_000, 1_000_000)
    ]
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_vertical_residue_wheel_benchmark_20260906.csv"
    )
