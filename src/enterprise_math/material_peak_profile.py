"""Build an E001 material curve directly from the intrinsic projected-wave peak.

The base deformation samples are the y-coordinates from ``(A,0)`` through the
last strictly rising/peak state detected by the integer rise-margin certificate.
No external step count, angle, sine table, or pi/2 phase target is supplied.

The resulting monotone base can then be transformed by the existing integer
hardening/softening/retention material operators.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation
from .material_peak_wave import ProjectedPeakTrace, projected_peak_trace
from .material_response import MaterialCurveProfile, material_curve_profile


@dataclass(frozen=True)
class IntrinsicPeakMaterialProfile:
    """Intrinsic oscillator peak trace plus the derived material curve."""

    rotation: PythagoreanRotation
    amplitude: int
    peak_trace: ProjectedPeakTrace
    base_samples: tuple[int, ...]
    material_profile: MaterialCurveProfile


def intrinsic_peak_base_samples(
    amplitude: int,
    rotation: PythagoreanRotation,
) -> tuple[int, ...]:
    """Return y samples through the peak state, excluding the first non-rising after-state."""
    trace = projected_peak_trace(amplitude, rotation)
    if trace.first_nonrise_step == 0:
        return (0,)
    # The non-rising step begins at peak_state and appends one after-state.  All
    # states before that final after-state, including peak_state, form the base.
    base_states = trace.states[:-1]
    samples = tuple(state[1] for state in base_states)
    if not samples:
        raise AssertionError("intrinsic peak trace produced an empty material base")
    if samples[0] != 0:
        raise AssertionError("intrinsic peak material base must start at zero")
    if any(left >= right for left, right in zip(samples, samples[1:])):
        raise AssertionError("intrinsic peak material base is not strictly increasing")
    if samples[-1] != trace.peak_state[1]:
        raise AssertionError("intrinsic peak base lost the certified peak sample")
    return samples


def intrinsic_peak_material_profile(
    amplitude: int,
    rotation: PythagoreanRotation,
    loading_power: int = 1,
    return_power: int = 1,
    return_retention: int | None = None,
) -> IntrinsicPeakMaterialProfile:
    """Generate a full material curve from the integer oscillator's own turning point."""
    trace = projected_peak_trace(amplitude, rotation)
    samples = intrinsic_peak_base_samples(amplitude, rotation)
    profile = material_curve_profile(
        samples,
        amplitude=amplitude,
        loading_power=loading_power,
        return_power=return_power,
        return_retention=return_retention,
    )
    return IntrinsicPeakMaterialProfile(
        rotation=rotation,
        amplitude=amplitude,
        peak_trace=trace,
        base_samples=samples,
        material_profile=profile,
    )
