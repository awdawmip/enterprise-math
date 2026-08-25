#!/usr/bin/env python3
"""Exact-rational exponent bookkeeping for the four-sevenths trivial-pair reduction.

This verifies only algebraic exponent relations extracted from the displayed
Iwaniec-Laborde Lemma-4 proof estimates. It does not make the implicit analytic
constants effective and does not prove a numerical P2 threshold.
"""

from fractions import Fraction as Q


def main() -> None:
    theta = Q(4999, 10000)
    eps = Q(1, 200)
    d = Q(4, 7)
    mu = Q(25, 56)
    nu = Q(1, 8)

    assert mu + nu == d

    # A2: M < y X^(-6 eps).
    a2_margin = theta - 6 * eps - mu
    assert a2_margin == Q(1643, 70000) > 0

    # A3: M N^2 < X.
    mn2_exp = mu + 2 * nu
    a3_margin = 1 - mn2_exp
    assert mn2_exp == Q(39, 56)
    assert a3_margin == Q(17, 56) > 0

    # A4: M N^2 <= y^(5/2) X^(-1/2-4 eps).
    a4_rhs_exp = Q(5, 2) * theta - Q(1, 2) - 4 * eps
    a4_margin = a4_rhs_exp - mn2_exp
    assert a4_rhs_exp == Q(2919, 4000)
    assert a4_margin == Q(933, 28000) > 0

    # Cauchy + displayed diagonal estimate.
    diag_s2_exp = mu - theta + 3 * eps
    diag_delta = -diag_s2_exp / 2
    assert diag_s2_exp == -Q(2693, 70000)
    assert diag_delta == Q(2693, 140000) > 0

    # Cauchy + displayed trivial off-diagonal estimate (10).
    off_s2_exp = (
        2 * (d - theta)
        + (1 - theta) / 2
        + 3 * eps
        - mu
    )
    off_delta = -off_s2_exp / 2
    assert off_s2_exp == -Q(1073, 28000)
    assert off_delta == Q(1073, 56000) > 0

    bottleneck_delta = min(diag_delta, off_delta)
    assert bottleneck_delta == off_delta

    effective_target = Q(1, 100)
    reserve_after_target = bottleneck_delta - effective_target
    assert reserve_after_target == Q(513, 56000) > 0

    print("P017 four-sevenths trivial-pair exponent certificate: PASS")
    print("M exponent =", mu)
    print("N exponent =", nu)
    print("A2 margin =", a2_margin)
    print("A3 margin =", a3_margin)
    print("A4 margin =", a4_margin)
    print("diagonal delta =", diag_delta, "~=", float(diag_delta))
    print("off-diagonal delta =", off_delta, "~=", float(off_delta))
    print("reserve above X^(-1/100) target =", reserve_after_target)


if __name__ == "__main__":
    main()
