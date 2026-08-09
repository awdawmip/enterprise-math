"""Coarse MAY/MUST two-stage support frontiers.

Each fine endpoint pair has a Pareto-minimal budget frontier for staged support.
For a coarse endpoint block pair:

- MAY is the upward union of those fine truth regions;
- MUST is their upward intersection.

Finite upward unions/intersections are represented exactly by Pareto antichains.
Intersection is computed by coordinatewise joins followed by Pareto pruning.
"""

from __future__ import annotations

from dataclasses import dataclass

from .relation_support_bridge import DistanceMatrix, integer_relation_distance_matrix
from .staged_support_frontier import (
    Frontier,
    pareto_minimal_budgets,
    staged_budget_frontier_from_metric,
    staged_supported_from_frontier,
)
from .weighted_relation_field import WeightedField

ClassPartition = tuple[tuple[int, ...], ...]
FrontierMatrix = tuple[tuple[Frontier, ...], ...]


@dataclass(frozen=True)
class CoarseStagedSupportProfile:
    """Exact all-budget staged MAY/MUST frontiers for one coarse partition."""

    may_frontier: FrontierMatrix
    must_frontier: FrontierMatrix


def _require_partition(class_count: int, partition: ClassPartition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be a non-empty tuple")
    flattened: list[int] = []
    for group in partition:
        if not isinstance(group, tuple) or not group:
            raise ValueError("partition groups must be non-empty tuples")
        if len(set(group)) != len(group):
            raise ValueError("class indices must be unique within a group")
        if any(
            isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= class_count
            for index in group
        ):
            raise ValueError("partition class index out of range")
        flattened.extend(group)
    if sorted(flattened) != list(range(class_count)):
        raise ValueError("partition must cover each class exactly once")


def frontier_union(frontiers: tuple[Frontier, ...]) -> Frontier:
    """Pareto frontier of the union of finite upward-closed truth regions."""
    if not frontiers:
        raise ValueError("at least one frontier is required")
    return pareto_minimal_budgets(point for frontier in frontiers for point in frontier)


def frontier_intersection_two(left: Frontier, right: Frontier) -> Frontier:
    """Pareto frontier of intersection via coordinatewise joins."""
    if not left or not right:
        raise ValueError("frontiers must be nonempty")
    return pareto_minimal_budgets(
        (max(a, c), max(b, d))
        for a, b in left
        for c, d in right
    )


def frontier_intersection(frontiers: tuple[Frontier, ...]) -> Frontier:
    """Exact finite intersection frontier with pruning after each step."""
    if not frontiers:
        raise ValueError("at least one frontier is required")
    result = frontiers[0]
    for frontier in frontiers[1:]:
        result = frontier_intersection_two(result, frontier)
    return result


def coarse_staged_frontiers_from_metric(
    metric: DistanceMatrix, partition: ClassPartition
) -> CoarseStagedSupportProfile:
    """Return exact B17/B18 frontier matrices for one class partition."""
    class_count = len(metric)
    if class_count == 0 or any(len(row) != class_count for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    _require_partition(class_count, partition)

    may_rows: list[tuple[Frontier, ...]] = []
    must_rows: list[tuple[Frontier, ...]] = []
    for left_group in partition:
        may_row: list[Frontier] = []
        must_row: list[Frontier] = []
        for right_group in partition:
            fine_frontiers = tuple(
                staged_budget_frontier_from_metric(metric, source, target)
                for source in left_group
                for target in right_group
            )
            may_row.append(frontier_union(fine_frontiers))
            must_row.append(frontier_intersection(fine_frontiers))
        may_rows.append(tuple(may_row))
        must_rows.append(tuple(must_row))

    return CoarseStagedSupportProfile(
        may_frontier=tuple(may_rows),
        must_frontier=tuple(must_rows),
    )


def coarse_staged_support_profile(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    partition: ClassPartition,
) -> CoarseStagedSupportProfile:
    """Build exact staged MAY/MUST frontiers from an A3 weighted state."""
    return coarse_staged_frontiers_from_metric(
        integer_relation_distance_matrix(block_sizes, field), partition
    )


def coarse_staged_may(
    profile: CoarseStagedSupportProfile,
    left_group: int,
    right_group: int,
    left_radius: int,
    right_radius: int,
) -> bool:
    """Evaluate one staged MAY budget query from the coarse frontier."""
    return staged_supported_from_frontier(
        profile.may_frontier[left_group][right_group],
        left_radius,
        right_radius,
    )


def coarse_staged_must(
    profile: CoarseStagedSupportProfile,
    left_group: int,
    right_group: int,
    left_radius: int,
    right_radius: int,
) -> bool:
    """Evaluate one staged MUST budget query from the coarse frontier."""
    return staged_supported_from_frontier(
        profile.must_frontier[left_group][right_group],
        left_radius,
        right_radius,
    )
