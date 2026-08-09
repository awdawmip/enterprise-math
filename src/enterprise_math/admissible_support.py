"""E001.3 finite admissible-support relation diagnostics.

A radius-indexed support family can be treated as finite relations ``R_r`` on a
terminal state set.  The deliberately small structural contract checked here is:

1. zero radius is the identity relation;
2. support is monotone in radius;
3. relational composition is subadditive:
   ``R_r ; R_s`` is contained in ``R_(r+s)`` whenever that radius is supplied.

Exact equality in (3) is a stronger *split-complete* property, not a universal
axiom.  Unit-step graph balls have it.  Integer-weight atomic geometries can
satisfy the basic contract while failing split-completeness.

These checks are finite diagnostics for candidate Enterprise Math geometry.
They do not claim that filtered relations, graph balls, or relation composition
are new mathematics.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass

State = Hashable
Relation = frozenset[tuple[State, State]]


@dataclass(frozen=True)
class AdmissibleSupportReport:
    """Finite structural status of one radius-indexed relation family."""

    radii: tuple[int, ...]
    zero_identity: bool
    monotone: bool
    subadditive: bool
    split_complete: bool


def compose_relations(left: Relation, right: Relation) -> Relation:
    """Finite relational composition: a-left-b-right-c implies a-result-c."""
    right_by_source: dict[State, set[State]] = {}
    for source, target in right:
        right_by_source.setdefault(source, set()).add(target)
    return frozenset(
        (source, target)
        for source, middle in left
        for target in right_by_source.get(middle, ())
    )


def analyze_admissible_support_family(
    states: frozenset[State], relations: Mapping[int, Relation]
) -> AdmissibleSupportReport:
    """Check the minimal finite support contract and stronger split completeness."""
    if not states:
        raise ValueError("terminal state set must be nonempty")
    if 0 not in relations:
        raise ValueError("radius family must contain radius 0")
    radii = tuple(sorted(relations))
    if any(isinstance(radius, bool) or not isinstance(radius, int) or radius < 0 for radius in radii):
        raise ValueError("radii must be non-negative integers")

    state_pairs = {(left, right) for left in states for right in states}
    for relation in relations.values():
        if not set(relation).issubset(state_pairs):
            raise ValueError("relation contains a state outside the terminal set")

    identity = frozenset((state, state) for state in states)
    zero_identity = relations[0] == identity

    monotone = True
    for left_radius in radii:
        for right_radius in radii:
            if left_radius <= right_radius and not relations[left_radius].issubset(
                relations[right_radius]
            ):
                monotone = False

    subadditive = True
    split_complete = True
    for left_radius in radii:
        for right_radius in radii:
            total = left_radius + right_radius
            if total not in relations:
                continue
            composed = compose_relations(relations[left_radius], relations[right_radius])
            if not composed.issubset(relations[total]):
                subadditive = False
            if composed != relations[total]:
                split_complete = False

    return AdmissibleSupportReport(
        radii=radii,
        zero_identity=zero_identity,
        monotone=monotone,
        subadditive=subadditive,
        split_complete=split_complete,
    )
