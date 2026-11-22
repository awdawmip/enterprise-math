from math import gcd

from enterprise_math.p017_p018_carry_primitive_gauss import (
    exact_odd_frequency_gauss_magnitude,
    primitive_global_odd_carry_bound,
    primitive_odd_carry_bound,
)


def test_odd_external_frequency_has_exact_internal_gauss_zero_selection():
    for modulus in (5, 15, 21):
        for frequency in range(1, 2 * modulus, 2):
            for h in range(1, 2 * modulus):
                data = exact_odd_frequency_gauss_magnitude(modulus, h, frequency)
                assert data["selection_law_verified"] is True
                if h % 2 == 0 or frequency % gcd(h, modulus) != 0:
                    assert data["actual_magnitude"] < 1e-8


def test_primitive_odd_single_modulus_carry_modes_have_clean_square_root_bound():
    for modulus in (5, 15, 35, 105):
        for frequency in range(1, 2 * modulus, 2):
            if gcd(frequency, modulus) != 1:
                continue
            data = primitive_odd_carry_bound(modulus, frequency)
            assert data["primitive_odd_bound_verified"] is True
            assert data["coefficient_magnitude"] <= data["primitive_odd_bound"] + 1e-10


def test_primitive_global_odd_mode_is_top_modulus_only_and_bounded():
    for P in (15, 105):
        for frequency in range(1, 2 * P, 2):
            if gcd(frequency, P) != 1:
                continue
            data = primitive_global_odd_carry_bound(P, frequency)
            assert data["top_modulus_square_root_bound_verified"] is True
            assert len(data["source_rows"]) == 1
            assert data["source_rows"][0]["source_modulus"] == P
