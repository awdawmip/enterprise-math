"""Exact precision/deformation thresholds for integer rebound budget steps.

For incoming budget ``B`` and a nondecreasing RETURNING branch ``R_k`` on
amplitude scale ``A``, the declared coupling returns

    b_k = floor(B*R_k/A).

For each integer rebound level ``m=1..B``:

    b_k >= m  iff  R_k >= ceil(m*A/B).

Thus every additional returned unit has an exact response-sample threshold and,
for a fixed positive primitive clearance ``g`` in the collapse layer, an exact
spatial-factor onset ``d_m=g+k_m`` where ``k_m`` is the first represented depth
meeting that threshold.

No real restitution coefficient is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import MaterialCurveProfile
from .material_scale_response import returning_branch_is_monotone


@dataclass(frozen=True)
class ReboundStepThreshold:
    """Onset of one additional integer returned-budget unit."""

    returned_budget_level: int
    minimum_response_sample: int
    first_deformation_depth: int | None
    first_collapse_factor: int | None


@dataclass(frozen=True)
class ReboundStaircase:
    """All integer rebound-step onsets for one budget/material/gap tuple."""

    incoming_budget: int
    amplitude: int
    controlling_gap: int
    thresholds: tuple[ReboundStepThreshold, ...]
    maximum_representable_returned_budget: int


def _ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def rebound_staircase(
    profile: MaterialCurveProfile,
    incoming_budget: int,
    controlling_gap: int,
) -> ReboundStaircase:
    """Return exact depth/factor thresholds for every possible returned unit."""
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")
    if (
        isinstance(controlling_gap, bool)
        or not isinstance(controlling_gap, int)
        or controlling_gap <= 0
    ):
        raise ValueError("controlling_gap must be a positive integer")
    if not returning_branch_is_monotone(profile):
        raise ValueError("rebound staircase requires a nondecreasing return branch")

    if incoming_budget == 0:
        return ReboundStaircase(
            incoming_budget=0,
            amplitude=profile.amplitude,
            controlling_gap=controlling_gap,
            thresholds=(),
            maximum_representable_returned_budget=0,
        )

    thresholds: list[ReboundStepThreshold] = []
    for level in range(1, incoming_budget + 1):
        minimum_sample = _ceil_div(level * profile.amplitude, incoming_budget)
        depth = next(
            (
                index
                for index, sample in enumerate(profile.returning)
                if index >= 1 and sample >= minimum_sample
            ),
            None,
        )
        factor = None if depth is None else controlling_gap + depth
        thresholds.append(
            ReboundStepThreshold(
                returned_budget_level=level,
                minimum_response_sample=minimum_sample,
                first_deformation_depth=depth,
                first_collapse_factor=factor,
            )
        )

    maximum = max(
        (
            threshold.returned_budget_level
            for threshold in thresholds
            if threshold.first_deformation_depth is not None
        ),
        default=0,
    )
    return ReboundStaircase(
        incoming_budget=incoming_budget,
        amplitude=profile.amplitude,
        controlling_gap=controlling_gap,
        thresholds=tuple(thresholds),
        maximum_representable_returned_budget=maximum,
    )
