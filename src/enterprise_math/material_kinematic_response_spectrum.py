"""Exact spatial-to-material-to-kinematic spectra for the unified E001 world.

This module composes three already explicit finite layers:

    coarse clearance shell -> material branch sample -> kinematic return budget.

For scalar incoming budget ``B`` and material sample ``r/A``, the returned
budget is ``floor(B*r/A)``.  Every represented clearance shell has an exact
integer multiplicity, so equal returned budgets can be aggregated without
enumerating primitive states.

A represented interaction is not automatically a true rebound.  The kinematic
return is strictly positive exactly when ``B*r >= A``.  Consequently the
represented coarse layer splits into ZERO_RETURN and NONZERO_RETURN state mass.
For a fixed positive material sample the minimum incoming budget resolving one
return quantum is ``ceil(A/r)``.

For a 2D incoming integer vector, the same shell can additionally be classified
by whether componentwise exact L-infinity budget scaling stays on the original
primitive lattice ray or exposes the direction-vs-budget remainder tradeoff.
The resulting counts are finite state multiplicities, not probabilities.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .clearance_precision import clearance_shell_multiplicity
from .material_clearance_spectrum import (
    MaterialClearanceCoverage,
    material_clearance_coverage,
)
from .material_hysteresis import LOADING, RETURNING
from .material_kinematic_coupling import rebound_budget
from .material_kinematic_coupling_2d import direction_budget_report_2d
from .material_response import MaterialCurveProfile


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def minimum_budget_for_nonzero_return(response_sample: int, amplitude: int) -> int | None:
    """Return ``ceil(A/r)`` for positive ``r``, else None for a zero response."""
    _require_nonnegative("response_sample", response_sample)
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    if response_sample > amplitude:
        raise ValueError("response_sample must not exceed amplitude")
    if response_sample == 0:
        return None
    return (amplitude + response_sample - 1) // response_sample


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
    zero_return_states: int
    nonzero_return_states: int


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
    zero_return_states = 0
    nonzero_return_states = 0
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
        if returned == 0:
            zero_return_states += multiplicity
        else:
            nonzero_return_states += multiplicity
    if sum(counts.values()) != coverage.represented_states:
        raise AssertionError("scalar kinematic spectrum lost represented states")
    if zero_return_states + nonzero_return_states != coverage.represented_states:
        raise AssertionError("zero/nonzero return split lost represented states")
    return ScalarKinematicSpectrum(
        coverage=coverage,
        branch=branch,
        incoming_budget=incoming_budget,
        bins=tuple(
            ScalarKinematicBudgetBin(returned_budget=budget, state_count=count)
            for budget, count in sorted(counts.items())
        ),
        zero_return_states=zero_return_states,
        nonzero_return_states=nonzero_return_states,
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
    zero_return_states: int
    nonzero_return_states: int
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
    zero_return_states = 0
    nonzero_return_states = 0
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
        if report.componentwise_linf_budget == 0:
            zero_return_states += multiplicity
        else:
            nonzero_return_states += multiplicity
        if report.componentwise_preserves_primitive_ray:
            preserved_states += multiplicity
        else:
            conflict_states += multiplicity

    if zero_return_states + nonzero_return_states != coverage.represented_states:
        raise AssertionError("directional zero/nonzero return split lost represented states")
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
        zero_return_states=zero_return_states,
        nonzero_return_states=nonzero_return_states,
        direction_preserved_states=preserved_states,
        direction_conflict_states=conflict_states,
    )