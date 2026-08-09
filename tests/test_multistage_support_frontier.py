from enterprise_math.multistage_support_frontier import (
    all_frontiers_are_simplex,
    endpoint_frontier_is_simplex,
    multistage_frontier,
    multistage_supported,
    weak_composition_simplex,
)
from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
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

    # Directly enumerate all two-intermediate chains for small budgets.
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
