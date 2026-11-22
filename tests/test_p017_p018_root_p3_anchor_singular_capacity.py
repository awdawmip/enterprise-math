from enterprise_math.p017_p018_root_p3_anchor_singular_capacity import (
    large_anchor_primes_at_p3_root,
    root_p3_anchor_singular_capacity,
)


def test_at_most_two_large_anchor_prime_columns() -> None:
    for k in (4, 8, 15, 17, 31, 100, 203, 500, 1000, 8191):
        data = large_anchor_primes_at_p3_root(k)
        assert len(data["large_anchor_primes_dividing_k"]) <= 1
        assert len(data["large_anchor_primes_dividing_k_plus_1"]) <= 1
        assert data["large_anchor_prime_count"] <= 2
        assert all(p > data["p3_cutoff"] for p in data["large_anchor_primes"])


def test_anchor_singular_root_rough_rows_fit_signed_capacity() -> None:
    for k in (8, 15, 17, 31, 100, 203, 500, 1000):
        data = root_p3_anchor_singular_capacity(k)
        assert data["direct_anchor_singular_rough_count"] <= data["exact_capacity_bound"]
        assert data["exact_capacity_bound"] <= data["uniform_two_column_bound"]
        assert data["status"] == "ROOT_P3_ANCHOR_SINGULAR_CAPACITY"

        for p, bound in data["signed_column_bounds"]:
            assert bound == (k - 1) // p + 1
