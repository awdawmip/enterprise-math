from enterprise_math.p022_barlow_half_support_companion import (
    canonical_half_A_relation,
    canonical_half_support_offsets,
    companion_support_avoidance_holds,
    companion_support_equivalence,
    companion_support_hits,
    direct_support_zero_hits,
    midpoint_defect_valuation,
    p157_cancellation_certificate,
    support_valuation_correction,
)


def test_companion_coordinate_matches_direct_support_zero_hits() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 157, 173, 191):
        assert companion_support_equivalence(prime)


def test_target_half_defect_examples_avoid_companion_hits() -> None:
    # These are the proved infinite residue-family examples currently used by
    # the half-index witness theorem.  This is finite regression, not a global
    # proof of support avoidance.
    for prime in (23, 29, 47, 53, 71, 101, 149, 173, 191):
        assert companion_support_hits(prime) == ()
        assert direct_support_zero_hits(prime) == ()
        assert companion_support_avoidance_holds(prime)


def test_p157_is_exact_forced_midpoint_support_cancellation() -> None:
    relation, hits, midpoint_valuation, correction, defect = p157_cancellation_certificate()
    assert relation == canonical_half_A_relation(157)
    assert hits == ((16, 1, 62),)
    assert midpoint_valuation == 1
    assert correction == 1
    assert defect == 0
    assert midpoint_defect_valuation(157) == 0
    assert support_valuation_correction(157) == 1
    assert not companion_support_avoidance_holds(157)


def test_p157_support_offset_explicitly_contains_companion_zero_62() -> None:
    offsets = canonical_half_support_offsets(157)
    assert 62 in offsets
    assert companion_support_hits(157) == ((16, 1, 62),)
