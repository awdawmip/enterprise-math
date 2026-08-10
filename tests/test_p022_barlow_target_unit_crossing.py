from enterprise_math.p022_barlow_target_unit_crossing import (
    TARGET_BOUNDARY_MAX_INDEX,
    TARGET_UNIT_CROSSING_PRIME,
    target_boundary_candidate_indices,
    target_boundary_zero_indices,
    target_unit_crossing_coefficient,
    target_unit_crossing_forces_lattice_one,
    target_unit_crossing_prime_is_in_family,
    target_unit_edge_multiplicities,
    target_unit_marker_is_positive_for_all_depths,
    target_unit_zero_is_simple,
)


def test_target_unit_crossing_certificate_is_exact() -> None:
    assert TARGET_UNIT_CROSSING_PRIME == 518_220_701
    assert target_unit_crossing_prime_is_in_family()
    assert target_unit_zero_is_simple()
    assert target_unit_edge_multiplicities() == (0, 1)
    assert target_unit_crossing_coefficient() == 1
    assert target_unit_crossing_forces_lattice_one()


def test_all_transfer_boundary_candidates_have_only_one_zero() -> None:
    candidates = target_boundary_candidate_indices()
    assert len(candidates) == 21
    assert max(candidates) == TARGET_BOUNDARY_MAX_INDEX == 2_591_104
    assert 50 in candidates
    assert target_boundary_zero_indices() == (50,)
    assert target_unit_marker_is_positive_for_all_depths()
