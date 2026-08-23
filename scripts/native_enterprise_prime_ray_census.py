#!/usr/bin/env python3
"""Cyclic ray-polynomial census for the Enterprise tri-sector allocation.

For a primitive S12 ray (u,v,0), gcd(u,v)=1, and m>=1, the fixed
tri-sector shell spiral sends the three cyclic rotations to quadratic labels

  F0(m) = B_{(u+v)m} + v m
  F1(m) = F0(m) + (u+v)m
  F2(m) = F0(m) + 2(u+v)m,

where B_r = 3r(r-1)/2 + 1.

This script enumerates primitive rays of bounded coordinate complexity and
measures prime rate plus C3 imbalance.  Placement is fixed before primality
is tested; this is an exploration statistic, not a theorem of infinitude.
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path


# Deterministic Miller-Rabin for unsigned 64-bit integers.
_MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in _MR_BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def label(u: int, v: int, cyclic_slot: int, m: int) -> int:
    s = u + v
    r = s * m
    base = 3 * r * (r - 1) // 2 + 1
    return base + (cyclic_slot * s + v) * m


def census(max_sum: int, samples: int):
    rows = []
    for u in range(max_sum + 1):
        for v in range(max_sum + 1 - u):
            if u == v == 0 or math.gcd(u, v) != 1:
                continue
            counts = []
            rates = []
            for k in range(3):
                c = sum(is_prime(label(u, v, k, m)) for m in range(1, samples + 1))
                counts.append(c)
                rates.append(c / samples)
            mean = statistics.mean(rates)
            cv = statistics.pstdev(rates) / mean if mean else 0.0
            rows.append({
                "u": u,
                "v": v,
                "complexity_u_plus_v": u + v,
                "samples_per_slot": samples,
                "slot0_prime_count": counts[0],
                "slot1_prime_count": counts[1],
                "slot2_prime_count": counts[2],
                "slot0_rate": rates[0],
                "slot1_rate": rates[1],
                "slot2_rate": rates[2],
                "mean_rate": mean,
                "c3_cv": cv,
            })
    return rows


def run(max_sum: int, samples: int, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    rows = census(max_sum, samples)
    rows.sort(key=lambda r: (-r["mean_rate"], r["c3_cv"], r["complexity_u_plus_v"]))
    path = out / f"ray_census_sum{max_sum}_m{samples}.csv"
    fields = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    balanced = [r for r in rows if r["c3_cv"] < 0.1]
    balanced.sort(key=lambda r: (-r["mean_rate"], r["c3_cv"], r["complexity_u_plus_v"]))
    best = balanced[0] if balanced else None
    print(f"RAYS={len(rows)}")
    print(f"CSV={path}")
    if best:
        print(
            "BEST_C3_BALANCED="
            f"(u,v)=({best['u']},{best['v']}),"
            f"counts={best['slot0_prime_count']}/{best['slot1_prime_count']}/{best['slot2_prime_count']},"
            f"mean={best['mean_rate']:.12f},cv={best['c3_cv']:.12f}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-sum", type=int, default=10)
    parser.add_argument("--samples", type=int, default=1500)
    parser.add_argument("--out", type=Path, default=Path("native_enterprise_ray_out"))
    args = parser.parse_args()
    run(args.max_sum, args.samples, args.out)
