from itertools import product

from enterprise_math.p022_barlow_excursion_repair import (
    absolute_prefix_history,
    excursion_count,
)
from enterprise_math.p022_barlow_orientation_variance import (
    one_sided_orientation_mean,
    one_sided_orientation_second_moment,
    one_sided_orientation_variance,
    return_probability_convolution_identity,
    two_sided_orientation_mean,
    two_sided_orientation_variance,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _one_sided_values(length: int):
    return tuple(
        excursion_count(absolute_prefix_history(word))
        for word in _words(length)
    )


def _reduce_power_two_fraction(numerator: int, denominator: int):
    while numerator and numerator % 2 == 0 and denominator % 2 == 0:
        numerator //= 2
        denominator //= 2
    return numerator, denominator


def test_return_probability_convolution_is_exactly_one() -> None:
    for index in range(0, 50):
        assert return_probability_convolution_identity(index) == (1, 1)


def test_one_sided_mean_and_second_moment_match_direct_words() -> None:
    for length in range(0, 13):
        values = _one_sided_values(length)
        denominator = 2**length
        mean = _reduce_power_two_fraction(sum(values), denominator)
        second = _reduce_power_two_fraction(
            sum(value * value for value in values), denominator
        )
        assert one_sided_orientation_mean(length) == mean
        assert one_sided_orientation_second_moment(length) == second


def test_one_sided_variance_matches_exact_direct_moment_identity() -> None:
    for length in range(0, 13):
        values = _one_sided_values(length)
        denominator = 2**length
        total = sum(values)
        square_total = sum(value * value for value in values)
        variance_num = square_total * denominator - total * total
        variance_den = denominator * denominator
        direct = _reduce_power_two_fraction(variance_num, variance_den)
        assert one_sided_orientation_variance(length) == direct


def test_two_sided_orientation_mean_and_variance_are_independent_sums() -> None:
    for length in range(0, 20):
        one_mean_num, one_mean_den = one_sided_orientation_mean(length)
        two_mean_num, two_mean_den = two_sided_orientation_mean(length)
        assert two_mean_num * one_mean_den == 2 * one_mean_num * two_mean_den

        one_var_num, one_var_den = one_sided_orientation_variance(length)
        two_var_num, two_var_den = two_sided_orientation_variance(length)
        assert two_var_num * one_var_den == 2 * one_var_num * two_var_den


def test_orientation_variance_is_same_order_as_horizon_not_mean_squared_error() -> None:
    # Exact finite inequalities only; the theorem note supplies the asymptotic
    # constant 2*(1-2/pi) for the two-sided variance.
    for length in range(8, 80):
        numerator, denominator = two_sided_orientation_variance(length)
        assert numerator > 0
        # Linear upper bound is intentionally loose but exact and integer-only.
        assert numerator < 2 * length * denominator


def test_relative_fluctuation_does_not_numerically_collapse_on_moderate_horizons() -> None:
    # This is regression evidence for the analytic limit, not the proof.
    ratios = []
    for length in (20, 40, 80, 160):
        mean_num, mean_den = two_sided_orientation_mean(length)
        var_num, var_den = two_sided_orientation_variance(length)
        # Compare CV^2 = Var / Mean^2 as a rational.
        cv2_num = var_num * mean_den * mean_den
        cv2_den = var_den * mean_num * mean_num
        ratios.append(cv2_num / cv2_den)
    # Analytic limit is (pi-2)/4 ~= 0.2854; finite values move toward it.
    assert ratios[-1] > 0.20
    assert ratios[-1] < 0.35
