#!/usr/bin/env python3
"""Exact regression for RS-ABC-ENTERPRISE-CAPPED-CORE-ENERGY.

Load-bearing checks use integer inequalities only. Logarithms are not needed.
"""
from __future__ import annotations
import argparse
import math
from typing import NamedTuple

class ExactData(NamedTuple):
    a: int
    b: int
    c: int
    rad: int
    height: int
    cap2: int
    surplus2: int

def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def exact_data(a: int, b: int) -> ExactData:
    c = a + b
    if math.gcd(a, b) != 1:
        raise ValueError("triple must be primitive")
    exponents: dict[int, int] = {}
    for n in (a, b, c):
        for p, e in factor(n).items():
            exponents[p] = exponents.get(p, 0) + e
    rad = height = cap2 = surplus2 = 1
    for p, e in exponents.items():
        rad *= p
        height *= p ** (e - 1)
        cap2 *= p ** min(e - 1, 2)
        surplus2 *= p ** max(e - 3, 0)
    assert height == cap2 * surplus2
    assert rad * height == a * b * c
    return ExactData(a, b, c, rad, height, cap2, surplus2)

def scan(limit: int):
    checked = 0
    first_boundary_failure = None
    first_height_failure = None
    for c in range(3, limit + 1):
        for a in range(1, c // 2 + 1):
            b = c - a
            if math.gcd(a, b) != 1:
                continue
            d = exact_data(a, b)
            checked += 1
            # I_2 <= 2R, exponentiated.
            assert d.cap2 <= d.rad * d.rad
            # I_2 + beta + log 4 <= 2R, beta=log(c^2/(4ab)).
            if first_boundary_failure is None and d.cap2 * c * c > d.rad * d.rad * a * b:
                first_boundary_failure = d
            # H <= 2R.
            if first_height_failure is None and d.height > d.rad * d.rad:
                first_height_failure = d
    return checked, first_boundary_failure, first_height_failure

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=5000)
    args = ap.parse_args()
    checked, bf, hf = scan(args.limit)
    print(f"primitive_unordered_triples_checked={checked}")
    print("raw_cap2_failures=0")
    print(f"first_boundary_paid_coeff2_failure={bf}")
    print(f"first_full_height_coeff2_failure={hf}")
    if args.limit >= 81:
        assert bf == ExactData(1, 8, 9, 6, 12, 12, 1)
        assert hf == ExactData(32, 49, 81, 42, 3024, 252, 12)
        assert 12 * 9 * 9 > 6 * 6 * 1 * 8  # 972 > 288
        assert 3024 > 42 * 42               # 3024 > 1764
        print("regression=PASS")

if __name__ == "__main__":
    main()
