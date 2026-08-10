from enterprise_math.p022_barlow_franel_third_index_bailey_tail import (
    bailey_pole_tail_residue,
    bailey_pole_tail_sum,
    bailey_tail_integer_parameters,
    third_index_zero_via_bailey_tail,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import _is_prime


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


def test_p149_is_a_genuine_third_index_zero_and_p17_is_not() -> None:
    assert third_index_zero_via_bailey_tail(149)
    assert not third_index_zero_via_bailey_tail(17)


def test_tail_has_natural_terminating_integer_parameters() -> None:
    assert bailey_tail_integer_parameters(17) == (-3, -3, 12, 4, 9)
    assert bailey_tail_integer_parameters(149) == (-25, -25, 100, 26, 75)


def test_bailey_tail_reduction_for_primes_below_500() -> None:
    for prime in range(5, 500):
        if prime % 6 == 5 and _is_prime(prime):
            bailey_pole_tail_residue(prime)
            bailey_tail_integer_parameters(prime)


def test_universal_tail_begins_with_exact_rational_values() -> None:
    assert bailey_pole_tail_sum(0).numerator == 5
    assert bailey_pole_tail_sum(0).denominator == 3
    assert bailey_pole_tail_sum(1).numerator == 193
    assert bailey_pole_tail_sum(1).denominator == 63
