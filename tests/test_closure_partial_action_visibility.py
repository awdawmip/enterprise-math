from enterprise_math.closure_partial_action_visibility import (
    is_predecessor_closed_visible_set,
    partial_visibility_report,
)


def test_predecessor_closed_action_subset_recovers_projected_progress():
    visible = frozenset({"h1", "h2", "h5"})
    assert is_predecessor_closed_visible_set(8, visible)
    report = partial_visibility_report(8, visible)
    assert report.predecessor_closed
    assert report.projected_exact_if_closed
    assert report.factorization_collision_left is None
    assert report.recovery_collision_left is None


def test_nonclosed_single_upper_action_depends_on_hidden_predecessors():
    visible = frozenset({"h5"})
    assert not is_predecessor_closed_visible_set(8, visible)
    report = partial_visibility_report(8, visible)
    assert not report.predecessor_closed
    assert report.factorization_collision_left is not None
    assert report.factorization_collision_right is not None
    assert report.same_projection == frozenset()
    assert report.left_visible_enabled != report.right_visible_enabled


def test_nonclosed_visible_enabledness_can_also_fail_to_recover_projection():
    report = partial_visibility_report(8, frozenset({"h5"}))
    assert report.recovery_collision_left is not None
    assert report.recovery_collision_right is not None
    assert report.same_visible_enabled == frozenset()
    left_projection = report.recovery_collision_left.intersection({"h5"})
    right_projection = report.recovery_collision_right.intersection({"h5"})
    assert left_projection != right_projection


def test_first_layer_visibility_is_automatically_predecessor_closed():
    visible = frozenset({"h1", "h3"})
    report = partial_visibility_report(8, visible)
    assert report.predecessor_closed
    assert report.projected_exact_if_closed
