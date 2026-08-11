from fractions import Fraction

from enterprise_math.p022_barlow_franel_gessel_lucas_copy import (
    franel_formal_derivative,
    franel_formal_derivative_recurrence_residual,
    franel_gessel_lucas_mod_square,
    simple_zero_copy_linear_residue,
    two_multipliers_cannot_both_raise_depth,
)


def test_franel_formal_derivative_initial_values_and_recurrence() -> None:
    assert franel_formal_derivative(0) == 0
    assert franel_formal_derivative(1) == 3
    assert franel_formal_derivative(2) == Fraction(33, 2)
    assert franel_formal_derivative(3) == 100
    for n in range(1, 9):
        assert franel_formal_derivative_recurrence_residual(n) == 0


def test_gessel_lucas_mod_square_on_primitive_franel_copies() -> None:
    for rank, prime in ((6, 13), (6, 73), (15, 179)):
        for multiplier in (1, 2):
            actual, predicted = franel_gessel_lucas_mod_square(rank, prime, multiplier)
            assert actual == predicted
            assert actual % prime == 0


def test_simple_copy_first_jet_is_linear_in_multiplier() -> None:
    for rank, prime in ((6, 13), (6, 73), (15, 179)):
        for multiplier in (1, 2):
            actual, predicted = simple_zero_copy_linear_residue(rank, prime, multiplier)
            assert actual == predicted


def test_two_distinct_copy_multipliers_cannot_both_raise_depth() -> None:
    for rank, prime in ((6, 13), (6, 73), (15, 179)):
        first, second = two_multipliers_cannot_both_raise_depth(rank, prime, 1, 2)
        assert first != 0 or second != 0
