from enterprise_math.perfect_binary_schedule_counts import (
    perfect_binary_schedule_count,
    perfect_tree_gate_count,
    perfect_tree_linear_extensions,
)


def test_perfect_tree_gate_counts():
    assert [perfect_tree_gate_count(h) for h in range(1, 5)] == [1, 3, 7, 15]


def test_linear_extension_recurrence_values():
    assert perfect_tree_linear_extensions(1) == 1
    assert perfect_tree_linear_extensions(2) == 2
    assert perfect_tree_linear_extensions(3) == 80
    assert perfect_tree_linear_extensions(4) == 21_964_800


def test_complete_schedule_count_explodes_beyond_state_count():
    expected = {
        2: (4, 2, 4),
        3: (8, 80, 25),
        4: (16, 21_964_800, 676),
    }
    for depth, (arity, schedules, states) in expected.items():
        report = perfect_binary_schedule_count(depth)
        assert report.arity == arity
        assert report.completing_schedule_count == schedules
        assert report.async_progress_state_count == states
        assert report.endpoint_class_count == 1
        assert report.completing_schedule_count >= report.endpoint_class_count
