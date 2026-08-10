from enterprise_math.poset_bounded_witness_skeleton import (
    bounded_witness_skeleton,
    jointly_may_up_to_k,
)


def antichain_poset(*labels: str):
    elements = tuple(labels)
    leq = frozenset((x, x) for x in elements)
    return elements, leq


def test_arity_one_is_exactly_pointwise_may_support():
    elements, leq = antichain_poset("a", "b", "c")
    family = frozenset({frozenset({"a", "b"}), frozenset({"b", "c"})})
    skeleton = bounded_witness_skeleton(elements, leq, family, 1)
    assert skeleton.may_support == frozenset({"a", "b", "c"})
    assert skeleton.maximal_faces == frozenset(
        {frozenset({"a"}), frozenset({"b"}), frozenset({"c"})}
    )


def test_arity_two_detects_pairwise_correlation_hidden_by_pointwise_support():
    elements, leq = antichain_poset("a", "b", "c")
    family = frozenset({frozenset({"a", "b"}), frozenset({"b", "c"})})
    one = bounded_witness_skeleton(elements, leq, family, 1)
    two = bounded_witness_skeleton(elements, leq, family, 2)
    assert one.may_support == two.may_support == frozenset({"a", "b", "c"})
    assert jointly_may_up_to_k(two, frozenset({"a", "b"}))
    assert jointly_may_up_to_k(two, frozenset({"b", "c"}))
    assert not jointly_may_up_to_k(two, frozenset({"a", "c"}))


def test_full_arity_recovers_full_maximal_witness_faces():
    elements, leq = antichain_poset("a", "b", "c", "d")
    family = frozenset(
        {
            frozenset({"a", "b", "c"}),
            frozenset({"b", "d"}),
            frozenset({"a"}),
        }
    )
    skeleton = bounded_witness_skeleton(elements, leq, family, 4)
    assert skeleton.maximal_faces == frozenset(
        {frozenset({"a", "b", "c"}), frozenset({"b", "d"})}
    )


def test_arity_three_can_refine_pairwise_complete_signature():
    elements, leq = antichain_poset("a", "b", "c")
    # Every pair appears somewhere, but no exact state contains all three.
    family = frozenset(
        {
            frozenset({"a", "b"}),
            frozenset({"a", "c"}),
            frozenset({"b", "c"}),
        }
    )
    two = bounded_witness_skeleton(elements, leq, family, 2)
    three = bounded_witness_skeleton(elements, leq, family, 3)
    assert all(
        jointly_may_up_to_k(two, pair)
        for pair in (
            frozenset({"a", "b"}),
            frozenset({"a", "c"}),
            frozenset({"b", "c"}),
        )
    )
    assert not jointly_may_up_to_k(three, frozenset({"a", "b", "c"}))
