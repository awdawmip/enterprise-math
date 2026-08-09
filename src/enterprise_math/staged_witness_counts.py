"""Count-complete two-stage witness state for the A3-generated A4 subclass.

For endpoints x,z, the exact cost histogram

    H_xz(a,b) = #{y : rho(x,y)=a and rho(y,z)=b}

is information-equivalent to all budgeted witness-count queries via 2D prefix
sums and integer inclusion-exclusion.  Its Pareto support shadow is the staged
existence frontier.
"""

from __future__ import annotations

from collections import Counter

from .relation_support_bridge import DistanceMatrix, integer_relation_distance_matrix
from .staged_support_frontier import Frontier, pareto_minimal_budgets
from .support_language_quotient import support_relation_from_metric
from .weighted_relation_field import WeightedField

Budget = tuple[int, int]
Histogram = tuple[tuple[Budget, int], ...]
CountMatrix = tuple[tuple[int, ...], ...]


def staged_witness_histogram_from_metric(
    metric: DistanceMatrix, source: int, target: int
) -> Histogram:
    """Return sparse exact H_xz sorted by cost pair."""
    size = len(metric)
    if size == 0 or any(len(row) != size for row in metric):
        raise ValueError("metric must be a non-empty square matrix")
    if not 0 <= source < size or not 0 <= target < size:
        raise ValueError("source and target must index the metric")
    counts = Counter(
        (metric[source][middle], metric[middle][target])
        for middle in range(size)
    )
    return tuple(sorted(counts.items()))


def staged_witness_histogram(
    block_sizes: tuple[int, ...], field: WeightedField, source: int, target: int
) -> Histogram:
    """Build the exact two-stage cost histogram from an A3 weighted state."""
    return staged_witness_histogram_from_metric(
        integer_relation_distance_matrix(block_sizes, field), source, target
    )


def budget_witness_count(histogram: Histogram, left_radius: int, right_radius: int) -> int:
    """2D prefix sum N(r,s) from a sparse exact histogram."""
    if (
        isinstance(left_radius, bool)
        or not isinstance(left_radius, int)
        or left_radius < 0
        or isinstance(right_radius, bool)
        or not isinstance(right_radius, int)
        or right_radius < 0
    ):
        raise ValueError("radii must be non-negative integers")
    return sum(
        count
        for (left_cost, right_cost), count in histogram
        if left_cost <= left_radius and right_cost <= right_radius
    )


def histogram_frontier(histogram: Histogram) -> Frontier:
    """Existence frontier obtained by forgetting counts then Pareto-pruning."""
    if not histogram:
        raise ValueError("histogram must be nonempty")
    if any(count <= 0 for _point, count in histogram):
        raise ValueError("histogram coefficients must be positive")
    return pareto_minimal_budgets(point for point, _count in histogram)


def histogram_from_budget_count_table(table: tuple[tuple[int, ...], ...]) -> Histogram:
    """Recover H by exact 2D finite difference / Möbius inversion."""
    if not table or any(len(row) != len(table[0]) for row in table):
        raise ValueError("count table must be a non-empty rectangle")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for row in table
        for value in row
    ):
        raise ValueError("count table entries must be non-negative integers")

    height = len(table)
    width = len(table[0])

    def value(left: int, right: int) -> int:
        if left < 0 or right < 0:
            return 0
        return table[left][right]

    histogram: list[tuple[Budget, int]] = []
    for left in range(height):
        for right in range(width):
            coefficient = (
                value(left, right)
                - value(left - 1, right)
                - value(left, right - 1)
                + value(left - 1, right - 1)
            )
            if coefficient < 0:
                raise ValueError("table is not a valid 2D cumulative count function")
            if coefficient:
                histogram.append(((left, right), coefficient))
    return tuple(histogram)


def complete_budget_count_table(histogram: Histogram) -> tuple[tuple[int, ...], ...]:
    """Return N(r,s) for 0..max exact cost in each coordinate."""
    if not histogram:
        raise ValueError("histogram must be nonempty")
    max_left = max(point[0] for point, _count in histogram)
    max_right = max(point[1] for point, _count in histogram)
    return tuple(
        tuple(
            budget_witness_count(histogram, left, right)
            for right in range(max_right + 1)
        )
        for left in range(max_left + 1)
    )


def common_target_count_matrix(
    metric: DistanceMatrix, left_radius: int, right_radius: int
) -> CountMatrix:
    """Natural-number product of support matrices M_r M_s."""
    left_relation = support_relation_from_metric(metric, left_radius)
    right_relation = support_relation_from_metric(metric, right_radius)
    size = len(metric)
    left_rows = [set() for _ in range(size)]
    right_rows = [set() for _ in range(size)]
    for source, target in left_relation:
        left_rows[source].add(target)
    for source, target in right_relation:
        right_rows[source].add(target)

    # The generated support metric is symmetric, so y R_s z can be read from
    # right_rows[y].  Count every intermediate y satisfying both stages.
    return tuple(
        tuple(
            sum(
                1
                for middle in range(size)
                if middle in left_rows[source] and target in right_rows[middle]
            )
            for target in range(size)
        )
        for source in range(size)
    )
