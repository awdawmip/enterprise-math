from enterprise_math.p017_p018_walsh_p2_cutoff_pareto import (
    cutoff_reuse_width_ceiling,
    exact_linear_cutoff_zone,
    p2_cutoff_pareto_profile,
    p2_zone_orientation_weight,
)


def test_minimal_p2_cutoff_already_gives_exact_nonnegative_linear_detector():
    k = 46
    z2, C = exact_linear_cutoff_zone(k)
    assert z2 <= C
    rows = []
    for radius in range(1, k):
        for orientation in ("upper", "lower"):
            try:
                row = p2_zone_orientation_weight(k, radius, z2, orientation)
            except ValueError:
                continue
            rows.append(row)
            assert row["linear_weight"] >= 0
            assert (row["linear_weight"] > 0) == row["target_prime"]
    assert rows


def test_reuse_width_decreases_from_p2_cutoff_to_half_cutoff():
    for k in (46, 82, 862):
        z2, C = exact_linear_cutoff_zone(k)
        shallow = cutoff_reuse_width_ceiling(k, z2)
        deep = cutoff_reuse_width_ceiling(k, C)
        assert shallow >= deep
        assert deep <= 2
        assert shallow <= (k - 1) // (z2 + 1) + 1


def test_cutoff_profiles_preserve_prime_signal_and_large_tail_nonreuse():
    for k in (46, 82, 862):
        z2, C = exact_linear_cutoff_zone(k)
        cutoffs = sorted(set((z2, (z2 + C) // 2, C)))
        previous_width = None
        for cutoff in cutoffs:
            data = p2_cutoff_pareto_profile(k, cutoff)
            assert data["proof_depth_reuse_width_pareto"] is True
            assert data["positive_iff_prime_exists"] is True
            assert data["weighted_prime_signal"] > 0
            if previous_width is not None:
                assert data["cutoff_reuse_width_ceiling"] <= previous_width
            previous_width = data["cutoff_reuse_width_ceiling"]
            q_values = [edge["q"] for edge in data["terminal_edges"]]
            assert len(q_values) == len(set(q_values))
            assert max((degree for _p, degree in data["high_prime_degrees"]), default=0) <= data[
                "cutoff_reuse_width_ceiling"
            ]
