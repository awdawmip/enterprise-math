from enterprise_math.p017_p018_walsh_critical_truncation import (
    critical_walsh_prime_weight,
    critical_walsh_profile,
)


def test_pointwise_critical_truncation_keeps_at_least_half_full_weight():
    for k in (17, 46, 82):
        profile = critical_walsh_profile(k)
        for row in profile["prime_rows"]:
            assert row["pointwise_half_retention"] is True
            assert 1 in row["critical_squarefree_transverse_divisors"]
            assert all(d <= k for d in row["critical_squarefree_transverse_divisors"])
            assert 2 * row["critical_walsh_divisor_weight"] >= row["full_walsh_divisor_weight"]


def test_known_half_retention_boundary_is_attained():
    profile = critical_walsh_profile(46)
    assert any(abs(row["critical_to_full_ratio"] - 0.5) < 1e-15 for row in profile["prime_rows"])
    assert profile["half_retention_global"] is True


def test_critical_divisor_switch_preserves_positivity_and_triples():
    for k in (17, 46, 82):
        data = critical_walsh_profile(k)
        assert data["positivity_equivalent_to_prime_existence"] is True
        assert data["critical_walsh_weighted_prime_count"] > 0
        assert data["critical_walsh_weighted_prime_count"] <= data["full_walsh_weighted_prime_count"]
        assert 2 * data["critical_walsh_weighted_prime_count"] >= data["full_walsh_weighted_prime_count"]
        for row in data["critical_dual_titchmarsh_triples"]:
            assert row["divisor"] <= k
            assert row["prime"] + row["divisor"] * row["quotient"] == 2 * data["center"]


def test_k17_prime_with_large_tail_keeps_unit_and_small_divisor_only():
    row = critical_walsh_prime_weight(17, 307)
    assert row["opposite_state"] == 305
    assert row["full_walsh_divisor_weight"] == 2
    assert row["critical_squarefree_transverse_divisors"] == (1, 5)
    assert row["critical_walsh_divisor_weight"] == 2
