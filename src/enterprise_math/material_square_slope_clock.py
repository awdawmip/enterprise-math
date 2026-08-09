"""Compile the exact square-slope material family onto one integer time clock.

For the unit-grid square-slope material

    L_k=b^2*k,
    R_k=a^2*k,     0<=a<=b,

all represented loading/returning work prefixes are perfect momentum squares.
A full represented bounce at any depth K has branch durations

    tau_load   = 2*m/b,
    tau_return = 2*m/a     (a>0),

independent of K.  Therefore one base time quantum ``1/T`` represents every
branch duration exactly when T is divisible by the reduced denominators of those
two rationals.  The minimal clock denominator is their least common multiple.

On that clock the loading and returning durations become integer tick counts,
and momentum retention remains the curve-derived ratio ``a/b``.  This gives a
fully exact finite reference family spanning constitutive work, momentum and time
without a post-collision restitution command.

When a=0 the material has no return work; no returning clock is fabricated.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .material_edge_time_compatibility import ExactDuration
from .material_square_slope_family import (
    SquareSlopeMaterialFamily,
    square_slope_material_family,
)
from .material_turn_return_witness import (
    EXACT_TURN_RETURN,
    NO_RETURN_MOTION,
    material_turn_return_witness,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _duration(numerator: int, denominator: int) -> ExactDuration:
    common = gcd(numerator, denominator)
    return ExactDuration(numerator // common, denominator // common)


@dataclass(frozen=True)
class SquareSlopeClockCompilation:
    material: SquareSlopeMaterialFamily
    mass_count: int
    loading_duration: ExactDuration
    returning_duration: ExactDuration | None
    minimal_time_grid_denominator: int
    loading_tick_count: int
    returning_tick_count: int | None
    total_bounce_tick_count: int | None


def compile_square_slope_clock(
    max_depth: int,
    loading_momentum_root: int,
    returning_momentum_root: int,
    mass_count: int = 1,
) -> SquareSlopeClockCompilation:
    """Compile one square-slope material onto its smallest common rational clock."""
    _positive("mass_count", mass_count)
    family = square_slope_material_family(
        max_depth,
        loading_momentum_root,
        returning_momentum_root,
    )
    b = loading_momentum_root
    a = returning_momentum_root
    load = _duration(2 * mass_count, b)
    if a == 0:
        return SquareSlopeClockCompilation(
            material=family,
            mass_count=mass_count,
            loading_duration=load,
            returning_duration=None,
            minimal_time_grid_denominator=load.denominator,
            loading_tick_count=load.numerator,
            returning_tick_count=None,
            total_bounce_tick_count=None,
        )
    ret = _duration(2 * mass_count, a)
    denominator = lcm(load.denominator, ret.denominator)
    load_ticks = load.numerator * (denominator // load.denominator)
    return_ticks = ret.numerator * (denominator // ret.denominator)
    compilation = SquareSlopeClockCompilation(
        material=family,
        mass_count=mass_count,
        loading_duration=load,
        returning_duration=ret,
        minimal_time_grid_denominator=denominator,
        loading_tick_count=load_ticks,
        returning_tick_count=return_ticks,
        total_bounce_tick_count=load_ticks + return_ticks,
    )
    # Check one shallow and one deepest represented event against the generic
    # turn/return relation; depth independence is the point of this compiler.
    for depth in {1, max_depth}:
        witness = material_turn_return_witness(
            family.law,
            incoming_momentum=b * depth,
            mass_count=mass_count,
        )
        if witness.status != EXACT_TURN_RETURN:
            raise AssertionError("square-slope clock failed exact turn/return witness")
        if witness.loading_duration != load or witness.returning_duration != ret:
            raise AssertionError("square-slope branch duration changed with depth")
    return compilation
