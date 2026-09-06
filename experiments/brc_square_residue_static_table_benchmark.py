"""Deterministic timing harness for checked-in BRC square-residue tables.

The timings are implementation/environment diagnostics, not mathematical claims.
The harness separates (1) the second squarehood test on a precomputed gap from
(2) the full ceiling-gap pipeline, which must also compute ceil(sqrt(target)).
"""

from __future__ import annotations

import random
from math import isqrt
from statistics import median
from time import perf_counter

from enterprise_math.brc_square_gap_prefilter import square_residue_table

MODULI = (4032, 20160)


def _passes(value: int, modulus: int, table: bytes) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


def _direct_square_count(values: list[int]) -> int:
    count = 0
    for value in values:
        root = isqrt(value)
        count += int(root * root == value)
    return count


def _filtered_square_count(values: list[int], modulus: int) -> tuple[int, int]:
    table = square_residue_table(modulus)
    squares = 0
    survivors = 0
    for value in values:
        if not _passes(value, modulus, table):
            continue
        survivors += 1
        root = isqrt(value)
        squares += int(root * root == value)
    return squares, survivors


def _direct_full_pipeline(targets: list[int]) -> int:
    squares = 0
    for target in targets:
        lower = isqrt(target)
        upper = lower if lower * lower == target else lower + 1
        gap = upper * upper - target
        root = isqrt(gap)
        squares += int(root * root == gap)
    return squares


def _filtered_full_pipeline(targets: list[int], modulus: int) -> tuple[int, int]:
    table = square_residue_table(modulus)
    squares = 0
    survivors = 0
    for target in targets:
        lower = isqrt(target)
        upper = lower if lower * lower == target else lower + 1
        gap = upper * upper - target
        if not _passes(gap, modulus, table):
            continue
        survivors += 1
        root = isqrt(gap)
        squares += int(root * root == gap)
    return squares, survivors


def _make_gap_values(bits: int, count: int, square_every: int = 33) -> list[int]:
    rng = random.Random(20260906 + bits + count)
    values: list[int] = []
    for index in range(count):
        if index % square_every == 0:
            root_bits = max(1, (bits + 1) // 2)
            root = rng.getrandbits(max(1, root_bits - 1)) | (1 << max(0, root_bits - 1))
            values.append(root * root)
        else:
            values.append(rng.getrandbits(bits - 1) | (1 << (bits - 1)))
    return values


def _make_targets(bits: int, count: int, square_every: int = 33) -> list[int]:
    rng = random.Random(98765 + bits + count)
    values: list[int] = []
    half = (bits + 1) // 2
    for index in range(count):
        if index % square_every == 0:
            upper = (1 << (half - 1)) | rng.getrandbits(max(1, half - 1))
            max_b = isqrt(max(1, 2 * upper - 2))
            b = rng.randrange(1, max_b + 1)
            target = upper * upper - b * b
            assert (upper - 1) ** 2 < target < upper**2
            values.append(target)
        else:
            values.append(rng.getrandbits(bits - 1) | (1 << (bits - 1)))
    return values


def _median_time(callable_, repeats: int = 3):
    times = []
    result = None
    for _ in range(repeats):
        start = perf_counter()
        result = callable_()
        times.append(perf_counter() - start)
    return result, median(times)


def benchmark_gap_square_test(bits: int, count: int) -> dict[str, float | int]:
    values = _make_gap_values(bits, count)
    direct_count, direct_seconds = _median_time(lambda: _direct_square_count(values))
    row: dict[str, float | int] = {
        "bits": bits,
        "candidates": count,
        "direct_squares": int(direct_count),
        "direct_seconds": direct_seconds,
    }
    for modulus in MODULI:
        result, seconds = _median_time(lambda m=modulus: _filtered_square_count(values, m))
        squares, survivors = result
        assert squares == direct_count
        row[f"survivors_{modulus}"] = survivors
        row[f"seconds_{modulus}"] = seconds
        row[f"speedup_{modulus}"] = direct_seconds / seconds
    return row


def benchmark_full_pipeline(bits: int, count: int) -> dict[str, float | int]:
    targets = _make_targets(bits, count)
    direct_count, direct_seconds = _median_time(lambda: _direct_full_pipeline(targets))
    row: dict[str, float | int] = {
        "bits": bits,
        "candidates": count,
        "direct_square_gaps": int(direct_count),
        "direct_seconds": direct_seconds,
    }
    for modulus in MODULI:
        result, seconds = _median_time(lambda m=modulus: _filtered_full_pipeline(targets, m))
        squares, survivors = result
        assert squares == direct_count
        row[f"survivors_{modulus}"] = survivors
        row[f"seconds_{modulus}"] = seconds
        row[f"speedup_{modulus}"] = direct_seconds / seconds
    return row


if __name__ == "__main__":
    for bits, count in ((64, 80_000), (72, 80_000), (128, 60_000), (512, 40_000), (1024, 30_000), (2048, 20_000)):
        print("gap", benchmark_gap_square_test(bits, count))
    for bits, count in ((128, 30_000), (512, 20_000), (1024, 15_000), (2048, 10_000)):
        print("full", benchmark_full_pipeline(bits, count))
