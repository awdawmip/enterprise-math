"""Classical quadratic-residue prefilter for BRC square-completion gaps.

This module composes the BRC multiplier cost surface with a classical exact
necessary condition for squarehood.  It is an engineering subtool, not a new
factorization theorem.

The canonical BRC ``addition_cost`` means distance to the *next* square.  The
classical difference-of-squares bridge instead needs the ceiling-square
completion cost, which is zero when the target is already a square.  The two
coordinates agree only for nonsquare targets.
"""

from __future__ import annotations

from functools import lru_cache
from math import isqrt

from .core import integer_nth_root

DEFAULT_SQUARE_RESIDUE_MODULUS = 4032


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@lru_cache(maxsize=None)
def square_residue_mask(modulus: int = DEFAULT_SQUARE_RESIDUE_MODULUS) -> int:
    """Return the exact packed bit mask of quadratic residues modulo modulus."""
    _require_positive("modulus", modulus)
    mask = 0
    for value in range(modulus):
        mask |= 1 << ((value * value) % modulus)
    return mask


def square_residue_count(modulus: int = DEFAULT_SQUARE_RESIDUE_MODULUS) -> int:
    """Return the number of quadratic-residue classes modulo modulus."""
    return square_residue_mask(modulus).bit_count()


def passes_square_residue_filter(
    value: int, modulus: int = DEFAULT_SQUARE_RESIDUE_MODULUS
) -> bool:
    """Necessary but not sufficient modular test for integer squarehood.

    Every exact square passes, so rejection has zero false negatives.
    """
    _require_natural("value", value)
    _require_positive("modulus", modulus)
    residue = value % modulus
    return bool((square_residue_mask(modulus) >> residue) & 1)


def filtered_square_root(
    value: int, modulus: int = DEFAULT_SQUARE_RESIDUE_MODULUS
) -> int | None:
    """Return the exact square root after a safe residue prefilter, else None."""
    _require_natural("value", value)
    if not passes_square_residue_filter(value, modulus):
        return None
    root = isqrt(value)
    return root if root * root == value else None


def ceiling_completion_cost(n: int, multiplier: int) -> tuple[int, int]:
    """Return ``(x,x**2-m*n)`` with ``x=ceil(sqrt(m*n))`` exactly.

    This is the classical Fermat/difference-of-squares completion coordinate.
    It differs from the BRC next-square addition cost only when ``m*n`` is
    already a perfect square.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    target = n * multiplier
    lower = integer_nth_root(target, 2)
    if lower * lower == target:
        return lower, 0
    upper = lower + 1
    return upper, upper * upper - target


def ceiling_completion_square_witness(
    n: int,
    multiplier: int,
    modulus: int = DEFAULT_SQUARE_RESIDUE_MODULUS,
) -> tuple[int, int] | None:
    """Return ``(x,b)`` if the immediate ceiling gap satisfies x^2-mn=b^2.

    This is only the classical immediate difference-of-squares witness surface.
    No claim is made that scanning multipliers is a novel factoring algorithm.
    """
    x, gap = ceiling_completion_cost(n, multiplier)
    b = filtered_square_root(gap, modulus)
    if b is None:
        return None
    return x, b


__all__ = [
    "DEFAULT_SQUARE_RESIDUE_MODULUS",
    "square_residue_mask",
    "square_residue_count",
    "passes_square_residue_filter",
    "filtered_square_root",
    "ceiling_completion_cost",
    "ceiling_completion_square_witness",
]
