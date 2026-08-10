from fractions import Fraction
from math import factorial

from enterprise_math.p022_barlow_franel_third_index_fixed_hypergeom import (
    fixed_parameter_full_truncation_residue,
    fixed_parameter_integer_bridge,
    fixed_parameter_term_ratio,
    fixed_parameter_truncation_residue,
    third_index_zero_via_fixed_hypergeom,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import _is_prime


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1, 1)
    for step in range(length):
        result *= value + step
    return result


def _fraction_mod_prime(value: Fraction, prime: int) -> int:
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def _direct_full_truncation(prime: int) -> int:
    total = 0
    for k in range(prime):
        term = (
            _pochhammer(Fraction(-1, 6), k)
            * _pochhammer(Fraction(1, 3), k)
            * _pochhammer(Fraction(4, 3), k)
            / factorial(k) ** 3
        )
        total = (total + _fraction_mod_prime(term, prime)) % prime
    return total


def test_fixed_parameter_term_ratio() -> None:
    assert fixed_parameter_term_ratio(0) == Fraction(-2, 27)
    assert fixed_parameter_term_ratio(1) == Fraction(35, 108)


def test_fixed_full_truncation_matches_independent_fraction_oracle() -> None:
    for prime in (5, 11, 17, 23, 29):
        assert prime % 6 == 5
        assert fixed_parameter_full_truncation_residue(prime) == (
            _direct_full_truncation(prime)
        )


def test_integer_and_fixed_hypergeometric_residues_agree() -> None:
    expected = {
        5: 0,
        11: 1,
        17: 12,
        23: 19,
        29: 24,
        107: 17,
        149: 0,
    }
    for prime, residue in expected.items():
        assert fixed_parameter_integer_bridge(prime) == (residue, residue)
        M, truncated = fixed_parameter_truncation_residue(prime)
        assert M == (prime + 1) // 6
        assert truncated == residue


def test_fixed_hypergeometric_detects_same_zeros_below_500() -> None:
    zeros = []
    for prime in range(5, 500):
        if prime % 6 == 5 and _is_prime(prime):
            if third_index_zero_via_fixed_hypergeom(prime):
                zeros.append(prime)
    assert zeros == [5, 149]
