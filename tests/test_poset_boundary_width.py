from enterprise_math.poset_boundary_width import (
    analyze_boundary_width,
    boundaries_to_ideal_path,
    ideal_path_to_boundaries,
)


def test_chain_width_one_recovers_scalar_boundary():
    elements = (0, 1, 2, 3)
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    report = analyze_boundary_width(elements, leq)
    assert report.width == 1
    assert report.maximum_boundary_size == 1
    assert report.chain_case


def test_two_point_antichain_width_two_is_tight():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    report = analyze_boundary_width(elements, leq)
    assert report.width == 2
    assert report.maximum_boundary_size == 2
    assert not report.chain_case
    assert report.witness_antichain == frozenset({"a", "b"})
    assert report.witness_ideal == frozenset({"a", "b"})


def test_diamond_width_two_boundary_path_round_trip():
    # a is below b,c; both b,c are below d.
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
    report = analyze_boundary_width(elements, leq)
    assert report.width == 2
    assert report.maximum_boundary_size == 2

    ideals = (
        frozenset(),
        frozenset({"a"}),
        frozenset({"a", "b"}),
        frozenset({"a", "b", "c"}),
        frozenset(elements),
    )
    boundaries = ideal_path_to_boundaries(elements, leq, ideals)
    assert boundaries == (
        frozenset(),
        frozenset({"a"}),
        frozenset({"b"}),
        frozenset({"b", "c"}),
        frozenset({"d"}),
    )
    assert boundaries_to_ideal_path(elements, leq, boundaries) == ideals


def test_boundary_labels_matter_even_at_fixed_width_and_size():
    elements = ("a", "b", "c")
    leq = frozenset({("a", "a"), ("b", "b"), ("c", "c")})
    report = analyze_boundary_width(elements, leq)
    assert report.width == 3

    left = (frozenset({"a"}),)
    right = (frozenset({"b"}),)
    assert len(left[0]) == len(right[0]) == 1
    assert boundaries_to_ideal_path(elements, leq, left) != boundaries_to_ideal_path(
        elements, leq, right
    )
