"""Intrinsic quarter-wave turning certificate for projected Pythagorean material basis.

For a first-quadrant integer state ``x>=0,y>=0`` under toward-zero projected
Pythagorean rotation,

    raw_y = b*x + a*y.

Compare it with ``c*y`` through the integer rise margin

    m = b*x - (c-a)*y.

Then exactly:

* ``m>=c``  iff ``y_next>y``;
* ``0<=m<c`` iff ``y_next==y``;
* ``m<0``   iff ``y_next<y``.

No angle or sine is needed to detect the finite quarter-wave turning/plateau.
Also, whenever ``x>0,y>=0``, the projected next x is strictly smaller than x,
so a first-quadrant rising run cannot continue indefinitely.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import TOWARD_ZERO, PythagoreanRotation, projected_rotation_step

RISE = "RISE"
PLATEAU = "PLATEAU"
FALL = "FALL"


@dataclass(frozen=True)
class QuarterWaveStep:
    """One intrinsic rise/fall certificate before an integer oscillator step."""

    before: tuple[int, int]
    after: tuple[int, int]
    rise_margin: int
    y_status: str
    x_strictly_decreases_if_positive: bool


@dataclass(frozen=True)
class QuarterWaveTrace:
    """Finite samples through the first non-rising y step."""

    initial_amplitude: int
    states: tuple[tuple[int, int], ...]
    steps: tuple[QuarterWaveStep, ...]
    first_nonrise_step: int | None
    termination_status: str | None


def quarter_wave_step(
    x: int,
    y: int,
    rotation: PythagoreanRotation,
) -> QuarterWaveStep:
    """Return exact rise-margin classification for one nonnegative state."""
    if x < 0 or y < 0:
        raise ValueError("quarter-wave certificate requires x,y>=0")
    report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
    next_x, next_y = report.after
    margin = rotation.b * x - (rotation.c - rotation.a) * y
    if margin >= rotation.c:
        status = RISE
        if not next_y > y:
            raise AssertionError("rise margin failed to predict strict y increase")
    elif margin >= 0:
        status = PLATEAU
        if next_y != y:
            raise AssertionError("plateau margin failed to predict equal y")
    else:
        status = FALL
        if not next_y < y:
            raise AssertionError("negative rise margin failed to predict y decrease")

    x_decreases = True
    if x > 0 and y >= 0 and not next_x < x:
        x_decreases = False
        raise AssertionError("positive first-quadrant x failed to strictly decrease")
    return QuarterWaveStep(
        before=(x, y),
        after=report.after,
        rise_margin=margin,
        y_status=status,
        x_strictly_decreases_if_positive=x_decreases,
    )


def intrinsic_quarter_wave(
    amplitude: int,
    rotation: PythagoreanRotation,
) -> QuarterWaveTrace:
    """Start at (A,0) and stop immediately after the first non-rising y step."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    state = (amplitude, 0)
    states = [state]
    steps: list[QuarterWaveStep] = []
    first_nonrise = None
    termination = None

    # x strictly decreases while positive in the certified quadrant, so A+1
    # attempts are enough to encounter a non-rise or leave the quadrant.
    for step_index in range(1, amplitude + 2):
        x, y = state
        if x < 0 or y < 0:
            break
        report = quarter_wave_step(x, y, rotation)
        steps.append(report)
        state = report.after
        states.append(state)
        if report.y_status != RISE:
            first_nonrise = step_index
            termination = report.y_status
            break
        if state[0] < 0 or state[1] < 0:
            break

    return QuarterWaveTrace(
        initial_amplitude=amplitude,
        states=tuple(states),
        steps=tuple(steps),
        first_nonrise_step=first_nonrise,
        termination_status=termination,
    )
