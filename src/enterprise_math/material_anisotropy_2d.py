"""Finite 2D anisotropic material response from clearance active sets.

The unified coarse-contact geometry already exposes more structure than a scalar
layer depth. For a positive coarse-only clearance vector ``(g_x,g_y)``, let

    q = max(g_x,g_y),       k = d-q,

and retain the set of coordinates attaining ``q``. In two dimensions the
possible active sets are exactly ``{x}``, ``{y}``, and ``{x,y}``.

This module uses those finite witnesses as a minimal anisotropy coordinate. A
material may provide one explicit ``MaterialCurveProfile`` for each active set.
No continuous angle, tensor, interpolation, or hidden real-valued normal is
introduced.

The generic clearance quotient/counting rules are imported from canonical
``clearance_precision`` rather than duplicated here. This module remains only
an E001 material-law specialization.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import comb

from .clearance_precision import (
    ACTIVE_COUNT,
    ACTIVE_SET,
    SCALAR_DEPTH,
    active_axis_count_multiplicity,
    clearance_behavior_signature,
)
from .material_clearance_spectrum import (
    MaterialClearanceCoverage,
    material_clearance_coverage,
)
from .material_hysteresis import LOADING, RETURNING
from .material_response import MaterialCurveProfile

PRIMITIVE_CONTACT = "PRIMITIVE_CONTACT"
COARSE_ONLY_CONTACT = "COARSE_ONLY_CONTACT"
RESOLVED = "RESOLVED"

X_ACTIVE = (0,)
Y_ACTIVE = (1,)
XY_ACTIVE = (0, 1)
ActiveSet2D = tuple[int, ...]


def _branch_samples(profile: MaterialCurveProfile, branch: str) -> tuple[int, ...]:
    if branch == LOADING:
        return profile.loading
    if branch == RETURNING:
        return profile.returning
    raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True)
class AnisotropicMaterialProfile2D:
    x_profile: MaterialCurveProfile
    y_profile: MaterialCurveProfile
    corner_profile: MaterialCurveProfile
    amplitude: int
    depth_count: int


def anisotropic_material_profile_2d(
    x_profile: MaterialCurveProfile,
    y_profile: MaterialCurveProfile,
    corner_profile: MaterialCurveProfile,
) -> AnisotropicMaterialProfile2D:
    """Assemble three explicit active-set profiles on one finite scale/domain."""
    profiles = (x_profile, y_profile, corner_profile)
    amplitudes = {profile.amplitude for profile in profiles}
    lengths = {len(profile.loading) for profile in profiles}
    if len(amplitudes) != 1:
        raise ValueError("anisotropic profiles must share one response amplitude")
    if len(lengths) != 1 or any(
        len(profile.loading) != len(profile.returning) or not profile.loading
        for profile in profiles
    ):
        raise ValueError("anisotropic profiles must share one nonempty deformation domain")
    amplitude = next(iter(amplitudes))
    depth_count = next(iter(lengths))
    return AnisotropicMaterialProfile2D(
        x_profile=x_profile,
        y_profile=y_profile,
        corner_profile=corner_profile,
        amplitude=amplitude,
        depth_count=depth_count,
    )


def profile_for_active_set_2d(
    profile: AnisotropicMaterialProfile2D,
    active_set: ActiveSet2D,
) -> MaterialCurveProfile:
    if active_set == X_ACTIVE:
        return profile.x_profile
    if active_set == Y_ACTIVE:
        return profile.y_profile
    if active_set == XY_ACTIVE:
        return profile.corner_profile
    raise ValueError("2D coarse clearance active set must be {x}, {y}, or {x,y}")


def minimum_clearance_observable_for_anisotropy_2d(
    profile: AnisotropicMaterialProfile2D,
    branch: str = RETURNING,
) -> str:
    """Return the coarsest current clearance signature preserving this branch law."""
    x = _branch_samples(profile.x_profile, branch)
    y = _branch_samples(profile.y_profile, branch)
    corner = _branch_samples(profile.corner_profile, branch)
    if x == y == corner:
        return SCALAR_DEPTH
    if x == y:
        return ACTIVE_COUNT
    return ACTIVE_SET


@dataclass(frozen=True)
class AnisotropicClearanceWitness2D:
    """Thin E001 adapter around the canonical clearance quotient signature."""

    collapse_factor: int
    clearances: tuple[int, int]
    status: str
    layer_depth: int | None
    active_indices: ActiveSet2D


def _clearance_witness_2d(
    clearances: tuple[int, int], collapse_factor: int
) -> AnisotropicClearanceWitness2D:
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    values = tuple(clearances)
    if len(values) != 2:
        raise ValueError("2D anisotropy requires exactly two clearance coordinates")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("clearance coordinates must be non-negative integers")
    q = max(values)
    if q == 0:
        return AnisotropicClearanceWitness2D(
            collapse_factor, values, PRIMITIVE_CONTACT, None, ()
        )
    if q >= collapse_factor:
        return AnisotropicClearanceWitness2D(
            collapse_factor, values, RESOLVED, None, ()
        )
    depth, active = clearance_behavior_signature(values, collapse_factor, ACTIVE_SET)
    if not isinstance(depth, int) or not isinstance(active, tuple):
        raise AssertionError("canonical active-set signature returned an invalid shape")
    return AnisotropicClearanceWitness2D(
        collapse_factor, values, COARSE_ONLY_CONTACT, depth, active
    )


def _specific_active_set_multiplicity_2d(
    collapse_factor: int, layer_depth: int, active_axis_count: int
) -> int:
    total = active_axis_count_multiplicity(
        2, collapse_factor, layer_depth, active_axis_count
    )
    return total // comb(2, active_axis_count)


@dataclass(frozen=True)
class AnisotropicClearanceResponse2D:
    clearance: AnisotropicClearanceWitness2D
    branch: str
    response_sample: int | None


def anisotropic_response_for_clearance_2d(
    clearances: tuple[int, int],
    collapse_factor: int,
    profile: AnisotropicMaterialProfile2D,
    branch: str = RETURNING,
) -> AnisotropicClearanceResponse2D:
    """Evaluate one finite clearance state using only depth and active-set witness."""
    signature = _clearance_witness_2d(clearances, collapse_factor)
    _branch_samples(profile.x_profile, branch)
    if signature.status != COARSE_ONLY_CONTACT:
        return AnisotropicClearanceResponse2D(signature, branch, None)
    if signature.layer_depth is None:
        raise AssertionError("coarse-only contact lost scalar layer depth")
    if signature.layer_depth >= profile.depth_count:
        raise ValueError("anisotropic material depth is underrepresented")
    active_profile = profile_for_active_set_2d(profile, signature.active_indices)
    samples = _branch_samples(active_profile, branch)
    return AnisotropicClearanceResponse2D(
        clearance=signature,
        branch=branch,
        response_sample=samples[signature.layer_depth],
    )


@dataclass(frozen=True, order=True)
class AnisotropicResponseBin2D:
    response_sample: int
    state_count: int


@dataclass(frozen=True)
class AnisotropicResponseSpectrum2D:
    coverage: MaterialClearanceCoverage
    branch: str
    minimum_clearance_observable: str
    bins: tuple[AnisotropicResponseBin2D, ...]


def anisotropic_response_spectrum_2d(
    collapse_factor: int,
    profile: AnisotropicMaterialProfile2D,
    branch: str = RETURNING,
) -> AnisotropicResponseSpectrum2D:
    """Count represented 2D clearance states by anisotropic material response."""
    _branch_samples(profile.x_profile, branch)
    coverage = material_clearance_coverage(
        2,
        collapse_factor,
        profile.depth_count - 1,
    )
    counts: Counter[int] = Counter()
    for depth in range(1, coverage.effective_represented_depth + 1):
        one_axis_count = _specific_active_set_multiplicity_2d(
            collapse_factor, depth, 1
        )
        corner_count = _specific_active_set_multiplicity_2d(
            collapse_factor, depth, 2
        )
        for active_set, multiplicity in (
            (X_ACTIVE, one_axis_count),
            (Y_ACTIVE, one_axis_count),
            (XY_ACTIVE, corner_count),
        ):
            active_profile = profile_for_active_set_2d(profile, active_set)
            sample = _branch_samples(active_profile, branch)[depth]
            counts[sample] += multiplicity
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("anisotropic response spectrum lost represented states")
    return AnisotropicResponseSpectrum2D(
        coverage=coverage,
        branch=branch,
        minimum_clearance_observable=minimum_clearance_observable_for_anisotropy_2d(
            profile, branch
        ),
        bins=tuple(
            AnisotropicResponseBin2D(response_sample=sample, state_count=count)
            for sample, count in sorted(counts.items())
        ),
    )