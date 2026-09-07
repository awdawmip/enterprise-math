"""Finite benchmark for staged BRC square-gap residue tables.

The benchmark composes the Round-11 order-1 linear deep-tail root transport with
three square-gap policies:

1. no modular table: every gap reaches exact isqrt;
2. BASE: the existing 504-byte mod-4032 table;
3. BALANCED: 4032 -> 12155 -> 12673 staged tables.

The direct baseline carries target by h*N and recomputes math.isqrt at each
retained multiplier.  Pipeline checksums must agree across every policy.
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
from enterprise_math.brc_square_gap_cascade import passes_square_residue_cascade

BITS = (1024, 2048, 4096, 8192)
SAMPLES = 16
STEPS = 700
REPEATS = 3
SEED = 20260907


def _align_representative(multiplier: int) -> int:
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def _population(bits: int) -> tuple[int, ...]:
    rng = random.Random(SEED + 10000 + bits)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(SAMPLES)
    )


def _accept_gap(gap: int, profile: str | None) -> bool:
    return True if profile is None else passes_square_residue_cascade(gap, profile)


def _direct_pipeline(n: int, start: int, profile: str | None) -> tuple[int, int]:
    target = start * n
    multiplier = start
    checksum = 0
    survivors = 0
    for _ in range(STEPS):
        nxt = next_odd_n_representative_multiplier(multiplier)
        step = nxt - multiplier
        target += step * n
        root = isqrt(target)
        remainder = target - root * root
        multiplier = nxt
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        if _accept_gap(gap, profile):
            survivors += 1
            gap_root = isqrt(gap)
            checksum ^= int(gap_root * gap_root == gap)
    return checksum, survivors


def _linear_pipeline(n: int, start: int, profile: str | None) -> tuple[int, int]:
    target = start * n
    root = isqrt(target)
    remainder = target - root * root
    multiplier = start
    checksum = 0
    survivors = 0
    for _ in range(STEPS):
        nxt = next_odd_n_representative_multiplier(multiplier)
        step = nxt - multiplier
        d = (2 * step * root) // (4 * multiplier + step)
        candidate = root + d
        state_gap = remainder + step * n - d * (2 * root + d)
        corrections = 0
        while state_gap >= 2 * candidate + 1:
            state_gap -= 2 * candidate + 1
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("linear deep-tail correction theorem failed")
        root = candidate
        remainder = state_gap
        multiplier = nxt
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        if _accept_gap(gap, profile):
            survivors += 1
            gap_root = isqrt(gap)
            checksum ^= int(gap_root * gap_root == gap)
    return checksum, survivors


def _median_seconds(values, fn) -> float:
    fn(*values[0])
    samples = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for args in values:
            fn(*args)
        samples.append(time.perf_counter() - before)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for bits in BITS:
        values = tuple(
            (n, _align_representative(common_mod8_linear_tail_threshold(n)))
            for n in _population(bits)
        )
        direct_none_values = tuple((n, start, None) for n, start in values)
        direct_base_values = tuple((n, start, "BASE") for n, start in values)
        linear_base_values = tuple((n, start, "BASE") for n, start in values)
        linear_balanced_values = tuple((n, start, "BALANCED") for n, start in values)

        # All paths must agree on exact-square parity/checksum.  Survivor counts
        # differ only because stronger necessary filters reject more nonsquares.
        reference_checksum = 0
        for n, start in values:
            reference_checksum ^= _direct_pipeline(n, start, None)[0]
            if _direct_pipeline(n, start, "BASE")[0] != _linear_pipeline(n, start, "BASE")[0]:
                raise AssertionError("BASE direct/linear pipelines disagreed")
            if _direct_pipeline(n, start, None)[0] != _linear_pipeline(n, start, "BALANCED")[0]:
                raise AssertionError("BALANCED cascade lost an exact-square witness")

        direct_none = _median_seconds(direct_none_values, _direct_pipeline)
        direct_base = _median_seconds(direct_base_values, _direct_pipeline)
        linear_base = _median_seconds(linear_base_values, _linear_pipeline)
        linear_balanced = _median_seconds(linear_balanced_values, _linear_pipeline)
        base_survivors = sum(_linear_pipeline(n, start, "BASE")[1] for n, start in values)
        balanced_survivors = sum(
            _linear_pipeline(n, start, "BALANCED")[1] for n, start in values
        )
        rows.append(
            {
                "n_bits": bits,
                "samples": SAMPLES,
                "steps_per_sample": STEPS,
                "base_survivors": base_survivors,
                "balanced_survivors": balanced_survivors,
                "direct_no_table_seconds": direct_none,
                "direct_base4032_seconds": direct_base,
                "linear_base4032_seconds": linear_base,
                "linear_balanced_cascade_seconds": linear_balanced,
                "direct_no_table_over_linear_balanced": direct_none / linear_balanced,
                "linear_base_over_linear_balanced": linear_base / linear_balanced,
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
        / "brc_square_gap_cascade_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
