from enterprise_math.coarse_staged_support import (
    coarse_staged_may,
    coarse_staged_must,
    coarse_staged_support_profile,
    frontier_intersection_two,
    frontier_union,
)
from enterprise_math.staged_support_frontier import staged_budget_frontier
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_frontier_union_and_intersection_algebra() -> None:
    first = ((0, 2), (1, 1), (2, 0))
    second = ((0, 1), (1, 0))
    assert frontier_union((first, second)) == second
    assert frontier_intersection_two(first, second) == first


def test_coarse_geodesic_example_has_distinct_may_and_must_frontiers() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    profile = coarse_staged_support_profile(sizes, field, ((0, 1), (2,)))
    assert profile.may_frontier[0][1] == ((0, 1), (1, 0))
    assert profile.must_frontier[0][1] == ((0, 2), (1, 1), (2, 0))
    assert coarse_staged_may(profile, 0, 1, 1, 0)
    assert not coarse_staged_must(profile, 0, 1, 1, 0)
    assert coarse_staged_must(profile, 0, 1, 1, 1)


def test_staged_must_implies_may_for_all_small_budgets() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 5)
    field = weighted_relation_field(sizes, totals)
    profile = coarse_staged_support_profile(sizes, field, ((0, 1), (2, 3)))
    for left_group in range(2):
        for right_group in range(2):
            for left_radius in range(6):
                for right_radius in range(6):
                    if coarse_staged_must(
                        profile,
                        left_group,
                        right_group,
                        left_radius,
                        right_radius,
                    ):
                        assert coarse_staged_may(
                            profile,
                            left_group,
                            right_group,
                            left_radius,
                            right_radius,
                        )


def test_one_step_thresholds_do_not_determine_staged_semantics() -> None:
    # Both endpoint systems have direct distance 2, hence singleton one-step
    # d_minus=d_plus=2.  Only the filled system contains a 1+1 witness.
    filled_sizes = (1, 1, 1)
    filled_totals = (0, 1, 2)
    filled_field = weighted_relation_field(filled_sizes, filled_totals)
    sparse_sizes = (1, 1)
    sparse_totals = (0, 2)
    sparse_field = weighted_relation_field(sparse_sizes, sparse_totals)

    filled = staged_budget_frontier(filled_sizes, filled_field, 0, 2)
    sparse = staged_budget_frontier(sparse_sizes, sparse_field, 0, 1)
    assert filled == ((0, 2), (1, 1), (2, 0))
    assert sparse == ((0, 2), (2, 0))
    assert filled != sparse


def test_coarse_frontiers_match_direct_quantified_semantics() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    field = weighted_relation_field(sizes, totals)
    partition = ((0, 1), (2, 3))
    profile = coarse_staged_support_profile(sizes, field, partition)

    # Fine classes are singleton for these distinct unit values.
    from enterprise_math.relation_support_bridge import integer_relation_distance_matrix

    metric = integer_relation_distance_matrix(sizes, field)
    for left_group, left_members in enumerate(partition):
        for right_group, right_members in enumerate(partition):
            for r in range(7):
                for s in range(7):
                    pair_truths = []
                    for source in left_members:
                        for target in right_members:
                            pair_truths.append(
                                any(
                                    metric[source][middle] <= r
                                    and metric[middle][target] <= s
                                    for middle in range(len(metric))
                                )
                            )
                    assert coarse_staged_may(
                        profile, left_group, right_group, r, s
                    ) == any(pair_truths)
                    assert coarse_staged_must(
                        profile, left_group, right_group, r, s
                    ) == all(pair_truths)
