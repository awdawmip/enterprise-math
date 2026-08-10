from enterprise_math.p017_p018_centered_jacobsthal_slice import (
    centered_jacobsthal_slice,
    square_basin_candidate_progression,
)


def test_candidate_progression_has_exact_parity_dependent_shape():
    even = square_basin_candidate_progression(8)
    assert even["candidate_count"] == 8
    assert even["top_candidate"] == 79
    assert even["bottom_candidate"] == 65

    odd = square_basin_candidate_progression(9)
    assert odd["candidate_count"] == 8
    assert odd["top_candidate"] == 97
    assert odd["bottom_candidate"] == 83


def test_half_primorial_map_is_consecutive_and_preserves_roughness_exactly():
    for k in range(4, 30):
        data = centered_jacobsthal_slice(k)
        interval = data["half_primorial_interval_descending"]
        assert len(interval) == data["candidate_count"]
        assert data["interval_length"] == data["candidate_count"]
        assert all(interval[index] - interval[index + 1] == 1 for index in range(len(interval) - 1))
        assert data["roughness_bits"] == data["prime_bits"]
        assert data["centered_jacobsthal_equivalence"] is True


def test_centered_slice_prime_count_matches_known_small_square_intervals():
    expected = {
        4: 2,   # 17,19
        5: 2,   # 29,31
        6: 2,   # 37,43
        7: 3,   # 53,59,61
        8: 2,   # 67,71
        9: 3,   # 83,89,97
    }
    for k, count in expected.items():
        assert centered_jacobsthal_slice(k)["prime_count"] == count
