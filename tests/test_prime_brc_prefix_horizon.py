from enterprise_math.prime_brc_prefix_horizon import (
    adjacent_midpoint_divisor_defect_transition,
    lower_cumulative_divisor_state,
    lower_factor_prefix_horizon,
    midpoint_divisor_defect_transition,
    upper_cumulative_divisor_state,
    upper_factor_prefix_horizon,
)


def test_cumulative_divisor_offsets_lock_exactly_at_D_gt_r():
    # k=31, M=992, r=7, lower=985=5*197, upper=999=3^3*37.
    assert lower_cumulative_divisor_state(31, 7, 5)["midpoint_offset"] == -1
    assert lower_cumulative_divisor_state(31, 7, 197)["midpoint_offset"] == 0
    assert upper_cumulative_divisor_state(31, 7, 3)["midpoint_offset"] == 3
    assert upper_cumulative_divisor_state(31, 7, 9)["midpoint_offset"] == 1


def test_midpoint_divisor_action_is_ternary_monotone_up():
    # -1 -> 0 example under a midpoint divisor.
    first = midpoint_divisor_defect_transition(0, 2, 5, 2)
    assert first["input_defect"] == -1
    assert first["output_defect"] == 0
    # 0 -> +1 minimal example.
    second = midpoint_divisor_defect_transition(1, 2, 3, 2)
    assert second["input_defect"] == 0
    assert second["output_defect"] == 1
    # +1 is absorbing.
    third = midpoint_divisor_defect_transition(3, 5, 6, 5)
    assert third["output_defect"] == 1


def test_adjacent_midpoint_divisor_action_is_ternary_monotone_down():
    # +1 -> 0.
    first = adjacent_midpoint_divisor_defect_transition(0, 1, 1, 2)
    assert first["input_defect"] == 1
    assert first["output_defect"] == 0
    # 0 -> -1.
    second = adjacent_midpoint_divisor_defect_transition(0, 1, 2, 2)
    assert second["input_defect"] == 0
    assert second["output_defect"] == -1
    # -1 is absorbing.
    third = adjacent_midpoint_divisor_defect_transition(2, 4, 7, 5)
    assert third["output_defect"] == -1


def test_lower_factor_prefix_horizon_recoalesces_suffix():
    # k=31,r=7, 985=5*197. First factor does not lock; cumulative 985 does.
    data = lower_factor_prefix_horizon(31, 7, (5, 197))
    assert data["lock_index"] == 2
    assert tuple(item["midpoint_offset"] for item in data["records"]) == (-1, 0)
    assert tuple(item["defect"] for item in data["records"]) == (0, 1)


def test_lower_immediate_lock_then_monotone_suffix():
    # 1331=11^3 around k=36,M=1332,r=1.
    data = lower_factor_prefix_horizon(36, 1, (11, 11, 11))
    assert data["lock_index"] == 1
    assert tuple(item["midpoint_offset"] for item in data["records"]) == (0, 0, 0)
    assert tuple(item["defect"] for item in data["records"]) == (1, 1, 1)


def test_upper_factor_prefix_horizon_recoalesces_to_adjacent_center():
    # k=31,r=7, 999=3^3*37. Cumulative 9 first exceeds r.
    data = upper_factor_prefix_horizon(31, 7, (3, 3, 3, 37))
    assert data["lock_index"] == 2
    assert tuple(item["midpoint_offset"] for item in data["records"]) == (3, 1, 1, 1)
    # Once locked, the defect cannot increase and ends at -1.
    locked_defects = tuple(item["defect"] for item in data["records"][1:])
    assert all(b <= a for a, b in zip(locked_defects, locked_defects[1:]))
    assert locked_defects[-1] == -1
