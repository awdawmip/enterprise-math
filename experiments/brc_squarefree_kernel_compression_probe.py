"""Finite falsification probe for squarefree-kernel multiplier compression.

Question: can a small set of squarefree kernels d, with all multipliers m=a^2*d
through m<=1000, replace the full odd-N mod-8 representative multiplier set?

Training uses all distinct semiprimes p*q with 101<=p<q<=997.  Kernels are
selected greedily by training coverage.  Two larger disjoint prime ranges are
then used only for validation.  The factor test is the classical immediate
multiplier-Fermat square-gap witness.
"""

from __future__ import annotations

import csv
import random
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path

MAX_MULTIPLIER = 1000
TRAIN_KERNELS_EXPECTED = (1, 13, 14, 3, 15, 2, 5, 6, 30, 22, 105, 33, 7)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def squarefree_kernel(value: int) -> int:
    remaining = value
    kernel = 1
    p = 2
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent % 2:
            kernel *= p
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        kernel *= remaining
    return kernel


def representative_multipliers(limit: int = MAX_MULTIPLIER) -> tuple[int, ...]:
    return tuple(m for m in range(1, limit + 1) if m % 8 in (0, 1, 3, 5, 7))


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


def all_distinct_pairs(primes: list[int]) -> list[int]:
    return [primes[i] * primes[j] for i in range(len(primes)) for j in range(i + 1, len(primes))]


def deterministic_pairs(primes: list[int], count: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    chosen: set[tuple[int, int]] = set()
    while len(chosen) < count:
        i = rng.randrange(len(primes) - 1)
        j = rng.randrange(i + 1, len(primes))
        chosen.add((i, j))
    return [primes[i] * primes[j] for i, j in chosen]


def greedy_training_kernels(training: list[int], multipliers: tuple[int, ...]) -> tuple[int, ...]:
    kernels = sorted({squarefree_kernel(m) for m in multipliers})
    coverage: dict[int, set[int]] = {kernel: set() for kernel in kernels}
    for index, n in enumerate(training):
        for m in multipliers:
            if immediate_factor_success(n, m):
                coverage[squarefree_kernel(m)].add(index)

    remaining = set(range(len(training)))
    selected: list[int] = []
    while remaining:
        kernel = max(kernels, key=lambda d: (len(coverage[d] & remaining), -d))
        gain = coverage[kernel] & remaining
        if not gain:
            break
        selected.append(kernel)
        remaining -= gain
    return tuple(selected)


def hit_count(population: list[int], multipliers: tuple[int, ...]) -> int:
    return sum(any(immediate_factor_success(n, m) for m in multipliers) for n in population)


def benchmark_rows() -> tuple[list[dict[str, object]], tuple[int, ...]]:
    reps = representative_multipliers()
    train_primes = [p for p in primes_up_to(997) if p >= 101]
    training = all_distinct_pairs(train_primes)
    selected_kernels = greedy_training_kernels(training, reps)

    selected_set = set(selected_kernels)
    selected_multipliers = tuple(m for m in reps if squarefree_kernel(m) in selected_set)

    val_a_primes = [p for p in primes_up_to(4999) if p >= 1009]
    val_b_primes = [p for p in primes_up_to(19997) if p >= 5003]
    populations = (
        ("train_all_101_997", training),
        ("validation_1009_4999_seed_20260906", deterministic_pairs(val_a_primes, 20_000, 20260906)),
        ("validation_5003_19997_seed_20260907", deterministic_pairs(val_b_primes, 30_000, 20260907)),
    )

    rows: list[dict[str, object]] = []
    for name, population in populations:
        full = hit_count(population, reps)
        selected = hit_count(population, selected_multipliers)
        rows.append(
            {
                "population": name,
                "population_size": len(population),
                "full_representative_multipliers": len(reps),
                "selected_kernel_count": len(selected_kernels),
                "selected_multiplier_count": len(selected_multipliers),
                "full_hittable": full,
                "selected_hittable": selected,
                "selected_rate_all": selected / len(population),
                "selected_rate_given_full_hit": selected / full if full else 0.0,
            }
        )
    return rows, selected_kernels


def write_csv(path: str | Path) -> None:
    rows, kernels = benchmark_rows()
    if kernels != TRAIN_KERNELS_EXPECTED:
        raise AssertionError(f"training kernel order drifted: {kernels}")
    output = Path(path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    target = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_squarefree_kernel_compression_probe_20260907.csv"
    )
    write_csv(target)
    print(target)
