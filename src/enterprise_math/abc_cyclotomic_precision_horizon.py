"""Periodic versus supermodular precision regimes for odd-prime cyclotomic atoms.

For a repeated cyclotomic residual d=m(F), the full repeated modulus is exactly

    M = d * rad(d),

and the number of labelled CRT ratio classes is

    (ell-1)^omega(d).

When M<=P, a height-P observation window sees many full periods and the usual
class-density cost C/M applies.  When M>P, that periodic gain saturates: each
class contains at most one candidate p for a fixed q inside the window.  In
that supermodular regime M<=d^2 forces d>sqrt(P).

The analytic weighted tail over all d is documented in Supplement 80; this
module stores the exact finite compiler and regime split.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_odd_prime_exponent_cyclotomic import (
    OddPrimeExponentCyclotomicState,
    activation_pressure_bounds,
)
from .abc_support import radical


@dataclass(frozen=True)
class CyclotomicPrecisionHorizonState:
    height: int
    exponent: int
    mode: str
    threshold: Fraction
    cyclotomic_residual: int
    repeated_modulus: int
    root_choice_count: int
    periodic_regime: bool
    candidates_per_q_per_root: int
    signature_incidence_bound: int
    ambient_ordered_pair_count: int
    class_density: Fraction


def residual_modulus_identity(d: int) -> int:
    """Return the unique powerful repeated modulus ``M=d*rad(d)``."""
    if isinstance(d, bool) or not isinstance(d, int) or d < 1:
        raise ValueError("d must be a positive integer")
    return d * radical(d)


def cyclotomic_precision_horizon_state(
    state: OddPrimeExponentCyclotomicState,
    height: int,
    threshold: Fraction = Fraction(1, 1),
) -> CyclotomicPrecisionHorizonState:
    """Compile one activated state against a finite prime-base height window."""
    if isinstance(height, bool) or not isinstance(height, int) or height < max(state.p, state.q):
        raise ValueError("height must be an integer at least max(p,q)")
    if threshold < 1:
        raise ValueError("threshold must be at least one")
    pressure = activation_pressure_bounds(state, threshold)
    if not pressure["active"]:
        raise ValueError("state does not meet the supplied activation threshold")

    d = state.cyclotomic_residual
    M = state.repeated_modulus
    if M != residual_modulus_identity(d):
        raise AssertionError("repeated modulus must equal d*rad(d)")
    choices = state.crt_root_choice_count
    if choices != (state.exponent - 1) ** state.repeated_prime_count:
        raise AssertionError("CRT root count disagreed with repeated support")

    per = (height - 1) // M + 1
    raw = choices * height * per
    ambient = height * height
    bound = min(ambient, raw)
    periodic = M <= height

    if periodic:
        # ceil(P/M)<=2P/M when M<=P.
        if bound > 2 * choices * height * height // M + 1:
            raise AssertionError("periodic incidence escaped two-period envelope")
    else:
        # M=d*rad(d)<=d^2.  Therefore M>P implies d^2>P.
        if d * d <= height:
            raise AssertionError("supermodular regime failed sqrt-height residual floor")
        if per != 1:
            raise AssertionError("supermodular residue class should hit at most once per q")

    return CyclotomicPrecisionHorizonState(
        height=height,
        exponent=state.exponent,
        mode=state.mode,
        threshold=threshold,
        cyclotomic_residual=d,
        repeated_modulus=M,
        root_choice_count=choices,
        periodic_regime=periodic,
        candidates_per_q_per_root=per,
        signature_incidence_bound=bound,
        ambient_ordered_pair_count=ambient,
        class_density=Fraction(choices, M),
    )


def periodic_pressure_incidence_upper_bound(
    state: OddPrimeExponentCyclotomicState,
    height: int,
    threshold: Fraction = Fraction(1, 1),
) -> Fraction:
    """Return the threshold-dependent fixed-signature periodic envelope.

    If M<=P and rho>=T, Supplement 79 gives

        choices/M <= (1/(2T))*((ell-1)/(2ell+1))^k.

    The height-window incidence is at most twice P^2 times this density, hence

        P^2/T * ((ell-1)/(2ell+1))^k.
    """
    horizon = cyclotomic_precision_horizon_state(state, height, threshold)
    if not horizon.periodic_regime:
        raise ValueError("periodic pressure envelope requires repeated_modulus <= height")
    ell = state.exponent
    k = state.repeated_prime_count
    envelope = Fraction(height * height, 1) / threshold
    envelope *= Fraction((ell - 1) ** k, (2 * ell + 1) ** k)
    if horizon.signature_incidence_bound > envelope:
        # The theorem envelope is rational; the integer incidence bound may only
        # be compared directly because both count the same ordered-pair universe.
        raise AssertionError("exact periodic incidence exceeded pressure envelope")
    return envelope
