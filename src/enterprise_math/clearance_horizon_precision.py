"""Horizon-indexed future-safe precision for finite clearance states.

This module is a concrete P024 specialization.  Axis ``i`` has positive coarse
factor ``d_i`` and represented clearance coordinate ``g_i``.  The interaction
box is

    0 <= g_i < d_i  for every i.

For an inside state put

    m_i = d_i - g_i,
    k   = min_i m_i,
    r_i = m_i - k.

``k`` is the shortest number of named primitive ``+e_i`` actions needed to
leave the interaction box.  If future action words have total length at most
``h`` and the future observable is only the scalar residual escape depth, then
the coarsest exact state is

    (k, min(r_1,h), ..., min(r_n,h)).

Deficits deeper than the remaining horizon cannot influence any scalar-depth
future inside that horizon.

The quotient is itself closed under consuming named primitive actions.  This
module also gives exact class counts for named anisotropic axes and for the
isotropic quotient after full coordinate-permutation symmetry.

These are finite future-signature formulas; they do not identify spatial factor,
material amplitude precision, measurement scale, or physical length.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

INSIDE = "INSIDE"
OUTSIDE = "OUTSIDE"


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _validated_factors(axis_factors: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    factors = tuple(axis_factors)
    if not factors:
        raise ValueError("axis_factors must be nonempty")
    for factor in factors:
        _require_positive("axis factor", factor)
    return factors


@dataclass(frozen=True)
class ClearanceHorizonState:
    """Coarsest scalar-depth future signature at one remaining horizon."""

    axis_factors: tuple[int, ...]
    horizon: int
    status: str
    escape_depth: int
    capped_deficits: tuple[int, ...]

    @property
    def dimension(self) -> int:
        return len(self.axis_factors)


def clearance_escape_depth(
    clearance: tuple[int, ...] | list[int],
    axis_factors: tuple[int, ...] | list[int],
) -> int:
    """Return shortest named ``+e_i`` escape length, or 0 outside the box."""
    factors = _validated_factors(axis_factors)
    state = tuple(clearance)
    if len(state) != len(factors):
        raise ValueError("clearance and axis_factors must have equal dimension")
    for value in state:
        _require_nonnegative("clearance coordinate", value)
    if any(value >= factor for value, factor in zip(state, factors, strict=True)):
        return 0
    return min(
        factor - value for value, factor in zip(state, factors, strict=True)
    )


def compile_clearance_horizon_state(
    clearance: tuple[int, ...] | list[int],
    axis_factors: tuple[int, ...] | list[int],
    horizon: int,
) -> ClearanceHorizonState:
    """Compile the exact horizon-h scalar-depth future quotient state."""
    _require_nonnegative("horizon", horizon)
    factors = _validated_factors(axis_factors)
    state = tuple(clearance)
    if len(state) != len(factors):
        raise ValueError("clearance and axis_factors must have equal dimension")
    for value in state:
        _require_nonnegative("clearance coordinate", value)

    depth = clearance_escape_depth(state, factors)
    if depth == 0:
        return ClearanceHorizonState(
            axis_factors=factors,
            horizon=horizon,
            status=OUTSIDE,
            escape_depth=0,
            capped_deficits=(),
        )

    margins = tuple(
        factor - value for value, factor in zip(state, factors, strict=True)
    )
    deficits = tuple(margin - depth for margin in margins)
    return ClearanceHorizonState(
        axis_factors=factors,
        horizon=horizon,
        status=INSIDE,
        escape_depth=depth,
        capped_deficits=tuple(min(deficit, horizon) for deficit in deficits),
    )


def residual_escape_depth_after_action_counts(
    clearance: tuple[int, ...] | list[int],
    axis_factors: tuple[int, ...] | list[int],
    action_counts: tuple[int, ...] | list[int],
) -> int:
    """Independent full-state oracle after a commutative count of named actions."""
    factors = _validated_factors(axis_factors)
    state = tuple(clearance)
    actions = tuple(action_counts)
    if len(state) != len(factors) or len(actions) != len(factors):
        raise ValueError("clearance, factors and actions must have equal dimension")
    for value in state:
        _require_nonnegative("clearance coordinate", value)
    for count in actions:
        _require_nonnegative("action count", count)
    post = tuple(value + count for value, count in zip(state, actions, strict=True))
    return clearance_escape_depth(post, factors)


def advance_clearance_horizon_state(
    state: ClearanceHorizonState,
    axis: int,
) -> ClearanceHorizonState:
    """Consume one named primitive action entirely inside the compact quotient."""
    if isinstance(axis, bool) or not isinstance(axis, int) or not 0 <= axis < state.dimension:
        raise ValueError("axis must identify one clearance coordinate")
    if state.horizon <= 0:
        raise ValueError("no future horizon remains to consume an action")
    next_horizon = state.horizon - 1
    if state.status == OUTSIDE:
        return ClearanceHorizonState(
            axis_factors=state.axis_factors,
            horizon=next_horizon,
            status=OUTSIDE,
            escape_depth=0,
            capped_deficits=(),
        )
    if state.status != INSIDE:
        raise ValueError("unknown clearance horizon state status")
    if len(state.capped_deficits) != state.dimension:
        raise ValueError("inside state must carry one capped deficit per axis")

    deficits = list(state.capped_deficits)
    if deficits[axis] == 0:
        if state.escape_depth == 1:
            return ClearanceHorizonState(
                axis_factors=state.axis_factors,
                horizon=next_horizon,
                status=OUTSIDE,
                escape_depth=0,
                capped_deficits=(),
            )
        next_depth = state.escape_depth - 1
        next_deficits = tuple(
            0 if index == axis else min(value + 1, next_horizon)
            for index, value in enumerate(deficits)
        )
    else:
        next_depth = state.escape_depth
        next_deficits = tuple(
            value - 1 if index == axis else min(value, next_horizon)
            for index, value in enumerate(deficits)
        )

    return ClearanceHorizonState(
        axis_factors=state.axis_factors,
        horizon=next_horizon,
        status=INSIDE,
        escape_depth=next_depth,
        capped_deficits=next_deficits,
    )


def anisotropic_named_horizon_class_count(
    axis_factors: tuple[int, ...] | list[int],
    horizon: int,
    exclude_primitive_origin: bool = True,
) -> int:
    """Return exact horizon-h quotient classes for named anisotropic axes.

    The subtraction term removes the all-zero primitive-clearance state only when
    the horizon is deep enough for its capped-deficit signature to be unique
    among the deepest-shell states.
    """
    _require_nonnegative("horizon", horizon)
    factors = _validated_factors(axis_factors)
    d_min = min(factors)
    total = 0
    for depth in range(1, d_min + 1):
        caps = tuple(min(horizon, factor - depth) for factor in factors)
        all_vectors = 1
        no_zero_vectors = 1
        for cap in caps:
            all_vectors *= cap + 1
            no_zero_vectors *= cap
        total += all_vectors - no_zero_vectors

    if exclude_primitive_origin:
        origin_unique_horizon = max(factor - d_min for factor in factors)
        if horizon >= origin_unique_horizon:
            total -= 1
    return total


def isotropic_named_horizon_class_count(
    dimension: int,
    collapse_factor: int,
    horizon: int,
) -> int:
    """Named-axis positive-clearance class count for isotropic factor d."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    return anisotropic_named_horizon_class_count(
        (collapse_factor,) * dimension,
        horizon,
        exclude_primitive_origin=True,
    )


def isotropic_named_horizon_closed_form(
    dimension: int,
    collapse_factor: int,
    horizon: int,
) -> int:
    """Closed form of the named isotropic count.

    For h<=d-1:

      (h+1)^n - 1 + (d-1-h)*((h+1)^n-h^n).

    For deeper horizons the quotient is already the full positive vector state.
    """
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    effective = min(horizon, collapse_factor - 1)
    shell = (effective + 1) ** dimension - effective**dimension
    return (
        (effective + 1) ** dimension
        - 1
        + (collapse_factor - 1 - effective) * shell
    )


def isotropic_horizon_growth_increment(
    dimension: int,
    collapse_factor: int,
    horizon: int,
) -> int:
    """Exact new quotient classes exposed by extending horizon h to h+1."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    if horizon >= collapse_factor - 1:
        return 0
    return (collapse_factor - 1 - horizon) * (
        (horizon + 2) ** dimension
        - 2 * (horizon + 1) ** dimension
        + horizon**dimension
    )


def permutation_symmetric_isotropic_class_count(
    dimension: int,
    collapse_factor: int,
    horizon: int,
) -> int:
    """Exact classes after also quotienting by full coordinate permutation symmetry.

    At fixed q=max(g), capped deficits use values 0..m with at least one zero,
    where m=min(h,q).  Under S_n only the histogram matters.  The number of such
    histograms is ``binom(n+m-1,m)``.
    """
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    return sum(
        comb(dimension + min(horizon, q) - 1, min(horizon, q))
        for q in range(1, collapse_factor)
    )
