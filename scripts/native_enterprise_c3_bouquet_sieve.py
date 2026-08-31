#!/usr/bin/env python3
"""Exact small-prime gate for the C3 equal-coordinate prime bouquet.

Bouquet:
    F-(m)=6m^2-2m+1
    F0(m)=6m^2+1
    F+(m)=6m^2+2m+1

For simultaneous primality beyond tiny exceptional values, m must be divisible
by 3, 5 and 7, hence by 105.  This script verifies the residue coverage and
optionally searches triple-prime events only on the surviving 105-wheel.
"""

from __future__ import annotations

import argparse

_MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
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
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def bouquet(m: int) -> tuple[int, int, int]:
    return (6*m*m - 2*m + 1, 6*m*m + 1, 6*m*m + 2*m + 1)


def roots(q: int):
    ans = []
    for k in range(3):
        rs = [m for m in range(q) if bouquet(m)[k] % q == 0]
        ans.append(rs)
    return ans


def run(limit: int) -> None:
    for q in (3, 5, 7):
        rs = roots(q)
        union = sorted(set().union(*map(set, rs)))
        expected = list(range(1, q))
        if union != expected:
            raise AssertionError((q, rs, union, expected))
        print(f"MOD_{q}_ROOTS={rs}; UNION_NONZERO={union}")

    triples = []
    for m in range(105, limit + 1, 105):
        vals = bouquet(m)
        if all(is_prime(v) for v in vals):
            triples.append((m, *vals))

    print(f"LIMIT={limit}")
    print(f"SURVIVING_105_MULTIPLES={limit // 105}")
    print(f"TRIPLE_PRIME_EVENTS={len(triples)}")
    for row in triples:
        print("TRIPLE", *row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    args = parser.parse_args()
    run(args.limit)
