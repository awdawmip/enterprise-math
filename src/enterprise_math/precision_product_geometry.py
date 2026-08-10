"""Cartesian-product geometry from independent ordered precision axes.

Each axis first acquires the exact path geometry supplied by
``precision_ordered_geometry``.  Their Cartesian graph product is then a finite
integer grid.  The shortest-path distance is the ordinary coordinate L1 sum,
consuming the same established graph/lattice mathematics already recognized by
P012 rather than claiming a new metric theorem.

The R004-specific use is diagnostic: the number of independent ordered axes is
additional structural data.  A scalar finest-state capacity does not determine
spatial dimension or macroscopic graph geometry.
"""
from __future__ import annotations

from collections.abc import Sequence
from itertools import product
from math import prod

from enterprise_math.precision_ordered_geometry import (
    ordered_boundary_path_theorem_holds_for_scales,
)

GridState = tuple[int, ...]
GridEdge = frozenset[GridState]


def _axis_sizes(axis_scales: Sequence[Sequence[int]]) -> tuple[int, ...]:
    chains = tuple(tuple(chain) for chain in axis_scales)
    if not chains:
        raise ValueError("at least one ordered precision axis is required")
    sizes = []
    for chain in chains:
        if not ordered_boundary_path_theorem_holds_for_scales(chain):
            raise ValueError("every axis must carry the ordered boundary path law")
        sizes.append(chain[-1])
    return tuple(sizes)


def product_grid_states(axis_scales: Sequence[Sequence[int]]) -> tuple[GridState, ...]:
    sizes = _axis_sizes(axis_scales)
    return tuple(product(*(range(size) for size in sizes)))


def product_grid_edges(axis_scales: Sequence[Sequence[int]]) -> frozenset[GridEdge]:
    sizes = _axis_sizes(axis_scales)
    edges: set[GridEdge] = set()
    for state in product(*(range(size) for size in sizes)):
        for axis, size in enumerate(sizes):
            if state[axis] + 1 >= size:
                continue
            target = list(state)
            target[axis] += 1
            edges.add(frozenset((state, tuple(target))))
    return frozenset(edges)


def product_grid_vertex_count(axis_scales: Sequence[Sequence[int]]) -> int:
    return prod(_axis_sizes(axis_scales))


def product_grid_edge_count(axis_scales: Sequence[Sequence[int]]) -> int:
    sizes = _axis_sizes(axis_scales)
    return sum(
        (size - 1) * prod(other for index, other in enumerate(sizes) if index != axis)
        for axis, size in enumerate(sizes)
    )


def product_grid_distance(
    left: GridState,
    right: GridState,
    axis_scales: Sequence[Sequence[int]],
) -> int:
    sizes = _axis_sizes(axis_scales)
    if len(left) != len(sizes) or len(right) != len(sizes):
        raise ValueError("grid state dimension must match the number of axes")
    for state in (left, right):
        if any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or not 0 <= value < size
            for value, size in zip(state, sizes)
        ):
            raise ValueError("grid coordinate outside declared axis")
    return sum(abs(a - b) for a, b in zip(left, right))


def product_grid_diameter(axis_scales: Sequence[Sequence[int]]) -> int:
    return sum(size - 1 for size in _axis_sizes(axis_scales))


def product_grid_ball(
    center: GridState,
    radius: int,
    axis_scales: Sequence[Sequence[int]],
) -> frozenset[GridState]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    states = product_grid_states(axis_scales)
    return frozenset(
        state
        for state in states
        if product_grid_distance(center, state, axis_scales) <= radius
    )


def equal_capacity_geometry_profiles(capacity: int) -> dict[str, tuple[int, int, int]]:
    """Return canonical power-of-two factorizations exposing dimension nonuniqueness.

    For capacity ``2^m`` this includes a one-axis path of length ``capacity``;
    when ``m`` is even it also includes a square ``2^(m/2) x 2^(m/2)``; and it
    includes the ``m``-dimensional binary cube.  Each tuple is
    ``(dimension, vertex_count, diameter)``.
    """
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    exponent = 0
    value = capacity
    while value > 1 and value % 2 == 0:
        exponent += 1
        value //= 2
    if value != 1:
        raise ValueError("profile helper currently requires a power-of-two capacity")

    profiles = {"path": (1, capacity, capacity - 1)}
    if exponent and exponent % 2 == 0:
        side = 2 ** (exponent // 2)
        profiles["square"] = (2, side * side, 2 * (side - 1))
    if exponent:
        profiles["binary_cube"] = (exponent, 2**exponent, exponent)
    return profiles
