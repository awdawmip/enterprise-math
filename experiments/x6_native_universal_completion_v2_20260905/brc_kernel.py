"""Exact positive-axis N-BRC kernel for the X6 universal Cell completion."""
from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Iterable


def _base_counts(length: int, p: int, q: int) -> tuple[int, int, int] | None:
    if type(length) is not int or length < 0 or type(p) is not int or type(q) is not int:
        raise ValueError("length,p,q must be integers with length>=0")
    nums = (length + 2 * p - q, length - p + 2 * q, length - p - q)
    if any(n % 3 for n in nums):
        return None
    counts = tuple(n // 3 for n in nums)
    if min(counts) < 0:
        return None
    return counts


def equal_axis_endpoint_multiplicity(length: int, p: int, q: int, sheet: int) -> int:
    """Exact number of length-m positive six-axis words ending at (p,q,sheet)."""
    if sheet not in (0, 1):
        raise ValueError("sheet must be 0 or 1")
    if length == 0:
        return int(p == 0 and q == 0 and sheet == 0)
    counts = _base_counts(length, p, q)
    if counts is None:
        return 0
    n1, n2, n3 = counts
    multinomial = factorial(length) // (factorial(n1) * factorial(n2) * factorial(n3))
    return (1 << (length - 1)) * multinomial


def equal_axis_visible_multiplicity(length: int, p: int, q: int) -> int:
    """Multiplicity after forgetting the companion sheet."""
    return (
        equal_axis_endpoint_multiplicity(length, p, q, 0)
        + equal_axis_endpoint_multiplicity(length, p, q, 1)
    )


def origin_companion_return_multiplicity(length: int) -> tuple[int, int]:
    """Return counts to origin and companion under equal positive-axis branching."""
    return (
        equal_axis_endpoint_multiplicity(length, 0, 0, 0),
        equal_axis_endpoint_multiplicity(length, 0, 0, 1),
    )


def c2_weight_channels(pair_weights: Iterable[tuple[Fraction | int, Fraction | int]]):
    """Return the derived C2 character coefficients (plus,minus) for 3 opposite pairs.

    Input order is the three base directions (u,ut), (v,vt), (w,wt).
    Original branch weights must be strictly positive.  The minus channel is a
    signed derived readout and is not a Positive Weighted-BRC state.
    """
    pairs = tuple(pair_weights)
    if len(pairs) != 3:
        raise ValueError("expected three opposite-axis weight pairs")
    plus = []
    minus = []
    for left, right in pairs:
        if isinstance(left, bool) or isinstance(right, bool):
            raise TypeError("weights must be exact int/Fraction")
        left = Fraction(left)
        right = Fraction(right)
        if left <= 0 or right <= 0:
            raise ValueError("original branch weights must be positive")
        plus.append(left + right)
        minus.append(left - right)
    return tuple(plus), tuple(minus)


__all__ = [
    "equal_axis_endpoint_multiplicity",
    "equal_axis_visible_multiplicity",
    "origin_companion_return_multiplicity",
    "c2_weight_channels",
]
