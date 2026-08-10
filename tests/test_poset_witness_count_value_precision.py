from enterprise_math.poset_witness_count_value_precision import (
    positive_support_family,
    witness_count_value_state,
)


def test_exact_count_collapses_to_three_support_statuses():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    multiplicities = {
        frozenset({"a"}): 1,
        frozenset({"b"}): 1,
        frozenset({"a", "b"}): 2,
    }
    assert witness_count_value_state(elements, leq, multiplicities, frozenset({"a", "b"})).support_status == "MAY"
    assert witness_count_value_state(elements, leq, multiplicities, frozenset({"a"})).support_status == "MAY"
    assert witness_count_value_state(elements, leq, multiplicities, frozenset()).support_status == "MUST"


def test_same_support_and_total_can_hide_different_exact_counts():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    left = {
        frozenset({"a"}): 1,
        frozenset({"b"}): 1,
        frozenset({"a", "b"}): 2,
    }
    right = {
        frozenset({"a"}): 2,
        frozenset({"b"}): 1,
        frozenset({"a", "b"}): 1,
    }
    assert positive_support_family(elements, leq, left) == positive_support_family(elements, leq, right)
    left_b = witness_count_value_state(elements, leq, left, frozenset({"b"}))
    right_b = witness_count_value_state(elements, leq, right, frozenset({"b"}))
    assert left_b.total_multiplicity == right_b.total_multiplicity == 4
    assert left_b.support_status == right_b.support_status == "MAY"
    assert left_b.exact_count == 3
    assert right_b.exact_count == 2


def test_must_is_exactly_count_equal_total():
    elements = (0, 1)
    leq = frozenset({(0, 0), (1, 1)})
    multiplicities = {
        frozenset({0}): 2,
        frozenset({0, 1}): 3,
    }
    state = witness_count_value_state(elements, leq, multiplicities, frozenset({0}))
    assert state.total_multiplicity == 5
    assert state.exact_count == 5
    assert state.support_status == "MUST"


def test_impossible_is_exactly_zero_count():
    elements = (0, 1)
    leq = frozenset({(0, 0), (1, 1)})
    multiplicities = {frozenset({0}): 4}
    state = witness_count_value_state(elements, leq, multiplicities, frozenset({1}))
    assert state.exact_count == 0
    assert state.support_status == "IMPOSSIBLE"
