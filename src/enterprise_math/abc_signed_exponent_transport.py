"""Signed exponent transport and exact dyadic resonance for P025 atoms.

For odd primes p>q set

    D_m = p^m-q^m,
    S_m = p^m+q^m.

The doubling factorization D_{2m}=D_m*S_m has gcd(D_m,S_m)=2.  Hence

    m(D_{2m}) = 2*m(D_m)*m(S_m),

and the equal-exponent projective pressures satisfy exactly

    rho_{2m,-} = rho_{m,-} * m(S_m)
                = rho_{m,+} * m(D_m).

Both multipliers are positive integers, so doubling never attenuates pressure.
This is the cross-sign cover connecting the sum Hasse graph to the difference
Hasse graph.  The module also records dyadic-tower monotonicity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_support import multiplicity_residual
from .legendre import is_prime


@dataclass(frozen=True)
class SignedDoublingTransportState:
    q: int
    p: int
    lower_exponent: int
    upper_exponent: int
    difference_component: int
    sum_component: int
    doubled_difference_component: int
    difference_residual: int
    sum_residual: int
    doubled_difference_residual: int
    lower_difference_ratio: Fraction
    lower_sum_ratio: Fraction
    upper_difference_ratio: Fraction
    difference_to_difference_multiplier: int
    sum_to_difference_multiplier: int
    difference_transport_class: str
    sum_transport_class: str


@dataclass(frozen=True)
class DyadicDifferencePressureTower:
    q: int
    p: int
    base_exponent: int
    steps: int
    exponents: tuple[int, ...]
    pressures: tuple[Fraction, ...]
    step_multipliers: tuple[int, ...]
    nondecreasing_verified: bool


def signed_doubling_transport_state(
    q: int, p: int, exponent: int
) -> SignedDoublingTransportState:
    """Return exact transports (m,-)->(2m,-) and (m,+)->(2m,-)."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, p, exponent)):
        raise ValueError("q, p, exponent must be integers")
    if not (3 <= q < p and is_prime(q) and is_prime(p)):
        raise ValueError("require distinct odd primes 3 <= q < p")
    if exponent < 2:
        raise ValueError("exponent must be at least two")

    m = exponent
    D = p**m - q**m
    S = p**m + q**m
    high = p ** (2 * m) - q ** (2 * m)
    if high != D * S:
        raise AssertionError("doubling difference factorization failed")
    if gcd(D, S) != 2:
        raise AssertionError("odd-prime sum/difference components must intersect at exactly two")

    mD = multiplicity_residual(D)
    mS = multiplicity_residual(S)
    mHigh = multiplicity_residual(high)
    if mHigh != 2 * mD * mS:
        raise AssertionError("dyadic residual recomposition failed")

    denominator = m * (p + q)
    rhoD = Fraction(mD, denominator)
    rhoS = Fraction(mS, denominator)
    rhoHigh = Fraction(mHigh, 2 * denominator)
    if rhoHigh != rhoD * mS:
        raise AssertionError("difference-to-doubled-difference transport failed")
    if rhoHigh != rhoS * mD:
        raise AssertionError("sum-to-doubled-difference transport failed")
    if rhoHigh < rhoD or rhoHigh < rhoS:
        raise AssertionError("doubling must not attenuate either lower pressure")

    return SignedDoublingTransportState(
        q=q,
        p=p,
        lower_exponent=m,
        upper_exponent=2 * m,
        difference_component=D,
        sum_component=S,
        doubled_difference_component=high,
        difference_residual=mD,
        sum_residual=mS,
        doubled_difference_residual=mHigh,
        lower_difference_ratio=rhoD,
        lower_sum_ratio=rhoS,
        upper_difference_ratio=rhoHigh,
        difference_to_difference_multiplier=mS,
        sum_to_difference_multiplier=mD,
        difference_transport_class="resonant" if mS == 1 else "amplified",
        sum_transport_class="resonant" if mD == 1 else "amplified",
    )


def dyadic_difference_pressure_tower(
    q: int, p: int, base_exponent: int, steps: int
) -> DyadicDifferencePressureTower:
    """Compile rho_{2^j m,-} and its integer residual multipliers."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    first = signed_doubling_transport_state(q, p, base_exponent)
    exponents = [base_exponent]
    pressures = [first.lower_difference_ratio]
    multipliers: list[int] = []
    current_exponent = base_exponent
    for _ in range(steps):
        edge = signed_doubling_transport_state(q, p, current_exponent)
        multipliers.append(edge.difference_to_difference_multiplier)
        exponents.append(edge.upper_exponent)
        pressures.append(edge.upper_difference_ratio)
        current_exponent *= 2
    if any(later < earlier for earlier, later in zip(pressures, pressures[1:])):
        raise AssertionError("dyadic difference pressure must be nondecreasing")
    return DyadicDifferencePressureTower(
        q=q,
        p=p,
        base_exponent=base_exponent,
        steps=steps,
        exponents=tuple(exponents),
        pressures=tuple(pressures),
        step_multipliers=tuple(multipliers),
        nondecreasing_verified=True,
    )
