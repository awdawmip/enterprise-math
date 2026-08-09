"""Cumulative Franel transfer mismatch and multiplicative holonomy increments.

Let Psi be the Franel transfer obtained by substituting F_j for the canonical
central-binomial A_j representation of positive integers.  The direct segment
coordinate F_N and the canonical integer-factorization route for A_N need not
agree after this substitution.

Define Q_N as their multiplicative mismatch.  Without factoring A_N directly,
Q_N is generated recursively by the unified boundary defects Delta_n:

    Q_1=1,
    Q_N/Q_(N-1)=Delta_N.

Prime odd boundaries have Delta=1; composite boundaries have Delta=D_n.  Thus
Q_N is the cumulative product of composite Franel defects.  Multiplicativity of
Psi also gives the telescoping factorial/double-factorial formula.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_transfer_defect import (
    boundary_transfer_defect,
    franel_transfer,
)
from .p022_barlow_low_order_defect_reduction import composite_indices
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def cumulative_transfer_mismatch(max_segment: int) -> Fraction:
    """Q_N=product_(n=2..N) Delta_n; prime-boundary factors are one."""
    _require_positive("max_segment", max_segment)
    result = Fraction(1, 1)
    for segment in range(2, max_segment + 1):
        result *= boundary_transfer_defect(segment)
    return result


def composite_defect_product(max_segment: int) -> Fraction:
    """Same Q_N product restricted to the nontrivial composite boundaries."""
    _require_positive("max_segment", max_segment)
    result = Fraction(1, 1)
    for segment in composite_indices(max_segment):
        result *= boundary_transfer_defect(segment)
    return result


def factorial_transfer_product(max_segment: int) -> Fraction:
    """Psi(N!) evaluated multiplicatively without constructing the factorial."""
    _require_positive("max_segment", max_segment)
    result = Fraction(1, 1)
    for value in range(2, max_segment + 1):
        result *= franel_transfer(value)
    return result


def odd_double_factorial_transfer_product(max_segment: int) -> Fraction:
    """Psi((2N-1)!!) with the factor one omitted harmlessly."""
    _require_positive("max_segment", max_segment)
    result = Fraction(1, 1)
    for segment in range(2, max_segment + 1):
        result *= franel_transfer(2 * segment - 1)
    return result


def telescoping_transfer_mismatch(max_segment: int) -> Fraction:
    """Exact F_N Psi(N!) / (2^N Psi((2N-1)!!)) formula."""
    _require_positive("max_segment", max_segment)
    numerator = (
        Fraction(triple_moment_factor(max_segment), 1)
        * factorial_transfer_product(max_segment)
    )
    denominator = (
        Fraction(2**max_segment, 1)
        * odd_double_factorial_transfer_product(max_segment)
    )
    return numerator / denominator


def defect_is_discrete_multiplicative_derivative(segment: int) -> bool:
    """Check Delta_n=Q_n/Q_(n-1) exactly."""
    _require_positive("segment", segment)
    if segment < 2:
        raise ValueError("segment must be at least two")
    return (
        cumulative_transfer_mismatch(segment)
        == cumulative_transfer_mismatch(segment - 1)
        * boundary_transfer_defect(segment)
    )
