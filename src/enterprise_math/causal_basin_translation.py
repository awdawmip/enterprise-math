"""Additive future-safety obstruction for P008 level-only collapse.

Let V(k) be strictly increasing integer complete growth and q_V its P008 root
level.  The k-th basin is the full integer interval

    [V(k), V(k+1)-1]

of width w_k=V(k+1)-V(k).

For any fixed positive translation t, if one basin has width w_k>t, then the two
same-level states V(k) and V(k+1)-1 are separated by +t:

    q(V(k)+t)=k,
    q(V(k+1)-1+t)>=k+1.

Therefore a level-only quotient cannot be future-safe for +t whenever any basin
is wider than t.  If basin widths are unbounded, no fixed positive additive
future can be globally safe on the level-only quotient.

Consequently any causally generated complete-growth polynomial of degree at
least two (with positive leading growth) has intrinsically detail-sensitive
additive dynamics: its first difference has positive degree and unbounded basin
width.  Linear constant-width growth is the exceptional regime where aligned
whole-block translations may descend.
"""

from __future__ import annotations

from .causal_completion_collapse import completion_root_index


def _validate_growth(growth: tuple[int, ...]) -> None:
    if not isinstance(growth, tuple) or len(growth) < 2:
        raise ValueError("growth must contain at least two complete levels")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in growth
    ):
        raise ValueError("growth values must be non-negative integers")
    if any(left >= right for left, right in zip(growth, growth[1:])):
        raise ValueError("growth must be strictly increasing")


def basin_width(growth: tuple[int, ...], level: int) -> int:
    _validate_growth(growth)
    if isinstance(level, bool) or not isinstance(level, int) or not (0 <= level < len(growth) - 1):
        raise ValueError("level must have a represented next complete level")
    return growth[level + 1] - growth[level]


def translation_separation_witness(
    growth: tuple[int, ...],
    increment: int,
) -> tuple[int, int, int] | None:
    """Return `(level,left,right)` for the first basin wider than positive increment."""
    _validate_growth(growth)
    if isinstance(increment, bool) or not isinstance(increment, int) or increment <= 0:
        raise ValueError("increment must be a positive integer")
    for level in range(len(growth) - 1):
        if basin_width(growth, level) > increment:
            return level, growth[level], growth[level + 1] - 1
    return None


def witness_really_separates_after_translation(
    growth: tuple[int, ...],
    increment: int,
    witness: tuple[int, int, int],
) -> bool:
    level, left, right = witness
    if completion_root_index(growth, left) != level:
        return False
    if completion_root_index(growth, right) != level:
        return False
    left_after = completion_root_index(growth, left + increment)
    right_after = completion_root_index(growth, right + increment)
    return left_after == level and right_after is not None and right_after > level


def quotient_translation_safe_on_represented_sample(
    growth: tuple[int, ...],
    increment: int,
    maximum_amount: int,
) -> bool:
    """Finite exact check of q(x)=q(x') => q(x+t)=q(x'+t) on represented amounts."""
    _validate_growth(growth)
    if isinstance(increment, bool) or not isinstance(increment, int) or increment < 0:
        raise ValueError("increment must be a non-negative integer")
    if isinstance(maximum_amount, bool) or not isinstance(maximum_amount, int) or maximum_amount < 0:
        raise ValueError("maximum_amount must be a non-negative integer")
    classes = {
        amount: completion_root_index(growth, amount)
        for amount in range(maximum_amount + increment + 1)
    }
    for left in range(maximum_amount + 1):
        for right in range(left + 1, maximum_amount + 1):
            if classes[left] != classes[right]:
                continue
            if classes[left + increment] != classes[right + increment]:
                return False
    return True


def has_wide_basin_obstruction(growth: tuple[int, ...], increment: int) -> bool:
    witness = translation_separation_witness(growth, increment)
    return witness is not None and witness_really_separates_after_translation(
        growth, increment, witness
    )
