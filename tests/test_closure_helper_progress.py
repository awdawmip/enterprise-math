from enterprise_math.closure_helper_progress import helper_progress_report


def test_one_raw_projection_fiber_contains_k_minus_one_progress_states():
    for arity in range(3, 8):
        report = helper_progress_report(arity)
        assert report.raw_projection_constant
        assert report.progress_state_count == arity - 1
        assert report.distinct_remaining_rounds
        assert tuple(state.remaining_rounds for state in report.progress_states) == tuple(
            range(arity - 2, -1, -1)
        )


def test_five_way_progress_fixture():
    report = helper_progress_report(5)
    assert report.raw_seed == frozenset({"a1", "a2", "a3", "a4"})
    assert report.progress_state_count == 4
    assert {state.raw_projection for state in report.progress_states} == {report.raw_seed}
    assert tuple(state.remaining_rounds for state in report.progress_states) == (3, 2, 1, 0)
