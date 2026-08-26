#!/usr/bin/env python3
"""Exact-rational audit certificate for the P017 P2 W1 source formula.

This script certifies the corrected source-normalized W1 reserves for the
four-sevenths and five-ninth a=4 root-edge packages.  It uses only Fraction
arithmetic and the atanh expansion for logarithms with an explicit tail.
"""

from fractions import Fraction as Q


def log_bounds(x: Q, degree: int) -> tuple[Q, Q]:
    """Return exact rational lower/upper bounds for log(x), x>0."""
    if x <= 0:
        raise ValueError("x must be positive")
    if degree < 0:
        raise ValueError("degree must be non-negative")

    z = (x - 1) / (x + 1)
    partial = Q(0)
    for k in range(degree + 1):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)

    tail = (
        2
        * abs(z) ** (2 * degree + 3)
        / ((2 * degree + 3) * (1 - z * z))
    )
    if z >= 0:
        return partial, partial + tail
    return partial - tail, partial


def interval_scale(c: Q, interval: tuple[Q, Q]) -> tuple[Q, Q]:
    lo, hi = interval
    if c >= 0:
        return c * lo, c * hi
    return c * hi, c * lo


def interval_sum(*intervals: tuple[Q, Q]) -> tuple[Q, Q]:
    return (
        sum(interval[0] for interval in intervals),
        sum(interval[1] for interval in intervals),
    )


def four_sevenths_bounds() -> tuple[Q, Q, Q]:
    # Correct source-normalized formulas:
    # J3 = 3/8 + (9/8) log(3/4)
    # J4 = (1/4) log(((34993/25000)^7)*(1669/5000))
    n = 6

    log3 = log_bounds(Q(3), n)
    log5 = log_bounds(Q(5), n)
    ratio2 = Q(8**8 * 3**7 * 5**5 * 7, 63**8)
    log_ratio2 = log_bounds(ratio2, n)
    log_three_quarters = log_bounds(Q(3, 4), n)
    ratio4 = Q(34993, 25000) ** 7 * Q(1669, 5000)
    log_ratio4 = log_bounds(ratio4, n)

    j1 = interval_scale(Q(1, 4), log5)
    j2 = interval_scale(Q(1, 8), log_ratio2)
    j3 = interval_sum(
        (Q(3, 8), Q(3, 8)),
        interval_scale(Q(9, 8), log_three_quarters),
    )
    j4 = interval_scale(Q(1, 4), log_ratio4)
    jsum = interval_sum(j1, j2, j3, j4)

    c1 = interval_sum(
        interval_scale(Q(2), log3),
        interval_scale(-Q(16, 7), jsum),
    )
    c1_lo, c1_hi = c1

    # Simple exact reserve used in the audit note.
    assert c1_lo > Q(533, 5000)

    c2 = Q(128, 174790063)
    net_simple = Q(533, 5000) - c2
    assert net_simple == Q(93162463579, 873950315000)
    assert net_simple > 0

    return c1_lo, c1_hi, net_simple


def five_ninth_bounds() -> tuple[Q, Q]:
    # Correct source-normalized formulas:
    # J3 = 2/5 + (11/10) log(11/15)
    # J4 = (1/5) log(((44991/32500)^9)*(5009/17500))
    n = 20

    log3 = log_bounds(Q(3), n)
    log_39_over_7 = log_bounds(Q(39, 7), n)
    ratio2 = Q(5**20 * 13**13 * 7**7, 3**21 * 11**22)
    log_ratio2 = log_bounds(ratio2, n)
    log_11_over_15 = log_bounds(Q(11, 15), n)
    ratio4 = Q(44991, 32500) ** 9 * Q(5009, 17500)
    log_ratio4 = log_bounds(ratio4, n)

    j1 = interval_scale(Q(1, 4), log_39_over_7)
    j2 = interval_scale(Q(1, 20), log_ratio2)
    j3 = interval_sum(
        (Q(2, 5), Q(2, 5)),
        interval_scale(Q(11, 10), log_11_over_15),
    )
    j4 = interval_scale(Q(1, 5), log_ratio4)
    jsum = interval_sum(j1, j2, j3, j4)

    c1 = interval_sum(
        interval_scale(Q(2), log3),
        interval_scale(-Q(20, 9), jsum),
    )
    c1_lo, c1_hi = c1

    # Entire rigorous interval is negative.
    assert c1_hi < -Q(3, 2500)

    return c1_lo, c1_hi


def main() -> None:
    four_lo, four_hi, net_simple = four_sevenths_bounds()
    five_lo, five_hi = five_ninth_bounds()

    print("P017 P2 W1 source-formula audit certificate: PASS")
    print("4/7 corrected C1 interval:")
    print("  lower =", four_lo, "~=", float(four_lo))
    print("  upper =", four_hi, "~=", float(four_hi))
    print("4/7 certified simple net reserve >", net_simple, "~=", float(net_simple))
    print("5/9 corrected C1 interval:")
    print("  lower =", five_lo, "~=", float(five_lo))
    print("  upper =", five_hi, "~=", float(five_hi))
    print("5/9 certified C1 < -3/2500")


if __name__ == "__main__":
    main()
