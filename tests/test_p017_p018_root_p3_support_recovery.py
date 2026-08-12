from enterprise_math.p017_p018_root_p3_support_recovery import (
    exact_prime_indicator_from_support_depth,
    odd_token_candidate,
    quadratic_lower_weight_numerator,
    repeated_support_prime_ceiling,
    root_cutoff_token_capacity,
    root_p3_support_profile,
)


def test_exact_support_polynomial_and_quadratic_lower_weight_on_all_depths():
    assert [exact_prime_indicator_from_support_depth(c) for c in range(4)] == [1, 0, 0, 0]
    assert [quadratic_lower_weight_numerator(c) for c in range(4)] == [3, 0, -1, 0]


def test_fourth_root_is_the_first_root_cutoff_with_all_pair_tokens_single_use():
    for k in (16, 31, 64, 127, 257, 1024):
        p3_pair = root_cutoff_token_capacity(k, 3, 2)
        p3_triple = root_cutoff_token_capacity(k, 3, 3)
        p4_pair = root_cutoff_token_capacity(k, 4, 2)
        p4_triple = root_cutoff_token_capacity(k, 4, 3)
        assert p3_pair["structurally_single_use"] is True
        assert p3_pair["token_exceeds_k"] is True
        assert p3_triple["structurally_single_use"] is True
        assert p4_pair["structurally_single_use"] is False
        assert p4_triple["structurally_single_use"] is True


def test_bounded_profiles_recover_prime_count_and_never_reuse_pair_tokens():
    for k in (4, 5, 8, 17, 31, 64, 100, 257):
        data = root_p3_support_profile(k)
        assert data["prime_count"] == data["exact_support_polynomial_prime_count"]
        assert 3 * data["prime_count"] == data["quadratic_identity_rhs"]
        assert data["pair_token_max_usage"] <= 1
        assert data["triple_token_max_usage"] <= 1
        assert data["depth_two_repeated_count"] <= data["repeated_square_column_capacity_bound"]


def test_k1000_checkpoint_exposes_nontrivial_support_depth_distribution():
    data = root_p3_support_profile(1000)
    assert data["fourth_root_cutoff"] == 31
    assert data["rough_count"] == 309
    assert data["support_moment_1"] == 184
    assert data["support_moment_2"] == 39
    assert data["support_moment_3"] == 12
    assert data["support_depth_counts"] == (152, 142, 3, 12)
    assert data["prime_count"] == 152
    assert data["quadratic_certificate_numerator"] == 453
    assert data["quadratic_identity_rhs"] == 456


def test_repeated_prime_ceiling_allows_the_known_k100_counterexample_to_old_bound():
    # 10051 = 19 * 23^2 lies between 100^2 and 101^2.  Here z_3=10 and
    # z_2=21, so the repeated prime 23 disproves the old p<=z_2 claim while
    # satisfying the corrected p<=sqrt(U/(z_3+1)) capacity ceiling.
    assert repeated_support_prime_ceiling(100) >= 23


def test_odd_token_candidate_has_at_most_one_parity_compatible_lift():
    row = odd_token_candidate(100, 11 * 13)
    assert row["single_use"] is True
    assert row["candidate_value"] == row["token"] * row["odd_quotient"]
    assert row["odd_quotient"] % 2 == 1
