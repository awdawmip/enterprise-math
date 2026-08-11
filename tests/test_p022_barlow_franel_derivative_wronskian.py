from fractions import Fraction

from enterprise_math.p022_barlow_franel_derivative_wronskian import (
    derivative_wronskian,
    lagrange_coordinate_has_power_two_denominator,
    lagrange_increment_identity,
    two_integral_lagrange_coordinate,
    wronskian_integer_increment,
    wronskian_recurrence_residual,
)


def test_wronskian_first_order_recurrence_is_exact() -> None:
    for index in range(1, 20):
        assert wronskian_recurrence_residual(index) == 0


def test_integrating_factor_increment_is_exact_and_integer_forcing() -> None:
    for index in range(1, 30):
        assert isinstance(wronskian_integer_increment(index), int)
        left, right = lagrange_increment_identity(index)
        assert left == right


def test_lagrange_coordinate_has_only_power_two_denominators() -> None:
    expected = {
        1: Fraction(-3, 2),
        2: Fraction(171, 16),
        3: Fraction(-627, 16),
        4: Fraction(207435, 1024),
        5: Fraction(-2241927, 2048),
    }
    for index, value in expected.items():
        assert two_integral_lagrange_coordinate(index) == value
        assert lagrange_coordinate_has_power_two_denominator(index)


def test_endpoint_wronskian_is_not_trivially_zero() -> None:
    for index in range(0, 12):
        assert derivative_wronskian(index) != 0
