"""Four-phase precision diagram for one capped nonclosing contact response.

For one closing contact with score ``-q<0``, self-coupling ``K>0``, impulse
denominator ``s`` and material impulse-capacity numerator ``u_s``, the minimum
nonclosing response numerator is

    a_s = ceil(q*s/K).

This exposes four distinct finite states that should not be conflated:

* CAPACITY_DEFICIT: ``u_s<a_s``; the declared material cannot realize a
  nonclosing response on this tick;
* ACTIVE_ARTIFACT: capacity is sufficient but the minimum representable
  nonclosing response injects kinetic energy, equivalently ``2*q*s<K``;
* PASSIVE_OVERSHOOT: capacity is sufficient and the response is passive, but
  final contact score is strictly positive because ``K`` does not divide
  ``q*s``;
* EXACT_PLASTIC: capacity is sufficient and ``K | q*s``, so the final relative
  score is exactly zero.

Passivity and exact plastic closure have different precision geometry:

    s_passive = ceil(K/(2q))

is a scalar eventual threshold: every larger integer denominator is passive.
By contrast exact plastic closure occurs precisely on the divisibility sublattice

    s in (K/gcd(K,q)) * N_{>0}.

Thus refinement can permanently eliminate false energy injection while exact
zero-score closure continues to alternate with passive overshoot between its
multiples.

This is an E001 specialization of the single-contact passivity identity and
ordinary divisibility arithmetic; no generic impact-mechanics novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_contact_passivity_precision import (
    minimum_single_contact_passivity_report,
)

CAPACITY_DEFICIT = "CAPACITY_DEFICIT"
ACTIVE_ARTIFACT = "ACTIVE_ARTIFACT"
PASSIVE_OVERSHOOT = "PASSIVE_OVERSHOOT"
EXACT_PLASTIC = "EXACT_PLASTIC"


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


@dataclass(frozen=True)
class SingleContactPrecisionPhaseReport:
    closing_score: int
    self_coupling: int
    denominator: int
    material_capacity_numerator: int
    minimum_required_impulse_numerator: int
    final_score_numerator: int
    kinetic_energy_change_numerator: int
    minimum_passive_denominator: int
    exact_plastic_base_denominator: int
    phase: str

    @property
    def capacity_sufficient(self) -> bool:
        return self.material_capacity_numerator >= self.minimum_required_impulse_numerator

    @property
    def passive(self) -> bool:
        return self.capacity_sufficient and self.kinetic_energy_change_numerator <= 0

    @property
    def exact_plastic(self) -> bool:
        return self.phase == EXACT_PLASTIC


def single_contact_precision_phase_report(
    closing_score: int,
    self_coupling: int,
    denominator: int,
    material_capacity_numerator: int,
) -> SingleContactPrecisionPhaseReport:
    """Classify material capacity, passivity and exact closure at one denominator."""
    _nonnegative("material_capacity_numerator", material_capacity_numerator)
    base = minimum_single_contact_passivity_report(
        closing_score,
        self_coupling,
        denominator,
    )
    exact_base = self_coupling // gcd(self_coupling, closing_score)
    if material_capacity_numerator < base.minimum_impulse_numerator:
        phase = CAPACITY_DEFICIT
    elif base.kinetic_energy_change_numerator > 0:
        phase = ACTIVE_ARTIFACT
    elif base.final_score_numerator == 0:
        phase = EXACT_PLASTIC
    else:
        phase = PASSIVE_OVERSHOOT

    if (denominator % exact_base == 0) != (base.final_score_numerator == 0):
        raise AssertionError("exact plastic phase disagrees with divisibility sublattice")
    if denominator >= base.minimum_passive_denominator and base.kinetic_energy_change_numerator > 0:
        raise AssertionError("eventual passivity threshold regressed")

    return SingleContactPrecisionPhaseReport(
        closing_score=closing_score,
        self_coupling=self_coupling,
        denominator=denominator,
        material_capacity_numerator=material_capacity_numerator,
        minimum_required_impulse_numerator=base.minimum_impulse_numerator,
        final_score_numerator=base.final_score_numerator,
        kinetic_energy_change_numerator=base.kinetic_energy_change_numerator,
        minimum_passive_denominator=base.minimum_passive_denominator,
        exact_plastic_base_denominator=exact_base,
        phase=phase,
    )
