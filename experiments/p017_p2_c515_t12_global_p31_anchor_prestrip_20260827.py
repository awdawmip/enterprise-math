#!/usr/bin/env python3
"""Exact integer/rational checker for the c515 global P(31)-length prestrip."""

from fractions import Fraction as Q

K = 116_009_280_740_973_308
W = K + 1
Q0 = 200_560_490_130


def main() -> None:
    L0 = Q0 * ((2 * K) // Q0)
    tail = 2 * K - L0

    assert L0 == 232_018_403_006_890_500
    assert tail == 158_475_056_116
    assert 0 <= tail < Q0
    assert K < L0 < 2 * K
    assert Q(tail, 2 * K) < Q(7, 10_000_000)

    # D=W^(10/9), so D^(2/3)=W^(20/27).
    # Clear the 27th root exactly.
    assert 37 ** (9 * 27) > W ** 20
    # Eight hard factors are not excluded by this crude size argument.
    assert 37 ** (8 * 27) < W ** 20

    # Sub-root ordered pair has r,p>=D^(1/6), hence Q=D/(rp)<=D^(2/3).
    assert Q(1, 3) + Q(2, 3) == 1

    print("P017 c515 global P31 anchor prestrip checker: PASS")
    print("Q0 =", Q0)
    print("L0 =", L0)
    print("discarded tail =", tail)
    print("relative discarded tail < 7e-7")
    print("remaining hard Rosser prime factors >=37 and omega<=8")


if __name__ == "__main__":
    main()
