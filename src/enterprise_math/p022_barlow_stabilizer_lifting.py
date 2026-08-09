"""Stabilizer-index formula for the B2 Barlow quotient-path lift count.

The B2 signed-permutation group acts on labelled signed drift states.  For a
canonical chamber transition p->q, the number of labelled next lifts from a
fixed labelled lift of p is the index

    |Stab(p)| / |Stab(p,q)|,

where the edge stabilizer fixes both canonical endpoints.  In this concrete
step graph the index is always 1, 2, or 4 and equals ``2^(one-step E+B)``.
Multiplying the indices along a chamber path recovers the exact microscopic
fiber ``2^(E+B)``.
"""

from __future__ import annotations

from itertools import product

from .p022_barlow_repair_polynomial import chamber_successors
from .p022_barlow_weyl_quotient import (
    ChamberPath,
    ChamberState,
    path_wall_event_counts,
    quotient_path_lift_count,
)

# Group element: (swap, first_sign, second_sign)
B2Element = tuple[bool, int, int]


def b2_elements() -> tuple[B2Element, ...]:
    return tuple(
        (swap, first_sign, second_sign)
        for swap in (False, True)
        for first_sign, second_sign in product((-1, 1), repeat=2)
    )


def apply_b2(element: B2Element, state: tuple[int, int]) -> tuple[int, int]:
    """Apply one signed permutation to an integer pair."""
    swap, first_sign, second_sign = element
    x, y = state
    if swap:
        x, y = y, x
    return first_sign * x, second_sign * y


def vertex_stabilizer(state: tuple[int, int]) -> tuple[B2Element, ...]:
    """Elements fixing one labelled integer state exactly."""
    return tuple(
        element for element in b2_elements() if apply_b2(element, state) == state
    )


def edge_stabilizer(
    source: tuple[int, int], target: tuple[int, int]
) -> tuple[B2Element, ...]:
    """Elements fixing both endpoints of one directed edge."""
    return tuple(
        element
        for element in b2_elements()
        if apply_b2(element, source) == source
        and apply_b2(element, target) == target
    )


def local_stabilizer_index(
    source: ChamberState, target: ChamberState
) -> int:
    """Exact local lift branching index for one legal chamber transition."""
    if target not in chamber_successors(source):
        raise ValueError("target is not a legal chamber successor")
    vertex_size = len(vertex_stabilizer(source))
    edge_size = len(edge_stabilizer(source, target))
    if edge_size <= 0 or vertex_size % edge_size:
        raise AssertionError("edge stabilizer must be a subgroup of vertex stabilizer")
    return vertex_size // edge_size


def local_event_branch_factor(
    source: ChamberState, target: ChamberState
) -> int:
    """Existing event rule ``2^(zero departures + diagonal split)``."""
    if target not in chamber_successors(source):
        raise ValueError("target is not a legal chamber successor")
    orientation = int(source[0] == 0) + int(source[1] == 0)
    split = int(source[0] == source[1] and target[0] != target[1])
    return 2 ** (orientation + split)


def verify_local_stabilizer_event_identity(
    source: ChamberState, target: ChamberState
) -> tuple[int, int]:
    """Return stabilizer index and event factor and require exact equality."""
    stabilizer = local_stabilizer_index(source, target)
    event = local_event_branch_factor(source, target)
    if stabilizer != event:
        raise AssertionError("B2 stabilizer index must equal event branching factor")
    return stabilizer, event


def stabilizer_product_lift_count(path: ChamberPath) -> int:
    """Product of local vertex/edge stabilizer indices along one chamber path."""
    if not isinstance(path, tuple):
        raise ValueError("path must be a tuple")
    previous: ChamberState = (0, 0)
    result = 1
    for current in path:
        result *= local_stabilizer_index(previous, current)
        previous = current
    return result


def verify_path_stabilizer_lifting(path: ChamberPath) -> tuple[int, int, int]:
    """Cross-check stabilizer product, event product and existing lift theorem."""
    stabilizer = stabilizer_product_lift_count(path)
    orientation, split = path_wall_event_counts(path)
    event = 2 ** (orientation + split)
    existing = quotient_path_lift_count(path)
    if not (stabilizer == event == existing):
        raise AssertionError("all B2 path-lift formulas must agree")
    return stabilizer, event, existing
