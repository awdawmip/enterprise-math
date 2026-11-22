from enterprise_math.p017_p018_balanced_chen_mirror import (
    balanced_chen_mirror_witness,
    least_mirror_product_omega,
    mirror_product_omega,
)


def test_omega_at_most_three_mirror_pair_forces_prime_plus_p2():
    data = balanced_chen_mirror_witness(17, 1)
    assert data["lower_state"] == 305
    assert data["upper_state"] == 307
    assert data["mirror_product_omega"] == 3
    assert data["prime_summand"] == 307
    assert data["p2_summand"] == 305
    assert data["p2_omega"] == 2
    assert data["even_target"] == 612
    assert data["balanced_window_radius"] == 1
    assert data["legendre_certificate"] is True


def test_symmetric_prime_pair_is_strictly_stronger_and_can_fail():
    for k in (17, 19, 46, 58, 64, 67, 85):
        data = least_mirror_product_omega(k)
        assert data["symmetric_prime_pair_exists"] is False
        assert data["least_mirror_product_omega"] == 3
        assert data["omega_at_most_three_witness"] is True


def test_some_larger_pressure_scales_have_even_stronger_prime_prime_witnesses():
    for k in (862, 8191):
        data = least_mirror_product_omega(k)
        assert data["least_mirror_product_omega"] == 2
        assert data["symmetric_prime_pair_exists"] is True
        row = data["best_row"]
        assert row["lower_prime"] is True
        assert row["upper_prime"] is True


def test_both_composite_mirror_pair_has_total_omega_at_least_four():
    # Search a bounded family and verify the L043 multiplicative-depth consequence.
    for k in range(4, 40):
        for radius in range(1, k):
            try:
                row = mirror_product_omega(k, radius)
            except ValueError:
                continue
            if not row["lower_prime"] and not row["upper_prime"]:
                assert row["mirror_product_omega"] >= 4
