from enterprise_math.relation_support_bridge import integer_relation_distance_matrix
from enterprise_math.staged_witness_counts import (
    budget_witness_count,
    common_target_count_matrix,
    complete_budget_count_table,
    histogram_from_budget_count_table,
    histogram_frontier,
    staged_witness_histogram,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_histogram_and_budget_counts_are_exactly_invertible() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 5)
    field = weighted_relation_field(sizes, totals)
    histogram = staged_witness_histogram(sizes, field, 0, 3)
    table = complete_budget_count_table(histogram)
    assert histogram_from_budget_count_table(table) == histogram


def test_histogram_frontier_matches_existence_shadow() -> None:
    sizes = (10, 10, 10, 10)
    totals = (0, 9, 11, 20)
    field = weighted_relation_field(sizes, totals)
    histogram = staged_witness_histogram(sizes, field, 0, 3)
    assert histogram == (
        ((0, 2), 1),
        ((1, 2), 1),
        ((2, 0), 1),
        ((2, 1), 1),
    )
    assert histogram_frontier(histogram) == ((0, 2), (2, 0))
    assert budget_witness_count(histogram, 2, 2) == 4


def test_same_frontier_but_different_histograms_and_counts() -> None:
    first_sizes = (10, 10, 10)
    first_totals = (0, 9, 20)
    first_field = weighted_relation_field(first_sizes, first_totals)
    first_histogram = staged_witness_histogram(first_sizes, first_field, 0, 2)

    second_sizes = (10, 10, 10, 10)
    second_totals = (0, 9, 11, 20)
    second_field = weighted_relation_field(second_sizes, second_totals)
    second_histogram = staged_witness_histogram(second_sizes, second_field, 0, 3)

    assert histogram_frontier(first_histogram) == histogram_frontier(second_histogram)
    assert first_histogram != second_histogram
    assert budget_witness_count(first_histogram, 2, 2) == 3
    assert budget_witness_count(second_histogram, 2, 2) == 4


def test_natural_number_support_product_matches_histogram_prefix_count() -> None:
    sizes = (1, 1, 1, 1)
    totals = (0, 1, 3, 5)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)

    for left_radius in range(4):
        for right_radius in range(4):
            counts = common_target_count_matrix(metric, left_radius, right_radius)
            for source in range(len(metric)):
                for target in range(len(metric)):
                    histogram = staged_witness_histogram(sizes, field, source, target)
                    assert counts[source][target] == budget_witness_count(
                        histogram, left_radius, right_radius
                    )
