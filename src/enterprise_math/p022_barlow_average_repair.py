"""Exact microscopic-average repair for two-sided Barlow coordination history.

The total repair dimension is E+B, where E counts zero-wall orientation releases
and B counts diagonal-split side-label releases.  All formulas are integer/rational.
"""

from __future__ import annotations

from math import comb, gcd

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def one_sided_orientation_mean(length: int) -> Rational:
    """Mean excursion/orientation repair for one microscopic sign word."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    m = (length - 1) // 2
    return _reduce((2 * m + 1) * comb(2 * m, m), 4**m)


def diagonal_split_mean(length: int) -> Rational:
    """Mean diagonal-split repair over ordered two-sided microscopic windows."""
    _require_natural("length", length)
    if length <= 1:
        return 0, 1
    denominator = 4 ** (length - 1)
    numerator = 0
    for time in range(1, length):
        equal_abs = comb(2 * time, time)
        if time % 2 == 0:
            equal_abs -= comb(time, time // 2) ** 2
        numerator += equal_abs * 4 ** (length - 1 - time)
    return _reduce(numerator, denominator)


def diagonal_split_mean_closed_first_term(length: int) -> tuple[Rational, Rational]:
    """Return the two exact terms D_N=A_N-H_N.

    A_N = sum_{t=1}^{N-1} C(2t,t)/4^t has a central-binomial closed form.
    H_N = sum_{j=1}^{floor((N-1)/2)} C(2j,j)^2/16^j is the simultaneous-zero
    correction.  The caller receives each rational separately.
    """
    _require_natural("length", length)
    if length <= 1:
        return (0, 1), (0, 1)
    m = length - 1
    first_num = (2 * m + 1) * comb(2 * m, m) - 4**m
    first = _reduce(first_num, 4**m)
    hmax = (length - 1) // 2
    hden = 16**hmax
    hnum = sum(
        comb(2 * j, j) ** 2 * 16 ** (hmax - j)
        for j in range(1, hmax + 1)
    )
    correction = _reduce(hnum, hden)
    return first, correction


def total_event_repair_mean(length: int) -> Rational:
    """Exact mean repair bits over all 4^N ordered two-sided windows."""
    _require_natural("length", length)
    o_num, o_den = one_sided_orientation_mean(length)
    d_num, d_den = diagonal_split_mean(length)
    return _reduce(2 * o_num * d_den + d_num * o_den, o_den * d_den)


def raw_state_bit_ratio(length: int) -> Rational:
    """Exact mean-repair / raw-two-sided-sign-bit ratio for N>0."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    mean_num, mean_den = total_event_repair_mean(length)
    return _reduce(mean_num, 2 * length * mean_den)
