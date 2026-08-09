"""Square-slope linear force families with exact integer work/momentum closure.

On a unit deformation grid, the linear force branch

    F_k = c*k

has doubled chord work

    W_2(K) = c*K^2.

Therefore choosing square branch slopes

    L_k = b^2*k,
    R_k = a^2*k,       0 <= a <= b,

makes every represented loading and returning work prefix a perfect square:

    W_L,2(K) = (b*K)^2,
    W_R,2(K) = (a*K)^2.

Under unit mass/force/deformation/momentum scales, an incoming whole momentum
``b*K`` turns exactly at depth K and a full return releases exactly enough work
for outgoing whole momentum ``a*K``.  The momentum retention ratio is therefore
``a/b`` and the dissipated doubled-work resource is

    (b^2-a^2)K^2.

Thus any rational retention ``a/b`` in [0,1] can be realized as a finite material
loading/returning work structure rather than an explicit post-collision velocity
rule.  ``a=b`` is elastic; ``a=0`` has no return work.

More generally, linear slopes sharing one squarefree factor remain in the same
quadratic momentum field; square slopes are the stronger whole-integer closure
case.  This is a synthesis/comparator family, not a claim that real materials are
linear or that measured restitution is determined only by two slopes.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_force_work import FiniteForceLaw, force_cycle_work_report, uniform_force_law
from .material_response import explicit_material_curve_profile
from .material_work_energy_oracle import static_material_rebound_report
from .material_work_momentum_closure import material_rebound_momentum_closure_report


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class SquareSlopeMaterialFamily:
    max_depth: int
    loading_momentum_root: int
    returning_momentum_root: int
    law: FiniteForceLaw
    retention_numerator: int
    retention_denominator: int


def square_slope_material_family(
    max_depth: int,
    loading_momentum_root: int,
    returning_momentum_root: int,
) -> SquareSlopeMaterialFamily:
    """Construct L_k=b^2*k, R_k=a^2*k with exact whole-momentum closure."""
    _positive("max_depth", max_depth)
    _positive("loading_momentum_root", loading_momentum_root)
    _nonnegative("returning_momentum_root", returning_momentum_root)
    b = loading_momentum_root
    a = returning_momentum_root
    if a > b:
        raise ValueError("returning momentum root must not exceed loading root")
    loading = tuple(b * b * depth for depth in range(max_depth + 1))
    returning = tuple(a * a * depth for depth in range(max_depth + 1))
    amplitude = max(1, loading[-1], returning[-1])
    profile = explicit_material_curve_profile(loading, returning, amplitude)
    law = uniform_force_law(profile)
    common = gcd(a, b)
    return SquareSlopeMaterialFamily(
        max_depth=max_depth,
        loading_momentum_root=b,
        returning_momentum_root=a,
        law=law,
        retention_numerator=a // common,
        retention_denominator=b // common,
    )


@dataclass(frozen=True)
class SquareSlopeDepthReport:
    depth: int
    loading_work_numerator2: int
    returning_work_numerator2: int
    dissipated_work_numerator2: int
    incoming_whole_momentum: int
    outgoing_whole_momentum: int
    retention_numerator: int
    retention_denominator: int
    exact_work_energy_turn: bool
    exact_rational_momentum_closure: bool


def square_slope_depth_report(
    family: SquareSlopeMaterialFamily,
    depth: int,
) -> SquareSlopeDepthReport:
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= family.max_depth:
        raise ValueError("depth lies outside square-slope material family")
    b = family.loading_momentum_root
    a = family.returning_momentum_root
    cycle = force_cycle_work_report(family.law, depth)
    expected_load = (b * depth) ** 2
    expected_return = (a * depth) ** 2
    if cycle.loading_work_numerator2 != expected_load:
        raise AssertionError("square loading slope lost square-work identity")
    if cycle.returned_work_numerator2 != expected_return:
        raise AssertionError("square returning slope lost square-work identity")
    rebound = static_material_rebound_report(family.law, expected_load)
    closure = material_rebound_momentum_closure_report(family.law, expected_load)
    exact_turn = rebound.turning.exact_turn_depth == depth
    exact_momentum = (
        closure.exact_momentum is not None
        and closure.exact_momentum.whole_integer
        and closure.exact_momentum.coefficient_numerator == a * depth
    )
    return SquareSlopeDepthReport(
        depth=depth,
        loading_work_numerator2=cycle.loading_work_numerator2,
        returning_work_numerator2=cycle.returned_work_numerator2,
        dissipated_work_numerator2=cycle.dissipated_work_numerator2,
        incoming_whole_momentum=b * depth,
        outgoing_whole_momentum=a * depth,
        retention_numerator=family.retention_numerator,
        retention_denominator=family.retention_denominator,
        exact_work_energy_turn=exact_turn,
        exact_rational_momentum_closure=exact_momentum,
    )
