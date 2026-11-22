from fractions import Fraction

from enterprise_math.p017_p018_walsh_remainder_descent import (
    selected_modulus_remainder_descent,
    selected_modulus_tent_contribution,
)


def test_selected_modulus_contribution_descends_to_k_mod_m_exactly():
    for k, m in ((46, 31), (82, 55), (82, 85), (862, 577), (862, 899)):
        data = selected_modulus_remainder_descent(k, m)
        assert data["selected_modulus_remainder_descent_exact"] is True
        assert data["selected_contribution_at_k"] == data["reconstructed_from_remainder_scale"]
        assert data["scaled_boundary_numerator"] == k * data["selected_contribution_at_k"]


def test_exact_nonzero_example_matches_local_boundary_scale():
    data = selected_modulus_remainder_descent(82, 55)
    assert data["remainder_r"] == 27
    assert data["selected_contribution_at_k"] == Fraction(5, 41)
    assert data["selected_contribution_at_remainder_scale"] == Fraction(10, 27)
    assert Fraction(27, 82) * Fraction(10, 27) == Fraction(5, 41)


def test_transverse_selected_modulus_tent_sum_is_exact_fraction():
    value = selected_modulus_tent_contribution(46, 31)
    assert isinstance(value, Fraction)
