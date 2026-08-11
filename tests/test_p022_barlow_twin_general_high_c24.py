from fractions import Fraction

from enterprise_math.p022_barlow_twin_general_high_c24 import (
    c24_fixed_numerator_gcd,
    c24_fixed_transfer_parameters,
    c24_high_to_low_gap,
    c24_source_high_specializes_to_18_24,
)


def test_c24_high_to_low_gap_is_exact_quadratic() -> None:
    for gap in (0, 3, 6, 9, 12):
        s = 2 * gap + 3
        assert c24_high_to_low_gap(gap) == 2 * s * s


def test_source_high_is_the_s3_first_member() -> None:
    assert c24_source_high_specializes_to_18_24()
    assert c24_fixed_transfer_parameters(0) == (
        Fraction(25, 8),
        18,
        Fraction(289, 32),
        24,
    )


def test_first_nontrivial_c24_members_are_coprime_pressure_cases() -> None:
    # These are exact finite Euclidean computations, used as pressure evidence
    # for the unproved one-parameter coprimality/large-common-prime frontier.
    for gap in (3, 6, 9, 12, 15, 18, 21, 24, 27):
        assert c24_fixed_numerator_gcd(gap) == 1
