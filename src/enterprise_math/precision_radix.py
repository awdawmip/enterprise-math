"""Exact finite detail charts for multi-step precision refinement.

A total detail state modulo ``r*s`` can be written uniquely in either mixed-radix
chart

    value = s * u + v,  0 <= u < r, 0 <= v < s,

or the swapped chart

    value = r * u' + v', 0 <= u' < s, 0 <= v' < r.

The coordinate transition is exact and integer-only. These utilities are an
executable pressure test for P018 Supplement 08; mixed-radix arithmetic and its
coordinate changes are established mathematics, not a novelty claim.
"""

from __future__ import annotations


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_digit(name: str, value: int, radix: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < radix:
        raise ValueError(f"{name} must satisfy 0 <= {name} < {radix}")


def split_detail(value: int, outer_radix: int, inner_radix: int) -> tuple[int, int]:
    """Return the unique ``(outer, inner)`` digits of a total detail state."""
    _require_positive("outer_radix", outer_radix)
    _require_positive("inner_radix", inner_radix)
    total = outer_radix * inner_radix
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < total:
        raise ValueError(f"value must satisfy 0 <= value < {total}")
    return value // inner_radix, value % inner_radix


def join_detail(outer: int, inner: int, outer_radix: int, inner_radix: int) -> int:
    """Reconstruct a total detail state from one mixed-radix chart."""
    _require_positive("outer_radix", outer_radix)
    _require_positive("inner_radix", inner_radix)
    _require_digit("outer", outer, outer_radix)
    _require_digit("inner", inner, inner_radix)
    return inner_radix * outer + inner


def radix_swap(outer: int, inner: int, outer_radix: int, inner_radix: int) -> tuple[int, int]:
    """Change from radices ``(r,s)`` to ``(s,r)`` without changing the detail state."""
    value = join_detail(outer, inner, outer_radix, inner_radix)
    return split_detail(value, inner_radix, outer_radix)


def carry(radix: int, first: int, second: int) -> int:
    """Canonical binary carry for two detail digits at one radix."""
    _require_positive("radix", radix)
    _require_digit("first", first, radix)
    _require_digit("second", second, radix)
    return (first + second) // radix


def staged_carry(outer_radix: int, inner_radix: int, first: int, second: int) -> int:
    """Carry at the coarse endpoint after a two-level mixed-radix addition."""
    _require_positive("outer_radix", outer_radix)
    _require_positive("inner_radix", inner_radix)
    total = outer_radix * inner_radix
    if not 0 <= first < total or not 0 <= second < total:
        raise ValueError("details must lie in the total product-radix fiber")
    first_outer, first_inner = split_detail(first, outer_radix, inner_radix)
    second_outer, second_inner = split_detail(second, outer_radix, inner_radix)
    inner_carry = carry(inner_radix, first_inner, second_inner)
    return (first_outer + second_outer + inner_carry) // outer_radix


def direct_carry(total_radix: int, first: int, second: int) -> int:
    """Carry obtained by treating the whole finite detail fiber as one digit."""
    return carry(total_radix, first, second)


def braid_left(r: int, s: int, t: int, a: int, b: int, c: int) -> tuple[int, int, int]:
    """Apply adjacent radix swaps in the order 12, 23, 12."""
    _require_positive("r", r)
    _require_positive("s", s)
    _require_positive("t", t)
    _require_digit("a", a, r)
    _require_digit("b", b, s)
    _require_digit("c", c, t)
    a1, b1 = radix_swap(a, b, r, s)
    b2, c2 = radix_swap(b1, c, r, t)
    a3, b3 = radix_swap(a1, b2, s, t)
    return a3, b3, c2


def braid_right(r: int, s: int, t: int, a: int, b: int, c: int) -> tuple[int, int, int]:
    """Apply adjacent radix swaps in the order 23, 12, 23."""
    _require_positive("r", r)
    _require_positive("s", s)
    _require_positive("t", t)
    _require_digit("a", a, r)
    _require_digit("b", b, s)
    _require_digit("c", c, t)
    b1, c1 = radix_swap(b, c, s, t)
    a2, b2 = radix_swap(a, b1, r, t)
    b3, c3 = radix_swap(b2, c1, r, s)
    return a2, b3, c3


def additive_diamond_flat(r: int, s: int, first: int, second: int) -> bool:
    """Check endpoint carry equality through the two swapped precision charts."""
    _require_positive("r", r)
    _require_positive("s", s)
    total = r * s
    if not 0 <= first < total or not 0 <= second < total:
        raise ValueError("details must lie in the total product-radix fiber")
    direct = direct_carry(total, first, second)
    via_r_then_s = staged_carry(r, s, first, second)
    via_s_then_r = staged_carry(s, r, first, second)
    return direct == via_r_then_s == via_s_then_r
