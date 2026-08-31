#!/usr/bin/env python3
"""12D prime-collapse residual / semicircle experiment.

This is an experimental collapse-tower audit. It does not assert a new
classical theorem. The normalized residual is compared against the known
semicircle/Sato-Tate density after the raw experiment is frozen.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

from highdim_prime_collapse_experiment_p5000 import sieve, support_spectrum, signed_completion


def semicircle_cdf(x: float) -> float:
    if x <= -1.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    return 0.5 + (x * math.sqrt(1.0 - x * x) + math.asin(x)) / math.pi


def ks_distance(values: list[float]) -> float:
    values = sorted(values)
    n = len(values)
    d_plus = max((i + 1) / n - semicircle_cdf(x) for i, x in enumerate(values))
    d_minus = max(semicircle_cdf(x) - i / n for i, x in enumerate(values))
    return max(d_plus, d_minus)


def moment(values: list[float], k: int) -> float:
    return sum(x**k for x in values) / len(values)


def run(nmax: int, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    is_prime = sieve(nmax)
    primes = [n for n in range(3, nmax + 1, 2) if is_prime[n]]
    A = support_spectrum(nmax, 12)

    rows = []
    values = []
    by_mod8 = {1: [], 3: [], 5: [], 7: []}

    for p in primes:
        r12 = signed_completion(A, 12, p)
        t = (r12 - 8 * (p**5 + 1)) / (32 * (p ** 2.5))
        if not (-1.000000000001 <= t <= 1.000000000001):
            raise AssertionError(("outside_unit_band", p, t))
        values.append(t)
        by_mod8[p % 8].append(t)
        rows.append({"prime": p, "p_mod8": p % 8, "R12": r12, "t12": format(t, ".17g")})

    csv_path = out / f"d12_semicircle_p{nmax}.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["prime", "p_mod8", "R12", "t12"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    mean = moment(values, 1)
    variance = moment(values, 2) - mean * mean
    print(f"ODD_PRIME_COUNT={len(values)}")
    print(f"MIN={min(values):.17g}")
    print(f"MAX={max(values):.17g}")
    print(f"MEAN={mean:.17g}")
    print(f"STD={math.sqrt(variance):.17g}")
    print(f"M2={moment(values, 2):.17g} TARGET=0.25")
    print(f"M4={moment(values, 4):.17g} TARGET=0.125")
    print(f"M6={moment(values, 6):.17g} TARGET=0.078125")
    print(f"KS_SEMICIRCLE={ks_distance(values):.17g}")
    for r in (1, 3, 5, 7):
        v = by_mod8[r]
        print(
            f"MOD8={r} N={len(v)} MEAN={moment(v,1):.12g} "
            f"STD={math.sqrt(moment(v,2)-moment(v,1)**2):.12g} "
            f"KS={ks_distance(v):.12g}"
        )
    print(f"CSV={csv_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5000)
    parser.add_argument("--out", type=Path, default=Path("highdim_prime_experiment_out"))
    args = parser.parse_args()
    run(args.max_n, args.out)
