from enterprise_math.p017_p018_walsh_smooth_shadow_main import (
    anchor_coprime_smooth_shadow,
    walsh_linear_floor_main,
)


def test_smooth_shadow_exactly_equals_constant_floor_minus_disjoint_medium_columns():
    expected = {
        (46, 6): (22, 8, 14),
        (82, 9): (40, 14, 26),
        (862, 29): (430, 201, 229),
        (8191, 90): (4095, 2181, 1914),
    }
    for (k, cutoff), (B0, linear, psi) in expected.items():
        data = anchor_coprime_smooth_shadow(k, cutoff)
        assert data["constant_anchor_floor_B0"] == B0
        assert data["linear_medium_floor_sum"] == linear
        assert data["smooth_shadow_count_Psi"] == psi
        assert B0 - linear == psi
        assert data["exact_floor_main_equals_smooth_shadow"] is True


def test_half_cutoff_smooth_shadow_is_the_complete_anchor_coprime_shadow():
    k = 8191
    cutoff = (k - 1) // 2
    data = anchor_coprime_smooth_shadow(k, cutoff)
    assert data["repeatable_medium_primes"] == ()
    assert data["linear_medium_floor_sum"] == 0
    assert data["smooth_shadow_count_Psi"] == data["constant_anchor_floor_B0"] == 4095


def test_walsh_floor_main_is_integer_smooth_shadow_not_an_euler_heuristic():
    for k, cutoff in ((46, 6), (82, 9), (862, 29)):
        data = walsh_linear_floor_main(k, cutoff)
        assert data["one_orientation_reusable_floor_main"] == data["smooth_shadow_count_Psi"]
        assert data["symmetric_reusable_floor_main"] == 2 * data["smooth_shadow_count_Psi"]
        assert data["remaining_nonconstant_terms"] == "FINITE_BOUNDARY_ONLY"
