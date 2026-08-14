#!/usr/bin/env python3
"""Exact rational certificate for ZERO_FREE_SECTOR_EXTENSION.md (V2)."""
from fractions import Fraction
from math import factorial

H = 3_000_000_000_000
R = Fraction(4_896, 1_000)  # 4.896
PI_LOWER = Fraction(31_415, 10_000)
RANK_CERT = 9_559_151_102_982
VERIFY_ONLY_CERT = 9_424_499_999_999


def main():
    e_partial = sum(Fraction(1, factorial(n)) for n in range(7))
    assert e_partial == Fraction(1957, 720)
    assert e_partial > Fraction(2718, 1000)
    assert Fraction(2718, 1000) ** 29 > H

    denom = Fraction(1) - Fraction(2) / (29 * R)
    rank_bound = PI_LOWER * H / denom

    expected = Fraction(83_633_013_000_000_000, 8_749)
    assert rank_bound == expected
    assert RANK_CERT + 1 <= rank_bound

    verification_only_bound = PI_LOWER * H
    assert VERIFY_ONLY_CERT + 1 <= verification_only_bound
    assert RANK_CERT - VERIFY_ONLY_CERT == 134_651_102_983

    print("V2 zero-free PF certificate: PASS")
    print("published verification height:", H)
    print("zero-free R:", float(R))
    print("certified PF rank:", RANK_CERT)
    print("conservative gain:", RANK_CERT - VERIFY_ONLY_CERT)
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
