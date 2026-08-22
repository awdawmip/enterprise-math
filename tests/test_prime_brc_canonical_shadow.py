from enterprise_math.prime_brc_canonical_shadow import (
    canonical_cofactor_shadow,
    canonical_shadow_depth_bound,
)


def test_k13_silent_semiprime_has_one_even_shadow_then_singleton():
    # M=182; 187=11*17 and its 17-shadow is 170=10*17.
    data = canonical_cofactor_shadow(13, 5, 1)
    assert data["p"] == 11
    assert data["q"] == 17
    assert data["shadow"] == 170
    assert data["shadow_least_factor"] == 2
    assert data["shadow_canonical_cofactor"] == 85
    assert data["shadow_canonical_hit_count"] == 1
    assert data["shadow_depth"] == 1


def test_singleton_canonical_cofactor_needs_no_shadow():
    # Choose the first such endpoint in a small dense search through the helper.
    found = False
    for r in range(1, 20):
        for side in (-1, 1):
            try:
                data = canonical_cofactor_shadow(20, r, side)
            except ValueError:
                continue
            if data["shadow_depth"] == 0:
                assert data["q_hit_count"] == 1
                assert data["q_chi"] in (-1, 1)
                found = True
                break
        if found:
            break
    assert found


def test_canonical_shadow_depth_is_at_most_one_dense():
    for k in range(10, 180):
        data = canonical_shadow_depth_bound(k)
        assert data["max_shadow_depth"] <= 1
