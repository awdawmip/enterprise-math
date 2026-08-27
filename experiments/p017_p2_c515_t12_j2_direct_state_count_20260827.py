#!/usr/bin/env python3
"""Exact finite checker for the corrected c515 T1-T2 valuation-j=2 carrier.

The proof bypasses the 254-state inner Rosser sieve.  A j=2 residual state is
divisible by r^2 and can carry at most seven later distinct-prime residual
pairs.  Summing interval divisibility counts over the finite dangerous r-range
proves the whole j=2 residual penalty is < 3/25000 of the P(23)-anchored length.
"""

from fractions import Fraction as Q
from math import isqrt

K0 = 116_009_280_740_973_308
W = K0 + 1
Q23 = 223_092_870
L23 = Q23 * ((2 * K0) // Q23)
SCALE = 10**18
RMAX = 585_014


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def main() -> None:
    assert L23 == 232_018_561_402_828_200

    # z=W^(5/27) lies strictly between the consecutive primes 1439 and 1447.
    assert 1439**27 < W**5 < 1447**27

    # Dangerous least-prime range r<D^(73/240)=W^(73/216).
    assert RMAX**216 < W**73 < (RMAX + 1) ** 216

    rs = [p for p in primes_upto(RMAX) if p >= 1447]
    assert len(rs) == 47_735

    # Fixed-point upper bound for sum 1/r^2.
    reciprocal_square_upper = sum(
        (SCALE + p * p - 1) // (p * p) for p in rs
    )
    assert reciprocal_square_upper < Q(423, 5_000_000) * SCALE

    # A j=2 residual state has r^2, the second distinct prime q, and k later
    # distinct primes p. All are >=z=D^(1/6), while every basin state is <D^(9/5).
    # Thus z^(k+3)<D^(9/5), i.e. 5(k+3)<54, so k<=7.
    assert 5 * (7 + 3) < 54
    assert 5 * (8 + 3) > 54

    # Each r^2-divisibility hit count on an interval of length L23 is <=L23/r^2+1.
    hit_density = Q(423, 5_000_000) + Q(len(rs), L23)

    # Restore kappa<=73/80 and the source outside factor 1/Delta, Delta=93/20.
    normalized = Q(20, 93) * Q(73, 80) * 7 * hit_density
    assert normalized < Q(3, 25_000)

    print("P017 c515 T1-T2 j=2 direct-state certificate: PASS")
    print("dangerous r primes =", len(rs))
    print("sum 1/r^2 < 423/5000000")
    print("later residual-prime multiplicity <= 7")
    print("normalized upper ~=", float(normalized))
    print("certified < 3/25000 = 0.00012")


if __name__ == "__main__":
    main()
