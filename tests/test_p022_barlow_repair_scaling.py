from itertools import product
from math import comb

from enterprise_math.p022_barlow_excursion_repair import (
    absolute_prefix_history,
    excursion_count,
)
from enterprise_math.p022_barlow_repair_scaling import (
    average_to_worst_cross_fraction,
    central_binomial_partial_sum_identity,
    diagonal_split_average_common_denominator,
    diagonal_split_average_fraction,
    microscopic_average_two_sided_repair_fraction,
    one_sided_average_excursion_fraction,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_one_sided_average_fraction_matches_direct_words() -> None:
    for length in range(0, 13):
        words = _words(length)
        direct = sum(excursion_count(absolute_prefix_history(word)) for word in words)
        numerator, denominator = one_sided_average_excursion_fraction(length)
        assert numerator * len(words) == direct * denominator


def test_diagonal_split_average_has_two_independent_exact_forms() -> None:
    for length in range(0, 30):
        assert diagonal_split_average_fraction(
            length
        ) == diagonal_split_average_common_denominator(length)


def test_two_sided_average_matches_direct_microscopic_enumeration() -> None:
    for length in range(0, 7):
        words = _words(length)
        direct = 0
        for left in words:
            for right in words:
                direct += two_sided_repair_bit_count(
                    unordered_absolute_pair_history(left, right)
                )
        numerator, denominator = microscopic_average_two_sided_repair_fraction(length)
        assert numerator * (4 ** length) == direct * denominator


def test_central_binomial_partial_sum_identity_is_exact() -> None:
    for length in range(1, 30):
        numerator, denominator = central_binomial_partial_sum_identity(length)
        common = 4 ** (length - 1)
        direct_num = sum(
            comb(2 * time, time) * 4 ** (length - 1 - time)
            for time in range(length)
        )
        assert numerator * common == direct_num * denominator


def test_mean_to_worst_ratio_decreases_on_a_long_finite_window() -> None:
    # Finite evidence for the asymptotic theorem; no floating point is used.
    previous_num, previous_den = average_to_worst_cross_fraction(8)
    for length in range(9, 60):
        numerator, denominator = average_to_worst_cross_fraction(length)
        assert numerator * previous_den < previous_num * denominator
        previous_num, previous_den = numerator, denominator
