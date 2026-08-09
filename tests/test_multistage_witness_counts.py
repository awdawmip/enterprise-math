from enterprise_math.multistage_support_frontier import multistage_frontier_from_metric
from enterprise_math.multistage_witness_counts import (
    convolve_count_matrices,
    count_histogram_frontier,
    multistage_budget_count,
    multistage_count_histogram,
    multistage_count_histogram_from_metric,
    one_stage_count_matrix,
    recursive_count_matrix,
)
from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_count_tensor_positive_support_projects_to_existence_frontier() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 2, 3, 6)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    for stages in range(1, 4):
        histogram = multistage_count_histogram_from_metric(metric, 0, 3, stages)
        assert count_histogram_frontier(histogram) == multistage_frontier_from_metric(
            metric, 0, 3, stages
        )


def test_recursive_coefficient_convolution_matches_direct_chain_counting() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 5)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    for stages in range(1, 4):
        recursive = recursive_count_matrix(metric, stages)
        for source in range(len(metric)):
            for target in range(len(metric)):
                assert recursive[source][target] == multistage_count_histogram_from_metric(
                    metric, source, target, stages
                )


def test_count_convolution_is_associative() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 3)
    metric = integer_relation_distance_matrix(
        sizes, weighted_relation_field(sizes, totals)
    )
    one = one_stage_count_matrix(metric)
    two = convolve_count_matrices(one, one)
    assert convolve_count_matrices(two, one) == convolve_count_matrices(one, two)


def test_geodesic_existence_can_have_different_multiplicity() -> None:
    # A: normalized positions 0, 0.75, 1.5.
    first_sizes = (20, 20, 20)
    first_totals = (0, 15, 30)
    first_field = weighted_relation_field(first_sizes, first_totals)
    first_metric = integer_relation_distance_matrix(first_sizes, first_field)
    first_histogram = multistage_count_histogram(first_sizes, first_field, 0, 2, 2)

    # B: normalized positions 0, 0.6, 0.9, 1.5.
    second_sizes = (20, 20, 20, 20)
    second_totals = (0, 12, 18, 30)
    second_field = weighted_relation_field(second_sizes, second_totals)
    second_metric = integer_relation_distance_matrix(second_sizes, second_field)
    second_histogram = multistage_count_histogram(second_sizes, second_field, 0, 3, 2)

    assert first_metric[0][2] == 2
    assert second_metric[0][3] == 2
    assert count_histogram_frontier(first_histogram) == (
        (0, 2),
        (1, 1),
        (2, 0),
    )
    assert count_histogram_frontier(second_histogram) == count_histogram_frontier(
        first_histogram
    )
    assert multistage_budget_count(first_histogram, (1, 1)) == 1
    assert multistage_budget_count(second_histogram, (1, 1)) == 2
