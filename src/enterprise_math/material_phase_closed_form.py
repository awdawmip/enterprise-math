"""Closed-form phase masses for arbitrary saved-state wall jumps.

Let ``C=g_pre+g_post`` for positive integer endpoint clearances.  Ordered
positive pairs have total multiplicity ``C-1``.  The number with
``L <= min(g_pre,g_post) <= U`` is exactly

    max(0, C-2L+1) - max(0, C-2U-1).

This one identity gives exact phase masses for the endpoint-only E001 world:

* TRANSMIT: controlling gap ``g>=d``;
* UNDERRESOLVED: ``g<d-K`` where ``K`` is finite material depth;
* ZERO_RETURN: represented depths below the first nonzero kinematic return;
* REBOUND: represented depths at or above that threshold.

No continuous path sweep is reconstructed.  A sufficiently long saved-state
jump may therefore cross from one side of the interaction layer to the other
and transmit when both saved endpoint gaps are resolved.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import MaterialCurveProfile
from .material_scale_phase_diagram import minimum_rebound_depth
from .material_scale_response import returning_branch_is_monotone
from .scale_tunneling_1d import Wall1D, minimum_positive_clearance_crossing_displacement


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def minimum_gap_range_phase_count(
    clearance_sum: int,
    lower_gap: int,
    upper_gap: int,
) -> int:
    """Count ordered positive pairs with min gap in the inclusive interval."""
    if isinstance(clearance_sum, bool) or not isinstance(clearance_sum, int) or clearance_sum < 2:
        raise ValueError("clearance_sum must be an integer >=2")
    _require_positive("lower_gap", lower_gap)
    if isinstance(upper_gap, bool) or not isinstance(upper_gap, int):
        raise ValueError("upper_gap must be an integer")
    if upper_gap < lower_gap:
        return 0
    _require_positive("upper_gap", upper_gap)
    at_least_lower = max(0, clearance_sum - 2 * lower_gap + 1)
    at_least_after_upper = max(0, clearance_sum - 2 * (upper_gap + 1) + 1)
    return at_least_lower - at_least_after_upper


@dataclass(frozen=True)
class ClosedFormMaterialPhaseMass1D:
    clearance_sum: int
    positive_clearance_phases: int
    collapse_factor: int
    material_max_depth: int
    minimum_rebound_depth: int | None
    transmitting_phases: int
    underresolved_phases: int
    zero_return_phases: int
    rebound_phases: int

    @property
    def interaction_phases(self) -> int:
        return self.underresolved_phases + self.zero_return_phases + self.rebound_phases


def closed_form_material_phase_mass(
    clearance_sum: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> ClosedFormMaterialPhaseMass1D:
    """Return exact four-way phase counts for a monotone finite return branch."""
    if isinstance(clearance_sum, bool) or not isinstance(clearance_sum, int) or clearance_sum < 2:
        raise ValueError("clearance_sum must be an integer >=2")
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("incoming_budget", incoming_budget)
    if not profile.returning or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if not returning_branch_is_monotone(profile):
        raise ValueError("returning branch must be nondecreasing for interval phase counts")

    d = collapse_factor
    total = clearance_sum - 1
    transmitting = max(0, clearance_sum - 2 * d + 1)
    interaction = total - transmitting
    max_depth = len(profile.returning) - 1
    represented_depth = min(max_depth, d - 1)

    if represented_depth <= 0:
        underresolved = interaction
        zero_return = 0
        rebound = 0
        first = None
    else:
        represented_low_gap = d - represented_depth
        underresolved = minimum_gap_range_phase_count(
            clearance_sum,
            1,
            represented_low_gap - 1,
        )
        first_global = minimum_rebound_depth(incoming_budget, profile)
        first = (
            first_global
            if first_global is not None and first_global <= represented_depth
            else None
        )
        if first is None:
            zero_return = minimum_gap_range_phase_count(
                clearance_sum,
                represented_low_gap,
                d - 1,
            )
            rebound = 0
        else:
            rebound = minimum_gap_range_phase_count(
                clearance_sum,
                represented_low_gap,
                d - first,
            )
            zero_return = minimum_gap_range_phase_count(
                clearance_sum,
                d - first + 1,
                d - 1,
            )

    if transmitting + underresolved + zero_return + rebound != total:
        raise AssertionError("closed-form phase masses failed total conservation")
    if underresolved + zero_return + rebound != interaction:
        raise AssertionError("closed-form interaction phase masses failed conservation")
    return ClosedFormMaterialPhaseMass1D(
        clearance_sum=clearance_sum,
        positive_clearance_phases=total,
        collapse_factor=d,
        material_max_depth=max_depth,
        minimum_rebound_depth=first,
        transmitting_phases=transmitting,
        underresolved_phases=underresolved,
        zero_return_phases=zero_return,
        rebound_phases=rebound,
    )


def closed_form_wall_phase_mass(
    wall: Wall1D,
    radius: int,
    displacement: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> ClosedFormMaterialPhaseMass1D | None:
    """Wall/body wrapper; returns None when no separated positive-gap phase exists."""
    _require_nonnegative("radius", radius)
    _require_nonnegative("displacement", displacement)
    effective = minimum_positive_clearance_crossing_displacement(wall, radius)
    clearance_sum = displacement - effective + 2
    if clearance_sum < 2:
        return None
    return closed_form_material_phase_mass(
        clearance_sum,
        collapse_factor,
        incoming_budget,
        profile,
    )
