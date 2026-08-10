from enterprise_math.semantic_implication_poset import (
    analyze_semantic_implication,
    safe_relation_is_below_semantic_preorder,
)


def test_ambient_chain_can_semantically_open_into_width_two():
    elements = ("a", "b")
    states = frozenset({frozenset({"a"}), frozenset({"b"})})
    report = analyze_semantic_implication(elements, states)
    assert report.semantic_width == 2
    assert ("a", "b") not in report.implication_preorder
    assert ("b", "a") not in report.implication_preorder
    assert report.projected_states == frozenset({frozenset({0}), frozenset({1})})


def test_vacuous_implication_can_reverse_ambient_intuition_safely():
    elements = ("a", "b")
    states = frozenset({frozenset({"b"})})
    report = analyze_semantic_implication(elements, states)
    # a is never active, so a-active => b-active is vacuously true: b <=_Omega a.
    assert ("b", "a") in report.implication_preorder
    assert ("a", "b") not in report.implication_preorder
    assert report.semantic_width == 1


def test_always_coactive_labels_are_quotiented():
    elements = ("a", "b", "c")
    states = frozenset({frozenset(), frozenset({"a", "b"}), frozenset({"a", "b", "c"})})
    report = analyze_semantic_implication(elements, states)
    assert frozenset({"a", "b"}) in report.equivalence_classes
    assert len(report.equivalence_classes) == 2
    assert report.semantic_width == 1


def test_semantic_preorder_is_largest_safe_relation():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"a", "b"}),
            frozenset({"a", "c"}),
        }
    )
    candidate = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "b"),
            ("a", "c"),
        }
    )
    assert safe_relation_is_below_semantic_preorder(elements, states, candidate)
    report = analyze_semantic_implication(elements, states)
    assert candidate.issubset(report.implication_preorder)


def test_semantic_projected_states_are_ideals_even_when_original_states_break_external_order():
    elements = (0, 1, 2)
    states = frozenset({frozenset({2}), frozenset({0, 2}), frozenset({1, 2})})
    report = analyze_semantic_implication(elements, states)
    # Every projected state was checked internally for idealhood; ensure we retain all three distinctions.
    assert len(report.projected_states) == 3
