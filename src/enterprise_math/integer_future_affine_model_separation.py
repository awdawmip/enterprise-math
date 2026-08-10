"""Modular separation of affine integer observation models by augmentation.

For affine observation

    F(x) = C x + d,

use augmented state ``x_tilde=(x,1)`` and augmented row matrix

    C_tilde = [ C | d ].

Two affine maps on the same state/output dimensions agree modulo M for every
integer state iff their augmented matrices agree modulo M.  Therefore the whole
modular indistinguishability region is again the divisor down-set of the gcd
content of the augmented-matrix difference.

This complements the within-model state-equality result: when comparing two
states under the **same** affine map, the common offset cancels; when comparing
two different affine models, offset differences are themselves observable and
must be retained.

Affine augmentation and modular congruence are standard prior mathematics.  The
project value is the exact semantic boundary between state precision and model
precision.
"""

from __future__ import annotations

from typing import Sequence

from .integer_future_modular_model_separation import (
    first_distinguishing_prime_power_exponent,
    models_indistinguishable_modulus,
    observation_model_difference_content,
)


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _linear(values: Sequence[Sequence[int]], *, name: str) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError(f"{name} must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError(f"{name} rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{name} entries must be integers")
    return rows


def _offset(values: Sequence[int], row_count: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != row_count:
        raise ValueError(f"{name} must have one entry per observation row")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} entries must be integers")
    return result


def augmented_affine_observation_matrix(
    linear_rows: Sequence[Sequence[int]],
    offset: Sequence[int],
) -> Matrix:
    linear = _linear(linear_rows, name="linear_rows")
    shift = _offset(offset, len(linear), name="offset")
    return tuple(
        tuple((*row, shift_value))
        for row, shift_value in zip(linear, shift, strict=True)
    )


def affine_model_difference_content(
    left_linear: Sequence[Sequence[int]],
    left_offset: Sequence[int],
    right_linear: Sequence[Sequence[int]],
    right_offset: Sequence[int],
) -> int:
    left = augmented_affine_observation_matrix(left_linear, left_offset)
    right = augmented_affine_observation_matrix(right_linear, right_offset)
    return observation_model_difference_content(left, right)


def affine_models_indistinguishable_modulus(
    left_linear: Sequence[Sequence[int]],
    left_offset: Sequence[int],
    right_linear: Sequence[Sequence[int]],
    right_offset: Sequence[int],
    modulus: int,
) -> bool:
    left = augmented_affine_observation_matrix(left_linear, left_offset)
    right = augmented_affine_observation_matrix(right_linear, right_offset)
    return models_indistinguishable_modulus(left, right, modulus)


def first_distinguishing_affine_prime_power_exponent(
    left_linear: Sequence[Sequence[int]],
    left_offset: Sequence[int],
    right_linear: Sequence[Sequence[int]],
    right_offset: Sequence[int],
    prime: int,
) -> int | None:
    left = augmented_affine_observation_matrix(left_linear, left_offset)
    right = augmented_affine_observation_matrix(right_linear, right_offset)
    return first_distinguishing_prime_power_exponent(left, right, prime)


def affine_observation_value(
    linear_rows: Sequence[Sequence[int]],
    offset: Sequence[int],
    state: Sequence[int],
    *,
    modulus: int | None = None,
) -> Vector:
    linear = _linear(linear_rows, name="linear_rows")
    shift = _offset(offset, len(linear), name="offset")
    values = tuple(state)
    if len(values) != len(linear[0]):
        raise ValueError("state dimension must match affine linear part")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("state entries must be integers")
    result = tuple(
        sum(coefficient * value for coefficient, value in zip(row, values, strict=True)) + shift_value
        for row, shift_value in zip(linear, shift, strict=True)
    )
    if modulus is None:
        return result
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be positive integer")
    return tuple(value % modulus for value in result)
