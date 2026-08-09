"""Pareto-minimal two-stage support budgets for the A3 -> A4 bridge.

For endpoints x,z in the A3 zero-relation quotient and every represented
intermediate y, define the two-stage cost

    (rho(x,y), rho(y,z)).

The coordinatewise Pareto-minimal antichain is an exact finite encoding of all
queries of the form ``(x,z) in R_r ; R_s``.  This is the executable Stage-05
specialization of P023 task-relative repair.
"""

from __future__ import annotations

from collections.abc import Iterable

from .relation_support_bridge import (
    DistanceMatrix,
    integer_relation_distance_matrix,
)
from .weighted_relation_field import WeightedField

Budget = tuple[int, int]
Frontier = tuple[Budget, ...]
FrontierMatrix = tuple[tuple[Frontier, ...], ...]


def pareto_minimal_budgets(points: Iterable[Budget]) -> Frontier:
    """Return the coordinatewise-minimal antichain of a finite budget set."""
    unique = sorted(set(points))
    if not unique:
        raise ValueError("budget set must be nonempty")
    if any(
        isinstance(a, bool)
        or isinstance(b, bool)
        or not isinstance(a, int)
        or not isinstance(b, int)
        or a < 0
        or b < 0
        for a, b in unique
    ):
        raise ValueError("budgets must be pairs of non-negative integers")
    result = []
    for candidate in unique:
        if any(
            other != candidate
            and other[0] <= candidate[0]
            and other[1] <= candidate[1]
            for other in unique
        ):
            continue
        result.append(candidate)
    return tuple(result)


def staged_budget_frontier_from_metric(
    metric: DistanceMatrix, source: int, target: int
) -> Frontier:
    """Return F_xz from a finite integer metric matrix."""
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    if not 0 <= source < size or not 0 <= target < size:
        raise ValueError("source and target must index the metric")
    return pareto_minimal_budgets(
        (metric[source][middle], metric[middle][target])
        for middle in range(size)
    )


def staged_budget_frontier(
    block_sizes: tuple[int, ...], field: WeightedField, source: int, target: int
) -> Frontier:
    """Return the exact staged-budget frontier for one quotient endpoint pair."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    return staged_budget_frontier_from_metric(metric, source, target)


def staged_frontier_matrix(
    block_sizes: tuple[int, ...], field: WeightedField
) -> FrontierMatrix:
    """Return F_xz for all ordered pairs of zero-relation quotient classes."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    return tuple(
        tuple(
            staged_budget_frontier_from_metric(metric, source, target)
            for target in range(len(metric))
        )
        for source in range(len(metric))
    )


def staged_supported_from_frontier(
    frontier: Frontier, left_radius: int, right_radius: int
) -> bool:
    """Answer whether a two-stage budget dominates any Pareto witness cost."""
    if (
        isinstance(left_radius, bool)
        or not isinstance(left_radius, int)
        or left_radius < 0
        or isinstance(right_radius, bool)
        or not isinstance(right_radius, int)
        or right_radius < 0
    ):
        raise ValueError("radii must be non-negative integers")
    return any(a <= left_radius and b <= right_radius for a, b in frontier)


def exact_geodesic_frontier(distance: int) -> Frontier:
    """Return the anti-diagonal G_n={(k,n-k):0<=k<=n}."""
    if isinstance(distance, bool) or not isinstance(distance, int) or distance < 0:
        raise ValueError("distance must be a non-negative integer")
    return tuple((left, distance - left) for left in range(distance + 1))


def missing_exact_splits(metric: DistanceMatrix, source: int, target: int) -> Frontier:
    """Return anti-diagonal exact splits absent from the staged frontier."""
    frontier = set(staged_budget_frontier_from_metric(metric, source, target))
    distance = metric[source][target]
    return tuple(point for point in exact_geodesic_frontier(distance) if point not in frontier)


def detour_frontier_points(metric: DistanceMatrix, source: int, target: int) -> Frontier:
    """Return nondominated staged costs using positive total slack."""
    distance = metric[source][target]
    return tuple(
        point
        for point in staged_budget_frontier_from_metric(metric, source, target)
        if point[0] + point[1] > distance
    )


def endpoint_frontier_is_geodesic(
    metric: DistanceMatrix, source: int, target: int
) -> bool:
    """Audit B16 for one endpoint pair."""
    return staged_budget_frontier_from_metric(
        metric, source, target
    ) == exact_geodesic_frontier(metric[source][target])


def all_endpoint_frontiers_are_geodesic(
    block_sizes: tuple[int, ...], field: WeightedField
) -> bool:
    """Global B16 audit for every endpoint pair."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    return all(
        endpoint_frontier_is_geodesic(metric, source, target)
        for source in range(len(metric))
        for target in range(len(metric))
    )
