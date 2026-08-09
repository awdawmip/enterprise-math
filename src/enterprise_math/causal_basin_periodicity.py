"""Periodic P008 basin widths generate natural safe superblock translations.

Let a strictly increasing integer growth law V have basin widths
w_k=V(k+1)-V(k).  If the width sequence is periodic with period p, then the total
capacity of one period

    T = sum_(j=0)^(p-1) w_j

satisfies V(k+p)=V(k)+T.  Therefore every basin state
n=V(k)+detail maps under +T to V(k+p)+the same detail, so

    R_V(n+T)=R_V(n)+p.

Thus +T descends exactly to the level-only quotient and even preserves the basin
detail coordinate.  Constant-width block precision is the period-one special
case.  Periodic width patterns therefore generate safe superblock scales without
requiring every local basin to have the same width.
"""

from __future__ import annotations


def _validate_growth(growth: tuple[int, ...]) -> None:
    if not isinstance(growth, tuple) or len(growth) < 2:
        raise ValueError("growth must contain at least two levels")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in growth
    ):
        raise ValueError("growth values must be non-negative integers")
    if any(left >= right for left, right in zip(growth, growth[1:])):
        raise ValueError("growth must be strictly increasing")


def growth_widths(growth: tuple[int, ...]) -> tuple[int, ...]:
    _validate_growth(growth)
    return tuple(right - left for left, right in zip(growth, growth[1:]))


def widths_are_periodic(widths: tuple[int, ...], period: int) -> bool:
    if not isinstance(widths, tuple) or not widths:
        raise ValueError("widths must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in widths):
        raise ValueError("widths must be positive integers")
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be a positive integer")
    return all(
        widths[index] == widths[index % period]
        for index in range(len(widths))
    )


def period_capacity(widths: tuple[int, ...], period: int) -> int:
    if not widths_are_periodic(widths, period):
        raise ValueError("width sequence does not match the declared period")
    if len(widths) < period:
        raise ValueError("need at least one full represented period")
    return sum(widths[:period])


def periodic_translation_identity(
    growth: tuple[int, ...],
    period: int,
) -> tuple[int, bool]:
    """Return `(T, verified)` for V(k+p)=V(k)+T on represented complete levels."""
    widths = growth_widths(growth)
    if not widths_are_periodic(widths, period):
        raise ValueError("growth widths are not periodic with declared period")
    total = period_capacity(widths, period)
    verified = all(
        growth[index + period] == growth[index] + total
        for index in range(len(growth) - period)
    )
    return total, verified


def periodic_translation_preserves_basin_detail(
    growth: tuple[int, ...],
    period: int,
    level: int,
    detail: int,
) -> bool:
    widths = growth_widths(growth)
    total, verified = periodic_translation_identity(growth, period)
    if not verified:
        return False
    if (
        isinstance(level, bool)
        or not isinstance(level, int)
        or not (0 <= level < len(growth) - period)
    ):
        raise ValueError("level must have a represented period-ahead level")
    width = widths[level]
    if isinstance(detail, bool) or not isinstance(detail, int) or not (0 <= detail < width):
        raise ValueError("detail must lie inside the selected basin")
    return (
        growth[level] + detail + total
        == growth[level + period] + detail
        and widths[level + period] == width
    )


def periodic_superblock_translations(widths: tuple[int, ...], period: int, multiples: int) -> tuple[int, ...]:
    """First positive multiples of the natural period capacity T."""
    if isinstance(multiples, bool) or not isinstance(multiples, int) or multiples <= 0:
        raise ValueError("multiples must be a positive integer")
    total = period_capacity(widths, period)
    return tuple(total * multiplier for multiplier in range(1, multiples + 1))
