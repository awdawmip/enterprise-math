"""Exact finite atlas for R005-B prime/collapse experiments.

All truth values are integer-exact. ``carry_limit`` bounds only the displayed
modulus window; each displayed carry is exact for its modulus.
"""

import argparse
import json
from collections import Counter

from enterprise_math.legendre import is_prime
from enterprise_math.prime_collapse_field import (
    factor_horizon,
    interior_width,
    interior_width_carry,
    polynomial_carry,
)


def big_omega(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    count = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            count += 1
            n //= factor
        factor += 1
    if n > 1:
        count += 1
    return count


def basin_record(k: int, power: int, carry_limit: int = 24) -> dict[str, object]:
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    if carry_limit < 1:
        raise ValueError("carry_limit must be positive")

    lower = k**power
    upper = (k + 1) ** power
    horizon = factor_horizon(k, power)
    primes = [n for n in range(lower + 1, upper) if is_prime(n)]
    offsets = [q - lower for q in primes]
    gaps = [b - a for a, b in zip(primes, primes[1:])]
    factor_depth = Counter(big_omega(n) for n in range(lower + 1, upper))
    center2 = lower + upper
    prime_set = set(primes)
    symmetric_pairs = []
    for q in primes:
        mate = center2 - q
        if q < mate < upper and mate in prime_set:
            symmetric_pairs.append([q, mate])

    modulus_stop = min(horizon, carry_limit)
    carry_signature = [
        {
            "d": d,
            "width_carry": interior_width_carry(k, d, power),
            "polynomial_carry": polynomial_carry(k, d, power),
        }
        for d in range(1, modulus_stop + 1)
    ]

    return {
        "power": power,
        "k": k,
        "lower": lower,
        "upper": upper,
        "interior_width": interior_width(k, power),
        "factor_horizon": horizon,
        "factor_horizon_mismatch": horizon - k,
        "prime_count": len(primes),
        "prime_offsets": offsets,
        "first_prime_offset": offsets[0] if offsets else None,
        "last_prime_offset": offsets[-1] if offsets else None,
        "max_internal_prime_gap": max(gaps) if gaps else None,
        "factor_depth_histogram": dict(sorted(factor_depth.items())),
        "center_twice": center2,
        "symmetric_prime_pairs": symmetric_pairs,
        "carry_modulus_complete_through": modulus_stop,
        "carry_signature": carry_signature,
    }


def build_atlas(k_max: int = 3, carry_limit: int = 24) -> list[dict[str, object]]:
    if k_max < 1:
        raise ValueError("k_max must be positive")
    return [
        basin_record(k, power, carry_limit)
        for power in range(2, 9)
        for k in range(1, k_max + 1)
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-max", type=int, default=3)
    parser.add_argument("--carry-limit", type=int, default=24)
    args = parser.parse_args()
    print(json.dumps(build_atlas(args.k_max, args.carry_limit), indent=2))


if __name__ == "__main__":
    main()
