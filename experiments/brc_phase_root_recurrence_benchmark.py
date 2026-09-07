"""Benchmark fixed-phase third-difference BRC root transport.

Three equal-semantics deep-tail pipelines are compared:

1. direct order-one quotient at every retained multiplier;
2. Round-13 quotient/remainder phase tracker;
3. Round-14 fixed-phase root/remainder third-difference tracker.

All three use the same BALANCED square-gap residue cascade and exact gap isqrt
on survivors.  The direct baseline incrementally transports the exact BRC state;
it does not recompute m*N from scratch.
"""
from __future__ import annotations

import csv
from math import isqrt
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_threshold,
    next_odd_n_representative_multiplier,
    odd_n_multiplier_is_representative,
)
from enterprise_math.brc_phase_quotient_remainder import (
    PhaseQuotientRemainderTracker,
)
from enterprise_math.brc_phase_root_recurrence import (
    PhaseRootRemainderTracker,
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
SEED = 2026090712


def _align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def _population(bits: int, samples: int) -> tuple[tuple[int, int], ...]:
    rng = random.Random(SEED + bits)
    values = []
    for _ in range(samples):
        n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        start = _align_representative(common_mod8_linear_tail_threshold(n))
        values.append((n, start))
    return tuple(values)


def _check_gap(gap: int) -> tuple[int, int]:
    if not passes_square_residue_cascade(gap, "BALANCED"):
        return 0, 0
    root = isqrt(gap)
    return 1, int(root * root == gap)


def _direct_order1(n: int, start: int, steps: int) -> tuple[int, int, int, int, int]:
    multiplier = start
    target = multiplier * n
    root = isqrt(target)
    remainder = target - root * root
    survivors = exact_squares = 0

    for _ in range(steps):
        target_multiplier = next_odd_n_representative_multiplier(multiplier)
        h = target_multiplier - multiplier
        quotient = (2 * h * root) // (4 * multiplier + h)
        candidate = root + quotient
        gap_state = remainder + h * n - quotient * (2 * root + quotient)
        while gap_state >= 2 * candidate + 1:
            gap_state -= 2 * candidate + 1
            candidate += 1

        multiplier = target_multiplier
        root = candidate
        remainder = gap_state
        completion = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, exact = _check_gap(completion)
        survivors += survived
        exact_squares += exact

    return survivors, exact_squares, root, remainder, multiplier


def _phase_quotient(n: int, start: int, steps: int) -> tuple[int, int, int, int, int]:
    multiplier = start
    target = multiplier * n
    root = isqrt(target)
    remainder = target - root * root
    tracker = PhaseQuotientRemainderTracker(n)
    survivors = exact_squares = 0

    for _ in range(steps):
        target_multiplier = next_odd_n_representative_multiplier(multiplier)
        h = target_multiplier - multiplier
        quotient, _ = tracker.divide_pair(root, multiplier, h)
        candidate = root + quotient
        gap_state = remainder + h * n - quotient * (2 * root + quotient)
        while gap_state >= 2 * candidate + 1:
            gap_state -= 2 * candidate + 1
            candidate += 1

        multiplier = target_multiplier
        root = candidate
        remainder = gap_state
        completion = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, exact = _check_gap(completion)
        survivors += survived
        exact_squares += exact

    return survivors, exact_squares, root, remainder, multiplier


def _phase_root(n: int, start: int, steps: int) -> tuple[int, int, int, int, int]:
    tracker = PhaseRootRemainderTracker(n, start)
    survivors = exact_squares = 0

    for _ in range(steps):
        root, remainder, multiplier = tracker.advance_pair()
        completion = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, exact = _check_gap(completion)
        survivors += survived
        exact_squares += exact

    return survivors, exact_squares, root, remainder, multiplier


def _median_seconds(values: tuple[tuple[int, int], ...], steps: int, fn) -> float:
    fn(values[0][0], values[0][1], steps)
    timings = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for n, start in values:
            fn(n, start, steps)
        timings.append(time.perf_counter() - before)
    return statistics.median(timings)


def _phase_stats(
    values: tuple[tuple[int, int], ...],
    steps: int,
) -> tuple[int, int, int, int, int]:
    survivors = seeds = recurrent = 0
    correction_min = 10**9
    correction_max = -10**9
    for n, start in values:
        tracker = PhaseRootRemainderTracker(n, start)
        for _ in range(steps):
            root, remainder, _ = tracker.advance_pair()
            if tracker.last_mode == "PHASE_RECURRENCE":
                correction_min = min(correction_min, tracker.last_phase_correction)
                correction_max = max(correction_max, tracker.last_phase_correction)
            completion = 0 if remainder == 0 else 2 * root + 1 - remainder
            survivors += int(passes_square_residue_cascade(completion, "BALANCED"))
        seeds += tracker.seed_divisions
        recurrent += tracker.recurrent_transitions
    return survivors, seeds, recurrent, correction_min, correction_max


def benchmark_rows() -> list[dict[str, object]]:
    rows = []
    for bits, samples, steps in CONFIGS:
        values = _population(bits, samples)
        reference = _direct_order1(values[0][0], values[0][1], steps)
        if _phase_quotient(values[0][0], values[0][1], steps) != reference:
            raise AssertionError("phase quotient pipeline changed semantics")
        if _phase_root(values[0][0], values[0][1], steps) != reference:
            raise AssertionError("phase root pipeline changed semantics")

        direct_seconds = _median_seconds(values, steps, _direct_order1)
        quotient_seconds = _median_seconds(values, steps, _phase_quotient)
        root_seconds = _median_seconds(values, steps, _phase_root)
        survivors, seeds, recurrent, correction_min, correction_max = _phase_stats(
            values,
            steps,
        )

        rows.append(
            {
                "n_bits": bits,
                "samples": samples,
                "steps_per_sample": steps,
                "seed_transitions_total": seeds,
                "recurrent_transitions_total": recurrent,
                "balanced_survivors": survivors,
                "observed_phase_correction_min": correction_min,
                "observed_phase_correction_max": correction_max,
                "direct_order1_seconds": direct_seconds,
                "phase_qr_seconds": quotient_seconds,
                "phase_root_seconds": root_seconds,
                "direct_over_phase_root": direct_seconds / root_seconds,
                "phase_qr_over_phase_root": quotient_seconds / root_seconds,
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
        / "brc_phase_root_recurrence_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
