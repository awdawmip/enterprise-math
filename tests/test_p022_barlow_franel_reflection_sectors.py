from enterprise_math.p022_barlow_franel_integer_companion import midpoint_integer_companion
from enterprise_math.p022_barlow_franel_reflection_sectors import (
    diagonal_companion_mutual_exclusion,
    franel_reflection_sectors_hold,
    midpoint_even_companion,
    midpoint_sector_casoratian,
    second_solution_midpoint_zero_criterion,
    third_index_franel_zero_via_companion,
)


def test_franel_and_second_solution_are_opposite_reflection_sectors() -> None:
    for prime in (5, 7, 11, 13, 17, 23, 29):
        for index in range(prime):
            assert franel_reflection_sectors_hold(index, prime)


def test_second_solution_has_the_complementary_midpoint_zero() -> None:
    assert second_solution_midpoint_zero_criterion(11)
    assert second_solution_midpoint_zero_criterion(17)
    assert not second_solution_midpoint_zero_criterion(5)
    assert not second_solution_midpoint_zero_criterion(7)
    assert not second_solution_midpoint_zero_criterion(13)
    assert not second_solution_midpoint_zero_criterion(23)


def test_even_midpoint_companion_and_sector_casoratian() -> None:
    assert tuple(midpoint_even_companion(d) for d in range(5)) == (
        2,
        -1,
        45,
        -5733,
        1675449,
    )
    for offset in range(10):
        value = midpoint_sector_casoratian(offset)
        assert value != 0


def test_special_third_index_uses_the_correct_universal_sector() -> None:
    # p=149 is a genuine F_50 zero in the forced-midpoint sector A.
    assert third_index_franel_zero_via_companion(149) == (50, 24, "A", True)
    assert midpoint_integer_companion(24) % 149 == 0
    assert midpoint_even_companion(24) % 149 != 0

    # p=743 is a useful opposite-sector control: E_123 vanishes, but p=7 mod8
    # means F uses sector A here and F_248 is nonzero.
    assert third_index_franel_zero_via_companion(743) == (248, 123, "A", False)
    assert midpoint_integer_companion(123) % 743 != 0
    assert midpoint_even_companion(123) % 743 == 0

    # First surviving dangerous-boundary examples use E and are nonzero.
    assert third_index_franel_zero_via_companion(17) == (6, 2, "E", False)
    assert third_index_franel_zero_via_companion(107) == (36, 17, "E", False)
    assert third_index_franel_zero_via_companion(467) == (156, 77, "E", False)
    assert third_index_franel_zero_via_companion(521) == (174, 86, "E", False)


def test_diagonal_sectors_cannot_vanish_together() -> None:
    for prime in (5, 17, 107, 149, 467, 521, 743):
        assert diagonal_companion_mutual_exclusion(prime)
