from enterprise_math.p022_barlow_lucas_copy_capture import (
    forced_composite_copy_segment,
    forced_copy_is_q_divisible,
    forced_copy_multiplier,
    forced_copy_nonpositive_support_captures,
    forced_copy_q_divisible_support,
)


def test_multiplier_forces_a_composite_boundary_mod_three() -> None:
    assert forced_copy_multiplier(73) == 2
    assert forced_copy_multiplier(179) == 1
    assert forced_copy_multiplier(2593) == 2
    assert forced_composite_copy_segment(6, 73) == (2, 152)
    assert forced_composite_copy_segment(15, 179) == (1, 194)
    assert forced_composite_copy_segment(30, 2593) == (2, 5216)


def test_p_lucas_copy_is_digit_local() -> None:
    assert forced_copy_is_q_divisible(6, 73)
    assert forced_copy_is_q_divisible(15, 179)


def test_clean_copy_support_gives_unit_pivots() -> None:
    assert forced_copy_q_divisible_support(6, 73) == ()
    assert forced_copy_q_divisible_support(15, 179) == ()
    assert forced_copy_nonpositive_support_captures(6, 73) == 1
    assert forced_copy_nonpositive_support_captures(15, 179) == 1


def test_old_source_can_strengthen_instead_of_cancel_the_forced_copy() -> None:
    # This is the exceptional support pattern found at rank 30: the old source
    # occurs with exponent -1, so it adds to the repeated marker valuation.
    assert forced_copy_q_divisible_support(30, 2593) == ((30, -1),)
