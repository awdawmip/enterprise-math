from enterprise_math.conjunctive_state_closure import (
    analyze_conjunctive_closure,
    conjunctive_closure,
    extent,
    same_conjunctive_future,
)
from enterprise_math.semantic_implication_poset import analyze_semantic_implication


def test_higher_order_closure_compresses_beyond_unary_implication_poset():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    semantic = analyze_semantic_implication(elements, states)
    assert semantic.semantic_width == 2
    assert conjunctive_closure(elements, states, frozenset({"a"})) == frozenset({"a"})
    assert conjunctive_closure(elements, states, frozenset({"b"})) == frozenset({"b"})
    assert conjunctive_closure(elements, states, frozenset({"a", "b"})) == frozenset({"a", "b", "c"})
    assert conjunctive_closure(elements, states, frozenset({"c"})) == frozenset({"a", "b", "c"})
    assert same_conjunctive_future(
        elements, states, frozenset({"a", "b"}), frozenset({"c"})
    )


def test_closure_equality_is_exactly_extent_equality():
    elements = (0, 1, 2)
    states = frozenset(
        {
            frozenset(),
            frozenset({0}),
            frozenset({0, 1}),
            frozenset({0, 1, 2}),
        }
    )
    assert same_conjunctive_future(elements, states, frozenset({1}), frozenset({0, 1}))
    assert not same_conjunctive_future(elements, states, frozenset({0}), frozenset({1}))


def test_impossible_query_closes_to_full_universe_and_keeps_empty_extent():
    elements = ("a", "b")
    states = frozenset({frozenset({"a"}), frozenset({"b"})})
    required = frozenset({"a", "b"})
    assert extent(elements, states, required) == frozenset()
    assert conjunctive_closure(elements, states, required) == frozenset(elements)
    assert extent(elements, states, frozenset(elements)) == frozenset()


def test_every_exact_state_is_closed():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b", "c"}),
        }
    )
    analyze_conjunctive_closure(elements, states)
    for state in states:
        assert conjunctive_closure(elements, states, state) == state


def test_closure_can_reduce_raw_query_state_count():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    report = analyze_conjunctive_closure(elements, states)
    assert report.raw_query_count == 8
    assert report.closure_count == 4
    assert report.closed_sets == frozenset(
        {
            frozenset(),
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
