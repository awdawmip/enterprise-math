"""Conformally irreducible unit-amplitude events for total modular conservation.

An allowed unit event delta in {-1,0,+1}^N is causally decomposable when its
support/sign pattern can be partitioned into two nonzero allowed events without
coordinate cancellation.  Equivalently delta=a+b with a,b allowed, each nonzero,
and every nonzero coordinate of a or b has the same sign as delta at that slot.

This gives a causal irreducibility notion before importing polynomial degree or
matrix bases.  For total sum modulo m:

* m=1: irreducibles are single-slot +/-e_i;
* m=2: irreducibles are all two-slot sign pairs +/-e_i +/-e_j (D grammar);
* m>=3: irreducibles are exactly
    - opposite-sign two-slot transfers e_i-e_j;
    - all-plus or all-minus events on exactly m distinct slots.

For m>=3 the first family gives the A-type primitive shell while the m-slot
creation/annihilation family is the first higher-support channel distinguishing
mod-m conservation from exact total conservation.  For integer linear kernels,
conformal irreducibility is closely related to classical Graver-basis language;
that prior theory is a computational shadow, not claimed as new here.
"""

from __future__ import annotations

from itertools import combinations, product

Vector = tuple[int, ...]


def support_size(event: Vector) -> int:
    return sum(value != 0 for value in event)


def unit_events(slot_count: int) -> tuple[Vector, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    return tuple(
        tuple(event)
        for event in product((-1, 0, 1), repeat=slot_count)
        if any(event)
    )


def modular_allowed(event: Vector, modulus: int) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1:
        raise ValueError("modulus must be positive")
    return any(event) and sum(event) % modulus == 0


def _conformal_subevents(event: Vector) -> tuple[Vector, ...]:
    nonzero_positions = [index for index, value in enumerate(event) if value != 0]
    result = []
    # Choose a proper nonempty subset of the event's signed coordinates.
    for mask in range(1, (1 << len(nonzero_positions)) - 1):
        sub = [0] * len(event)
        for local_index, position in enumerate(nonzero_positions):
            if mask & (1 << local_index):
                sub[position] = event[position]
        result.append(tuple(sub))
    return tuple(result)


def conformally_decomposable(event: Vector, modulus: int) -> bool:
    if not modular_allowed(event, modulus):
        raise ValueError("event must be nonzero and allowed by declared modulus")
    for left in _conformal_subevents(event):
        if not modular_allowed(left, modulus):
            continue
        right = tuple(value - part for value, part in zip(event, left))
        if modular_allowed(right, modulus):
            return True
    return False


def irreducible_modular_events(slot_count: int, modulus: int) -> tuple[Vector, ...]:
    return tuple(
        event
        for event in unit_events(slot_count)
        if modular_allowed(event, modulus)
        and not conformally_decomposable(event, modulus)
    )


def closed_irreducible_modular_events(slot_count: int, modulus: int) -> set[Vector]:
    if slot_count < 1 or modulus < 1:
        raise ValueError("slot_count and modulus must be positive")
    events: set[Vector] = set()

    if modulus == 1:
        for index in range(slot_count):
            for sign in (-1, 1):
                vector = [0] * slot_count
                vector[index] = sign
                events.add(tuple(vector))
        return events

    # Opposite-sign transfers are irreducible for every nontrivial modulus.
    for receiver in range(slot_count):
        for donor in range(slot_count):
            if receiver == donor:
                continue
            vector = [0] * slot_count
            vector[receiver] = 1
            vector[donor] = -1
            events.add(tuple(vector))

    if modulus == 2:
        # Same-sign pair creation/annihilation is already support two.
        for i, j in combinations(range(slot_count), 2):
            for sign in (-1, 1):
                vector = [0] * slot_count
                vector[i] = sign
                vector[j] = sign
                events.add(tuple(vector))
        return events

    if slot_count >= modulus:
        for support in combinations(range(slot_count), modulus):
            for sign in (-1, 1):
                vector = [0] * slot_count
                for index in support:
                    vector[index] = sign
                events.add(tuple(vector))
    return events


def irreducible_closed_form_identity(slot_count: int, modulus: int) -> bool:
    return set(irreducible_modular_events(slot_count, modulus)) == closed_irreducible_modular_events(slot_count, modulus)


def irreducible_support_histogram(slot_count: int, modulus: int) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for event in closed_irreducible_modular_events(slot_count, modulus):
        size = support_size(event)
        histogram[size] = histogram.get(size, 0) + 1
    return dict(sorted(histogram.items()))
