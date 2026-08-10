from enterprise_math.closure_partial_action_subsystem import (
    partial_subsystem_report,
)


def test_predecessor_closed_visible_actions_form_exact_projected_partial_subsystem():
    visible = frozenset({"h1", "h2", "h5"})
    report = partial_subsystem_report(8, visible)
    assert report.predecessor_closed
    assert report.one_step_factorization_verified
    assert report.current_enabled_recovers_projection
    assert not report.nonclosed_legality_collision


def test_first_layer_subset_is_an_autonomous_partial_action_family():
    visible = frozenset({"h1", "h3"})
    report = partial_subsystem_report(8, visible)
    assert report.predecessor_closed
    assert report.one_step_factorization_verified
    assert report.current_enabled_recovers_projection


def test_nonclosed_upper_action_fails_at_length_one():
    report = partial_subsystem_report(8, frozenset({"h5"}))
    assert not report.predecessor_closed
    assert not report.one_step_factorization_verified
    assert not report.current_enabled_recovers_projection
    assert report.nonclosed_legality_collision
