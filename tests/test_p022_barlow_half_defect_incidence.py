from enterprise_math.p022_barlow_half_defect_incidence import (
    companion_hits_match_direct_franel_zeros,
    half_defect_companion_zero_hits,
    half_defect_support_avoidance_generic,
    half_defect_support_exponents_generic,
    half_defect_valuation_terms,
    residual_prime_candidates,
)
from enterprise_math.p022_barlow_franel_lucas_rank import franel_zero_digits


def test_target_family_examples_have_no_support_zero_incidence() -> None:
    for prime in (23, 29, 53, 101, 149, 173, 197, 269, 389, 701):
        assert half_defect_support_avoidance_generic(prime)
        assert half_defect_companion_zero_hits(prime) == ()
        assert companion_hits_match_direct_franel_zeros(prime)


def test_p157_is_exact_cancellation_negative_boundary() -> None:
    # p=157 is forced by mod 8 and has composite p-2, but lies outside the
    # target p=5,23 mod 24 family.  Its earlier zero at j=16 is used with
    # exponent +1 by the canonical A-elimination.
    support = dict(half_defect_support_exponents_generic(157))
    assert support[16] == 1
    assert half_defect_companion_zero_hits(157) == ((16, 62, 1),)
    assert residual_prime_candidates(157, 16) == (31,)
    assert companion_hits_match_direct_franel_zeros(157)

    midpoint_valuation, corrections, total = half_defect_valuation_terms(157)
    assert midpoint_valuation == 1
    assert corrections == ((16, 1, 1),)
    assert total == 0


def test_p173_early_zero_is_not_a_support_hit() -> None:
    # p=173 has a very early Franel zero at j=4 (offset 82), but the canonical
    # support does not contain j=4, so the defect keeps the midpoint witness.
    support = dict(half_defect_support_exponents_generic(173))
    assert 4 not in support
    assert half_defect_companion_zero_hits(173) == ()
    midpoint_valuation, corrections, total = half_defect_valuation_terms(173)
    assert midpoint_valuation == 1
    assert corrections == ()
    assert total == 1


def test_zero_alphabet_cardinality_does_not_determine_defect_survival() -> None:
    assert franel_zero_digits(157) == (16, 75, 78, 81, 140)
    assert franel_zero_digits(389) == (25, 176, 194, 212, 363)
    assert len(franel_zero_digits(157)) == len(franel_zero_digits(389)) == 5

    assert half_defect_valuation_terms(157)[2] == 0
    assert half_defect_valuation_terms(389)[2] == 1
