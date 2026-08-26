"""Total-affine offsets do not change linear future-equivalence partitions.

Use column-state convention.  A total affine action is

    F_a(x) = A_a x + b_a,

and an affine scalar observation is

    O(x) = c x + d.

For two states following the same literal action word, affine offsets cancel in
their difference.  If ``A_w`` is the corresponding product of linear parts,

    O(F_w(x)) - O(F_w(y)) = c A_w (x-y).

Therefore the equality kernel induced by a declared family of **total affine**
actions depends only on their linear parts and the linear observation rows.
Translation offsets affect absolute outputs but not which initial states are
future-equivalent.

This reduction fails once the future language contains state-dependent domains.
An affine offset can move a state across a later guard boundary, changing
future definedness even when the linear part is unchanged.  Such a world belongs
to the DOMAIN/partial-operation layer and must retain legality in its future
signature.

Affine systems and difference dynamics are standard prior mathematics.  This
module records the exact boundary for the integer P023 compiler.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


Vector = tuple[int, ...]
Matrix = tuple[Vector, ...]


def _vector(values: Sequence[int], *, length: int | None = None) -> Vector:
    result = tuple(values)
    if length is not None and len(result) != length:
        raise ValueError("vector length mismatch")
    if not result:
        raise ValueError("vector must be nonempty")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("vector entries must be integers")
    return result


def _square_matrix(values: Sequence[Sequence[int]], dimension: int) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if len(rows) != dimension or any(len(row) != dimension for row in rows):
        raise ValueError("matrix must be square on the state dimension")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return rows


def apply_linear_action(matrix: Sequence[Sequence[int]], state: Sequence[int]) -> Vector:
    x = _vector(state)
    a = _square_matrix(matrix, len(x))
    return tuple(
        sum(a[row][column] * x[column] for column in range(len(x)))
        for row in range(len(x))
    )


def apply_affine_action(
    matrix: Sequence[Sequence[int]],
    offset: Sequence[int],
    state: Sequence[int],
) -> Vector:
    x = _vector(state)
    b = _vector(offset, length=len(x))
    linear = apply_linear_action(matrix, x)
    return tuple(left + right for left, right in zip(linear, b, strict=True))


def apply_affine_word(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    action_offsets: Sequence[Sequence[int]],
    word: Sequence[int],
    state: Sequence[int],
) -> Vector:
    x = _vector(state)
    matrices = tuple(_square_matrix(matrix, len(x)) for matrix in action_matrices)
    offsets = tuple(_vector(offset, length=len(x)) for offset in action_offsets)
    if len(matrices) != len(offsets):
        raise ValueError("one offset is required per affine action")
    if not matrices:
        raise ValueError("at least one affine action is required")
    current = x
    for action in word:
        if isinstance(action, bool) or not isinstance(action, int):
            raise TypeError("word symbols must be integer action indices")
        if not 0 <= action < len(matrices):
            raise ValueError("word action index is outside the action family")
        current = apply_affine_action(
            matrices[action],
            offsets[action],
            current,
        )
    return current


def apply_linear_word_to_difference(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    word: Sequence[int],
    difference: Sequence[int],
) -> Vector:
    delta = _vector(difference)
    matrices = tuple(_square_matrix(matrix, len(delta)) for matrix in action_matrices)
    if not matrices:
        raise ValueError("at least one linear action is required")
    current = delta
    for action in word:
        if isinstance(action, bool) or not isinstance(action, int):
            raise TypeError("word symbols must be integer action indices")
        if not 0 <= action < len(matrices):
            raise ValueError("word action index is outside the action family")
        current = apply_linear_action(matrices[action], current)
    return current


def affine_scalar_observation(
    row: Sequence[int],
    offset: int,
    state: Sequence[int],
) -> int:
    x = _vector(state)
    c = _vector(row, length=len(x))
    if isinstance(offset, bool) or not isinstance(offset, int):
        raise TypeError("observation offset must be an integer")
    return sum(coefficient * value for coefficient, value in zip(c, x, strict=True)) + offset


@dataclass(frozen=True)
class AffineFutureDifferenceReport:
    word: tuple[int, ...]
    affine_output_difference: int
    linearized_output_difference: int

    @property
    def offsets_cancel_exactly(self) -> bool:
        return self.affine_output_difference == self.linearized_output_difference


def affine_word_observation_difference(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    action_offsets: Sequence[Sequence[int]],
    observation_row: Sequence[int],
    observation_offset: int,
    word: Sequence[int],
    left_state: Sequence[int],
    right_state: Sequence[int],
) -> AffineFutureDifferenceReport:
    """Verify exact cancellation of all affine offsets for one future word."""
    left = _vector(left_state)
    right = _vector(right_state, length=len(left))
    c = _vector(observation_row, length=len(left))
    literal_word = tuple(word)

    left_after = apply_affine_word(
        action_matrices,
        action_offsets,
        literal_word,
        left,
    )
    right_after = apply_affine_word(
        action_matrices,
        action_offsets,
        literal_word,
        right,
    )
    affine_difference = (
        affine_scalar_observation(c, observation_offset, left_after)
        - affine_scalar_observation(c, observation_offset, right_after)
    )

    initial_difference = tuple(
        a - b for a, b in zip(left, right, strict=True)
    )
    linear_difference_state = apply_linear_word_to_difference(
        action_matrices,
        literal_word,
        initial_difference,
    )
    linearized_difference = sum(
        coefficient * value
        for coefficient, value in zip(c, linear_difference_state, strict=True)
    )
    if affine_difference != linearized_difference:
        raise AssertionError("total-affine offsets failed to cancel in state difference")

    return AffineFutureDifferenceReport(
        word=literal_word,
        affine_output_difference=affine_difference,
        linearized_output_difference=linearized_difference,
    )


def one_dimensional_guard_after_affine_step(
    state: int,
    shift: int,
) -> tuple[bool, int | None, bool | None]:
    """Sharp DOMAIN boundary: ``x->x+shift`` is allowed only while ``x<0``.

    Returns first-step definedness, the first after-state when defined, and
    whether a second identical guarded step would be defined.
    """
    for name, value in (("state", state), ("shift", shift)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if state >= 0:
        return False, None, None
    after = state + shift
    return True, after, after < 0
