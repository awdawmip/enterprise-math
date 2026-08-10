from enterprise_math.poset_joint_query_normal import (
    ideal_contains_query,
    joint_query_normal_form,
    same_joint_query_future,
    worst_case_essential_arity,
)


def test_chain_query_collapses_to_single_maximal_label():
    elements = (0, 1, 2, 3, 4)
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    normal = joint_query_normal_form(elements, leq, frozenset({0, 1, 3, 4}))
    assert normal.raw_arity == 4
    assert normal.maximal_antichain == frozenset({4})
    assert normal.essential_arity == 1
    assert worst_case_essential_arity(elements, leq, 4) == 1


def test_antichain_query_does_not_collapse():
    elements = ("a", "b", "c")
    leq = frozenset((x, x) for x in elements)
    required = frozenset(elements)
    normal = joint_query_normal_form(elements, leq, required)
    assert normal.maximal_antichain == required
    assert normal.essential_arity == 3
    assert worst_case_essential_arity(elements, leq, 10) == 3


def test_comparable_raw_queries_have_same_future_normal_form():
    elements = ("a", "b", "c")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "b"),
            ("b", "c"),
            ("a", "c"),
        }
    )
    assert same_joint_query_future(
        elements,
        leq,
        frozenset({"a", "b", "c"}),
        frozenset({"c"}),
    )


def test_ideal_membership_uses_only_maximal_query_antichain():
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
    ideal = frozenset({"a", "b", "c"})
    assert ideal_contains_query(elements, leq, ideal, frozenset({"a", "b", "c"}))
    assert not ideal_contains_query(elements, leq, ideal, frozenset({"b", "d"}))
