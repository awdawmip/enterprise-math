"""Pair-unit LEGO interaction as the causal origin of bilinear/tensor shadows.

The primitive object is a table of effects produced by one left unit meeting one
right unit.  If the cross interaction is additive under LEGO composition on each
side separately, the response for arbitrary integer multiplicities is forced to
be the finite integer sum

    B(x,y) = sum_{i,j} x_i y_j B(e_i,f_j).

Traditional bilinear matrices/tensors are coordinate shadows of this unit-pair
effect table.  No real scalar field, tensor completion, or continuum is assumed.
"""

from __future__ import annotations


Vector = tuple[int, ...]
PairEffects = tuple[tuple[Vector, ...], ...]


def _require_vector(vector: Vector, name: str) -> None:
    if not isinstance(vector, tuple) or not vector:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError(f"{name} entries must be integers")


def _effect_shape(effects: PairEffects) -> tuple[int, int, int]:
    if not isinstance(effects, tuple) or not effects:
        raise ValueError("effects must be a non-empty tuple")
    right_size = len(effects[0])
    if right_size == 0 or any(not isinstance(row, tuple) or len(row) != right_size for row in effects):
        raise ValueError("effects must be a rectangular pair table")
    output_size = len(effects[0][0])
    if output_size == 0:
        raise ValueError("effect vectors must be non-empty")
    for row in effects:
        for effect in row:
            if not isinstance(effect, tuple) or len(effect) != output_size:
                raise ValueError("all pair effects must share one output dimension")
            if any(isinstance(value, bool) or not isinstance(value, int) for value in effect):
                raise ValueError("pair effects must be integer vectors")
    return len(effects), right_size, output_size


def pair_interaction_from_unit_effects(
    left: Vector,
    right: Vector,
    effects: PairEffects,
) -> Vector:
    """Exact separately additive pair response from unit-pair effects."""
    _require_vector(left, "left")
    _require_vector(right, "right")
    left_size, right_size, output_size = _effect_shape(effects)
    if len(left) != left_size or len(right) != right_size:
        raise ValueError("state dimensions do not match the pair-effect table")
    result = [0] * output_size
    for i, left_count in enumerate(left):
        for j, right_count in enumerate(right):
            multiplicity = left_count * right_count
            for output in range(output_size):
                result[output] += multiplicity * effects[i][j][output]
    return tuple(result)


def unit_pair_effects_determine_same_response(
    left_a: Vector,
    left_b: Vector,
    right: Vector,
    effects: PairEffects,
) -> bool:
    """Executable separate-additivity check on the left argument."""
    _require_vector(left_a, "left_a")
    _require_vector(left_b, "left_b")
    if len(left_a) != len(left_b):
        raise ValueError("left vectors must share a dimension")
    combined = tuple(a + b for a, b in zip(left_a, left_b))
    whole = pair_interaction_from_unit_effects(combined, right, effects)
    first = pair_interaction_from_unit_effects(left_a, right, effects)
    second = pair_interaction_from_unit_effects(left_b, right, effects)
    return whole == tuple(a + b for a, b in zip(first, second))
