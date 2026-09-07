"""Finite benchmark for the BRC square-increment difference jet.

Three equal-semantics pipelines start at the certified quotient-jet tail and
scan the same exact odd-N mod-8 representative multipliers:

1. direct incremental target plus ``math.isqrt`` at every retained multiplier;
2. quotient/remainder jet plus a fresh ``q*(2J+q)`` square increment;
3. quotient/remainder jet plus the new exact third-difference energy jet.

Every pipeline uses the same BALANCED square-gap residue cascade and exact gap
``isqrt`` on survivors.  Table construction is warmed before timing.
"""
from __future__ import annotations

import csv
from math import isqrt
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_energy_difference_jet_tail import (
    EnergyDifferenceJetTailScanner,
)
from enterprise_math.brc_quotient_jet_tail import (
    QuotientJetTailScanner,
    outgoing_sparse_step,
    quotient_jet_tail_threshold,
)
from enterprise_math.brc_square_gap_cascade import (
    cascade_table,
    passes_square_residue_cascade,
)

BITS = (1024, 2048, 4096, 8192, 16384)
SAMPLES = 5
TRANSITIONS = 1500
REPEATS = 3
SEED = 2026090713


def _population(bits: int) -> tuple[int, ...]:
    rng = random.Random(SEED + bits)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(SAMPLES)
    )


def _finish_gap(gap: int) -> tuple[int, int]:
    if not passes_square_residue_cascade(gap, "BALANCED"):
        return 0, 0
    root = isqrt(gap)
    return 1, int(root * root == gap)


def _direct_root_pipeline(n: int) -> tuple[int, int, int, int, int, int]:
    multiplier = quotient_jet_tail_threshold(n)
    target = multiplier * n
    root = isqrt(target)
    remainder = target - root * root
    survivors = 0
    squares = 0
    checksum = 0
    for _ in range(TRANSITIONS):
        step = outgoing_sparse_step(multiplier)
        multiplier += step
        target += step * n
        root = isqrt(target)
        remainder = target - root * root
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        survived, square = _finish_gap(gap)
        survivors += survived
        squares += square
        checksum ^= (root & 65535) ^ (remainder & 65535) ^ survivors
    return multiplier, root, remainder, survivors, squares, checksum


def _quotient_product_pipeline(n: int) -> tuple[int, int, int, int, int, int]:
    scanner = QuotientJetTailScanner(n)
    survivors = 0
    squares = 0
    checksum = 0
    for _ in range(TRANSITIONS):
        scanner.advance_inplace()
        gap = 0 if scanner.remainder == 0 else 2 * scanner.root + 1 - scanner.remainder
        survived, square = _finish_gap(gap)
        survivors += survived
        squares += square
        checksum ^= (scanner.root & 65535) ^ (scanner.remainder & 65535) ^ survivors
    return (
        scanner.multiplier,
        scanner.root,
        scanner.remainder,
        survivors,
        squares,
        checksum,
    )


def _energy_difference_pipeline(
    n: int,
) -> tuple[int, int, int, int, int, int, int, int, int]:
    scanner = EnergyDifferenceJetTailScanner(n)
    survivors = 0
    squares = 0
    checksum = 0
    for _ in range(TRANSITIONS):
        scanner.advance_inplace()
        gap = 0 if scanner.remainder == 0 else 2 * scanner.root + 1 - scanner.remainder
        survived, square = _finish_gap(gap)
        survivors += survived
        squares += square
        checksum ^= (scanner.root & 65535) ^ (scanner.remainder & 65535) ^ survivors
    return (
        scanner.multiplier,
        scanner.root,
        scanner.remainder,
        survivors,
        squares,
        checksum,
        scanner.seed_divisions,
        scanner.seed_square_increment_products,
        scanner.max_root_third_difference,
    )


def _median_seconds(values: tuple[int, ...], function) -> float:
    function(values[0])
    timings = []
    for _ in range(REPEATS):
        before = time.perf_counter()
        for n in values:
            function(n)
        timings.append(time.perf_counter() - before)
    return statistics.median(timings)


def benchmark_rows() -> list[dict[str, object]]:
    # Exclude deterministic one-time table compilation from the scan timings.
    for modulus in (4032, 12155, 12673):
        cascade_table(modulus)

    rows = []
    for bits in BITS:
        values = _population(bits)
        direct_outputs = tuple(_direct_root_pipeline(n) for n in values)
        quotient_outputs = tuple(_quotient_product_pipeline(n) for n in values)
        energy_outputs = tuple(_energy_difference_pipeline(n) for n in values)
        energy_semantics = tuple(output[:6] for output in energy_outputs)
        if not (direct_outputs == quotient_outputs == energy_semantics):
            raise AssertionError("benchmark pipelines disagreed")

        direct = _median_seconds(values, _direct_root_pipeline)
        quotient = _median_seconds(values, _quotient_product_pipeline)
        energy = _median_seconds(values, _energy_difference_pipeline)
        rows.append(
            {
                "n_bits": bits,
                "samples": SAMPLES,
                "transitions_per_sample": TRANSITIONS,
                "balanced_cascade_survivors": sum(x[3] for x in direct_outputs),
                "direct_incremental_isqrt_seconds": direct,
                "quotient_jet_fresh_product_seconds": quotient,
                "energy_difference_jet_seconds": energy,
                "direct_over_quotient_product": direct / quotient,
                "direct_over_energy_difference": direct / energy,
                "quotient_product_over_energy_difference": quotient / energy,
                "seed_divisions_per_sample": energy_outputs[0][6],
                "seed_square_increment_products_per_sample": energy_outputs[0][7],
                "max_root_third_difference_seen": max(x[8] for x in energy_outputs),
            }
        )
    return rows


def write_csv(path: str | Path) -> None:
    rows = benchmark_rows()
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    target = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_energy_difference_jet_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
