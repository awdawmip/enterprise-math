from itertools import product
from math import comb

from enterprise_math.p022_barlow_repair_covariance import (
    microscopic_total_repair_variance,
)
from enterprise_math.p022_barlow_repair_variance_bound import (
    lazy_axis_local_time_mean_fraction,
    lazy_axis_local_time_second_moment_fraction,
    split_second_moment_linear_bound,
    total_repair_variance_linear_bound,
    two_sided_orientation_second_moment_fraction,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    total_zero_departure_events,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_lazy_return_convolution_is_exactly_one() -> None:
    for total in range(0, 40):
        denominator = 4**total
        numerator = sum(
            comb(2 * left, left)
            * comb(2 * (total - left), total - left)
            for left in range(total + 1)
        )
        assert numerator == denominator


def test_lazy_axis_second_moment_matches_direct_cardinal_walk_enumeration() -> None:
    # Enumerate the four cardinal steps as integers 0..3 and track U only.
    increments = (1, -1, 0, 0)
    for length in range(0, 8):
        total_l = 0
        total_l2 = 0
        for steps in product(increments, repeat=length):
            u = 0
            local_time = 0
            for step in steps:
                local_time += int(u == 0)
                u += step
            total_l += local_time
            total_l2 += local_time * local_time
        domain = 4**length
        mean_num, mean_den = lazy_axis_local_time_mean_fraction(length)
        second_num, second_den = lazy_axis_local_time_second_moment_fraction(length)
        assert total_l * mean_den == mean_num * domain
        assert total_l2 * second_den == second_num * domain


def test_two_sided_orientation_second_moment_matches_direct_words() -> None:
    for length in range(0, 7):
        words = _words(length)
        total = 0
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                orientation = total_zero_departure_events(history)
                total += orientation * orientation
        numerator, denominator = two_sided_orientation_second_moment_fraction(length)
        assert total * denominator == numerator * (4**length)


def test_split_second_moment_obeys_axis_local_time_bound() -> None:
    for length in range(0, 7):
        words = _words(length)
        total_b2 = 0
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                split = diagonal_split_count(history)
                total_b2 += split * split
        assert total_b2 <= split_second_moment_linear_bound(length) * (4**length)


def test_exact_total_variance_is_below_linear_certificate() -> None:
    for length in range(0, 40):
        numerator, denominator = microscopic_total_repair_variance(length)
        assert numerator <= total_repair_variance_linear_bound(length) * denominator
