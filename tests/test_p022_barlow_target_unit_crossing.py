from enterprise_math.p022_barlow_target_unit_crossing import (
    TARGET_UNIT_CROSSING_PRIME,
    target_unit_crossing_coefficient,
    target_unit_crossing_forces_lattice_one,
    target_unit_crossing_prime_is_in_family,
    target_unit_edge_multiplicities,
    target_unit_zero_is_simple,
)


def test_target_unit_crossing_certificate_is_exact() -> None:
    assert TARGET_UNIT_CROSSING_PRIME == 518_220_701
    assert target_unit_crossing_prime_is_in_family()
    assert target_unit_zero_is_simple()
    assert target_unit_edge_multiplicities() == (0, 1)
    assert target_unit_crossing_coefficient() == 1
    assert target_unit_crossing_forces_lattice_one()
