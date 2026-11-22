from fractions import Fraction

from enterprise_math.p017_p018_biprimitive_boundary_energy import (
    biprimitive_boundary_energy_ceiling,
    primitive_energy_scale_descent,
    primitive_tent_energy,
    primitive_tent_energy_profile,
)


def test_primitive_energy_is_exact_pure_boundary_spectrum():
    expected = {
        (46, 51): Fraction(168, 2346),
        (82, 85): Fraction(198, 6970),
    }
    for key, value in expected.items():
        data = primitive_tent_energy_profile(*key)
        assert data["primitive_tent_energy"] == value
        assert data["energy_is_pure_boundary_for_nontrivial_modulus"] is True
        assert data["bulk_cancelled"] is True


def test_high_product_energy_excludes_zero_mode_exactly():
    for k, m in ((46, 51), (82, 85), (862, 899)):
        data = primitive_tent_energy_profile(k, m)
        assert data["high_zero_mode_ceiling"] == Fraction(m - k, m)
        assert data["primitive_tent_energy"] <= data["high_zero_mode_ceiling"]


def test_primitive_energy_descends_exactly_to_k_mod_m():
    for k, m in ((46, 31), (82, 11), (862, 577), (862, 899)):
        data = primitive_energy_scale_descent(k, m)
        assert data["energy_scale_descent_exact"] is True
        assert data["primitive_energy_at_k"] == data["reconstructed_from_remainder_scale"]
        assert data["primitive_energy_at_k"] <= data["euclidean_boundary_ceiling"]
        if m <= k:
            assert data["primitive_energy_at_k"] <= Fraction(m, 4 * k)


def test_moduli_dividing_k_have_zero_primitive_energy():
    for k, m in ((46, 23), (82, 41), (862, 431)):
        assert k % m == 0
        assert primitive_tent_energy(k, m) == 0


def test_boundary_energy_ceiling_depends_only_on_cross_modulus():
    assert biprimitive_boundary_energy_ceiling(82, 5, 17) == primitive_tent_energy(82, 85)
    assert biprimitive_boundary_energy_ceiling(82, 17, 5) == primitive_tent_energy(82, 85)
