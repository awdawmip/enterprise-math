from math import comb

from enterprise_math.p022_barlow_franel_graded_basin import (
    alpha_profile,
    average_valuation_lower_bound_fraction,
    delaygue_valuation_lower_bound,
    forced_midpoint_tower_lower_bound,
    guaranteed_valuation_tail_count,
    odd_level_composite_boundary_tower,
    repeated_midpoint_index,
    total_alpha_load,
    zero_digit_multiplicity,
)
from enterprise_math.p022_barlow_franel_lucas_rank import franel_zero_digit_count


def _franel(index: int) -> int:
    return sum(comb(index, k) ** 3 for k in range(index + 1))


def _valuation(value: int, prime: int) -> int:
    exponent = 0
    while value and value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def test_alpha_profile_partitions_complete_blocks() -> None:
    for prime in (5, 7, 29):
        for length in range(0, 5):
            profile = alpha_profile(prime, length)
            assert sum(profile) == prime**length
            expected_load = sum(alpha * count for alpha, count in enumerate(profile))
            assert expected_load == total_alpha_load(prime, length)


def test_average_lower_bound_matches_digit_count_formula() -> None:
    for prime in (5, 7, 29):
        z = franel_zero_digit_count(prime)
        for length in range(0, 6):
            numerator, denominator = average_valuation_lower_bound_fraction(prime, length)
            assert (numerator, denominator) == (length * z, prime)


def test_delaygue_bound_matches_exact_small_franel_values() -> None:
    for prime, limit in ((5, 50), (7, 45), (29, 35)):
        for value in range(limit + 1):
            alpha = delaygue_valuation_lower_bound(value, prime)
            assert _valuation(_franel(value), prime) >= alpha


def test_repeated_midpoint_tower_has_exact_digit_alpha() -> None:
    for prime in (5, 7, 13, 23):
        for length in range(1, 4):
            value, lower = forced_midpoint_tower_lower_bound(prime, length)
            assert value == repeated_midpoint_index(prime, length)
            assert lower == length
            assert zero_digit_multiplicity(value, prime) == length
            # Keep direct exact checks to short tower points only.
            if value <= 80:
                assert _valuation(_franel(value), prime) >= length


def test_graded_tail_count_is_exact_for_alpha_language() -> None:
    # For p=5, z_p=1. On two digits there are:
    # alpha 0: 4^2=16, alpha 1: 2*4=8, alpha 2: 1.
    assert alpha_profile(5, 2) == (16, 8, 1)
    assert guaranteed_valuation_tail_count(5, 2, 1) == 9
    assert guaranteed_valuation_tail_count(5, 2, 2) == 1


def test_odd_tower_levels_stay_on_composite_boundary_family() -> None:
    for prime in (23, 29, 47, 53):
        for length in (1, 3):
            value, boundary, lower = odd_level_composite_boundary_tower(prime, length)
            assert boundary == prime**length - 2
            assert boundary % 3 == 0
            assert lower == length
            assert value == (prime**length - 1) // 2
