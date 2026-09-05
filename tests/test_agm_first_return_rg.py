from fractions import Fraction

from enterprise_math.agm_first_return_rg import (
    finite_geometric_channel,
    finite_return_mass,
    finite_shape_update,
    one_shell_shape_update,
    quadratic_universality_bounds,
    required_return_depth,
    s4_predictive_state_cost,
    shape_truncation_error_bound,
    standard_shape_dyadic_exponent,
)


def test_one_shell_formula() -> None:
    for denominator in range(4, 33):
        for numerator in range(0, denominator // 4 + 1):
            s = Fraction(numerator, denominator)
            assert finite_shape_update(s, 1) == one_shell_shape_update(s)


def test_finite_depth_monotone_and_quadratic_bounds() -> None:
    for denominator in range(4, 33):
        for numerator in range(1, denominator // 4 + 1):
            s = Fraction(numerator, denominator)
            lower, upper = quadratic_universality_bounds(s)
            previous = Fraction(0)
            for depth in range(1, 9):
                t = finite_shape_update(s, depth)
                assert previous < t
                assert lower <= t < upper
                previous = t
                assert shape_truncation_error_bound(s, depth) > 0


def test_finite_geometric_channel_decreases_with_depth() -> None:
    h = Fraction(3, 2)
    s = Fraction(1, 5)
    values = [finite_geometric_channel(h, s, depth) for depth in range(1, 9)]
    assert all(left > right for left, right in zip(values, values[1:]))


def test_standard_adaptive_schedule_and_cost() -> None:
    assert [standard_shape_dyadic_exponent(n) for n in range(6)] == [1, 4, 10, 22, 46, 94]
    assert [required_return_depth(256, n) for n in range(9)] == [127, 31, 12, 5, 2, 1, 1, 1, 1]
    assert [s4_predictive_state_cost(depth) for depth in [127, 31, 12, 5, 2, 1]] == [
        3060,
        756,
        300,
        132,
        60,
        36,
    ]


def test_return_mass_is_rational() -> None:
    assert finite_return_mass(Fraction(1, 4), 1) == Fraction(1, 32)
    assert finite_return_mass(Fraction(1, 4), 2) == Fraction(65, 2048)
