from fractions import Fraction
from math import comb

from enterprise_math.p022_barlow_franel_midpoint_transversality import (
    midpoint_central_harmonic_lift_quotient,
    midpoint_derivative_lift_quotient,
    midpoint_harmonic_lift_quotient,
    midpoint_transversality_profile,
    parameter_derivative_harmonic_mod,
    parameter_derivative_table_mod,
)
from enterprise_math.p022_barlow_half_defect_obstructions import half_index_lift_quotient
from enterprise_math.p022_barlow_low_order_defect_reduction import primes_through


def _parameter_derivative_exact(index: int) -> Fraction:
    harmonic = [Fraction(0, 1)]
    for k in range(1, index + 1):
        harmonic.append(harmonic[-1] + Fraction(1, k))
    return 3 * sum(
        Fraction(comb(index, k) ** 3, 1)
        * (harmonic[index] - harmonic[index - k])
        for k in range(index + 1)
    )


def test_differentiated_recurrence_matches_direct_harmonic_derivative() -> None:
    for prime in (7, 11, 13, 23, 29):
        stop = min((prime - 1) // 2, 10)
        table = parameter_derivative_table_mod(prime, stop)
        for index in range(stop + 1):
            direct = parameter_derivative_harmonic_mod(prime, index)
            exact = _parameter_derivative_exact(index)
            exact_mod = exact.numerator * pow(exact.denominator, -1, prime) % prime
            assert table[index] == direct == exact_mod


def test_midpoint_derivative_and_both_harmonic_forms_equal_p2_lift() -> None:
    for prime in primes_through(251):
        if prime > 2 and prime % 8 in (5, 7):
            expected = half_index_lift_quotient(prime)
            assert midpoint_derivative_lift_quotient(prime) == expected
            assert midpoint_harmonic_lift_quotient(prime) == expected
            assert midpoint_central_harmonic_lift_quotient(prime) == expected


def test_known_transversality_profiles_are_nonzero() -> None:
    expected = {
        5: 2,
        7: 1,
        13: 11,
        23: 2,
        29: 2,
        47: 41,
        53: 34,
        71: 69,
        101: 38,
    }
    for prime, lift in expected.items():
        derivative, derivative_lift, direct_lift, transverse = midpoint_transversality_profile(prime)
        assert derivative_lift == direct_lift == lift
        assert derivative == (2 * lift) % prime
        assert transverse
