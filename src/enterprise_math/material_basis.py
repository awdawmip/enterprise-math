"""Quarter-wave extraction and finite diagnostics for E001 material bases.

Compression/return experiments need a monotone deformation basis before they
need a globally periodic trigonometric function.  This module extracts and
compares three intrinsic integer bases without using real-valued sine.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    digital_circle_quarter,
    projected_rotation_step,
    recurrence_sine_samples,
)

ROTATION_PHASE = "ROTATION_PHASE"
RECURRENCE_PHASE = "RECURRENCE_PHASE"
DIGITAL_X_PHASE = "DIGITAL_X_PHASE"


@dataclass(frozen=True)
class MaterialBasisDiagnostics:
    """Finite shape diagnostics of one nonnegative quarter-wave basis."""

    phase_kind: str
    samples: tuple[int, ...]
    sample_count: int
    distinct_sample_count: int
    plateau_count: int
    peak: int
    peak_defect_from_amplitude: int
    monotone_nondecreasing: bool


def _validate_amplitude(amplitude: int) -> None:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")


def diagnose_material_basis(
    samples: tuple[int, ...] | list[int],
    amplitude: int,
    phase_kind: str,
) -> MaterialBasisDiagnostics:
    """Return finite monotonicity, plateau, and peak diagnostics."""
    _validate_amplitude(amplitude)
    values = tuple(samples)
    if not values:
        raise ValueError("material basis must be nonempty")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("material basis samples must be non-negative integers")
        if value > amplitude:
            raise ValueError("material basis sample exceeds amplitude")
    monotone = all(left <= right for left, right in zip(values, values[1:]))
    plateaus = sum(left == right for left, right in zip(values, values[1:]))
    peak = max(values)
    return MaterialBasisDiagnostics(
        phase_kind=phase_kind,
        samples=values,
        sample_count=len(values),
        distinct_sample_count=len(set(values)),
        plateau_count=plateaus,
        peak=peak,
        peak_defect_from_amplitude=amplitude - peak,
        monotone_nondecreasing=monotone,
    )


def rotation_quarter_basis(
    amplitude: int,
    rotation: PythagoreanRotation,
    max_steps: int = 10_000,
) -> MaterialBasisDiagnostics:
    """Extract y-samples until the projected x-coordinate first becomes nonpositive.

    The x sign is retained as an intrinsic phase witness, so this does not choose
    the quarter-wave endpoint by comparing to a hidden real angle.
    """
    _validate_amplitude(amplitude)
    if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps <= 0:
        raise ValueError("max_steps must be a positive integer")

    x, y = amplitude, 0
    samples = [y]
    if x == 0:
        return diagnose_material_basis(samples, amplitude, ROTATION_PHASE)

    for _ in range(max_steps):
        report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
        x, y = report.after
        if y < 0:
            raise AssertionError("rotation left the nonnegative quarter before x crossing")
        samples.append(y)
        if x <= 0:
            return diagnose_material_basis(samples, amplitude, ROTATION_PHASE)
        if (x, y) == (0, 0):
            return diagnose_material_basis(samples, amplitude, ROTATION_PHASE)
    raise ValueError("rotation quarter endpoint not reached within max_steps")


def recurrence_quarter_basis(
    amplitude: int,
    rotation: PythagoreanRotation,
    max_samples: int = 10_000,
) -> MaterialBasisDiagnostics:
    """Extract the maximal initial nondecreasing nonnegative recurrence prefix."""
    _validate_amplitude(amplitude)
    if isinstance(max_samples, bool) or not isinstance(max_samples, int) or max_samples < 2:
        raise ValueError("max_samples must be an integer >=2")

    raw = recurrence_sine_samples(amplitude, rotation, max_samples, TOWARD_ZERO)
    prefix = [raw[0]]
    for value in raw[1:]:
        if value < 0 or value < prefix[-1]:
            break
        if value > amplitude:
            raise AssertionError("recurrence quarter sample exceeded amplitude")
        prefix.append(value)
    return diagnose_material_basis(prefix, amplitude, RECURRENCE_PHASE)


def digital_circle_y_basis(amplitude: int) -> MaterialBasisDiagnostics:
    """Use the inward root-basin circle y-coordinate under integer x-phase."""
    _validate_amplitude(amplitude)
    samples = tuple(y for _x, y in digital_circle_quarter(amplitude))
    return diagnose_material_basis(samples, amplitude, DIGITAL_X_PHASE)
