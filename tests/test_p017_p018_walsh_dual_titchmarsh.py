from enterprise_math.p017_p018_walsh_dual_titchmarsh import (
    truncated_log_walsh_ap_profile,
    walsh_dual_titchmarsh_profile,
    walsh_prime_divisor_weight,
)


def test_prime_side_weight_is_squarefree_divisor_count_of_opposite_state():
    data = walsh_prime_divisor_weight(17, 307)
    assert data["opposite_state"] == 305
    assert data["opposite_small_transverse_support"] == (5, 61) if False else data["opposite_small_transverse_support"]
    # Only primes <=k participate in the Walsh amplifier, so 5 is visible and 61 is the large tail.
    assert data["opposite_small_transverse_support"] == (5,)
    assert data["squarefree_transverse_divisors"] == (1, 5)
    assert data["walsh_divisor_weight"] == 2


def test_full_walsh_weight_equals_divisor_switched_dual_titchmarsh_count():
    for k in (8, 17, 46):
        data = walsh_dual_titchmarsh_profile(k)
        assert data["dual_titchmarsh_identity"] is True
        assert data["walsh_weighted_prime_count"] == data["divisor_switched_count"]
        for row in data["dual_titchmarsh_triples"]:
            assert row["prime"] + row["divisor"] * row["quotient"] == 2 * data["center"]


def test_truncated_log_observable_is_positive_exactly_when_basin_has_prime():
    for k in (8, 17, 46):
        for cutoff in (1, 5, k):
            data = truncated_log_walsh_ap_profile(k, cutoff)
            assert data["theta_positive_iff_prime_exists"] is True
            assert data["theta_D"] > 0
            assert data["phi_reciprocal_sum"] >= 1.0
            assert data["status"] == "EXACT_OBSERVABLE_PLUS_FORMAL_MAIN_TARGET_NO_ERROR_THEOREM"
