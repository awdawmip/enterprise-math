from enterprise_math.p017_p018_terminal_shadow import (
    half_rough_shadow_saturation,
    odd_reciprocal_successor,
    terminal_candidate_shadow,
)


def test_reciprocal_successor_is_least_odd_above_the_hyperbola():
    for k in range(10, 61):
        for x in range(k // 2 + 1, 2 * k + 4):
            q = odd_reciprocal_successor(k, x)
            assert q % 2 == 1
            assert q * x > k * k
            if q >= 3:
                assert (q - 2) * x <= k * k


def test_terminal_shadow_edges_are_reciprocal_and_shell_edge_complete():
    for k in range(10, 81):
        data = terminal_candidate_shadow(k)
        assert data["near_involution_verified"] is True
        for p, q, value, offset in data["shadow_edges"]:
            assert value == p * q == k * k + offset
            assert odd_reciprocal_successor(k, q) == p
            assert 1 <= offset <= 2 * k


def test_prime_offsets_are_exact_half_rough_minus_terminal_shadow():
    for k in range(10, 81):
        data = half_rough_shadow_saturation(k)
        assert data["prime_offsets_equal_half_rough_minus_shadow"] is True
        assert data["counterexample_equivalence_verified"] is True
        half_rough = set(data["half_rough_offsets"])
        shadow = set(data["shadow_offsets"])
        assert set(data["prime_offsets"]) == half_rough - shadow
        assert set(data["semiprime_offsets"]) == half_rough & shadow


def test_positive_shadow_cardinality_margin_is_a_prime_certificate():
    for k in range(10, 101):
        data = half_rough_shadow_saturation(k)
        if data["shadow_cardinality_certificate_margin"] > 0:
            assert data["prime_count"] > 0
            assert data["counterexample_shadow_saturated"] is False
