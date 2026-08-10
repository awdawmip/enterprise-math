from enterprise_math.conjunctive_generator_horizon import analyze_generator_horizon
from enterprise_math.poset_observation_boundary import enumerate_order_ideals


def test_higher_order_dependency_makes_horizon_strictly_smaller_than_unary_width():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    report = analyze_generator_horizon(elements, states)
    assert report.semantic_width == 2
    assert report.generator_horizon == 1
    assert report.strict_below_width


def test_all_ideals_of_chain_recover_width_one_horizon():
    elements = (0, 1, 2, 3)
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    states = frozenset(enumerate_order_ideals(elements, leq))
    report = analyze_generator_horizon(elements, states)
    assert report.semantic_width == 1
    assert report.generator_horizon == 1
    assert not report.strict_below_width


def test_all_ideals_of_diamond_recover_poset_width_two_horizon():
    elements = ("a", "b", "c", "d")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("d", "d"),
            ("a", "b"),
            ("a", "c"),
            ("a", "d"),
            ("b", "d"),
            ("c", "d"),
        }
    )
    states = frozenset(enumerate_order_ideals(elements, leq))
    report = analyze_generator_horizon(elements, states)
    assert report.semantic_width == 2
    assert report.generator_horizon == 2
    assert not report.strict_below_width


def test_single_full_state_has_zero_generator_horizon():
    elements = ("a", "b")
    states = frozenset({frozenset(elements)})
    report = analyze_generator_horizon(elements, states)
    assert report.semantic_width == 1
    assert report.generator_horizon == 0
    assert report.strict_below_width


def test_minimum_generator_for_top_closure_can_be_single_derived_label():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    report = analyze_generator_horizon(elements, states)
    top = next(info for info in report.closure_generators if info.closed_set == frozenset(elements))
    assert top.minimum_size == 1
    assert frozenset({"c"}) in top.minimum_generators
