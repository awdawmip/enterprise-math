"""Boolean predicate-transformer diagnostic for DOMAIN versus RELATION defects.

For finite relation ``R`` on state set X define the existential backward
predicate transformer

    T_R(P) = { x : exists y in P, x R y }.

For every relation, ``T_R`` preserves bottom and finite joins (unions).
Two stronger Boolean laws diagnose two different world-structure questions.

### Top preservation = totality / DOMAIN

    T_R(X) = X

iff every source has at least one successor.  Failure identifies exactly the
sources on which the relation is undefined.

### Meet preservation = functionality / RELATION

    T_R(P intersect Q) = T_R(P) intersect T_R(Q)  for all P,Q

iff every source has at most one successor.  If source x branches to distinct
y,z, singleton predicates {y} and {z} give an immediate meet counterexample at
x.  Conversely a source with at most one successor cannot satisfy two target
predicates through different witnesses, so intersections are preserved.

Therefore:

* partial deterministic action: meet-preserving, top-defective;
* total multivalued relation: top-preserving, meet-defective;
* total deterministic function: preserves joins, meets, bottom and top, hence is
  a Boolean-algebra homomorphism on predicates (and preserves complements).

This gives one exact algebraic table for the project DOMAIN/RELATION boundary.
Observable-UNDEFINED totalization of a deterministic partial map can restore the
total Boolean-homomorphism law on an extended verification codomain, consistent
with FQ-006, without declaring the marker to be a new physical state.

Predicate transformers and modal relation semantics are standard prior
mathematics/logic.  The project value is the precision-state diagnostic routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable, Iterable

from .admissible_support import Relation


State = Hashable


def _states(values: Iterable[State]) -> frozenset[State]:
    result = frozenset(values)
    if not result:
        raise ValueError("state set must be nonempty")
    return result


def _relation(states: frozenset[State], relation: Relation) -> Relation:
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    if any(source not in states or target not in states for source, target in relation):
        raise ValueError("relation contains state outside declared state set")
    return relation


def existential_preimage(
    states: Iterable[State],
    relation: Relation,
    predicate: Iterable[State],
) -> frozenset[State]:
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    target_set = frozenset(predicate)
    if not target_set.issubset(state_values):
        raise ValueError("predicate contains state outside declared state set")
    return frozenset(
        source
        for source, target in relation_values
        if target in target_set
    )


def relation_undefined_sources(
    states: Iterable[State],
    relation: Relation,
) -> frozenset[State]:
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    domain = existential_preimage(state_values, relation_values, state_values)
    return state_values - domain


def relation_branching_sources(
    states: Iterable[State],
    relation: Relation,
) -> frozenset[State]:
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    targets: dict[State, set[State]] = {state: set() for state in state_values}
    for source, target in relation_values:
        targets[source].add(target)
    return frozenset(source for source, values in targets.items() if len(values) > 1)


def predicate_transformer_preserves_top(
    states: Iterable[State],
    relation: Relation,
) -> bool:
    state_values = _states(states)
    return existential_preimage(state_values, relation, state_values) == state_values


def predicate_transformer_preserves_all_meets(
    states: Iterable[State],
    relation: Relation,
) -> bool:
    """Finite exact check; theorem-equivalent to absence of branching sources."""
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    ordered = tuple(state_values)
    predicates = tuple(
        frozenset(subset)
        for size in range(len(ordered) + 1)
        for subset in combinations(ordered, size)
    )
    for left in predicates:
        for right in predicates:
            lhs = existential_preimage(
                state_values,
                relation_values,
                left & right,
            )
            rhs = (
                existential_preimage(state_values, relation_values, left)
                & existential_preimage(state_values, relation_values, right)
            )
            if lhs != rhs:
                return False
    return True


def singleton_meet_branch_witness(
    states: Iterable[State],
    relation: Relation,
) -> tuple[State, State, State] | None:
    """Return ``(source,y,z)`` witnessing meet failure by distinct targets."""
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    targets: dict[State, list[State]] = {state: [] for state in state_values}
    for source, target in relation_values:
        if target not in targets[source]:
            targets[source].append(target)
    for source, values in targets.items():
        if len(values) >= 2:
            return source, values[0], values[1]
    return None


@dataclass(frozen=True)
class PredicateTransformerDiagnostic:
    undefined_sources: frozenset[State]
    branching_sources: frozenset[State]
    preserves_top: bool
    preserves_all_meets: bool

    @property
    def total(self) -> bool:
        return not self.undefined_sources

    @property
    def functional(self) -> bool:
        return not self.branching_sources

    @property
    def total_deterministic(self) -> bool:
        return self.total and self.functional


def relation_predicate_transformer_diagnostic(
    states: Iterable[State],
    relation: Relation,
) -> PredicateTransformerDiagnostic:
    state_values = _states(states)
    relation_values = _relation(state_values, relation)
    undefined = relation_undefined_sources(state_values, relation_values)
    branching = relation_branching_sources(state_values, relation_values)
    top = predicate_transformer_preserves_top(state_values, relation_values)
    meets = predicate_transformer_preserves_all_meets(state_values, relation_values)
    if top != (not undefined):
        raise AssertionError("top-preservation/totality theorem failed")
    if meets != (not branching):
        raise AssertionError("meet-preservation/functionality theorem failed")
    return PredicateTransformerDiagnostic(
        undefined_sources=undefined,
        branching_sources=branching,
        preserves_top=top,
        preserves_all_meets=meets,
    )
