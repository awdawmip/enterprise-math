"""Finite full-pipeline benchmark for the BRC quotient/remainder jet.

All paths start at the certified quotient-jet threshold and process the same
retained odd-N mod-8 multiplier transitions. Every path also uses the same
BALANCED square-gap residue cascade and exact gap isqrt on survivors.

Compared paths:
1. incremental target plus direct isqrt at every multiplier;
2. order-one linear BRC transport with a fresh quotient division every step;
3. the quotient jet, including its fixed fifteen seed divisions.
"""
from __future__ import annotations

import csv
from math import isqrt
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_quotient_jet_tail import (
    QuotientJetTailScanner,
    outgoing_sparse_step,
    quotient_jet_tail_threshold,
)
from enterprise_math.brc_square_gap_cascade import (
    passes_square_residue_cascade,
)

BITS = (1024, 2048, 4096, 8192, 16384)
SAMPLES_BY_BITS = {
    1024: 16,
    2048: 12,
    4096: 8,
    8192: 4,
    16384: 2,
}
TRANSITIONS = 1500
REPEATS = 3
SEED = 20260907


def _consume_gap(root: int, remainder: int) -> tuple[int, int]:
    gap = 0 if remainder == 0 else 2 * root + 1 - remainder
    if not passes_square_residue_cascade(gap, "BALANCED"):
        return 0, 0
    gap_root = isqrt(gap)
    return 1, int(gap_root * gap_root == gap)


def direct_pipeline(n: int, start: int) -> tuple[int, int]:
    multiplier = start
    target = multiplier * n
    survivors = 0
    checksum = 0
    for _ in range(TRANSITIONS):
        step = outgoing_sparse_step(multiplier)
        multiplier += step
        target += step * n
        root = isqrt(target)
        remainder = target - root * root
        survived, square = _consume_gap(root, remainder)
        survivors += survived
        checksum ^= square
    return survivors, checksum


def linear_division_pipeline(n: int, start: int) -> tuple[int, int]:
    multiplier = start
    target = multiplier * n
    root = isqrt(target)
    remainder = target - root * root
    survivors = 0
    checksum = 0

    for _ in range(TRANSITIONS):
        step = outgoing_sparse_step(multiplier)
        quotient = (2 * step * root) // (4 * multiplier + step)
        candidate = root + quotient
        gap_state = (
            remainder
            + step * n
            - quotient * (2 * root + quotient)
        )
        corrections = 0
        odd_width = 2 * candidate + 1
        while gap_state >= odd_width:
            gap_state -= odd_width
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("linear-tail correction theorem failed")
            odd_width += 2

        multiplier += step
        root = candidate
        remainder = gap_state
        survived, square = _consume_gap(root, remainder)
        survivors += survived
        checksum ^= square

    return survivors, checksum


def quotient_jet_pipeline(n: int, start: int) -> tuple[int, int, int, int]:
    scanner = QuotientJetTailScanner(n, start)
    survivors = 0
    checksum = 0
    for _ in range(TRANSITIONS):
        scanner.advance_inplace()
        survived, square = _consume_gap(scanner.root, scanner.remainder)
        survivors += survived
        checksum ^= square
    return (
        survivors,
        checksum,
        scanner.seed_divisions,
        scanner.max_abs_quotient_correction,
    )


def _median_seconds(values: tuple[tuple[int, int], ...], function) -> float:
    function(*values[0])
    samples: list[float] = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for arguments in values:
            function(*arguments)
        samples.append(time.perf_counter() - before)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for bits in BITS:
        rng = random.Random(SEED + bits)
        values: list[tuple[int, int]] = []
        max_abs_correction = 0
        survivor_count = 0

        for _ in range(SAMPLES_BY_BITS[bits]):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            start = quotient_jet_tail_threshold(n)
            values.append((n, start))

            direct_result = direct_pipeline(n, start)
            linear_result = linear_division_pipeline(n, start)
            jet_result = quotient_jet_pipeline(n, start)
            if direct_result != linear_result or direct_result != jet_result[:2]:
                raise AssertionError("benchmark pipelines disagreed")
            if jet_result[2] != 15:
                raise AssertionError("seed division count drifted")
            max_abs_correction = max(max_abs_correction, jet_result[3])
            survivor_count += jet_result[0]

        frozen_values = tuple(values)
        direct_seconds = _median_seconds(frozen_values, direct_pipeline)
        linear_seconds = _median_seconds(
            frozen_values,
            linear_division_pipeline,
        )
        jet_seconds = _median_seconds(frozen_values, quotient_jet_pipeline)
        rows.append(
            {
                "n_bits": bits,
                "samples": len(frozen_values),
                "transitions_per_sample": TRANSITIONS,
                "seed_divisions_per_sample": 15,
                "max_abs_quotient_correction": max_abs_correction,
                "balanced_cascade_survivors": survivor_count,
                "direct_incremental_isqrt_seconds": direct_seconds,
                "linear_fresh_division_seconds": linear_seconds,
                "quotient_jet_seconds": jet_seconds,
                "direct_over_quotient_jet": direct_seconds / jet_seconds,
                "linear_over_quotient_jet": linear_seconds / jet_seconds,
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
        / "brc_quotient_jet_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
