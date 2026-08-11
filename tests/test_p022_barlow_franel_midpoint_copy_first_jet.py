from enterprise_math.p022_barlow_franel_midpoint_copy_first_jet import (
    forced_midpoint_copy_residue,
    forced_midpoint_copy_stays_simple,
)


def test_p149_midpoint_copy_unit_is_explicit_linear_multiplier() -> None:
    midpoint, unit, actual, predicted = forced_midpoint_copy_residue(149, 3)
    assert midpoint == 74
    assert unit == 93
    assert actual == predicted
    assert actual == (56 * 7 * 93) % 149  # F_3=56.
    assert forced_midpoint_copy_stays_simple(149, 3)


def test_all_small_pre_midpoint_unit_multipliers_stay_simple() -> None:
    for prime in (13, 23, 29, 53, 71, 101, 149):
        midpoint = (prime - 1) // 2
        for multiplier in range(1, min(midpoint, 8)):
            # Skip a multiplier only if its Franel value is itself a p-zero.
            try:
                assert forced_midpoint_copy_stays_simple(prime, multiplier)
            except ValueError as error:
                assert "p-unit" in str(error)


def test_self_midpoint_multiplier_is_the_unique_depth_raising_copy() -> None:
    for prime in (13, 23, 29, 53, 71, 101, 149):
        midpoint = (prime - 1) // 2
        _, _, actual, predicted = forced_midpoint_copy_residue(prime, midpoint)
        assert actual == predicted == 0
        assert not forced_midpoint_copy_stays_simple(prime, midpoint)
