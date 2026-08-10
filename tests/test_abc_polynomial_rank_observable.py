from fractions import Fraction
from math import factorial

from enterprise_math.abc_polynomial_rank_observable import (
    polynomial_boolean_difference,
    polynomial_degree,
    polynomial_value,
    stage111_exact_polynomial_fixture,
)


def test_polynomial_evaluation_and_degree() -> None:
    coefficients = (Fraction(5), Fraction(-3), Fraction(0), Fraction(2))
    assert polynomial_degree(coefficients) == 3
    assert polynomial_value(coefficients, 2) == 5 - 6 + 16


def test_exact_top_coefficient_for_mixed_polynomial() -> None:
    coefficients = (Fraction(5), Fraction(-3), Fraction(0), Fraction(2))
    data = stage111_exact_polynomial_fixture(coefficients)
    assert data["degree"] == 3
    assert data["top_interaction_order"] == 4
    assert data["top_coefficient"] == Fraction(2 * factorial(3), 1)


def test_affine_and_constant_cases() -> None:
    affine = stage111_exact_polynomial_fixture((Fraction(7), Fraction(3)))
    constant = stage111_exact_polynomial_fixture((Fraction(5),))
    assert affine["top_interaction_order"] == 2
    assert affine["top_coefficient"] == 3
    assert constant["top_interaction_order"] == 1
    assert constant["top_coefficient"] == 5


def test_one_order_above_degree_plus_one_vanishes() -> None:
    coefficients = (Fraction(1), Fraction(-2), Fraction(3), Fraction(4))
    data = stage111_exact_polynomial_fixture(coefficients)
    path = data["path"]
    # Add one extra candidate variable by using a degree-four fixture path,
    # then evaluate the degree-three polynomial across four candidates + one future.
    larger = stage111_exact_polynomial_fixture((Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1)))
    assert polynomial_boolean_difference(
        larger["path"],
        coefficients,
        (0, 1, 2, 3),
        (0,),
    ) == 0
