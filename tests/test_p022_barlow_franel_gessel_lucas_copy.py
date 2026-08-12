from fractions import Fraction

from enterprise_math.p022_barlow_franel_gessel_lucas_copy import (
    copy_depth_obstruction,
    copy_quotient_linear_residue,
    forced_composite_copy_pair,
    forced_composite_depth_one_pair,
    franel_formal_derivative,
    franel_formal_derivative_recurrence_residual,
    franel_gessel_lucas_mod_square,
    simple_zero_copy_linear_residue,
    source_first_jet_data,
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


def test_forced_composite_pair_uses_same_mod_three_multipliers() -> None:
    assert forced_composite_depth_one_pair(6, 13) == (
        (2, 32, 3),
        (5, 71, 4),
    )
    assert forced_composite_depth_one_pair(6, 73) == (
        (2, 152, 49),
        (5, 371, 66),
    )
    assert forced_composite_depth_one_pair(15, 179) == (
        (1, 194, 59),
        (4, 731, 97),
    )


def test_deep_source_with_nonzero_formal_derivative_copies_back_to_depth_one() -> None:
    # 67 is primitive at F_23 with depth two.  The first jet is nevertheless
    # nonstationary, so every nonzero p-unit multiplier has a simple copy.
    depth, source_unit, derivative = source_first_jet_data(23, 67)
    assert (depth, source_unit, derivative) == (2, 0, 23)
    assert copy_depth_obstruction(23, 67) == (2, 23, False)
    assert copy_quotient_linear_residue(23, 67, 1) == (23, 23)
    assert copy_quotient_linear_residue(23, 67, 2) == (46, 46)


def test_general_forced_pair_matches_simple_pair_on_depth_one_sources() -> None:
    for rank, prime in ((6, 13), (6, 73), (15, 179), (30, 1361)):
        assert forced_composite_copy_pair(rank, prime) == forced_composite_depth_one_pair(
            rank, prime
        )
        assert not copy_depth_obstruction(rank, prime)[2]
