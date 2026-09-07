"""Finite benchmark for BRC completion-gap residue transport.

The parent square-increment energy jet is identical on both paths. The native
path materializes every completion gap and sends it through the current
4032/12155/12673 cascade. The COMPACT residue path transports J modulo
4032*12155 on five stride-eight source orbits, tests the first two tables from
that word-size residue, and materializes the exact gap only for their survivors.

Five deterministic populations are used at each bit size. Timing ratios are
reported population-by-population and then summarized by their median so a
single noisy process interval is not treated as a stable crossover claim.
"""

from __future__ import annotations

import csv
import gc
from math import isqrt
from pathlib import Path
import random
import statistics
import time

from enterprise_math.brc_energy_difference_jet_tail import (
    EnergyDifferenceJetTailScanner,
)
from enterprise_math.brc_gap_residue_jet_tail import GapResidueJetTailScanner
from enterprise_math.brc_square_gap_cascade import (
    cascade_table,
    passes_square_residue_cascade,
)

BITS = (1024, 2048, 4096, 8192, 16384)
POPULATIONS = 5
SAMPLES_PER_POPULATION = 4
TRANSITIONS = 2000
REPEATS = 3
SEED = 2026090720


def _population(bits: int, population_index: int) -> tuple[int, ...]:
    rng = random.Random(SEED + bits + population_index * 100000)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(SAMPLES_PER_POPULATION)
    )


def _native_pipeline(n: int) -> tuple[int, int, int, int, int]:
    scanner = EnergyDifferenceJetTailScanner(n)
    survivors = squares = 0
    for _ in range(TRANSITIONS):
        root, remainder = scanner.root, scanner.remainder
        scanner.advance_inplace()
        gap = 0 if remainder == 0 else 2 * root + 1 - remainder
        if passes_square_residue_cascade(gap, "BALANCED"):
            survivors += 1
            gap_root = isqrt(gap)
            squares += int(gap_root * gap_root == gap)
    return (
        scanner.multiplier,
        scanner.root,
        scanner.remainder,
        survivors,
        squares,
    )


def _compact_pipeline(n: int) -> tuple[int, ...]:
    scanner = GapResidueJetTailScanner(n, transported_profile="COMPACT")
    survivors = squares = 0
    for _ in range(TRANSITIONS):
        scanner.advance_filter_inplace()
        survivors += int(scanner.last_cascade_passed)
        squares += int(bool(scanner.last_exact_square))
    return (
        scanner.multiplier,
        scanner.root,
        scanner.remainder,
        survivors,
        squares,
        scanner.root_seed_mod_reductions,
        scanner.root_residue_jet_steps,
        scanner.exact_gap_materializations,
        scanner.native_big_mod_reductions,
    )


def _median_cpu_seconds(values: tuple[int, ...], function) -> float:
    timings: list[float] = []
    for _ in range(REPEATS):
        before = time.process_time_ns()
        for n in values:
            function(n)
        timings.append((time.process_time_ns() - before) / 1e9)
    return statistics.median(timings)


def benchmark_rows() -> list[dict[str, object]]:
    for modulus in (4032, 12155, 12673):
        cascade_table(modulus)

    rows: list[dict[str, object]] = []
    gc.disable()
    try:
        for bits in BITS:
            ratios: list[float] = []
            first_two_survivors = full_survivors = 0
            seed_reductions: set[int] = set()
            jet_steps: set[int] = set()
            for population_index in range(POPULATIONS):
                values = _population(bits, population_index)
                native_outputs = tuple(
                    _native_pipeline(n) for n in values
                )
                compact_outputs = tuple(
                    _compact_pipeline(n) for n in values
                )
                if tuple(x[:5] for x in compact_outputs) != native_outputs:
                    raise AssertionError(
                        "native and compact residue pipelines disagreed"
                    )
                first_two_survivors += sum(x[7] for x in compact_outputs)
                full_survivors += sum(x[3] for x in compact_outputs)
                seed_reductions.update(x[5] for x in compact_outputs)
                jet_steps.update(x[6] for x in compact_outputs)

                if population_index & 1:
                    compact = _median_cpu_seconds(
                        values,
                        _compact_pipeline,
                    )
                    native = _median_cpu_seconds(values, _native_pipeline)
                else:
                    native = _median_cpu_seconds(values, _native_pipeline)
                    compact = _median_cpu_seconds(
                        values,
                        _compact_pipeline,
                    )
                ratios.append(native / compact)

            if seed_reductions != {15}:
                raise AssertionError(
                    f"unexpected root seed count: {seed_reductions}"
                )
            if jet_steps != {TRANSITIONS - 15}:
                raise AssertionError(
                    f"unexpected residue-jet step count: {jet_steps}"
                )
            rows.append(
                {
                    "n_bits": bits,
                    "populations": POPULATIONS,
                    "samples_per_population": SAMPLES_PER_POPULATION,
                    "transitions_per_sample": TRANSITIONS,
                    "total_states": (
                        POPULATIONS
                        * SAMPLES_PER_POPULATION
                        * TRANSITIONS
                    ),
                    "first_two_stage_survivors": first_two_survivors,
                    "balanced_survivors": full_survivors,
                    "median_native_over_compact": statistics.median(
                        ratios
                    ),
                    "mean_native_over_compact": statistics.mean(ratios),
                    "min_native_over_compact": min(ratios),
                    "max_native_over_compact": max(ratios),
                    "population_ratios": ";".join(
                        f"{ratio:.9f}" for ratio in ratios
                    ),
                    "root_seed_mod_reductions_per_sample": 15,
                    "residue_jet_steps_per_sample": TRANSITIONS - 15,
                }
            )
    finally:
        gc.enable()
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
        / "brc_gap_residue_jet_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
