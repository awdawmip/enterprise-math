"""Integer-only fitting helpers for E001 finite material curves.

The fitter is deliberately narrow. Experimental observations are first
represented as integers on their declared input/output scales. A candidate
loading curve is then built entirely from existing Enterprise Math primitives:

* nearest finite interval projection of deformation to ``0..A``;
* scale-preserving integer root ``G_r`` on the input coordinate;
* root-basin quarter-circle complement (a finite versine-like basis);
* scale-preserving integer hardening ``H_p`` on the output;
* one integer output-scale calibration.

This is an engineering benchmark family, not a universal constitutive law.
Continuous material models remain external baselines and may outperform it.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .material_response import hardening_sample, softening_sample


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_natural(name: str, value: int) -> None:
    _require_integer(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def project_interval_nearest(value: int, lower: int, upper: int, amplitude: int) -> int:
    """Project one integer observation from ``[lower,upper]`` onto ``0..A``."""
    _require_integer("value", value)
    _require_integer("lower", lower)
    _require_integer("upper", upper)
    _require_positive("amplitude", amplitude)
    if upper <= lower:
        raise ValueError("upper must be strictly greater than lower")
    if value < lower or value > upper:
        raise ValueError("value must lie in the declared interval")
    span = upper - lower
    offset = value - lower
    return (2 * offset * amplitude + span) // (2 * span)


def root_basin_versine_sample(
    deformation: int,
    lower: int,
    upper: int,
    amplitude: int,
    input_root_power: int,
    output_hardening_power: int,
) -> int:
    """Return one finite root-basin/versine loading sample on scale ``0..A``."""
    _require_positive("input_root_power", input_root_power)
    _require_positive("output_hardening_power", output_hardening_power)
    k = project_interval_nearest(deformation, lower, upper, amplitude)
    softened = softening_sample(k, amplitude, input_root_power)
    radius_sq = amplitude * amplitude
    remainder_sq = radius_sq - softened * softened
    if remainder_sq < 0:
        raise AssertionError("softened input escaped the finite amplitude disk")
    versine = amplitude - isqrt(remainder_sq)
    return hardening_sample(versine, amplitude, output_hardening_power)


def root_basin_versine_basis(
    deformations: tuple[int, ...] | list[int],
    amplitude: int,
    input_root_power: int,
    output_hardening_power: int,
) -> tuple[int, ...]:
    _require_positive("amplitude", amplitude)
    values = tuple(deformations)
    if len(values) < 2:
        raise ValueError("at least two deformation samples are required")
    for value in values:
        _require_integer("deformation sample", value)
    if tuple(sorted(values)) != values:
        raise ValueError("deformation samples must be non-decreasing")
    lower = values[0]
    upper = values[-1]
    if lower == upper:
        raise ValueError("deformation interval must have positive width")
    return tuple(
        root_basin_versine_sample(
            value,
            lower,
            upper,
            amplitude,
            input_root_power,
            output_hardening_power,
        )
        for value in values
    )


def predict_scaled_basis(
    basis: tuple[int, ...] | list[int], amplitude: int, output_scale: int
) -> tuple[int, ...]:
    _require_positive("amplitude", amplitude)
    _require_natural("output_scale", output_scale)
    result = []
    for sample in basis:
        _require_natural("basis sample", sample)
        if sample > amplitude:
            raise ValueError("basis sample must not exceed amplitude")
        result.append((2 * output_scale * sample + amplitude) // (2 * amplitude))
    return tuple(result)


def squared_error(
    targets: tuple[int, ...] | list[int], predictions: tuple[int, ...] | list[int]
) -> int:
    if len(targets) != len(predictions):
        raise ValueError("targets and predictions must have equal length")
    total = 0
    for target, prediction in zip(targets, predictions, strict=True):
        _require_natural("target", target)
        _require_natural("prediction", prediction)
        total += (target - prediction) ** 2
    return total


def absolute_error(
    targets: tuple[int, ...] | list[int], predictions: tuple[int, ...] | list[int]
) -> int:
    if len(targets) != len(predictions):
        raise ValueError("targets and predictions must have equal length")
    total = 0
    for target, prediction in zip(targets, predictions, strict=True):
        _require_natural("target", target)
        _require_natural("prediction", prediction)
        total += abs(target - prediction)
    return total


@dataclass(frozen=True)
class IntegerMaterialFit:
    amplitude: int
    input_root_power: int
    output_hardening_power: int
    output_scale: int
    basis: tuple[int, ...]
    predictions: tuple[int, ...]
    sse: int
    absolute_error: int
    max_absolute_error: int


def fit_integer_output_scale(
    targets: tuple[int, ...] | list[int],
    basis: tuple[int, ...] | list[int],
    amplitude: int,
    max_output_scale: int,
) -> tuple[int, tuple[int, ...], int, int, int]:
    """Exhaustively fit one integer output scale on a bounded domain."""
    _require_positive("amplitude", amplitude)
    _require_natural("max_output_scale", max_output_scale)
    target_values = tuple(targets)
    basis_values = tuple(basis)
    if not target_values or len(target_values) != len(basis_values):
        raise ValueError("targets and basis must be nonempty and have equal length")
    best: tuple[int, int, int, int, tuple[int, ...]] | None = None
    for output_scale in range(max_output_scale + 1):
        predictions = predict_scaled_basis(basis_values, amplitude, output_scale)
        sse = squared_error(target_values, predictions)
        l1 = absolute_error(target_values, predictions)
        max_error = max(
            abs(t - p) for t, p in zip(target_values, predictions, strict=True)
        )
        candidate = (sse, l1, max_error, output_scale, predictions)
        if best is None or candidate[:4] < best[:4]:
            best = candidate
    if best is None:
        raise AssertionError("finite output-scale search produced no candidate")
    sse, l1, max_error, output_scale, predictions = best
    return output_scale, predictions, sse, l1, max_error


def search_root_basin_material_fit(
    deformations: tuple[int, ...] | list[int],
    targets: tuple[int, ...] | list[int],
    amplitude: int,
    max_input_root_power: int,
    max_output_hardening_power: int,
    max_output_scale: int,
) -> IntegerMaterialFit:
    """Search a small discrete family of integer-only loading curves."""
    _require_positive("amplitude", amplitude)
    _require_positive("max_input_root_power", max_input_root_power)
    _require_positive("max_output_hardening_power", max_output_hardening_power)
    deformation_values = tuple(deformations)
    target_values = tuple(targets)
    if len(deformation_values) != len(target_values):
        raise ValueError("deformations and targets must have equal length")

    best: IntegerMaterialFit | None = None
    best_ordering: tuple[int, ...] | None = None
    for input_power in range(1, max_input_root_power + 1):
        for output_power in range(1, max_output_hardening_power + 1):
            basis = root_basin_versine_basis(
                deformation_values,
                amplitude,
                input_power,
                output_power,
            )
            output_scale, predictions, sse, l1, max_error = fit_integer_output_scale(
                target_values,
                basis,
                amplitude,
                max_output_scale,
            )
            candidate = IntegerMaterialFit(
                amplitude=amplitude,
                input_root_power=input_power,
                output_hardening_power=output_power,
                output_scale=output_scale,
                basis=basis,
                predictions=predictions,
                sse=sse,
                absolute_error=l1,
                max_absolute_error=max_error,
            )
            ordering = (
                candidate.sse,
                candidate.absolute_error,
                candidate.max_absolute_error,
                candidate.input_root_power + candidate.output_hardening_power,
                candidate.input_root_power,
                candidate.output_hardening_power,
                candidate.output_scale,
            )
            if best is None or best_ordering is None or ordering < best_ordering:
                best = candidate
                best_ordering = ordering
    if best is None:
        raise AssertionError("finite material-family search produced no candidate")
    return best
