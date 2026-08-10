from enterprise_math.closure_async_progress_poset import asynchronous_progress_report
from enterprise_math.perfect_binary_progress_counts import (
    perfect_binary_progress_count,
    perfect_gate_ideal_count,
)


def test_gate_subtree_recurrence_values():
    assert [perfect_gate_ideal_count(h) for h in range(1, 5)] == [2, 5, 26, 677]


def test_perfect_compiler_exact_async_counts():
    expected = {
        2: (4, 4),
        3: (8, 25),
        4: (16, 676),
        5: (32, 458329),
    }
    for depth, (arity, async_count) in expected.items():
        report = perfect_binary_progress_count(depth)
        assert report.arity == arity
        assert report.asynchronous_preoutput_state_count == async_count
        assert report.synchronous_preoutput_state_count == depth
        assert report.helper_poset_width == arity // 2
        assert report.helper_count == arity - 2


def test_closed_form_recurrence_matches_explicit_small_compiler_enumeration():
    for depth in (2, 3):
        arity = 1 << depth
        explicit = asynchronous_progress_report(arity)
        formula = perfect_binary_progress_count(depth)
        assert explicit.ideal_count == formula.asynchronous_preoutput_state_count
        assert explicit.helper_poset_width == formula.helper_poset_width
        assert explicit.synchronous_preoutput_state_count == formula.synchronous_preoutput_state_count
