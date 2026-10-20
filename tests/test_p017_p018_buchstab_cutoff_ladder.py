from enterprise_math.p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    integer_nth_root_floor,
    prime_or_semiprime_cutoff_decomposition,
    square_interval_upper,
)


def test_integer_nth_root_floor_exactly_brackets_input():
    for n in range(0, 200):
        for degree in (2, 3, 4, 5):
            root = integer_nth_root_floor(n, degree)
            assert root**degree <= n < (root + 1) ** degree


def test_root_cutoff_ladder_hits_prime_p2_p3_scales():
    for k in range(3, 61):
        upper = square_interval_upper(k)
        prime_cutoff = almost_prime_cutoff(k, 1)
        p2_cutoff = almost_prime_cutoff(k, 2)
        p3_cutoff = almost_prime_cutoff(k, 3)
        assert prime_cutoff["cutoff"] == k
        assert (p2_cutoff["cutoff"] + 1) ** 3 > upper
        assert (p3_cutoff["cutoff"] + 1) ** 4 > upper
        assert p3_cutoff["cutoff"] <= p2_cutoff["cutoff"] <= k


def test_cubic_root_cutoff_survivors_are_exactly_primes_or_semiprimes():
    for k in range(3, 51):
        data = prime_or_semiprime_cutoff_decomposition(k)
        assert data["prime_gap_equals_rough_minus_semiprime"] is True
        assert data["rough_count"] == data["prime_count"] + data["semiprime_count"]
        for p, q, value, offset in data["semiprime_edges"]:
            assert data["cubic_root_cutoff"] < p <= k < q
            assert value == p * q == k * k + offset
