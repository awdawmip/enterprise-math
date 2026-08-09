"""E001 bridge from collapse-generated contact layers to material rebound resolution.

This module tests one deliberately minimal coupling hypothesis:

* a spatial collapse factor ``d`` creates a one-sided positive-gap rebound shell
  of capacity ``A_d = d - 1``;
* the material oscillator may use that shell capacity as its integer amplitude;
* contact and oscillatory rebound therefore have separate exact thresholds.

The coupling is an engineering pressure-test rule, not a physical constitutive
law.  In particular, ``CONTACT_DEAD_ZONE`` means that contact exists at the
chosen scale but the chosen oscillator cannot resolve even its first transverse
integer response; another material response law may still act there.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_invariants import parameter_rotation_minimum_transverse_amplitude

NO_CONTACT = "NO_CONTACT"
CONTACT_DEAD_ZONE = "CONTACT_DEAD_ZONE"
CONTACT_REBOUND_RESOLVED = "CONTACT_REBOUND_RESOLVED"
MaterialContactStatus = str


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def rebound_layer_capacity(collapse_factor: int) -> int:
    """Return the maximum positive primitive gap collapsed to contact.

    Under ``Contact_d(g) iff g < d``, positive gaps ``1..d-1`` are the
    scale-generated shell outside the primitive contact core.  Its one-sided
    depth/capacity is therefore exactly ``d-1``.
    """
    _require_positive("collapse_factor", collapse_factor)
    return collapse_factor - 1


def minimum_collapse_factor_for_parameter_rebound(m: int) -> int:
    """Smallest ``d`` whose shell can resolve one transverse rotor quantum."""
    minimum_amplitude = parameter_rotation_minimum_transverse_amplitude(m)
    return minimum_amplitude + 1


def minimum_collapse_factor_for_contact_and_rebound(
    primitive_gap: int, m: int
) -> int:
    """Smallest integer factor satisfying both contact and rebound resolution."""
    _require_natural("primitive_gap", primitive_gap)
    contact_threshold = primitive_gap + 1
    rebound_threshold = minimum_collapse_factor_for_parameter_rebound(m)
    return max(contact_threshold, rebound_threshold)


@dataclass(frozen=True)
class MaterialContactPhase:
    """One exact phase classification for the minimal contact/material coupling."""

    primitive_gap: int
    collapse_factor: int
    rebound_capacity: int
    minimum_rebound_amplitude: int
    status: MaterialContactStatus

    @property
    def contact(self) -> bool:
        return self.status != NO_CONTACT

    @property
    def rebound_resolved(self) -> bool:
        return self.status == CONTACT_REBOUND_RESOLVED


def material_contact_phase(
    primitive_gap: int,
    collapse_factor: int,
    m: int,
) -> MaterialContactPhase:
    """Classify no-contact, contact-dead-zone, or resolved-rebound phase.

    The rules are exact once the candidate coupling ``A_d=d-1`` is declared:

    * contact iff ``primitive_gap < collapse_factor``;
    * material rebound is resolved iff shell capacity is at least
      ``floor(m/2)+1``.
    """
    _require_natural("primitive_gap", primitive_gap)
    _require_positive("collapse_factor", collapse_factor)
    minimum_amplitude = parameter_rotation_minimum_transverse_amplitude(m)
    capacity = rebound_layer_capacity(collapse_factor)

    if primitive_gap >= collapse_factor:
        status = NO_CONTACT
    elif capacity < minimum_amplitude:
        status = CONTACT_DEAD_ZONE
    else:
        status = CONTACT_REBOUND_RESOLVED

    return MaterialContactPhase(
        primitive_gap=primitive_gap,
        collapse_factor=collapse_factor,
        rebound_capacity=capacity,
        minimum_rebound_amplitude=minimum_amplitude,
        status=status,
    )
