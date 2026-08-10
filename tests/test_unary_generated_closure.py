from enterprise_math.poset_observation_boundary import enumerate_order_ideals
from enterprise_math.unary_generated_closure import analyze_unary_generated_closure


def test_all_ideals_are_unary_generated_and_recover_poset_width():
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
    report = analyze_unary_generated_closure(elements, states)
    assert report.unary_generated
    assert report.mandatory_core == frozenset()
    assert report.optional_semantic_width == 2
    assert report.generator_horizon == 2
    assert report.first_defect_query is None


def test_higher_order_synergy_is_detected_exactly():
    elements = ("a", "b", "c")
    states = frozenset(
        {
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    report = analyze_unary_generated_closure(elements, states)
    assert not report.unary_generated
    assert report.optional_semantic_width == 2
    assert report.generator_horizon == 1
    assert report.first_defect_query == frozenset({"a", "b"})
    assert report.first_defect_labels == frozenset({"c"})


def test_mandatory_core_is_removed_before_width_horizon():
    elements = ("m", "a", "b")
    states = frozenset(
        {
            frozenset({"m"}),
            frozenset({"m", "a"}),
            frozenset({"m", "a", "b"}),
        }
    )
    report = analyze_unary_generated_closure(elements, states)
    assert report.unary_generated
    assert report.mandatory_core == frozenset({"m"})
    assert report.optional_semantic_width == 1
    assert report.generator_horizon == 1


def test_all_labels_mandatory_gives_zero_optional_width_and_zero_horizon():
    elements = ("a", "b")
    states = frozenset({frozenset({"a", "b"})})
    report = analyze_unary_generated_closure(elements, states)
    assert report.unary_generated
    assert report.mandatory_core == frozenset({"a", "b"})
    assert report.optional_semantic_width == 0
    assert report.generator_horizon == 0


def test_two_independent_optional_labels_have_width_two_horizon():
    elements = ("a", "b")
    states = frozenset(
        {
            frozenset(),
            frozenset({"a"}),
            frozenset({"b"}),
            frozenset({"a", "b"}),
        }
    )
    report = analyze_unary_generated_closure(elements, states)
    assert report.unary_generated
    assert report.optional_semantic_width == 2
    assert report.generator_horizon == 2
