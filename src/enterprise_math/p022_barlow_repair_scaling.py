"""Exact microscopic-average scaling data for two-sided Barlow repair.

The event-driven repair dimension r=E+B has worst case N+1, but its arithmetic
mean over all 4^N ordered microscopic word pairs is sublinear.  This module
keeps the exact finite means as reduced integer fractions; the accompanying
proof note derives the classical asymptotic

    E_micro[r_N]
      = 2(1+sqrt(2))*sqrt(N/pi) - (1/pi) log N + O(1).

No floating-point value is part of the executable state.
"""

from __future__ import annotations

from math import comb, gcd

from .p022_barlow_excursion_repair import total_orientation_repair_bit_load
from .p022_barlow_two_sided_repair import (
    total_diagonal_split_bit_load,
    total_two_sided_repair_bit_load,
)

FractionPair = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> FractionPair:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def one_sided_average_excursion_fraction(length: int) -> FractionPair:
    """Exact average excursion/orientation-bit load over ``2^N`` words."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    return _reduce(total_orientation_repair_bit_load(length), 2 ** length)


def diagonal_split_average_fraction(length: int) -> FractionPair:
    """Exact average number of diagonal-split bits over ``4^N`` word pairs."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    return _reduce(total_diagonal_split_bit_load(length), 4 ** length)


def microscopic_average_two_sided_repair_fraction(length: int) -> FractionPair:
    """Exact arithmetic mean of ``E+B`` over all ordered microscopic windows."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    return _reduce(total_two_sided_repair_bit_load(length), 4 ** length)


def diagonal_split_average_common_denominator(length: int) -> FractionPair:
    """Independent closed finite sum for the diagonal-split average.

    Put ``a_t=C(2t,t)/4^t``. Then

      E[B_N] = sum_{t=1}^{N-1} a_t
               - sum_{j=1}^{floor((N-1)/2)} a_j^2.

    A common denominator ``4^(N-1)`` gives a pure integer numerator:

      sum_t C(2t,t) 4^(N-1-t)
      - sum_j C(2j,j)^2 4^(N-1-2j).
    """
    _require_natural("length", length)
    if length <= 1:
        return 0, 1
    denominator = 4 ** (length - 1)
    numerator = sum(
        comb(2 * time, time) * 4 ** (length - 1 - time)
        for time in range(1, length)
    )
    numerator -= sum(
        comb(2 * index, index) ** 2 * 4 ** (length - 1 - 2 * index)
        for index in range(1, (length - 1) // 2 + 1)
    )
    return _reduce(numerator, denominator)


def central_binomial_partial_sum_identity(length: int) -> FractionPair:
    """Exact value of ``sum_{t=0}^{N-1} C(2t,t)/4^t``.

    The classical identity is

      sum_{t=0}^{M} C(2t,t)/4^t
        = (2M+1) C(2M,M)/4^M.

    Here ``M=N-1``.  Return the reduced rational pair.
    """
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    index = length - 1
    return _reduce(
        (2 * index + 1) * comb(2 * index, index),
        4 ** index,
    )


def average_to_worst_cross_fraction(length: int) -> FractionPair:
    """Exact ``mean / (N+1)`` ratio for nonempty horizon."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    numerator, denominator = microscopic_average_two_sided_repair_fraction(length)
    return _reduce(numerator, denominator * (length + 1))
