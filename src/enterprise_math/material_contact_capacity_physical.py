"""Exact physical material impulse capacity on a declared contact denominator.

A finite material sample ``r/A`` should not be converted to an integer force and
then independently converted to impulse if the intermediate rounding is not part
of the declared world law.  Combining the existing E001 force/time/momentum
count scales gives one exact contact impulse capacity first.

Let

    material force fraction = r/A,
    full-scale force count   = F_max,
    dt                       = tau/T_s,
    force                    = f/F_s,
    momentum                 = p_count/P_s.

The exact non-negative momentum-count impulse available from this material sample
in one tick is

    J_exact = N/D,

with

    N = F_max * r * tau * P_s,
    D = A * F_s * T_s.

The material response amplitude ``A`` and the physical force/time count scales
are therefore separate factors of the exact divisor.  At a declared contact
impulse denominator ``s`` we use the conservative finite capacity

    u_s = floor(N*s/D),
    rho_s = N*s - D*u_s,      0 <= rho_s < D.

Thus ``u_s/s <= J_exact``: finite representation never invents material impulse
capacity.  Exact representability occurs iff the reduced denominator

    D/gcd(N,D)

divides ``s``.

For a true divisibility refinement ``s' = m*s`` there is an exact carry law

    u_{m s} = m*u_s + floor(m*rho_s/D),
    rho_{m s} = (m*rho_s) mod D.

Consequently represented physical capacity is monotone under true refinement and
all coarse capacity is embedded in the fine lattice.  Numerically larger
non-multiple denominators are not called refinements here.

This is standard rational/floor arithmetic specialized to the E001 material
unit boundary.  The project-side value is keeping material precision, physical
unit scales, and contact impulse precision as distinct state coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_physical_projection import ForceImpulseCountScale


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


@dataclass(frozen=True)
class ExactMaterialImpulseCapacity:
    response_sample: int
    response_amplitude: int
    full_scale_force_count: int
    raw_numerator: int
    raw_denominator: int
    reduced_numerator: int
    reduced_denominator: int


@dataclass(frozen=True)
class ContactImpulseCapacityAtPrecision:
    exact: ExactMaterialImpulseCapacity
    contact_denominator: int
    capacity_numerator: int
    projection_remainder: int
    exactly_represented: bool


@dataclass(frozen=True)
class ContactImpulseCapacityRefinement:
    coarse: ContactImpulseCapacityAtPrecision
    refinement_multiplier: int
    fine: ContactImpulseCapacityAtPrecision
    exact_capacity_carry: int
    expected_fine_remainder: int
    coarse_capacity_embeds: bool


def exact_material_impulse_capacity(
    response_sample: int,
    response_amplitude: int,
    full_scale_force_count: int,
    scale: ForceImpulseCountScale,
) -> ExactMaterialImpulseCapacity:
    """Return the exact one-tick material impulse capacity before contact quantization."""
    _nonnegative("response_sample", response_sample)
    _positive("response_amplitude", response_amplitude)
    _nonnegative("full_scale_force_count", full_scale_force_count)
    if response_sample > response_amplitude:
        raise ValueError("response_sample must not exceed response_amplitude")
    numerator = (
        full_scale_force_count
        * response_sample
        * scale.tick_duration_count
        * scale.momentum_scale_factor
    )
    denominator = (
        response_amplitude
        * scale.force_scale_factor
        * scale.time_scale_factor
    )
    common = gcd(numerator, denominator)
    reduced_numerator = numerator // common
    reduced_denominator = denominator // common
    if reduced_denominator <= 0:
        raise AssertionError("material impulse capacity lost positive denominator")
    return ExactMaterialImpulseCapacity(
        response_sample=response_sample,
        response_amplitude=response_amplitude,
        full_scale_force_count=full_scale_force_count,
        raw_numerator=numerator,
        raw_denominator=denominator,
        reduced_numerator=reduced_numerator,
        reduced_denominator=reduced_denominator,
    )


def contact_impulse_capacity_at_precision(
    response_sample: int,
    response_amplitude: int,
    full_scale_force_count: int,
    scale: ForceImpulseCountScale,
    contact_denominator: int,
) -> ContactImpulseCapacityAtPrecision:
    """Project exact material capacity downward onto one contact impulse lattice."""
    _positive("contact_denominator", contact_denominator)
    exact = exact_material_impulse_capacity(
        response_sample,
        response_amplitude,
        full_scale_force_count,
        scale,
    )
    scaled_numerator = exact.raw_numerator * contact_denominator
    capacity, remainder = divmod(scaled_numerator, exact.raw_denominator)
    if not 0 <= remainder < exact.raw_denominator:
        raise AssertionError("contact capacity remainder escaped exact divisor")
    represented_exactly = remainder == 0
    if represented_exactly != (
        contact_denominator % exact.reduced_denominator == 0
    ):
        raise AssertionError("capacity exactness disagrees with reduced denominator lattice")
    return ContactImpulseCapacityAtPrecision(
        exact=exact,
        contact_denominator=contact_denominator,
        capacity_numerator=capacity,
        projection_remainder=remainder,
        exactly_represented=represented_exactly,
    )


def contact_impulse_capacity_refinement(
    response_sample: int,
    response_amplitude: int,
    full_scale_force_count: int,
    scale: ForceImpulseCountScale,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> ContactImpulseCapacityRefinement:
    """Return the exact carry when contact capacity is refined by a denominator multiple."""
    _positive("coarse_denominator", coarse_denominator)
    _positive("refinement_multiplier", refinement_multiplier)
    coarse = contact_impulse_capacity_at_precision(
        response_sample,
        response_amplitude,
        full_scale_force_count,
        scale,
        coarse_denominator,
    )
    fine = contact_impulse_capacity_at_precision(
        response_sample,
        response_amplitude,
        full_scale_force_count,
        scale,
        coarse_denominator * refinement_multiplier,
    )
    divisor = coarse.exact.raw_denominator
    carry = refinement_multiplier * coarse.projection_remainder // divisor
    expected_capacity = (
        refinement_multiplier * coarse.capacity_numerator + carry
    )
    expected_remainder = (
        refinement_multiplier * coarse.projection_remainder % divisor
    )
    if fine.capacity_numerator != expected_capacity:
        raise AssertionError("contact capacity refinement lost exact quotient carry")
    if fine.projection_remainder != expected_remainder:
        raise AssertionError("contact capacity refinement lost exact remainder carry")
    embeds = fine.capacity_numerator >= (
        refinement_multiplier * coarse.capacity_numerator
    )
    if not embeds:
        raise AssertionError("true contact precision refinement lost coarse material capacity")
    return ContactImpulseCapacityRefinement(
        coarse=coarse,
        refinement_multiplier=refinement_multiplier,
        fine=fine,
        exact_capacity_carry=carry,
        expected_fine_remainder=expected_remainder,
        coarse_capacity_embeds=embeds,
    )
