"""Corrected intrinsic peak tracer for projected Pythagorean material waves.

The y rise-margin identity does not require x>=0.  For any integer x and y>=0,

    m = b*x - (c-a)*y

classifies the next toward-zero projected y exactly:

* m>=c       <=> y_next>y;
* 0<=m<c     <=> y_next==y;
* m<0        <=> y_next<y.

A discrete step can cross from x>0 to x<0 while y still rises.  Therefore an
intrinsic peak tracer must not stop merely because the first-quadrant x sign was
lost.  Once x<0 and y>=0, however, m<0 automatically, so the next step is a
strict fall.  Starting from (A,0), positive x strictly decreases while y>=0; a
first non-rise is therefore reached after finitely many integer steps without
using an angle or pi/2 target.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import TOWARD_ZERO, PythagoreanRotation, projected_rotation_step

RISE = "RISE"
PLATEAU = "PLATEAU"
FALL = "FALL"


@dataclass(frozen=True)
class PeakStep:
    """One exact y-direction certificate before a projected oscillator step."""

    before: tuple[int, int]
    after: tuple[int, int]
    rise_margin: int
    status: str


@dataclass(frozen=True)
class ProjectedPeakTrace:
    """Integer oscillator states through the first non-rising y transition."""

    amplitude: int
    states: tuple[tuple[int, int], ...]
    steps: tuple[PeakStep, ...]
    peak_state: tuple[int, int]
    first_nonrise_step: int
    termination_status: str


def peak_step(
    x: int,
    y: int,
    rotation: PythagoreanRotation,
) -> PeakStep:
    """Classify the next projected y move exactly for y>=0."""
    if y < 0:
        raise ValueError("peak tracer requires y>=0 before the turning point")
    report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
    next_x, next_y = report.after
    margin = rotation.b * x - (rotation.c - rotation.a) * y
    if margin >= rotation.c:
        status = RISE
        if not next_y > y:
            raise AssertionError("rise margin failed strict-y prediction")
    elif margin >= 0:
        status = PLATEAU
        if next_y != y:
            raise AssertionError("plateau margin failed equal-y prediction")
    else:
        status = FALL
        if not next_y < y:
            raise AssertionError("negative margin failed falling-y prediction")
    return PeakStep(
        before=(x, y),
        after=report.after,
        rise_margin=margin,
        status=status,
    )


def projected_peak_trace(
    amplitude: int,
    rotation: PythagoreanRotation,
) -> ProjectedPeakTrace:
    """Trace from (A,0) until the first plateau/fall and return the sampled peak."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    if amplitude == 0:
        return ProjectedPeakTrace(
            amplitude=0,
            states=((0, 0),),
            steps=(),
            peak_state=(0, 0),
            first_nonrise_step=0,
            termination_status=PLATEAU,
        )

    state = (amplitude, 0)
    states = [state]
    steps: list[PeakStep] = []

    # While x>0 and y>=0, x_next<x, so after at most A steps x<=0.
    # If x<0 while y is still nonnegative, the next margin is automatically
    # negative.  A+2 steps therefore suffice as a structural guard.
    for step_index in range(1, amplitude + 3):
        x, y = state
        if y < 0:
            raise AssertionError("projected peak trace crossed below y=0 before detecting a turn")
        report = peak_step(x, y, rotation)
        steps.append(report)
        states.append(report.after)
        if report.status != RISE:
            peak_state = report.before
            return ProjectedPeakTrace(
                amplitude=amplitude,
                states=tuple(states),
                steps=tuple(steps),
                peak_state=peak_state,
                first_nonrise_step=step_index,
                termination_status=report.status,
            )
        state = report.after

    raise AssertionError("projected peak trace exceeded its finite integer guard")
