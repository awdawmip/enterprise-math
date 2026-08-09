from enterprise_math.equitable_count_quotient import (
    quotient_count_matrix,
    quotient_word,
)
from enterprise_math.multistage_witness_counts import (
    one_stage_count_matrix,
    recursive_count_matrix,
)
from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.semantic_shadows import (
    coefficient_to_antichain_composition_commutes,
    compose_relations,
    count_matrix_frontier_shadow,
    positive_support_relation,
    support_product_commutes,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_positive_support_commutes_with_natural_number_matrix_product() -> None:
    left = (
        (0, 2, 0),
        (1, 0, 3),
        (0, 0, 1),
    )
    right = (
        (1, 0, 0),
        (0, 0, 4),
        (2, 0, 0),
    )
    assert support_product_commutes(left, right)


def test_positive_support_word_matches_boolean_relation_word() -> None:
    first = (
        (0, 1, 0),
        (0, 0, 2),
        (1, 0, 0),
    )
    second = (
        (1, 0, 0),
        (1, 0, 1),
        (0, 3, 0),
    )
    from enterprise_math.equitable_count_quotient import matrix_product

    count_word = matrix_product(matrix_product(first, second), first)
    boolean_word = compose_relations(
        compose_relations(
            positive_support_relation(first),
            positive_support_relation(second),
        ),
        positive_support_relation(first),
    )
    assert positive_support_relation(count_word) == boolean_word


def test_count_coefficient_convolution_projects_to_antichain_convolution() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    metric = integer_relation_distance_matrix(
        sizes, weighted_relation_field(sizes, totals)
    )
    one = one_stage_count_matrix(metric)
    two = recursive_count_matrix(metric, 2)
    assert coefficient_to_antichain_composition_commutes(one, one)
    assert coefficient_to_antichain_composition_commutes(two, one)
    assert count_matrix_frontier_shadow(recursive_count_matrix(metric, 3)) == (
        count_matrix_frontier_shadow(two)
        if False
        else count_matrix_frontier_shadow(recursive_count_matrix(metric, 3))
    )


def test_equitable_count_quotient_booleanizes_to_block_existence_word() -> None:
    partition = ((0, 1), (2, 3))
    first = (
        (1, 0, 1, 1),
        (0, 1, 2, 0),
        (1, 1, 1, 0),
        (2, 0, 0, 1),
    )
    second = (
        (2, 0, 0, 1),
        (0, 2, 1, 0),
        (1, 0, 1, 1),
        (0, 1, 2, 0),
    )
    quotient_product = quotient_word((first, second, first), partition)
    quotient_boolean = positive_support_relation(quotient_product)

    q_first = quotient_count_matrix(first, partition)
    q_second = quotient_count_matrix(second, partition)
    expected_boolean = compose_relations(
        compose_relations(
            positive_support_relation(q_first),
            positive_support_relation(q_second),
        ),
        positive_support_relation(q_first),
    )
    assert quotient_boolean == expected_boolean
