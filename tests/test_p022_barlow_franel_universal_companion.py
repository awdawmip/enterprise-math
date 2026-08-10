from enterprise_math.p022_barlow_franel_universal_companion import (
    companion_kind,
    first_large_terminal_offsets_are_excluded,
    nonforced_midpoint_center_ratio_holds,
    nonforced_midpoint_integer_companion,
    terminal_common_zero_companion_condition,
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


def test_large_terminal_offset_reduction_on_real_common_zero() -> None:
    # q=41 divides F_10; if one declares r=6 then the terminal offset is d=10.
    # q does not divide F_6, so this is deliberately not a primitive example;
    # it demonstrates the companion side of the affine reduction.
    assert nonforced_midpoint_integer_companion(10) % 41 == 0


def test_first_two_large_terminal_candidates_are_impossible() -> None:
    # Structural twin-center examples with prime candidates.
    assert first_large_terminal_offsets_are_excluded(6, 23)
    assert first_large_terminal_offsets_are_excluded(9, 37)
    assert first_large_terminal_offsets_are_excluded(15, 61)


def test_actual_common_zero_pair_maps_to_one_companion() -> None:
    # The non-twin example r=10,q=41 has q|F_10 and q|F_18?  It exercises
    # only when the actual common-zero prerequisite holds.
    # Keep a known real pair from the zero alphabet: r=7 gives terminal 12.
    assert terminal_common_zero_companion_condition(7, 41) == (8, 13, "K")
