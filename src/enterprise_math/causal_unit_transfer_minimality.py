"""Causal-minimality theorem forcing the A_(N-1) primitive event language.

Assume N equivalent integer slots.  A primitive displacement has coordinates in
{-1,0,+1}, is nonzero, conserves the total sum, and affects as few slots as
possible.  Any nonzero zero-sum unit-amplitude displacement must contain at least
one +1 and one -1, hence support at least two.  Support two is attainable and the
only such vectors are e_i-e_j.  Slot-permutation symmetry then closes one allowed
transfer under all ordered pairs, yielding exactly the traditional A_(N-1) root
set.

This is an internal theorem of the declared slot/conservation model.  It does not
prove that physical space itself must satisfy these axioms.
"""

from __future__ import annotations

from itertools import product

Vector = tuple[int, ...]


def support_size(vector: Vector) -> int:
    return sum(value != 0 for value in vector)


def unit_amplitude_displacements(slot_count: int) -> tuple[Vector, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    return tuple(
        tuple(vector)
        for vector in product((-1, 0, 1), repeat=slot_count)
        if any(vector)
    )


def conserved_unit_displacements(slot_count: int) -> tuple[Vector, ...]:
    return tuple(
        vector
        for vector in unit_amplitude_displacements(slot_count)
        if sum(vector) == 0
    )


def minimum_conserved_support(slot_count: int) -> int:
    conserved = conserved_unit_displacements(slot_count)
    if not conserved:
        raise AssertionError("at least one +1/-1 transfer must exist")
    return min(support_size(vector) for vector in conserved)


def minimum_support_conserved_events(slot_count: int) -> tuple[Vector, ...]:
    minimum = minimum_conserved_support(slot_count)
    return tuple(
        vector
        for vector in conserved_unit_displacements(slot_count)
        if support_size(vector) == minimum
    )


def expected_a_root_events(slot_count: int) -> tuple[Vector, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    return tuple(
        tuple(
            1 if index == receiver else -1 if index == donor else 0
            for index in range(slot_count)
        )
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    )


def minimum_support_events_are_exact_a_roots(slot_count: int) -> bool:
    return (
        minimum_conserved_support(slot_count) == 2
        and set(minimum_support_conserved_events(slot_count))
        == set(expected_a_root_events(slot_count))
    )


def causal_relation_dimension(slot_count: int) -> int:
    """One conserved total removes exactly one free integer slot direction."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    return slot_count - 1


def primitive_direction_count(slot_count: int) -> int:
    return slot_count * (slot_count - 1)
