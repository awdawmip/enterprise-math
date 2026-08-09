"""Exact amplitude-to-phase budget for the projected Pythagorean material wave.

Use the standard rational Pythagorean family

    R_m = (m^2-1, 2m, m^2+1),    m>=2.

Starting from ``(A,0)``, the first represented transverse coordinate is

    y_1 = floor(2*m*A/(m^2+1)).

Hence a nonzero transverse mode exists exactly when ``m<2*A``.  The sharp last
live parameter is ``m=2*A-1`` and it produces exactly one transverse quantum;
``m>=2*A`` is a zero-start dead zone.

During the canonical peak trace every strict RISE step decreases the integer
``x`` coordinate, so there can be at most ``A`` strict rises from amplitude A.
This gives a purely finite upper phase budget, independent of any external angle
or sine comparison.

The linear scaling is constructive.  For ``A>=2`` choose ``m=A``.  For

    n = 0,...,ceil(A/2)-1

the projected state is exactly ``(A-n,n)`` and the next state exactly
``(A-n-1,n+1)``.  Thus the trace has exactly ``ceil(A/2)`` strict rises before its
first non-rise.  The Pythagorean projected family therefore realizes phase count
on the same linear scale as amplitude precision:

    ceil(A/2) <= attainable strict-rise count <= A.

This is a finite representability statement, not a claim that phase count equals
a continuum angle resolution.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation, projected_rotation_step
from .material_peak_wave import RISE, ProjectedPeakTrace, projected_peak_trace


def pythagorean_family_rotation(parameter: int) -> PythagoreanRotation:
    if isinstance(parameter, bool) or not isinstance(parameter, int) or parameter < 2:
        raise ValueError("parameter must be an integer >=2")
    m = parameter
    return PythagoreanRotation(m * m - 1, 2 * m, m * m + 1)


def first_transverse_quantum(amplitude: int, parameter: int) -> int:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    rotation = pythagorean_family_rotation(parameter)
    return projected_rotation_step(amplitude, 0, rotation).after[1]


def strict_rise_count(trace: ProjectedPeakTrace) -> int:
    return sum(step.status == RISE for step in trace.steps)


@dataclass(frozen=True)
class PythagoreanPhaseBudgetReport:
    amplitude: int
    parameter: int
    first_transverse_quantum: int
    strict_rises: int
    finite_upper_bound: int
    live_transverse_mode: bool


def pythagorean_phase_budget(amplitude: int, parameter: int) -> PythagoreanPhaseBudgetReport:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    rotation = pythagorean_family_rotation(parameter)
    trace = projected_peak_trace(amplitude, rotation)
    rises = strict_rise_count(trace)
    if rises > amplitude:
        raise AssertionError("projected peak trace exceeded its integer x phase budget")
    first = first_transverse_quantum(amplitude, parameter)
    return PythagoreanPhaseBudgetReport(
        amplitude=amplitude,
        parameter=parameter,
        first_transverse_quantum=first,
        strict_rises=rises,
        finite_upper_bound=amplitude,
        live_transverse_mode=first > 0,
    )


def sharp_last_live_parameter(amplitude: int) -> int:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 2:
        raise ValueError("amplitude must be at least 2 for the m>=2 family")
    return 2 * amplitude - 1


def balanced_linear_phase_trace(amplitude: int) -> ProjectedPeakTrace:
    """Return the explicit m=A construction with exactly ceil(A/2) strict rises."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 2:
        raise ValueError("amplitude must be at least 2")
    trace = projected_peak_trace(amplitude, pythagorean_family_rotation(amplitude))
    expected_rises = (amplitude + 1) // 2
    if strict_rise_count(trace) != expected_rises:
        raise AssertionError("m=A projected phase construction lost its exact rise count")
    for n in range(expected_rises + 1):
        if trace.states[n] != (amplitude - n, n):
            raise AssertionError("m=A phase construction left the exact diagonal staircase")
    return trace
