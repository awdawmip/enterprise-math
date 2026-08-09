"""Closed-form nD state masses for the finite effective material interaction layer.

The positive coarse-only clearance box at collapse factor ``d`` is

    {0,...,d-1}^n \ {(0,...,0)},

with ``d^n-1`` states.  Coarse layer depth is

    k = d-max(g_i),

and shell multiplicity is

    M_n(d,k) = (d-k+1)^n - (d-k)^n.

For a finite nondecreasing returning material branch with maximum depth ``K``
put ``K'=min(K,d-1)``.  For incoming budget ``B`` let ``k_B`` be the first
represented depth resolving one nonzero return quantum.  Then the box splits
exactly into zero-return outer states, true-rebound represented states, and
underresolved inner states.

If ``k_B`` exists within the represented depth range,

    N_under = (d-K')^n - 1,
    N_rebound = (d-k_B+1)^n - (d-K')^n,
    N_zero = d^n - (d-k_B+1)^n.

If no represented depth returns a nonzero quantum, ``N_rebound=0`` and all
represented states are zero-return.  Their sum is always ``d^n-1``.  In one
dimension these state counts reduce exactly to the effective shell thicknesses.

These are finite clearance-state multiplicities, not continuum volumes or
probabilities.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_clearance_response_spectrum import material_clearance_coverage
from .material_response import MaterialCurveProfile
from .material_scale_phase_diagram import minimum_rebound_depth
from .material_scale_response import returning_branch_is_monotone


@dataclass(frozen=True)
class EffectiveMaterialStateMassND:
    dimension: int
    collapse_factor: int
    incoming_budget: int
    material_max_depth: int
    represented_max_depth: int
    minimum_rebound_depth: int | None
    coarse_only_states: int
    underresolved_states: int
    zero_return_states: int
    rebound_states: int

    @property
    def represented_states(self) -> int:
        return self.zero_return_states + self.rebound_states


def effective_material_state_mass_nd(
    dimension: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> EffectiveMaterialStateMassND:
    """Return the exact nD zero/rebound/underresolved coarse-state partition."""
    for name, value in (("dimension", dimension), ("collapse_factor", collapse_factor)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")
    if not profile.returning or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if not returning_branch_is_monotone(profile):
        raise ValueError("returning branch must be nondecreasing for contiguous depth classes")

    max_depth = len(profile.returning) - 1
    coverage = material_clearance_coverage(
        dimension,
        collapse_factor,
        max_depth,
    )
    represented_max = coverage.effective_represented_depth
    first = minimum_rebound_depth(incoming_budget, profile)
    k_min = first if first is not None and first <= represented_max else None

    underresolved = coverage.underresolved_states
    if k_min is None:
        rebound = 0
        zero_return = coverage.represented_states
    else:
        inner_side = collapse_factor - represented_max
        rebound_outer_side = collapse_factor - k_min + 1
        rebound = rebound_outer_side**dimension - inner_side**dimension
        zero_return = collapse_factor**dimension - rebound_outer_side**dimension

    if zero_return + rebound != coverage.represented_states:
        raise AssertionError("represented nD material-state partition lost states")
    if zero_return + rebound + underresolved != coverage.coarse_only_states:
        raise AssertionError("nD material-state partition failed coarse-box conservation")
    return EffectiveMaterialStateMassND(
        dimension=dimension,
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        material_max_depth=max_depth,
        represented_max_depth=represented_max,
        minimum_rebound_depth=k_min,
        coarse_only_states=coverage.coarse_only_states,
        underresolved_states=underresolved,
        zero_return_states=zero_return,
        rebound_states=rebound,
    )
