"""Finite rank recheck for the opportunistic multiplier-order portfolio.

This recheck is intentionally about *candidate rank*, not machine runtime.
Every compared order contains the same exact mod-8 representative set.  It
therefore measures whether preserving specialist prefixes can bring exact
witnesses earlier without changing coverage.

Populations:
- all distinct semiprimes p*q with 101<=p<q<=997;
- 20,000 deterministic distinct pairs from primes 1009..4999.

The factor test is the classical immediate multiplier-Fermat square-gap witness.
"""
from __future__ import annotations

import csv
from math import gcd, isqrt
from pathlib import Path
import random
import statistics

from enterprise_math.brc_opportunistic_shortcuts import (
    flatten_probe_batches,
    learned_cover_order,
    multiplier_probe_batches,
    ratio_cover_order,
    structural_order,
)

SAMPLE_SEED = 20260906


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                ((limit - start) // p) + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def immediate_factor_success(n: int, multiplier: int) -> bool:
    target = multiplier * n
    x = isqrt(target)
    if x * x < target:
        x += 1
    gap = x * x - target
    b = isqrt(gap)
    if b * b != gap:
        return False
    factor = gcd(x - b, n)
    return 1 < factor < n


def all_distinct_semiprimes(lo: int, hi: int) -> list[int]:
    primes = [p for p in primes_up_to(hi) if p >= lo]
    return [
        primes[i] * primes[j]
        for i in range(len(primes))
        for j in range(i + 1, len(primes))
    ]


def deterministic_semiprimes(
    lo: int, hi: int, count: int, seed: int
) -> list[int]:
    primes = [p for p in primes_up_to(hi) if p >= lo]
    rng = random.Random(seed)
    pairs: set[tuple[int, int]] = set()
    while len(pairs) < count:
        i, j = rng.sample(range(len(primes)), 2)
        if i > j:
            i, j = j, i
        pairs.add((i, j))
    return [primes[i] * primes[j] for i, j in pairs]


def first_rank(n: int, order: tuple[int, ...]) -> int | None:
    for rank, multiplier in enumerate(order, 1):
        if immediate_factor_success(n, multiplier):
            return rank
    return None


def _p90(values: list[int]) -> float:
    ordered = sorted(values)
    index = max(0, (9 * len(ordered) + 9) // 10 - 1)
    return float(ordered[index])


def summarize(
    population_name: str,
    population: list[int],
    order_name: str,
    order: tuple[int, ...],
) -> dict[str, object]:
    ranks = [
        rank
        for n in population
        if (rank := first_rank(n, order)) is not None
    ]
    return {
        "population": population_name,
        "population_size": len(population),
        "order": order_name,
        "candidate_count": len(order),
        "hittable": len(ranks),
        "mean_first_hit_rank": statistics.mean(ranks),
        "median_first_hit_rank": statistics.median(ranks),
        "p90_first_hit_rank": _p90(ranks),
        "top5_rate_given_hit": sum(rank <= 5 for rank in ranks) / len(ranks),
        "top10_rate_given_hit": sum(rank <= 10 for rank in ranks) / len(ranks),
    }


def benchmark_rows() -> list[dict[str, object]]:
    orders = {
        "structural": structural_order(100),
        "learned_prefix_then_fallback": learned_cover_order(100),
        "ratio_prefix_then_fallback": ratio_cover_order(100),
        "round_robin_structural_learned_q4": flatten_probe_batches(
            multiplier_probe_batches(max_multiplier=100, quantum=4)
        ),
        "round_robin_plus_ratio_q4": flatten_probe_batches(
            multiplier_probe_batches(
                max_multiplier=100,
                include_ratio_specialist=True,
                quantum=4,
            )
        ),
    }
    baseline_set = set(orders["structural"])
    if any(set(order) != baseline_set for order in orders.values()):
        raise AssertionError("portfolio order changed exact scan coverage")

    populations = (
        ("all_101_997", all_distinct_semiprimes(101, 997)),
        (
            "sample_1009_4999_seed_20260906",
            deterministic_semiprimes(1009, 4999, 20_000, SAMPLE_SEED),
        ),
    )
    return [
        summarize(pop_name, population, order_name, order)
        for pop_name, population in populations
        for order_name, order in orders.items()
    ]


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
        / "brc_opportunistic_shortcut_rank_probe_20260907.csv"
    )
    write_csv(target)
    print(target)
