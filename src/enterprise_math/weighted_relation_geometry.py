"""Square-layer geometry reconstructed from capacity-weighted relations.

For a block of capacity m and total c, the balanced minimum has internal pair
dispersion epsilon_m(c)=r*(m-r).  For two blocks A,B, their minimum cross-pair
squared dispersion C_AB obeys

    m*n*C_AB = n^2*epsilon_m(a) + m^2*epsilon_n(b) + Z_AB^2.

Together these reconstruct the pair dispersion of the fully expanded balanced
unit-slot representative without explicitly expanding the blocks.
"""

from __future__ import annotations

from .contraction_trace import square_residue_correction
from .dimension_contraction import partition_power_energy
from .weighted_relation_field import (
    WeightedField,
    recover_totals_from_weighted_field,
    weighted_relation_field_is_closed,
)


def minimum_cross_pair_dispersion(
    left_size: int,
    right_size: int,
    left_total: int,
    right_total: int,
    weighted_relation: int,
) -> int:
    """Minimum cross-block sum of squared unit differences for balanced blocks."""
    if isinstance(left_size, bool) or not isinstance(left_size, int) or left_size <= 0:
        raise ValueError("left_size must be a positive integer")
    if isinstance(right_size, bool) or not isinstance(right_size, int) or right_size <= 0:
        raise ValueError("right_size must be a positive integer")
    for name, value in (
        ("left_total", left_total),
        ("right_total", right_total),
        ("weighted_relation", weighted_relation),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")

    expected_relation = right_size * left_total - left_size * right_total
    if weighted_relation != expected_relation:
        raise ValueError("weighted relation is incompatible with capacities and totals")

    left_internal = square_residue_correction(left_size, left_total)
    right_internal = square_residue_correction(right_size, right_total)
    numerator = (
        right_size * right_size * left_internal
        + left_size * left_size * right_internal
        + weighted_relation * weighted_relation
    )
    divisor = left_size * right_size
    if numerator % divisor != 0:
        raise AssertionError("balanced cross-pair dispersion must be integral")
    return numerator // divisor


def minimum_expanded_pair_dispersion(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    grand_total: int,
) -> int:
    """Pair dispersion of the balanced expanded unit-slot representative."""
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field must be closed")
    totals = recover_totals_from_weighted_field(block_sizes, field, grand_total)
    internal = sum(
        square_residue_correction(block_size, total)
        for block_size, total in zip(block_sizes, totals)
    )
    cross = 0
    for left in range(len(block_sizes)):
        for right in range(left + 1, len(block_sizes)):
            cross += minimum_cross_pair_dispersion(
                block_sizes[left],
                block_sizes[right],
                totals[left],
                totals[right],
                field[left][right],
            )
    return internal + cross


def zero_total_square_energy_from_weighted_relations(
    block_sizes: tuple[int, ...], field: WeightedField
) -> int:
    """Recover E_m^(2)=sum Psi_(m_i,2)(c_i) from weighted relations.

    For grand total zero and total capacity M, expanded pair dispersion is

        P = M * E_m^(2).

    The final division is exact.
    """
    total_capacity = sum(block_sizes)
    dispersion = minimum_expanded_pair_dispersion(block_sizes, field, grand_total=0)
    if dispersion % total_capacity != 0:
        raise AssertionError("zero-total expanded dispersion must be divisible by total capacity")
    energy = dispersion // total_capacity

    # Cross-check the direct fiber-minimum expression without exposing it as
    # a required representation.
    totals = recover_totals_from_weighted_field(block_sizes, field, 0)
    if energy != partition_power_energy(block_sizes, 2, totals):
        raise AssertionError("relation reconstruction must equal square fiber-minimum energy")
    return energy
