"""Intrinsic peak tracer for projected Pythagorean material waves.

For any integer ``x`` and ``y>=0`` under toward-zero projected rotation, write

    raw_y = b*x + a*y = c*y + m,
    m = b*x - (c-a)*y.

The rise margin ``m`` classifies the next represented y exactly, but the zero
axis has an additional toward-zero plateau on its negative side:

* ``m>=c``                         iff ``y_next>y``;
* ``y>0`` and ``0<=m<c``          iff ``y_next==y``;
* ``y>0`` and ``m<0``             iff ``y_next<y``;
* ``y=0`` and ``-c<m<c``          iff ``y_next==0``;
* ``y=0`` and ``m<=-c``           iff ``y_next<0``.

The ``y=0`` negative-margin plateau is not a numerical accident.  It is exactly
the signed toward-zero quotient dead zone: negative raw values with magnitude
strictly below one divisor quantum still project to zero.

A discrete step may cross from ``x>0`` to ``x<0`` while y still rises.  The
intrinsic peak tracer therefore does not stop merely because the x sign changes;
it stops at the first represented y plateau or fall.  If ``x<0,y>0`` the margin
is negative and the next y strictly falls; if ``x<0,y=0`` a finite zero-axis
plateau may occur, which is already a non-rise and therefore also terminates the
peak trace.  No angle, real sine, or pi/2 target is used.
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
    """Classify the next toward-zero projected y move exactly for ``y>=0``."""
    if y < 0:
        raise ValueError("peak tracer requires y>=0 before the turning point")
    report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
    _next_x, next_y = report.after
    margin = rotation.b * x - (rotation.c - rotation.a) * y

    if margin >= rotation.c:
        status = RISE
        if not next_y > y:
            raise AssertionError("rise margin failed strict-y prediction")
    elif y == 0:
        if margin > -rotation.c:
            status = PLATEAU
            if next_y != 0:
                raise AssertionError("zero-axis dead-zone margin failed plateau prediction")
        else:
            status = FALL
            if not next_y < 0:
                raise AssertionError("zero-axis negative-quantum margin failed fall prediction")
    elif margin >= 0:
        status = PLATEAU
        if next_y != y:
            raise AssertionError("positive-y plateau margin failed equal-y prediction")
    else:
        status = FALL
        if not next_y < y:
            raise AssertionError("positive-y negative margin failed falling-y prediction")

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
    """Trace from ``(A,0)`` until the first plateau/fall and return the sampled peak."""
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

    # While x>0 and y>=0, x_next<x.  Once x becomes negative, either y>0 and
    # the next y step falls, or y=0 and the zero-axis signed projection is a
    # plateau/fall.  A+2 steps therefore remain a finite structural guard.
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
