"""Exact global passivity identity for refined multi-contact impulse response.

After ``material_refined_contact_momentum_bridge`` lifts all body momentum and
all delivered contact impulses to one common denominator, the contact-network
kinetic metric closes exactly.

Let

    r = B^T D P,
    K = B^T D B,
    P' = P + B j,
    r' = r + K j,

where ``P`` and ``j`` are common-denominator numerators.  For

    E(P) = sum_i D_i P_i^2,

the exact change is

    Delta E = E(P')-E(P)
            = 2 j^T r + j^T K j
            = j^T (r+r').

Thus a response can make every contact nonclosing (``r'>=0``) and still inject
kinetic energy if it over-shoots too far.  Conversely, one local contact may
overshoot its own initial closing magnitude while dissipation on other contacts
keeps the global quadratic form non-positive.

A simple sufficient, not necessary, contactwise certificate is

    0 <= r'_e <= -r_e

for every contact receiving positive impulse, with all initial active scores
non-positive.  Then every term ``j_e(r_e+r'_e)`` is non-positive and the whole
network is passive.

The quadratic identity is standard contact/Gram mechanics.  This E001 bridge
exists to keep finite denominator precision, nonclosing feasibility and global
passivity as distinct checks rather than conflating them.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
)
from .material_refined_contact_momentum_bridge import (
    RefinedContactMomentumBridgeReport,
    apply_refined_contact_impulses_to_lifted_momentum,
)


@dataclass(frozen=True)
class RefinedContactPassivityReport:
    bridge: RefinedContactMomentumBridgeReport
    common_impulse_numerators: tuple[int, ...]
    kinetic_numerator_before: int
    kinetic_numerator_after: int
    kinetic_change_numerator: int
    linear_plus_quadratic_change_numerator: int
    score_pairing_change_numerator: int
    all_contacts_nonclosing: bool
    globally_passive: bool
    contactwise_passive_envelope: bool


def refined_contact_passivity_report(
    state: ContactNetworkMomentum1D,
    momentum_denominator: int,
    momentum_detail_numerators: tuple[int, ...] | list[int],
    impulse_numerators: tuple[int, ...] | list[int],
    impulse_denominators: tuple[int, ...] | list[int],
) -> RefinedContactPassivityReport:
    """Return the exact common-denominator kinetic/passivity diagnostics."""
    impulses = tuple(impulse_numerators)
    bridge = apply_refined_contact_impulses_to_lifted_momentum(
        state,
        momentum_denominator,
        momentum_detail_numerators,
        impulses,
        impulse_denominators,
    )
    common_impulses = tuple(
        value * scale
        for value, scale in zip(impulses, bridge.contact_scale_factors)
    )
    weights = state.body_scale_weights
    before_energy = sum(
        weight * value * value
        for weight, value in zip(weights, bridge.body_numerators_before)
    )
    after_energy = sum(
        weight * value * value
        for weight, value in zip(weights, bridge.body_numerators_after)
    )
    change = after_energy - before_energy
    gram = contact_coupling_gram(state)
    r_before = bridge.contact_score_numerators_before
    r_after = bridge.contact_score_numerators_after
    linear_quadratic = (
        2 * sum(j * r for j, r in zip(common_impulses, r_before))
        + sum(
            common_impulses[row]
            * gram[row][col]
            * common_impulses[col]
            for row in range(len(common_impulses))
            for col in range(len(common_impulses))
        )
    )
    score_pairing = sum(
        j * (left + right)
        for j, left, right in zip(common_impulses, r_before, r_after)
    )
    if change != linear_quadratic or change != score_pairing:
        raise AssertionError("refined contact kinetic identity failed")

    all_nonclosing = all(value >= 0 for value in r_after)
    passive = change <= 0
    initial_active_nonpositive = all(value <= 0 for value in r_before)
    envelope = initial_active_nonpositive and all(
        j == 0 or (0 <= right <= -left)
        for j, left, right in zip(common_impulses, r_before, r_after)
    )
    if envelope and not passive:
        raise AssertionError("contactwise passive envelope failed global passivity")

    return RefinedContactPassivityReport(
        bridge=bridge,
        common_impulse_numerators=common_impulses,
        kinetic_numerator_before=before_energy,
        kinetic_numerator_after=after_energy,
        kinetic_change_numerator=change,
        linear_plus_quadratic_change_numerator=linear_quadratic,
        score_pairing_change_numerator=score_pairing,
        all_contacts_nonclosing=all_nonclosing,
        globally_passive=passive,
        contactwise_passive_envelope=envelope,
    )
