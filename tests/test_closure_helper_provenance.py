from enterprise_math.closure_helper_provenance import (
    helper_provenance_report,
    local_cache_complete,
    local_provenance_holds,
)


def test_local_provenance_equals_global_prefix_validity_and_holds_on_reachable_states():
    for arity in range(4, 7):
        report = helper_provenance_report(arity)
        assert report.all_reachable_locally_sound
        assert report.local_global_validity_equivalent
        assert report.all_saturated_locally_complete


def test_transient_state_is_sound_but_not_locally_complete():
    report = helper_provenance_report(4)
    state = report.transient_reverse_failure_state
    assert local_provenance_holds(4, state)
    assert not local_cache_complete(4, state)
    assert report.transient_reverse_failure_helper == "e3"


def test_local_provenance_detects_stale_helper_directly():
    assert not local_provenance_holds(5, frozenset({"e3", "a3"}))
    assert local_provenance_holds(5, frozenset({"a1", "a2", "a3", "e2", "e3"}))
