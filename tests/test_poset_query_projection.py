from enterprise_math.poset_query_projection import (
    analyze_query_projection,
    lift_query_ideal,
    project_ideal_to_query,
    query_boundary,
)


def diamond_poset():
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
    return elements, leq


def test_full_query_recovers_ambient_width_two():
    elements, leq = diamond_poset()
    report = analyze_query_projection(elements, leq, elements)
    assert report.query_width == 2
    assert report.signature_count == report.ambient_ideal_count
    assert not report.scalar_rank_complete


def test_chain_query_inside_width_two_ambient_recovers_scalar_rank():
    elements, leq = diamond_poset()
    query = ("a", "d")
    report = analyze_query_projection(elements, leq, query)
    assert report.query_width == 1
    assert report.scalar_rank_complete
    assert report.signature_count == 3
    assert report.signature_count < report.ambient_ideal_count


def test_single_label_query_collapses_wide_antichain():
    elements = ("a", "b", "c", "d")
    leq = frozenset((x, x) for x in elements)
    report = analyze_query_projection(elements, leq, ("c",))
    assert report.query_width == 1
    assert report.scalar_rank_complete
    assert report.signature_count == 2
    assert report.ambient_ideal_count == 16


def test_every_induced_query_ideal_lifts_exactly():
    elements, leq = diamond_poset()
    query = ("b", "c")
    for query_ideal in (
        frozenset(),
        frozenset({"b"}),
        frozenset({"c"}),
        frozenset({"b", "c"}),
    ):
        ambient = lift_query_ideal(elements, leq, query, query_ideal)
        assert project_ideal_to_query(elements, leq, ambient, query) == query_ideal


def test_query_boundary_can_be_smaller_than_ambient_boundary():
    elements, leq = diamond_poset()
    ambient_ideal = frozenset({"a", "b", "c"})
    # Ambient boundary is {b,c}, but query asks only along chain a<d.
    assert query_boundary(elements, leq, ambient_ideal, ("a", "d")) == frozenset({"a"})
