"""Guard-induced noncommutativity for E001 contact-network unit impulses.

The contact-network owner gives the unguarded integer update

    p' = p + B j,
    r' = r + K j,
    K = B^T D B.

For two unit contact impulses ``e_i`` and ``e_j``, ordinary addition implies
that the *unguarded* update operators commute exactly.  This module keeps that
algebra and adds one explicit partial-action guard:

    G_i is defined only when r_i < 0.

The distinction matters.  For distinct contacts i,j,

    G_j after G_i is defined
        iff r_i < 0 and r_j + K_ji < 0,

while

    G_i after G_j is defined
        iff r_j < 0 and r_i + K_ij < 0.

Because K is symmetric, the same cross coupling controls both directions, but
the two current scores can sit at different distances from the guard boundary.
Thus commuting total additions can become noncommuting *partial* operations.

The sign boundary is exact:

* if ``K_ij <= 0`` and both contacts are initially closing, updating either
  contact cannot disable the other.  Both guarded orders are legal and finish
  at the same body momentum state;
* if ``K_ij > 0``, updating i disables an initially closing j exactly in the
  algebraic competition band

      -K_ji <= r_j < 0.

For the simple contact Gram, two contacts that share body v have

    K_ij = D_v * B_vi * B_vj.

So opposite incidence signs at the shared body give negative coupling and
reinforce the other closing guard, while equal incidence signs give positive
coupling and a competition band of algebraic width ``D_v``.  The Z-matrix
owner already characterizes exactly which contact topologies have no positive
off-diagonal coupling; this module consumes that owner rather than duplicating
its topology theorem.

No generic partial-map, rewriting, confluence, M-matrix or graph-orientation
novelty is claimed.  The E001 result is the exact finite contact specialization
and its world-law consequence: algebraic commutativity of impulse addition does
not by itself imply causal commutativity once legal-action domains are part of
the state semantics.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkImpulseStep1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_z_contact_least_action_1d import contact_coupling_is_z_matrix


def _validate_contact_index(
    state: ContactNetworkMomentum1D,
    contact_index: int,
) -> None:
    if (
        isinstance(contact_index, bool)
        or not isinstance(contact_index, int)
        or not 0 <= contact_index < len(state.contacts)
    ):
        raise ValueError("contact_index is outside the declared contact set")


def _unit_impulse_vector(
    contact_count: int,
    contact_index: int,
) -> tuple[int, ...]:
    return tuple(
        1 if index == contact_index else 0
        for index in range(contact_count)
    )


def contact_guarded_unit_is_legal(
    state: ContactNetworkMomentum1D,
    contact_index: int,
) -> bool:
    """Return whether the declared contact is currently closing."""
    _validate_contact_index(state, contact_index)
    return contact_relative_scores(state)[contact_index] < 0


def apply_guarded_contact_unit(
    state: ContactNetworkMomentum1D,
    contact_index: int,
) -> ContactNetworkImpulseStep1D:
    """Apply one delivered unit only to a currently closing contact."""
    _validate_contact_index(state, contact_index)
    if not contact_guarded_unit_is_legal(state, contact_index):
        raise ValueError("guarded contact unit is legal only on a closing contact")
    return apply_contact_impulse_vector(
        state,
        _unit_impulse_vector(len(state.contacts), contact_index),
    )


def contact_cross_guard_delta(
    state: ContactNetworkMomentum1D,
    actor_contact: int,
    target_contact: int,
) -> int:
    """Return the exact score increment delivered from actor to target guard."""
    _validate_contact_index(state, actor_contact)
    _validate_contact_index(state, target_contact)
    if actor_contact == target_contact:
        raise ValueError("cross-guard delta requires distinct contacts")
    return contact_coupling_gram(state)[target_contact][actor_contact]


def contact_actor_disables_closing_target(
    state: ContactNetworkMomentum1D,
    actor_contact: int,
    target_contact: int,
) -> bool:
    """Return whether one legal actor unit closes the target's legal domain."""
    _validate_contact_index(state, actor_contact)
    _validate_contact_index(state, target_contact)
    if actor_contact == target_contact:
        raise ValueError("actor and target must be distinct contacts")
    scores = contact_relative_scores(state)
    if scores[actor_contact] >= 0 or scores[target_contact] >= 0:
        return False
    delta = contact_cross_guard_delta(
        state, actor_contact, target_contact
    )
    after_target = scores[target_contact] + delta
    disables = after_target >= 0
    if delta <= 0 and disables:
        raise AssertionError("non-positive cross coupling unexpectedly disabled closing guard")
    if delta > 0:
        band = -delta <= scores[target_contact] < 0
        if disables != band:
            raise AssertionError("positive cross coupling lost exact competition-band criterion")
    return disables


@dataclass(frozen=True)
class GuardedContactPairReport:
    left_contact: int
    right_contact: int
    cross_coupling: int
    scores_before: tuple[int, ...]
    left_initially_legal: bool
    right_initially_legal: bool
    left_then_right_defined: bool
    right_then_left_defined: bool
    unguarded_final_momenta: tuple[int, ...]
    left_then_right_final_momenta: tuple[int, ...] | None
    right_then_left_final_momenta: tuple[int, ...] | None

    @property
    def unguarded_actions_commute(self) -> bool:
        return True

    @property
    def both_guarded_orders_defined(self) -> bool:
        return self.left_then_right_defined and self.right_then_left_defined

    @property
    def guarded_pair_commutes_when_defined(self) -> bool:
        if not self.both_guarded_orders_defined:
            return False
        return (
            self.left_then_right_final_momenta
            == self.right_then_left_final_momenta
            == self.unguarded_final_momenta
        )

    @property
    def guard_domain_is_order_sensitive(self) -> bool:
        return self.left_then_right_defined != self.right_then_left_defined


def guarded_contact_pair_report(
    state: ContactNetworkMomentum1D,
    left_contact: int,
    right_contact: int,
) -> GuardedContactPairReport:
    """Compare algebraic commutation with guarded partial-operation domains."""
    _validate_contact_index(state, left_contact)
    _validate_contact_index(state, right_contact)
    if left_contact == right_contact:
        raise ValueError("pair report requires distinct contacts")

    count = len(state.contacts)
    left_unit = _unit_impulse_vector(count, left_contact)
    right_unit = _unit_impulse_vector(count, right_contact)

    left_unguarded = apply_contact_impulse_vector(state, left_unit).after
    left_right_unguarded = apply_contact_impulse_vector(
        left_unguarded, right_unit
    ).after
    right_unguarded = apply_contact_impulse_vector(state, right_unit).after
    right_left_unguarded = apply_contact_impulse_vector(
        right_unguarded, left_unit
    ).after
    if left_right_unguarded != right_left_unguarded:
        raise AssertionError("contact unit additions stopped commuting algebraically")

    scores = contact_relative_scores(state)
    left_legal = scores[left_contact] < 0
    right_legal = scores[right_contact] < 0

    left_then_right_defined = False
    right_then_left_defined = False
    left_then_right_final = None
    right_then_left_final = None

    if left_legal:
        after_left = apply_guarded_contact_unit(state, left_contact).after
        if contact_guarded_unit_is_legal(after_left, right_contact):
            left_then_right_defined = True
            left_then_right_final = apply_guarded_contact_unit(
                after_left, right_contact
            ).after.momenta

    if right_legal:
        after_right = apply_guarded_contact_unit(state, right_contact).after
        if contact_guarded_unit_is_legal(after_right, left_contact):
            right_then_left_defined = True
            right_then_left_final = apply_guarded_contact_unit(
                after_right, left_contact
            ).after.momenta

    gram = contact_coupling_gram(state)
    cross = gram[left_contact][right_contact]
    if cross != gram[right_contact][left_contact]:
        raise AssertionError("contact Gram lost symmetry")

    if cross <= 0 and left_legal and right_legal:
        if not left_then_right_defined or not right_then_left_defined:
            raise AssertionError("Z cross coupling lost no-cross-disable guarantee")
        if left_then_right_final != right_then_left_final:
            raise AssertionError("defined Z guarded unit pair lost algebraic final-state equality")

    return GuardedContactPairReport(
        left_contact=left_contact,
        right_contact=right_contact,
        cross_coupling=cross,
        scores_before=scores,
        left_initially_legal=left_legal,
        right_initially_legal=right_legal,
        left_then_right_defined=left_then_right_defined,
        right_then_left_defined=right_then_left_defined,
        unguarded_final_momenta=left_right_unguarded.momenta,
        left_then_right_final_momenta=left_then_right_final,
        right_then_left_final_momenta=right_then_left_final,
    )


def contact_network_has_no_cross_disable_guarantee(
    state: ContactNetworkMomentum1D,
) -> bool:
    """Reuse the Z-owner sign certificate as the global no-cross-disable guarantee."""
    return contact_coupling_is_z_matrix(state)
