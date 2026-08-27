#!/usr/bin/env python3
"""Exact seventh-order Bonferroni certificate for the c515 base rough count.

On the P(23)-anchored interval, count odd states and sieve only by the 227 odd
primes 3..1439.  Every odd squarefree modulus has a one-unit arithmetic-
progression carry, so the seventh-order Bonferroni truncation gives a fully
finite lower bound with no fundamental-lemma or Mertens error.
"""

from fractions import Fraction as Q
from math import comb, isqrt

L23 = 232_018_561_402_828_200


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def main() -> None:
    primes = [p for p in primes_upto(1439) if p >= 3]
    assert len(primes) == 227

    # Exact elementary symmetric sums of {1/p} through degree seven.
    e = [Q(0) for _ in range(8)]
    e[0] = Q(1)
    for p in primes:
        x = Q(1, p)
        for j in range(7, 0, -1):
            e[j] += e[j - 1] * x

    bonferroni7 = sum((-1) ** j * e[j] for j in range(8))
    main_density = bonferroni7 / 2

    # The degree-zero odd population is exact on an even-length interval.
    # Every nonzero squarefree odd modulus contributes carry of magnitude <1.
    carry_terms = sum(comb(227, j) for j in range(1, 8))
    assert carry_terms == 5_795_560_160_583

    lower_density = main_density - Q(carry_terms, L23)
    assert lower_density > Q(3839, 50_000)  # 0.07678

    print("P017 c515 base odd Bonferroni-7 certificate: PASS")
    print("odd sieve primes =", len(primes))
    print("seventh-order main density ~=", float(main_density))
    print("carry density <", float(Q(carry_terms, L23)))
    print("finite rough-count density >", float(Q(3839, 50_000)))


if __name__ == "__main__":
    main()
