"""Semantic implication preorder induced by a finite family of Boolean states.

For a nonempty exact-state family Omega subseteq 2^P define

    x <=_Omega y  iff  every state containing y also contains x.

This is the largest preorder under which every exact state is downward closed.
Mutually implying labels have identical membership columns and are quotiented
into one semantic label.  The quotient is a finite poset, and every exact state
projects to an order ideal of that semantic poset.

This is elementary implication/preorder mathematics used as an A2/A4 pressure
test; no generic novelty claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_boundary_width import poset_width
from .poset_observation_boundary import Relation

Element = object
State = frozenset[object]


@dataclass(frozen=True)
class SemanticImplicationPoset:
    elements: tuple[object, ...]
    exact_states: frozenset[State]
    implication_preorder: Relation
    equivalence_classes: tuple[frozenset[object], ...]
    class_relation: Relation
    projected_states: frozenset[frozenset[int]]
    semantic_width: int


def _validate_states(elements: tuple[object, ...], states: frozenset[State]) -> None:
    if not elements or len(set(elements)) != len(elements):
        raise ValueError("elements must be a non-empty tuple of distinct labels")
    if not states:
        raise ValueError("exact state family must be non-empty")
    universe = set(elements)
    if any(not set(state).issubset(universe) for state in states):
        raise ValueError("exact state contains a label outside the universe")


def semantic_implication_preorder(
    elements: tuple[object, ...], states: frozenset[State]
) -> Relation:
    _validate_states(elements, states)
    return frozenset(
        (lower, upper)
        for lower in elements
        for upper in elements
        if all(upper not in state or lower in state for state in states)
    )


def relation_is_safe_for_states(
    elements: tuple[object, ...], states: frozenset[State], relation: Relation
) -> bool:
    _validate_states(elements, states)
    universe = set(elements)
    if any(x not in universe or y not in universe for x, y in relation):
        raise ValueError("relation contains a label outside the universe")
    return all(
        lower in state
        for state in states
        for upper in state
        for lower in elements
        if (lower, upper) in relation
    )


def _equivalence_classes(
    elements: tuple[object, ...], preorder: Relation
) -> tuple[frozenset[object], ...]:
    remaining = set(elements)
    classes: list[frozenset[object]] = []
    for seed in elements:
        if seed not in remaining:
            continue
        eq = frozenset(
            x for x in elements if (x, seed) in preorder and (seed, x) in preorder
        )
        classes.append(eq)
        remaining.difference_update(eq)
    return tuple(classes)


def analyze_semantic_implication(
    elements: tuple[object, ...], states: frozenset[State]
) -> SemanticImplicationPoset:
    preorder = semantic_implication_preorder(elements, states)

    # Reflexive and transitive checks.
    if any((x, x) not in preorder for x in elements):
        raise AssertionError("semantic implication must be reflexive")
    for x in elements:
        for y in elements:
            for z in elements:
                if (x, y) in preorder and (y, z) in preorder and (x, z) not in preorder:
                    raise AssertionError("semantic implication must be transitive")
    if not relation_is_safe_for_states(elements, states, preorder):
        raise AssertionError("semantic implication must make every exact state downward closed")

    classes = _equivalence_classes(elements, preorder)
    class_of = {label: index for index, cls in enumerate(classes) for label in cls}
    class_relation = frozenset(
        (class_of[x], class_of[y]) for x, y in preorder
    )
    class_elements = tuple(range(len(classes)))

    # Quotient must be a partial order.
    for i in class_elements:
        if (i, i) not in class_relation:
            raise AssertionError("quotient relation must be reflexive")
    for i in class_elements:
        for j in class_elements:
            if i != j and (i, j) in class_relation and (j, i) in class_relation:
                raise AssertionError("mutual implication should have been quotiented")

    projected: set[frozenset[int]] = set()
    for state in states:
        # Equivalent labels have identical membership across every exact state.
        for cls in classes:
            membership = {label in state for label in cls}
            if len(membership) != 1:
                raise AssertionError("semantic equivalence class split inside one state")
        projection = frozenset(
            index for index, cls in enumerate(classes) if next(iter(cls)) in state
        )
        # Verify idealhood in semantic quotient.
        if any(
            lower not in projection
            for upper in projection
            for lower in class_elements
            if (lower, upper) in class_relation
        ):
            raise AssertionError("projected exact state must be a semantic ideal")
        projected.add(projection)

    width = poset_width(class_elements, class_relation)
    return SemanticImplicationPoset(
        elements=elements,
        exact_states=states,
        implication_preorder=preorder,
        equivalence_classes=classes,
        class_relation=class_relation,
        projected_states=frozenset(projected),
        semantic_width=width,
    )


def safe_relation_is_below_semantic_preorder(
    elements: tuple[object, ...],
    states: frozenset[State],
    candidate_relation: Relation,
) -> bool:
    if not relation_is_safe_for_states(elements, states, candidate_relation):
        raise ValueError("candidate relation is not safe for the exact states")
    semantic = semantic_implication_preorder(elements, states)
    return candidate_relation.issubset(semantic)
