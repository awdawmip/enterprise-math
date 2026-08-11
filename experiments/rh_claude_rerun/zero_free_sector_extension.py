#!/usr/bin/env python3
"""Exact rational certificate for the zero-free-region PF-order extension.

The mathematical use of Schoenberg's sector theorem and the published zeta
zero-free region is documented in ZERO_FREE_SECTOR_EXTENSION.md. This script
checks only the conservative arithmetic reductions.
"""
from fractions import Fraction
from math import factorial

H = 3_000_175_332_800
R = Fraction(5_558_691, 1_000_000)
PI_LOWER = Fraction(31_415, 10_000)
RANK_CERT = 9_543_454_452_405


def main():
    # e > sum_{n=0}^6 1/n! = 1957/720 > 2.718.
    e_partial = sum(Fraction(1, factorial(n)) for n in range(7))
    assert e_partial == Fraction(1957, 720)
    assert e_partial > Fraction(2718, 1000)

    # Hence e^29 > 2.718^29 > H, so log H < 29.
    assert Fraction(2718, 1000) ** 29 > H

    # Conservative angular envelope:
    # theta_H < (1 - 2/(29R))/H.
    denom = Fraction(1) - Fraction(2, 1) / (29 * R)
    rank_bound = PI_LOWER * H / denom

    expected = Fraction(7_596_687_039_633_894_670_284, 796_010_195)
    assert rank_bound == expected
    assert Fraction(RANK_CERT + 1) <= rank_bound

    print("log-bound rational certificate: PASS")
    print("rank-bound rational certificate: PASS")
    print("certified PF rank lower bound:", RANK_CERT)
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
