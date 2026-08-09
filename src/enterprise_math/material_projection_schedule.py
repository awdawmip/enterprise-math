"""Projection-cadence pressure tests for the E001 integer oscillator.

A tempting assumption is that postponing projection must preserve at least as
much squared radius as projecting after every lift.  That is false because the
projection defects are rotated and mixed by later exact lifts.

This module compares two explicit schedules for the same rational rotation word:

* sequential: lift -> project after every step;
* batched: perform all exact lifts first, then project once by c**steps.

No monotone ordering between the two final squared radii is assumed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    integer_rotation_lift,
    projected_rotation_step,
    signed_project,
)


@dataclass(frozen=True)
class ProjectionScheduleComparison:
    """Final states and squared radii under two projection schedules."""

    initial_state: tuple[int, int]
    steps: int
    sequential_state: tuple[int, int]
    batched_state: tuple[int, int]
    sequential_norm_sq: int
    batched_norm_sq: int
    norm_sq_difference: int


def _validate_state(state: tuple[int, int]) -> None:
    x, y = state
    if isinstance(x, bool) or not isinstance(x, int):
        raise ValueError("state x must be an integer")
    if isinstance(y, bool) or not isinstance(y, int):
        raise ValueError("state y must be an integer")


def sequential_rotation_projection(
    state: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[int, int]:
    """Project toward zero after every exact lift."""
    _validate_state(state)
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    current = state
    for _ in range(steps):
        current = projected_rotation_step(
            *current, rotation, TOWARD_ZERO
        ).after
    return current


def batched_rotation_projection(
    state: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[int, int]:
    """Apply ``steps`` exact integer lifts, then one projection by c**steps."""
    _validate_state(state)
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    raw = state
    for _ in range(steps):
        raw = integer_rotation_lift(*raw, rotation)
    divisor = rotation.c**steps
    return (
        signed_project(raw[0], divisor, TOWARD_ZERO),
        signed_project(raw[1], divisor, TOWARD_ZERO),
    )


def compare_projection_schedules(
    state: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> ProjectionScheduleComparison:
    """Compare sequential and batched schedules without imposing an ordering."""
    sequential = sequential_rotation_projection(state, rotation, steps)
    batched = batched_rotation_projection(state, rotation, steps)
    sequential_norm = sequential[0] * sequential[0] + sequential[1] * sequential[1]
    batched_norm = batched[0] * batched[0] + batched[1] * batched[1]
    return ProjectionScheduleComparison(
        initial_state=state,
        steps=steps,
        sequential_state=sequential,
        batched_state=batched,
        sequential_norm_sq=sequential_norm,
        batched_norm_sq=batched_norm,
        norm_sq_difference=sequential_norm - batched_norm,
    )
