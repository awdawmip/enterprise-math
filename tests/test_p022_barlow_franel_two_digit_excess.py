from enterprise_math.p022_barlow_franel_two_digit_excess import (
    simple_high_zero_transport_residual,
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


def test_simple_high_zero_residual_is_negative_for_unit_low_digit() -> None:
    # N=79=(6,1)_13 and N-1=78=(6,0)_13 both have exact depth one.
    branch, residual, excess = simple_high_zero_transport_residual(6, 1, 13)
    assert branch == "unit-low"
    assert residual == -1
    assert excess == -1

    branch, residual, excess = simple_high_zero_transport_residual(6, 5, 13)
    assert branch == "unit-low"
    assert residual <= -1
    assert excess == -1


def test_zero_low_digit_turns_residual_into_delaygue_excess() -> None:
    # N=84=(6,6)_13 has depth two while 83=(6,5)_13 has depth one.
    # Therefore R=2-1-1=0, exactly the zero excess of the two-zero term.
    branch, residual, excess = simple_high_zero_transport_residual(6, 6, 13)
    assert branch == "two-zero"
    assert residual == excess == 0

    # The same minimal saturation occurs for 12=(2,2)_5 over predecessor 11=(2,1)_5.
    branch, residual, excess = simple_high_zero_transport_residual(2, 2, 5)
    assert branch == "two-zero"
    assert residual == excess == 0
