"""Sufficient pre-contact reversal certificate for monotone loading impulse curves.

The constant-impulse stopping theorem is sharp when every interaction tick uses
the same impulse.  A hardening material usually produces a loading response that
is nondecreasing with deformation depth.  In that case the *current* loading
sample gives a lower bound on every later inward-phase material impulse.

Use inward-oriented retained lifted momentum

    Pi0 = A*p + eta,

with ``Pi0>0`` and ``|eta|<A``.  At current material depth ``k>=1`` let loading
sample ``r_k>0`` and declared full-scale impulse capacity ``J`` give the minimum
raw outward impulse numerator

    h = J*r_k.

As long as the body keeps drifting inward, depth can only increase and a
nondecreasing loading branch gives responses >=r_k.  Therefore actual lifted
momentum is no larger than the constant-minimum comparison trajectory

    Pi_t = Pi0 - t*h.

Whole inward momentum remains positive while ``Pi_t>=A``.  Its saved drift is
``floor(Pi_t/(A*M))`` because nested positive floor division composes.  Hence

    n = max(0, floor((Pi0-A)/h)),
    S_max = sum_{t=1..n} floor((Pi0-t*h)/(A*M))

is an upper bound on total inward saved drift before whole momentum ceases to be
inward.  If primitive clearance ``g>S_max`` and the finite material profile
represents every depth through ``k+S_max``, no terminal core contact or material
underresolution can occur first.

With ``h>0`` the same comparison reaches true outward whole momentum no later
than

    ceil((Pi0+A)/h)

material ticks.  While whole momentum is zero there is no inward drift, so the
current depth and positive loading sample remain available for this comparison.

This is a sufficient certificate for nondecreasing loading branches.  It is
sharp for a constant branch and may be conservative for hardening branches.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import MaterialCurveProfile


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class MonotoneLoadingReversalCertificate:
    primitive_clearance: int
    current_depth: int
    material_max_depth: int
    amplitude: int
    initial_lifted_inward_numerator: int
    current_loading_sample: int
    max_impulse_per_tick: int
    mass_quanta: int
    minimum_impulse_numerator_per_tick: int
    comparison_positive_drift_ticks: int
    maximum_inward_drift_cells: int
    maximum_reached_depth_before_noninward: int
    latest_noninward_tick: int
    latest_true_outward_tick: int
    clearance_sufficient: bool
    material_depth_sufficient: bool
    guaranteed_precontact_reversal: bool


def loading_branch_is_nondecreasing(profile: MaterialCurveProfile) -> bool:
    return all(
        left <= right
        for left, right in zip(profile.loading, profile.loading[1:])
    )


def monotone_loading_reversal_certificate(
    primitive_clearance: int,
    current_depth: int,
    initial_lifted_inward_numerator: int,
    profile: MaterialCurveProfile,
    mass_quanta: int,
    max_impulse_per_tick: int,
) -> MonotoneLoadingReversalCertificate:
    """Certify reversal before primitive contact using the current force as a lower bound."""
    _require_positive("primitive_clearance", primitive_clearance)
    _require_positive("current_depth", current_depth)
    _require_positive("initial_lifted_inward_numerator", initial_lifted_inward_numerator)
    _require_positive("mass_quanta", mass_quanta)
    _require_positive("max_impulse_per_tick", max_impulse_per_tick)
    if not profile.loading or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if current_depth >= len(profile.loading):
        raise ValueError("current_depth lies outside the finite material profile")
    if not loading_branch_is_nondecreasing(profile):
        raise ValueError("loading branch must be nondecreasing for this comparison certificate")

    amplitude = profile.amplitude
    response = profile.loading[current_depth]
    if response <= 0:
        raise ValueError("current loading sample must be positive for a positive impulse lower bound")
    h = max_impulse_per_tick * response
    if h <= 0:
        raise AssertionError("positive response and capacity produced non-positive impulse numerator")

    if initial_lifted_inward_numerator >= amplitude:
        positive_ticks = max(
            0,
            (initial_lifted_inward_numerator - amplitude) // h,
        )
    else:
        positive_ticks = 0
    denominator = amplitude * mass_quanta
    drift = sum(
        (initial_lifted_inward_numerator - tick * h) // denominator
        for tick in range(1, positive_ticks + 1)
    )
    if drift < 0:
        raise AssertionError("monotone comparison produced negative inward drift")
    max_depth = len(profile.loading) - 1
    reached_depth = current_depth + drift
    latest_noninward = (
        0
        if initial_lifted_inward_numerator < amplitude
        else positive_ticks + 1
    )
    latest_outward = (
        initial_lifted_inward_numerator + amplitude + h - 1
    ) // h
    clearance_ok = primitive_clearance > drift
    depth_ok = reached_depth <= max_depth
    return MonotoneLoadingReversalCertificate(
        primitive_clearance=primitive_clearance,
        current_depth=current_depth,
        material_max_depth=max_depth,
        amplitude=amplitude,
        initial_lifted_inward_numerator=initial_lifted_inward_numerator,
        current_loading_sample=response,
        max_impulse_per_tick=max_impulse_per_tick,
        mass_quanta=mass_quanta,
        minimum_impulse_numerator_per_tick=h,
        comparison_positive_drift_ticks=positive_ticks,
        maximum_inward_drift_cells=drift,
        maximum_reached_depth_before_noninward=reached_depth,
        latest_noninward_tick=latest_noninward,
        latest_true_outward_tick=latest_outward,
        clearance_sufficient=clearance_ok,
        material_depth_sufficient=depth_ok,
        guaranteed_precontact_reversal=clearance_ok and depth_ok,
    )
