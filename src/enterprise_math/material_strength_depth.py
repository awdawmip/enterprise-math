"""Physical material-strength activation depth from a finite force-response curve.

A coarse interaction layer can be geometrically represented while the material
at its current deformation depth is still too weak to supply the impulse needed
to make one closing contact nonclosing in the declared tick.

For material response sample ``r_k`` on amplitude ``A``, full-scale force count
``F_max``, and the existing physical count scales, the exact one-tick impulse
capacity is

    C_k = F_max * r_k * tau * P_s / (A * F_s * T_s).

One contact with closing score magnitude ``q`` and self-coupling ``K`` has exact
zero-score demand ``q/K``.  Physical sufficiency at depth k is therefore the
pure-integer inequality

    F_max * tau * P_s * K * r_k
      >= q * A * F_s * T_s.

For a nondecreasing material branch this gives one exact positive-depth
activation threshold.  Put

    G = F_max * tau * P_s * K,
    H = q * A * F_s * T_s.

If ``G=0`` or ``ceil(H/G)>A`` then no represented material sample can meet the
contact demand.  Otherwise the minimum sufficient response sample is

    r_required = ceil(H/G),

and the first positive material depth whose branch sample reaches that value is
the first physically strong contact layer.

For a fixed positive primitive gap ``g`` and static sampled interaction depth
``k=d-g``, the corresponding collapse-factor threshold is simply

    d_strength = g + k_strength.

This is a static current-state strength threshold, not a monotonicity theorem for
full causal trajectories: saved-state motion can skip force-active depths or
enter material underresolution, producing the reentry phenomena already present
in the impulse world.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_physical_projection import ForceImpulseCountScale
from .material_response import MaterialCurveProfile


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _branch_samples(
    profile: MaterialCurveProfile,
    branch: MaterialBranch,
) -> tuple[int, ...]:
    if branch == LOADING:
        return profile.loading
    if branch == RETURNING:
        return profile.returning
    raise ValueError("branch must be LOADING or RETURNING")


def _ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class MaterialPhysicalStrengthDepthReport:
    branch: MaterialBranch
    closing_score: int
    self_coupling: int
    full_scale_force_count: int
    response_amplitude: int
    strength_per_response_sample: int
    required_strength_product: int
    required_response_sample: int | None
    first_sufficient_positive_depth: int | None
    sufficient_positive_depths: tuple[int, ...]
    represented_positive_depth_count: int

    @property
    def any_represented_depth_physically_strong_enough(self) -> bool:
        return self.first_sufficient_positive_depth is not None


def material_physical_strength_depth_report(
    profile: MaterialCurveProfile,
    branch: MaterialBranch,
    full_scale_force_count: int,
    scale: ForceImpulseCountScale,
    closing_score: int,
    self_coupling: int,
) -> MaterialPhysicalStrengthDepthReport:
    """Return the first positive depth whose exact one-tick force can meet contact demand."""
    _nonnegative("full_scale_force_count", full_scale_force_count)
    _positive("closing_score", closing_score)
    _positive("self_coupling", self_coupling)
    samples = _branch_samples(profile, branch)
    if not samples or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if any(left > right for left, right in zip(samples, samples[1:])):
        raise ValueError("declared branch must be nondecreasing for one strength-depth threshold")
    if any(sample < 0 or sample > profile.amplitude for sample in samples):
        raise ValueError("material branch sample lies outside response amplitude")

    strength_per_sample = (
        full_scale_force_count
        * scale.tick_duration_count
        * scale.momentum_scale_factor
        * self_coupling
    )
    required_product = (
        closing_score
        * profile.amplitude
        * scale.force_scale_factor
        * scale.time_scale_factor
    )
    if strength_per_sample == 0:
        required_sample = None
        first = None
        sufficient: tuple[int, ...] = ()
    else:
        candidate = _ceil_div(required_product, strength_per_sample)
        if candidate > profile.amplitude:
            required_sample = None
            first = None
            sufficient = ()
        else:
            required_sample = candidate
            sufficient = tuple(
                depth
                for depth, sample in enumerate(samples[1:], start=1)
                if sample >= candidate
            )
            first = sufficient[0] if sufficient else None
            if sufficient and sufficient != tuple(
                range(sufficient[0], len(samples))
            ):
                raise AssertionError("nondecreasing material strength depths lost terminal interval")

    if first is not None:
        lhs = strength_per_sample * samples[first]
        if lhs < required_product:
            raise AssertionError("reported first strong material depth is physically insufficient")
        if first > 1 and strength_per_sample * samples[first - 1] >= required_product:
            raise AssertionError("reported first strong material depth is not minimal")

    return MaterialPhysicalStrengthDepthReport(
        branch=branch,
        closing_score=closing_score,
        self_coupling=self_coupling,
        full_scale_force_count=full_scale_force_count,
        response_amplitude=profile.amplitude,
        strength_per_response_sample=strength_per_sample,
        required_strength_product=required_product,
        required_response_sample=required_sample,
        first_sufficient_positive_depth=first,
        sufficient_positive_depths=sufficient,
        represented_positive_depth_count=max(0, len(samples) - 1),
    )


def minimum_collapse_factor_for_physical_strength(
    primitive_gap: int,
    report: MaterialPhysicalStrengthDepthReport,
) -> int | None:
    """Translate positive material depth k into static sampled factor d=g+k."""
    _positive("primitive_gap", primitive_gap)
    depth = report.first_sufficient_positive_depth
    return None if depth is None else primitive_gap + depth
