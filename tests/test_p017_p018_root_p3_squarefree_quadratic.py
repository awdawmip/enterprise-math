from enterprise_math.p017_p018_root_p3_squarefree_quadratic import (
    squarefree_quadratic_indicator_numerator,
    squarefree_root_p3_profile,
)


def test_squarefree_quadratic_weight_is_exact_on_allowed_depths():
    assert squarefree_quadratic_indicator_numerator(0) == 3
    assert squarefree_quadratic_indicator_numerator(1) == 0
    assert squarefree_quadratic_indicator_numerator(3) == 0


def test_squarefree_fourth_root_profiles_have_no_depth_two_states():
    for k in (4, 5, 8, 17, 31, 64, 100, 257):
        data = squarefree_root_p3_profile(k)
        assert data["exact_quadratic_recovery"] is True
        assert data["quadratic_prime_numerator"] == 3 * data["prime_count"]
        assert sum(data["support_depth_counts"]) == data["squarefree_rough_count"]


def test_k1000_squarefree_repair_removes_exactly_the_three_depth_two_states():
    data = squarefree_root_p3_profile(1000)
    assert data["fourth_root_cutoff"] == 31
    assert len(data["removed_squareful_offsets"]) >= 3
    assert data["quadratic_prime_numerator"] == 3 * 152
    assert data["prime_count"] == 152
