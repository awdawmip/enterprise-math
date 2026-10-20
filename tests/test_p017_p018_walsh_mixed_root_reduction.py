from enterprise_math.p017_p018_walsh_mixed_root_reduction import (
    even_conductor_orientation_splits,
    mixed_denominator_horizon,
)


def test_even_conductor_pure_roots_are_positive_and_mixed_denominator_is_small():
    data = even_conductor_orientation_splits(1000, (3, 5, 7, 11))
    assert len(data["pure_splits"]) == 2
    assert all(row["coefficient"] == 1 for row in data["pure_splits"])
    assert data["pure_root_contribution_nonnegative"] is True
    assert data["harmful_boundary_reduces_to_mixed_roots"] is True
    assert all(
        row["small_factor_at_most_sqrt_floor_cutoff"] is True
        for row in data["mixed_unordered_factor_pairs"]
    )


def test_two_prime_conductor_has_one_unordered_mixed_pair():
    data = even_conductor_orientation_splits(100, (3, 5))
    assert len(data["mixed_ordered_splits"]) == 2
    assert len(data["mixed_unordered_factor_pairs"]) == 1
    row = data["mixed_unordered_factor_pairs"][0]
    assert row["small_factor"] == 3
    assert row["large_factor"] == 5


def test_universal_mixed_denominator_horizon_is_sqrt_half_cutoff():
    data = mixed_denominator_horizon(8191)
    assert data["reusable_floor_cutoff"] == 4095
    assert data["mixed_small_denominator_ceiling"] == 63
    assert data["one_mixed_denominator_is_square_root_scale"] is True
