from fractions import Fraction

import pytest

from enterprise_math.p022_barlow_franel_third_index_gamma_triple import (
    THIRD_INDEX_ALPHA,
    THIRD_INDEX_BETA,
    THIRD_INDEX_CLOSURE_ALPHA,
    THIRD_INDEX_CLOSURE_BETA,
    THIRD_INDEX_CONJUGATE_ALPHA,
    all_gamma_twists,
    dwork_dash,
    ehmm_direct_gamma_barrier,
    frobenius_character_orbits,
    gamma_power,
    gamma_twist_parameters,
    inert_residue_field_size,
    rational_galois_closure_certificate,
    target_character_orbit_closure,
    third_index_dash_cycle,
    third_index_gamma_triple_certificate,
)


def test_explicit_gamma_triple_represents_the_rank_three_datum() -> None:
    assert third_index_gamma_triple_certificate()
    assert gamma_power() == Fraction(-1, 4)


def test_all_six_gamma_twists_are_exact() -> None:
    expected = (
        ((Fraction(1, 2),), (Fraction(1),)),
        (
            (Fraction(1, 3), Fraction(1, 3), Fraction(5, 6)),
            (Fraction(1),) * 3,
        ),
        (
            (
                Fraction(1, 2),
                Fraction(2, 3),
                Fraction(2, 3),
                Fraction(2, 3),
            ),
            (Fraction(1),) * 4,
        ),
        ((Fraction(1, 2),), (Fraction(1),)),
        (
            (
                Fraction(1, 3),
                Fraction(1, 3),
                Fraction(1, 3),
                Fraction(1, 2),
            ),
            (Fraction(1),) * 4,
        ),
        (
            (Fraction(1, 6), Fraction(2, 3), Fraction(2, 3)),
            (Fraction(1),) * 3,
        ),
    )
    assert all_gamma_twists() == expected
    for character, row in enumerate(expected):
        assert gamma_twist_parameters(character) == row
        assert gamma_twist_parameters(character + 6) == row


def test_dwork_dash_is_exactly_the_galois_conjugation_at_inert_primes() -> None:
    for prime in (5, 11, 17, 23, 29, 107, 149):
        original, conjugate, returned = third_index_dash_cycle(prime)
        assert original == tuple(sorted(THIRD_INDEX_ALPHA))
        assert conjugate == tuple(sorted(THIRD_INDEX_CONJUGATE_ALPHA))
        assert returned == original
        assert inert_residue_field_size(prime) == prime * prime


def test_individual_dash_values_make_the_period_two_cycle_transparent() -> None:
    assert dwork_dash(Fraction(5, 6), 5) == Fraction(1, 6)
    assert dwork_dash(Fraction(1, 3), 5) == Fraction(2, 3)
    assert dwork_dash(Fraction(1, 6), 5) == Fraction(5, 6)
    assert dwork_dash(Fraction(2, 3), 5) == Fraction(1, 3)


def test_inert_frobenius_character_orbits_are_exact() -> None:
    for prime in (5, 11, 17, 23, 29, 107, 149):
        assert frobenius_character_orbits(prime) == (
            (0,),
            (1, 5),
            (2, 4),
            (3,),
        )
        assert target_character_orbit_closure(prime)


def test_split_prime_character_orbits_are_singletons() -> None:
    for prime in (7, 13, 19, 31):
        assert frobenius_character_orbits(prime) == (
            (0,),
            (1,),
            (2,),
            (3,),
            (4,),
            (5,),
        )


def test_rational_rank_six_galois_closure_is_exact() -> None:
    assert rational_galois_closure_certificate()
    assert THIRD_INDEX_CLOSURE_ALPHA == (
        Fraction(1, 6),
        Fraction(1, 3),
        Fraction(1, 3),
        Fraction(2, 3),
        Fraction(2, 3),
        Fraction(5, 6),
    )
    assert THIRD_INDEX_CLOSURE_BETA == (Fraction(1),) * 6
    assert target_character_orbit_closure(149)


def test_published_ehmm_sufficient_criterion_does_not_apply_directly() -> None:
    assert ehmm_direct_gamma_barrier() == Fraction(1, 2)


def test_dash_helpers_reject_wrong_prime_class_or_bad_denominator() -> None:
    with pytest.raises(ValueError, match="5 modulo 6"):
        third_index_dash_cycle(7)
    with pytest.raises(ValueError, match="p-adic unit"):
        dwork_dash(Fraction(1, 5), 5)
    with pytest.raises(ValueError, match="coprime to six"):
        frobenius_character_orbits(3)


def test_gamma_character_requires_an_integer() -> None:
    with pytest.raises(ValueError, match="integer"):
        gamma_twist_parameters(True)


def test_original_rank_three_parameters_are_irreducible_against_beta_one() -> None:
    assert all(
        alpha - beta not in (0, 1, -1)
        for alpha in THIRD_INDEX_ALPHA
        for beta in THIRD_INDEX_BETA
    )
