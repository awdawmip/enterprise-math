from enterprise_math.multistage_support_frontier import recursive_frontier_matrix
from enterprise_math.multistage_witness_counts import recursive_count_matrix
from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.semantic_shadows import (
    coefficient_to_antichain_composition_commutes,
    count_matrix_frontier_shadow,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_recursive_count_shadow_equals_independent_antichain_recursion() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    metric = integer_relation_distance_matrix(
        sizes, weighted_relation_field(sizes, totals)
    )
    for stages in range(1, 5):
        count_shadow = count_matrix_frontier_shadow(
            recursive_count_matrix(metric, stages)
        )
        assert count_shadow == recursive_frontier_matrix(metric, stages)


def test_projection_commutes_at_multiple_split_depths() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 4, 6)
    metric = integer_relation_distance_matrix(
        sizes, weighted_relation_field(sizes, totals)
    )
    one = recursive_count_matrix(metric, 1)
    two = recursive_count_matrix(metric, 2)
    three = recursive_count_matrix(metric, 3)
    assert coefficient_to_antichain_composition_commutes(one, two)
    assert coefficient_to_antichain_composition_commutes(two, two)
    assert coefficient_to_antichain_composition_commutes(three, one)
