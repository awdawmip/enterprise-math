"""Exact bridge between finite impulse denominators and lifted momentum state.

Several E001 material/contact owners use different but compatible precision
coordinates:

* the causal material world stores lifted momentum on a declared denominator;
* branching-contact response research may return an impulse numerator ``a`` on a
  separately declared denominator ``s``.

A refined contact impulse is only a representation-layer object until the body
momentum state can represent it.  This module supplies that missing thin bridge
without duplicating any contact-response solver.

For lifted momentum numerator ``P`` on denominator ``m`` and one signed impulse
``a/s`` in the same base momentum-count unit:

* if ``s | m``, the impulse is already exactly representable on the current
  momentum lattice;
* otherwise the least common exact refinement is

      L = lcm(m, s).

The old momentum embeds as ``P*(L/m)`` and the impulse as ``a*(L/s)``.  No
rounding is needed.  For several impulses the unique least common denominator is
``lcm(m, s_1, ..., s_n)`` and addition is order-independent on that common lift.

This is ordinary rational/common-denominator arithmetic specialized as an E001
state interface.  It is not a novelty claim.  The important world-engine
boundary is explicit: denominator refinement is physical-state refinement only
when the momentum state is actually lifted; a finer impulse numerator by itself
does not silently change body momentum.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .material_impulse_coupling import signed_toward_zero_divmod


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


@dataclass(frozen=True)
class LiftedMomentumCoordinate:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        _integer("numerator", self.numerator)
        _positive("denominator", self.denominator)

    @property
    def whole_and_detail(self) -> tuple[int, int]:
        return signed_toward_zero_divmod(self.numerator, self.denominator)


@dataclass(frozen=True)
class DeclaredImpulseFraction:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        _integer("numerator", self.numerator)
        _positive("denominator", self.denominator)

    @property
    def reduced(self) -> "DeclaredImpulseFraction":
        common = gcd(abs(self.numerator), self.denominator)
        return DeclaredImpulseFraction(
            self.numerator // common,
            self.denominator // common,
        )


@dataclass(frozen=True)
class ExactImpulseLiftReport:
    before: LiftedMomentumCoordinate
    impulse: DeclaredImpulseFraction
    common_denominator: int
    refined_momentum_numerator: int
    refined_impulse_numerator: int
    after: LiftedMomentumCoordinate
    denominator_refined: bool


def minimum_common_momentum_denominator(
    momentum_denominator: int,
    impulse_denominators: tuple[int, ...] | list[int],
) -> int:
    """Least denominator exactly carrying the old momentum and all impulses."""
    _positive("momentum_denominator", momentum_denominator)
    result = momentum_denominator
    for denominator in impulse_denominators:
        _positive("impulse_denominator", denominator)
        result = lcm(result, denominator)
    return result


def refine_lifted_momentum(
    momentum: LiftedMomentumCoordinate,
    target_denominator: int,
) -> LiftedMomentumCoordinate:
    """Embed one lifted momentum into a true divisibility refinement."""
    _positive("target_denominator", target_denominator)
    if target_denominator % momentum.denominator != 0:
        raise ValueError("target denominator must be a multiple of the source denominator")
    factor = target_denominator // momentum.denominator
    return LiftedMomentumCoordinate(momentum.numerator * factor, target_denominator)


def apply_fractional_impulse_exact(
    momentum: LiftedMomentumCoordinate,
    impulse: DeclaredImpulseFraction,
) -> ExactImpulseLiftReport:
    """Apply one impulse exactly on the least common lifted momentum lattice."""
    common = lcm(momentum.denominator, impulse.denominator)
    refined_momentum = momentum.numerator * (common // momentum.denominator)
    refined_impulse = impulse.numerator * (common // impulse.denominator)
    after_num = refined_momentum + refined_impulse
    report = ExactImpulseLiftReport(
        before=momentum,
        impulse=impulse,
        common_denominator=common,
        refined_momentum_numerator=refined_momentum,
        refined_impulse_numerator=refined_impulse,
        after=LiftedMomentumCoordinate(after_num, common),
        denominator_refined=common != momentum.denominator,
    )
    # Exact rational identity by cross multiplication.
    if (
        report.after.numerator * momentum.denominator * impulse.denominator
        != momentum.numerator * common * impulse.denominator
        + impulse.numerator * common * momentum.denominator
    ):
        raise AssertionError("common-denominator impulse lift lost exact momentum identity")
    return report


def apply_fractional_impulses_exact(
    momentum: LiftedMomentumCoordinate,
    impulses: tuple[DeclaredImpulseFraction, ...] | list[DeclaredImpulseFraction],
) -> LiftedMomentumCoordinate:
    """Apply many declared impulses on their one least common denominator."""
    items = tuple(impulses)
    common = minimum_common_momentum_denominator(
        momentum.denominator,
        [item.denominator for item in items],
    )
    total = momentum.numerator * (common // momentum.denominator)
    for item in items:
        total += item.numerator * (common // item.denominator)
    return LiftedMomentumCoordinate(total, common)


def material_response_impulse_fraction(
    response_sample: int,
    response_amplitude: int,
    full_scale_impulse_quanta: int,
    direction_sign: int = 1,
) -> DeclaredImpulseFraction:
    """Reduced impulse fraction J*r/A used by the normalized material coupling."""
    if isinstance(response_sample, bool) or not isinstance(response_sample, int) or response_sample < 0:
        raise ValueError("response_sample must be a non-negative integer")
    _positive("response_amplitude", response_amplitude)
    if response_sample > response_amplitude:
        raise ValueError("response_sample must not exceed response_amplitude")
    if isinstance(full_scale_impulse_quanta, bool) or not isinstance(full_scale_impulse_quanta, int) or full_scale_impulse_quanta < 0:
        raise ValueError("full_scale_impulse_quanta must be a non-negative integer")
    if direction_sign not in (-1, 1):
        raise ValueError("direction_sign must be -1 or +1")
    raw = direction_sign * full_scale_impulse_quanta * response_sample
    return DeclaredImpulseFraction(raw, response_amplitude).reduced


def material_amplitude_lattice_is_sufficient(
    response_sample: int,
    response_amplitude: int,
    full_scale_impulse_quanta: int,
) -> bool:
    """The J*r/A material impulse always closes on denominator A lifted momentum."""
    impulse = material_response_impulse_fraction(
        response_sample,
        response_amplitude,
        full_scale_impulse_quanta,
    )
    return response_amplitude % impulse.denominator == 0
