from enterprise_math.closure_action_state_support import (
    action_state_support_report,
    largest_single_action_support_comparison,
    q_only_state_support,
)


def test_q_only_words_factor_through_actions_plus_direct_helper_predecessors():
    for arity, actions in (
        (8, frozenset({"h5"})),
        (8, frozenset({"h1", "h3"})),
        (16, frozenset({"h13"})),
        (16, frozenset({"h13", "h14"})),
    ):
        report = action_state_support_report(arity, actions)
        assert report.q_word_one_step_factorization_verified
        assert report.direct_predecessor_necessity_verified
        assert report.state_support.issubset(report.autonomous_action_support)


def test_single_top_action_static_state_support_stays_three_while_action_closure_grows():
    expected = {
        8: (3, 3),
        16: (3, 7),
        32: (3, 15),
    }
    for arity, (state_count, action_support_count) in expected.items():
        report = largest_single_action_support_comparison(arity)
        assert report.raw_action_count == 1
        assert report.static_state_support_count == state_count
        assert report.autonomous_action_support_count == action_support_count


def test_two_top_actions_need_six_static_labels_but_full_helper_forest_as_action_support():
    report = action_state_support_report(16, frozenset({"h13", "h14"}))
    assert len(report.state_support) == 6
    assert len(report.autonomous_action_support) == 14


def test_first_layer_actions_have_no_hidden_helper_state_tax():
    actions = frozenset({"h1", "h3"})
    assert q_only_state_support(8, actions) == actions
