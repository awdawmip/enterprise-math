from fractions import Fraction

from enterprise_math.p017_p018_walsh_asymptotic_sieve import (
    actual_lower_amplifier_mass,
    walsh_continuous_main,
    walsh_sieve_density,
)


def test_local_density_is_product_one_over_p_plus_one():
    assert walsh_sieve_density(46, 3) == Fraction(1, 4)
    assert walsh_sieve_density(46, 5) == Fraction(1, 6)
    assert walsh_sieve_density(46, 15) == Fraction(1, 24)


def test_amplifier_and_upper_sieve_products_cancel_exactly():
    for k in (16, 46, 82, 862):
        data = walsh_continuous_main(k)
        assert data["local_density_cancellation"] is True
        assert data["continuous_sifted_main"] == data["anchor_surviving_continuous_radius_main"]
        assert data["continuous_total_main_X"] * data["upper_sieve_product_V"] == (
            data["continuous_sifted_main"]
        )


def test_actual_finite_A_d_is_exact_main_plus_returned_remainder():
    for k, divisors in ((46, (1, 3, 5, 15)), (82, (1, 3, 5, 7, 15))):
        for d in divisors:
            data = actual_lower_amplifier_mass(k, d)
            assert Fraction(data["actual_A_d"], 1) == (
                data["continuous_main_X_g_d"] + data["finite_remainder_R_d"]
            )


def test_anchor_free_and_anchored_continuous_mains_are_both_supported():
    # k=16 is an anchor-critical parity-only scale; k=46 has effective odd anchor 23.
    critical = walsh_continuous_main(16)
    anchored = walsh_continuous_main(46)
    assert critical["effective_odd_anchors"] == ()
    assert anchored["effective_odd_anchors"] == (23,)
    assert critical["anchor_density"] == 1
    assert anchored["anchor_density"] == Fraction(22, 23)
