"""Causal reachability of branching-star responses under a local unit action language.

The static star-response owner ``material_star_response_spectrum`` classifies
non-negative impulse vectors whose final contact scores are feasible.  This
module adds one explicitly declared causal operation language:

    UPDATE(i): add one impulse quantum to contact i,

and ``UPDATE(i)`` is legal only while contact ``i`` is currently closing.
For a star with common closing magnitude ``q``, current impulse vector ``j``
and total ``S=sum(j)``, the score is

    score_i = -q + S + j_i,

so the local action is legal exactly when ``S+j_i<q``.

This immediately separates static feasibility from causal reachability.  If a
forward legal update produced a current vector ``u`` of total ``U``, then the
last update on contact ``i`` can be reversed exactly when

    U + u_i <= q + 1.

During reverse peeling, removing one unit decreases ``U`` by one, so the
removal threshold ``q+1-U`` rises by one.  If any positive coordinate is
removable, a smallest positive coordinate is removable; once chosen, repeatedly
removing from it only makes that coordinate smaller while the threshold rises.
Therefore a terminal vector with sorted coordinates

    c_1 <= ... <= c_k

and total ``S`` is causally reachable from zero iff

    c_h <= q + 1 - S + sum_{ell<h} c_ell

for every ``h``.  This is a complete constructive criterion: greedy reverse
peeling of the smallest positive coordinate recovers a legal forward word.
The inequality is a star specialization of standard complete-sequence / greedy
peeling ideas, not a generic novelty claim.

Two exact boundaries follow.

1. Static minimum response can overstate causal choice.
   In the q=2, k=2 star the static minimum relation is

       (2,0), (1,1), (0,2),

   but only ``(1,1)`` is locally reachable.  More generally, using the upstream
   Euclidean baseline ``b=floor(q/(k+1))``, the *whole* static minimum relation
   is locally reachable iff ``q=1`` or ``b>=1`` (equivalently ``q=1`` or
   ``q>=k+1``).  When ``2<=q<=k``, the concentrated minimum ``(q,0,...,0)`` is
   feasible and minimum-total but fails the reverse-peeling criterion.

2. Local schedule can change total delivered impulse.
   The smallest such star is k=2, q=3.  A least-used legal scheduler executes
   contacts ``0,1`` and stops at the global minimum ``(1,1)`` of total two.
   A lowest-index legal scheduler executes ``0,0,1`` and stops at ``(2,1)`` of
   total three.  Every individual action was legal when taken.  Thus operation
   order/selection is a world law once branching destroys the Z-matrix
   least-action property; it is not rounding noise and not merely witness
   relabeling.

This module does not assert that either local scheduler is the physical law.
It exposes the action-language boundary so a future world must declare a
selection/simultaneity rule rather than silently equating a static optimizer
with causal dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .material_star_response_spectrum import (
    star_minimum_relation_parameters,
    star_minimum_total_impulse,
    star_score_vector,
)

StarLocalPolicy = Literal["LOWEST_INDEX", "LEAST_USED"]


def _validate_impulse_vector(values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    result = tuple(values)
    if len(result) < 2:
        raise ValueError("star response requires at least two contacts")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in result
    ):
        raise ValueError("impulse entries must be non-negative integers")
    return result


def _validate_closing_quantum(closing_quantum: int) -> None:
    if (
        isinstance(closing_quantum, bool)
        or not isinstance(closing_quantum, int)
        or closing_quantum <= 0
    ):
        raise ValueError("closing_quantum must be a positive integer")


def star_local_legal_contacts(
    impulse_vector: tuple[int, ...] | list[int],
    closing_quantum: int,
) -> tuple[int, ...]:
    """Return exactly the contacts whose current score is still negative."""
    values = _validate_impulse_vector(impulse_vector)
    _validate_closing_quantum(closing_quantum)
    scores = star_score_vector(values, closing_quantum)
    return tuple(index for index, score in enumerate(scores) if score < 0)


def star_apply_local_unit_update(
    impulse_vector: tuple[int, ...] | list[int],
    closing_quantum: int,
    contact_index: int,
) -> tuple[int, ...]:
    """Apply one unit to a currently closing contact, rejecting illegal actions."""
    values = _validate_impulse_vector(impulse_vector)
    _validate_closing_quantum(closing_quantum)
    if (
        isinstance(contact_index, bool)
        or not isinstance(contact_index, int)
        or not 0 <= contact_index < len(values)
    ):
        raise ValueError("contact_index is outside the star")
    if contact_index not in star_local_legal_contacts(values, closing_quantum):
        raise ValueError("local unit update is legal only on a closing contact")
    updated = list(values)
    updated[contact_index] += 1
    return tuple(updated)


def star_replay_local_contact_word(
    leaf_count: int,
    closing_quantum: int,
    contact_word: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Replay one explicit legal contact-action word from the zero response."""
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")
    _validate_closing_quantum(closing_quantum)
    state = (0,) * leaf_count
    for contact_index in contact_word:
        state = star_apply_local_unit_update(
            state, closing_quantum, contact_index
        )
    return state


def star_terminal_is_causally_reachable(
    impulse_vector: tuple[int, ...] | list[int],
    closing_quantum: int,
) -> bool:
    """Return the exact sorted-prefix criterion for local-unit reachability."""
    values = _validate_impulse_vector(impulse_vector)
    _validate_closing_quantum(closing_quantum)
    scores = star_score_vector(values, closing_quantum)
    if any(score < 0 for score in scores):
        return False
    total = sum(values)
    if total > closing_quantum:
        return False
    threshold = closing_quantum + 1 - total
    prefix = 0
    for count in sorted(values):
        if count > threshold + prefix:
            return False
        prefix += count
    return True


def star_reverse_peeling_word(
    impulse_vector: tuple[int, ...] | list[int],
    closing_quantum: int,
) -> tuple[int, ...] | None:
    """Return a constructive reverse word, or ``None`` when unreachable.

    Reversing the returned tuple gives a legal forward word from zero to the
    supplied terminal vector.
    """
    values = _validate_impulse_vector(impulse_vector)
    _validate_closing_quantum(closing_quantum)
    if not star_terminal_is_causally_reachable(values, closing_quantum):
        return None

    current = list(values)
    removals: list[int] = []
    while sum(current):
        total = sum(current)
        positive = [index for index, value in enumerate(current) if value > 0]
        chosen = min(positive, key=lambda index: (current[index], index))
        if total + current[chosen] > closing_quantum + 1:
            raise AssertionError("sorted-prefix certificate failed greedy reverse peeling")
        current[chosen] -= 1
        removals.append(chosen)

    forward = tuple(reversed(removals))
    if star_replay_local_contact_word(
        len(values), closing_quantum, forward
    ) != values:
        raise AssertionError("reverse peeling failed to reconstruct the terminal response")
    return tuple(removals)


def star_minimum_relation_is_fully_causally_reachable(
    leaf_count: int,
    closing_quantum: int,
) -> bool:
    """Classify when every static minimum response is locally reachable."""
    total, baseline, _ = star_minimum_relation_parameters(
        leaf_count, closing_quantum
    )
    if total != star_minimum_total_impulse(leaf_count, closing_quantum):
        raise AssertionError("star minimum owner disagrees with its parameterization")
    return closing_quantum == 1 or baseline >= 1


def star_concentrated_unreachable_minimum_witness(
    leaf_count: int,
    closing_quantum: int,
) -> tuple[int, ...] | None:
    """Return the canonical concentrated static-minimum witness when it is unreachable."""
    if star_minimum_relation_is_fully_causally_reachable(
        leaf_count, closing_quantum
    ):
        return None
    witness = (closing_quantum,) + (0,) * (leaf_count - 1)
    if sum(witness) != star_minimum_total_impulse(leaf_count, closing_quantum):
        raise AssertionError("concentrated witness stopped being minimum-total")
    if any(score < 0 for score in star_score_vector(witness, closing_quantum)):
        raise AssertionError("concentrated minimum witness stopped being statically feasible")
    if star_terminal_is_causally_reachable(witness, closing_quantum):
        raise AssertionError("concentrated minimum witness unexpectedly became locally reachable")
    return witness


@dataclass(frozen=True)
class StarLocalScheduleReport:
    leaf_count: int
    closing_quantum: int
    policy: StarLocalPolicy
    contact_word: tuple[int, ...]
    terminal_impulse: tuple[int, ...]
    terminal_scores: tuple[int, ...]
    global_minimum_total: int

    @property
    def delivered_total(self) -> int:
        return sum(self.terminal_impulse)

    @property
    def overdelivery(self) -> int:
        return self.delivered_total - self.global_minimum_total


def star_run_local_unit_policy(
    leaf_count: int,
    closing_quantum: int,
    policy: StarLocalPolicy,
) -> StarLocalScheduleReport:
    """Run one explicit local scheduler until no contact remains closing."""
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")
    _validate_closing_quantum(closing_quantum)
    if policy not in ("LOWEST_INDEX", "LEAST_USED"):
        raise ValueError("unknown star local scheduling policy")

    state = (0,) * leaf_count
    word: list[int] = []
    while True:
        legal = star_local_legal_contacts(state, closing_quantum)
        if not legal:
            break
        if policy == "LOWEST_INDEX":
            chosen = min(legal)
        else:
            chosen = min(legal, key=lambda index: (state[index], index))
        state = star_apply_local_unit_update(
            state, closing_quantum, chosen
        )
        word.append(chosen)
        if len(word) > closing_quantum:
            raise AssertionError("local star schedule exceeded exact q-step bound")

    scores = star_score_vector(state, closing_quantum)
    if any(score < 0 for score in scores):
        raise AssertionError("local scheduler stopped before terminal feasibility")
    if not star_terminal_is_causally_reachable(state, closing_quantum):
        raise AssertionError("executed local scheduler produced an unreachable terminal")

    return StarLocalScheduleReport(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        policy=policy,
        contact_word=tuple(word),
        terminal_impulse=state,
        terminal_scores=scores,
        global_minimum_total=star_minimum_total_impulse(
            leaf_count, closing_quantum
        ),
    )
