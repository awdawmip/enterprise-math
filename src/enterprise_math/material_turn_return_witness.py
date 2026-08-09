"""Explicit represented-turn witness for one complete finite material rebound event.

A branch-aware hysteretic material cannot safely treat a loading endpoint whose
momentum has already reversed as one pure loading step.  The minimal finite repair
is to retain one represented turning witness:

    (depth 0, p_in)
      --LOADING--> (depth K, 0)
      --RETURNING--> (depth 0, p_out).

No primitive intermediate trajectory is reconstructed.  K is a declared material
state and must be exactly represented by the loading work table:

    p_in^2 = W2_L(K).

If the input work lies between represented loading-work levels, the turn is
``TURN_UNDERRESOLVED``.  If it exceeds the finite material domain, the result is
``MATERIAL_UNDERRESOLVED``.

At an exact turn the returning branch determines the exact released work.  A
whole-integer outgoing momentum exists only when

    p_out^2 = W2_R(K)

is a perfect square in the current value language.  Otherwise the branch event is
``RETURN_MOMENTUM_UNDERRESOLVED`` (the separate algebraic-closure layer can retain
a radical instead of projecting it).

For unit work/momentum scales and integer mass m, midpoint timing is exact:

    tau_load   = 2*m*x_K / p_in,
    tau_return = 2*m*x_K / p_out.

A zero return-work branch has no finite return-to-zero-deformation duration from
rest and is reported as ``NO_RETURN_MOTION`` rather than fabricating a bounce.

This relation is an optional explicit turning-event policy.  It preserves branch
history without introducing hidden trajectory subdivision.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .material_edge_time_compatibility import ExactDuration
from .material_force_work import FiniteForceLaw, force_cycle_work_report
from .material_work_energy_oracle import (
    EXACT_TURN,
    material_turning_report,
)

EXACT_TURN_RETURN = "EXACT_TURN_RETURN"
RETURN_MOMENTUM_UNDERRESOLVED = "RETURN_MOMENTUM_UNDERRESOLVED"
NO_RETURN_MOTION = "NO_RETURN_MOTION"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _duration(numerator: int, denominator: int) -> ExactDuration:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("duration numerator/denominator must be positive")
    common = gcd(numerator, denominator)
    return ExactDuration(numerator // common, denominator // common)


def _add_duration(left: ExactDuration, right: ExactDuration) -> ExactDuration:
    return _duration(
        left.numerator * right.denominator + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


@dataclass(frozen=True)
class MaterialTurnReturnWitness:
    incoming_momentum: int
    mass_count: int
    status: str
    turn_depth: int | None
    turn_deformation_span: int | None
    loading_work_numerator2: int | None
    returning_work_numerator2: int | None
    dissipated_work_numerator2: int | None
    outgoing_momentum: int | None
    momentum_retention_numerator: int | None
    momentum_retention_denominator: int | None
    loading_duration: ExactDuration | None
    returning_duration: ExactDuration | None
    total_duration: ExactDuration | None
    turning_status: str


def material_turn_return_witness(
    law: FiniteForceLaw,
    incoming_momentum: int,
    mass_count: int = 1,
) -> MaterialTurnReturnWitness:
    """Return one exact represented branch-aware full rebound witness when available."""
    _positive("incoming_momentum", incoming_momentum)
    _positive("mass_count", mass_count)
    incoming_work2 = incoming_momentum * incoming_momentum
    turning = material_turning_report(law, incoming_work2)
    if turning.status != EXACT_TURN:
        return MaterialTurnReturnWitness(
            incoming_momentum=incoming_momentum,
            mass_count=mass_count,
            status=turning.status,
            turn_depth=turning.exact_turn_depth,
            turn_deformation_span=None,
            loading_work_numerator2=None,
            returning_work_numerator2=None,
            dissipated_work_numerator2=None,
            outgoing_momentum=None,
            momentum_retention_numerator=None,
            momentum_retention_denominator=None,
            loading_duration=None,
            returning_duration=None,
            total_duration=None,
            turning_status=turning.status,
        )
    depth = turning.exact_turn_depth
    if depth is None:
        raise AssertionError("exact turn lost represented depth")
    if depth == 0:
        raise AssertionError("positive incoming momentum cannot turn at zero work/deformation")
    span = law.deformation_counts[depth] - law.deformation_counts[0]
    cycle = force_cycle_work_report(law, depth)
    returned = cycle.returned_work_numerator2
    root = isqrt(returned)
    if root * root != returned:
        return MaterialTurnReturnWitness(
            incoming_momentum=incoming_momentum,
            mass_count=mass_count,
            status=RETURN_MOMENTUM_UNDERRESOLVED,
            turn_depth=depth,
            turn_deformation_span=span,
            loading_work_numerator2=cycle.loading_work_numerator2,
            returning_work_numerator2=returned,
            dissipated_work_numerator2=cycle.dissipated_work_numerator2,
            outgoing_momentum=None,
            momentum_retention_numerator=None,
            momentum_retention_denominator=None,
            loading_duration=_duration(2 * mass_count * span, incoming_momentum),
            returning_duration=None,
            total_duration=None,
            turning_status=turning.status,
        )
    if root == 0:
        return MaterialTurnReturnWitness(
            incoming_momentum=incoming_momentum,
            mass_count=mass_count,
            status=NO_RETURN_MOTION,
            turn_depth=depth,
            turn_deformation_span=span,
            loading_work_numerator2=cycle.loading_work_numerator2,
            returning_work_numerator2=returned,
            dissipated_work_numerator2=cycle.dissipated_work_numerator2,
            outgoing_momentum=0,
            momentum_retention_numerator=0,
            momentum_retention_denominator=1,
            loading_duration=_duration(2 * mass_count * span, incoming_momentum),
            returning_duration=None,
            total_duration=None,
            turning_status=turning.status,
        )
    load_duration = _duration(2 * mass_count * span, incoming_momentum)
    return_duration = _duration(2 * mass_count * span, root)
    common = gcd(root, incoming_momentum)
    retention_num = root // common
    retention_den = incoming_momentum // common
    return MaterialTurnReturnWitness(
        incoming_momentum=incoming_momentum,
        mass_count=mass_count,
        status=EXACT_TURN_RETURN,
        turn_depth=depth,
        turn_deformation_span=span,
        loading_work_numerator2=cycle.loading_work_numerator2,
        returning_work_numerator2=returned,
        dissipated_work_numerator2=cycle.dissipated_work_numerator2,
        outgoing_momentum=root,
        momentum_retention_numerator=retention_num,
        momentum_retention_denominator=retention_den,
        loading_duration=load_duration,
        returning_duration=return_duration,
        total_duration=_add_duration(load_duration, return_duration),
        turning_status=turning.status,
    )
