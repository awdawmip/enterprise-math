from enterprise_math.p022_barlow_franel_two_digit_excess import (
    simple_high_zero_unit_low_residue,
    simple_low_zero_unit_high_residue,
    two_zero_digit_baseline,
    two_zero_digit_excess,
)


def test_simple_high_zero_copies_exact_depth_one_across_unit_low_digits() -> None:
    # Z_13={6}; 79=(6,1)_13 has the zero in the high digit.
    index, actual, predicted = simple_high_zero_unit_low_residue(6, 1, 13)
    assert index == 79
    assert actual == predicted != 0

    # The low digit may also be zero itself only in the separate two-zero branch;
    # use another unit low digit here to keep the orientation theorem explicit.
    index, actual, predicted = simple_high_zero_unit_low_residue(6, 5, 13)
    assert index == 83
    assert actual == predicted != 0


def test_simple_low_zero_has_one_exceptional_unit_high_multiplier() -> None:
    # p=29 has a simple zero at low digit 12.  Its first-jet exceptional high
    # multiplier is 17, which is a p-unit; the copied term 505 has depth >=2.
    index, quotient, exceptional = simple_low_zero_unit_high_residue(12, 17, 29)
    assert index == 505
    assert exceptional == 17
    assert quotient == 0

    # A different unit high digit stays at exact first-jet depth one.
    index, quotient, exceptional = simple_low_zero_unit_high_residue(12, 1, 29)
    assert index == 41
    assert exceptional == 17
    assert quotient != 0


def test_two_zero_digits_start_at_delaygue_depth_two() -> None:
    # 84=(6,6)_13 and 12=(2,2)_5 both saturate the two-zero baseline.
    assert two_zero_digit_baseline(6, 6, 13) == (84, 2)
    assert two_zero_digit_excess(6, 6, 13) == (2, 2, 0)
    assert two_zero_digit_baseline(2, 2, 5) == (12, 2)
    assert two_zero_digit_excess(2, 2, 5) == (2, 2, 0)
