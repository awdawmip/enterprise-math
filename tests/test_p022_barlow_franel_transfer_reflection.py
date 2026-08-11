from fractions import Fraction

from enterprise_math.p022_barlow_franel_transfer_reflection import (
    symmetric_transfer_derivative_from_value,
    symmetric_transfer_log_derivative,
    symmetric_transfer_value,
    transfer_reflection_values,
)


def test_zero_transfer_reflection_on_generic_rational_intervals() -> None:
    cases = (
        (Fraction(1, 3), 2),
        (Fraction(5, 8), 4),
        (Fraction(11, 7), 5),
        (Fraction(-9, 4), 6),
    )
    for parameter, length in cases:
        left, right = transfer_reflection_values(parameter, length)
        assert left == right


def test_symmetric_even_gap_values_match_exact_oracle() -> None:
    expected = {
        2: Fraction(1),
        4: Fraction(145),
        6: Fraction(100009, 9),
        8: Fraction(172943569, 225),
        10: Fraction(2516682289, 49),
    }
    for length, value in expected.items():
        assert symmetric_transfer_value(length) == value
        ratio, predicted = symmetric_transfer_log_derivative(length)
        assert ratio == predicted == Fraction(-4, length - 1)
        assert symmetric_transfer_derivative_from_value(length) == predicted * value
