from enterprise_math.closure_async_bounded_progress import (
    bounded_progress_deadline,
    bounded_progress_deadline_class_count,
)
from enterprise_math.closure_async_progress_poset import helper_ideals


def test_exact_deadline_is_window_times_remaining_rank():
    for arity in range(4, 9):
        for ideal in helper_ideals(arity):
            for window in (1, 2, 5):
                report = bounded_progress_deadline(arity, ideal, window)
                assert report.worst_case_steps == window * report.remaining_helpers
                assert report.sharp


def test_deadline_future_has_same_class_count_as_remaining_work_rank():
    for arity in range(4, 9):
        helper_count = bounded_progress_deadline(arity, frozenset(), 3).remaining_helpers
        assert bounded_progress_deadline_class_count(arity, 3) == helper_count + 1


def test_four_way_empty_progress_deadlines_scale_with_contract():
    assert bounded_progress_deadline(4, frozenset(), 1).worst_case_steps == 2
    assert bounded_progress_deadline(4, frozenset(), 4).worst_case_steps == 8
