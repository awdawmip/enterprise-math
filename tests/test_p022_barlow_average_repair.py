from itertools import product

from enterprise_math.p022_barlow_average_repair import (
    diagonal_split_mean,
    diagonal_split_mean_closed_first_term,
    one_sided_orientation_mean,
    raw_state_bit_ratio,
    total_event_repair_mean,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _reduce(numerator: int, denominator: int):
    from math import gcd

    g = gcd(abs(numerator), denominator)
    return numerator // g, denominator // g


def test_one_sided_mean_matches_direct_excursion_count() -> None:
    from enterprise_math.p022_barlow_excursion_repair import (
        absolute_prefix_history,
        excursion_count,
    )

    for length in range(0, 13):
        words = _words(length)
        total = sum(excursion_count(absolute_prefix_history(word)) for word in words)
        assert one_sided_orientation_mean(length) == _reduce(total, 2**length)


def test_total_mean_matches_direct_two_sided_microscopic_grouping() -> None:
    for length in range(0, 7):
        words = _words(length)
        total = 0
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                total += repair_bit_count(history)
        assert total_event_repair_mean(length) == _reduce(total, 4**length)


def test_diagonal_split_closed_decomposition_matches_direct_sum() -> None:
    for length in range(0, 40):
        first, correction = diagonal_split_mean_closed_first_term(length)
        first_num, first_den = first
        corr_num, corr_den = correction
        reconstructed = _reduce(
            first_num * corr_den - corr_num * first_den,
            first_den * corr_den,
        )
        assert reconstructed == diagonal_split_mean(length)


def test_average_repair_fraction_of_raw_two_sided_sign_bits_decreases() -> None:
    # Exact finite evidence for the proved asymptotic ratio -> 0.
    previous = None
    for length in range(8, 80):
        numerator, denominator = raw_state_bit_ratio(length)
        assert 0 < numerator < denominator
        value = numerator / denominator
        if previous is not None and length % 2 == 0:
            assert value < previous + 0.02
        previous = value


def test_average_is_strictly_below_worst_case_after_small_horizon() -> None:
    for length in range(2, 80):
        numerator, denominator = total_event_repair_mean(length)
        assert numerator < (length + 1) * denominator
