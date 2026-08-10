from enterprise_math.closure_async_progress_poset import (
    asynchronous_progress_report,
    asynchronous_reachable_helper_sets,
    helper_ideals,
)


def test_async_reachable_progress_equals_helper_ideal_lattice():
    for arity in range(4, 9):
        report = asynchronous_progress_report(arity)
        assert report.reachable_equals_ideals
        assert report.reachable_async_count == report.ideal_count


def test_four_way_async_scheduler_expands_two_sync_states_to_four_ideals():
    report = asynchronous_progress_report(4)
    assert report.helper_count == 2
    assert report.helper_poset_width == 2
    assert report.synchronous_preoutput_state_count == 2
    assert report.ideal_count == 4


def test_eight_way_balanced_tree_has_twenty_five_preoutput_async_states():
    report = asynchronous_progress_report(8)
    assert report.helper_count == 6
    assert report.helper_poset_width == 4
    assert report.synchronous_preoutput_state_count == 3
    assert report.ideal_count == 25


def test_explicit_reachable_and_ideal_sets_match_for_five_way_tree():
    assert set(asynchronous_reachable_helper_sets(5)) == set(helper_ideals(5))
    assert len(helper_ideals(5)) == 5
