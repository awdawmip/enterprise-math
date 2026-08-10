"""Composition law and reactivation boundary for relation-observable signatures.

A relation can branch in raw target state while looking deterministic under a
coarse target observation ``O``.  That one-step collapse is not automatically
safe for later relation composition: a later relation can still read the hidden
intermediate target identity and make the branch visible again.

Let

    Sigma_(S,O)(y) = { O(z) : (y,z) in S }.

The observation ``O`` is a one-step congruence for the later relation ``S``
exactly when this powerset-valued signature is constant on ``O``-fibers:

    O(y)=O(y') -> Sigma_(S,O)(y)=Sigma_(S,O)(y').

When that condition holds, define the descended coarse set-transition

    barSigma_S(a) = Sigma_(S,O)(y)    for any O(y)=a.

Then every earlier relation ``R`` satisfies the exact terminal composition law

    Sigma_(R;S,O)(x)
      = union_(a in Sigma_(R,O)(x)) barSigma_S(a).

So raw intermediate states may be erased before composition precisely when the
later set-valued future signature descends through the chosen observation.

In particular, if ``R`` and ``S`` are both observable-deterministic and ``S``
is observation-compatible in this sense, then ``R;S`` remains observable-
deterministic.  Without the compatibility condition the implication is false:
two raw targets hidden in one current observation class can be split again by
``S``.

This is terminal-only relational composition.  If the future language observes
whether each intermediate branch remains defined, a dead branch must be kept in
that richer signature; ordinary relational composition drops dead paths and is
therefore insufficient for FQ-006-style legality-sensitive semantics.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable
from dataclasses import dataclass

from .admissible_support import Relation
from .relation_observable_signature import (
    composed_relation_observation_signature_map,
    quotient_is_relation_observation_safe,
    relation_observable_is_deterministic,
    relation_observation_signature_map,
)


State = Hashable
Observation = Hashable


def relation_signature_factors_through_observation(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
) -> bool:
    """Whether the set-valued next-observation signature is constant on O-fibers."""
    return quotient_is_relation_observation_safe(
        states,
        relation,
        observation,
        observation,
    )


def descended_relation_observation_transition(
    states: Iterable[State],
    relation: Relation,
    observation: Callable[[State], Observation],
) -> dict[Observation, frozenset[Observation]]:
    """Return ``barSigma`` on observation classes when exact descent is valid."""
    state_values = frozenset(states)
    if not state_values:
        raise ValueError("state set must be nonempty")
    signatures = relation_observation_signature_map(
        state_values,
        relation,
        observation,
    )
    result: dict[Observation, frozenset[Observation]] = {}
    for state in state_values:
        key = observation(state)
        signature = signatures[state]
        if key in result and result[key] != signature:
            raise ValueError(
                "relation observation signature does not descend through observation"
            )
        result[key] = signature
    return result


def composed_signature_from_descended_transition(
    states: Iterable[State],
    first: Relation,
    second: Relation,
    observation: Callable[[State], Observation],
) -> dict[State, frozenset[Observation]]:
    """Compose at the observed-signature level, requiring second-step descent."""
    state_values = frozenset(states)
    if not state_values:
        raise ValueError("state set must be nonempty")
    first_signatures = relation_observation_signature_map(
        state_values,
        first,
        observation,
    )
    second_coarse = descended_relation_observation_transition(
        state_values,
        second,
        observation,
    )
    result = {
        source: frozenset(
            next_observation
            for intermediate_observation in first_signature
            for next_observation in second_coarse[intermediate_observation]
        )
        for source, first_signature in first_signatures.items()
    }
    direct = composed_relation_observation_signature_map(
        state_values,
        first,
        second,
        observation,
    )
    if result != direct:
        raise AssertionError("descended relation composition disagreed with raw composition")
    return result


@dataclass(frozen=True)
class RelationObservableCompositionReport:
    first_observable_deterministic: bool
    second_observable_deterministic: bool
    second_signature_descends: bool
    composed_observable_deterministic: bool
    sufficient_determinism_hypotheses_hold: bool
    hidden_branch_reactivated: bool


def relation_observable_composition_report(
    states: Iterable[State],
    first: Relation,
    second: Relation,
    observation: Callable[[State], Observation],
) -> RelationObservableCompositionReport:
    """Classify one two-step relation/observation composition boundary."""
    state_values = frozenset(states)
    if not state_values:
        raise ValueError("state set must be nonempty")
    first_det = relation_observable_is_deterministic(
        state_values,
        first,
        observation,
    )
    second_det = relation_observable_is_deterministic(
        state_values,
        second,
        observation,
    )
    second_descends = relation_signature_factors_through_observation(
        state_values,
        second,
        observation,
    )
    composed_signatures = composed_relation_observation_signature_map(
        state_values,
        first,
        second,
        observation,
    )
    composed_det = all(len(signature) <= 1 for signature in composed_signatures.values())
    sufficient = first_det and second_det and second_descends
    if sufficient and not composed_det:
        raise AssertionError(
            "observable-deterministic compatible relations lost determinism under composition"
        )
    return RelationObservableCompositionReport(
        first_observable_deterministic=first_det,
        second_observable_deterministic=second_det,
        second_signature_descends=second_descends,
        composed_observable_deterministic=composed_det,
        sufficient_determinism_hypotheses_hold=sufficient,
        hidden_branch_reactivated=first_det and second_det and not composed_det,
    )
