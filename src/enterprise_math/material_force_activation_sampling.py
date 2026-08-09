"""Exact saved-state sampling of a monotone material force-activation layer.

A causal impulse world samples material force only at saved states.  Therefore a
material may contain a positive-force region geometrically while a fast finite
state transition never samples it.

Assume a nondecreasing LOADING branch.  Its zero prefix is followed, if at all,
by one positive-force depth interval.  Let ``k0`` be the first positive loading
depth, current same-side layer depth ``k<k0``, collapse factor ``d``, and finite
material maximum depth ``K``.  While response is zero, retained lifted momentum
``Pi`` is constant, so the whole inward saved drift per tick is

    q = floor(Pi/(A*M))

for positive inward ``Pi`` and integer mass ``M``.  The sampled depth sequence is
therefore

    k, k+q, k+2q, ...

until the same-side represented region ends.  Put ``K'=min(K,d-1)``.  For
``q>0`` the first possible positive-force sample is

    t0 = ceil((k0-k)/q),
    k_hit = k+t0*q.

The positive-force layer is actually sampled iff ``k_hit<=K'``.  Otherwise the
saved-state dynamics skips every represented positive-force depth.  This is a
time-sampling/material-layer effect, not hidden trajectory incidence.

If force is sampled, the resulting gap ``d-k_hit`` and depth ``k_hit`` can be fed
directly into ``monotone_loading_reversal_certificate`` because no impulse has
acted during the zero-force prefix and the lifted momentum is unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_reversal_certificate import (
    MonotoneLoadingReversalCertificate,
    loading_branch_is_nondecreasing,
    monotone_loading_reversal_certificate,
)
from .material_response import MaterialCurveProfile

ALREADY_ACTIVE = "ALREADY_ACTIVE"
SAMPLED_AFTER_ZERO_PREFIX = "SAMPLED_AFTER_ZERO_PREFIX"
ZERO_DRIFT_STALL = "ZERO_DRIFT_STALL"
NO_POSITIVE_FORCE_REPRESENTED = "NO_POSITIVE_FORCE_REPRESENTED"
SKIPPED_POSITIVE_FORCE_WINDOW = "SKIPPED_POSITIVE_FORCE_WINDOW"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ForceActivationSamplingReport:
    collapse_factor: int
    current_depth: int
    current_gap: int
    represented_max_depth: int
    first_positive_loading_depth: int | None
    inward_lifted_momentum_numerator: int
    mass_quanta: int
    zero_force_saved_drift_cells: int
    first_positive_sample_tick: int | None
    first_positive_sample_depth: int | None
    first_positive_sample_gap: int | None
    status: str

    @property
    def force_layer_sampled(self) -> bool:
        return self.status in (ALREADY_ACTIVE, SAMPLED_AFTER_ZERO_PREFIX)


def first_positive_loading_depth(profile: MaterialCurveProfile) -> int | None:
    """First positive LOADING sample at a positive deformation depth."""
    for depth, sample in enumerate(profile.loading[1:], start=1):
        if sample > 0:
            return depth
    return None


def force_activation_sampling_report(
    collapse_factor: int,
    current_depth: int,
    inward_lifted_momentum_numerator: int,
    profile: MaterialCurveProfile,
    mass_quanta: int,
) -> ForceActivationSamplingReport:
    """Classify whether saved zero-force drift ever samples the positive force layer."""
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("current_depth", current_depth)
    _require_positive("inward_lifted_momentum_numerator", inward_lifted_momentum_numerator)
    _require_positive("mass_quanta", mass_quanta)
    if not profile.loading or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if current_depth >= collapse_factor:
        raise ValueError("current_depth must correspond to a positive same-side gap")
    if current_depth >= len(profile.loading):
        raise ValueError("current_depth lies outside the finite material profile")
    if not loading_branch_is_nondecreasing(profile):
        raise ValueError("loading branch must be nondecreasing for one activation interval")

    max_depth = len(profile.loading) - 1
    represented_max = min(max_depth, collapse_factor - 1)
    current_gap = collapse_factor - current_depth
    k0 = first_positive_loading_depth(profile)
    q = inward_lifted_momentum_numerator // (profile.amplitude * mass_quanta)

    if profile.loading[current_depth] > 0:
        return ForceActivationSamplingReport(
            collapse_factor,
            current_depth,
            current_gap,
            represented_max,
            k0,
            inward_lifted_momentum_numerator,
            mass_quanta,
            q,
            0,
            current_depth,
            current_gap,
            ALREADY_ACTIVE,
        )
    if k0 is None or k0 > represented_max:
        return ForceActivationSamplingReport(
            collapse_factor,
            current_depth,
            current_gap,
            represented_max,
            k0,
            inward_lifted_momentum_numerator,
            mass_quanta,
            q,
            None,
            None,
            None,
            NO_POSITIVE_FORCE_REPRESENTED,
        )
    if q == 0:
        return ForceActivationSamplingReport(
            collapse_factor,
            current_depth,
            current_gap,
            represented_max,
            k0,
            inward_lifted_momentum_numerator,
            mass_quanta,
            0,
            None,
            None,
            None,
            ZERO_DRIFT_STALL,
        )

    ticks = (k0 - current_depth + q - 1) // q
    hit = current_depth + ticks * q
    if hit > represented_max:
        return ForceActivationSamplingReport(
            collapse_factor,
            current_depth,
            current_gap,
            represented_max,
            k0,
            inward_lifted_momentum_numerator,
            mass_quanta,
            q,
            None,
            None,
            None,
            SKIPPED_POSITIVE_FORCE_WINDOW,
        )
    return ForceActivationSamplingReport(
        collapse_factor,
        current_depth,
        current_gap,
        represented_max,
        k0,
        inward_lifted_momentum_numerator,
        mass_quanta,
        q,
        ticks,
        hit,
        collapse_factor - hit,
        SAMPLED_AFTER_ZERO_PREFIX,
    )


@dataclass(frozen=True)
class EngagementThenReversalCertificate:
    engagement: ForceActivationSamplingReport
    reversal: MonotoneLoadingReversalCertificate | None

    @property
    def guaranteed_precontact_reversal(self) -> bool:
        return (
            self.reversal is not None
            and self.reversal.guaranteed_precontact_reversal
        )


def engagement_then_reversal_certificate(
    collapse_factor: int,
    current_depth: int,
    inward_lifted_momentum_numerator: int,
    profile: MaterialCurveProfile,
    mass_quanta: int,
    max_impulse_per_tick: int,
) -> EngagementThenReversalCertificate:
    """Chain exact zero-force sampling with the monotone positive-force certificate."""
    engagement = force_activation_sampling_report(
        collapse_factor,
        current_depth,
        inward_lifted_momentum_numerator,
        profile,
        mass_quanta,
    )
    if not engagement.force_layer_sampled:
        return EngagementThenReversalCertificate(engagement, None)
    if engagement.first_positive_sample_depth is None or engagement.first_positive_sample_gap is None:
        raise AssertionError("sampled force layer lost its hit depth/gap")
    reversal = monotone_loading_reversal_certificate(
        primitive_clearance=engagement.first_positive_sample_gap,
        current_depth=engagement.first_positive_sample_depth,
        initial_lifted_inward_numerator=inward_lifted_momentum_numerator,
        profile=profile,
        mass_quanta=mass_quanta,
        max_impulse_per_tick=max_impulse_per_tick,
    )
    return EngagementThenReversalCertificate(engagement, reversal)
