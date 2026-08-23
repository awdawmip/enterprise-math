#!/usr/bin/env python3
"""Exact checker for maximal five-prime flower self-localization."""

from __future__ import annotations

import argparse
import math
from collections import Counter


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def label(r: int, t: int, sigma: int) -> int:
    return shell_base(r) + t + sigma * r


def sieve(nmax: int) -> bytearray:
    p = bytearray(b"\x01") * (nmax + 1)
    p[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(nmax) + 1):
        if p[q]:
            p[q*q:nmax+1:q] = b"\x00" * (((nmax-q*q)//q)+1)
    return p


def neighbors(r: int, n: int, sigma: int):
    offsets = (
        3*r+sigma,
        6*r+4+2*sigma,
        3*r+1+sigma,
        -3*r+3-sigma,
        -6*r+8-2*sigma,
        -3*r+2-sigma,
    )
    return [n+d for d in offsets]


def expected_gap_word(r: int):
    if r % 2 == 0:
        return [3*r-4, 3*r-2, 3*r+2, 3*r+4]
    return [3*r-5, 3*r-1, 3*r+1, 3*r+5]


def census(rmax: int):
    max_n = 3 * rmax * (rmax + 1) // 2 + 6 * rmax + 20
    prime = sieve(max_n)
    counts = Counter()
    events = 0

    for sigma in range(3):
        for r in range(4, rmax + 1):
            base = shell_base(r) + sigma * r
            for t in range(2, r - 1):
                n = base + t
                if not prime[n]:
                    continue
                nbr = neighbors(r, n, sigma)
                v = [bool(prime[x]) for x in nbr]
                if sum(v) != 4:
                    continue
                edge = [int(v[i] and v[(i+1)%6]) for i in range(6)]
                if sum(edge) != 3:
                    continue

                ps = sorted([n] + [nbr[i] for i,b in enumerate(v) if b])
                assert len(ps) == 5
                assert ps[2] == n
                assert ps[4] - ps[0] == 12 * r
                assert ps[0] - 2 * ps[2] + ps[4] == 12
                inner = ps[1] - 2 * ps[2] + ps[3]
                assert inner == (4 if r % 2 == 0 else 2)
                gaps = [ps[i+1] - ps[i] for i in range(4)]
                assert gaps == expected_gap_word(r)
                assert (ps[4] - ps[0]) // 12 == r

                counts[(r % 2, inner)] += 1
                events += 1

    return events, counts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-max", type=int, default=5000)
    args = ap.parse_args()

    events, counts = census(args.r_max)
    print(f"RMAX={args.r_max}")
    print(f"MAXIMAL_FIVE_PRIME_FLOWERS={events}")
    print(f"PARITY_INNER_CURVATURE_COUNTS={dict(counts)}")
    print("SHELL_RECOVERY_FROM_PRIME_DIAMETER=PASS")
    print("OUTER_CURVATURE_12=PASS")
    print("INNER_CURVATURE_2_OR_4=PASS")

    if args.r_max == 5000:
        assert events == 400
        assert counts[(0,4)] == 219
        assert counts[(1,2)] == 181
        print("FROZEN_R5000_CENSUS=PASS")


if __name__ == "__main__":
    main()
