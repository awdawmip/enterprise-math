"""Scale-response monotonicity for the coarse collapse-material wall toy world.

Fix a positive sampled controlling clearance ``g`` and incoming motion budget
``B``.  While ``d>g``, the coarse interaction-layer depth is ``k=d-g``.  If the
RETURNING branch is nondecreasing in deformation index, then

    floor(B*R_k/A)

is also nondecreasing in ``k``.  Therefore coarse-to-fine refinement (decreasing
``d``) can only weakly reduce the returned motion budget, until ``d<=g`` removes
the coarse-only layer and the sampled transition is accepted/transmitted.

This is a theorem of the declared toy coupling, not a physical restitution law.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_collapse_world_1d import (
    REBOUND,
    CollapseMaterialWorldOutcome1D,
    collapse_material_wall_step,
)
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import Wall1D


@dataclass(frozen=True)
class RefinementReboundProfile1D:
    """One coarse-to-fine sequence for a fixed sampled wall proposal."""

    factors: tuple[int, ...]
    outcomes: tuple[CollapseMaterialWorldOutcome1D, ...]
    rebound_budgets: tuple[int | None, ...]
    returning_branch_monotone: bool
    rebound_weakens_under_refinement: bool


def returning_branch_is_monotone(profile: MaterialCurveProfile) -> bool:
    """Whether return response is nondecreasing with deformation depth."""
    return all(
        left <= right
        for left, right in zip(profile.returning, profile.returning[1:])
    )


def refinement_rebound_profile(
    wall: Wall1D,
    start_center: int,
    proposed_end_center: int,
    radius: int,
    coarsest_factor: int,
    material_profile: MaterialCurveProfile,
) -> RefinementReboundProfile1D:
    """Evaluate every integer factor from ``coarsest_factor`` down to terminal 1."""
    if (
        isinstance(coarsest_factor, bool)
        or not isinstance(coarsest_factor, int)
        or coarsest_factor <= 0
    ):
        raise ValueError("coarsest_factor must be a positive integer")
    monotone = returning_branch_is_monotone(material_profile)
    factors = tuple(range(coarsest_factor, 0, -1))
    outcomes = tuple(
        collapse_material_wall_step(
            wall,
            start_center,
            proposed_end_center,
            radius,
            factor,
            material_profile,
        )
        for factor in factors
    )
    budgets = tuple(
        None if outcome.rebound is None else outcome.rebound.returned_budget
        for outcome in outcomes
    )

    # Ignore post-extinction None values and check only the rebound segment.
    rebound_values = tuple(
        outcome.rebound.returned_budget
        for outcome in outcomes
        if outcome.kind == REBOUND and outcome.rebound is not None
    )
    weakens = all(
        later <= earlier
        for earlier, later in zip(rebound_values, rebound_values[1:])
    )
    if monotone and not weakens:
        raise AssertionError("monotone return branch produced stronger rebound under refinement")

    return RefinementReboundProfile1D(
        factors=factors,
        outcomes=outcomes,
        rebound_budgets=budgets,
        returning_branch_monotone=monotone,
        rebound_weakens_under_refinement=weakens,
    )
