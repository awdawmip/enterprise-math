from enterprise_math.p017_p018_walsh_even_l2_kernel import (
    even_conductor_l2_energy,
    even_pair_kernel,
    pair_collision_partition,
)


def test_midpoint_difference_coordinates_reconstruct_collision_orientations():
    data = pair_collision_partition(46, 1, 11, 23)
    assert data["midpoint_x"] == 6
    assert data["difference_y"] == -5
    assert data["collision_sets_disjoint"] is True
    assert data["self_similar_midpoint_difference_geometry"] is True


def test_hyperbolic_pair_kernel_matches_direct_even_conductor_sum():
    for r, s in ((1, 1), (1, 11), (5, 17), (19, 23)):
        data = even_pair_kernel(46, r, s, prime_cutoff=23, conductor_cutoff=22)
        assert data["kernel_identity"] is True
        assert (
            data["direct_even_nontrivial_pair_kernel"]
            == data["hyperbolic_even_nontrivial_pair_kernel"]
        )


def test_l2_energy_collapses_exactly_to_radius_pair_kernel():
    for k, prime_cutoff in ((46, 23), (82, 41)):
        data = even_conductor_l2_energy(
            k,
            prime_cutoff=prime_cutoff,
            conductor_cutoff=(k - 1) // 2,
        )
        assert data["l2_pair_collapse"] is True
        assert data["direct_column_l2_energy"] == data["radius_pair_kernel_energy"]
        assert data["direct_column_l2_energy"] >= 0
