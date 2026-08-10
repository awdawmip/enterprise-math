"""Exact collisions showing Ferrers activation area is not a sufficient state.

Two dyadic threshold staircases may use the same threshold grid and horizon,
have the same scalar activation area, but different activation matrices,
crossing depths, node ranks and Ferrers boundaries.  The module records such
collision certificates and therefore separates Stage-96's scalar potential from
the full future-safe threshold state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import DyadicThresholdStaircase


@dataclass(frozen=True)
class ActivationAreaCollision:
    threshold_grid_equal: bool
    horizon_equal: bool
    area_equal: bool
    activation_matrix_equal: bool
    crossing_depths_equal: bool
    node_ranks_equal: bool
    boundary_word_equal: bool
    common_area: int
    first_distinguishing_cell: tuple[int, int] | None
    left_cell_value: bool | None
    right_cell_value: bool | None
    collision_verified: bool


def activation_area_collision(
    left: DyadicThresholdStaircase,
    right: DyadicThresholdStaircase,
) -> ActivationAreaCollision:
    """Certify an equal-area/different-boundary collision on one declared grid."""
    if left.thresholds != right.thresholds:
        raise ValueError("collision comparison requires the same threshold grid")
    if left.horizon_steps != right.horizon_steps:
        raise ValueError("collision comparison requires the same orbit horizon")

    left_boundary = ferrers_boundary_from_staircase(left)
    right_boundary = ferrers_boundary_from_staircase(right)
    area_equal = left_boundary.activation_area == right_boundary.activation_area
    matrix_equal = left.activation_matrix == right.activation_matrix

    first: tuple[int, int] | None = None
    left_value: bool | None = None
    right_value: bool | None = None
    if not matrix_equal:
        for row_index, (left_row, right_row) in enumerate(
            zip(left.activation_matrix, right.activation_matrix)
        ):
            for column_index, (a, b) in enumerate(zip(left_row, right_row)):
                if a != b:
                    first = (row_index, column_index)
                    left_value = a
                    right_value = b
                    break
            if first is not None:
                break

    collision = area_equal and not matrix_equal
    if collision and first is None:
        raise AssertionError("different activation matrices must expose a distinguishing cell")

    return ActivationAreaCollision(
        threshold_grid_equal=True,
        horizon_equal=True,
        area_equal=area_equal,
        activation_matrix_equal=matrix_equal,
        crossing_depths_equal=left.crossing_depths == right.crossing_depths,
        node_ranks_equal=left_boundary.node_ranks == right_boundary.node_ranks,
        boundary_word_equal=left_boundary.boundary_word == right_boundary.boundary_word,
        common_area=left_boundary.activation_area if area_equal else -1,
        first_distinguishing_cell=first,
        left_cell_value=left_value,
        right_cell_value=right_value,
        collision_verified=collision,
    )
