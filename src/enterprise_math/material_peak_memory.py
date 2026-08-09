"""Finite peak-history material state for Mullins-style path dependence.

The baseline ``MaterialHistoryState`` remembers deformation index and current
loading/returning branch.  That is sufficient for one fixed two-branch profile,
but it is not sufficient for material laws whose future response depends on the
largest deformation previously reached.

This module adds one deliberately minimal finite extension:

    state = (deformation_index, branch, historical_peak, response_sample).

A ``PeakConditionedMaterialFamily`` supplies one complete finite curve profile
for each allowed historical peak.  The current profile is selected by the
largest deformation index seen so far.  Increasing deformation updates the peak;
decreasing deformation preserves it; holding preserves both peak and branch.

This is a pressure-test model for path-dependent material memory, not a claim
that historical peak alone is sufficient for real Mullins softening.  Repeated
cycles, time, temperature, and other histories may require further finite state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_response import MaterialCurveProfile


@dataclass(frozen=True)
class PeakConditionedMaterialFamily:
    """Finite map from historical maximum deformation to a complete profile."""

    peak_profiles: tuple[tuple[int, MaterialCurveProfile], ...]
    amplitude: int
    deformation_count: int


def peak_conditioned_material_family(
    peak_profiles: dict[int, MaterialCurveProfile]
    | tuple[tuple[int, MaterialCurveProfile], ...]
    | list[tuple[int, MaterialCurveProfile]],
) -> PeakConditionedMaterialFamily:
    """Validate and freeze one finite peak-conditioned material law."""
    if isinstance(peak_profiles, dict):
        raw_items = tuple(peak_profiles.items())
    else:
        raw_items = tuple(peak_profiles)
    if not raw_items:
        raise ValueError("at least one historical-peak profile is required")
    raw_peaks = tuple(peak for peak, _profile in raw_items)
    if len(raw_peaks) != len(set(raw_peaks)):
        raise ValueError("historical peaks must be unique")
    items = tuple(sorted(raw_items))
    peaks = tuple(peak for peak, _profile in items)
    if any(
        isinstance(peak, bool) or not isinstance(peak, int) or peak < 0
        for peak in peaks
    ):
        raise ValueError("historical peaks must be non-negative integers")

    amplitudes = {profile.amplitude for _peak, profile in items}
    lengths = {len(profile.loading) for _peak, profile in items}
    if len(amplitudes) != 1:
        raise ValueError("peak-conditioned profiles must share one response amplitude")
    if len(lengths) != 1:
        raise ValueError("peak-conditioned profiles must share one deformation domain")
    deformation_count = next(iter(lengths))
    if deformation_count <= 0:
        raise ValueError("material deformation domain must be nonempty")
    for peak, profile in items:
        if len(profile.loading) != len(profile.returning):
            raise ValueError("every peak-conditioned profile must have equal branches")
        if peak >= deformation_count:
            raise ValueError("historical peak lies outside material deformation domain")
    return PeakConditionedMaterialFamily(
        peak_profiles=items,
        amplitude=next(iter(amplitudes)),
        deformation_count=deformation_count,
    )


def _profile_for_peak(
    family: PeakConditionedMaterialFamily,
    historical_peak: int,
) -> MaterialCurveProfile:
    for peak, profile in family.peak_profiles:
        if peak == historical_peak:
            return profile
    raise ValueError("historical peak is not represented by this material family")


def _validate_index(family: PeakConditionedMaterialFamily, index: int) -> None:
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("deformation index must be an integer")
    if not 0 <= index < family.deformation_count:
        raise ValueError("deformation index lies outside material domain")


@dataclass(frozen=True)
class PeakHistoryMaterialState:
    deformation_index: int
    branch: MaterialBranch
    historical_peak: int
    response_sample: int


def peak_history_material_state(
    family: PeakConditionedMaterialFamily,
    deformation_index: int,
    branch: MaterialBranch,
    historical_peak: int,
) -> PeakHistoryMaterialState:
    """Construct one represented peak-conditioned material state."""
    _validate_index(family, deformation_index)
    _validate_index(family, historical_peak)
    if historical_peak < deformation_index:
        raise ValueError("historical peak cannot be below current deformation")
    profile = _profile_for_peak(family, historical_peak)
    if branch == LOADING:
        response = profile.loading[deformation_index]
    elif branch == RETURNING:
        response = profile.returning[deformation_index]
    else:
        raise ValueError("unknown material branch")
    return PeakHistoryMaterialState(
        deformation_index=deformation_index,
        branch=branch,
        historical_peak=historical_peak,
        response_sample=response,
    )


def advance_peak_history_material(
    family: PeakConditionedMaterialFamily,
    current: PeakHistoryMaterialState,
    next_index: int,
) -> PeakHistoryMaterialState:
    """Advance deformation while retaining the largest represented past index."""
    _validate_index(family, next_index)
    if current.historical_peak < current.deformation_index:
        raise ValueError("current state has invalid peak history")
    if next_index > current.deformation_index:
        branch = LOADING
    elif next_index < current.deformation_index:
        branch = RETURNING
    else:
        branch = current.branch
    new_peak = max(current.historical_peak, next_index)
    return peak_history_material_state(family, next_index, branch, new_peak)


def trace_peak_history_schedule(
    family: PeakConditionedMaterialFamily,
    schedule: tuple[int, ...] | list[int],
    initial_peak: int | None = None,
    initial_branch: MaterialBranch = LOADING,
) -> tuple[PeakHistoryMaterialState, ...]:
    """Trace one finite deformation history with explicit maximum-state memory."""
    indices = tuple(schedule)
    if not indices:
        raise ValueError("deformation schedule must be nonempty")
    first = indices[0]
    _validate_index(family, first)
    peak = first if initial_peak is None else initial_peak
    state = peak_history_material_state(family, first, initial_branch, peak)
    states = [state]
    for next_index in indices[1:]:
        state = advance_peak_history_material(family, state, next_index)
        states.append(state)
    return tuple(states)


def branch_bit_is_sufficient_for_family(
    family: PeakConditionedMaterialFamily,
) -> bool:
    """Whether response is independent of historical peak at fixed index/branch.

    Only represented peak/index combinations are compared.  ``False`` is a
    finite witness that ``(deformation_index, branch)`` is not a sufficient
    state description for this declared material law.
    """
    for index in range(family.deformation_count):
        admissible_peaks = [
            peak for peak, _profile in family.peak_profiles if peak >= index
        ]
        for branch in (LOADING, RETURNING):
            responses = {
                peak_history_material_state(family, index, branch, peak).response_sample
                for peak in admissible_peaks
            }
            if len(responses) > 1:
                return False
    return True
