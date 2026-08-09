from fractions import Fraction
from itertools import product
from math import comb

from enterprise_math.p022_barlow_repair_variance_asymptotic import (
    cardinal_origin_local_time_mean_fraction,
    cardinal_origin_local_time_second_moment_fraction,
    cardinal_origin_return_probability_fraction,
    finite_total_variance_ratio_fraction,
    lazy_axis_zero_probability_fraction,
    repair_variance_limit_descriptor,
    thinning_martingale_second_moment_fraction,
    wall_surrogate_error_l2_bound_fraction,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_path_statistics(left, right):
    s = 0
    t = 0
    orientation = 0
    axis_u = 0
    axis_v = 0
    origin = 0
    martingale = Fraction(0, 1)

    for left_step, right_step in zip(left, right, strict=True):
        u = (s + t) // 2
        v = (s - t) // 2
        orientation += int(s == 0) + int(t == 0)
        axis_u += int(u == 0)
        axis_v += int(v == 0)
        origin += int(u == 0 and v == 0)

        move_u = int(left_step == right_step)
        move_v = 1 - move_u
        if u == 0:
            martingale += Fraction(2 * move_u - 1, 2)
        if v == 0:
            martingale += Fraction(2 * move_v - 1, 2)

        s += left_step
        t += right_step

    history = unordered_absolute_pair_history(left, right)
    repair = two_sided_repair_bit_count(history)
    surrogate = Fraction(orientation, 1) + Fraction(axis_u + axis_v, 2)
    difference = Fraction(repair, 1) - surrogate
    assert difference == martingale - origin
    return origin, martingale, difference


def test_cardinal_origin_return_probability_matches_direct_pair_walks() -> None:
    for time in range(0, 10):
        words = _words(time)
        direct = sum(
            int(sum(left) == 0 and sum(right) == 0)
            for left in words
            for right in words
        )
        numerator, denominator = cardinal_origin_return_probability_fraction(time)
        assert direct * denominator == numerator * (4**time)


def test_lazy_axis_zero_probability_is_central_binomial() -> None:
    for time in range(0, 30):
        numerator, denominator = lazy_axis_zero_probability_fraction(time)
        assert numerator * (4**time) == comb(2 * time, time) * denominator


def test_origin_local_time_first_two_moments_match_direct_enumeration() -> None:
    for length in range(0, 7):
        words = _words(length)
        values = []
        for left in words:
            for right in words:
                origin, _, _ = _direct_path_statistics(left, right)
                values.append(origin)
        domain = 4**length
        mean_num, mean_den = cardinal_origin_local_time_mean_fraction(length)
        second_num, second_den = cardinal_origin_local_time_second_moment_fraction(length)
        assert sum(values) * mean_den == mean_num * domain
        assert sum(value * value for value in values) * second_den == second_num * domain


def test_thinning_martingale_second_moment_matches_direct_enumeration() -> None:
    for length in range(0, 7):
        words = _words(length)
        square_total = Fraction(0, 1)
        for left in words:
            for right in words:
                _, martingale, _ = _direct_path_statistics(left, right)
                square_total += martingale * martingale
        numerator, denominator = thinning_martingale_second_moment_fraction(length)
        assert square_total * denominator == numerator * (4**length)


def test_wall_surrogate_l2_error_bound_covers_exact_difference() -> None:
    for length in range(0, 7):
        words = _words(length)
        square_total = Fraction(0, 1)
        for left in words:
            for right in words:
                _, _, difference = _direct_path_statistics(left, right)
                square_total += difference * difference
        bound_num, bound_den = wall_surrogate_error_l2_bound_fraction(length)
        assert square_total * bound_den <= bound_num * (4**length)


def test_variance_limit_descriptor_is_exact_symbolic_form() -> None:
    assert repair_variance_limit_descriptor() == (7, 6, 8)


def test_finite_total_variance_ratios_are_positive_after_first_horizon() -> None:
    for length in range(2, 20):
        numerator, denominator = finite_total_variance_ratio_fraction(length)
        assert numerator > 0
        assert denominator > 0
