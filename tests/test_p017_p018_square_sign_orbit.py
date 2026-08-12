from enterprise_math.p017_p018_square_sign_orbit import (
    fixed_cutoff_square_survivors,
    square_sign_orbit,
    verify_fixed_cutoff_orbit_invariance,
)


def test_square_sign_orbit_size_is_product_of_free_local_signs():
    for k in range(2, 16):
        data = square_sign_orbit(k, 7)
        assert data["orbit_size"] == data["expected_orbit_size"]
        assert data["all_classes_share_square_phase"] is True
        wheel = data["wheel"]
        for x in data["orbit"]:
            assert (x * x - k * k) % wheel == 0


def test_fixed_cutoff_survivor_pattern_is_constant_on_the_sign_orbit():
    for k in range(3, 13):
        data = verify_fixed_cutoff_orbit_invariance(k, 7, 2 * k)
        assert data["fixed_cutoff_orbit_invariant"] is True
        baseline = fixed_cutoff_square_survivors(k, 7, 2 * k)
        for x in data["orbit"]:
            assert fixed_cutoff_square_survivors(x, 7, 2 * k) == baseline


def test_sign_twist_can_change_lift_height_without_changing_fixed_cutoff_data():
    data = verify_fixed_cutoff_orbit_invariance(7, 11, 14)
    assert data["moving_diagonal_data_required"] is True
    assert 7 in data["orbit"]
    assert any(x > 7 for x in data["orbit"])
    for x in data["orbit"]:
        assert fixed_cutoff_square_survivors(x, 11, 14) == data["survivor_offsets"]
