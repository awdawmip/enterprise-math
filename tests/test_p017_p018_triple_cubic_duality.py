from enterprise_math.p017_p018_triple_cubic_duality import triple_cubic_duality_profile


def test_dual_cubic_charts_reconstruct_every_bounded_triple():
    for k in (17, 31, 64, 100, 257):
        data = triple_cubic_duality_profile(k)
        assert data["cubic_pivot_duality"] is True
        for row in data["rows"]:
            assert row["recover_a"] == row["a"]
            assert row["middle_factor_gcd"] == row["b"]
            assert row["recover_c"] == row["c"]
            assert row["D_above_sqrt_U"] is True
            assert row["D_at_most_U_two_thirds"] is True
            assert row["Q_above_X_two_thirds"] is True
            assert row["Q_below_fourth_root_P2_ceiling"] is True


def test_k1000_duality_has_twelve_rows_matching_canonical_pair_count():
    data = triple_cubic_duality_profile(1000)
    assert data["triple_count"] == 12
    assert len(data["dual_chart_pairs"]) == 12
