"""Exact finite horizon after which kinematic response aliasing never returns.

For a finite response alphabet ``S`` on amplitude ``A``, the scalar kinematic
quotient at incoming budget ``B`` is ``K_B(r)=floor(B*r/A)``.  The minimum
positive response gap gives a simple sufficient injectivity bound, but favorable
remainders can make the last alias disappear earlier.

Because no alias can occur at or above that sufficient bound, the exact
permanent injectivity threshold is finite:

    B_stable = 1 + max { B below the bound : K_B is not injective },

with threshold zero for a singleton response alphabet.

The 2D anisotropy specialization uses only material depths reachable at the
declared spatial collapse factor.  Its exact threshold is the earliest budget
after which the kinematic quotient permanently requires the same clearance
observable as the *reachable raw material law*.  Unreachable deeper anisotropy
must not force current geometric precision.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_anisotropy_2d import AnisotropicMaterialProfile2D
from .material_anisotropy_visibility_2d import kinematic_anisotropy_visibility_2d
from .clearance_precision import ACTIVE_COUNT, ACTIVE_SET, SCALAR_DEPTH
from .material_hysteresis import LOADING, RETURNING
from .material_response_aliasing import (
    guaranteed_injective_budget,
    kinematic_response_partition,
)


@dataclass(frozen=True)
class PermanentAliasStability:
    responses: tuple[int, ...]
    amplitude: int
    guaranteed_injective_budget: int | None
    exact_permanent_injective_budget: int
    last_noninjective_budget: int | None


def permanent_alias_stability(
    responses: tuple[int, ...] | list[int],
    amplitude: int,
) -> PermanentAliasStability:
    """Return the exact first budget after which this alphabet stays injective."""
    values = tuple(sorted(set(responses)))
    if not values:
        raise ValueError("at least one material response is required")
    guaranteed = guaranteed_injective_budget(values, amplitude)
    if len(values) == 1:
        return PermanentAliasStability(
            responses=values,
            amplitude=amplitude,
            guaranteed_injective_budget=None,
            exact_permanent_injective_budget=0,
            last_noninjective_budget=None,
        )
    if guaranteed is None:
        raise AssertionError("multi-class response alphabet lost injectivity bound")

    last_alias: int | None = None
    for budget in range(guaranteed):
        if not kinematic_response_partition(values, budget, amplitude).injective:
            last_alias = budget
    stable = 0 if last_alias is None else last_alias + 1
    if stable > guaranteed:
        raise AssertionError("exact permanent threshold exceeded sufficient bound")
    for budget in range(stable, guaranteed + 1):
        if not kinematic_response_partition(values, budget, amplitude).injective:
            raise AssertionError("alias reappeared after exact permanent threshold")
    return PermanentAliasStability(
        responses=values,
        amplitude=amplitude,
        guaranteed_injective_budget=guaranteed,
        exact_permanent_injective_budget=stable,
        last_noninjective_budget=last_alias,
    )


def _branch_triplet(
    profile: AnisotropicMaterialProfile2D,
    branch: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if branch == LOADING:
        return (
            profile.x_profile.loading,
            profile.y_profile.loading,
            profile.corner_profile.loading,
        )
    if branch == RETURNING:
        return (
            profile.x_profile.returning,
            profile.y_profile.returning,
            profile.corner_profile.returning,
        )
    raise ValueError("branch must be LOADING or RETURNING")


def _reachable_raw_observable(
    x: tuple[int, ...],
    y: tuple[int, ...],
    corner: tuple[int, ...],
    represented_max_depth: int,
) -> str:
    required = SCALAR_DEPTH
    for depth in range(1, represented_max_depth + 1):
        xv, yv, cv = x[depth], y[depth], corner[depth]
        if xv != yv:
            return ACTIVE_SET
        if xv != cv:
            required = ACTIVE_COUNT
    return required


@dataclass(frozen=True)
class PermanentAnisotropyVisibility2D:
    collapse_factor: int
    branch: str
    represented_max_depth: int
    reachable_raw_minimum_clearance_observable: str
    guaranteed_response_injective_budget: int | None
    exact_permanent_observable_budget: int
    last_budget_with_coarser_observable: int | None


def permanent_anisotropy_visibility_2d(
    profile: AnisotropicMaterialProfile2D,
    collapse_factor: int,
    branch: str = RETURNING,
) -> PermanentAnisotropyVisibility2D:
    """Exact first budget after which reachable raw anisotropy precision persists."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    x, y, corner = _branch_triplet(profile, branch)
    represented_max = min(profile.depth_count - 1, collapse_factor - 1)
    raw = _reachable_raw_observable(x, y, corner, represented_max)
    if represented_max <= 0:
        return PermanentAnisotropyVisibility2D(
            collapse_factor=collapse_factor,
            branch=branch,
            represented_max_depth=0,
            reachable_raw_minimum_clearance_observable=SCALAR_DEPTH,
            guaranteed_response_injective_budget=None,
            exact_permanent_observable_budget=0,
            last_budget_with_coarser_observable=None,
        )

    reachable_responses = tuple(
        value
        for depth in range(1, represented_max + 1)
        for value in (x[depth], y[depth], corner[depth])
    )
    alias = permanent_alias_stability(reachable_responses, profile.amplitude)
    guaranteed = alias.guaranteed_injective_budget or 0

    last_coarser: int | None = None
    for budget in range(guaranteed + 1):
        observed = kinematic_anisotropy_visibility_2d(
            profile,
            collapse_factor,
            budget,
            branch,
        ).minimum_clearance_observable
        if observed != raw:
            last_coarser = budget
    stable = 0 if last_coarser is None else last_coarser + 1
    for budget in range(stable, guaranteed + 1):
        observed = kinematic_anisotropy_visibility_2d(
            profile,
            collapse_factor,
            budget,
            branch,
        ).minimum_clearance_observable
        if observed != raw:
            raise AssertionError("anisotropy observable changed after permanent threshold")
    return PermanentAnisotropyVisibility2D(
        collapse_factor=collapse_factor,
        branch=branch,
        represented_max_depth=represented_max,
        reachable_raw_minimum_clearance_observable=raw,
        guaranteed_response_injective_budget=alias.guaranteed_injective_budget,
        exact_permanent_observable_budget=stable,
        last_budget_with_coarser_observable=last_coarser,
    )
