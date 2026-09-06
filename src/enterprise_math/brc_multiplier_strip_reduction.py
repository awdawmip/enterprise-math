"""Exact 2-adic strip reduction for odd-N difference-of-squares scans.

For odd N, multiplier strips split into three universal 2-adic types:

- m == 2 (mod 4): impossible, because a difference of integer squares is never
  2 modulo 4;
- m == 4 (mod 8): every representation x^2-y^2=mN has x,y even and divides by
  four to a representation for (m/4)N.  Moreover the vertical offset maps by
  t_parent=floor(t/2), so the whole strip is redundant in any common finite
  t-window;
- m odd or 8|m: no analogous universal factor-two reduction is forced.

This is elementary difference-of-squares arithmetic composed with the BRC
multiplier/vertical coordinates; it is not a new factoring principle.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_multiplier_factor_scan import admissible_multipliers


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_sqrt(value: int) -> int:
    root = isqrt(value)
    return root if root * root == value else root + 1


def multiplier_strip_class(multiplier: int) -> str:
    """Return IMPOSSIBLE, REDUNDANT_BY_4, or PRIMITIVE_2ADIC."""
    _require_positive("multiplier", multiplier)
    if multiplier % 4 == 2:
        return "IMPOSSIBLE"
    if multiplier % 8 == 4:
        return "REDUNDANT_BY_4"
    return "PRIMITIVE_2ADIC"


def strip_reduced_multipliers(max_multiplier: int = 100) -> tuple[int, ...]:
    """Return admissible strips after deleting the universally redundant v2=2 family."""
    return tuple(
        multiplier
        for multiplier in admissible_multipliers(max_multiplier)
        if multiplier_strip_class(multiplier) == "PRIMITIVE_2ADIC"
    )


@dataclass(frozen=True)
class StripReductionWitness:
    n: int
    multiplier: int
    t: int
    x: int
    y: int
    parent_multiplier: int
    parent_t: int
    parent_x: int
    parent_y: int

    def __post_init__(self) -> None:
        if self.n % 2 != 1:
            raise ValueError("n must be odd")
        if self.multiplier % 8 != 4:
            raise ValueError("multiplier must be 4 mod 8")
        if self.x * self.x - self.y * self.y != self.multiplier * self.n:
            raise ValueError("source witness failed reconstruction")
        if (
            self.parent_x * self.parent_x - self.parent_y * self.parent_y
            != self.parent_multiplier * self.n
        ):
            raise ValueError("parent witness failed reconstruction")
        if self.parent_multiplier * 4 != self.multiplier:
            raise ValueError("parent multiplier must be multiplier/4")
        if self.parent_t != self.t // 2:
            raise ValueError("parent vertical offset must equal floor(t/2)")


def reduce_square_hit_to_parent(
    n: int, multiplier: int, t: int
) -> StripReductionWitness | None:
    """Map one exact square-gap hit on m==4 mod8 to its m/4 parent hit.

    Returns None when the supplied vertical position is not a square-gap hit.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    if isinstance(t, bool) or not isinstance(t, int) or t < 0:
        raise ValueError("t must be a non-negative integer")
    if n % 2 != 1:
        raise ValueError("n must be odd")
    if multiplier % 8 != 4:
        raise ValueError("multiplier must be 4 mod 8")

    source_base = _ceil_sqrt(multiplier * n)
    x = source_base + t
    gap = x * x - multiplier * n
    y = isqrt(gap)
    if y * y != gap:
        return None

    # mN == 4 (mod 8). A square difference congruent to 4 mod 8 forces both
    # x and y even; division by four is exact.
    if x % 2 or y % 2:
        raise AssertionError("4 mod 8 square difference did not force even x,y")

    parent_multiplier = multiplier // 4
    parent_x = x // 2
    parent_y = y // 2
    parent_base = _ceil_sqrt(parent_multiplier * n)
    parent_t = parent_x - parent_base
    if parent_t < 0:
        raise AssertionError("reduced parent fell below its ceiling-root base")
    if parent_t != t // 2:
        raise AssertionError("strip offset halving law failed")

    return StripReductionWitness(
        n=n,
        multiplier=multiplier,
        t=t,
        x=x,
        y=y,
        parent_multiplier=parent_multiplier,
        parent_t=parent_t,
        parent_x=parent_x,
        parent_y=parent_y,
    )


def two_adic_strip_counts(max_multiplier: int = 100) -> dict[str, int]:
    _require_positive("max_multiplier", max_multiplier)
    counts = {"IMPOSSIBLE": 0, "REDUNDANT_BY_4": 0, "PRIMITIVE_2ADIC": 0}
    for multiplier in range(1, max_multiplier + 1):
        counts[multiplier_strip_class(multiplier)] += 1
    return counts


__all__ = [
    "StripReductionWitness",
    "multiplier_strip_class",
    "strip_reduced_multipliers",
    "reduce_square_hit_to_parent",
    "two_adic_strip_counts",
]
