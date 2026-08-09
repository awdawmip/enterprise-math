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

Response plateaus aggregate shell multiplicities with no vector enumeration.
The counts are combinatorial state counts, not probabilities or physical
weights.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .clearance_precision import clearance_shell_multiplicity
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
