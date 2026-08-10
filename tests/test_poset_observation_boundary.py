from enterprise_math.poset_observation_boundary import (
    analyze_poset_observation,
    antichain_dominates,
    down_closure,
    maximal_boundary,
)


def chain_poset(n: int):
    elements = tuple(range(n))
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    return elements, leq


def test_chain_is_exactly_rank_complete():
    elements, leq = chain_poset(4)
    report = analyze_poset_observation(elements, leq)
    assert report.is_chain
    assert report.rank_complete
    assert report.ideal_count == 5
    assert report.antichain_count == 5
    assert report.equal_rank_collision is None


def test_two_point_antichain_is_minimal_rank_collision():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    report = analyze_poset_observation(elements, leq)
    assert not report.is_chain
    assert not report.rank_complete
    assert report.ideal_count == 4
    left, right = report.equal_rank_collision
    assert len(left) == len(right) == 1
    assert left != right
    assert {left, right} == {frozenset({"a"}), frozenset({"b"})}


def test_maximal_antichain_reconstructs_branching_ideal():
    # a,b are incomparable and both lie below c.
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
    ideal = frozenset({"a", "b"})
    boundary = maximal_boundary(elements, leq, ideal)
    assert boundary == frozenset({"a", "b"})
    assert down_closure(elements, leq, boundary) == ideal

    top_ideal = frozenset(elements)
    top_boundary = maximal_boundary(elements, leq, top_ideal)
    assert top_boundary == frozenset({"c"})
    assert down_closure(elements, leq, top_boundary) == top_ideal


def test_monotone_ideal_path_becomes_antichain_dominance_path():
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
    boundaries = (
        frozenset(),
        frozenset({"a"}),
        frozenset({"a", "b"}),
        frozenset({"c"}),
    )
    assert all(
        antichain_dominates(elements, leq, left, right)
        for left, right in zip(boundaries, boundaries[1:])
    )


def test_equal_boundary_cardinality_is_not_semantic_equality():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    left = frozenset({"a"})
    right = frozenset({"b"})
    assert len(left) == len(right) == 1
    assert down_closure(elements, leq, left) != down_closure(elements, leq, right)
