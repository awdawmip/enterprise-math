from enterprise_math.p022_barlow_twin_seven_rank_barrier import (
    complete_escape_or_seven_rank_barrier,
    fivefold_reflected_zero_index,
)


def test_fivefold_reflection_index_is_q_minus_5r_plus_3_segment() -> None:
    assert fivefold_reflected_zero_index(9, 79) == 31
    assert fivefold_reflected_zero_index(15, 127) == 49
    assert fivefold_reflected_zero_index(21, 173) == 65


def test_known_primitive_twin_rows_are_captured_before_seven_rank_branch() -> None:
    expected = {
        (9, 937): ("capture", 17, 1),
        (15, 179): ("capture", 29, 1),
        (21, 3019): ("capture", 41, 1),
        (30, 2593): ("capture", 59, 1),
    }
    for key, value in expected.items():
        assert complete_escape_or_seven_rank_barrier(*key) == value
