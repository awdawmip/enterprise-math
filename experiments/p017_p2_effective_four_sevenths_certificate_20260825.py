#!/usr/bin/env python3
"""Exact-rational regression for the P017 four-sevenths P2 package."""

from fractions import Fraction as Q
from math import factorial


def exp_partial(x: Q, degree: int) -> Q:
    return sum((x**k) / factorial(k) for k in range(degree + 1))


def main() -> None:
    theta = Q(4999, 10000)
    d = Q(4, 7)
    a = Q(4)
    b = Q(5, 2)
    c = Q(7, 2)
    delta = 2 * c - b - 1

    assert b + c + 1 == Q(7) == a / d
    assert 1 < b < c < a
    assert d / a == Q(1, 7)
    assert d * b / a == Q(5, 14)
    assert d * c / a == Q(1, 2)

    bilinear_gap = 2 * theta - Q(5, 14) - d
    assert bilinear_gap == Q(2493, 35000) > 0

    selberg_gap = 2 * (d / a) - (3 * theta - 1) / 2
    assert selberg_gap == Q(5021, 140000) > 0
    assert Q(5, 14) < theta < Q(1, 2) < Q(3, 2) * theta

    # J1 < 41/100.
    assert exp_partial(Q(41, 25), 6) > Q(5)
    j1_upper = Q(41, 100)

    # J2 < 15/100.
    ratio2 = Q(8**8 * 3**7 * 5**5 * 7, 63**8)
    assert exp_partial(Q(6, 5), 6) > ratio2
    j2_upper = Q(15, 100)

    # J3 < 17/100.
    ratio3 = Q(3**9 * 7**7, 16**8)
    assert exp_partial(Q(34, 25), 6) > ratio3
    j3_upper = Q(17, 100)

    # J4 < 16/100.
    ratio4 = Q(5007 * 34993**7, 2**24 * 5**39 * 3)
    assert exp_partial(Q(32, 25), 6) > ratio4
    j4_upper = Q(16, 100)

    jsum_upper = j1_upper + j2_upper + j3_upper + j4_upper
    assert jsum_upper == Q(89, 100)

    log3_lower = 2 * (Q(1, 2) + Q(1, 2)**3 / 3 + Q(1, 2)**5 / 5)
    assert log3_lower > Q(109, 100)

    w1_lower = 2 * Q(109, 100) - (2 * a / delta) * jsum_upper
    assert w1_lower == Q(51, 350)

    mismatch = c * d - a * theta
    assert mismatch == Q(1, 2500)
    w2 = 16 * mismatch**2 / (a * delta * (3 * theta - 1)**2)
    assert w2 == Q(128, 174790063)

    net = w1_lower - w2
    assert net == Q(181923437, 1248500450) > 0

    print("P017 P2 four-sevenths rational certificate: PASS")
    print("bilinear exponent gap =", bilinear_gap)
    print("Lemma-6 z^2 exponent gap =", selberg_gap)
    print("W1 coarse lower coefficient =", w1_lower)
    print("W2 coarse upper coefficient =", w2)
    print("net coarse coefficient >", net, "~=", float(net))


if __name__ == "__main__":
    main()
