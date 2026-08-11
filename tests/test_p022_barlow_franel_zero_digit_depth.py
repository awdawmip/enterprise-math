from enterprise_math.p022_barlow_franel_zero_digit_depth import (
    excess_decomposition,
    franel_delaygue_lower_bound_holds,
    franel_valuation_excess,
    franel_zero_digit_count,
    two_digit_zero_pattern,
)


def test_single_and_double_zero_digit_baselines_at_p13() -> None:
    # Z_13={6}.  The three indices exercise low-zero, high-zero and two-zero
    # base-13 patterns without relying on the Lucas product alone.
    assert two_digit_zero_pattern(19, 13) == (1, 6, False, True)
    assert two_digit_zero_pattern(79, 13) == (6, 1, True, False)
    assert two_digit_zero_pattern(84, 13) == (6, 6, True, True)
    assert franel_zero_digit_count(19, 13) == 1
    assert franel_zero_digit_count(79, 13) == 1
    assert franel_zero_digit_count(84, 13) == 2


def test_delaygue_bound_is_sharp_on_basic_two_digit_patterns() -> None:
    assert excess_decomposition(19, 13) == (1, 1, 0)
    assert excess_decomposition(79, 13) == (1, 1, 0)
    assert excess_decomposition(84, 13) == (2, 2, 0)
    for index in (6, 19, 79, 84):
        assert franel_delaygue_lower_bound_holds(index, 13)
        assert franel_valuation_excess(index, 13) == 0


def test_p5_two_zero_digit_baseline_is_already_depth_two() -> None:
    # Z_5={2}; 12=(22)_5 has two zero digits.
    assert two_digit_zero_pattern(12, 5) == (2, 2, True, True)
    assert excess_decomposition(12, 5) == (2, 2, 0)
