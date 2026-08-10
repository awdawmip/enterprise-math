from enterprise_math.closure_action_support_cost import (
    action_dependency_support,
    action_support_report,
    largest_single_action_support,
    maximal_action_generators,
)


def test_single_upper_action_support_grows_linearly_in_perfect_family():
    expected = {
        4: 1,
        8: 3,
        16: 7,
        32: 15,
    }
    for arity, support_size in expected.items():
        report = largest_single_action_support(arity)
        assert report.raw_action_count == 1
        assert report.support_generator_count == 1
        assert report.dependency_support_count == support_size
        assert support_size == arity // 2 - 1


def test_maximal_action_boundary_generates_same_dependency_support():
    actions = frozenset({"h1", "h2", "h5"})
    generators = maximal_action_generators(8, actions)
    assert generators == frozenset({"h5"})
    assert action_dependency_support(8, actions) == action_dependency_support(8, generators)
    report = action_support_report(8, actions)
    assert report.raw_action_count == 3
    assert report.support_generator_count == 1
    assert report.dependency_support_count == 3


def test_independent_first_layer_actions_have_no_hidden_helper_support():
    report = action_support_report(8, frozenset({"h1", "h3"}))
    assert report.support_generators == frozenset({"h1", "h3"})
    assert report.dependency_support == frozenset({"h1", "h3"})
