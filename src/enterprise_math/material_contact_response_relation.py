"""Finite minimum-total response relation for a general declared contact network.

The Z-path owner proves that some contact topologies have one unique
componentwise-least impulse.  Branching networks need not: several incomparable
minimum responses may coexist.  This module does not force an ID-based selector.
Instead it exposes a finite relation-valued response under one explicit total
impulse budget.

For ``m`` declared contacts and a non-negative integer impulse vector ``j``, let
``|j|_1=sum(j)``.  Given finite budget ``B``, enumerate total impulse levels

    S = 0,1,...,B

and every weak composition of ``S`` into ``m`` contact coordinates.  The first
level containing any feasible response is exact: every globally smaller total
has already been exhausted.  Therefore that whole first feasible layer is the
*global* minimum-total response relation, even though larger total responses
were never searched.

If no feasible vector appears by budget ``B``, the result is explicitly
``IMPULSE_UNDERRESOLVED``.  No infeasibility claim beyond the declared budget is
made and no response is fabricated.

All distinct vectors in a fixed minimum-total layer are automatically
componentwise incomparable: if ``u<=v`` and ``sum(u)=sum(v)``, then ``u=v``.
Thus a multivalued minimum response is a genuine finite antichain, not duplicate
encoding noise.

This is an E001 finite-search/reference operator.  Weak compositions, discrete
optimization and Pareto/antichain terminology are standard; no generic integer
programming novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_relative_scores,
)

MINIMUM_TOTAL_RESOLVED = "MINIMUM_TOTAL_RESOLVED"
IMPULSE_UNDERRESOLVED = "IMPULSE_UNDERRESOLVED"


def _require_budget(maximum_total_impulse: int) -> None:
    if (
        isinstance(maximum_total_impulse, bool)
        or not isinstance(maximum_total_impulse, int)
        or maximum_total_impulse < 0
    ):
        raise ValueError("maximum_total_impulse must be a non-negative integer")


def weak_compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    """Return all ordered non-negative ``parts``-tuples summing to ``total``."""
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if isinstance(parts, bool) or not isinstance(parts, int) or parts <= 0:
        raise ValueError("parts must be a positive integer")
    if parts == 1:
        return ((total,),)
    result: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            result.append((first,) + tail)
    return tuple(result)


def contact_impulse_candidate_is_feasible(
    state: ContactNetworkMomentum1D,
    impulse_vector: tuple[int, ...] | list[int],
) -> bool:
    """Whether one non-negative integer impulse makes every contact nonclosing."""
    impulses = tuple(impulse_vector)
    if len(impulses) != len(state.contacts):
        raise ValueError("impulse_vector must match the declared contact count")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in impulses
    ):
        raise ValueError("impulse_vector entries must be non-negative integers")
    return all(
        score >= 0
        for score in apply_contact_impulse_vector(
            state, impulses
        ).relative_scores_after
    )


@dataclass(frozen=True)
class ContactMinimumResponseRelation1D:
    status: str
    before: ContactNetworkMomentum1D
    maximum_total_impulse: int
    minimum_total_impulse: int | None
    response_relation: tuple[tuple[int, ...], ...]
    final_score_vectors: tuple[tuple[int, ...], ...]

    @property
    def resolved(self) -> bool:
        return self.status == MINIMUM_TOTAL_RESOLVED

    @property
    def single_valued(self) -> bool:
        return self.resolved and len(self.response_relation) == 1


def bounded_minimum_total_response_relation(
    state: ContactNetworkMomentum1D,
    maximum_total_impulse: int,
) -> ContactMinimumResponseRelation1D:
    """Search total-impulse layers exactly up to one explicit finite budget."""
    _require_budget(maximum_total_impulse)
    contact_count = len(state.contacts)
    if contact_count < 1:
        raise ValueError("at least one declared contact is required")

    for total in range(maximum_total_impulse + 1):
        feasible: list[tuple[int, ...]] = []
        score_vectors: list[tuple[int, ...]] = []
        for candidate in weak_compositions(total, contact_count):
            step = apply_contact_impulse_vector(state, candidate)
            if any(score < 0 for score in step.relative_scores_after):
                continue
            feasible.append(candidate)
            score_vectors.append(step.relative_scores_after)
        if feasible:
            relation = tuple(feasible)
            if any(sum(vector) != total for vector in relation):
                raise AssertionError("minimum response relation left its total layer")
            for left_index, left in enumerate(relation):
                for right in relation[left_index + 1 :]:
                    if all(a <= b for a, b in zip(left, right)) or all(
                        b <= a for a, b in zip(left, right)
                    ):
                        raise AssertionError("distinct minimum-total responses became comparable")
            return ContactMinimumResponseRelation1D(
                status=MINIMUM_TOTAL_RESOLVED,
                before=state,
                maximum_total_impulse=maximum_total_impulse,
                minimum_total_impulse=total,
                response_relation=relation,
                final_score_vectors=tuple(score_vectors),
            )

    return ContactMinimumResponseRelation1D(
        status=IMPULSE_UNDERRESOLVED,
        before=state,
        maximum_total_impulse=maximum_total_impulse,
        minimum_total_impulse=None,
        response_relation=(),
        final_score_vectors=(),
    )


def minimum_relation_is_permutation_closed(
    relation: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
    permutations: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
) -> bool:
    """Check closure under one declared set of contact-coordinate permutations."""
    vectors = tuple(relation)
    if not vectors:
        raise ValueError("relation must be nonempty")
    width = len(vectors[0])
    if any(len(vector) != width for vector in vectors):
        raise ValueError("relation vectors must have common width")
    vector_set = set(vectors)
    for permutation in permutations:
        permutation = tuple(permutation)
        if len(permutation) != width or set(permutation) != set(range(width)):
            raise ValueError("permutation must reorder every response coordinate")
        for vector in vectors:
            if tuple(vector[index] for index in permutation) not in vector_set:
                return False
    return True
