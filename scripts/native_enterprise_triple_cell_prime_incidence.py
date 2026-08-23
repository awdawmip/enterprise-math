#!/usr/bin/env python3
"""Exact checker/census for native Enterprise triple-cell prime incidence.

The triangular carrier is used only for incidence adjacency. No carrier-Euclidean
metric is used as a native Enterprise length law.
"""

from __future__ import annotations

import argparse
import math
import statistics
from collections import Counter


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def label(r: int, t: int, sigma: int) -> int:
    return shell_base(r) + t + sigma * r


def incidence_labels(r: int, t: int, sigma: int, orient: str):
    n = label(r, t, sigma)
    if orient == "A":
        return (n, n + 3 * r + sigma, n + 6 * r + 4 + 2 * sigma)
    if orient == "B":
        return (n, n + 3 * r + 1 + sigma, n + 6 * r + 4 + 2 * sigma)
    raise ValueError(orient)


def predicted_word(orient: str, sigma: int):
    return {
        ("A", 0): (1, 1, 5),
        ("A", 1): (1, 5, 1),
        ("A", 2): (5, 1, 1),
        ("B", 0): (1, 5, 5),
        ("B", 1): (5, 1, 5),
        ("B", 2): (5, 5, 1),
    }[(orient, sigma)]


def decode_word(word):
    if any(x not in (1, 5) for x in word) or len(set(word)) == 1:
        raise ValueError(word)
    signs = [1 if x == 1 else -1 for x in word]
    prod = signs[0] * signs[1] * signs[2]
    if prod == -1:
        orient = "A"
        minority = signs.index(-1)
        sigma = (2 - minority) % 3
    else:
        orient = "B"
        minority = signs.index(1)
        sigma = minority
    return orient, sigma


def sieve(nmax: int) -> bytearray:
    prime = bytearray(b"\x01") * (nmax + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(nmax) + 1):
        if prime[p]:
            prime[p*p:nmax+1:p] = b"\x00" * (((nmax - p*p)//p) + 1)
    return prime


def run(rmax: int) -> None:
    max_label = max(
        max(incidence_labels(rmax, rmax - 1, sigma, orient))
        for sigma in range(3)
        for orient in ("A", "B")
    )
    prime = sieve(max_label)
    counts = Counter()
    violations = []

    for r in range(2, rmax + 1):
        for t in range(1, r):
            for sigma in range(3):
                for orient in ("A", "B"):
                    vals = incidence_labels(r, t, sigma, orient)
                    if all(prime[v] for v in vals):
                        key = f"{orient}{sigma}"
                        counts[key] += 1
                        if min(vals) > 3:
                            word = tuple(v % 6 for v in vals)
                            if word != predicted_word(orient, sigma):
                                violations.append((r, t, orient, sigma, vals, word))
                            if decode_word(word) != (orient, sigma):
                                violations.append(("decode", r, t, orient, sigma, word))

    ordered = {k: counts[k] for k in ("A0","A1","A2","B0","B1","B2")}
    values = list(ordered.values())
    cv = statistics.pstdev(values) / statistics.mean(values)

    print(f"RMAX={rmax}")
    print("COUNTS=" + ",".join(f"{k}:{v}" for k, v in ordered.items()))
    print(f"MEAN={statistics.mean(values):.12f}")
    print(f"C3xC2_CV={cv:.12f}")
    print(f"MOD6_CODE_VIOLATIONS={len(violations)}")

    for orient in ("A", "B"):
        for sigma in range(3):
            assert decode_word(predicted_word(orient, sigma)) == (orient, sigma)

    if rmax == 3000:
        assert ordered == {
            "A0": 2859, "A1": 2870, "A2": 2910,
            "B0": 2987, "B1": 2933, "B2": 2845,
        }
        assert not violations
        print("FROZEN_R3000_CENSUS=PASS")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-max", type=int, default=3000)
    args = ap.parse_args()
    run(args.r_max)
