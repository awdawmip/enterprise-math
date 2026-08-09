"""Arbitrary finite-depth Pareto support frontiers.

For a finite integer metric rho, a k-stage represented chain contributes the
vector of k segment costs.  Coordinatewise Pareto minima encode exactly all
k-stage budget queries.  In a geodesic/split-complete metric the frontier is
the integer simplex layer of weak compositions of the endpoint distance.
"""

from __future__ import annotations

from itertools import product

from .relation_support_bridge import DistanceMatrix, integer_relation_distance_matrix
from .weighted_relation_field import WeightedField

BudgetVector = tuple[int, ...]
MultiFrontier = tuple[BudgetVector, ...]


def pareto_minimal_vectors(vectors: tuple[BudgetVector, ...]) -> MultiFrontier:
    """Coordinatewise Pareto minima of a nonempty fixed-dimension vector set."""
    if not vectors:
        raise ValueError("vector set must be nonempty")
    dimension = len(vectors[0])
    if dimension == 0 or any(len(vector) != dimension for vector in vectors):
        raise ValueError("vectors must share one positive dimension")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for vector in vectors
        for value in vector
    ):
        raise ValueError("budget coordinates must be non-negative integers")
    unique = sorted(set(vectors))
    return tuple(
        candidate
        for candidate in unique
        if not any(
            other != candidate
            and all(left <= right for left, right in zip(other, candidate))
            for other in unique
        )
    )


def multistage_frontier_from_metric(
    metric: DistanceMatrix,
    source: int,
    target: int,
    stages: int,
) -> MultiFrontier:
    """Exact F^(k)_xz by finite chain enumeration; reference implementation."""
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    if not 0 <= source < size or not 0 <= target < size:
        raise ValueError("source and target must index the metric")
    if isinstance(stages, bool) or not isinstance(stages, int) or stages <= 0:
        raise ValueError("stages must be a positive integer")

    if stages == 1:
        return ((metric[source][target],),)

    costs: list[BudgetVector] = []
    for intermediate in product(range(size), repeat=stages - 1):
        chain = (source,) + intermediate + (target,)
        costs.append(
            tuple(metric[chain[index]][chain[index + 1]] for index in range(stages))
        )
    return pareto_minimal_vectors(tuple(costs))


def multistage_frontier(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    source: int,
    target: int,
    stages: int,
) -> MultiFrontier:
    """Build a k-stage frontier from an A3 weighted relation state."""
    return multistage_frontier_from_metric(
        integer_relation_distance_matrix(block_sizes, field), source, target, stages
    )


def multistage_supported(frontier: MultiFrontier, budget: BudgetVector) -> bool:
    """Whether one Pareto chain cost fits the declared stage budgets."""
    if not frontier:
        raise ValueError("frontier must be nonempty")
    dimension = len(frontier[0])
    if len(budget) != dimension:
        raise ValueError("budget dimension must match the frontier")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in budget):
        raise ValueError("budget coordinates must be non-negative integers")
    return any(
        all(cost <= allowance for cost, allowance in zip(point, budget))
        for point in frontier
    )


def weak_composition_simplex(total: int, stages: int) -> MultiFrontier:
    """Return Sigma_k(total): all weak compositions of total into k parts."""
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if isinstance(stages, bool) or not isinstance(stages, int) or stages <= 0:
        raise ValueError("stages must be a positive integer")

    def generate(remaining: int, parts: int) -> list[BudgetVector]:
        if parts == 1:
            return [(remaining,)]
        output: list[BudgetVector] = []
        for first in range(remaining + 1):
            for rest in generate(remaining - first, parts - 1):
                output.append((first,) + rest)
        return output

    return tuple(generate(total, stages))


def endpoint_frontier_is_simplex(
    metric: DistanceMatrix,
    source: int,
    target: int,
    stages: int,
) -> bool:
    """Audit B23 for one endpoint pair at one finite stage depth."""
    return multistage_frontier_from_metric(
        metric, source, target, stages
    ) == weak_composition_simplex(metric[source][target], stages)


def all_frontiers_are_simplex(
    block_sizes: tuple[int, ...], field: WeightedField, stages: int
) -> bool:
    """Check the Stage-06 simplex law for every endpoint pair."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    return all(
        endpoint_frontier_is_simplex(metric, source, target, stages)
        for source in range(len(metric))
        for target in range(len(metric))
    )
