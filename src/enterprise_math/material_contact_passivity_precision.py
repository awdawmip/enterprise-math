"""Exact impulse-denominator threshold for passive minimum single-contact response.

The contact-network owner supplies, for one active contact, a closing score
``r=-q<0`` and positive self-coupling ``K``.  At declared impulse denominator
``s`` the exact scaled nonclosing constraint is

    -q*s + K*a >= 0,

so the minimum non-negative impulse numerator is

    a_s = ceil(q*s/K).

Using the owner kinetic metric ``E_num=sum_i D_i P_i^2`` on body momentum
numerators ``P_i=s*p_i``, the exact change under the contact impulse is

    Delta E_num = 2*a_s*(-q*s) + K*a_s^2
                = a_s*(K*a_s - 2*q*s).

Hence the minimum nonclosing response is passive exactly when

    K*a_s <= 2*q*s.

For ``q,s>0`` this is equivalent to the much simpler exact lattice threshold

    2*q*s >= K.

Therefore the least impulse denominator at which the minimum nonclosing response
cannot inject kinetic energy is

    s_passive = ceil(K/(2*q)).

Below that threshold ``q*s<K/2``, so ``a_s=1`` and the only representable
nonclosing impulse necessarily over-shoots enough to increase kinetic energy.
This is a finite precision artifact of the delivered-impulse lattice, not a
claim that the material is physically active.

The identity and threshold are elementary quadratic/contact arithmetic.  This
module is an E001 bridge specialization joining response precision to the
contact-network kinetic metric; no generic mechanics novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class MinimumSingleContactPassivityReport:
    closing_score: int
    self_coupling: int
    denominator: int
    minimum_impulse_numerator: int
    final_score_numerator: int
    kinetic_energy_change_numerator: int
    passive: bool
    minimum_passive_denominator: int

    @property
    def active_precision_artifact(self) -> bool:
        return self.kinetic_energy_change_numerator > 0


def minimum_single_contact_passivity_report(
    closing_score: int,
    self_coupling: int,
    denominator: int,
) -> MinimumSingleContactPassivityReport:
    """Classify the exact minimum nonclosing numerator at one impulse precision."""
    _positive("closing_score", closing_score)
    _positive("self_coupling", self_coupling)
    _positive("denominator", denominator)
    q = closing_score
    k = self_coupling
    s = denominator
    impulse = _ceil_div(q * s, k)
    final_score = -q * s + k * impulse
    if not 0 <= final_score < k:
        raise AssertionError("minimum nonclosing impulse lost its exact overshoot range")
    energy_change = impulse * (k * impulse - 2 * q * s)
    threshold = _ceil_div(k, 2 * q)
    passive = energy_change <= 0
    if passive != (s >= threshold):
        raise AssertionError("single-contact passivity disagrees with exact denominator threshold")
    return MinimumSingleContactPassivityReport(
        closing_score=q,
        self_coupling=k,
        denominator=s,
        minimum_impulse_numerator=impulse,
        final_score_numerator=final_score,
        kinetic_energy_change_numerator=energy_change,
        passive=passive,
        minimum_passive_denominator=threshold,
    )


def minimum_single_contact_passivity_from_network(
    state: ContactNetworkMomentum1D,
    denominator: int,
) -> MinimumSingleContactPassivityReport:
    """Specialize one declared closing contact-network state to the exact report."""
    if len(state.contacts) != 1:
        raise ValueError("single-contact passivity report requires exactly one contact")
    score = contact_relative_scores(state)[0]
    if score >= 0:
        raise ValueError("declared contact must be strictly closing")
    coupling = contact_coupling_gram(state)[0][0]
    return minimum_single_contact_passivity_report(
        closing_score=-score,
        self_coupling=coupling,
        denominator=denominator,
    )
