"""Exact microscopic-average repair complexity for two-sided Barlow history.

The coordination-history quotient has exact event-driven repair dimension
``r=E+B``: zero-boundary excursion orientations plus diagonal side splits.
This module studies the *microscopic-weighted* average additional repair bits
across all ``4^N`` ordered two-sided stacking windows.

The stored formulas are finite and integer/rational.  The asymptotic theorem in
the companion note is derived from standard central-binomial estimates; no
floating-point value is part of the exact state here.
"""

from __future__ import annotations

from math import comb, gcd

from .p022_barlow_excursion_repair import total_orientation_repair_bit_load
from .p022_barlow_two_sided_repair import (
    total_diagonal_split_bit_load,
    total_two_sided_repair_bit_load,
)

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def _add(left: Rational, right: Rational) -> Rational:
    return _reduce(
        left[0] * right[1] + right[0] * left[1],
        left[1] * right[1],
    )


def _subtract(left: Rational, right: Rational) -> Rational:
    return _reduce(
        left[0] * right[1] - right[0] * left[1],
        left[1] * right[1],
    )


def one_sided_orientation_average(length: int) -> Rational:
    """Exact average one-sided excursion-orientation repair bits.

    For ``m=floor((N-1)/2)`` and ``N>0`` this is

        (2m+1) C(2m,m) / 4^m.

    This equals the average number of zero-departure excursions of one signed
    ``+/-1`` prefix.
    """
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    m = (length - 1) // 2
    return _reduce((2 * m + 1) * comb(2 * m, m), 4**m)


def central_binomial_partial_average(max_time: int) -> Rational:
    """Exact normalized central-binomial partial sum.

        sum_{t=0}^M C(2t,t)/4^t
        = (2M+1) C(2M,M)/4^M.
    """
    _require_natural("max_time", max_time)
    return _reduce(
        (2 * max_time + 1) * comb(2 * max_time, max_time),
        4**max_time,
    )


def even_zero_overlap_correction(length: int) -> Rational:
    """Exact diagonal-split correction from simultaneous zero overlaps.

    For ``m=floor((N-1)/2)`` this is

        sum_{j=1}^m C(2j,j)^2 / 16^j.
    """
    _require_natural("length", length)
    m = (length - 1) // 2 if length else 0
    total: Rational = (0, 1)
    for j in range(1, m + 1):
        total = _add(total, _reduce(comb(2 * j, j) ** 2, 16**j))
    return total


def diagonal_split_average(length: int) -> Rational:
    """Exact microscopic average number of diagonal side-split bits.

    Directly from the finite event count,

        sum_{t=1}^{N-1}
          [C(2t,t) - 1_(t even) C(t,t/2)^2] / 4^t.

    The first part is collapsed by the central-binomial partial-sum identity;
    the second is :func:`even_zero_overlap_correction`.
    """
    _require_natural("length", length)
    if length <= 1:
        return 0, 1
    central = central_binomial_partial_average(length - 1)
    central_without_t0 = _subtract(central, (1, 1))
    return _subtract(central_without_t0, even_zero_overlap_correction(length))


def two_sided_repair_average_closed(length: int) -> Rational:
    """Exact average additional repair bits over all ``4^N`` windows.

    This is the closed decomposition

        2*A_N + C_(N-1) - 1 - H_N,

    where ``A_N`` is the one-sided excursion average,
    ``C_(N-1)`` the normalized central-binomial partial sum, and ``H_N`` the
    squared-central even-overlap correction.
    """
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    orientation = one_sided_orientation_average(length)
    two_orientation = _reduce(2 * orientation[0], orientation[1])
    return _add(two_orientation, diagonal_split_average(length))


def two_sided_repair_average_from_total(length: int) -> Rational:
    """Same average computed from the independently derived total event load."""
    _require_natural("length", length)
    return _reduce(total_two_sided_repair_bit_load(length), 4**length)


def exact_average_identity(length: int) -> tuple[Rational, Rational]:
    """Return both independent exact constructions and assert equality."""
    closed = two_sided_repair_average_closed(length)
    direct = two_sided_repair_average_from_total(length)
    if closed != direct:
        raise AssertionError("closed average decomposition must match event total")
    return closed, direct


def orientation_total_identity(length: int) -> tuple[int, int]:
    """Cross-check one-sided closed average against the existing total load."""
    _require_natural("length", length)
    average = one_sided_orientation_average(length)
    lhs = average[0] * (2**length)
    rhs = average[1] * total_orientation_repair_bit_load(length)
    if lhs != rhs:
        raise AssertionError("one-sided average must match total excursion load")
    return lhs, rhs


def diagonal_total_identity(length: int) -> tuple[int, int]:
    """Cross-check the closed diagonal average against exact finite event load."""
    _require_natural("length", length)
    average = diagonal_split_average(length)
    lhs = average[0] * (4**length)
    rhs = average[1] * total_diagonal_split_bit_load(length)
    if lhs != rhs:
        raise AssertionError("diagonal average must match total split-event load")
    return lhs, rhs


def leading_sqrt_constant_equation() -> tuple[int, int, int]:
    """Integer descriptor of the leading asymptotic constant.

    The companion proof gives

        average_r_N = c sqrt(N) - (1/pi) log N + O(1),
        c = 2(sqrt(2)+1)/sqrt(pi).

    The exact stored descriptor ``(2,1,1)`` records the algebraic numerator
    ``2*(sqrt(2)+1)``; the ``1/sqrt(pi)`` factor is analytic prior art rather
    than a finite state coordinate.
    """
    return 2, 1, 1
