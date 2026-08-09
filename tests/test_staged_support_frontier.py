from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.staged_support_frontier import (
    all_endpoint_frontiers_are_geodesic,
    detour_frontier_points,
    endpoint_frontier_is_geodesic,
    exact_geodesic_frontier,
    missing_exact_splits,
    pareto_minimal_budgets,
    staged_budget_frontier,
    staged_supported_from_frontier,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_pareto_minimal_budgets_remove_dominated_costs() -> None:
    assert pareto_minimal_budgets(((0, 3), (1, 2), (2, 2), (3, 0), (1, 2))) == (
        (0, 3),
        (1, 2),
        (3, 0),
    )


def test_geodesic_interval_frontier_is_exact_antidiagonal() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    frontier = staged_budget_frontier(sizes, field, 0, 2)
    assert frontier == ((0, 2), (1, 1), (2, 0))
    assert frontier == exact_geodesic_frontier(2)
    assert missing_exact_splits(metric, 0, 2) == ()
    assert detour_frontier_points(metric, 0, 2) == ()
    assert endpoint_frontier_is_geodesic(metric, 0, 2)
    assert all_endpoint_frontiers_are_geodesic(sizes, field)


def test_missing_midpoint_removes_one_exact_split() -> None:
    sizes = (1, 1)
    totals = (0, 2)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    frontier = staged_budget_frontier(sizes, field, 0, 1)
    assert frontier == ((0, 2), (2, 0))
    assert missing_exact_splits(metric, 0, 1) == ((1, 1),)
    assert not staged_supported_from_frontier(frontier, 1, 1)
    assert staged_supported_from_frontier(frontier, 0, 2)
    assert not endpoint_frontier_is_geodesic(metric, 0, 1)


def test_connected_non_geodesic_example_still_misses_11_split() -> None:
    # Equal capacities 10 encode normalized positions 0, 0.7, 1.4, 2
    # without floats.  Unit edges form a connected length-3 chain, while
    # direct rho(0,3)=2.  No intermediate realizes the exact 1+1 split.
    sizes = (10, 10, 10, 10)
    totals = (0, 7, 14, 20)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    assert metric[0][3] == 2
    frontier = staged_budget_frontier(sizes, field, 0, 3)
    assert frontier == ((0, 2), (2, 0))
    assert missing_exact_splits(metric, 0, 3) == ((1, 1),)
    assert not endpoint_frontier_is_geodesic(metric, 0, 3)


def test_two_stage_truth_function_is_reconstructed_from_frontier() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 5, 6)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    frontier = staged_budget_frontier(sizes, field, 0, 3)
    # Check the frontier against direct existential intermediate semantics on
    # all budgets up to the metric diameter.
    diameter = max(max(row) for row in metric)
    for left_radius in range(diameter + 1):
        for right_radius in range(diameter + 1):
            direct = any(
                metric[0][middle] <= left_radius
                and metric[middle][3] <= right_radius
                for middle in range(len(metric))
            )
            assert staged_supported_from_frontier(
                frontier, left_radius, right_radius
            ) == direct
