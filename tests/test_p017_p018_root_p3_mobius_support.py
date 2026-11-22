from enterprise_math.p017_p018_root_p3_mobius_support import (
    affine_mobius_support_weight,
    mobius_value,
    root_p3_mobius_support_profile,
    rough_prime_cube_offsets,
)


def test_mobius_reference_values_cover_squarefree_and_squareful_types():
    assert mobius_value(2) == -1
    assert mobius_value(2 * 3) == 1
    assert mobius_value(2 * 3 * 5) == -1
    assert mobius_value(3 * 3 * 5) == 0
    assert mobius_value(7**3) == 0


def test_affine_weight_annihilates_all_composite_types_except_cubes():
    # k=100 examples are all fourth-root rough because z_3(100)=10.
    assert affine_mobius_support_weight(100, 10009) == 3  # prime
    assert affine_mobius_support_weight(100, 10043) == 0  # 11^2 * 83
    assert affine_mobius_support_weight(100, 10051) == 0  # 19 * 23^2


def test_affine_profiles_recover_prime_count_exactly():
    for k in (4, 5, 8, 17, 31, 64, 100, 257):
        data = root_p3_mobius_support_profile(k)
        assert data["exact_affine_recovery"] is True
        assert data["affine_identity_rhs"] == 3 * data["prime_count"]
        assert data["rough_prime_cube_count"] <= 1


def test_k1000_affine_checkpoint_matches_support_profile():
    data = root_p3_mobius_support_profile(1000)
    assert data["fourth_root_cutoff"] == 31
    assert data["rough_count"] == 309
    assert data["support_moment_1"] == 184
    assert data["prime_count"] == 152
    assert data["affine_identity_rhs"] == 456


def test_rough_prime_cube_layer_is_globally_at_most_one():
    for k in range(4, 150):
        assert len(rough_prime_cube_offsets(k)) <= 1
