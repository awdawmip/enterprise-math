#!/usr/bin/env python3
"""Exact integer/rational checker for the preferred c515 global P(41) anchor."""

from fractions import Fraction as Q

K = 116_009_280_740_973_308
W = K + 1
Q41 = 304_250_263_527_210
Q43 = 13_082_761_331_670_030


def main() -> None:
    L41 = Q41 * ((2 * K) // Q41)
    tail41 = 2 * K - L41

    assert (2 * K) // Q41 == 762
    assert L41 == 231_838_700_807_734_020
    assert tail41 == 179_860_674_212_596
    assert K < L41 < 2 * K
    assert 0 <= tail41 < Q41
    assert Q(tail41, 2 * K) < Q(776, 1_000_000)

    # D^(2/3)=W^(20/27).  Eight hard primes >=43 are impossible.
    assert 43 ** 216 > W ** 20
    assert 43 ** 189 < W ** 20

    # P43 fits, but does not improve the depth class.
    L43 = Q43 * ((2 * K) // Q43)
    tail43 = 2 * K - L43
    assert Q43 < K
    assert Q(tail43, 2 * K) > Q(41, 1000)
    assert 47 ** 189 < W ** 20
    assert 47 ** 216 > W ** 20

    print("P017 c515 preferred P41 anchor checker: PASS")
    print("L41 =", L41)
    print("relative tail < 0.000776")
    print("hard primes >=43; omega(hard)<=7")
    print("P43 costs >4.1% interval but leaves the same depth class")


if __name__ == "__main__":
    main()
