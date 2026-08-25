#!/usr/bin/env python3
"""Exact-rational arithmetic certificate for the explicit B-spline P017 P2 package.

This checks only normalization constants and exponent bookkeeping. It does not
supply the hidden analytic constants in the bilinear exponential-sum estimate
and does not prove a finite numerical P2 threshold.
"""

from fractions import Fraction as Q


def main() -> None:
    theta = Q(4999, 10000)
    d = Q(4, 7)
    p = 7
    eta = Q(1, 70)
    mu = Q(16, 35)
    nu = Q(4, 35)

    assert mu + nu == d
    assert mu + 2 * nu == Q(24, 35) < 1

    # Fourier tail: p=7 and eta=1/70.
    tail_delta = (p - 1) * eta - (d - theta)
    assert tail_delta == Q(993, 70000) > 0

    # Elementary pi>3 upper bound for C_7.
    c7_upper = Q(2 * 7**7, 3**7 * 6)
    assert c7_upper == Q(823543, 6561) < 126
    total_modulus_tail_constant = 4 * c7_upper
    assert total_modulus_tail_constant == Q(3294172, 6561)

    # Diagonal structural exponent after Cauchy with explicit H exponent eta.
    diag_s2_exp = mu - theta + eta
    diag_delta = -diag_s2_exp / 2
    assert diag_s2_exp == -Q(1993, 70000)
    assert diag_delta == Q(1993, 140000) > 0

    # Trivial off-diagonal structural exponent after Cauchy.
    off_s2_exp = (
        2 * (d - theta)
        + (1 - theta) / 2
        + Q(5, 2) * eta
        - mu
    )
    off_delta = -off_s2_exp / 2
    assert off_s2_exp == -Q(793, 28000)
    assert off_delta == Q(793, 56000) > 0

    # Three-way balance is tight.
    deltas = (diag_delta, off_delta, tail_delta)
    assert min(deltas) == off_delta
    assert max(deltas) - min(deltas) == Q(21, 280000)  # 0.000075

    print("P017 explicit B-spline balanced exponent certificate: PASS")
    print("D exponent =", d)
    print("M exponent =", mu)
    print("N exponent =", nu)
    print("tail constant C7 <", c7_upper, "~=", float(c7_upper))
    print("4*C7 <", total_modulus_tail_constant, "~=", float(total_modulus_tail_constant))
    print("delta_diag =", diag_delta, "~=", float(diag_delta))
    print("delta_off =", off_delta, "~=", float(off_delta))
    print("delta_tail =", tail_delta, "~=", float(tail_delta))
    print("delta spread =", max(deltas) - min(deltas))


if __name__ == "__main__":
    main()
