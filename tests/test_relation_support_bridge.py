from enterprise_math.relation_support_bridge import (
    coarse_pair_supported_from_partition,
    missing_interpolations,
    quotient_support_relation,
    split_complete_at,
    support_family_is_admissible,
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
    # Values 0,1,2 contain the midpoint needed to split a radius-2 relation
    # into radius-1 followed by radius-1.
    sizes = (1, 1, 1)
    totals = (0, 1, 2)
    field = weighted_relation_field(sizes, totals)
    assert split_complete_at(sizes, field, 1, 1)
    assert missing_interpolations(sizes, field, 1, 1) == frozenset()


def test_hole_in_unit_state_breaks_split_completeness() -> None:
    # Values 0 and 2 are within total radius 2, but there is no quotient class
    # at value 1 to witness a 1+1 split.
    sizes = (1, 1)
    totals = (0, 2)
    field = weighted_relation_field(sizes, totals)
    assert not split_complete_at(sizes, field, 1, 1)
    missing = missing_interpolations(sizes, field, 1, 1)
    assert (0, 1) in missing
    assert (1, 0) in missing
