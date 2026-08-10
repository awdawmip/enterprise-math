from enterprise_math.poset_antichain_witness_spectrum import (
    antichain_witness_spectrum,
    full_maximal_ideal_boundaries,
)


def test_chain_saturates_at_arity_one():
    elements = (0, 1, 2, 3)
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    family = frozenset({frozenset({0, 1}), frozenset({0, 1, 2, 3})})
    one = antichain_witness_spectrum(elements, leq, family, 1)
    four = antichain_witness_spectrum(elements, leq, family, 4)
    assert one.poset_width == 1
    assert one.saturated
    assert one.may_antichains == four.may_antichains
    assert one.maximal_generators == four.maximal_generators == frozenset({frozenset({3})})


def test_width_two_poset_saturates_at_two():
    elements = ("a", "b", "c")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "c"),
            ("b", "c"),
        }
    )
    family = frozenset({frozenset({"a", "b"})})
    one = antichain_witness_spectrum(elements, leq, family, 1)
    two = antichain_witness_spectrum(elements, leq, family, 2)
    three = antichain_witness_spectrum(elements, leq, family, 3)
    assert one.poset_width == 2
    assert not one.saturated
    assert two.saturated and three.saturated
    assert two.may_antichains == three.may_antichains
    assert frozenset({"a", "b"}) in two.may_antichains
    assert frozenset({"a", "b"}) not in one.may_antichains


def test_antichain_geometry_recovers_raw_hypergraph_skeleton():
    elements = ("a", "b", "c")
    leq = frozenset((x, x) for x in elements)
    family = frozenset({frozenset({"a", "b"}), frozenset({"b", "c"})})
    spectrum = antichain_witness_spectrum(elements, leq, family, 2)
    assert spectrum.maximal_generators == frozenset(
        {frozenset({"a", "b"}), frozenset({"b", "c"})}
    )


def test_full_spectrum_generators_match_boundaries_of_maximal_ideals():
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
    family = frozenset(
        {
            frozenset({"a", "b"}),
            frozenset({"a", "c"}),
            frozenset({"a"}),
        }
    )
    spectrum = antichain_witness_spectrum(elements, leq, family, 4)
    assert spectrum.saturated
    assert spectrum.maximal_generators == full_maximal_ideal_boundaries(
        elements, leq, family
    ) == frozenset({frozenset({"b"}), frozenset({"c"})})
