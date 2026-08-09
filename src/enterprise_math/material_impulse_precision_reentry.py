"""Exact coarsening re-entry family for the causal finite impulse material world.

The older direct-response scale diagram could be interval-like because a fixed
positive gap mapped directly to one material depth and one immediate returned
budget.  Causal impulse dynamics is richer: zero-force saved drift can skip
material depths before the next force sample.

This module gives an infinite integer family where material underresolution is
**not monotone under spatial coarsening** even though the loading branch is
nondecreasing.

Choose integers

    q >= 2,
    K >= q+1,
    g >= q+1.

Use amplitude 1, unit mass, inward whole momentum ``p=q``, full-scale impulse
capacity ``J=q``, and a material branch that is zero at depths ``0..K-1`` and
one at depth ``K``.  Fix primitive gap ``g`` and define

    d_hit   = g + K - q,
    d_under = d_hit + 1,
    d_rein  = g + K.

At ``d_hit`` the first zero-force drift of q cells lands exactly on depth K, so
the following kicks stall and reverse momentum.  At ``d_under`` the same drift
lands on depth K+1, so the next saved state is MATERIAL_UNDERRESOLVED.  At
``d_rein`` the initial saved state already lies on depth K and force acts before
any inward drift, restoring reversal.

Hence the exact deterministic outcome pattern is

    REVERSE -> UNDERRESOLVED -> REVERSE

under strictly increasing collapse factor.  The mechanism is saved-state phase
alignment, not nonmonotone material force.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_world_1d import (
    CROSSING_TRANSMIT,
    MATERIAL_UNDERRESOLVED,
    TERMINAL_CONTACT,
    ImpulseMaterialHistory1D,
    MomentumMaterialState1D,
    run_impulse_material_world_1d,
)
from .material_response import MaterialCurveProfile, explicit_material_curve_profile
from .scale_tunneling_1d import Wall1D

REVERSE = "REVERSE"
UNDERRESOLVED = MATERIAL_UNDERRESOLVED
TRANSMIT = "TRANSMIT"
TERMINAL = TERMINAL_CONTACT
NO_REVERSAL = "NO_REVERSAL"


@dataclass(frozen=True)
class ImpulsePrecisionReentryWitness:
    inward_drift_cells: int
    material_max_depth: int
    primitive_gap: int
    hit_factor: int
    underresolved_factor: int
    reentry_factor: int
    profile: MaterialCurveProfile
    hit_history: ImpulseMaterialHistory1D
    underresolved_history: ImpulseMaterialHistory1D
    reentry_history: ImpulseMaterialHistory1D
    outcome_pattern: tuple[str, str, str]


def classify_impulse_history(history: ImpulseMaterialHistory1D) -> str:
    if history.first_reversal_tick is not None:
        return REVERSE
    if history.halted_kind == MATERIAL_UNDERRESOLVED:
        return UNDERRESOLVED
    if history.halted_kind == TERMINAL_CONTACT:
        return TERMINAL
    if any(
        transition.kind == CROSSING_TRANSMIT
        for transition in history.transitions
    ):
        return TRANSMIT
    return NO_REVERSAL


def precision_reentry_witness(
    inward_drift_cells: int,
    material_max_depth: int,
    primitive_gap: int,
) -> ImpulsePrecisionReentryWitness:
    """Construct and verify one member of the exact R-U-R coarsening family."""
    q = inward_drift_cells
    K = material_max_depth
    g = primitive_gap
    for name, value in (("inward_drift_cells", q), ("material_max_depth", K), ("primitive_gap", g)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if q < 2:
        raise ValueError("inward_drift_cells must be at least 2")
    if K < q + 1:
        raise ValueError("material_max_depth must be at least q+1")
    if g < q + 1:
        raise ValueError("primitive_gap must exceed the zero-force drift")

    samples = (0,) * K + (1,)
    profile = explicit_material_curve_profile(samples, samples, amplitude=1)
    initial = MomentumMaterialState1D(center=-g, momentum_quanta=q)
    wall = Wall1D(0, 0)
    d_hit = g + K - q
    d_under = d_hit + 1
    d_rein = g + K

    def run(factor: int) -> ImpulseMaterialHistory1D:
        return run_impulse_material_world_1d(
            initial,
            wall,
            radius=0,
            collapse_factor=factor,
            material_profile=profile,
            mass_quanta=1,
            max_impulse_per_tick=q,
            ticks=4,
            retain_impulse_detail=True,
        )

    hit = run(d_hit)
    under = run(d_under)
    rein = run(d_rein)
    pattern = (
        classify_impulse_history(hit),
        classify_impulse_history(under),
        classify_impulse_history(rein),
    )
    expected = (REVERSE, UNDERRESOLVED, REVERSE)
    if pattern != expected:
        raise AssertionError("constructed impulse precision re-entry witness failed")
    return ImpulsePrecisionReentryWitness(
        inward_drift_cells=q,
        material_max_depth=K,
        primitive_gap=g,
        hit_factor=d_hit,
        underresolved_factor=d_under,
        reentry_factor=d_rein,
        profile=profile,
        hit_history=hit,
        underresolved_history=under,
        reentry_history=rein,
        outcome_pattern=pattern,
    )
