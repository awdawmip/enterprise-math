from enterprise_math.poset_may_must_support import (
    joint_may,
    may_must_support,
    pointwise_status,
    same_pointwise_future,
)


def test_union_and_intersection_are_exact_pointwise_supports():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    family = frozenset({frozenset({"a"}), frozenset({"b"})})
    state = may_must_support(elements, leq, family)
    assert state.must_ideal == frozenset()
    assert state.may_ideal == frozenset({"a", "b"})
    assert pointwise_status(state, "a") == "MAY"
    assert pointwise_status(state, "b") == "MAY"


def test_nested_poset_pointwise_status_respects_ideal_geometry():
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
    family = frozenset(
        {
            frozenset({"a"}),
            frozenset({"a", "b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    state = may_must_support(elements, leq, family)
    assert state.must_ideal == frozenset({"a"})
    assert state.may_ideal == frozenset({"a", "b", "c"})
    assert pointwise_status(state, "a") == "MUST"
    assert pointwise_status(state, "b") == "MAY"
    assert pointwise_status(state, "c") == "MAY"


def test_same_may_must_support_can_hide_joint_correlation():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})

    separated = frozenset({frozenset({"a"}), frozenset({"b"})})
    correlated = frozenset({frozenset(), frozenset({"a", "b"})})

    state_left = may_must_support(elements, leq, separated)
    state_right = may_must_support(elements, leq, correlated)
    assert same_pointwise_future(state_left, state_right)
    assert state_left.must_ideal == state_right.must_ideal == frozenset()
    assert state_left.may_ideal == state_right.may_ideal == frozenset({"a", "b"})

    required = frozenset({"a", "b"})
    assert not joint_may(separated, required)
    assert joint_may(correlated, required)


def test_singleton_family_collapses_may_and_must_to_exact_ideal():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    exact = frozenset({"a"})
    state = may_must_support(elements, leq, frozenset({exact}))
    assert state.must_ideal == exact
    assert state.may_ideal == exact
    assert state.must_boundary == state.may_boundary == frozenset({"a"})
