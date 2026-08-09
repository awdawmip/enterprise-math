"""Exact spatial-to-material-to-kinematic spectra for the unified E001 world.

This module composes three already explicit finite layers:

    coarse clearance shell -> material branch sample -> kinematic return budget.

For scalar incoming budget ``B`` and material sample ``r/A``, the returned
budget is ``floor(B*r/A)``.  Every represented clearance shell has an exact
integer multiplicity, so equal returned budgets can be aggregated without
enumerating primitive states.

For a 2D incoming integer vector, the same shell can additionally be classified
by whether componentwise exact L-infinity budget scaling stays on the original
primitive lattice ray or exposes the direction-vs-budget remainder tradeoff.
The resulting counts are finite state multiplicities, not probabilities.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_clearance_response_spectrum import (
    MaterialClearanceCoverage,
    material_clearance_coverage,
)
from .material_clearance_shells import clearance_shell_multiplicity
from .material_hysteresis import LOADING, RETURNING
from .material_kinematic_coupling import rebound_budget
from .material_kinematic_coupling_2d import direction_budget_report_2d
from .material_response import MaterialCurveProfile


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _branch_samples(profile: MaterialCurveProfile, branch: str) -> tuple[int, ...]:
    if not profile.loading or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if branch == LOADING:
        return profile.loading
    if branch == RETURNING:
        return profile.returning
    raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True, order=True)
class ScalarKinematicBudgetBin:
    returned_budget: int
    state_count: int


@dataclass(frozen=True)
class ScalarKinematicSpectrum:
    coverage: MaterialClearanceCoverage
    branch: str
    incoming_budget: int
    bins: tuple[ScalarKinematicBudgetBin, ...]


def scalar_kinematic_spectrum(
    dimension: int,
    collapse_factor: int,
    profile: MaterialCurveProfile,
    incoming_budget: int,
    branch: str = RETURNING,
) -> ScalarKinematicSpectrum:
    """Aggregate represented clearance states by final scalar return budget."""
    _require_nonnegative("incoming_budget", incoming_budget)
    samples = _branch_samples(profile, branch)
    coverage = material_clearance_coverage(
        dimension,
        collapse_factor,
        len(samples) - 1,
    )
    counts: Counter[int] = Counter()
    for depth in range(1, coverage.effective_represented_depth + 1):
        multiplicity = clearance_shell_multiplicity(
            dimension, collapse_factor, depth
        )
        returned = rebound_budget(
            incoming_budget,
            samples[depth],
            profile.amplitude,
        ).returned_budget
        counts[returned] += multiplicity
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("scalar kinematic spectrum lost represented states")
    return ScalarKinematicSpectrum(
        coverage=coverage,
        branch=branch,
        incoming_budget=incoming_budget,
        bins=tuple(
            ScalarKinematicBudgetBin(returned_budget=budget, state_count=count)
            for budget, count in sorted(counts.items())
        ),
    )


@dataclass(frozen=True, order=True)
class DirectionalKinematicBudgetBin2D:
    componentwise_linf_budget: int
    primitive_ray_locked_linf_budget: int
    direction_preserved: bool
    state_count: int


@dataclass(frozen=True)
class DirectionalKinematicSpectrum2D:
    coverage: MaterialClearanceCoverage
    branch: str
    incoming_vector: tuple[int, int]
    bins: tuple[DirectionalKinematicBudgetBin2D, ...]
    direction_preserved_states: int
    direction_conflict_states: int


def directional_kinematic_spectrum_2d(
    collapse_factor: int,
    profile: MaterialCurveProfile,
    incoming_vector: tuple[int, int],
    branch: str = RETURNING,
) -> DirectionalKinematicSpectrum2D:
    """Count 2D spatial states by material return budget and ray-lock status."""
    samples = _branch_samples(profile, branch)
    coverage = material_clearance_coverage(
        2,
        collapse_factor,
        len(samples) - 1,
    )
    counts: Counter[tuple[int, int, bool]] = Counter()
    preserved_states = 0
    conflict_states = 0
    for depth in range(1, coverage.effective_represented_depth + 1):
        multiplicity = clearance_shell_multiplicity(2, collapse_factor, depth)
        report = direction_budget_report_2d(
            incoming_vector,
            samples[depth],
            profile.amplitude,
        )
        key = (
            report.componentwise_linf_budget,
            report.primitive_ray_locked_linf_budget,
            report.componentwise_preserves_primitive_ray,
        )
        counts[key] += multiplicity
        if report.componentwise_preserves_primitive_ray:
            preserved_states += multiplicity
        else:
            conflict_states += multiplicity

    if preserved_states + conflict_states != coverage.represented_states:
        raise AssertionError("directional spectrum lost represented states")
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("directional budget bins lost represented states")
    return DirectionalKinematicSpectrum2D(
        coverage=coverage,
        branch=branch,
        incoming_vector=incoming_vector,
        bins=tuple(
            DirectionalKinematicBudgetBin2D(
                componentwise_linf_budget=key[0],
                primitive_ray_locked_linf_budget=key[1],
                direction_preserved=key[2],
                state_count=count,
            )
            for key, count in sorted(counts.items())
        ),
        direction_preserved_states=preserved_states,
        direction_conflict_states=conflict_states,
    )
