"""Ordered boundary bridges turn a dyadic precision hierarchy into a path.

This is an exact finite specialization for R004 geometry research.  Hierarchy
alone does not determine local space; the extra ingredients are an inherited
integer order on fine states and the boundary-witness rule that adjacent child
blocks connect through the last leaf of the left block and first leaf of the
right block.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Hashable

from enterprise_math.precision_genesis import compatible_paths, scale_chain
from enterprise_math.precision_hierarchy_bridges import boundary_minimal_bridge_edges

Edge = frozenset[int]


def dyadic_interval_hierarchy(size: int) -> tuple[tuple[int, ...], dict[int, tuple[int, ...]]]:
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    scales = scale_chain(size)
    paths = compatible_paths(scales)
    return scales, {state: paths[state] for state in range(size)}


def integer_path_edges(size: int) -> frozenset[Edge]:
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return frozenset(frozenset((state, state + 1)) for state in range(size - 1))


def ordered_boundary_edges(size: int) -> frozenset[Edge]:
    scales, signatures = dyadic_interval_hierarchy(size)
    return boundary_minimal_bridge_edges(scales, signatures)


def ordered_boundary_path_theorem_holds(size: int) -> bool:
    """Check the exact identity boundary-bridge union = integer path edges."""
    return ordered_boundary_edges(size) == integer_path_edges(size)


def ordered_path_distance(left: int, right: int, size: int) -> int:
    if isinstance(left, bool) or isinstance(right, bool):
        raise ValueError("states must be integers")
    if not isinstance(left, int) or not isinstance(right, int):
        raise ValueError("states must be integers")
    if not 0 <= left < size or not 0 <= right < size:
        raise ValueError("state outside declared interval")
    if not ordered_boundary_path_theorem_holds(size):
        raise AssertionError("ordered dyadic boundary bridges must form a path")
    return abs(left - right)


def ordered_path_ball(center: int, radius: int, size: int) -> frozenset[int]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if not 0 <= center < size:
        raise ValueError("center outside declared interval")
    return frozenset(
        state
        for state in range(size)
        if ordered_path_distance(center, state, size) <= radius
    )


def hierarchy_matches_declared_order(
    scales: Sequence[int], signatures: Mapping[int, Sequence[Hashable]]
) -> bool:
    """Recognize the canonical interval hierarchy for its declared finest size."""
    states = tuple(sorted(signatures))
    if states != tuple(range(len(states))):
        return False
    expected_scales, expected = dyadic_interval_hierarchy(len(states))
    return tuple(scales) == expected_scales and {
        state: tuple(signature) for state, signature in signatures.items()
    } == expected
