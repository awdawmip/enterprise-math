"""Finite benchmark for phase quotient/remainder transport on the BRC deep tail.

Both paths use the same order-1 BRC root update and BALANCED square-gap cascade.
The only changed operation is the increment quotient

    floor(2*h*J/(4*m+h)).

Baseline performs a fresh native divmod every retained multiplier.  The phase
path uses PhaseQuotientRemainderTracker: two seed divmods in each of five mod-8
phases, then second-difference quotient/remainder transport plus the 1KB
normalized reciprocal table.
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
    RECIPROCAL_RAW_BYTES,
    PhaseQuotientRemainderTracker,
)
from enterprise_math.brc_square_gap_cascade import passes_square_residue_cascade

BITS = (1024, 2048, 4096, 8192)
SAMPLES = 16
STEPS = 700
REPEATS = 5
SEED = 20260907


def _align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def _population(bits: int) -> tuple[int, ...]:
    rng = random.Random(SEED + bits)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(SAMPLES)
    )


def _finish_step(n: int, root: int, remainder: int, m: int, h: int, d: int):
    candidate = root + d
    gap_state = remainder + h * n - d * (2 * root + d)
    corrections = 0
    odd_width = 2 * candidate + 1
    while gap_state >= odd_width:
        gap_state -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 2:
            raise AssertionError("order-1 two-correction theorem failed")
        odd_width += 2
    return candidate, gap_state, m + h


def _gap_check(root: int, remainder: int) -> tuple[int, int]:
    gap = 0 if remainder == 0 else 2 * root + 1 - remainder
    if not passes_square_residue_cascade(gap, "BALANCED"):
        return 0, 0
    gap_root = isqrt(gap)
    return 1, int(gap_root * gap_root == gap)


def _direct_pipeline(n: int, start: int) -> tuple[int, int]:
    target = start * n
    root = isqrt(target)
    remainder = target - root * root
    m = start
    survivors = checksum = 0
    for _ in range(STEPS):
        nxt = next_odd_n_representative_multiplier(m)
        h = nxt - m
        d, _ = divmod(2 * h * root, 4 * m + h)
        root, remainder, m = _finish_step(n, root, remainder, m, h, d)
        survived, square = _gap_check(root, remainder)
        survivors += survived
        checksum ^= square
    return survivors, checksum


def _phase_pipeline(n: int, start: int) -> tuple[int, int, int, int]:
    target = start * n
    root = isqrt(target)
    remainder = target - root * root
    m = start
    tracker = PhaseQuotientRemainderTracker(n)
    survivors = checksum = seeds = recurrent = 0
    for _ in range(STEPS):
        nxt = next_odd_n_representative_multiplier(m)
        h = nxt - m
        d, _ = tracker.divide_pair(root, m, h)
        if tracker.last_mode == "SEED_DIVMOD":
            seeds += 1
        else:
            recurrent += 1
        root, remainder, m = _finish_step(n, root, remainder, m, h, d)
        survived, square = _gap_check(root, remainder)
        survivors += survived
        checksum ^= square
    return survivors, checksum, seeds, recurrent


def _median_seconds(values: tuple[tuple[int, int], ...], fn) -> float:
    fn(*values[0])
    times = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for args in values:
            fn(*args)
        times.append(time.perf_counter() - before)
    return statistics.median(times)


def benchmark_rows() -> list[dict[str, object]]:
    rows = []
    for bits in BITS:
        values = tuple(
            (n, _align_representative(common_mod8_linear_tail_threshold(n)))
            for n in _population(bits)
        )
        seed_count = recurrent_count = 0
        for n, start in values:
            direct = _direct_pipeline(n, start)
            phase = _phase_pipeline(n, start)
            if direct != phase[:2]:
                raise AssertionError("direct and phase quotient pipelines disagreed")
            seed_count += phase[2]
            recurrent_count += phase[3]

        direct_seconds = _median_seconds(values, _direct_pipeline)
        phase_seconds = _median_seconds(values, _phase_pipeline)
        rows.append(
            {
                "n_bits": bits,
                "samples": SAMPLES,
                "steps_per_sample": STEPS,
                "reciprocal_table_raw_bytes": RECIPROCAL_RAW_BYTES,
                "seed_divmods": seed_count,
                "recurrent_quotients": recurrent_count,
                "direct_divmod_seconds": direct_seconds,
                "phase_qr_seconds": phase_seconds,
                "direct_over_phase_speedup": direct_seconds / phase_seconds,
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
        / "brc_phase_quotient_remainder_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
