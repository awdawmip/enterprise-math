from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.relation_support_precision import coarse_partition_threshold_matrix
from enterprise_math.support_language_quotient import (
    primitive_support_family,
    recover_metric_from_support_family,
    support_relation_from_metric,
    support_word_relation,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_primitive_support_family_reconstructs_metric_exactly() -> None:
    sizes = (2, 3, 1, 4)
    totals = (1, 7, -1, 10)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    family = primitive_support_family(metric)
    assert recover_metric_from_support_family(len(metric), family) == metric


def test_support_words_are_determined_by_metric_only() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 5)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    for radii in ((0,), (1,), (1, 1), (1, 2, 1), (0, 3, 0, 2)):
        relation = support_word_relation(metric, radii)
        # Re-evaluate via primitive metric thresholding to ensure no A3 data is read.
        direct = support_relation_from_metric(metric, radii[0])
        from enterprise_math.support_language_quotient import compose_relations

        for radius in radii[1:]:
            direct = compose_relations(direct, support_relation_from_metric(metric, radius))
        assert relation == direct


def test_same_metric_can_have_different_a3_partition_aggregation() -> None:
    sizes = (2, 2, 2, 2)
    first_totals = (-3, -2, -1, 2)
    second_totals = (-3, -1, -2, 2)
    first_field = weighted_relation_field(sizes, first_totals)
    second_field = weighted_relation_field(sizes, second_totals)
    first_metric = integer_relation_distance_matrix(sizes, first_field)
    second_metric = integer_relation_distance_matrix(sizes, second_field)

    expected_metric = (
        (0, 1, 1, 3),
        (1, 0, 1, 2),
        (1, 1, 0, 2),
        (3, 2, 2, 0),
    )
    assert first_metric == expected_metric
    assert second_metric == expected_metric

    partition = ((0, 1), (2, 3))
    first_coarse = coarse_partition_threshold_matrix(sizes, first_field, partition)
    second_coarse = coarse_partition_threshold_matrix(sizes, second_field, partition)
    assert first_coarse[0][1] == 2
    assert second_coarse[0][1] == 1

    # Every support-language word remains identical because it factors through rho.
    for radii in ((0,), (1,), (2,), (1, 1), (1, 2, 1), (3, 0, 2)):
        assert support_word_relation(first_metric, radii) == support_word_relation(
            second_metric, radii
        )
