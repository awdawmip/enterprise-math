"""Leakage-resistant validation for finite E001 material-curve fits.

All-points fitting measures representation capacity, not predictive
usefulness. This module keeps the benchmark deformation domain fixed before a
split and permits only training responses to influence shape/scale selection.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_fit import fit_integer_output_scale, predict_scaled_basis, root_basin_versine_sample


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


def _validate_domain(lower: int, upper: int) -> None:
    _require_integer("lower", lower)
    _require_integer("upper", upper)
    if upper <= lower:
        raise ValueError("upper must be greater than lower")


def _validate_dataset(
    deformations: tuple[int, ...],
    targets: tuple[int, ...],
    lower: int,
    upper: int,
) -> None:
    if not deformations or len(deformations) != len(targets):
        raise ValueError("deformations and targets must be nonempty and have equal length")
    _validate_domain(lower, upper)
    for value in deformations:
        _require_integer("deformation", value)
        if not lower <= value <= upper:
            raise ValueError("deformation lies outside the declared benchmark domain")
    for value in targets:
        _require_natural("target", value)


def _validated_indices(indices: tuple[int, ...] | list[int], count: int) -> tuple[int, ...]:
    values = tuple(indices)
    if not values:
        raise ValueError("index set must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError("indices must not contain duplicates")
    for index in values:
        _require_natural("index", index)
        if index >= count:
            raise ValueError("index lies outside the dataset")
    return values


def fixed_domain_basis(
    deformations: tuple[int, ...] | list[int],
    lower: int,
    upper: int,
    amplitude: int,
    input_root_power: int,
    output_hardening_power: int,
) -> tuple[int, ...]:
    _validate_domain(lower, upper)
    _require_positive("amplitude", amplitude)
    _require_positive("input_root_power", input_root_power)
    _require_positive("output_hardening_power", output_hardening_power)
    values = tuple(deformations)
    for value in values:
        _require_integer("deformation", value)
        if not lower <= value <= upper:
            raise ValueError("deformation lies outside the declared benchmark domain")
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


@dataclass(frozen=True)
class IntegerErrorReport:
    count: int
    sse: int
    absolute_error: int
    max_absolute_error: int


def integer_error_report(
    targets: tuple[int, ...] | list[int],
    predictions: tuple[int, ...] | list[int],
) -> IntegerErrorReport:
    target_values = tuple(targets)
    prediction_values = tuple(predictions)
    if not target_values or len(target_values) != len(prediction_values):
        raise ValueError("targets and predictions must be nonempty and have equal length")
    errors = []
    for target, prediction in zip(target_values, prediction_values, strict=True):
        _require_natural("target", target)
        _require_natural("prediction", prediction)
        errors.append(target - prediction)
    return IntegerErrorReport(
        count=len(errors),
        sse=sum(error * error for error in errors),
        absolute_error=sum(abs(error) for error in errors),
        max_absolute_error=max(abs(error) for error in errors),
    )


@dataclass(frozen=True)
class FixedDomainMaterialFit:
    lower_deformation: int
    upper_deformation: int
    amplitude: int
    input_root_power: int
    output_hardening_power: int
    output_scale: int
    training_indices: tuple[int, ...]
    predictions: tuple[int, ...]
    training_error: IntegerErrorReport


def search_fixed_domain_material_fit(
    deformations: tuple[int, ...] | list[int],
    targets: tuple[int, ...] | list[int],
    lower_deformation: int,
    upper_deformation: int,
    amplitude: int,
    training_indices: tuple[int, ...] | list[int],
    max_input_root_power: int,
    max_output_hardening_power: int,
    max_output_scale: int,
) -> FixedDomainMaterialFit:
    deformation_values = tuple(deformations)
    target_values = tuple(targets)
    _validate_dataset(deformation_values, target_values, lower_deformation, upper_deformation)
    _require_positive("amplitude", amplitude)
    _require_positive("max_input_root_power", max_input_root_power)
    _require_positive("max_output_hardening_power", max_output_hardening_power)
    _require_natural("max_output_scale", max_output_scale)
    train = _validated_indices(training_indices, len(deformation_values))

    best: FixedDomainMaterialFit | None = None
    best_ordering: tuple[int, ...] | None = None
    for input_power in range(1, max_input_root_power + 1):
        for output_power in range(1, max_output_hardening_power + 1):
            basis = fixed_domain_basis(
                deformation_values,
                lower_deformation,
                upper_deformation,
                amplitude,
                input_power,
                output_power,
            )
            training_basis = tuple(basis[index] for index in train)
            training_targets = tuple(target_values[index] for index in train)
            output_scale, _, sse, l1, max_error = fit_integer_output_scale(
                training_targets,
                training_basis,
                amplitude,
                max_output_scale,
            )
            predictions = predict_scaled_basis(basis, amplitude, output_scale)
            candidate = FixedDomainMaterialFit(
                lower_deformation=lower_deformation,
                upper_deformation=upper_deformation,
                amplitude=amplitude,
                input_root_power=input_power,
                output_hardening_power=output_power,
                output_scale=output_scale,
                training_indices=train,
                predictions=predictions,
                training_error=IntegerErrorReport(len(train), sse, l1, max_error),
            )
            ordering = (
                sse,
                l1,
                max_error,
                input_power + output_power,
                input_power,
                output_power,
                output_scale,
            )
            if best is None or best_ordering is None or ordering < best_ordering:
                best = candidate
                best_ordering = ordering
    if best is None:
        raise AssertionError("bounded fixed-domain material search produced no candidate")
    return best


def evaluate_fit_indices(
    fit: FixedDomainMaterialFit,
    targets: tuple[int, ...] | list[int],
    indices: tuple[int, ...] | list[int],
) -> IntegerErrorReport:
    target_values = tuple(targets)
    if len(target_values) != len(fit.predictions):
        raise ValueError("targets must correspond to the dataset used for this fit")
    selected = _validated_indices(indices, len(target_values))
    return integer_error_report(
        tuple(target_values[index] for index in selected),
        tuple(fit.predictions[index] for index in selected),
    )


def modulo_test_folds(observation_count: int, fold_count: int) -> tuple[tuple[int, ...], ...]:
    _require_positive("observation_count", observation_count)
    _require_positive("fold_count", fold_count)
    if fold_count < 2 or fold_count > observation_count:
        raise ValueError("fold_count must lie in 2..observation_count")
    return tuple(
        tuple(index for index in range(observation_count) if index % fold_count == fold)
        for fold in range(fold_count)
    )


@dataclass(frozen=True)
class MaterialFoldReport:
    fold_index: int
    training_indices: tuple[int, ...]
    test_indices: tuple[int, ...]
    fit: FixedDomainMaterialFit
    test_error: IntegerErrorReport


@dataclass(frozen=True)
class MaterialCrossValidationReport:
    fold_count: int
    observation_count: int
    folds: tuple[MaterialFoldReport, ...]
    aggregate_test_error: IntegerErrorReport


def cross_validate_fixed_domain_material_fit(
    deformations: tuple[int, ...] | list[int],
    targets: tuple[int, ...] | list[int],
    lower_deformation: int,
    upper_deformation: int,
    amplitude: int,
    fold_count: int,
    max_input_root_power: int,
    max_output_hardening_power: int,
    max_output_scale: int,
) -> MaterialCrossValidationReport:
    deformation_values = tuple(deformations)
    target_values = tuple(targets)
    _validate_dataset(deformation_values, target_values, lower_deformation, upper_deformation)
    test_folds = modulo_test_folds(len(deformation_values), fold_count)
    all_indices = set(range(len(deformation_values)))
    fold_reports = []
    all_test_targets = []
    all_test_predictions = []

    for fold_index, test_indices in enumerate(test_folds):
        training_indices = tuple(sorted(all_indices - set(test_indices)))
        fit = search_fixed_domain_material_fit(
            deformation_values,
            target_values,
            lower_deformation,
            upper_deformation,
            amplitude,
            training_indices,
            max_input_root_power,
            max_output_hardening_power,
            max_output_scale,
        )
        test_error = evaluate_fit_indices(fit, target_values, test_indices)
        fold_reports.append(
            MaterialFoldReport(fold_index, training_indices, test_indices, fit, test_error)
        )
        for index in test_indices:
            all_test_targets.append(target_values[index])
            all_test_predictions.append(fit.predictions[index])

    return MaterialCrossValidationReport(
        fold_count=fold_count,
        observation_count=len(deformation_values),
        folds=tuple(fold_reports),
        aggregate_test_error=integer_error_report(
            tuple(all_test_targets), tuple(all_test_predictions)
        ),
    )
