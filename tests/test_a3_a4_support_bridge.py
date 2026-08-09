from enterprise_math.a3_a4_support_bridge import (
    all_cross_pairs_supported,
    coarse_pair_supported_from_partition,
    common_target_support,
    generated_support_relation,
    generated_support_report,
    missing_interpolations,
    split_complete_at,
    universal_fine_support_implies_coarse_support,
    zero_relation_classes,
)
from enterprise_math.admissible_support import common_target_relation
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_zero_classes_and_radius_zero_identity():
    sizes = (1, 2, 1, 3)
    field = weighted_relation_field(sizes, (0, 4, 0, 6))
    assert zero_relation_classes(sizes, field) == ((0, 2), (1, 3))
    assert generated_support_relation(sizes, field, 0) == frozenset({(0, 0), (1, 1)})


def test_generated_family_uses_a4_contract():
    sizes = (1, 2, 3, 1)
    field = weighted_relation_field(sizes, (0, 3, 9, 5))
    report = generated_support_report(sizes, field, 8)
    assert report.zero_identity
    assert report.monotone
    assert report.subadditive


def test_common_target_is_canonical_a4_operation():
    sizes = (1, 1, 1)
    field = weighted_relation_field(sizes, (0, 1, 2))
    relation = generated_support_relation(sizes, field, 1)
    assert common_target_support(sizes, field, 1, 1) == common_target_relation(relation, relation)


def test_split_witness_and_missing_interpolation_cases():
    sizes = (1, 1, 1)
    field = weighted_relation_field(sizes, (0, 1, 2))
    assert split_complete_at(sizes, field, 1, 1)
    assert missing_interpolations(sizes, field, 1, 1) == frozenset()

    sizes = (1, 1)
    field = weighted_relation_field(sizes, (0, 2))
    assert not split_complete_at(sizes, field, 1, 1)
    missing = missing_interpolations(sizes, field, 1, 1)
    assert (0, 1) in missing and (1, 0) in missing


def test_fine_to_coarse_support_is_one_way():
    sizes = (1, 2, 1, 3)
    field = weighted_relation_field(sizes, (0, 2, 1, 6))
    assert all_cross_pairs_supported(sizes, field, (0, 1), (2, 3), 2)
    assert universal_fine_support_implies_coarse_support(sizes, field, (0, 1), (2, 3), 2)

    sizes = (1, 1, 1, 1)
    field = weighted_relation_field(sizes, (0, 10, 0, 10))
    assert coarse_pair_supported_from_partition(sizes, field, (0, 1), (2, 3), 0)
    assert not all_cross_pairs_supported(sizes, field, (0, 1), (2, 3), 0)
