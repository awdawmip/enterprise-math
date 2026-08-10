from fractions import Fraction
from math import factorial

from enterprise_math.p022_barlow_franel_third_index_fixed_hypergeom import (
    fixed_parameter_full_truncation_residue,
)
from enterprise_math.p022_barlow_franel_third_index_hasse_jet import (
    canonical_period_jet_residue,
    canonical_period_term_ratio,
    canonical_period_terminates_before_franel_tail,
    contiguous_gosper_reduction,
    franel_obstruction_from_hasse_jet,
    franel_to_canonical_term_ratio,
    franel_zero_is_fixed_log_derivative,
    gosper_boundary_factor,
    pulled_back_hasse_polynomial_critical_at_one,
)


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1)
    for step in range(length):
        result *= value + step
    return result


def _canonical_term(index: int) -> Fraction:
    return (
        _pochhammer(Fraction(5, 6), index)
        * _pochhammer(Fraction(1, 3), index) ** 2
        / factorial(index) ** 3
    )


def _franel_term(index: int) -> Fraction:
    return (
        _pochhammer(Fraction(-1, 6), index)
        * _pochhammer(Fraction(1, 3), index)
        * _pochhammer(Fraction(4, 3), index)
        / factorial(index) ** 3
    )


def test_term_ratios_against_independent_fraction_oracle() -> None:
    for index in range(0, 8):
        assert canonical_period_term_ratio(index) == (
            _canonical_term(index + 1) / _canonical_term(index)
        )
        assert franel_to_canonical_term_ratio(index) == (
            _franel_term(index) / _canonical_term(index)
        )


def test_exact_gosper_reduction_is_an_identity() -> None:
    for index in range(0, 30):
        left, right = contiguous_gosper_reduction(index)
        assert left == right
        direct = (
            Fraction(-5 - 27 * index)
            + gosper_boundary_factor(index + 1)
            * canonical_period_term_ratio(index)
            - gosper_boundary_factor(index)
        )
        assert direct == left


def test_finite_sum_telescopes_exactly_over_q() -> None:
    for cutoff in range(0, 8):
        left = sum(_franel_term(index) for index in range(cutoff + 1))
        period = sum(_canonical_term(index) for index in range(cutoff + 1))
        theta = sum(
            index * _canonical_term(index)
            for index in range(cutoff + 1)
        )
        boundary = gosper_boundary_factor(cutoff + 1) * _canonical_term(
            cutoff + 1
        )
        right = -5 * period - 27 * theta + boundary
        assert left == right


def test_mod_p_first_jet_bridge_on_small_and_distinguishing_primes() -> None:
    expected = {
        5: (1, 0, 1, 0),
        11: (2, 1, 7, 6),
        17: (3, 12, 13, 11),
        23: (4, 19, 15, 11),
        29: (5, 24, 20, 4),
        41: (7, 13, 1, 13),
        107: (18, 17, 0, 39),
        149: (25, 0, 91, 88),
    }
    for prime, row in expected.items():
        assert franel_obstruction_from_hasse_jet(prime) == row
        assert fixed_parameter_full_truncation_residue(prime) == row[1]
        assert canonical_period_jet_residue(prime) == (
            row[0],
            row[2],
            row[3],
        )
        assert canonical_period_terminates_before_franel_tail(prime)


def test_scalar_hasse_zero_and_franel_zero_are_independent_conditions() -> None:
    # p=107: canonical scalar period vanishes, but Franel obstruction does not.
    _, obstruction_107, period_107, _ = franel_obstruction_from_hasse_jet(107)
    assert period_107 == 0
    assert obstruction_107 == 17

    # p=149: Franel obstruction vanishes while the canonical scalar is a unit.
    _, obstruction_149, period_149, _ = franel_obstruction_from_hasse_jet(149)
    assert period_149 == 91
    assert obstruction_149 == 0


def test_p149_is_the_fixed_log_derivative_and_critical_point_witness() -> None:
    assert franel_zero_is_fixed_log_derivative(149)
    assert pulled_back_hasse_polynomial_critical_at_one(149)

    for prime in (5, 11, 17, 23, 29, 41, 107):
        if canonical_period_jet_residue(prime)[1] != 0:
            assert not franel_zero_is_fixed_log_derivative(prime)
        if prime != 5:
            assert not pulled_back_hasse_polynomial_critical_at_one(prime)
