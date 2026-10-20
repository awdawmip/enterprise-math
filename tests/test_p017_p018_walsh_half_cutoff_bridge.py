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
    assert data["terminal_high_prime"] == 13
    assert data["terminal_large_tail_prime"] == 23
    assert data["half_cutoff_terminal_weight"] == 0
    assert data["high_prime_deletion_single_use"] is True
    assert data["target_prime"] is False


def test_prime_side_weight_matches_existing_incidence_optimal_compiler():
    data = half_cutoff_orientation_weight(17, 1, "upper")
    assert data["target_state"] == 307
    assert data["target_prime"] is True
    assert data["terminal_high_prime_hit_count"] == 0
    assert data["terminal_high_prime"] is None
    assert data["terminal_large_tail_prime"] is None
    assert data["half_cutoff_terminal_weight"] > 0
    assert data["exact_prime_detector"] is True


def test_weighted_terminal_buchstab_identity_and_sparse_matching_geometry():
    for k in (17, 46, 82, 862):
        data = half_cutoff_bridge_profile(k)
        assert data["weighted_terminal_identity"] is True
        assert (
            data["low_band_amplified_half_rough_mass"]
            - data["single_use_high_prime_deletion_mass"]
            == data["incidence_optimal_weighted_prime_signal"]
        )
        assert data["incidence_optimal_weighted_prime_signal"] > 0
        assert data["positive_iff_prime_exists"] is True
        assert data["left_high_prime_degree_ceiling"] == 2
        assert data["right_large_tail_degree_ceiling"] == 1
        assert data["terminal_deletion_graph_is_sparse_matching"] is True

        orientation_labels = [(edge["orientation"], edge["p"]) for edge in data["deletion_edges"]]
        assert len(orientation_labels) == len(set(orientation_labels))
        q_values = [edge["q"] for edge in data["deletion_edges"]]
        assert len(q_values) == len(set(q_values))

    # k=862 has an actual left-degree-two p=521 edge pair; its q tails are twin primes.
    data = half_cutoff_bridge_profile(862)
    p521 = sorted(edge["q"] for edge in data["deletion_edges"] if edge["p"] == 521)
    assert p521 == [1427, 1429]
