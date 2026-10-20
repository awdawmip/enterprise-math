from enterprise_math.p017_p018_walsh_tent_complement_descent import (
    nearest_remainder_selected_descent,
    periodic_root_mean,
    tent_complement_identity,
)


def test_nontrivial_signed_root_function_has_zero_period_mean():
    for center, modulus in ((10, 7), (20, 13), (42, 17), (72, 35)):
        if center % modulus:
            assert periodic_root_mean(center, modulus) == 0


def test_tent_complement_identity_for_fixed_root_phase():
    cases = (
        (20, 13, 7),
        (42, 17, 12),
        (72, 35, 19),
    )
    for center, modulus, radius in cases:
        if center % modulus:
            data = tent_complement_identity(center, modulus, radius)
            assert data["tent_complement_identity"] is True
            assert data["large_tent"] == data["reconstructed_large_tent"]


def test_nearest_remainder_uses_backward_pronic_when_ordinary_remainder_exceeds_half_modulus():
    for k, m in ((46, 7), (46, 13), (82, 17), (100, 13)):
        data = nearest_remainder_selected_descent(k, m)
        assert data["pronic_orientation"] == "BACKWARD"
        assert data["nearest_remainder_delta"] == m - (k % m)
        assert data["parent_selected_tent"] == data["reconstructed_parent"]
        assert data["nearest_remainder_at_most_half_modulus"] is True


def test_forward_nearest_remainder_keeps_standard_pronic_center():
    for k, m in ((46, 15), (82, 35), (100, 21)):
        data = nearest_remainder_selected_descent(k, m)
        assert data["pronic_orientation"] == "FORWARD"
        delta = data["nearest_remainder_delta"]
        assert data["child_center"] == delta * (delta + 1)
        assert data["parent_selected_tent"] == data["reconstructed_parent"]


def test_reusable_symmetric_core_nearest_child_is_below_one_third_and_deep_single_use():
    for k, m in ((46, 7), (46, 13), (46, 15), (82, 17), (82, 35), (100, 21), (100, 37)):
        if m <= (k - 1) // 2 and (k * (k + 1)) % m:
            data = nearest_remainder_selected_descent(k, m)
            assert data["reusable_symmetric_core"] is True
            assert data["reusable_core_child_below_one_third"] is True
            assert data["reusable_core_conductor_exceeds_twice_child"] is True
            assert 3 * data["nearest_remainder_delta"] < k
            assert m > 2 * data["nearest_remainder_delta"]
