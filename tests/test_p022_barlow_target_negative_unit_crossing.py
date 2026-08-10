from enterprise_math.p022_barlow_target_negative_unit_crossing import (
    TARGET_NEGATIVE_UNIT_PRIME,
    certify_p_minus_one_large_prime,
    certify_r0_prime,
    certify_r1_prime,
    certify_target_negative_unit_prime,
    target_negative_unit_crossing_coefficient,
    target_negative_unit_edge_multiplicities,
    target_negative_unit_forces_lattice_one,
    target_negative_unit_zero_is_simple,
)


def test_pocklington_chain_certifies_large_target_prime() -> None:
    assert TARGET_NEGATIVE_UNIT_PRIME == 8_895_267_426_781_770_496_852_703
    assert certify_p_minus_one_large_prime()
    assert certify_target_negative_unit_prime()


def test_q97_ancestry_chain_is_exact() -> None:
    assert certify_r0_prime()
    assert certify_r1_prime()
    assert target_negative_unit_edge_multiplicities() == (0, 1)


def test_target_family_really_has_negative_unit_crossing() -> None:
    assert target_negative_unit_zero_is_simple()
    assert target_negative_unit_crossing_coefficient() == -1
    assert target_negative_unit_forces_lattice_one()
