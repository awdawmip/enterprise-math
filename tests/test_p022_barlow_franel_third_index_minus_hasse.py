from fractions import Fraction
from math import factorial

from enterprise_math.p022_barlow_franel_half_integer_solution import (
    integer_midpoint_companion,
)
from enterprise_math.p022_barlow_franel_third_index_hasse_jet import (
    canonical_period_jet_residue,
)
from enterprise_math.p022_barlow_franel_third_index_minus_hasse import (
    forced_diagonal_companion_hasse_bridge,
    forced_diagonal_zero_iff_scalar_hasse_zero,
    third_minus_hasse_bridge,
    third_minus_zero_iff_scalar_hasse_zero,
    whipple_third_minus_identity,
    whipple_third_minus_sum,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    triple_moment_factor,
)


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1)
    for step in range(length):
        result *= value + step
    return result


def _independent_whipple(k: int) -> Fraction:
    total = Fraction(0)
    for index in range(k):
        total += (
            _pochhammer(Fraction(2 * k), index)
            * _pochhammer(Fraction(1, 2) - k, index)
            * _pochhammer(Fraction(1 - k), index)
            / factorial(index) ** 3
        )
    return total


def test_exact_whipple_transform_matches_small_franel_numbers() -> None:
    for k in range(1, 9):
        assert whipple_third_minus_sum(k) == _independent_whipple(k)
        assert whipple_third_minus_identity(k)
        index = 2 * k - 1
        assert (
            2**index * whipple_third_minus_sum(k)
            == triple_moment_factor(index)
        )


def test_one_third_minus_is_exactly_the_canonical_scalar_hasse_coordinate() -> None:
    expected = {
        11: (2, 1, 7),
        17: (3, 8, 13),
        23: (4, 11, 15),
        29: (5, 3, 20),
        41: (7, 33, 1),
        107: (18, 0, 0),
        149: (25, 46, 91),
    }
    for prime, row in expected.items():
        k, franel, period, predicted = third_minus_hasse_bridge(prime)
        assert (k, franel, period) == row
        assert franel == predicted
        assert period == canonical_period_jet_residue(prime)[1]
        assert third_minus_zero_iff_scalar_hasse_zero(prime) == (period == 0)


def test_q107_is_the_shared_scalar_hasse_and_one_third_minus_zero() -> None:
    assert third_minus_zero_iff_scalar_hasse_zero(107)
    assert triple_moment_factor(35) % 107 == 0
    assert canonical_period_jet_residue(107)[1] == 0


def test_forced_midpoint_diagonal_companion_is_the_same_zero_condition() -> None:
    for prime in (5, 23, 29, 53, 71, 149):
        k, companion, period, predicted = forced_diagonal_companion_hasse_bridge(
            prime
        )
        assert companion == integer_midpoint_companion(k) % prime
        assert companion == predicted
        assert forced_diagonal_zero_iff_scalar_hasse_zero(prime) == (
            period == 0
        )


def test_known_target_primes_are_scalar_ordinary_on_the_diagonal() -> None:
    for prime in (23, 29, 53, 71, 149, 173, 191):
        if prime % 6 == 5 and prime % 8 in (5, 7):
            _, companion, period, _ = forced_diagonal_companion_hasse_bridge(
                prime
            )
            assert companion != 0
            assert period != 0
