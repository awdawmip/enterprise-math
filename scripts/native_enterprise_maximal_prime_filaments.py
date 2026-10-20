#!/usr/bin/env python3
"""Exact checker/census for maximal-prime native filaments."""

from __future__ import annotations

import argparse
import math
from collections import Counter


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def sieve(nmax: int) -> bytearray:
    p = bytearray(b"\x01") * (nmax + 1)
    p[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(nmax) + 1):
        if p[q]:
            p[q*q:nmax+1:q] = b"\x00" * (((nmax-q*q)//q)+1)
    return p


def is_maximal_flower(prime, r: int, t: int):
    sigma = 1
    n = shell_base(r) + r + t
    if not prime[n]:
        return None
    offsets = (
        3*r+1,
        6*r+6,
        3*r+2,
        -3*r+2,
        -6*r+6,
        -3*r+1,
    )
    nbr = [n+d for d in offsets]
    v = [bool(prime[x]) for x in nbr]
    if sum(v) != 4:
        return None
    edge = [int(v[i] and v[(i+1)%6]) for i in range(6)]
    if sum(edge) != 3:
        return None
    ps = tuple(sorted([n] + [nbr[i] for i,b in enumerate(v) if b]))
    return n, ps


def next_coord(r: int, t: int):
    return r+1, t+1 if r % 2 == 0 else t


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-max", type=int, default=10000)
    args = ap.parse_args()
    rmax = args.r_max

    prime = sieve(3*rmax*(rmax+1)//2 + 6*rmax + 20)
    flowers = {}

    for r in range(4, rmax+1):
        for t in range(2, r-1):
            got = is_maximal_flower(prime, r, t)
            if got is None:
                continue
            n, ps = got
            h = t - ((r+1)//2)
            assert h % 6 == 4
            assert ps[4]-ps[0] == 12*r
            flowers[(r,t)] = (n,ps,h)

    successor = {}
    for rt in flowers:
        nr = next_coord(*rt)
        if nr in flowers:
            assert flowers[nr][2] == flowers[rt][2]
            successor[rt] = nr

    targets = set(successor.values())
    starts = [rt for rt in flowers if rt not in targets]
    lengths = Counter()

    for start in starts:
        u = start
        L = 1
        while u in successor:
            u = successor[u]
            L += 1
        lengths[L] += 1

    print(f"RMAX={rmax}")
    print(f"MAXIMAL_FLOWERS={len(flowers)}")
    print("TRANSVERSE_CLASS=h=4 mod 6 PASS")
    print(f"CHAIN_LENGTHS={dict(sorted(lengths.items()))}")

    if rmax == 10000:
        assert len(flowers) == 1157
        assert lengths == Counter({1:822, 2:132, 3:17, 4:5})
        print("FROZEN_R10000_CENSUS=PASS")


if __name__ == "__main__":
    main()
