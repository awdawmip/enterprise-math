from enterprise_math.relation_support_bridge import (
    coarse_pair_supported_from_partition,
    geodesic_defect_matrix,
    integer_relation_distance_matrix,
    missing_interpolations,
    quotient_support_relation,
    split_complete_at,
    support_family_is_admissible,
    unit_graph_realizes_integer_metric,
    unit_graph_shortest_distances,
    universal_fine_support_implies_coarse_support,
    zero_relation_classes,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_zero_relation_quotient_makes_radius_zero_identity() -> None:
    sizes = (1, 2, 1, 3)
    # Equal normalized states: 0/1 == 0/1 and 4/2 == 6/3.
    totals = (0, 4, 0, 6)
    field = weighted_relation_field(sizes, totals)
    classes = zero_relation_classes(sizes, field)
    assert classes == ((0, 2), (1, 3))
    assert quotient_support_relation(sizes, field, 0) == frozenset({(0, 0), (1, 1)})


def test_weighted_relation_support_family_is_admissible() -> None:
    sizes = (1, 2, 3, 1)
    totals = (0, 3, 9, 5)
    field = weighted_relation_field(sizes, totals)
    assert support_family_is_admissible(sizes, field, 8)


def test_universal_fine_support_descends_to_coarse_support() -> None:
    sizes = (1, 2, 1, 3)
    totals = (0, 2, 1, 6)
    field = weighted_relation_field(sizes, totals)
    assert universal_fine_support_implies_coarse_support(
        sizes, field, (0, 1), (2, 3), 2
    )


def test_coarse_support_does_not_imply_universal_fine_support() -> None:
    # Unit-capacity example with exact cancellation across the coarse cut.
    # A=(0,10), B=(0,10): cross differences are 0,-10,10,0 and sum to 0.
    sizes = (1, 1, 1, 1)
    totals = (0, 10, 0, 10)
    field = weighted_relation_field(sizes, totals)
    assert coarse_pair_supported_from_partition(sizes, field, (0, 1), (2, 3), 0)
    assert not all(field[i][j] == 0 for i in (0, 1) for j in (2, 3))


def test_integer_convex_unit_state_has_split_witness() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    assert split_complete_at(sizes, field, 1, 1)
    assert missing_interpolations(sizes, field, 1, 1) == frozenset()


def test_hole_in_unit_state_breaks_split_completeness() -> None:
    sizes = (1, 1)
    totals = (0, 2)
    field = weighted_relation_field(sizes, totals)
    assert not split_complete_at(sizes, field, 1, 1)
    missing = missing_interpolations(sizes, field, 1, 1)
    assert (0, 1) in missing
    assert (1, 0) in missing


def test_integer_relation_metric_recovers_support_filtration() -> None:
    sizes = (1, 2, 3)
    totals = (0, 1, 6)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    assert metric == ((0, 1, 2), (1, 0, 2), (2, 2, 0))
    for radius in range(3):
        expected = frozenset(
            (i, j)
            for i in range(len(metric))
            for j in range(len(metric))
            if metric[i][j] <= radius
        )
        assert quotient_support_relation(sizes, field, radius) == expected


def test_unit_graph_metric_characterizes_global_split_completeness() -> None:
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    metric = integer_relation_distance_matrix(sizes, field)
    graph = unit_graph_shortest_distances(sizes, field)
    assert metric == ((0, 1, 2), (1, 0, 1), (2, 1, 0))
    assert graph == metric
    assert geodesic_defect_matrix(sizes, field) == ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    assert unit_graph_realizes_integer_metric(sizes, field)


def test_missing_midpoint_is_infinite_geodesic_defect() -> None:
    sizes = (1, 1)
    totals = (0, 2)
    field = weighted_relation_field(sizes, totals)
    assert integer_relation_distance_matrix(sizes, field) == ((0, 2), (2, 0))
    assert unit_graph_shortest_distances(sizes, field) == ((0, None), (None, 0))
    assert geodesic_defect_matrix(sizes, field) == ((0, None), (None, 0))
    assert not unit_graph_realizes_integer_metric(sizes, field)


def test_weighted_noninteger_normalized_states_can_be_geodesic() -> None:
    # Normalized values are 0, 1/2, 1. Integer support radius one connects
    # every distinct quotient class, so the unit graph realizes rho exactly.
    sizes = (2, 2, 2)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    assert integer_relation_distance_matrix(sizes, field) == (
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    )
    assert unit_graph_realizes_integer_metric(sizes, field)
