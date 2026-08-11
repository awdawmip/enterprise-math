from enterprise_math.p017_p018_walsh_half_cutoff_bridge import (
    half_cutoff_bridge_profile,
    half_cutoff_orientation_weight,
)


def test_half_rough_composite_has_one_single_use_high_prime_and_zero_weight():
    data = half_cutoff_orientation_weight(17, 7, "lower")
    assert data["target_state"] == 299  # 13*23
    assert data["target_low_support"] == ()
    assert data["target_high_support"] == (13,)
    assert data["terminal_high_prime_hit_count"] == 1
    assert data["half_cutoff_terminal_weight"] == 0
    assert data["high_prime_deletion_single_use"] is True
    assert data["target_prime"] is False


def test_prime_side_weight_matches_existing_incidence_optimal_compiler():
    data = half_cutoff_orientation_weight(17, 1, "upper")
    assert data["target_state"] == 307
    assert data["target_prime"] is True
    assert data["terminal_high_prime_hit_count"] == 0
    assert data["half_cutoff_terminal_weight"] > 0
    assert data["exact_prime_detector"] is True


def test_weighted_terminal_buchstab_identity_and_prime_positivity():
    for k in (17, 46, 82):
        data = half_cutoff_bridge_profile(k)
        assert data["weighted_terminal_identity"] is True
        assert (
            data["low_band_amplified_half_rough_mass"]
            - data["single_use_high_prime_deletion_mass"]
            == data["incidence_optimal_weighted_prime_signal"]
        )
        assert data["incidence_optimal_weighted_prime_signal"] > 0
        assert data["positive_iff_prime_exists"] is True
        labels = [(orientation, p) for orientation, p, _r in data["deletion_labels"]]
        assert len(labels) == len(set(labels))
