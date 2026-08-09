"""Exact material-response state spectrum over a finite clearance box.

This module consumes the canonical E001 ``MaterialCurveProfile`` without
changing its fitting/calibration semantics.  A scalar isotropic material profile
maps coarse-only clearance-shell depth ``k`` to a loading or returning sample.

For dimension n and spatial factor d, shell k contains exactly

    (d-k+1)^n - (d-k)^n

positive clearance states.  If the material profile represents depths ``0..K``
and ``K'=min(K,d-1)``, exact coverage is

    represented   = d^n - (d-K')^n,
    underresolved = (d-K')^n - 1.

For an exact required coverage fraction ``P/Q``, the minimum represented material
depth can be solved without scanning depths.  With ``N=d^n-1`` and
``T=ceil(P*N/Q)``, the smallest K satisfying represented>=T is

    K_min = d - R_n(d^n-T),

where ``R_n`` is the existing integer nth-root primitive.  This sizes the number
of represented deformation-depth states only; it does not identify the material
amplitude precision ``A`` with the spatial factor or with measurement scale.

Response plateaus aggregate shell multiplicities with no vector enumeration.
The counts are combinatorial state counts, not probabilities or physical
weights.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .clearance_precision import clearance_shell_multiplicity
from .core import integer_nth_root
from .material_response import MaterialCurveProfile

LOADING = "LOADING"
RETURNING = "RETURNING"


@dataclass(frozen=True)
class MaterialClearanceCoverage:
    dimension: int
    collapse_factor: int
    max_material_depth: int
    effective_represented_depth: int
    coarse_only_states: int
    represented_states: int
    underresolved_states: int


@dataclass(frozen=True, order=True)
class MaterialResponseStateBin:
    response_sample: int
    state_count: int


@dataclass(frozen=True)
class MaterialClearanceSpectrum:
    coverage: MaterialClearanceCoverage
    branch: str
    bins: tuple[MaterialResponseStateBin, ...]


@dataclass(frozen=True)
class MaterialDepthSizing:
    dimension: int
    collapse_factor: int
    required_numerator: int
    required_denominator: int
    coarse_only_states: int
    required_represented_states: int
    minimum_material_depth: int
    minimum_branch_samples: int
    achieved_represented_states: int


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def material_clearance_coverage(
    dimension: int,
    collapse_factor: int,
    max_material_depth: int,
) -> MaterialClearanceCoverage:
    """Return exact represented/underresolved counts in positive clearance space."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    if (
        isinstance(max_material_depth, bool)
        or not isinstance(max_material_depth, int)
        or max_material_depth < 0
    ):
        raise ValueError("max_material_depth must be a non-negative integer")
    effective = min(max_material_depth, collapse_factor - 1)
    total = collapse_factor**dimension - 1
    inner_side = collapse_factor - effective
    underresolved = inner_side**dimension - 1
    represented = total - underresolved
    return MaterialClearanceCoverage(
        dimension=dimension,
        collapse_factor=collapse_factor,
        max_material_depth=max_material_depth,
        effective_represented_depth=effective,
        coarse_only_states=total,
        represented_states=represented,
        underresolved_states=underresolved,
    )


def minimum_material_depth_for_coverage(
    dimension: int,
    collapse_factor: int,
    required_numerator: int,
    required_denominator: int,
) -> MaterialDepthSizing:
    """Solve the minimum represented deformation depth for exact count coverage.

    ``required_numerator/required_denominator`` is an exact rational requirement
    on the fraction of positive coarse-only clearance states that must have a
    represented material depth.  No floating-point ratio is formed.
    """
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("required_denominator", required_denominator)
    if (
        isinstance(required_numerator, bool)
        or not isinstance(required_numerator, int)
        or required_numerator < 0
        or required_numerator > required_denominator
    ):
        raise ValueError("required_numerator must lie in 0..required_denominator")

    total = collapse_factor**dimension - 1
    required = (
        required_numerator * total + required_denominator - 1
    ) // required_denominator
    remaining_power_budget = collapse_factor**dimension - required
    inner_side = integer_nth_root(remaining_power_budget, dimension)
    minimum_depth = collapse_factor - inner_side
    coverage = material_clearance_coverage(
        dimension,
        collapse_factor,
        minimum_depth,
    )
    if coverage.represented_states < required:
        raise AssertionError("integer-root sizing failed its requested coverage")
    if minimum_depth > 0:
        previous = material_clearance_coverage(
            dimension,
            collapse_factor,
            minimum_depth - 1,
        )
        if previous.represented_states >= required:
            raise AssertionError("integer-root sizing did not return the minimum depth")
    return MaterialDepthSizing(
        dimension=dimension,
        collapse_factor=collapse_factor,
        required_numerator=required_numerator,
        required_denominator=required_denominator,
        coarse_only_states=total,
        required_represented_states=required,
        minimum_material_depth=minimum_depth,
        minimum_branch_samples=minimum_depth + 1,
        achieved_represented_states=coverage.represented_states,
    )


def material_clearance_spectrum(
    dimension: int,
    collapse_factor: int,
    profile: MaterialCurveProfile,
    branch: str = RETURNING,
) -> MaterialClearanceSpectrum:
    """Aggregate represented clearance states by one canonical material branch."""
    if not profile.loading or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if branch == LOADING:
        samples = profile.loading
    elif branch == RETURNING:
        samples = profile.returning
    else:
        raise ValueError("branch must be LOADING or RETURNING")

    coverage = material_clearance_coverage(
        dimension,
        collapse_factor,
        len(samples) - 1,
    )
    counts: Counter[int] = Counter()
    for depth in range(1, coverage.effective_represented_depth + 1):
        counts[samples[depth]] += clearance_shell_multiplicity(
            dimension,
            collapse_factor,
            depth,
        )
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("material clearance spectrum lost represented states")
    return MaterialClearanceSpectrum(
        coverage=coverage,
        branch=branch,
        bins=tuple(
            MaterialResponseStateBin(response_sample=sample, state_count=count)
            for sample, count in sorted(counts.items())
        ),
    )
