from fractions import Fraction

from enterprise_math.p022_barlow_franel_boundary_three_section import (
    COMMON_ALPHA_MOD_ONE,
    COMMON_BETA_MOD_ONE,
    boundary_three_section_mod_prime,
    boundary_three_sections,
    common_cyclotomic_signature,
    dwork_complement_signature,
    dwork_period_two_certificate,
    section_term_counts,
)


def test_three_sections_have_equal_exact_horizon() -> None:
    for m in range(1, 8):
        assert section_term_counts(m) == (2 * m, 2 * m, 2 * m)


def test_small_exact_sections() -> None:
    assert boundary_three_sections(1) == (4001, 2745, 1836)
    assert boundary_three_sections(2) == (458054213, 488611992, 414567825)


def test_all_sections_share_one_conductor_18_signature() -> None:
    expected_alpha = tuple(
        sorted(
            (
                Fraction(1, 18),
                Fraction(7, 18),
                Fraction(13, 18),
                Fraction(2, 9),
                Fraction(2, 9),
                Fraction(5, 9),
                Fraction(5, 9),
                Fraction(8, 9),
                Fraction(8, 9),
            )
        )
    )
    expected_beta = tuple(
        sorted(
            (
                Fraction(0),
                Fraction(0),
                Fraction(0),
                Fraction(1, 3),
                Fraction(1, 3),
                Fraction(1, 3),
                Fraction(2, 3),
                Fraction(2, 3),
                Fraction(2, 3),
            )
        )
    )
    assert COMMON_ALPHA_MOD_ONE == expected_alpha
    assert COMMON_BETA_MOD_ONE == expected_beta
    for m in (1, 3, 5, 6):
        # q=18m-1 is prime for these samples.
        assert common_cyclotomic_signature(m) == (expected_alpha, expected_beta)


def test_dwork_dash_is_period_two_when_q_is_minus_one_mod_18() -> None:
    alpha_dash, beta_dash = dwork_complement_signature()
    assert alpha_dash == tuple(
        sorted(
            (
                Fraction(5, 18),
                Fraction(11, 18),
                Fraction(17, 18),
                Fraction(1, 9),
                Fraction(1, 9),
                Fraction(4, 9),
                Fraction(4, 9),
                Fraction(7, 9),
                Fraction(7, 9),
            )
        )
    )
    assert beta_dash == COMMON_BETA_MOD_ONE
    assert dwork_period_two_certificate()


def test_boundary_section_residues_match_regression_samples() -> None:
    assert boundary_three_section_mod_prime(1) == (17, 6, 8, 0)
    assert boundary_three_section_mod_prime(5) == (89, 19, 85, 59)
    assert boundary_three_section_mod_prime(6) == (107, 23, 1, 27)
