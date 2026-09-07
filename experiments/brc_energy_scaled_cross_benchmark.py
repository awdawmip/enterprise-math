"""Finite benchmark for the scaled cross-coordinate energy jet.

Compare the current M=(nabla q)(nabla^2 J) implementation with the
information-equivalent C=6K implementation on the same deterministic odd N
values, the same certified tail starts, and the same BALANCED square-gap table
cascade.  Both scanners produce exactly the same multiplier/root/remainder and
square-increment states; this experiment measures only the execution-coordinate
constant factor.
"""
from __future__ import annotations

import csv
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_energy_difference_jet_tail import (
    EnergyDifferenceJetTailScanner,
)
from enterprise_math.brc_energy_scaled_cross_tail import (
    ScaledCrossEnergyTailScanner,
)
from enterprise_math.brc_square_gap_cascade import passes_square_residue_cascade

BITS_AND_SAMPLES = (
    (1024, 8),
    (2048, 8),
    (4096, 8),
    (8192, 6),
    (16384, 4),
)
TRANSITIONS = 3000
REPEATS = 7
SEED = 2026090719


def _population(bits: int, samples: int) -> tuple[int, ...]:
    rng = random.Random(SEED + bits)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(samples)
    )


def _run(values: tuple[int, ...], scanner_type) -> int:
    checksum = 0
    for n in values:
        scanner = scanner_type(n)
        for _ in range(TRANSITIONS):
            scanner.advance_inplace()
            gap = (
                0
                if scanner.remainder == 0
                else 2 * scanner.root + 1 - scanner.remainder
            )
            checksum ^= int(passes_square_residue_cascade(gap, "BALANCED"))
    return checksum


def _median_seconds(values: tuple[int, ...], scanner_type) -> float:
    _run(values[:1], scanner_type)
    samples: list[float] = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        _run(values, scanner_type)
        samples.append(time.perf_counter() - before)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for bits, sample_count in BITS_AND_SAMPLES:
        values = _population(bits, sample_count)
        if _run(values, EnergyDifferenceJetTailScanner) != _run(
            values, ScaledCrossEnergyTailScanner
        ):
            raise AssertionError("energy coordinate variants disagreed")
        old_seconds = _median_seconds(values, EnergyDifferenceJetTailScanner)
        new_seconds = _median_seconds(values, ScaledCrossEnergyTailScanner)
        rows.append(
            {
                "n_bits": bits,
                "samples": sample_count,
                "transitions_per_sample": TRANSITIONS,
                "mixed_M_seconds": old_seconds,
                "scaled_cross_C_seconds": new_seconds,
                "mixed_over_scaled_cross_speedup": old_seconds / new_seconds,
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
        / "brc_energy_scaled_cross_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
