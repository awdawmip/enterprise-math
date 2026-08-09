"""Exact precision phase diagram for one triggered 1D material interaction.

Fix a positive primitive controlling gap ``g``, incoming integer motion budget
``B``, collapse factor ``d``, and a finite returning material branch ``R_k`` on
amplitude ``A``.  Positive coarse-only interaction has depth

    k = d-g.

Conditional on the world declaring that this represented contact should request a
material response, four finite precision phases are possible:

* RESOLVED: ``d<=g`` so the positive gap is visible and no coarse interaction exists;
* ZERO_RETURN: ``1<=k<=K`` is represented but ``B*R_k < A``;
* REBOUND: ``1<=k<=K`` and ``B*R_k >= A`` so at least one return quantum exists;
* UNDERRESOLVED: ``k>K`` exceeds the finite material deformation domain.

Here ``K=len(returning)-1``.  If the returning branch is nondecreasing in depth,
let

    k_B = min { k in 1..K : B*R_k >= A }.

When this set is nonempty, increasing ``d`` at fixed ``g`` moves through the
ordered interval structure

    RESOLVED -> ZERO_RETURN -> REBOUND -> UNDERRESOLVED

with exact boundaries

    d <= g,
    g < d < g+k_B,
    g+k_B <= d <= g+K,
    d > g+K.

If no ``k_B`` exists, the represented segment is entirely ZERO_RETURN.  Thus
coarsening strengthens represented response only inside the finite material
domain; excessive coarsening becomes explicitly underresolved rather than
silently hardening forever.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_kinematic_response_spectrum import minimum_budget_for_nonzero_return
from .material_response import MaterialCurveProfile
from .material_scale_response import returning_branch_is_monotone

RESOLVED_PHASE = "RESOLVED"
ZERO_RETURN_PHASE = "ZERO_RETURN"
REBOUND_PHASE = "REBOUND"
UNDERRESOLVED_PHASE = "UNDERRESOLVED"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


@dataclass(frozen=True)
class ScaleResponsePhase1D:
    primitive_gap: int
    collapse_factor: int
    incoming_budget: int
    material_max_depth: int
    layer_depth: int | None
    response_sample: int | None
    minimum_budget_for_sample: int | None
    returned_budget: int | None
    phase: str


def scale_response_phase_for_gap(
    primitive_gap: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> ScaleResponsePhase1D:
    """Classify one fixed-gap triggered interaction at one spatial precision."""
    _require_positive("primitive_gap", primitive_gap)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("incoming_budget", incoming_budget)
    if not profile.returning or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    max_depth = len(profile.returning) - 1

    if collapse_factor <= primitive_gap:
        return ScaleResponsePhase1D(
            primitive_gap=primitive_gap,
            collapse_factor=collapse_factor,
            incoming_budget=incoming_budget,
            material_max_depth=max_depth,
            layer_depth=None,
            response_sample=None,
            minimum_budget_for_sample=None,
            returned_budget=None,
            phase=RESOLVED_PHASE,
        )

    depth = collapse_factor - primitive_gap
    if depth > max_depth:
        return ScaleResponsePhase1D(
            primitive_gap=primitive_gap,
            collapse_factor=collapse_factor,
            incoming_budget=incoming_budget,
            material_max_depth=max_depth,
            layer_depth=depth,
            response_sample=None,
            minimum_budget_for_sample=None,
            returned_budget=None,
            phase=UNDERRESOLVED_PHASE,
        )

    sample = profile.returning[depth]
    minimum_budget = minimum_budget_for_nonzero_return(sample, profile.amplitude)
    returned = incoming_budget * sample // profile.amplitude
    phase = REBOUND_PHASE if returned > 0 else ZERO_RETURN_PHASE
    return ScaleResponsePhase1D(
        primitive_gap=primitive_gap,
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        material_max_depth=max_depth,
        layer_depth=depth,
        response_sample=sample,
        minimum_budget_for_sample=minimum_budget,
        returned_budget=returned,
        phase=phase,
    )


def minimum_rebound_depth(
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> int | None:
    """First positive material depth resolving one return quantum, if any."""
    _require_nonnegative("incoming_budget", incoming_budget)
    for depth, sample in enumerate(profile.returning[1:], start=1):
        if incoming_budget * sample >= profile.amplitude:
            return depth
    return None


@dataclass(frozen=True)
class MonotoneScalePhaseThresholds1D:
    primitive_gap: int
    incoming_budget: int
    material_max_depth: int
    minimum_rebound_depth: int | None
    resolved_max_factor: int
    zero_return_factor_range: tuple[int, int] | None
    rebound_factor_range: tuple[int, int] | None
    underresolved_min_factor: int


def monotone_scale_phase_thresholds(
    primitive_gap: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> MonotoneScalePhaseThresholds1D:
    """Return exact integer d-ranges when the return branch is nondecreasing."""
    _require_positive("primitive_gap", primitive_gap)
    _require_nonnegative("incoming_budget", incoming_budget)
    if not returning_branch_is_monotone(profile):
        raise ValueError("returning branch must be nondecreasing for interval thresholds")
    max_depth = len(profile.returning) - 1
    k_min = minimum_rebound_depth(incoming_budget, profile)
    represented_lo = primitive_gap + 1
    represented_hi = primitive_gap + max_depth
    if max_depth == 0:
        zero_range = None
        rebound_range = None
    elif k_min is None:
        zero_range = (represented_lo, represented_hi)
        rebound_range = None
    else:
        zero_hi = primitive_gap + k_min - 1
        zero_range = (
            None if zero_hi < represented_lo else (represented_lo, zero_hi)
        )
        rebound_range = (primitive_gap + k_min, represented_hi)
    return MonotoneScalePhaseThresholds1D(
        primitive_gap=primitive_gap,
        incoming_budget=incoming_budget,
        material_max_depth=max_depth,
        minimum_rebound_depth=k_min,
        resolved_max_factor=primitive_gap,
        zero_return_factor_range=zero_range,
        rebound_factor_range=rebound_range,
        underresolved_min_factor=primitive_gap + max_depth + 1,
    )
