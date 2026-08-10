"""Ferrers activation area as a biaxial discrete potential.

For a finite dyadic threshold staircase let

    A = # {(threshold,node): rho_node >= threshold}.

Adding one threshold changes A by the number of old orbit nodes on which the
new threshold is active.  Adding one orbit node changes A by that node's rank
(number of old thresholds reached).  Adding both axes gives the mixed second
difference

    Delta_J Delta_T A = Delta_T Delta_J A
                      = [new pressure >= new threshold].

Thus the crossing and rank coordinates are directional first differences of the
same scalar activation potential, while the new corner cell is its mixed second
difference.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import (
    DyadicThresholdStaircase,
    dyadic_threshold_staircase,
)


@dataclass(frozen=True)
class BiaxialActivationPotential:
    new_threshold: Fraction
    old_area: int
    threshold_extended_area: int
    orbit_extended_area: int
    biaxially_extended_area: int
    threshold_first_difference: int
    orbit_first_difference: int
    orbit_difference_after_threshold: int
    threshold_difference_after_orbit: int
    mixed_difference_threshold_then_orbit: int
    mixed_difference_orbit_then_threshold: int
    new_threshold_crossing_depth: int | None
    new_threshold_old_active_span: int
    new_node_old_threshold_rank: int
    new_corner_active: bool
    corner_law_verified: bool


def biaxial_activation_potential(
    staircase: DyadicThresholdStaircase,
    new_threshold: Fraction,
) -> BiaxialActivationPotential:
    """Compute all first/mixed area differences for one threshold+node extension."""
    if not isinstance(new_threshold, Fraction) or new_threshold <= 0:
        raise ValueError("new_threshold must be a positive Fraction")
    if new_threshold in staircase.thresholds:
        raise ValueError("new_threshold must not duplicate an existing threshold")

    thresholds = tuple(sorted((*staircase.thresholds, new_threshold)))
    insertion_index = thresholds.index(new_threshold)
    threshold_extended = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps,
        thresholds,
    )
    orbit_extended = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        staircase.thresholds,
    )
    both = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        thresholds,
    )

    old_boundary = ferrers_boundary_from_staircase(staircase)
    threshold_boundary = ferrers_boundary_from_staircase(threshold_extended)
    orbit_boundary = ferrers_boundary_from_staircase(orbit_extended)
    both_boundary = ferrers_boundary_from_staircase(both)

    A = old_boundary.activation_area
    A_T = threshold_boundary.activation_area
    A_J = orbit_boundary.activation_area
    A_TJ = both_boundary.activation_area

    dT = A_T - A
    dJ = A_J - A
    dJ_after_T = A_TJ - A_T
    dT_after_J = A_TJ - A_J
    mixed_TJ = dJ_after_T - dJ
    mixed_JT = dT_after_J - dT

    crossing = threshold_extended.crossing_depths[insertion_index]
    expected_span = (
        0
        if crossing is None
        else staircase.horizon_steps + 1 - crossing
    )
    if dT != expected_span:
        raise AssertionError("threshold area derivative disagreed with crossing span")

    new_rank_old_thresholds = orbit_boundary.node_ranks[-1]
    if dJ != new_rank_old_thresholds:
        raise AssertionError("orbit area derivative disagreed with new-node rank")

    corner = both.activation_matrix[insertion_index][-1]
    if mixed_TJ != mixed_JT:
        raise AssertionError("biaxial activation potential lost mixed-difference commutation")
    if mixed_TJ != int(corner):
        raise AssertionError("mixed area difference disagreed with new corner activation bit")

    return BiaxialActivationPotential(
        new_threshold=new_threshold,
        old_area=A,
        threshold_extended_area=A_T,
        orbit_extended_area=A_J,
        biaxially_extended_area=A_TJ,
        threshold_first_difference=dT,
        orbit_first_difference=dJ,
        orbit_difference_after_threshold=dJ_after_T,
        threshold_difference_after_orbit=dT_after_J,
        mixed_difference_threshold_then_orbit=mixed_TJ,
        mixed_difference_orbit_then_threshold=mixed_JT,
        new_threshold_crossing_depth=crossing,
        new_threshold_old_active_span=expected_span,
        new_node_old_threshold_rank=new_rank_old_thresholds,
        new_corner_active=corner,
        corner_law_verified=True,
    )
