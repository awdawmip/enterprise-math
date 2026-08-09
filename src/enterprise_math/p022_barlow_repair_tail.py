"""Finite microscopic tail bounds for Barlow event-driven repair.

The repair polynomial counts quotient states by exact repair dimension r, while
each such state represents 2^r microscopic two-sided stacking windows.  This
module converts that profile into exact microscopic tail counts and the finite
counting inequality

    L * #{windows with r>=L} <= total repair-bit load.

No stochastic model is assumed; probabilities are optional normalizations of a
finite counting identity.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_repair_polynomial import repair_polynomial_coefficients
from .p022_barlow_two_sided_repair import total_two_sided_repair_bit_load

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def microscopic_high_repair_count(length: int, threshold: int) -> int:
    """Exact number of microscopic windows whose repair dimension is >=L."""
    _require_natural("length", length)
    _require_natural("threshold", threshold)
    coefficients = repair_polynomial_coefficients(length)
    if threshold == 0:
        return 4**length
    return sum(
        history_count * (2**repair_bits)
        for repair_bits, history_count in enumerate(coefficients)
        if repair_bits >= threshold
    )


def microscopic_high_repair_fraction(length: int, threshold: int) -> Rational:
    """Reduced finite counting fraction of windows with repair >= threshold."""
    count = microscopic_high_repair_count(length, threshold)
    return _reduce(count, 4**length)


def counting_tail_upper_bound(length: int, threshold: int) -> int:
    """Integer Markov bound on high-repair microscopic windows.

    Since every counted window contributes at least ``threshold`` bits to the
    total repair load,

        threshold * H_N(threshold) <= total_load_N.

    The floor of ``total_load/threshold`` is therefore a valid integer upper
    bound. Threshold zero is the whole microscopic domain.
    """
    _require_natural("length", length)
    _require_natural("threshold", threshold)
    if threshold == 0:
        return 4**length
    return total_two_sided_repair_bit_load(length) // threshold


def counting_tail_bound_fraction(length: int, threshold: int) -> Rational:
    """Reduced finite fraction corresponding to the integer counting bound."""
    return _reduce(counting_tail_upper_bound(length, threshold), 4**length)


def exact_tail_inequality(length: int, threshold: int) -> tuple[int, int]:
    """Return both sides of ``threshold*H <= total_load`` and assert it."""
    _require_natural("length", length)
    _require_natural("threshold", threshold)
    left = threshold * microscopic_high_repair_count(length, threshold)
    right = total_two_sided_repair_bit_load(length)
    if left > right:
        raise AssertionError("finite repair-tail counting inequality failed")
    return left, right


def rational_linear_threshold(length: int, numerator: int, denominator: int) -> int:
    """Smallest integer L with ``L >= (numerator/denominator)*length``."""
    _require_natural("length", length)
    _require_positive("numerator", numerator)
    _require_positive("denominator", denominator)
    product = numerator * length
    return (product + denominator - 1) // denominator


def linear_repair_tail_bound_fraction(
    length: int, numerator: int, denominator: int
) -> Rational:
    """Finite bound for repair dimension at least a rational fraction of N."""
    threshold = rational_linear_threshold(length, numerator, denominator)
    return counting_tail_bound_fraction(length, threshold)
