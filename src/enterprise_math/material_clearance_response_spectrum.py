"""Exact material-response spectrum over a multidimensional coarse-clearance box.

A scalar isotropic material profile maps coarse-only layer depth ``k`` to one
integer response sample.  In n clearance dimensions, shell ``k`` has exact state
multiplicity

    M_n(d,k) = (d-k+1)^n - (d-k)^n.

Therefore response plateaus can be counted without enumerating clearance
vectors: sum shell multiplicities for every depth producing the same response.

If the material profile represents depths ``0..K`` and spatial collapse factor
is ``d``, put ``K'=min(K,d-1)``.  The positive coarse-only contact box contains
``d^n-1`` states, split exactly into

    represented   = d^n - (d-K')^n,
    underresolved = (d-K')^n - 1.

These are combinatorial state counts, not probabilities.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_clearance_shells import clearance_shell_multiplicity
from .material_hysteresis import LOADING, RETURNING
from .material_response import MaterialCurveProfile


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
class MaterialClearanceResponseSpectrum:
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
    """Return exact represented/underresolved state counts in clearance space."""
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
    if represented != collapse_factor**dimension - inner_side**dimension:
        raise AssertionError("clearance coverage telescoping identity failed")
    return MaterialClearanceCoverage(
        dimension=dimension,
        collapse_factor=collapse_factor,
        max_material_depth=max_material_depth,
        effective_represented_depth=effective,
        coarse_only_states=total,
        represented_states=represented,
        underresolved_states=underresolved,
    )


def material_clearance_response_spectrum(
    dimension: int,
    collapse_factor: int,
    profile: MaterialCurveProfile,
    branch: str = RETURNING,
) -> MaterialClearanceResponseSpectrum:
    """Aggregate represented clearance-shell states by material response sample."""
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
        count = clearance_shell_multiplicity(dimension, collapse_factor, depth)
        counts[samples[depth]] += count
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("material response spectrum lost represented shell states")
    return MaterialClearanceResponseSpectrum(
        coverage=coverage,
        branch=branch,
        bins=tuple(
            MaterialResponseStateBin(response_sample=sample, state_count=count)
            for sample, count in sorted(counts.items())
        ),
    )
