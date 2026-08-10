from enterprise_math.closure_auxiliary_simulation import auxiliary_simulation_report


def test_raw_embedding_is_semantics_preserving_but_arbitrary_helpers_are_not():
    for arity in range(3, 7):
        report = auxiliary_simulation_report(arity)
        assert report.raw_embedding_verified
        assert report.arbitrary_internal_state_counterexample is not None
        assert report.counterexample_compiled_projection != report.counterexample_expected_raw_closure
        assert "z" in report.counterexample_compiled_projection
        assert "z" not in report.counterexample_expected_raw_closure


def test_four_way_counterexample_is_concrete():
    report = auxiliary_simulation_report(4)
    assert report.arbitrary_internal_state_counterexample == frozenset({"e3", "a4"})
    assert report.counterexample_raw_projection == frozenset({"a4"})
    assert report.counterexample_compiled_projection == frozenset({"a4", "z"})
    assert report.counterexample_expected_raw_closure == frozenset({"a4"})
