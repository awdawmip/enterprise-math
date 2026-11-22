from enterprise_math.p017_p018_walsh_mobius_finite_difference import (
    four_prime_difference_witness,
    positive_inner_necessary_barrier,
    prime_scale_difference,
)


def test_prime_scale_difference_matches_direct_truncation_and_shell():
    cases = (
        ((3, 5, 7), 10),
        ((3, 5, 7, 11), 35),
        ((5, 7, 11, 13), 100),
    )
    for primes, budget in cases:
        data = prime_scale_difference(primes, budget)
        assert data["prime_scale_difference_identity"] is True
        assert data["direct_truncated_sum"] == data["finite_difference"]
        assert data["finite_difference"] == data["boundary_shell_sum"]


def test_positive_inner_requires_four_support_and_p2_p4_budget():
    for primes, budget in (
        ((3, 5, 7), 100),
        ((3, 5, 7, 11), 50),
        ((3, 5, 7, 11), 77),
    ):
        data = positive_inner_necessary_barrier(primes, budget)
        if data["positive_inner"]:
            assert data["support_size"] >= 4
            assert data["budget_B"] >= data["necessary_budget_p2_times_p4"]


def test_four_prime_threshold_witness_is_positive():
    data = four_prime_difference_witness()
    assert data["mixed_inner"] == 2
    assert data["sharp_support_threshold_witness"] is True
