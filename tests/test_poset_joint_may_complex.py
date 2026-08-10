from enterprise_math.poset_joint_may_complex import (
    enumerate_joint_may_faces,
    joint_may_from_maximals,
    joint_may_must_state,
    joint_must_from_intersection,
    maximal_admissible_ideals,
    same_joint_may_must_future,
)


def antichain_poset(*labels: str):
    elements = tuple(labels)
    leq = frozenset((x, x) for x in elements)
    return elements, leq


def test_nonmaximal_admissible_ideals_are_joint_may_redundant():
    elements, leq = antichain_poset("a", "b", "c")
    family = frozenset(
        {
            frozenset({"a"}),
            frozenset({"a", "b"}),
            frozenset({"a", "b", "c"}),
        }
    )
    maximals = maximal_admissible_ideals(elements, leq, family)
    assert maximals == frozenset({frozenset({"a", "b", "c"})})
    assert joint_may_from_maximals(maximals, frozenset({"a", "c"}))
    assert joint_may_from_maximals(maximals, frozenset({"a", "b", "c"}))


def test_joint_may_complex_is_generated_by_maximal_admissible_ideals():
    elements, leq = antichain_poset("a", "b", "c")
    family = frozenset({frozenset({"a", "b"}), frozenset({"b", "c"})})
    maximals = maximal_admissible_ideals(elements, leq, family)
    faces = enumerate_joint_may_faces(elements, maximals)
    assert frozenset({"a", "b"}) in faces
    assert frozenset({"b", "c"}) in faces
    assert frozenset({"a", "c"}) not in faces
    assert frozenset({"a", "b", "c"}) not in faces


def test_full_joint_may_must_state_needs_must_plus_maximal_faces():
    elements, leq = antichain_poset("a", "b")
    family = frozenset({frozenset({"a"}), frozenset({"a", "b"})})
    state = joint_may_must_state(elements, leq, family)
    assert state.must_ideal == frozenset({"a"})
    assert state.maximal_admissible_ideals == frozenset({frozenset({"a", "b"})})
    assert joint_must_from_intersection(state.must_ideal, frozenset({"a"}))
    assert not joint_must_from_intersection(state.must_ideal, frozenset({"b"}))
    assert joint_may_from_maximals(state.maximal_admissible_ideals, frozenset({"a", "b"}))


def test_same_joint_may_must_future_can_hide_exact_family_identity():
    elements, leq = antichain_poset("a", "b", "c")
    family_left = frozenset(
        {
            frozenset({"a", "b", "c"}),
            frozenset({"a"}),
            frozenset({"b"}),
        }
    )
    family_right = frozenset(
        {
            frozenset({"a", "b", "c"}),
            frozenset({"a"}),
            frozenset({"c"}),
        }
    )
    left = joint_may_must_state(elements, leq, family_left)
    right = joint_may_must_state(elements, leq, family_right)
    assert same_joint_may_must_future(left, right)
    assert family_left != family_right
    # Exact-state membership future sees a difference hidden by existential/universal support.
    assert frozenset({"b"}) in family_left
    assert frozenset({"b"}) not in family_right
