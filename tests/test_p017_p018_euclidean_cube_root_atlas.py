from math import gcd

from enterprise_math.p017_p018_euclidean_cube_root_atlas import (
    cube_root_atlas_partition,
    integer_cube_root_ceiling,
    long_strip_modulus_split,
)


def test_integer_cube_root_ceiling_is_exact():
    for k in range(1, 300):
        A = integer_cube_root_ceiling(k)
        assert A**3 >= k
        if A > 1:
            assert (A - 1) ** 3 < k


def test_cube_root_partition_forces_all_high_quotient_cells_to_singletons():
    for k in (46, 82, 862, 8191):
        data = cube_root_atlas_partition(k)
        A = data["cube_root_cutoff_A"]
        assert data["all_high_quotient_cells_singleton"] is True
        assert data["all_long_strips_have_small_quotient"] is True
        assert data["singleton_region_state_count"] <= k // A
        assert data["long_strip_count"] <= A - 1
        for a, values in data["long_strips"]:
            assert a < A
            assert all(k // n == a for n in values)


def test_long_strip_modulus_split_reconstructs_both_crt_components():
    examples = [
        (862, 200, 3 * 5 * 7),
        (862, 300, 5 * 7 * 11),
        (8191, 2000, 3 * 5 * 7),
        (8191, 3000, 5 * 7 * 11),
    ]
    for k, n, d in examples:
        if gcd(n, d) != 1:
            continue
        data = long_strip_modulus_split(k, n, d)
        assert data["long_strip_modulus_split_exact"] is True
        assert data["singular_modulus_below_cube_root"] is True
        assert data["full_channel_residue"] % data["singular_modulus_g"] == data["singular_channel_residue"]
        assert data["full_channel_residue"] % data["coprime_modulus_e"] == data["coprime_channel_residue"]
