"""Finite timing harness for consecutive BRC multiplier transport.

Compares direct roots, the existing mod-4032 gap residue filter, and the new
root-free m->m+1 transition composed with that filter. Timing is
environment-specific finite evidence, not a complexity theorem.
"""

from __future__ import annotations

import csv
import random
import time
from math import isqrt
from pathlib import Path
from statistics import median

from enterprise_math.brc_multiplier_transition import (
    multiplier_root_state_sequence,
    transition_table_mode,
)
from enterprise_math.brc_square_gap_prefilter import passes_square_residue_filter


BIT_CASES = (
    (128, 64, 7),
    (256, 64, 7),
    (512, 48, 7),
    (1024, 32, 7),
    (2048, 20, 5),
    (4096, 10, 5),
)


def _direct(n: int) -> int:
    hits = 0
    for m in range(1, 101):
        target = m * n
        root = isqrt(target)
        remainder = target - root * root
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        b = isqrt(gap)
        hits += int(b * b == gap)
    return hits


def _residue(n: int) -> int:
    hits = 0
    for m in range(1, 101):
        target = m * n
        root = isqrt(target)
        remainder = target - root * root
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        if passes_square_residue_filter(gap):
            b = isqrt(gap)
            hits += int(b * b == gap)
    return hits


def _transition_residue(n: int) -> tuple[int, int]:
    hits = 0
    corrections = 0
    if transition_table_mode(n) != "STATIC":
        raise AssertionError("reference benchmark is static-table-only")
    for state in multiplier_root_state_sequence(n, 100):
        corrections += state.correction_steps
        gap = state.ceiling_completion_gap
        if passes_square_residue_filter(gap):
            b = isqrt(gap)
            hits += int(b * b == gap)
    return hits, corrections


def benchmark() -> list[dict[str, object]]:
    rows = []
    for bits, sample_count, repeats in BIT_CASES:
        rng = random.Random(8800 + bits)
        values = [
            rng.getrandbits(bits - 1) | (1 << (bits - 1)) | 1
            for _ in range(sample_count)
        ]
        for n in values[:3]:
            direct = _direct(n)
            residue = _residue(n)
            transition, _ = _transition_residue(n)
            if not (direct == residue == transition):
                raise AssertionError("factor-gap pipeline methods disagreed")

        direct_times = []
        residue_times = []
        transition_times = []
        correction_total = 0
        correction_denominator = 0
        for _ in range(repeats):
            start = time.perf_counter()
            for n in values:
                _direct(n)
            direct_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            for n in values:
                _residue(n)
            residue_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            for n in values:
                _, corrections = _transition_residue(n)
                correction_total += corrections
                correction_denominator += 99
            transition_times.append(time.perf_counter() - start)

        direct = median(direct_times)
        residue = median(residue_times)
        transition = median(transition_times)
        rows.append({
            "n_bits": bits,
            "sample_count": sample_count,
            "direct_seconds": direct,
            "residue_seconds": residue,
            "transition_residue_seconds": transition,
            "residue_speedup_vs_direct": direct / residue,
            "transition_speedup_vs_direct": direct / transition,
            "transition_speedup_vs_residue": residue / transition,
            "mean_corrections_per_transition": correction_total / correction_denominator,
        })
    return rows


def write_csv(path: str | Path) -> None:
    rows = benchmark()
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    destination = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_multiplier_transition_benchmark_20260906.csv"
    )
    write_csv(destination)
    print(destination)
