"""Finite history state for E001 loading/return material curves.

The same deformation index may produce a different response sample depending on
whether that index is reached while loading or returning.  This module makes
that branch memory explicit; it does not prescribe how a collision geometry
must be converted into deformation or how a response sample changes velocity.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import MaterialCurveProfile

LOADING = "LOADING"
RETURNING = "RETURNING"
MaterialBranch = str


@dataclass(frozen=True)
class MaterialHistoryState:
    """One finite material state at a discrete deformation index."""

    deformation_index: int
    branch: MaterialBranch
    response_sample: int


def _validate_profile(profile: MaterialCurveProfile) -> None:
    if len(profile.loading) != len(profile.returning):
        raise ValueError("material branches must have equal length")
    if not profile.loading:
        raise ValueError("material profile must contain at least one sample")


def _validate_index(profile: MaterialCurveProfile, index: int) -> None:
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("deformation index must be an integer")
    if not 0 <= index < len(profile.loading):
        raise ValueError("deformation index lies outside the material curve")


def material_state(
    profile: MaterialCurveProfile,
    deformation_index: int,
    branch: MaterialBranch,
) -> MaterialHistoryState:
    """Construct one explicit branch-aware material state."""
    _validate_profile(profile)
    _validate_index(profile, deformation_index)
    if branch == LOADING:
        response = profile.loading[deformation_index]
    elif branch == RETURNING:
        response = profile.returning[deformation_index]
    else:
        raise ValueError("unknown material branch")
    return MaterialHistoryState(deformation_index, branch, response)


def advance_material_deformation(
    profile: MaterialCurveProfile,
    current: MaterialHistoryState,
    next_index: int,
) -> MaterialHistoryState:
    """Advance to one declared deformation index and update path memory.

    Increasing deformation selects LOADING; decreasing deformation selects
    RETURNING.  Holding the same deformation preserves the existing branch.
    """
    _validate_profile(profile)
    _validate_index(profile, current.deformation_index)
    _validate_index(profile, next_index)
    if current.branch not in (LOADING, RETURNING):
        raise ValueError("current material state has an unknown branch")

    if next_index > current.deformation_index:
        branch = LOADING
    elif next_index < current.deformation_index:
        branch = RETURNING
    else:
        branch = current.branch
    return material_state(profile, next_index, branch)


def trace_deformation_schedule(
    profile: MaterialCurveProfile,
    schedule: tuple[int, ...] | list[int],
    initial_branch: MaterialBranch = LOADING,
) -> tuple[MaterialHistoryState, ...]:
    """Trace one finite deformation-index schedule without hidden interpolation."""
    _validate_profile(profile)
    if not schedule:
        raise ValueError("deformation schedule must be nonempty")
    first = schedule[0]
    state = material_state(profile, first, initial_branch)
    states = [state]
    for next_index in schedule[1:]:
        state = advance_material_deformation(profile, state, next_index)
        states.append(state)
    return tuple(states)


def history_response_sum(states: tuple[MaterialHistoryState, ...] | list[MaterialHistoryState]) -> int:
    """Return a finite unsigned sum of visited response samples."""
    total = 0
    for state in states:
        if state.response_sample < 0:
            raise ValueError("material response sample must be non-negative")
        total += state.response_sample
    return total
