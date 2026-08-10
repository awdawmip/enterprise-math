"""Observable signatures for finite relation-valued future operations.

A4 owns finite multivalued support/correspondence.  A1/A2/P023 own functional
kernels, declared future signatures and factorization.  This bridge states the
small finite interface between those layers without identifying them.

Let ``R`` be a finite relation on a declared state set and let ``O`` be a
hashable observation of target states.  The one-step future signature of source
``x`` is the **set-valued** observation image

    Sigma_(R,O)(x) = { O(y) : (x,y) in R }.

The empty set means the relation is undefined / has no admissible target from
that source.  It is deliberately not identified with identity, omission or an
ordinary observation value.

Three different questions then have exact finite answers.

1. **Did the raw relation branch?**
   ``R(x)`` may contain several target states.
2. **Is the declared observable deterministic?**
   It is deterministic at ``x`` exactly when ``Sigma_(R,O)(x)`` has at most one
   element.  Several raw targets may therefore collapse to one observable value.
3. **Can a source quotient be used safely for this relation+observable?**
   A quotient key ``q`` is one-step future-safe exactly when

       q(x)=q(x')  ->  Sigma_(R,O)(x)=Sigma_(R,O)(x').

   Equality includes definedness: an empty set cannot be merged with a nonempty
   target-observation set merely because the latter is singleton.

The coarsest one-step partition for this declared future query is therefore the
functional kernel of the **set-valued signature map** ``Sigma_(R,O)``.  This does
not turn the underlying A4 correspondence into a deterministic state update; it
only says what the chosen future observation can distinguish.

For a sequence/composition of relations, compute the composed relation first and
apply the same signature.  If intermediate legality/observation is itself part of
the future language, it must be included separately rather than inferred from a
terminal-only composed relation.

Finite relations, powerset-valued maps, quotient factorization and behavioral
signatures are standard prior mathematics/computer science.  The project value
is the explicit A4<->P023 executable boundary and the refusal to conflate raw
relation branching with observable nondeterminism.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Mapping
from dataclasses import dataclass

from .admissible_support import Relation, compose_relations


State = Hashable
Observation = Hashable


def _state_set(states: Iterable[State]) -> frozenset[State]:
    result = frozenset(states)
    if not result:
        raise ValueError("state set must be nonempty")
    return result


def _validate_relation(
    states: frozenset[State],
    relation: Relation,
) -> None:
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset of ordered pairs")
    allowed = {(left, right) for left in states for right in states}
    if not set(relation).issubset(allowed):
        raise ValueError("relation contains a source or target outside the state set")


def raw_target_set(relation: Relation, source: State) -> frozenset[State]:
    """Return all raw targets related to one source."""
    return frozenset(target for current, target in relation if current == source)


def observed_target_set(
    relation: Relation,
    source: State,
    observation: Callable[[State], Observation],
) -> frozenset[Observation]:
    """Return ``{O(y):(source,y) in relation}``, preserving empty/undefined."""
    return frozenset(observation(target) for target in raw_target_set(relation, source))


@dataclass(frozen=True)
class RelationObservableSourceReport:
    source: State
    raw_targets: frozenset[State]
    observed_targets: frozenset[Observation]

    @property
    def defined(self) -> bool:
        return bool(self.raw_targets)

    @property
    def raw_relation_branches(self) -> bool:
        return len(self.raw_targets) > 1

    @property
    def observable_deterministic(self) -> bool:
        return len(self.observed_targets) <= 1

    @property
    def branching_hidden_by_observation(self) -> bool:
        return self.raw_relation_branches and len(self.observed_targets) == 1


def relation_observable_source_report(
    states: Iterable[State],
    relation: Relation,
    source: State,
    observation: Callable[[State], Observation],
) -> RelationObservableSourceReport:
    state_values = _state_set(states)
    _validate_relation(state_values, relation)
    if source not in state_values:
        raise ValueError("source is outside the state set")
    raw = raw_target_set(relation, source)
    observed = frozenset(observation(target) for target in raw)
    return RelationObservableSourceReport(
        source=source,
        raw_targets=raw,
        observed_targets=observed,
    )


def relation_observation_signature_map(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
) -> dict[State, frozenset[Observation]]:
    """Exact one-step powerset-valued future signature for every source."""
    state_values = _state_set(states)
    _validate_relation(state_values, relation)
    return {
        source: observed_target_set(relation, source, observation)
        for source in state_values
    }


def relation_observable_is_deterministic(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
    *,
    require_defined: bool = False,
) -> bool:
    """Whether every source has at most one observed target (and optionally one)."""
    signatures = relation_observation_signature_map(
        states,
        relation,
        observation,
    )
    if require_defined:
        return all(len(signature) == 1 for signature in signatures.values())
    return all(len(signature) <= 1 for signature in signatures.values())


def relation_observation_partition(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
) -> frozenset[frozenset[State]]:
    """Coarsest one-step source partition preserving the set-valued signature."""
    signatures = relation_observation_signature_map(
        states,
        relation,
        observation,
    )
    groups: dict[frozenset[Observation], set[State]] = {}
    for source, signature in signatures.items():
        groups.setdefault(signature, set()).add(source)
    return frozenset(frozenset(group) for group in groups.values())


def quotient_is_relation_observation_safe(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
    quotient_key: Callable[[State], Hashable],
) -> bool:
    """Whether the powerset-valued future signature factors through ``quotient_key``."""
    signatures = relation_observation_signature_map(
        states,
        relation,
        observation,
    )
    seen: dict[Hashable, frozenset[Observation]] = {}
    for source, signature in signatures.items():
        key = quotient_key(source)
        if key in seen and seen[key] != signature:
            return False
        seen[key] = signature
    return True


def deterministic_observed_transition(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
) -> dict[State, Observation | None]:
    """Compile a partial deterministic observed transition when every image is singleton/empty.

    ``None`` is used only as the returned Python marker for undefinedness.  To
    avoid collision with a legitimate observed ``None`` value, this helper
    rejects such observations.  The set-valued signature API above has no such
    restriction and remains the canonical semantic interface.
    """
    signatures = relation_observation_signature_map(
        states,
        relation,
        observation,
    )
    result: dict[State, Observation | None] = {}
    for source, signature in signatures.items():
        if len(signature) > 1:
            raise ValueError("relation is not deterministic under the declared observation")
        if None in signature:
            raise ValueError(
                "deterministic helper reserves None for undefinedness; use set-valued signature instead"
            )
        result[source] = next(iter(signature)) if signature else None
    return result


def composed_relation_observation_signature_map(
    states: Iterable[State],
    first: Relation,
    second: Relation,
    observation: Callable[[State], Observation],
) -> dict[State, frozenset[Observation]]:
    """Terminal-only observed signature of finite relational composition ``first;second``."""
    state_values = _state_set(states)
    _validate_relation(state_values, first)
    _validate_relation(state_values, second)
    composed = compose_relations(first, second)
    return relation_observation_signature_map(
        state_values,
        composed,
        observation,
    )


def partition_refines_relation_observation_partition(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
    candidate_partition: Iterable[Iterable[State]],
) -> bool:
    """Check that every candidate fiber is contained in one exact signature fiber."""
    state_values = _state_set(states)
    exact = relation_observation_partition(state_values, relation, observation)
    exact_by_state: dict[State, frozenset[State]] = {
        state: block for block in exact for state in block
    }
    candidate_blocks = tuple(frozenset(block) for block in candidate_partition)
    if not candidate_blocks:
        raise ValueError("candidate partition must be nonempty")
    if any(not block for block in candidate_blocks):
        raise ValueError("candidate partition cannot contain an empty block")
    covered = set().union(*candidate_blocks)
    if covered != set(state_values):
        raise ValueError("candidate partition must cover exactly the state set")
    if sum(len(block) for block in candidate_blocks) != len(covered):
        raise ValueError("candidate partition blocks must be disjoint")
    return all(
        all(exact_by_state[state] == exact_by_state[next(iter(block))] for state in block)
        for block in candidate_blocks
    )
