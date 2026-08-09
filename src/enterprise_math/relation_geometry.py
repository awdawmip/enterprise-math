"""Tree-independent geometry observables on P019 relation fields.

For a zero-total weighted relation state, the positive-mass graph radius is the
maximum directed cut relation divided exactly by total capacity.  For unit
blocks, the quadratic radial state q is the squared pair-relation sum divided
exactly by twice the slot count.
"""

from __future__ import annotations

from .relation_field import RelationField, pair_dispersion_from_field, relation_field_is_closed
from .weighted_relation_field import WeightedField, weighted_relation_field_is_closed


def _require_subset(block_count: int, subset: tuple[int, ...]) -> None:
    if not isinstance(subset, tuple):
        raise ValueError("subset must be a tuple")
    if len(set(subset)) != len(subset):
        raise ValueError("subset indices must be unique")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= block_count
        for index in subset
    ):
        raise ValueError("subset index out of range")


def directed_weighted_cut_sum(field: WeightedField, subset: tuple[int, ...]) -> int:
    """Return sum Z_ij across subset -> complement."""
    if not isinstance(field, tuple) or not field:
        raise ValueError("field must be a non-empty square tuple")
    count = len(field)
    if any(not isinstance(row, tuple) or len(row) != count for row in field):
        raise ValueError("field must be square")
    _require_subset(count, subset)
    inside = set(subset)
    return sum(
        field[i][j]
        for i in subset
        for j in range(count)
        if j not in inside
    )


def maximum_directed_weighted_cut_sum(field: WeightedField) -> int:
    """Reference finite maximum of directed cut sums over all block subsets."""
    if not isinstance(field, tuple) or not field:
        raise ValueError("field must be a non-empty square tuple")
    count = len(field)
    if any(not isinstance(row, tuple) or len(row) != count for row in field):
        raise ValueError("field must be square")
    best = 0
    for mask in range(1 << count):
        subset = tuple(index for index in range(count) if mask & (1 << index))
        best = max(best, directed_weighted_cut_sum(field, subset))
    return best


def zero_total_graph_radius_from_weighted_field(
    block_sizes: tuple[int, ...], field: WeightedField
) -> int:
    """Return sum of positive block totals from the weighted field alone.

    On a zero-grand-total state,

        max_S Z(S,S^c) = M * sum_{c_i>0} c_i.

    The final division by M is exact.
    """
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted field must satisfy weighted closure")
    total_capacity = sum(block_sizes)
    maximum = maximum_directed_weighted_cut_sum(field)
    if maximum % total_capacity != 0:
        raise AssertionError("zero-total weighted cut maximum must be divisible by total capacity")
    return maximum // total_capacity


def zero_total_l1_energy_from_weighted_field(
    block_sizes: tuple[int, ...], field: WeightedField
) -> int:
    """Return sum |c_i| = 2*graph radius for a zero-total weighted state."""
    return 2 * zero_total_graph_radius_from_weighted_field(block_sizes, field)


def zero_sum_quadratic_from_unit_relation_field(field: RelationField) -> int:
    """Return q from a closed unit-capacity zero-sum pair field.

    The exact identity is

        sum_{i<j} d_ij^2 = 2*N*q.
    """
    if not relation_field_is_closed(field):
        raise ValueError("unit relation field must be closed")
    count = len(field)
    dispersion = pair_dispersion_from_field(field)
    divisor = 2 * count
    if dispersion % divisor != 0:
        raise ValueError("field is not compatible with a zero-sum integer unit state")
    return dispersion // divisor
