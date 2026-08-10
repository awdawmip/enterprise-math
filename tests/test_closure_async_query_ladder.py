from enterprise_math.closure_async_query_ladder import (
    asynchronous_query_ladder_report,
    enabled_helpers,
)


def test_endpoint_rank_and_exact_progress_class_counts():
    for arity in range(4, 9):
        report = asynchronous_query_ladder_report(arity)
        assert report.endpoint_class_count == 1
        assert report.remaining_work_class_count == report.helper_count + 1
        assert report.exact_progress_class_count >= report.remaining_work_class_count


def test_same_rank_can_have_different_enabled_action_sets():
    report = asynchronous_query_ladder_report(4)
    assert report.same_rank_action_collision_left is not None
    assert report.same_rank_action_collision_right is not None
    assert len(report.same_rank_action_collision_left) == len(report.same_rank_action_collision_right)
    assert report.left_enabled != report.right_enabled


def test_four_way_collision_is_two_singleton_ideals():
    report = asynchronous_query_ladder_report(4)
    left = report.same_rank_action_collision_left
    right = report.same_rank_action_collision_right
    assert left is not None and right is not None
    assert len(left) == len(right) == 1
    assert report.left_enabled is not None and report.right_enabled is not None
    assert report.left_enabled != report.right_enabled
    assert len(report.left_enabled) == len(report.right_enabled) == 1


def test_completed_cardinality_determines_remaining_helper_firings_only():
    # In the async helper-only phase each legal action completes exactly one
    # helper and no helper can fire twice, so remaining work is m-|I|.
    report = asynchronous_query_ladder_report(8)
    m = report.helper_count
    assert report.remaining_work_class_count == m + 1
    assert enabled_helpers(8, frozenset())
