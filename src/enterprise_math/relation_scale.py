"""Primitive relation structure plus integer precision scale for P019.

A weighted relation state factors uniquely by g=gcd(capacities):

    m = g*m_hat,
    Z = g*Z_hat,

with primitive capacities gcd(m_hat)=1.  Partition coarsening may introduce a
new integer scale carry h=gcd(A*m_hat); then g' = g*h and the new primitive
capacities/relations are divided exactly by h.
"""

from __future__ import annotations

from .relation_lattice import capacity_gcd
from .weighted_relation_field import (
    Partition,
    WeightedField,
    coarsen_weighted_relation_field,
    weighted_relation_field_is_closed,
)


def primitive_relation_state(
    block_sizes: tuple[int, ...], field: WeightedField
) -> tuple[int, tuple[int, ...], WeightedField]:
    """Return `(scale, primitive_capacities, primitive_field)`."""
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field must be closed")
    scale = capacity_gcd(block_sizes)
    primitive_sizes = tuple(size // scale for size in block_sizes)
    primitive_rows = []
    for row in field:
        if any(value % scale != 0 for value in row):
            raise ValueError("weighted relation entries must share the capacity gcd")
        primitive_rows.append(tuple(value // scale for value in row))
    primitive_field = tuple(primitive_rows)
    if capacity_gcd(primitive_sizes) != 1:
        raise AssertionError("primitive capacities must have gcd one")
    if not weighted_relation_field_is_closed(primitive_sizes, primitive_field):
        raise AssertionError("primitive relation field must remain closed")
    return scale, primitive_sizes, primitive_field


def coarsen_primitive_relation_state(
    scale: int,
    primitive_sizes: tuple[int, ...],
    primitive_field: WeightedField,
    partition: Partition,
) -> tuple[int, int, tuple[int, ...], WeightedField]:
    """Coarsen a primitive relation state and extract the new scale carry.

    Returns `(scale_carry, new_scale, new_primitive_sizes, new_primitive_field)`.
    """
    if isinstance(scale, bool) or not isinstance(scale, int) or scale <= 0:
        raise ValueError("scale must be a positive integer")
    if capacity_gcd(primitive_sizes) != 1:
        raise ValueError("primitive_sizes must have gcd one")
    if not weighted_relation_field_is_closed(primitive_sizes, primitive_field):
        raise ValueError("primitive relation field must be closed")

    coarse_sizes, coarse_field = coarsen_weighted_relation_field(
        primitive_sizes, primitive_field, partition
    )
    carry, normalized_sizes, normalized_field = primitive_relation_state(
        coarse_sizes, coarse_field
    )
    return carry, scale * carry, normalized_sizes, normalized_field


def relation_scale_chain_product(
    initial_scale: int, carries: tuple[int, ...]
) -> int:
    """Multiply integer relation-scale carries along a coarsening chain."""
    if isinstance(initial_scale, bool) or not isinstance(initial_scale, int) or initial_scale <= 0:
        raise ValueError("initial_scale must be a positive integer")
    result = initial_scale
    for carry in carries:
        if isinstance(carry, bool) or not isinstance(carry, int) or carry <= 0:
            raise ValueError("all carries must be positive integers")
        result *= carry
    return result
