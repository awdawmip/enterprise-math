"""Structured transport fusion for radix-quotient addition.

The one-step transport branching layer says how many correction symbols are
necessary.  This module studies a positive composable case: n-ary addition under
Q_r.  The globally minimal one-shot correction is the total carry, while exact
recursive composition uses the pair ``(carry, remainder)``.  The remainder is
persistent state detail; the carry is transport data.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from functools import reduce


def _validate_radix(radix: int) -> None:
    if isinstance(radix, bool) or not isinstance(radix, int) or radix < 2:
        raise ValueError("radix must be an integer at least two")


def _validate_residue(radix: int, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < radix:
        raise ValueError("residue must be an integer in [0, radix)")


def nary_addition_transport_capacity(radix: int, arity: int) -> int:
    """Exact Q_r one-shot transport branching for n-ary addition."""
    _validate_radix(radix)
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 1:
        raise ValueError("arity must be a positive integer")
    return (arity * (radix - 1)) // radix + 1


def nary_addition_transport_bit_cost(radix: int, arity: int) -> int:
    capacity = nary_addition_transport_capacity(radix, arity)
    return (capacity - 1).bit_length()


def total_carry(radix: int, residues: Iterable[int]) -> int:
    _validate_radix(radix)
    values = tuple(residues)
    if not values:
        raise ValueError("at least one residue is required")
    for value in values:
        _validate_residue(radix, value)
    return sum(values) // radix


def carry_detail_state(radix: int, residues: Iterable[int]) -> tuple[int, int]:
    """Return Euclidean coordinates of the total residue sum: (carry, detail)."""
    _validate_radix(radix)
    values = tuple(residues)
    if not values:
        raise ValueError("at least one residue is required")
    for value in values:
        _validate_residue(radix, value)
    total = sum(values)
    return total // radix, total % radix


def combine_carry_detail(
    radix: int,
    left: tuple[int, int],
    right: tuple[int, int],
) -> tuple[int, int]:
    """Associative composition of additive transport with persistent detail."""
    _validate_radix(radix)
    left_carry, left_detail = left
    right_carry, right_detail = right
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (left_carry, right_carry)
    ):
        raise ValueError("carry coordinates must be non-negative integers")
    _validate_residue(radix, left_detail)
    _validate_residue(radix, right_detail)
    detail_sum = left_detail + right_detail
    return (
        left_carry + right_carry + detail_sum // radix,
        detail_sum % radix,
    )


def fold_carry_detail(
    radix: int,
    states: Sequence[tuple[int, int]],
) -> tuple[int, int]:
    _validate_radix(radix)
    values = tuple(states)
    if not values:
        return (0, 0)
    return reduce(lambda left, right: combine_carry_detail(radix, left, right), values)


def binary_carry_field_budget(arity: int) -> int:
    """Bits used by storing one separate binary carry field at every binary merge."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 1:
        raise ValueError("arity must be a positive integer")
    return arity - 1


def fused_carry_savings_lower_bound(radix: int, arity: int) -> int:
    """Guaranteed fixed-width saving vs n-1 independent one-bit carry fields."""
    modular = binary_carry_field_budget(arity)
    fused = nary_addition_transport_bit_cost(radix, arity)
    return modular - fused


def carry_token_alone_is_not_composable_witness(radix: int) -> dict[str, tuple[int, int] | int]:
    """Universal witness that equal subtree carry tokens can need different next carries.

    The two left subtree states `(0,0)` and `(0,r-1)` have the same carry token
    zero but different persistent remainder detail.  Combining either with
    `(0,1)` produces different resulting carries.
    """
    _validate_radix(radix)
    left_first = (0, 0)
    left_second = (0, radix - 1)
    right = (0, 1)
    combined_first = combine_carry_detail(radix, left_first, right)
    combined_second = combine_carry_detail(radix, left_second, right)
    if left_first[0] != left_second[0]:
        raise AssertionError("witness left states must share the same carry token")
    if combined_first[0] == combined_second[0]:
        raise AssertionError("witness failed to separate the next carry")
    return {
        "left_first": left_first,
        "left_second": left_second,
        "right": right,
        "combined_first_carry": combined_first[0],
        "combined_second_carry": combined_second[0],
    }
