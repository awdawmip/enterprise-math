from enterprise_math.p022_barlow_twin_divisor_reentry import (
    available_divisor_gates,
    formal_divisor_barrier_ladder,
    left_divisor_forbidden_interval,
    left_divisor_high_support,
    left_divisor_reentry_segment,
    right_divisor_forbidden_interval,
    right_divisor_high_support,
    right_divisor_reentry_segment,
)


def test_right_divisor_support_on_distinct_divisors() -> None:
    assert right_divisor_reentry_segment(30, 2) == 92
    assert right_divisor_high_support(30, 2) == (
        (30, -1),
        (31, 1),
        (91, 1),
    )
    assert right_divisor_reentry_segment(30, 3) == 153
    assert right_divisor_high_support(30, 3) == (
        (30, -1),
        (31, 1),
        (152, 1),
    )
    assert right_divisor_reentry_segment(30, 5) == 275
    assert right_divisor_high_support(30, 5) == (
        (30, -1),
        (31, 1),
        (274, 1),
    )


def test_left_divisor_support_on_distinct_divisors() -> None:
    assert left_divisor_reentry_segment(21, 2) == 62
    assert left_divisor_high_support(21, 2) == ((21, 1), (61, 1))
    assert left_divisor_reentry_segment(21, 4) == 144
    assert left_divisor_high_support(21, 4) == ((21, 1), (143, 1))
    assert left_divisor_reentry_segment(21, 5) == 185
    assert left_divisor_high_support(21, 5) == ((21, 1), (184, 1))


def test_divisor_gate_intervals_specialize_to_four_and_six_rank_scales() -> None:
    assert right_divisor_forbidden_interval(30, 2) == (61, 122)
    assert right_divisor_forbidden_interval(30, 3) == (122, 183)
    assert left_divisor_forbidden_interval(21, 2) == (41, 84)
    assert right_divisor_forbidden_interval(21, 3) == (86, 129)


def test_available_gates_record_both_source_sides() -> None:
    gates = available_divisor_gates(36, 6)
    assert (2, "right", (73, 146)) in gates
    assert (3, "right", (146, 219)) in gates
    assert (4, "right", (219, 292)) in gates
    assert (5, "left", (284, 357)) in gates
    assert (6, "right", (365, 438)) in gates


def test_formal_ladder_can_continue_when_divisor_intervals_overlap() -> None:
    # q>3r-1 is the post-boundary starting point.  For r=36 the d=2,3,4
    # right gates and then the d=5 left gate overlap consecutively.
    assert formal_divisor_barrier_ladder(36, 3 * 36 - 1, 6) == (
        (2, "right", 107, 146),
        (3, "right", 146, 219),
        (4, "right", 219, 292),
        (5, "left", 292, 357),
    )


def test_missing_small_divisor_stops_the_pure_interval_ladder() -> None:
    # r=30 has d=2 and d=3 on the right, but no d=4 gate.  Larger divisor
    # intervals start too far away to be reached without additional arithmetic.
    assert formal_divisor_barrier_ladder(30, 3 * 30 - 1, 10) == (
        (2, "right", 89, 122),
        (3, "right", 122, 183),
    )
