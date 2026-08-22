from enterprise_math.prime_brc_shadow_staircase import (
    cross_denominator_edge,
    double_hit_large_moduli,
    guaranteed_near_k_shadow_prefix,
    shadow_staircase,
)


def test_minimal_k8_shadow_edge_recovers_65_78_pair():
    data = cross_denominator_edge(8, 5)
    assert data["edge"] == 1
    assert data["q"] == 13
    assert data["lower_state"] == 65
    assert data["upper_state"] == 78
    assert data["s"] > data["h"]


def test_shadow_edges_are_strictly_monotone_and_match_large_double_hits():
    for k in range(5, 250):
        data = shadow_staircase(k)
        qs = data["q_labels"]
        assert all(a > b for a, b in zip(qs, qs[1:]))
        assert tuple(sorted(double_hit_large_moduli(k), reverse=True)) == qs


def test_residue_quotient_edge_criterion_dense():
    for k in range(5, 180):
        for p in range(k // 2 + 1, k):
            data = cross_denominator_edge(k, p)
            assert data["edge"] == int(data["s"] > data["h"])
            if data["edge"]:
                assert k < data["q"] <= 2 * k - 1
                assert data["lower_state"] < k * (k + 1) < data["upper_state"]


def test_near_k_subroot_prefix_always_exists_as_claimed():
    for k in range(5, 400):
        data = guaranteed_near_k_shadow_prefix(k)
        for t, p in zip(data["t_values"], data["p_values"]):
            assert t * t < p
            assert cross_denominator_edge(k, p)["edge"] == 1
