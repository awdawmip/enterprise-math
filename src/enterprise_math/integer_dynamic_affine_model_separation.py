"""Total-affine dynamic model separation by homogeneous augmentation.

For affine action

    x -> A x + b

on integer column state, use homogeneous state ``x_bar=(x,1)`` and matrix

    A_bar = [[A,b],
             [0,1]].

For affine observation ``C x + d``, use row ``C_bar=(C,d)``.

Two affine models with the same named action alphabet can then be compared by
the linear dynamic difference-module compiler on the augmented coordinates.
The projected difference rows contain both state coefficients and constant terms,
so modular congruence of every augmented coefficient is exactly equality of the
affine outputs for every original state.

This extends the static affine-content theorem to the whole future action
language and preserves the same semantic boundary: within one model a common
offset cancels between two states, but between two models action/observation
offset differences are observable model structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_dynamic_model_separation import (
    DynamicModelSeparationReport,
    dynamic_difference_content,
    dynamic_difference_module_basis,
    dynamic_model_separation_report,
    dynamic_models_indistinguishable_modulus,
)
from .integer_dynamic_model_separation_horizon import (
    DynamicSeparationHorizonReport,
    dynamic_model_separation_horizon_report,
)


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]
AffineAction = tuple[Matrix, Vector]


def _linear(values: Sequence[Sequence[int]], *, name: str) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError(f"{name} must contain at least one row")
    width = len(rows[0])
    if width == 0 or len(rows) != width or any(len(row) != width for row in rows):
        raise ValueError(f"{name} must be a nonempty square matrix")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{name} entries must be integers")
    return rows


def _vector(values: Sequence[int], length: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} length mismatch")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} entries must be integers")
    return result


def homogeneous_affine_action(
    linear: Sequence[Sequence[int]],
    offset: Sequence[int],
) -> Matrix:
    matrix = _linear(linear, name="linear")
    dimension = len(matrix)
    shift = _vector(offset, dimension, name="offset")
    return tuple(
        tuple((*matrix[row], shift[row]))
        for row in range(dimension)
    ) + (tuple(0 for _ in range(dimension)) + (1,),)


def homogeneous_affine_observation_rows(
    linear_rows: Sequence[Sequence[int]],
    offset: Sequence[int],
) -> Matrix:
    rows = tuple(tuple(row) for row in linear_rows)
    if not rows:
        raise ValueError("linear observation rows must be nonempty")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("linear observation rows must share positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("observation entries must be integers")
    shift = _vector(offset, len(rows), name="observation offset")
    return tuple(
        tuple((*row, shift_value))
        for row, shift_value in zip(rows, shift, strict=True)
    )


def homogeneous_affine_action_family(
    actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
) -> tuple[Matrix, ...]:
    values = tuple(actions)
    if not values:
        raise ValueError("affine action family must be nonempty")
    result = tuple(
        homogeneous_affine_action(linear, offset)
        for linear, offset in values
    )
    dimension = len(result[0])
    if any(len(action) != dimension for action in result):
        raise ValueError("all affine actions must share one state dimension")
    return result


def dynamic_affine_difference_module_basis(
    left_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    left_observation_rows: Sequence[Sequence[int]],
    left_observation_offset: Sequence[int],
    right_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    right_observation_rows: Sequence[Sequence[int]],
    right_observation_offset: Sequence[int],
) -> Matrix:
    return dynamic_difference_module_basis(
        homogeneous_affine_action_family(left_actions),
        homogeneous_affine_observation_rows(
            left_observation_rows,
            left_observation_offset,
        ),
        homogeneous_affine_action_family(right_actions),
        homogeneous_affine_observation_rows(
            right_observation_rows,
            right_observation_offset,
        ),
    )


def dynamic_affine_difference_content(
    left_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    left_observation_rows: Sequence[Sequence[int]],
    left_observation_offset: Sequence[int],
    right_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    right_observation_rows: Sequence[Sequence[int]],
    right_observation_offset: Sequence[int],
) -> int:
    return dynamic_difference_content(
        homogeneous_affine_action_family(left_actions),
        homogeneous_affine_observation_rows(left_observation_rows, left_observation_offset),
        homogeneous_affine_action_family(right_actions),
        homogeneous_affine_observation_rows(right_observation_rows, right_observation_offset),
    )


def dynamic_affine_models_indistinguishable_modulus(
    left_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    left_observation_rows: Sequence[Sequence[int]],
    left_observation_offset: Sequence[int],
    right_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    right_observation_rows: Sequence[Sequence[int]],
    right_observation_offset: Sequence[int],
    modulus: int,
) -> bool:
    return dynamic_models_indistinguishable_modulus(
        homogeneous_affine_action_family(left_actions),
        homogeneous_affine_observation_rows(left_observation_rows, left_observation_offset),
        homogeneous_affine_action_family(right_actions),
        homogeneous_affine_observation_rows(right_observation_rows, right_observation_offset),
        modulus,
    )


def dynamic_affine_model_separation_report(
    left_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    left_observation_rows: Sequence[Sequence[int]],
    left_observation_offset: Sequence[int],
    right_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    right_observation_rows: Sequence[Sequence[int]],
    right_observation_offset: Sequence[int],
) -> DynamicModelSeparationReport:
    return dynamic_model_separation_report(
        homogeneous_affine_action_family(left_actions),
        homogeneous_affine_observation_rows(left_observation_rows, left_observation_offset),
        homogeneous_affine_action_family(right_actions),
        homogeneous_affine_observation_rows(right_observation_rows, right_observation_offset),
    )


def dynamic_affine_model_separation_horizon_report(
    left_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    left_observation_rows: Sequence[Sequence[int]],
    left_observation_offset: Sequence[int],
    right_actions: Sequence[tuple[Sequence[Sequence[int]], Sequence[int]]],
    right_observation_rows: Sequence[Sequence[int]],
    right_observation_offset: Sequence[int],
) -> DynamicSeparationHorizonReport:
    return dynamic_model_separation_horizon_report(
        homogeneous_affine_action_family(left_actions),
        homogeneous_affine_observation_rows(left_observation_rows, left_observation_offset),
        homogeneous_affine_action_family(right_actions),
        homogeneous_affine_observation_rows(right_observation_rows, right_observation_offset),
    )
