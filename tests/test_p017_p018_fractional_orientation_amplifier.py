from fractions import Fraction

from enterprise_math.p017_p018_fractional_orientation_amplifier import (
    formal_fractional_sieve_model,
    fractional_local_factor,
    fractional_orientation_floor_coefficient,
    fractional_point_weight,
)


def test_fractional_local_density_remains_dimension_one_for_all_lambda():
    for lam in (Fraction(0), Fraction(1, 2), Fraction(1)):
        data = fractional_local_factor(101, lam)
        assert data["classical_sieve_dimension_first_order"] == 1
        assert data["upper_divisibility_density_g"] == 1 / (Fraction(101) + lam)
        assert data["p_times_g"] > Fraction(99, 100)
        assert data["p_times_g"] <= 1


def test_fractional_orientation_floor_coefficient_interpolates_to_unique_zero_bulk_endpoint():
    assert fractional_orientation_floor_coefficient(1, Fraction(0)) == -1
    assert fractional_orientation_floor_coefficient(3, Fraction(1, 2)) == Fraction(-1, 8)
    for degree in range(1, 7):
        assert fractional_orientation_floor_coefficient(degree, Fraction(1)) == 0


def test_formal_mass_growth_and_target_sieve_product_factor_exactly():
    for lam in (Fraction(0), Fraction(1, 2), Fraction(1)):
        data = formal_fractional_sieve_model(46, lam)
        assert data["formal_sifted_main"] == data["direct_signed_root_mean_product"]
        assert data["formal_sifted_main"] == data["net_decay_euler_product"]
        assert data["classical_target_sieve_dimension"] == 1
    hard = formal_fractional_sieve_model(46, Fraction(1))
    assert hard["net_log_decay_exponent_from_mass_times_sieve"] == 0
    assert hard["dimension_warning"].endswith("not the classical sieve dimension")


def test_fractional_point_weight_preserves_exact_upper_prime_zero_set():
    # At k=17,r=2 the upper state 307 is prime while lower 305=5*61.
    prime_side = fractional_point_weight(17, 2, Fraction(1, 2))
    assert prime_side["upper_prime"] is True
    assert prime_side["fractional_upper_prime_weight"] == Fraction(3, 2)
    assert prime_side["opposite_divisor_expansion"] == Fraction(3, 2)

    # At k=17,r=4 the upper state 309 is composite, so every lambda weight vanishes.
    composite_side = fractional_point_weight(17, 4, Fraction(1, 2))
    assert composite_side["upper_prime"] is False
    assert composite_side["fractional_upper_prime_weight"] == 0
    assert composite_side["positive_iff_upper_prime"] is True
