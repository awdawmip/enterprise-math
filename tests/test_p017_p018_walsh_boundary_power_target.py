from enterprise_math.p017_p018_walsh_boundary_power_target import (
    anchor_coprime_prefix_resource,
    anchor_factorial_height_certificate,
    boundary_power_sufficiency_target,
)


def test_anchor_coprime_prefix_is_exactly_inside_smooth_shadow():
    for k, cutoff in ((46, 6), (82, 9), (862, 29), (8191, 90)):
        data = anchor_coprime_prefix_resource(k, cutoff)
        assert data["smooth_shadow_Psi"] >= data["exact_anchor_coprime_prefix_Phi"]
        assert data["smooth_shadow_dominates_prefix"] is True
        assert data["exact_anchor_coprime_prefix_Phi"] >= data["certified_fractional_lower_bound"]


def test_distinct_anchor_product_has_factorial_height_lower_bound():
    for k in (46, 82, 862, 2000, 8191):
        data = anchor_factorial_height_certificate(k)
        assert data["factorial_height_certificate"] is True
        assert data["factorial_lower_bound"] <= data["effective_anchor_product"]
        assert data["effective_anchor_product"] <= data["center_upper_bound"]


def test_future_boundary_theorem_only_needs_to_beat_exact_smooth_resource():
    for k, cutoff in ((862, 29), (8191, 90)):
        data = boundary_power_sufficiency_target(k, cutoff)
        assert data["exact_boundary_loss_ceiling_needed_for_certificate"] == data["smooth_shadow_Psi"] - 1
        assert data["smooth_shadow_Psi"] > 0
        assert data["strict_target"] == "SIGNED_BOUNDARY_LOSS < smooth_shadow_Psi"
