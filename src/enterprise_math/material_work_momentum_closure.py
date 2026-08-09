"""Exact closure test from finite material work to momentum state language.

A material rebound oracle can return an exact doubled-work coordinate W2 while a
momentum value must satisfy a square-root relation.  With force/deformation count
scales ``F_s,X_s``, momentum count scale ``P_s``, and mass ``m_c/M_s``:

    p_count^2 = P_s^2 * m_c * W2 / (M_s * F_s * X_s).

The right-hand side is an exact rational number.  A rational momentum exists iff
the reduced numerator and denominator are both perfect squares.  Otherwise no
finite rational denominator can represent the exact momentum value.

The failure is still finitely describable algebraically.  Every non-negative
rational square root has a unique squarefree-radical form

    p = (a/b) * sqrt(s),

with squarefree integer ``s>=1``.  ``s=1`` is exactly the rationally closed case.
This module exposes that minimal quadratic radical as an E001 state-language
pressure test; it does not assert that quadratic algebraic momentum is the final
project ontology.

A material profile can therefore be classified by the set of radical fields
required by its exact returned-work prefixes.  A one-element set is much easier
to keep exact than a profile whose depths require many distinct squarefree
radicands.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .material_force_work import FiniteForceLaw, force_cycle_work_report
from .material_work_energy_oracle import EXACT_TURN, static_material_rebound_report

RATIONAL_MOMENTUM = "RATIONAL_MOMENTUM"
QUADRATIC_ALGEBRAIC_MOMENTUM = "QUADRATIC_ALGEBRAIC_MOMENTUM"
TURN_NOT_EXACTLY_REPRESENTED = "TURN_NOT_EXACTLY_REPRESENTED"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def square_part_and_squarefree(value: int) -> tuple[int, int]:
    """Return a,s with value=a^2*s and s squarefree, for value>=0."""
    _nonnegative("value", value)
    if value == 0:
        return 0, 1
    n = value
    square_root_part = 1
    squarefree = 1
    prime = 2
    while prime * prime <= n:
        exponent = 0
        while n % prime == 0:
            n //= prime
            exponent += 1
        if exponent:
            square_root_part *= prime ** (exponent // 2)
            if exponent % 2:
                squarefree *= prime
        prime += 1
    if n > 1:
        squarefree *= n
    if square_root_part * square_root_part * squarefree != value:
        raise AssertionError("squarefree decomposition failed")
    return square_root_part, squarefree


@dataclass(frozen=True)
class ExactMomentumSquareRatio:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        _nonnegative("numerator", self.numerator)
        _positive("denominator", self.denominator)
        if gcd(self.numerator, self.denominator) != 1:
            raise ValueError("momentum square ratio must be reduced")


@dataclass(frozen=True)
class AlgebraicMomentumMagnitude:
    coefficient_numerator: int
    coefficient_denominator: int
    squarefree_radicand: int
    rational: bool
    whole_integer: bool

    def __post_init__(self) -> None:
        _nonnegative("coefficient_numerator", self.coefficient_numerator)
        _positive("coefficient_denominator", self.coefficient_denominator)
        _positive("squarefree_radicand", self.squarefree_radicand)
        if gcd(self.coefficient_numerator, self.coefficient_denominator) != 1:
            raise ValueError("algebraic momentum coefficient must be reduced")


def momentum_square_ratio_from_returned_work(
    law: FiniteForceLaw,
    returned_work_numerator2: int,
    momentum_scale_factor: int,
    mass_scale_factor: int,
    mass_count: int,
) -> ExactMomentumSquareRatio:
    """Return reduced p_count^2 implied by one exact returned-work coordinate."""
    _nonnegative("returned_work_numerator2", returned_work_numerator2)
    _positive("momentum_scale_factor", momentum_scale_factor)
    _positive("mass_scale_factor", mass_scale_factor)
    _positive("mass_count", mass_count)
    numerator = (
        momentum_scale_factor
        * momentum_scale_factor
        * mass_count
        * returned_work_numerator2
    )
    denominator = (
        mass_scale_factor
        * law.force_scale_factor
        * law.deformation_scale_factor
    )
    common = gcd(numerator, denominator)
    return ExactMomentumSquareRatio(numerator // common, denominator // common)


def algebraic_momentum_from_square_ratio(
    ratio: ExactMomentumSquareRatio,
) -> AlgebraicMomentumMagnitude:
    """Return exact reduced (a/b)*sqrt(s) representation of sqrt(ratio)."""
    if ratio.numerator == 0:
        return AlgebraicMomentumMagnitude(0, 1, 1, True, True)
    n_root, n_sf = square_part_and_squarefree(ratio.numerator)
    d_root, d_sf = square_part_and_squarefree(ratio.denominator)
    radicand = n_sf * d_sf
    coefficient_num = n_root
    coefficient_den = d_root * d_sf
    common = gcd(coefficient_num, coefficient_den)
    coefficient_num //= common
    coefficient_den //= common
    rational = radicand == 1
    whole = rational and coefficient_den == 1
    # Verify by cross-multiplying squared representation:
    # (a^2*s)/(b^2) == numerator/denominator.
    if (
        coefficient_num * coefficient_num * radicand * ratio.denominator
        != ratio.numerator * coefficient_den * coefficient_den
    ):
        raise AssertionError("quadratic momentum representation failed exact square identity")
    return AlgebraicMomentumMagnitude(
        coefficient_numerator=coefficient_num,
        coefficient_denominator=coefficient_den,
        squarefree_radicand=radicand,
        rational=rational,
        whole_integer=whole,
    )


@dataclass(frozen=True)
class MaterialReboundMomentumClosureReport:
    incoming_work_resource_numerator2: int
    turning_status: str
    exact_turn_depth: int | None
    returned_work_numerator2: int | None
    momentum_square_ratio: ExactMomentumSquareRatio | None
    exact_momentum: AlgebraicMomentumMagnitude | None
    closure_status: str


def material_rebound_momentum_closure_report(
    law: FiniteForceLaw,
    incoming_work_resource_numerator2: int,
    momentum_scale_factor: int = 1,
    mass_scale_factor: int = 1,
    mass_count: int = 1,
) -> MaterialReboundMomentumClosureReport:
    """Classify whether curve-derived rebound closes in rational momentum values."""
    rebound = static_material_rebound_report(law, incoming_work_resource_numerator2)
    if rebound.turning.status != EXACT_TURN or rebound.outgoing_work_resource_numerator2 is None:
        return MaterialReboundMomentumClosureReport(
            incoming_work_resource_numerator2=incoming_work_resource_numerator2,
            turning_status=rebound.turning.status,
            exact_turn_depth=rebound.turning.exact_turn_depth,
            returned_work_numerator2=None,
            momentum_square_ratio=None,
            exact_momentum=None,
            closure_status=TURN_NOT_EXACTLY_REPRESENTED,
        )
    ratio = momentum_square_ratio_from_returned_work(
        law,
        rebound.outgoing_work_resource_numerator2,
        momentum_scale_factor,
        mass_scale_factor,
        mass_count,
    )
    momentum = algebraic_momentum_from_square_ratio(ratio)
    return MaterialReboundMomentumClosureReport(
        incoming_work_resource_numerator2=incoming_work_resource_numerator2,
        turning_status=rebound.turning.status,
        exact_turn_depth=rebound.turning.exact_turn_depth,
        returned_work_numerator2=rebound.outgoing_work_resource_numerator2,
        momentum_square_ratio=ratio,
        exact_momentum=momentum,
        closure_status=(
            RATIONAL_MOMENTUM if momentum.rational else QUADRATIC_ALGEBRAIC_MOMENTUM
        ),
    )


@dataclass(frozen=True)
class MaterialRadicalSpectrum:
    radicands_by_depth: tuple[int, ...]
    distinct_radicands: tuple[int, ...]
    rationally_closed_depths: tuple[int, ...]
    algebraic_depths: tuple[int, ...]


def material_return_radical_spectrum(
    law: FiniteForceLaw,
    momentum_scale_factor: int = 1,
    mass_scale_factor: int = 1,
    mass_count: int = 1,
) -> MaterialRadicalSpectrum:
    """Return squarefree momentum radicals required by every represented return prefix."""
    radicands: list[int] = []
    rational_depths: list[int] = []
    algebraic_depths: list[int] = []
    for depth in range(len(law.profile.returning)):
        returned = force_cycle_work_report(law, depth).returned_work_numerator2
        ratio = momentum_square_ratio_from_returned_work(
            law, returned, momentum_scale_factor, mass_scale_factor, mass_count
        )
        momentum = algebraic_momentum_from_square_ratio(ratio)
        radicands.append(momentum.squarefree_radicand)
        if momentum.rational:
            rational_depths.append(depth)
        else:
            algebraic_depths.append(depth)
    return MaterialRadicalSpectrum(
        radicands_by_depth=tuple(radicands),
        distinct_radicands=tuple(sorted(set(radicands))),
        rationally_closed_depths=tuple(rational_depths),
        algebraic_depths=tuple(algebraic_depths),
    )
