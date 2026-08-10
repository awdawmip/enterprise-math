from fractions import Fraction

from enterprise_math.p022_barlow_franel_lucas_rank import (
    franel_rank_of_apparition,
    franel_zero_digits,
    primitive_divisor_requires_large_prime,
)
from enterprise_math.p022_barlow_franel_third_index_bailey_tail import (
    bailey_dual_hahn_parameters,
    bailey_pole_tail_residue,
    bailey_pole_tail_sum,
    bailey_symmetric_binomial_denominator,
    bailey_symmetric_integer_identity,
    bailey_symmetric_integer_sum,
    bailey_symmetric_tail_residue,
    bailey_symmetric_transform,
    bailey_tail_integer_parameters,
    bailey_tail_modular_bridge,
    bailey_terminating_tail_sum,
    third_index_zero_via_bailey_tail,
    third_index_zero_via_integer_sum,
    third_index_zero_via_symmetric_tail,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import _is_prime
from enterprise_math.p022_barlow_low_order_identifiability import (
    triple_moment_factor,
)
from enterprise_math.p022_barlow_primitive_defect_criterion import (
    primitive_defect_pivot,
)


def test_bailey_tail_matches_small_third_index_franel_values() -> None:
    expected = {
        5: (2, 0, 1, 0),
        11: (4, 1, 8, 9),
        17: (6, 2, 8, 6),
        23: (8, 3, 22, 11),
        107: (36, 17, 77, 106),
        149: (50, 24, 148, 0),
    }
    for prime, row in expected.items():
        assert bailey_pole_tail_residue(prime) == row


def test_p149_is_a_simple_primitive_composite_boundary_witness() -> None:
    assert third_index_zero_via_bailey_tail(149)
    assert third_index_zero_via_integer_sum(149)
    assert franel_rank_of_apparition(149) == 50
    assert franel_zero_digits(149) == (50, 74, 98)
    assert primitive_divisor_requires_large_prime(50, 149)
    assert (2 * 50 - 1) % 3 == 0

    value = triple_moment_factor(50)
    assert value % 149 == 0
    assert value % (149 * 149) != 0
    assert primitive_defect_pivot(50, 149) == 1


def test_p17_is_not_a_third_index_zero() -> None:
    assert not third_index_zero_via_bailey_tail(17)
    assert not third_index_zero_via_integer_sum(17)


def test_tail_has_natural_terminating_integer_parameters() -> None:
    assert bailey_tail_integer_parameters(17) == (-3, -3, 12, 4, 9)
    assert bailey_tail_integer_parameters(149) == (-25, -25, 100, 26, 75)


def test_bailey_tail_reduction_for_primes_below_500() -> None:
    for prime in range(5, 500):
        if prime % 6 == 5 and _is_prime(prime):
            bailey_pole_tail_residue(prime)
            bailey_tail_integer_parameters(prime)
            left, right = bailey_tail_modular_bridge(prime)
            assert left == right
            assert third_index_zero_via_integer_sum(prime) == (
                bailey_pole_tail_residue(prime)[3] == 0
            )


def test_rational_tail_and_terminating_transform_are_not_equal_over_q() -> None:
    assert bailey_pole_tail_sum(0) == Fraction(65, 63)
    assert bailey_pole_tail_sum(1) == Fraction(22940, 22113)

    assert bailey_terminating_tail_sum(5) == Fraction(5, 3)
    assert bailey_terminating_tail_sum(11) == Fraction(193, 63)

    assert bailey_pole_tail_sum(0) != bailey_terminating_tail_sum(5)
    assert bailey_pole_tail_sum(1) != bailey_terminating_tail_sum(11)


def test_rational_and_terminating_tails_agree_only_after_mod_p_reduction() -> None:
    assert bailey_tail_modular_bridge(5) == (0, 0)
    assert bailey_tail_modular_bridge(11) == (9, 9)
    assert bailey_tail_modular_bridge(17) == (6, 6)
    assert bailey_tail_modular_bridge(149) == (0, 0)


def test_terminating_tail_has_exact_symmetric_three_parameter_form() -> None:
    for prime in (5, 11, 17, 23, 149):
        original, transformed = bailey_symmetric_transform(prime)
        assert original == transformed

    assert bailey_symmetric_tail_residue(5) == (0, 4, 0)
    assert bailey_symmetric_tail_residue(11) == (9, 8, 8)
    assert bailey_symmetric_tail_residue(149) == (0, 22, 0)


def test_symmetric_tail_integerizes_to_a_single_binomial_sum() -> None:
    expected = (10, 386, 18712, 1004866, 57203510)
    for truncation, value in enumerate(expected, start=1):
        assert bailey_symmetric_integer_sum(truncation) == value

    for prime in (5, 11, 17, 23, 149):
        denominator, integer_sum, scaled = bailey_symmetric_integer_identity(prime)
        assert denominator % prime != 0
        assert integer_sum == scaled

    assert bailey_symmetric_binomial_denominator(1) == 9
    assert bailey_symmetric_binomial_denominator(2) == 315


def test_symmetric_tail_is_a_dual_hahn_diagonal() -> None:
    assert bailey_dual_hahn_parameters(17) == (3, 3, 8, -15, 9, -9)
    assert bailey_dual_hahn_parameters(149) == (
        25,
        25,
        74,
        -125,
        75,
        -625,
    )


def test_symmetric_tail_detects_the_same_third_index_zeros() -> None:
    assert third_index_zero_via_symmetric_tail(5)
    assert third_index_zero_via_symmetric_tail(149)
    for prime in (11, 17, 23, 107):
        assert not third_index_zero_via_symmetric_tail(prime)
