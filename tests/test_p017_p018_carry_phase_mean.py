from fractions import Fraction

from enterprise_math.p017_p018_carry_phase_mean import (
    carry_period_profile,
    mobius_weighted_period_mean,
    unified_centered_carry_bit,
)


def _direct_centered_carry(K: int, modulus: int) -> int:
    center = (K + 1) * (K + 2)
    exact = sum(
        1
        for signed_point in range(-K, K + 1)
        if signed_point % 2 != 0 and (center - signed_point) % modulus == 0
    )
    return exact - K // modulus


def test_unified_centered_carry_matches_direct_residue_class_count_across_two_periods():
    for modulus in (1, 3, 5, 7, 15):
        for K in range(4 * modulus):
            carry = unified_centered_carry_bit(K, modulus)
            assert carry in (0, 1)
            assert carry == _direct_centered_carry(K, modulus)


def test_unified_centered_carry_is_periodic_mod_2E():
    for modulus in (3, 5, 15, 105):
        for K in range(2 * modulus):
            assert unified_centered_carry_bit(K, modulus) == unified_centered_carry_bit(
                K + 2 * modulus, modulus
            )


def test_second_half_regression_cases_stay_binary_and_exact():
    assert unified_centered_carry_bit(4, 3) == _direct_centered_carry(4, 3)
    assert unified_centered_carry_bit(7, 5) == _direct_centered_carry(7, 5)


def test_squarefree_period_mass_is_E_plus_one_minus_crt_root_count():
    expected = {
        3: 2,
        5: 4,
        7: 6,
        15: 12,
        21: 18,
        35: 32,
        105: 98,
    }
    for modulus, mass in expected.items():
        data = carry_period_profile(modulus)
        assert data["period_carry_mass"] == mass
        assert data["period_carry_mass"] == (
            modulus + 1 - 2 ** data["omega"]
        )


def test_squarefree_carry_has_universal_two_unit_half_period_skew():
    for modulus in (3, 5, 7, 15, 21, 35, 105):
        data = carry_period_profile(modulus)
        assert data["second_half_carry_mass"] - data["first_half_carry_mass"] == 2
        assert data["first_half_carry_mass"] == (
            modulus - 1 - 2 ** data["omega"]
        ) // 2
        assert data["second_half_carry_mass"] == (
            modulus + 3 - 2 ** data["omega"]
        ) // 2


def test_mobius_weighted_period_mean_factorizes_into_two_local_euler_products():
    data = mobius_weighted_period_mean((3, 5, 7))
    assert data["direct_mobius_period_mean"] == data["factorized_mobius_period_mean"]
    assert data["phi_euler_factor"] == Fraction(16, 35)
    assert data["two_root_euler_factor"] == Fraction(1, 7)
    assert data["factorized_mobius_period_mean"] == Fraction(11, 70)
