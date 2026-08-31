#!/usr/bin/env python3
"""Exact checker for the native Enterprise 13-state prime-incidence loop code."""

from __future__ import annotations

import argparse
import math
from collections import Counter


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def center_label(r: int, t: int, sigma: int) -> int:
    return shell_base(r) + t + sigma * r


def sieve(nmax: int) -> bytearray:
    p = bytearray(b"\x01") * (nmax + 1)
    p[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(nmax) + 1):
        if p[q]:
            p[q*q:nmax+1:q] = b"\x00" * (((nmax-q*q)//q)+1)
    return p


def maximal_residue_mask(rmod: int, nmod: int, sigma: int):
    nbr = [
        (nmod + 3*rmod + sigma) % 6,
        (nmod + 6*rmod + 4 + 2*sigma) % 6,
        (nmod + 3*rmod + 1 + sigma) % 6,
        (nmod - 3*rmod + 3 - sigma) % 6,
        (nmod - 6*rmod + 8 - 2*sigma) % 6,
        (nmod - 3*rmod + 2 - sigma) % 6,
    ]
    e = [x in (1,5) for x in nbr]
    return (
        int(e[0] and e[1]),
        int(e[1] and e[2]),
        int(e[2] and e[3]),
        int(e[3] and e[4]),
        int(e[4] and e[5]),
        int(e[5] and e[0]),
    )


def theoretical_code():
    upper = {
        maximal_residue_mask(r, n, s)
        for s in range(3)
        for r in range(6)
        for n in (1,5)
    }
    candidates = set()
    for mask in upper:
        idx = [i for i,b in enumerate(mask) if b]
        for sub in range(1 << len(idx)):
            out = [0]*6
            for j,i in enumerate(idx):
                out[i] = (sub >> j) & 1
            candidates.add(tuple(out))

    # Exact shared-neighbor closure: loop bits are edge-ANDs of one C6 vertex word.
    realizable = set()
    for vmask in range(64):
        v = [(vmask >> i) & 1 for i in range(6)]
        e = tuple(v[i] & v[(i+1)%6] for i in range(6))
        if e in candidates:
            realizable.add(e)
    return realizable


def census(rmax: int):
    max_center = max(center_label(rmax, rmax-2, s) for s in range(3))
    prime = sieve(max_center + 6*rmax + 8)
    counts = Counter()

    for sigma in range(3):
        for r in range(4, rmax+1):
            base = shell_base(r) + sigma*r
            for t in range(2, r-1):
                n = base + t
                if not prime[n]:
                    bits = (0,0,0,0,0,0)
                else:
                    E  = bool(prime[n+3*r+sigma])
                    NE = bool(prime[n+6*r+4+2*sigma])
                    N  = bool(prime[n+3*r+1+sigma])
                    W  = bool(prime[n-3*r+3-sigma])
                    SW = bool(prime[n-6*r+8-2*sigma])
                    S  = bool(prime[n-3*r+2-sigma])
                    bits = (
                        int(E and NE), int(NE and N), int(N and W),
                        int(W and SW), int(SW and S), int(S and E),
                    )
                counts[bits] += 1
    return counts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-max", type=int, default=1500)
    args = ap.parse_args()

    code = theoretical_code()
    expected_code = {
        tuple(map(int,s)) for s in (
            "000000","000001","000010","000100","001000","010000","100000",
            "000011","001100","011000","100001","011100","100011"
        )
    }
    assert code == expected_code
    assert max(sum(x) for x in code) == 3

    counts = census(args.r_max)
    assert set(counts) <= code

    print("THEORETICAL_LOOP_CODE_SIZE=13")
    print("MAX_BRIGHT_VERTICES_PER_CELL=3")
    print("OBSERVED_SIGNATURES=" + str(len(counts)))
    for sig in sorted(counts, key=lambda x:(sum(x),x)):
        print("".join(map(str,sig)), counts[sig])

    if args.r_max == 1500:
        expected = {
            "000000":3347973,"000001":2144,"000010":2492,"000100":2507,
            "001000":2126,"010000":2510,"100000":2482,"000011":366,
            "001100":360,"011000":355,"100001":370,"011100":42,"100011":32,
        }
        assert {"".join(map(str,k)):v for k,v in counts.items()} == expected
        print("FROZEN_R1500_CENSUS=PASS")


if __name__ == "__main__":
    main()
