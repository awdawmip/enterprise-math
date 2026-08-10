from enterprise_math.p017_p018_carry_fourier_conductor import (
    carry_fourier_gauss_reconstruction,
    carry_sawtooth_value,
    mobius_carry_field_fourier_coefficient,
    normalized_carry_fourier_coefficient,
    odd_frequency_squarefree_bound,
)
from enterprise_math.p017_p018_carry_phase_mean import unified_centered_carry_bit


def test_binary_carry_is_exact_ramp_plus_two_quadratic_sawteeth():
    for modulus in (3, 5, 15, 35):
        for K in range(2 * modulus):
            assert abs(carry_sawtooth_value(K, modulus) - unified_centered_carry_bit(K, modulus)) < 1e-12


def test_carry_fourier_coefficients_reconstruct_from_complete_quadratic_gauss_sums():
    for modulus in (5, 15):
        for frequency in range(0, 2 * modulus):
            data = carry_fourier_gauss_reconstruction(modulus, frequency)
            assert abs(data["reconstructed_carry_coefficient"] - data["direct_carry_coefficient"]) < 1e-9
            if frequency % 2 == 1:
                assert data["odd_frequency_is_purely_quadratic"] is True
                assert abs(data["ramp_coefficient"]) < 1e-12


def test_odd_frequency_coefficients_obey_squarefree_gauss_harmonic_bound():
    for modulus in (5, 15, 35, 105):
        bound = odd_frequency_squarefree_bound(modulus)
        for frequency in range(1, 2 * modulus, 2):
            assert abs(normalized_carry_fourier_coefficient(modulus, frequency)) <= bound + 1e-10


def test_global_mobius_field_has_exact_conductor_triangle():
    for P in (15, 105):
        for frequency in range(0, 2 * P):
            data = mobius_carry_field_fourier_coefficient(P, frequency)
            assert abs(data["direct_global_coefficient"] - data["triangular_coefficient"]) < 1e-9


def test_primitive_global_frequency_sees_only_top_modulus():
    P = 105
    for frequency in (1, 2, 11, 13, 16):
        data = mobius_carry_field_fourier_coefficient(P, frequency)
        assert data["primitive_frequency"] is True
        assert len(data["source_rows"]) == 1
        assert data["source_rows"][0]["source_modulus"] == P
