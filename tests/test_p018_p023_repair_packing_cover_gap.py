from enterprise_math.p018_p023_repair_packing_cover_gap import (
    COVER_LOWER_CORE,
    COVER_WITNESS,
    PACKING_WITNESS,
    RESIDUAL_COMPATIBILITY_CLASS,
    canonical_gap_certificate,
    cover_lower_core_needs_five_types,
    cover_witness_covers_all_hard_targets,
    four_class_coloring_is_valid,
    packing_witness_is_pairwise_incompatible,
)


def test_canonical_packing_cover_gap_certificate() -> None:
    assert canonical_gap_certificate() == (4, 5)


def test_cover_certificates_are_independent() -> None:
    assert len(COVER_WITNESS) == 5
    assert len(COVER_LOWER_CORE) == 7
    assert cover_witness_covers_all_hard_targets()
    assert cover_lower_core_needs_five_types()


def test_packing_certificates_are_independent() -> None:
    assert len(PACKING_WITNESS) == 4
    assert len(RESIDUAL_COMPATIBILITY_CLASS) == 5
    assert packing_witness_is_pairwise_incompatible()
    assert four_class_coloring_is_valid()
