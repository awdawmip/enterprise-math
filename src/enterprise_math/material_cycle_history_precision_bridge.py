"""Precision growth of hidden contact-history classes on a balanced four-cycle.

A cyclic contact graph can have impulse-allocation directions invisible to body
momentum.  This module gives one exact family showing that finer impulse
precision can *increase* the number of materially distinct histories even when
body after-state, contact scores, total delivered impulse and kinetic energy are
all unchanged.

Use four equal-mass bodies with contacts

    0--1, 1--2, 2--3, 0--3

and declared scalar normals chosen so the primitive cycle circulation is

    c = (1,-1,1,-1).

Then

    B c = 0,       sum(c)=0.

Take whole body momentum

    p = (2,-2,2,-2).

Every contact score is ``-4``.  At common impulse denominator ``s``, scale body
momentum by ``s``.  The exact minimum-total nonclosing relation is

    j(t) = (s+t, s-t, s+t, s-t),      -s <= t <= s.

Every member has total impulse numerator ``4s`` and sends the body momentum
numerators to zero, hence also sends all contact-score numerators to zero.
Conversely any nonclosing response satisfies ``sum(j)>=4s``; equality forces all
final contact scores to zero, so ``K(j-s*1)=0``.  The one-dimensional cycle
kernel then gives exactly the family above.

Therefore the minimum relation has exactly

    2s+1

contact-witness histories at denominator ``s`` even though all body-level and
aggregate kinetic observables agree.  Under a true divisibility refinement
``s | s'`` every old witness embeds by numerator scaling, while additional
intermediate cycle-history states appear.  If future material behavior depends
on contact-local cumulative impulse, damage, heat or reservoir state, a
body-only quotient is not future-safe.

This is a finite E001 specialization of standard incidence-cycle nullspace
algebra.  The project-side point is the precision/history boundary, not a new
graph-theory claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_cycle_kernel import (
    contact_impulse_vectors_same_body_update,
    contact_impulse_vectors_same_score_update,
    declared_cycle_circulation,
)
from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)


def balanced_four_cycle_state() -> ContactNetworkMomentum1D:
    """Return the canonical equal-mass closing state used by the theorem."""
    return ContactNetworkMomentum1D(
        masses=(1, 1, 1, 1),
        momenta=(2, -2, 2, -2),
        contacts=(
            ContactChannel1D(0, 1, 1),
            ContactChannel1D(1, 2, -1),
            ContactChannel1D(2, 3, 1),
            ContactChannel1D(0, 3, 1),
        ),
    )


def balanced_four_cycle_circulation() -> tuple[int, ...]:
    state = balanced_four_cycle_state()
    result = declared_cycle_circulation(state, (0, 1, 2, 3))
    if result != (1, -1, 1, -1):
        raise AssertionError("balanced four-cycle orientation lost primitive circulation")
    if sum(result) != 0:
        raise AssertionError("balanced cycle circulation lost zero total-impulse direction")
    return result


def balanced_four_cycle_minimum_relation(
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Return the exact ``2s+1`` minimum-total contact-history fiber."""
    if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("denominator must be a positive integer")
    s = denominator
    relation = tuple(
        (s + shift, s - shift, s + shift, s - shift)
        for shift in range(-s, s + 1)
    )
    if len(relation) != 2 * s + 1:
        raise AssertionError("balanced cycle history fiber lost exact cardinality")
    if any(any(value < 0 for value in vector) for vector in relation):
        raise AssertionError("balanced cycle minimum relation produced negative impulse")
    if any(sum(vector) != 4 * s for vector in relation):
        raise AssertionError("balanced cycle minimum relation lost total impulse")
    return relation


@dataclass(frozen=True)
class BalancedCycleHistoryPrecisionReport:
    denominator: int
    minimum_total_impulse_numerator: int
    history_class_count: int
    impulse_relation: tuple[tuple[int, ...], ...]
    common_body_after_numerators: tuple[int, ...]
    common_final_score_numerators: tuple[int, ...]
    common_kinetic_after_numerator: int


def balanced_four_cycle_history_precision_report(
    denominator: int,
) -> BalancedCycleHistoryPrecisionReport:
    """Verify exact minimum relation and its body-level invisibility at precision s."""
    if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("denominator must be a positive integer")
    s = denominator
    state = balanced_four_cycle_state()
    circulation = balanced_four_cycle_circulation()
    if contact_relative_scores(state) != (-4, -4, -4, -4):
        raise AssertionError("balanced four-cycle lost uniform closing scores")
    gram = contact_coupling_gram(state)
    relation = balanced_four_cycle_minimum_relation(s)
    scaled_state = ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(s * value for value in state.momenta),
        contacts=state.contacts,
    )
    reference = relation[s]  # shift 0
    reference_step = apply_contact_impulse_vector(scaled_state, reference)
    if reference_step.after.momenta != (0, 0, 0, 0):
        raise AssertionError("balanced cycle reference failed exact body cancellation")
    if reference_step.relative_scores_after != (0, 0, 0, 0):
        raise AssertionError("balanced cycle reference failed zero-score closure")

    kinetic_after = sum(value * value for value in reference_step.after.momenta)
    for vector in relation:
        step = apply_contact_impulse_vector(scaled_state, vector)
        if step.after.momenta != reference_step.after.momenta:
            raise AssertionError("cycle-kernel history changed body after-state")
        if step.relative_scores_after != reference_step.relative_scores_after:
            raise AssertionError("cycle-kernel history changed contact-score after-state")
        if not contact_impulse_vectors_same_body_update(scaled_state, reference, vector):
            raise AssertionError("balanced cycle relation escaped incidence kernel")
        if not contact_impulse_vectors_same_score_update(scaled_state, reference, vector):
            raise AssertionError("balanced cycle relation escaped coupling kernel")
        difference = tuple(a - b for a, b in zip(vector, reference))
        # Every difference is ``shift*c`` and therefore preserves total impulse.
        nonzero = [
            difference[index] // circulation[index]
            for index in range(len(circulation))
            if circulation[index] != 0
        ]
        if len(set(nonzero)) != 1:
            raise AssertionError("balanced cycle witness left primitive kernel line")
        if sum(vector) != sum(reference):
            raise AssertionError("balanced cycle witness changed total impulse")

    # Minimum-total proof: if all final scores are nonnegative, summing them gives
    # ``4*sum(j)-16s >= 0`` for this exact Gram/closing state.
    row_sums = tuple(sum(row) for row in gram)
    if row_sums != (4, 4, 4, 4):
        raise AssertionError("balanced four-cycle Gram lost uniform row sum")

    return BalancedCycleHistoryPrecisionReport(
        denominator=s,
        minimum_total_impulse_numerator=4 * s,
        history_class_count=2 * s + 1,
        impulse_relation=relation,
        common_body_after_numerators=reference_step.after.momenta,
        common_final_score_numerators=reference_step.relative_scores_after,
        common_kinetic_after_numerator=kinetic_after,
    )


def new_hidden_history_classes_under_refinement(
    coarse_denominator: int,
    fine_denominator: int,
) -> int:
    """Count new cycle-history states when ``coarse | fine`` in this exact family."""
    for name, value in (
        ("coarse_denominator", coarse_denominator),
        ("fine_denominator", fine_denominator),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if fine_denominator % coarse_denominator != 0:
        raise ValueError("fine denominator must be a divisibility refinement")
    coarse_count = 2 * coarse_denominator + 1
    fine_count = 2 * fine_denominator + 1
    return fine_count - coarse_count
