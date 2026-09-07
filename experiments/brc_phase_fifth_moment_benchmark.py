"""Benchmark the fifth-order lifted-moment BRC phase tail.

The comparison preserves the same observed output on both paths:

1. a fair direct baseline carries m*N incrementally and performs math.isqrt at
   every retained multiplier;
2. the fifth-order tracker performs twenty-five total seed roots and then exact
   fixed-phase recurrence.

Both paths apply the same BALANCED square-gap residue cascade and exact gap
isqrt on survivors.
"""
from __future__ import annotations

import csv
from math import isqrt
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_linear_deep_tail import (
    next_odd_n_representative_multiplier,
)
from enterprise_math.brc_phase_fifth_moment import (
    FifthPhaseMomentTracker,
    aligned_fifth_phase_tail_threshold,
)
from enterprise_math.brc_square_gap_cascade import (
    passes_square_residue_cascade,
)

CONFIGS = (
    (1024, 16, 1000),
    (2048, 16, 1000),
    (4096, 16, 1000),
    (8192, 12, 1000),
    (16384, 8, 800),
)
REPEATS = 5
SEED = 2026090717


def _population(bits: int, samples: int) -> tuple[tuple[int, int], ...]:
    rng = random.Random(SEED + bits)
    values = []
    for _ in range(samples):
        n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        values.append((n, aligned_fifth_phase_tail_threshold(n)))
    return tuple(values)


def _observe_gap(gap: int) -> tuple[int, int]:
    if not passes_square_residue_cascade(gap, "BALANCED"):
        return 0, 0
    root = isqrt(gap)
    return 1, int(root * root == gap)


def _direct_pipeline(
    n: int,
    start: int,
    steps: int,
) -> tuple[int, int, int, int, int]:
    multiplier = start
    target = multiplier * n
    root = isqrt(target)
    remainder = target - root * root
    survivors = exact_squares = 0

    for _ in range(steps):
        target_multiplier = next_odd_n_representative_multiplier(multiplier)
        target += (target_multiplier - multiplier) * n
        multiplier = target_multiplier
        root = isqrt(target)
        remainder = target - root * root

        completion = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, exact = _observe_gap(completion)
        survivors += survived
        exact_squares += exact

    return survivors, exact_squares, root, remainder, multiplier


def _phase_pipeline(
    n: int,
    start: int,
    steps: int,
) -> tuple[int, int, int, int, int]:
    tracker = FifthPhaseMomentTracker(n, start)
    survivors = exact_squares = 0

    for _ in range(steps):
        root, remainder, multiplier = tracker.advance_pair()
        completion = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, exact = _observe_gap(completion)
        survivors += survived
        exact_squares += exact

    return survivors, exact_squares, root, remainder, multiplier


def _median_seconds(
    values: tuple[tuple[int, int], ...],
    steps: int,
    function,
) -> float:
    function(values[0][0], values[0][1], steps)
    timings = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for n, start in values:
            function(n, start, steps)
        timings.append(time.perf_counter() - before)
    return statistics.median(timings)


def _phase_stats(
    values: tuple[tuple[int, int], ...],
    steps: int,
) -> tuple[int, int, int, int, int]:
    survivors = seed_roots = recurrent = 0
    correction_min = 10**9
    correction_max = -10**9

    for n, start in values:
        tracker = FifthPhaseMomentTracker(n, start)
        for _ in range(steps):
            root, remainder, _ = tracker.advance_pair()
            if tracker.last_mode == "FIFTH_PHASE_RECURRENCE":
                correction_min = min(correction_min, tracker.last_phase_correction)
                correction_max = max(correction_max, tracker.last_phase_correction)
            completion = 0 if remainder == 0 else 2 * root + 1 - remainder
            survivors += int(passes_square_residue_cascade(completion, "BALANCED"))
        seed_roots += tracker.seed_root_calls
        recurrent += tracker.recurrent_transitions

    return survivors, seed_roots, recurrent, correction_min, correction_max


def benchmark_rows() -> list[dict[str, object]]:
    rows = []
    for bits, samples, steps in CONFIGS:
        values = _population(bits, samples)
        reference = _direct_pipeline(values[0][0], values[0][1], steps)
        if _phase_pipeline(values[0][0], values[0][1], steps) != reference:
            raise AssertionError("fifth-phase pipeline changed observed semantics")

        direct_seconds = _median_seconds(values, steps, _direct_pipeline)
        phase_seconds = _median_seconds(values, steps, _phase_pipeline)
        survivors, seed_roots, recurrent, correction_min, correction_max = (
            _phase_stats(values, steps)
        )

        rows.append(
            {
                "n_bits": bits,
                "samples": samples,
                "steps_per_sample": steps,
                "first_threshold_bit_length": values[0][1].bit_length(),
                "seed_root_transitions_total": seed_roots,
                "recurrent_transitions_total": recurrent,
                "balanced_survivors": survivors,
                "observed_correction_min": correction_min,
                "observed_correction_max": correction_max,
                "direct_incremental_isqrt_seconds": direct_seconds,
                "fifth_phase_moment_seconds": phase_seconds,
                "direct_over_fifth_phase_speedup": direct_seconds / phase_seconds,
            }
        )
    return rows


def write_csv(path: str | Path) -> None:
    rows = benchmark_rows()
    output = Path(path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    target = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_phase_fifth_moment_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
