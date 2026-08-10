"""Ordered boundary bridges turn integer precision hierarchies into paths.

Hierarchy alone does not determine local space.  The extra ingredients here are
an inherited integer order on the finest states and a boundary-witness rule:
adjacent child fibers of one parent precision class are connected through the
last leaf of the left child and first leaf of the right child.

For every finite divisibility chain ``1=d_0 | d_1 | ... | d_t=L`` with the
canonical floor-division projection fibers on ``{0,...,L-1}``, the union of all
such boundary witnesses is exactly the ordinary integer path
``0--1--...--(L-1)``.  This is finite ordered/graph mathematics used as an R004
geometry construction; the integer order and boundary admissibility law are
additional structure, not consequences of hierarchy alone.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Hashable

from enterprise_math.precision_genesis import compatible_paths, scale_chain
from enterprise_math.precision_hierarchy_bridges import boundary_minimal_bridge_edges

Edge = frozenset[int]


def interval_hierarchy(
    scales: Sequence[int],
) -> tuple[tuple[int, ...], dict[int, tuple[int, ...]]]:
    chain = tuple(scales)
    if not chain:
        raise ValueError("scale chain must be nonempty")
    if chain[0] != 1:
        raise ValueError("ordered interval hierarchy needs one root scale 1")
    paths = compatible_paths(chain)
    finest = chain[-1]
    return chain, {state: paths[state] for state in range(finest)}


def dyadic_interval_hierarchy(
    size: int,
) -> tuple[tuple[int, ...], dict[int, tuple[int, ...]]]:
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return interval_hierarchy(scale_chain(size))


def integer_path_edges(size: int) -> frozenset[Edge]:
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return frozenset(frozenset((state, state + 1)) for state in range(size - 1))


def ordered_boundary_edges_for_scales(scales: Sequence[int]) -> frozenset[Edge]:
    chain, signatures = interval_hierarchy(scales)
    return boundary_minimal_bridge_edges(chain, signatures)


def ordered_boundary_path_theorem_holds_for_scales(scales: Sequence[int]) -> bool:
    chain, _ = interval_hierarchy(scales)
    return ordered_boundary_edges_for_scales(chain) == integer_path_edges(chain[-1])


def ordered_boundary_edges(size: int) -> frozenset[Edge]:
    scales, _ = dyadic_interval_hierarchy(size)
    return ordered_boundary_edges_for_scales(scales)


def ordered_boundary_path_theorem_holds(size: int) -> bool:
    """Dyadic convenience specialization of the general path identity."""
    scales, _ = dyadic_interval_hierarchy(size)
    return ordered_boundary_path_theorem_holds_for_scales(scales)


def ordered_path_distance_for_scales(
    left: int, right: int, scales: Sequence[int]
) -> int:
    chain, _ = interval_hierarchy(scales)
    size = chain[-1]
    if isinstance(left, bool) or isinstance(right, bool):
        raise ValueError("states must be integers")
    if not isinstance(left, int) or not isinstance(right, int):
        raise ValueError("states must be integers")
    if not 0 <= left < size or not 0 <= right < size:
        raise ValueError("state outside declared interval")
    if not ordered_boundary_path_theorem_holds_for_scales(chain):
        raise AssertionError("ordered boundary bridges must form the integer path")
    return abs(left - right)


def ordered_path_distance(left: int, right: int, size: int) -> int:
    scales, _ = dyadic_interval_hierarchy(size)
    return ordered_path_distance_for_scales(left, right, scales)


def ordered_path_ball(center: int, radius: int, size: int) -> frozenset[int]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    scales, _ = dyadic_interval_hierarchy(size)
    if not 0 <= center < size:
        raise ValueError("center outside declared interval")
    return frozenset(
        state
        for state in range(size)
        if ordered_path_distance_for_scales(center, state, scales) <= radius
    )


def hierarchy_matches_declared_order(
    scales: Sequence[int], signatures: Mapping[int, Sequence[Hashable]]
) -> bool:
    """Recognize the canonical interval hierarchy for the declared scale chain."""
    try:
        chain, expected = interval_hierarchy(scales)
    except ValueError:
        return False
    states = tuple(sorted(signatures))
    if states != tuple(range(chain[-1])):
        return False
    return {
        state: tuple(signature) for state, signature in signatures.items()
    } == expected
