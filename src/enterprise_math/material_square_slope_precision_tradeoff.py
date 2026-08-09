"""Space/time/momentum precision tradeoff for the exact square-slope family.

For loading force ``L_k=b^2*k`` on a unit deformation grid:

    W2_L(K)=(b*K)^2.

Hence exact whole-momentum turns occur on the momentum lattice ``p=b*K``.  For
an exactly supported incoming momentum p, the represented turning depth is
``K=p/b`` and the positive-gap collapse layer must have at least that depth:

    d_min = p/b + 1.

The same branch has depth-independent natural loading duration ``2*m/b``.  Its
minimal rational time-grid denominator is

    b/gcd(2*m,b).

Thus increasing b reduces spatial interaction depth for supported momentum while
coarsening the exact momentum lattice and usually increasing the time denominator.
This is an exact finite resource exchange, not a continuum stiffness asymptotic.

Adding returning root a<=b gives momentum retention ``a/b`` and a second time-grid
denominator ``a/gcd(2*m,a)``.  The exact full bounce clock uses their LCM.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .material_square_slope_clock import compile_square_slope_clock


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class SquareSlopePrecisionTradeoff:
    loading_root: int
    returning_root: int
    mass_count: int
    max_depth: int
    exact_incoming_momentum_step: int
    exact_outgoing_momentum_step: int | None
    max_exact_incoming_momentum: int
    exact_incoming_state_count: int
    momentum_span_state_count: int
    loading_time_grid_denominator: int
    returning_time_grid_denominator: int | None
    full_bounce_time_grid_denominator: int
    max_supported_min_collapse_factor: int
    retention_numerator: int
    retention_denominator: int

    @property
    def exact_momentum_coverage_numerator(self) -> int:
        return self.exact_incoming_state_count

    @property
    def exact_momentum_coverage_denominator(self) -> int:
        return self.momentum_span_state_count


def square_slope_precision_tradeoff(
    max_depth: int,
    loading_root: int,
    returning_root: int,
    mass_count: int = 1,
) -> SquareSlopePrecisionTradeoff:
    _positive("max_depth", max_depth)
    _positive("loading_root", loading_root)
    if isinstance(returning_root, bool) or not isinstance(returning_root, int) or returning_root < 0:
        raise ValueError("returning_root must be a non-negative integer")
    if returning_root > loading_root:
        raise ValueError("returning_root must not exceed loading_root")
    _positive("mass_count", mass_count)
    clock = compile_square_slope_clock(
        max_depth,
        loading_root,
        returning_root,
        mass_count=mass_count,
    )
    load_den = loading_root // gcd(2 * mass_count, loading_root)
    return_den = (
        None
        if returning_root == 0
        else returning_root // gcd(2 * mass_count, returning_root)
    )
    combined = load_den if return_den is None else lcm(load_den, return_den)
    if combined != clock.minimal_time_grid_denominator:
        raise AssertionError("square-slope tradeoff disagrees with clock compiler")
    max_momentum = loading_root * max_depth
    return SquareSlopePrecisionTradeoff(
        loading_root=loading_root,
        returning_root=returning_root,
        mass_count=mass_count,
        max_depth=max_depth,
        exact_incoming_momentum_step=loading_root,
        exact_outgoing_momentum_step=None if returning_root == 0 else returning_root,
        max_exact_incoming_momentum=max_momentum,
        exact_incoming_state_count=max_depth,
        momentum_span_state_count=max_momentum,
        loading_time_grid_denominator=load_den,
        returning_time_grid_denominator=return_den,
        full_bounce_time_grid_denominator=combined,
        max_supported_min_collapse_factor=max_depth + 1,
        retention_numerator=clock.material.retention_numerator,
        retention_denominator=clock.material.retention_denominator,
    )


def minimum_collapse_factor_for_exact_incoming_momentum(
    incoming_momentum: int,
    loading_root: int,
) -> int | None:
    """Return p/b+1 when p lies on the exact square-slope momentum lattice."""
    _positive("incoming_momentum", incoming_momentum)
    _positive("loading_root", loading_root)
    if incoming_momentum % loading_root:
        return None
    return incoming_momentum // loading_root + 1
