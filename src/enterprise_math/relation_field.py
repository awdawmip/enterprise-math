"""Tree-independent integer pair-relation field for P019.

For slot values x_i define d_ij=x_i-x_j.  The full field is antisymmetric and
cycle-closed, reconstructs the slot values once the root total is fixed, and
produces every contraction imbalance as a cut sum.
"""

from __future__ import annotations


RelationField = tuple[tuple[int, ...], ...]


def _require_values(values: tuple[int, ...]) -> None:
    if not isinstance(values, tuple) or not values:
        raise ValueError("values must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("values must be integers")


def _require_field(field: RelationField) -> None:
    if not isinstance(field, tuple) or not field:
        raise ValueError("field must be a non-empty square tuple")
    size = len(field)
    if any(not isinstance(row, tuple) or len(row) != size for row in field):
        raise ValueError("field must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in field
        for value in row
    ):
        raise ValueError("field entries must be integers")


def pair_difference_field(values: tuple[int, ...]) -> RelationField:
    """Return the complete integer relation field d_ij=x_i-x_j."""
    _require_values(values)
    return tuple(
        tuple(left - right for right in values)
        for left in values
    )


def relation_field_is_closed(field: RelationField) -> bool:
    """Check diagonal zero, antisymmetry, and d_ij+d_jk=d_ik."""
    _require_field(field)
    size = len(field)
    for i in range(size):
        if field[i][i] != 0:
            return False
        for j in range(size):
            if field[i][j] != -field[j][i]:
                return False
            for k in range(size):
                if field[i][j] + field[j][k] != field[i][k]:
                    return False
    return True


def recover_values_from_field(field: RelationField, total: int) -> tuple[int, ...]:
    """Recover slot values from a closed difference field and root total.

    Since sum_j d_ij = N*x_i-total,

        x_i = (total + sum_j d_ij)//N.

    The divisions must be exact for a legal integer state.
    """
    _require_field(field)
    if isinstance(total, bool) or not isinstance(total, int):
        raise ValueError("total must be an integer")
    if not relation_field_is_closed(field):
        raise ValueError("field must be antisymmetric and cycle-closed")
    size = len(field)
    values = []
    for row in field:
        numerator = total + sum(row)
        if numerator % size != 0:
            raise ValueError("field and total do not define integer slot values")
        values.append(numerator // size)
    result = tuple(values)
    if sum(result) != total or pair_difference_field(result) != field:
        raise AssertionError("recovered state must reproduce the relation field")
    return result


def block_cut_sum(
    field: RelationField,
    left_indices: tuple[int, ...],
    right_indices: tuple[int, ...],
) -> int:
    """Sum d_ij over the directed cut left -> right."""
    _require_field(field)
    size = len(field)
    if not left_indices or not right_indices:
        raise ValueError("both cut sides must be non-empty")
    if len(set(left_indices)) != len(left_indices) or len(set(right_indices)) != len(right_indices):
        raise ValueError("cut indices must be unique within each side")
    if set(left_indices) & set(right_indices):
        raise ValueError("cut sides must be disjoint")
    if any(index < 0 or index >= size for index in left_indices + right_indices):
        raise ValueError("cut index out of range")
    return sum(field[i][j] for i in left_indices for j in right_indices)


def block_imbalance_from_values(
    values: tuple[int, ...],
    left_indices: tuple[int, ...],
    right_indices: tuple[int, ...],
) -> int:
    """Return |R|*sum_L x_i-|L|*sum_R x_j for comparison with cut sums."""
    _require_values(values)
    size = len(values)
    if not left_indices or not right_indices:
        raise ValueError("both block sides must be non-empty")
    if set(left_indices) & set(right_indices):
        raise ValueError("block sides must be disjoint")
    if any(index < 0 or index >= size for index in left_indices + right_indices):
        raise ValueError("block index out of range")
    left_total = sum(values[index] for index in left_indices)
    right_total = sum(values[index] for index in right_indices)
    return len(right_indices) * left_total - len(left_indices) * right_total


def pair_dispersion_from_field(field: RelationField) -> int:
    """Return sum_{i<j} d_ij^2 from the relation field."""
    _require_field(field)
    size = len(field)
    return sum(field[i][j] ** 2 for i in range(size) for j in range(i + 1, size))
