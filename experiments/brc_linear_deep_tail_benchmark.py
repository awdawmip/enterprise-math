"""Finite benchmark for the order-1 linear deep-tail BRC stream.

The benchmark starts each odd N at the common certified threshold 4*m^5>=N,
aligns to the exact mod-8 representative set, and compares two equal-semantics
pipelines over 300 retained multiplier transitions:

1. direct incremental target + math.isqrt for every retained multiplier;
2. one initial isqrt followed by the linear order-1 Pell/BRC predictor.

Both pipelines use the same mod-4032 quadratic-residue gap filter and exact gap
isqrt on survivors.  The direct baseline therefore does not pay an artificial
m*N multiplication on every step.
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

BITS = (512, 1024, 2048, 4096, 8192)
SAMPLES = 16
STEPS = 300
REPEATS = 3
SEED = 20260907
MODULUS = 4032


def _square_residue_table() -> tuple[bool, ...]:
    table = [False] * MODULUS
    for value in range(MODULUS):
        table[(value * value) % MODULUS] = True
    return tuple(table)


QR = _square_residue_table()


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


def _direct_pipeline(n: int, start: int) -> tuple[int, int]:
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
        if QR[gap % MODULUS]:
            survivors += 1
            gap_root = isqrt(gap)
            checksum ^= int(gap_root * gap_root == gap)
    return checksum, survivors


def _linear_pipeline(n: int, start: int) -> tuple[int, int]:
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
        gap_state = remainder + step * n - d * (2 * root + d)
        corrections = 0
        while gap_state >= 2 * candidate + 1:
            gap_state -= 2 * candidate + 1
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("linear deep-tail correction theorem failed")
        root = candidate
        remainder = gap_state
        multiplier = nxt
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        if QR[gap % MODULUS]:
            survivors += 1
            gap_root = isqrt(gap)
            checksum ^= int(gap_root * gap_root == gap)
    return checksum, survivors


def _median_seconds(values: tuple[tuple[int, int], ...], fn) -> float:
    for n, start in values[:1]:
        fn(n, start)
    samples = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for n, start in values:
            fn(n, start)
        samples.append(time.perf_counter() - before)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for bits in BITS:
        population = _population(bits)
        values = tuple(
            (
                n,
                _align_representative(common_mod8_linear_tail_threshold(n)),
            )
            for n in population
        )
        for n, start in values:
            if _direct_pipeline(n, start) != _linear_pipeline(n, start):
                raise AssertionError("direct and linear deep-tail pipelines disagreed")

        direct = _median_seconds(values, _direct_pipeline)
        linear = _median_seconds(values, _linear_pipeline)
        survivor_count = sum(_direct_pipeline(n, start)[1] for n, start in values)
        rows.append(
            {
                "n_bits": bits,
                "samples": SAMPLES,
                "steps_per_sample": STEPS,
                "first_threshold_bit_length": values[0][1].bit_length(),
                "mod4032_survivors": survivor_count,
                "direct_incremental_isqrt_seconds": direct,
                "linear_pell_brc_seconds": linear,
                "direct_over_linear_speedup": direct / linear,
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
        / "brc_linear_deep_tail_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
