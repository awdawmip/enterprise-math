"""Arbitrary-depth exact witness-count tensors for staged support.

A sparse histogram maps each exact k-stage cost vector to the number of
represented labeled chains having that cost.  Matrix convolution multiplies
prefix/suffix counts and sums over split states.  Positive coefficient support,
followed by Pareto pruning, recovers the existence-only frontier.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

from .multistage_support_frontier import (
    BudgetVector,
    MultiFrontier,
    pareto_minimal_vectors,
)
from .relation_support_bridge import DistanceMatrix, integer_relation_distance_matrix
from .weighted_relation_field import WeightedField

CountHistogram = tuple[tuple[BudgetVector, int], ...]
CountHistogramMatrix = tuple[tuple[CountHistogram, ...], ...]


def multistage_count_histogram_from_metric(
    metric: DistanceMatrix, source: int, target: int, stages: int
) -> CountHistogram:
    """Exact H^(k)_xz by finite represented-chain enumeration."""
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    if not 0 <= source < size or not 0 <= target < size:
        raise ValueError("source and target must index the metric")
    if isinstance(stages, bool) or not isinstance(stages, int) or stages <= 0:
        raise ValueError("stages must be a positive integer")

    counts: Counter[BudgetVector] = Counter()
    if stages == 1:
        counts[(metric[source][target],)] = 1
    else:
        for intermediate in product(range(size), repeat=stages - 1):
            chain = (source,) + intermediate + (target,)
            cost = tuple(
                metric[chain[index]][chain[index + 1]] for index in range(stages)
            )
            counts[cost] += 1
    return tuple(sorted(counts.items()))


def multistage_count_histogram(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    source: int,
    target: int,
    stages: int,
) -> CountHistogram:
    """Build exact count tensor for one A3-generated endpoint pair."""
    return multistage_count_histogram_from_metric(
        integer_relation_distance_matrix(block_sizes, field), source, target, stages
    )


def multistage_budget_count(histogram: CountHistogram, budget: BudgetVector) -> int:
    """Count represented chains whose exact cost vector fits the budget."""
    if not histogram:
        raise ValueError("histogram must be nonempty")
    dimension = len(histogram[0][0])
    if len(budget) != dimension:
        raise ValueError("budget dimension must match histogram dimension")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in budget):
        raise ValueError("budget coordinates must be non-negative integers")
    return sum(
        count
        for cost, count in histogram
        if all(value <= allowance for value, allowance in zip(cost, budget))
    )


def count_histogram_frontier(histogram: CountHistogram) -> MultiFrontier:
    """Positive-support Pareto shadow of a count-complete histogram."""
    if not histogram or any(count <= 0 for _cost, count in histogram):
        raise ValueError("histogram must have positive coefficients")
    return pareto_minimal_vectors(tuple(cost for cost, _count in histogram))


def one_stage_count_matrix(metric: DistanceMatrix) -> CountHistogramMatrix:
    """One-stage coefficient matrix H^(1)_xy(rho_xy)=1."""
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    return tuple(
        tuple((((metric[source][target],), 1),) for target in range(size))
        for source in range(size)
    )


def convolve_count_matrices(
    left: CountHistogramMatrix, right: CountHistogramMatrix
) -> CountHistogramMatrix:
    """Exact B38 coefficient convolution: multiply counts, sum over split states."""
    size = len(left)
    if size == 0 or len(right) != size:
        raise ValueError("count matrices must be nonempty and same size")
    if any(len(row) != size for row in left) or any(len(row) != size for row in right):
        raise ValueError("count matrices must be square")

    rows: list[tuple[CountHistogram, ...]] = []
    for source in range(size):
        row: list[CountHistogram] = []
        for target in range(size):
            counts: Counter[BudgetVector] = Counter()
            for middle in range(size):
                for prefix, prefix_count in left[source][middle]:
                    for suffix, suffix_count in right[middle][target]:
                        counts[prefix + suffix] += prefix_count * suffix_count
            row.append(tuple(sorted(counts.items())))
        rows.append(tuple(row))
    return tuple(rows)


def recursive_count_matrix(metric: DistanceMatrix, stages: int) -> CountHistogramMatrix:
    """Generate H^(stages) recursively from one-stage coefficient state."""
    if isinstance(stages, bool) or not isinstance(stages, int) or stages <= 0:
        raise ValueError("stages must be a positive integer")
    one = one_stage_count_matrix(metric)
    result = one
    for _ in range(1, stages):
        result = convolve_count_matrices(result, one)
    return result
