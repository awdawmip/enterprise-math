#!/usr/bin/env python3
"""Exact-rational regression for the P017 near-half P2 parameter package.

This script verifies only rational algebra / Taylor-certificate inequalities.
It does not replace the analytic proofs in Iwaniec-Laborde and does not claim
an effective numerical threshold.
"""

from fractions import Fraction as Q
from math import factorial


def exp_partial(x: Q, n: int) -> Q:
    return sum((x ** k) / factorial(k) for k in range(n + 1))


def main() -> None:
    theta = Q(4999, 10000)
    a = Q(24, 5)
    b = Q(5, 2)
    c = Q(4)
    delta = 2 * c - b - 1
    total = b + c + 1
    d = a / total  # log D / log X

    assert total == Q(15, 2)
    assert d == Q(16, 25)
    assert 1 < b < c < a

    alpha = d / theta - 1
    assert alpha == Q(1401, 4999)

    z_exp = d / a
    low_exp = d * b / a
    w_exp = d * c / a
    assert z_exp == Q(2, 15)
    assert low_exp == Q(1, 3)
    assert w_exp == Q(8, 15)

    # Bilinear ceiling: D < X^(2 theta - 5/14), before the arbitrarily
    # small epsilon/delta losses in the paper.
    bilinear_gap = 2 * theta - Q(5, 14) - d
    assert bilinear_gap == Q(93, 35000) > 0

    # Lemma 6 geometry.
    d1_exp = (3 * theta - 1) / 2
    selberg_gap = 2 * z_exp - d1_exp
    assert selberg_gap == Q(1009, 60000) > 0
    assert theta - low_exp == Q(4997, 30000) > 0
    assert w_exp - theta == Q(1003, 30000) > 0
    assert Q(3, 2) * theta - w_exp == Q(12991, 60000) > 0

    # J1 < 49/100.
    # log(9/5) < 3/5 because exp(3/5) > 9/5.
    assert exp_partial(Q(3, 5), 3) == Q(227, 125) > Q(9, 5)
    # log(125/69) < 76/125 because exp(76/125) > 125/69.
    assert exp_partial(Q(76, 125), 3) > Q(125, 69)
    j1_bound = Q(1, 2) * Q(3, 5) + Q(5, 16) * Q(76, 125)
    assert j1_bound == Q(49, 100)

    # J2 = A+B.  First A < 13/100.
    # log(7/4) < 14/25 via the exponential series.
    assert exp_partial(Q(14, 25), 4) > Q(7, 4)
    u = Q(15, 76)
    log_61_76_upper = -(u + u**2 / 2 + u**3 / 3)
    a2_bound = Q(35, 48) * Q(14, 25) + Q(61, 48) * log_61_76_upper
    assert a2_bound == Q(13643573, 105354240) < Q(13, 100)

    # For B, log x <= (x-x^-1)/2 for x>=1 reduces B to
    # 1/4 - log(5/2)/6.  The atanh series gives log(5/2)>312/343>9/10.
    log_5_2_lower = 2 * (Q(3, 7) + (Q(3, 7) ** 3) / 3)
    assert log_5_2_lower == Q(312, 343) > Q(9, 10)
    b2_bound = Q(1, 4) - Q(1, 6) * Q(9, 10)
    assert b2_bound == Q(1, 10)
    j2_bound = Q(13, 100) + Q(1, 10)
    assert j2_bound == Q(23, 100)

    # J3 < 3/20 from elementary log series bounds.
    u1 = Q(1, 6)
    u2 = Q(11, 72)
    v = Q(11, 24)
    j3_bound = (
        Q(7, 36)
        + Q(2, 3) * (-(u1 + u1**2 / 2))
        + Q(35, 48) * (v - v**2 / 2 + v**3 / 3)
        + Q(61, 48) * (-(u2 + u2**2 / 2))
    )
    assert j3_bound == Q(96947, 663552) < Q(3, 20)

    # J4 < 21/100 because exp(63/50)>5103/1472.
    assert exp_partial(Q(63, 50), 4) > Q(5103, 1472)
    j4_bound = Q(21, 100)

    jsum = j1_bound + j2_bound + Q(3, 20) + j4_bound
    assert jsum == Q(27, 25)

    # With log(3)>1 and exp(-gamma)>1/2, the direct general W1 formula
    # gives coefficient > 12/125.
    w1_lower = Q(12, 125)

    # Lemma 6 coefficient after substituting z=D^(1/a), w=D^(c/a).
    A = c * d - a * theta
    assert A == Q(1003, 6250)
    w2 = 16 * A**2 / (a * delta * (3 * theta - 1) ** 2)
    assert w2 == Q(257538304, 3370951215)

    net = w1_lower - w2
    assert net == Q(1651825316, 84273780375) > 0

    print("P017 P2 near-half rational certificate: PASS")
    print("theta =", theta)
    print("D exponent =", d)
    print("bilinear exponent gap =", bilinear_gap)
    print("Selberg z^2 exponent gap =", selberg_gap)
    print("W1 coarse lower coefficient =", w1_lower)
    print("W2 coarse upper coefficient =", w2)
    print("net coarse coefficient >", net, "~=", float(net))


if __name__ == "__main__":
    main()
