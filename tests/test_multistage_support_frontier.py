from enterprise_math.multistage_support_frontier import (
    all_frontiers_are_simplex,
    convolve_frontier_matrices,
    endpoint_frontier_is_simplex,
    multistage_frontier,
    multistage_frontier_from_metric,
    multistage_supported,
    one_stage_frontier_matrix,
    recursive_frontier_matrix,
    weak_composition_simplex,
)
from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.staged_support_frontier import staged_budget_frontier
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_weak_composition_simplex_for_distance_two_depth_three() -> None:
    assert weak_composition_simplex(2, 3) == (
        (0, 0, 2),
        (0, 1, 1),
        (0, 2, 0),
        (1, 0, 1),
        (1, 1, 0),
        (2, 0, 0),
    )


def test_geodesic_state_collapses_every_checked_depth_to_total_budget() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)

    for stages in range(1, 5):
        frontier = multistage_frontier(sizes, field, 0, 2, stages)
        assert frontier == weak_composition_simplex(2, stages)
        assert endpoint_frontier_is_simplex(metric, 0, 2, stages)
        assert all_frontiers_are_simplex(sizes, field, stages)

        # In the geodesic regime, exact support depends only on total budget.
        for budget in weak_composition_simplex(3, stages):
            assert multistage_supported(frontier, budget)


def test_sparse_state_depth_three_frontier_misses_midpoint_compositions() -> None:
    sizes = (1, 1)
    totals = (0, 2)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    frontier = multistage_frontier(sizes, field, 0, 1, 3)
    assert frontier == (
        (0, 0, 2),
        (0, 2, 0),
        (2, 0, 0),
    )
    assert frontier != weak_composition_simplex(2, 3)
    assert not endpoint_frontier_is_simplex(metric, 0, 1, 3)
    assert not multistage_supported(frontier, (1, 1, 0))
    assert multistage_supported(frontier, (0, 0, 2))


def test_multistage_frontier_reconstructs_direct_chain_semantics() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    stages = 3
    frontier = multistage_frontier(sizes, field, 0, 3, stages)

    for r1 in range(4):
        for r2 in range(4):
            for r3 in range(4):
                direct = any(
                    metric[0][first] <= r1
                    and metric[first][second] <= r2
                    and metric[second][3] <= r3
                    for first in range(len(metric))
                    for second in range(len(metric))
                )
                assert multistage_supported(frontier, (r1, r2, r3)) == direct


def test_recursive_convolution_matches_direct_path_enumeration() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)

    for stages in range(1, 5):
        recursive = recursive_frontier_matrix(metric, stages)
        for source in range(len(metric)):
            for target in range(len(metric)):
                assert recursive[source][target] == multistage_frontier_from_metric(
                    metric, source, target, stages
                )


def test_frontier_convolution_is_associative_on_canonical_antichains() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 6)
    metric = integer_relation_distance_matrix(
        sizes, weighted_relation_field(sizes, totals)
    )
    one = one_stage_frontier_matrix(metric)
    two = convolve_frontier_matrices(one, one)
    left = convolve_frontier_matrices(two, one)
    right = convolve_frontier_matrices(one, two)
    assert left == right
    assert left == recursive_frontier_matrix(metric, 3)


def test_same_existence_frontier_can_hide_different_witness_counts() -> None:
    # System A: normalized positions 0,0.9,2.
    first_sizes = (10, 10, 10)
    first_totals = (0, 9, 20)
    first_field = weighted_relation_field(first_sizes, first_totals)
    first_metric = integer_relation_distance_matrix(first_sizes, first_field)
    first_frontier = staged_budget_frontier(first_sizes, first_field, 0, 2)

    # System B adds normalized position 1.1. Its cost (2,1) is dominated,
    # so existence frontier stays unchanged, but witness count grows.
    second_sizes = (10, 10, 10, 10)
    second_totals = (0, 9, 11, 20)
    second_field = weighted_relation_field(second_sizes, second_totals)
    second_metric = integer_relation_distance_matrix(second_sizes, second_field)
    second_frontier = staged_budget_frontier(second_sizes, second_field, 0, 3)

    assert first_frontier == ((0, 2), (2, 0))
    assert second_frontier == first_frontier

    def witness_count(metric, source, target, r, s):
        return sum(
            1
            for middle in range(len(metric))
            if metric[source][middle] <= r and metric[middle][target] <= s
        )

    assert witness_count(first_metric, 0, 2, 2, 2) == 3
    assert witness_count(second_metric, 0, 3, 2, 2) == 4
