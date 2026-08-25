#!/usr/bin/env python3
"""Exact-rational regression for the P017 five-ninth P2 effectivity package.

This verifies only rational parameter identities and Taylor-series comparison
certificates. It is not a substitute for the analytic Iwaniec-Laborde proof
and does not claim an explicit numerical threshold.
"""

from fractions import Fraction as Q
from math import factorial


def exp_partial(x: Q, degree: int) -> Q:
    return sum((x**k) / factorial(k) for k in range(degree + 1))


def main() -> None:
    theta = Q(4999, 10000)
    d = Q(5, 9)
    a = Q(4)
    b = Q(13, 5)
    c = Q(18, 5)
    delta = 2 * c - b - 1

    assert b + c + 1 == Q(36, 5) == a / d
    assert 1 < b < c < a
    assert delta == Q(18, 5)

    z_exp = d / a
    low_exp = d * b / a
    w_exp = d * c / a
    assert z_exp == Q(5, 36)
    assert low_exp == Q(13, 36)
    assert w_exp == Q(1, 2)

    bilinear_gap = 2 * theta - Q(5, 14) - d
    assert bilinear_gap == Q(27437, 315000) > 0

    d1_exp = (3 * theta - 1) / 2
    selberg_gap = 2 * z_exp - d1_exp
    assert selberg_gap == Q(5027, 180000) > 0
    assert low_exp < theta < w_exp < Q(3, 2) * theta

    # J1 < 43/100: exp(43/25) > 39/7.
    assert exp_partial(Q(43, 25), 6) > Q(39, 7)
    j1_upper = Q(43, 100)

    # J2 < 17/100 from the exact logarithmic ratio.
    ratio2 = (Q(5)**20 * Q(13)**13 * Q(7)**7) / (Q(3)**21 * Q(11)**22)
    assert exp_partial(Q(17, 5), 6) > ratio2
    j2_upper = Q(17, 100)

    # J3 < 19/100.
    ratio3 = Q(9, 5)**9 * Q(11, 15)**11
    assert exp_partial(Q(19, 10), 5) > ratio3
    j3_upper = Q(19, 100)

    # J4 < 17/100 after enlarging theta to 1/2 in the upper endpoint.
    ratio4 = Q(18, 13)**9 * Q(2, 7)
    assert exp_partial(Q(17, 10), 5) > ratio4
    j4_upper = Q(17, 100)

    jsum_upper = j1_upper + j2_upper + j3_upper + j4_upper
    assert jsum_upper == Q(24, 25)

    # log(3)>263/240>109/100 from the first three positive atanh terms.
    log3_lower = 2 * (Q(1, 2) + Q(1, 2)**3 / 3 + Q(1, 2)**5 / 5)
    assert log3_lower == Q(263, 240) > Q(109, 100)

    w1_lower = 2 * Q(109, 100) - (2 * a / delta) * jsum_upper
    assert w1_lower == Q(7, 150)

    # Generalized Lemma-6 coefficient.
    mismatch = c * d - a * theta
    assert mismatch == Q(1, 2500)
    w2 = 16 * mismatch**2 / (a * delta * (3 * theta - 1)**2)
    assert w2 == Q(160, 224730081)

    net = w1_lower - w2
    assert net == Q(524362189, 11236504050) > 0

    print("P017 P2 five-ninth rational certificate: PASS")
    print("theta =", theta)
    print("D exponent =", d)
    print("bilinear exponent gap =", bilinear_gap)
    print("Lemma-6 z^2 exponent gap =", selberg_gap)
    print("W1 coarse lower coefficient =", w1_lower)
    print("W2 coarse upper coefficient =", w2)
    print("net coarse coefficient >", net, "~=", float(net))


if __name__ == "__main__":
    main()
