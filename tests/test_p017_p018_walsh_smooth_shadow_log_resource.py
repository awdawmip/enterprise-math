from enterprise_math.p017_p018_walsh_smooth_shadow_log_resource import (
    half_cutoff_log_resource,
)


def test_half_cutoff_shadow_is_exact_anchor_coprime_prefix():
    for k in (46, 82, 862, 8191):
        data = half_cutoff_log_resource(k)
        assert data["exact_resource_identity"] is True
        assert data["exact_half_smooth_shadow_Psi"] == data["exact_anchor_coprime_prefix"]


def test_anchor_density_obeys_elementary_telescoping_lower_bound():
    for k in (46, 82, 862, 8191):
        data = half_cutoff_log_resource(k)
        assert (
            data["anchor_density_phi_over_A"]
            >= data["telescoping_density_lower_2_over_wplus2"]
        )
        assert (
            data["exact_half_smooth_shadow_Psi"]
            >= data["elementary_log_resource_lower"]
        )


def test_factorial_anchor_height_is_below_pronic_center():
    for k in (46, 82, 862, 8191):
        data = half_cutoff_log_resource(k)
        assert data["factorial_anchor_height_lower"] <= data["effective_anchor_product_A"]
        assert data["effective_anchor_product_A"] <= data["pronic_center_upper"]
