"""Typed diagonal-translation quotient normalization.

This module is a reusable *representation* operator for integer triples under the
common-translation relation

    z ~ z + k(1, 1, 1).

It provides the canonical nonnegative min-zero representative and the induced
Z^2 chart.  It does **not** authorize any semantic quotient by itself.  In
Enterprise geometry it is valid for the separately typed derived displacement
layer ``G_D/A_D``; it must not be used to identify primitive native point
addresses ``A_E`` unless a separate semantic theorem explicitly allows that.

Tool routing: T6 Operation-Safe Quotient / Predictive Refinement calculus,
typed/domain specialization.
"""

from __future__ import annotations

from collections.abc import Iterable

Triple = tuple[int, int, int]
Chart2 = tuple[int, int]


def as_triple(values: Iterable[int]) -> Triple:
    """Materialize exactly three integer coordinates."""
    triple = tuple(values)
    if len(triple) != 3:
        raise ValueError("expected exactly three coordinates")
    if not all(isinstance(value, int) for value in triple):
        raise TypeError("diagonal quotient coordinates must be integers")
    return triple  # type: ignore[return-value]


def diagonal_shift(values: Iterable[int], k: int) -> Triple:
    """Apply the common translation ``k(1,1,1)``."""
    if not isinstance(k, int):
        raise TypeError("diagonal shift must be an integer")
    a, b, c = as_triple(values)
    return (a + k, b + k, c + k)


def canonical_min_zero(values: Iterable[int]) -> Triple:
    """Return the unique nonnegative min-zero representative of a diagonal class."""
    a, b, c = as_triple(values)
    m = min(a, b, c)
    return (a - m, b - m, c - m)


def is_canonical_min_zero(values: Iterable[int]) -> bool:
    """Whether a triple is nonnegative with at least one zero coordinate."""
    a, b, c = as_triple(values)
    return min(a, b, c) == 0 and a >= 0 and b >= 0 and c >= 0


def diagonal_chart(values: Iterable[int]) -> Chart2:
    """The exact quotient chart ``chi(a,b,c)=(a-c,b-c)``."""
    a, b, c = as_triple(values)
    return (a - c, b - c)


def same_diagonal_class(left: Iterable[int], right: Iterable[int]) -> bool:
    """Exact class test for the subgroup ``Z(1,1,1)``."""
    return diagonal_chart(left) == diagonal_chart(right)


def class_shift(left: Iterable[int], right: Iterable[int]) -> int | None:
    """Return ``k`` with ``right = left + k(1,1,1)``, or ``None`` if classes differ."""
    a, b, c = as_triple(left)
    x, y, z = as_triple(right)
    k = x - a
    if y - b == k and z - c == k:
        return k
    return None


def compose_canonical(left: Iterable[int], right: Iterable[int]) -> Triple:
    """Transport quotient addition to canonical min-zero representatives."""
    a, b, c = as_triple(left)
    x, y, z = as_triple(right)
    return canonical_min_zero((a + x, b + y, c + z))


def inverse_canonical(values: Iterable[int]) -> Triple:
    """Transport the quotient additive inverse to canonical representatives."""
    a, b, c = as_triple(values)
    return canonical_min_zero((-a, -b, -c))


def identity_canonical() -> Triple:
    """Canonical representative of the quotient identity."""
    return (0, 0, 0)
