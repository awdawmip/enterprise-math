"""Explicit calibration boundary from measured response counts to material samples.

E001 keeps experimental measurement coordinates separate from the finite
``MaterialCurveProfile`` response scale.  A fitted/measured stress count is not
a kinematic return fraction by itself.  This module makes the first conversion
explicit:

    measured response count on a declared unit/scale
        -> fixed finite response interval
        -> integer sample on 0..A.

For source interval ``[L,U]`` and model amplitude ``A``, nearest projection is

    q = floor((2*(v-L)*A + (U-L)) / (2*(U-L))).

The doubled signed projection detail

    delta2 = 2*(v-L)*A - 2*(U-L)*q

is retained, so the calibration loss is explicit and bounded by the source
interval width.  This is a declared modeling/calibration map.  It does not turn
a stress unit into velocity, impulse, energy, or restitution by naming alone.

Two calibrated branches may be assembled into a ``MaterialCurveProfile`` only
when they use exactly the same calibration and exactly the same measured
deformation grid.  No interpolation or branch fabrication is performed here.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_measurement import FiniteMaterialDataset, FiniteMeasurementAxis
from .material_response import MaterialCurveProfile, explicit_material_curve_profile


@dataclass(frozen=True)
class ResponseCalibration:
    source_axis_name: str
    source_unit: str
    source_scale_factor: int
    lower_response_count: int
    upper_response_count: int
    model_amplitude: int

    def __post_init__(self) -> None:
        if not isinstance(self.source_axis_name, str) or not self.source_axis_name:
            raise ValueError("source_axis_name must be a nonempty string")
        if not isinstance(self.source_unit, str) or not self.source_unit:
            raise ValueError("source_unit must be a nonempty string")
        for name, value in (
            ("source_scale_factor", self.source_scale_factor),
            ("model_amplitude", self.model_amplitude),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        for name, value in (
            ("lower_response_count", self.lower_response_count),
            ("upper_response_count", self.upper_response_count),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if self.upper_response_count <= self.lower_response_count:
            raise ValueError("response calibration interval must have positive width")


@dataclass(frozen=True)
class CalibratedResponseSample:
    source_count: int
    model_sample: int
    doubled_projection_detail: int


def response_calibration_from_axis(
    axis: FiniteMeasurementAxis,
    model_amplitude: int,
    lower_response_count: int | None = None,
    upper_response_count: int | None = None,
) -> ResponseCalibration:
    """Freeze one measured-response domain before mapping it onto 0..A."""
    if isinstance(model_amplitude, bool) or not isinstance(model_amplitude, int) or model_amplitude <= 0:
        raise ValueError("model_amplitude must be a positive integer")
    lower = axis.lower_count if lower_response_count is None else lower_response_count
    upper = axis.upper_count if upper_response_count is None else upper_response_count
    if not axis.contains(lower) or not axis.contains(upper):
        raise ValueError("calibration response bounds must lie on the declared measurement axis")
    return ResponseCalibration(
        source_axis_name=axis.name,
        source_unit=axis.unit,
        source_scale_factor=axis.scale_factor,
        lower_response_count=lower,
        upper_response_count=upper,
        model_amplitude=model_amplitude,
    )


def calibrate_response_count(
    count: int,
    calibration: ResponseCalibration,
) -> CalibratedResponseSample:
    """Project one measured count onto 0..A and retain the exact finite detail."""
    if isinstance(count, bool) or not isinstance(count, int):
        raise ValueError("count must be an integer")
    lower = calibration.lower_response_count
    upper = calibration.upper_response_count
    if not lower <= count <= upper:
        raise ValueError("response count lies outside the frozen calibration interval")
    span = upper - lower
    offset = count - lower
    doubled_raw = 2 * offset * calibration.model_amplitude
    denominator = 2 * span
    sample = (doubled_raw + span) // denominator
    detail2 = doubled_raw - denominator * sample
    if not 0 <= sample <= calibration.model_amplitude:
        raise AssertionError("calibrated sample escaped model response scale")
    if not -span <= detail2 < span:
        raise AssertionError("nearest calibration detail escaped half-cell bound")
    return CalibratedResponseSample(
        source_count=count,
        model_sample=sample,
        doubled_projection_detail=detail2,
    )


@dataclass(frozen=True)
class CalibratedMeasurementBranch:
    source_id: str
    deformation_counts: tuple[int, ...]
    response_counts: tuple[int, ...]
    model_samples: tuple[int, ...]
    doubled_projection_details: tuple[int, ...]
    calibration: ResponseCalibration


def calibrate_measurement_branch(
    dataset: FiniteMaterialDataset,
    calibration: ResponseCalibration,
) -> CalibratedMeasurementBranch:
    """Apply one frozen response calibration without changing deformation coordinates."""
    axis = dataset.response_axis
    if (
        axis.name != calibration.source_axis_name
        or axis.unit != calibration.source_unit
        or axis.scale_factor != calibration.source_scale_factor
    ):
        raise ValueError("dataset response axis does not match calibration provenance")
    reports = tuple(
        calibrate_response_count(count, calibration)
        for count in dataset.responses
    )
    return CalibratedMeasurementBranch(
        source_id=dataset.source_id,
        deformation_counts=dataset.deformations,
        response_counts=dataset.responses,
        model_samples=tuple(report.model_sample for report in reports),
        doubled_projection_details=tuple(
            report.doubled_projection_detail for report in reports
        ),
        calibration=calibration,
    )


@dataclass(frozen=True)
class EmpiricalMaterialProfileAssembly:
    loading_source_id: str
    returning_source_id: str
    deformation_counts: tuple[int, ...]
    calibration: ResponseCalibration
    profile: MaterialCurveProfile


def assemble_calibrated_empirical_profile(
    loading: CalibratedMeasurementBranch,
    returning: CalibratedMeasurementBranch,
) -> EmpiricalMaterialProfileAssembly:
    """Assemble explicit empirical branches only on an identical measured grid."""
    if loading.calibration != returning.calibration:
        raise ValueError("loading and returning branches must share one frozen calibration")
    if loading.deformation_counts != returning.deformation_counts:
        raise ValueError("loading and returning branches require an identical deformation grid")
    profile = explicit_material_curve_profile(
        loading.model_samples,
        returning.model_samples,
        loading.calibration.model_amplitude,
    )
    return EmpiricalMaterialProfileAssembly(
        loading_source_id=loading.source_id,
        returning_source_id=returning.source_id,
        deformation_counts=loading.deformation_counts,
        calibration=loading.calibration,
        profile=profile,
    )
