from enterprise_math.p022_barlow_franel_universal_companion import (
    companion_kind,
    first_large_terminal_offsets_are_excluded,
    nonforced_midpoint_center_ratio_holds,
    nonforced_midpoint_integer_companion,
    terminal_companion_offsets,
    universal_companion_reconstructs_zero_digits,
    universal_zero_digits_from_companion,
)


def test_nonforced_companion_initial_values_and_recurrence() -> None:
    assert tuple(nonforced_midpoint_integer_companion(d) for d in range(7)) == (
        2,
        -1,
        45,
        -5733,
        1675449,
        -862396065,
        692480608677,
    )


def test_nonforced_center_ratio_and_zero_alphabet_examples() -> None:
    for prime in (11, 17, 41, 59, 73):
        assert nonforced_midpoint_center_ratio_holds(prime)
        assert universal_companion_reconstructs_zero_digits(prime)
    assert universal_zero_digits_from_companion(41) == (7, 10, 30, 33)
    assert universal_zero_digits_from_companion(59) == (17, 41)
    assert universal_zero_digits_from_companion(73) == (6, 66)


def test_forced_and_nonforced_companions_cover_both_residue_pairs() -> None:
    assert companion_kind(29) == "H"
    assert universal_zero_digits_from_companion(29) == (12, 14, 16)
    assert companion_kind(41) == "K"
    assert universal_zero_digits_from_companion(41) == (7, 10, 30, 33)


def test_large_terminal_offset_is_an_affine_companion_coordinate() -> None:
    # q=41 has midpoint 20.  For the formal terminal geometry at r=6,
    # t=2r-2=10 has d=10 while the declared source r has e=14.
    assert terminal_companion_offsets(6, 41) == (10, 14)
    assert 4 * 14 - 2 * 10 + 5 == 41
    assert nonforced_midpoint_integer_companion(10) % 41 == 0
    assert nonforced_midpoint_integer_companion(14) % 41 != 0


def test_first_two_large_terminal_candidates_are_impossible() -> None:
    assert first_large_terminal_offsets_are_excluded(6, 23)
    assert first_large_terminal_offsets_are_excluded(9, 37)
    assert first_large_terminal_offsets_are_excluded(15, 61)
