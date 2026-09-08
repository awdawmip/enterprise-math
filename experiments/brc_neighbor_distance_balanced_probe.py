"""Finite balanced-semiprime diagnostic for radius-64 distance compression."""
from __future__ import annotations

import csv
from math import gcd, isqrt
from pathlib import Path
import random

from enterprise_math.brc_multiplier_priority_jump import (
    prioritized_odd_multiplier_order,
)
from enterprise_math.brc_neighbor_square_lift_shortcut import (
    compressed_power2_neighbor_distance_candidates,
    probe_neighbor_distance_square_lift,
)

SAMPLES = 20_000
HORIZON = 100
DISTANCE = 64


def _primes_between(low: int, high: int) -> tuple[int, ...]:
    sieve = bytearray(b"\x01") * (high + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(high) + 1):
        if not sieve[p]:
            continue
        start = p * p
        sieve[start : high + 1 : p] = b"\x00" * (((high - start) // p) + 1)
    return tuple(p for p in range(low, high + 1) if sieve[p])


def _is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _random_prime(bits: int, rng: random.Random) -> int:
    while True:
        candidate = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        if _is_prime_64(candidate):
            return candidate


def _sample_from_pool(
    pool: tuple[int, ...], count: int, seed: int
) -> tuple[tuple[int, int, int], ...]:
    rng = random.Random(seed)
    out = []
    for _ in range(count):
        p, q = rng.sample(pool, 2)
        if p > q:
            p, q = q, p
        out.append((p * q, p, q))
    return tuple(out)


def _sample_random_bits(
    bits: int, count: int, seed: int
) -> tuple[tuple[int, int, int], ...]:
    rng = random.Random(seed)
    out = []
    for _ in range(count):
        p = _random_prime(bits, rng)
        q = _random_prime(bits, rng)
        while q == p:
            q = _random_prime(bits, rng)
        if p > q:
            p, q = q, p
        out.append((p * q, p, q))
    return tuple(out)


def _m100_factor(n: int) -> int | None:
    for multiplier in prioritized_odd_multiplier_order(HORIZON):
        target = multiplier * n
        floor_root = isqrt(target)
        ceiling_root = floor_root if floor_root * floor_root == target else floor_root + 1
        gap = ceiling_root * ceiling_root - target
        gap_root = isqrt(gap)
        if gap_root * gap_root != gap:
            continue
        factor = gcd(ceiling_root - gap_root, n)
        if not 1 < factor < n:
            factor = gcd(ceiling_root + gap_root, n)
        if 1 < factor < n:
            return factor
    return None


def _measure(
    name: str,
    source: str,
    values: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    triggers = factor_hits = incremental = 0
    for n, _, _ in values:
        candidates = compressed_power2_neighbor_distance_candidates(
            n,
            ordinary_horizon=HORIZON,
            max_distance=DISTANCE,
            all_levels=False,
        )
        triggers += len(candidates)
        for distance, epsilon, a, _ in candidates:
            probe = probe_neighbor_distance_square_lift(
                n, a, distance, epsilon
            )
            if not probe.factor_hit:
                continue
            factor_hits += 1
            incremental += int(_m100_factor(n) is None)
    return {
        "cohort": name,
        "prime_source": source,
        "samples": len(values),
        "ordinary_horizon": HORIZON,
        "max_distance": DISTANCE,
        "triggers": triggers,
        "factor_hits": factor_hits,
        "incremental_vs_m_le_100": incremental,
    }


def rows() -> list[dict[str, object]]:
    pool_a = _primes_between(1009, 4999)
    pool_b = _primes_between(10007, 50000)
    return [
        _measure(
            "A",
            "primes_1009_4999",
            _sample_from_pool(pool_a, SAMPLES, 20260908),
        ),
        _measure(
            "B",
            "primes_10007_50000",
            _sample_from_pool(pool_b, SAMPLES, 2026090802),
        ),
        _measure(
            "C",
            "random_24bit_primes",
            _sample_random_bits(24, SAMPLES, 123),
        ),
    ]


def write_csv(path: str | Path) -> None:
    data = rows()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    write_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_neighbor_distance_balanced_probe_20260908.csv"
    )
