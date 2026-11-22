from fractions import Fraction

from enterprise_math.p017_p018_walsh_soft_endpoint import (
    balanced_soft_local_moments,
    endpoint_jet_order,
    prime_free_soft_pair_ceiling,
    soft_walsh_profile,
)


def test_unique_mean_one_soft_local_factor_has_exact_second_moment():
    epsilon = Fraction(1, 32)
    data = balanced_soft_local_moments(5, epsilon)
    assert data["lower_hit_value"] == 2 - epsilon
    assert data["upper_hit_value"] == epsilon
    assert data["mean"] == 1
    assert data["second_moment"] == 1 + Fraction(2, 5) * (1 - epsilon) ** 2


def test_endpoint_jet_order_is_minimum_two_sided_support_depth():
    prime_side = endpoint_jet_order(0, 3)
    one_deep = endpoint_jet_order(1, 4)
    balanced = endpoint_jet_order(2, 2)
    assert prime_side["vanishing_order_at_t_one"] == 0
    assert prime_side["leading_u_coefficient"] == 8
    assert one_deep["vanishing_order_at_t_one"] == 1
    assert one_deep["leading_u_coefficient"] == 16
    assert balanced["vanishing_order_at_t_one"] == 2
    assert balanced["leading_u_coefficient"] == 8


def test_canonical_softness_puts_every_prime_free_pair_below_one_for_depth_at_least_three():
    for J in range(3, 10):
        epsilon = Fraction(1, 2 ** (J - 1))
        ceiling = prime_free_soft_pair_ceiling(J, epsilon)
        assert ceiling < 1


def test_soft_physical_mean_certificate_works_on_tight_and_anchor_critical_examples():
    # k=37 is a deliberately tight finite pressure point for the canonical
    # epsilon=2^(1-J) choice; k=46 has an effective odd anchor.
    for k in (37, 46, 82):
        data = soft_walsh_profile(k)
        assert data["prime_free_pair_weight_ceiling"] < 1
        assert data["soft_physical_average"] > data["prime_free_pair_weight_ceiling"]
        assert data["soft_prime_certificate"] is True
        assert data["prime_mirror_side_exists"] is True
        assert data["complete_period_pair_mean"] == 2
