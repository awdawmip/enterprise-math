"""Local primitive geometry under modular total-conservation laws.

Let unit-amplitude events have coordinates in {-1,0,+1}.  Impose

    sum(delta) == 0 mod m

and choose nonzero events of minimum support.

* m=1: support-one axis events +/-e_i (Z grammar);
* m=2: all support-two sign pairs +/-e_i +/-e_j (D grammar);
* m>=3: only opposite-sign support-two transfers e_i-e_j (A grammar).

Therefore A-type primitive geometry cannot distinguish exact total conservation
from modular conservation m>=3.  For m>=3 and at least m slots, exact and mod-m
unit-amplitude event languages agree at every support <m; the first mod-m event
that changes the exact total has support m and is an all-plus or all-minus event.
Geometry is therefore a finite-support shadow of the deeper conservation law.
"""

from __future__ import annotations

from itertools import product

Vector = tuple[int, ...]


def support_size(vector: Vector) -> int:
    return sum(value != 0 for value in vector)


def unit_events(slot_count: int) -> tuple[Vector, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    return tuple(
        tuple(event)
        for event in product((-1, 0, 1), repeat=slot_count)
        if any(event)
    )


def modular_events(slot_count: int, modulus: int) -> tuple[Vector, ...]:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1:
        raise ValueError("modulus must be positive")
    return tuple(event for event in unit_events(slot_count) if sum(event) % modulus == 0)


def exact_conservation_events(slot_count: int) -> tuple[Vector, ...]:
    return tuple(event for event in unit_events(slot_count) if sum(event) == 0)


def minimum_modular_events(slot_count: int, modulus: int) -> tuple[Vector, ...]:
    allowed = modular_events(slot_count, modulus)
    if not allowed:
        return ()
    minimum = min(support_size(event) for event in allowed)
    return tuple(event for event in allowed if support_size(event) == minimum)


def primitive_geometry_family(modulus: int) -> str:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1:
        raise ValueError("modulus must be positive")
    if modulus == 1:
        return "Z"
    if modulus == 2:
        return "D"
    return "A"


def first_exact_total_changing_support(slot_count: int, modulus: int) -> int | None:
    """Minimum support of a mod-m event with nonzero exact total, if available."""
    if modulus < 1:
        raise ValueError("modulus must be positive")
    candidates = [
        support_size(event)
        for event in modular_events(slot_count, modulus)
        if sum(event) != 0
    ]
    return min(candidates) if candidates else None


def exact_and_modular_agree_below_support(
    slot_count: int,
    modulus: int,
    support_bound: int,
) -> bool:
    if support_bound < 0:
        raise ValueError("support_bound must be non-negative")
    exact = {
        event
        for event in exact_conservation_events(slot_count)
        if support_size(event) < support_bound
    }
    modular = {
        event
        for event in modular_events(slot_count, modulus)
        if support_size(event) < support_bound
    }
    return exact == modular
