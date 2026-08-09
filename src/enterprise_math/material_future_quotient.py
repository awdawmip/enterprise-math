"""Future-language sufficiency of the E001 material branch bit.

A loading/returning branch distinction is genuine finite history, but it is not
necessarily relevant to every future task.  If a future deformation schedule
immediately changes index, the next direction overwrites the current branch.  A
schedule that can hold the current deformation can preserve and observe the
branch distinction.

This module is an E001 specialization of future-compatible quotient reasoning;
it does not replace the general A2/P023 theory.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import (
    LOADING,
    RETURNING,
    MaterialBranch,
    material_state,
    trace_deformation_schedule,
)
from .material_response import MaterialCurveProfile


@dataclass(frozen=True)
class MaterialFutureSignature:
    """Terminal response signature over one finite language of index schedules."""

    initial_index: int
    initial_branch: MaterialBranch
    terminal_responses: tuple[int, ...]
    terminal_branches: tuple[MaterialBranch, ...]


def _validate_schedules(
    initial_index: int,
    schedules: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
) -> tuple[tuple[int, ...], ...]:
    if isinstance(initial_index, bool) or not isinstance(initial_index, int):
        raise ValueError("initial_index must be an integer")
    normalized = tuple(tuple(schedule) for schedule in schedules)
    for schedule in normalized:
        if not schedule:
            raise ValueError("future schedule must be nonempty")
        if schedule[0] != initial_index:
            raise ValueError("every future schedule must start at initial_index")
    return normalized


def material_future_signature(
    profile: MaterialCurveProfile,
    initial_index: int,
    initial_branch: MaterialBranch,
    schedules: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
) -> MaterialFutureSignature:
    """Evaluate terminal material states for a declared finite schedule language."""
    normalized = _validate_schedules(initial_index, schedules)
    # Validate the initial state/branch even for an empty language.
    material_state(profile, initial_index, initial_branch)

    terminal_responses: list[int] = []
    terminal_branches: list[MaterialBranch] = []
    for schedule in normalized:
        trace = trace_deformation_schedule(profile, schedule, initial_branch)
        terminal = trace[-1]
        terminal_responses.append(terminal.response_sample)
        terminal_branches.append(terminal.branch)

    return MaterialFutureSignature(
        initial_index=initial_index,
        initial_branch=initial_branch,
        terminal_responses=tuple(terminal_responses),
        terminal_branches=tuple(terminal_branches),
    )


def branch_bit_future_equivalent(
    profile: MaterialCurveProfile,
    initial_index: int,
    schedules: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
    include_terminal_branch: bool = False,
) -> bool:
    """Whether LOADING/RETURNING can be merged for the declared terminal task."""
    loading = material_future_signature(
        profile, initial_index, LOADING, schedules
    )
    returning = material_future_signature(
        profile, initial_index, RETURNING, schedules
    )
    if loading.terminal_responses != returning.terminal_responses:
        return False
    if include_terminal_branch and loading.terminal_branches != returning.terminal_branches:
        return False
    return True
