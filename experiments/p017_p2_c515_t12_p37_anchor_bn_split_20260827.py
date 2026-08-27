#!/usr/bin/env python3
"""Exact checker for the c515 P(37) anchor and B x N pair split."""

from fractions import Fraction as Q

K = 116_009_280_740_973_308
W = K + 1
Q37 = 7_420_738_134_810


def main() -> None:
    L37 = Q37 * ((2 * K) // Q37)
    tail = 2 * K - L37
    assert (2 * K) // Q37 == 31_266
    assert L37 == 232_016_640_662_977_460
    assert tail == 1_762_958_977_156
    assert 0 <= tail < Q37
    assert K < L37 < 2 * K
    assert Q(tail, 2 * K) < Q(76, 10_000_000)

    # D^(2/3)=W^(20/27): hard primes >=41 and depth <=7.
    assert 41 ** 216 > W ** 20
    assert 41 ** 189 < W ** 20

    # c515 exact B*N exponent split in x=W^2 coordinates.
    assert Q(5, 9) - Q(31, 72) == Q(1, 8)

    # At the splice N0=x^(1/8)=W^(1/4), so 23^3<N0<29^3.
    assert 23 ** 12 < W
    assert 29 ** 12 > W

    print("P017 c515 P37 anchor / BxN split checker: PASS")
    print("relative P37 tail < 7.6e-6")
    print("hard primes >=41; hard omega<=7")
    print("B=x^(31/72), N0=x^(1/8), B*N0=D=x^(5/9)")
    print("high-pair inner upper-sieve primes <=23")


if __name__ == "__main__":
    main()
