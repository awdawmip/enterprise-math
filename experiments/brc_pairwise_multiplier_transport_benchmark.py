"""Finite benchmark for pairwise BRC priority-state transport.

The benchmark separates:
1. the pre-Round-7 priority sequence API;
2. an idealized direct-from-one stream with the m=1 state cached once;
3. the new pairwise chain along the same structural priority order.

It measures state materialization only. Factor-search semantics and ranking are
identical across the three paths.
"""

from __future__ import annotations

import csv
import random
import statistics
import time
from pathlib import Path

from enterprise_math.brc_multiplier_priority_jump import (
    prioritized_odd_multiplier_order,
    prioritized_odd_multiplier_states,
)
from enterprise_math.brc_multiplier_transition import initial_multiplier_root_state
from enterprise_math.brc_pairwise_multiplier_transport import (
    pairwise_prioritized_odd_multiplier_states,
    transport_multiplier_root_state,
)

BITS = (128, 256, 512, 1024, 2048, 4096)
SAMPLES = 500
REPEATS = 5
SEED = 20260907


def population(bits: int) -> tuple[int, ...]:
    rng = random.Random(SEED + bits)
    return tuple(
        rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        for _ in range(SAMPLES)
    )


def current_sequence(n: int):
    return prioritized_odd_multiplier_states(n, 100)


def optimized_direct_from_one(n: int):
    base = initial_multiplier_root_state(n)
    order = prioritized_odd_multiplier_order(100)
    return tuple(transport_multiplier_root_state(base, m) for m in order)


def pairwise_chain(n: int):
    return pairwise_prioritized_odd_multiplier_states(n, 100)


def median_seconds(values: tuple[int, ...], fn) -> float:
    fn(values[0])
    samples = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        for n in values:
            fn(n)
        samples.append(time.perf_counter() - start)
    return statistics.median(samples)


def benchmark_rows() -> list[dict[str, object]]:
    rows = []
    for bits in BITS:
        values = population(bits)
        current = median_seconds(values, current_sequence)
        direct = median_seconds(values, optimized_direct_from_one)
        pairwise = median_seconds(values, pairwise_chain)

        n = values[0]
        a = current_sequence(n)
        b = optimized_direct_from_one(n)
        c = pairwise_chain(n)
        triples_a = tuple((s.multiplier, s.root, s.remainder) for s in a)
        triples_b = tuple((s.multiplier, s.root, s.remainder) for s in b)
        triples_c = tuple((s.multiplier, s.root, s.remainder) for s in c)
        if not (triples_a == triples_b == triples_c):
            raise AssertionError("priority transport paths disagreed")

        rows.append(
            {
                "n_bits": bits,
                "samples": SAMPLES,
                "current_priority_seconds": current,
                "optimized_direct_from_one_seconds": direct,
                "pairwise_chain_seconds": pairwise,
                "current_over_pairwise": current / pairwise,
                "optimized_direct_over_pairwise": direct / pairwise,
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
        / "brc_pairwise_multiplier_transport_benchmark_20260907.csv"
    )
    write_csv(target)
    print(target)
