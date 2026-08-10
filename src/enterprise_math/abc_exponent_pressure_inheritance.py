"""Exact pressure inheritance along exponent divisibility for P025 atoms.

If m|n and the same-sign low component divides the high component, write

    A_n = A_m * Q.

For differences this always holds.  For sums it holds when n/m is odd.  Let

    Gamma = rad(A_m) rad(Q) / rad(A_n),

which measures support reused between the inherited component and the new
quotient.  Then the equal-exponent projective ratios satisfy exactly

    rho_n = rho_m * Gamma*m(Q)/(n/m).

The factor Lambda=Gamma*m(Q)/(n/m) is the pressure inheritance multiplier.
It can attenuate, preserve, or amplify lower-exponent pressure.  Composite
hard states from Stages 82-83 are resonant lifts with Lambda=1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_cyclotomic_divisor_carrier import cyclotomic_index_set
from .abc_support import multiplicity_residual, radical
from .legendre import is_prime


@dataclass(frozen=True)
class ExponentPressureInheritanceState:
    q: int
    p: int
    lower_exponent: int
    upper_exponent: int
    exponent_ratio: int
    mode: str
    lower_component: int
    upper_component: int
    quotient_component: int
    quotient_residual: int
    overlap_factor: int
    lower_ratio: Fraction
    upper_ratio: Fraction
    inheritance_multiplier: Fraction
    lower_indices: tuple[int, ...]
    upper_indices: tuple[int, ...]
    new_indices: tuple[int, ...]
    transport_class: str


def _component(p: int, q: int, exponent: int, mode: str) -> int:
    if mode == "difference":
        return p**exponent - q**exponent
    if mode == "sum":
        return p**exponent + q**exponent
    raise ValueError("mode must be 'sum' or 'difference'")


def exponent_pressure_inheritance_state(
    q: int,
    p: int,
    lower_exponent: int,
    upper_exponent: int,
    mode: str,
) -> ExponentPressureInheritanceState:
    """Return exact same-sign pressure transport from m to n."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, p)):
        raise ValueError("q and p must be integers")
    if not (3 <= q < p and is_prime(q) and is_prime(p)):
        raise ValueError("require distinct odd primes 3 <= q < p")
    if (
        isinstance(lower_exponent, bool)
        or not isinstance(lower_exponent, int)
        or isinstance(upper_exponent, bool)
        or not isinstance(upper_exponent, int)
        or lower_exponent < 2
        or upper_exponent <= lower_exponent
        or upper_exponent % lower_exponent
    ):
        raise ValueError("require integers 2<=lower<upper with lower|upper")
    k = upper_exponent // lower_exponent
    if mode == "sum" and k % 2 == 0:
        raise ValueError("same-sign sum inheritance requires upper/lower odd")
    if mode not in {"sum", "difference"}:
        raise ValueError("mode must be 'sum' or 'difference'")

    low = _component(p, q, lower_exponent, mode)
    high = _component(p, q, upper_exponent, mode)
    if high % low:
        raise AssertionError("declared same-sign inheritance lost divisibility")
    quotient = high // low

    gamma_numerator = radical(low) * radical(quotient)
    rad_high = radical(high)
    if gamma_numerator % rad_high:
        raise AssertionError("inheritance overlap factor lost integrality")
    gamma = gamma_numerator // rad_high
    qres = multiplicity_residual(quotient)

    low_ratio = Fraction(
        multiplicity_residual(low),
        lower_exponent * (p + q),
    )
    high_ratio = Fraction(
        multiplicity_residual(high),
        upper_exponent * (p + q),
    )
    multiplier = Fraction(gamma * qres, k)
    if high_ratio != low_ratio * multiplier:
        raise AssertionError("exact exponent-pressure inheritance law failed")

    lower_indices = cyclotomic_index_set(lower_exponent, mode)
    upper_indices = cyclotomic_index_set(upper_exponent, mode)
    if not set(lower_indices).issubset(upper_indices):
        raise AssertionError("same-sign inheritance lost cyclotomic index inclusion")
    new_indices = tuple(index for index in upper_indices if index not in lower_indices)

    if multiplier < 1:
        transport = "attenuated"
    elif multiplier > 1:
        transport = "amplified"
    else:
        transport = "resonant"

    return ExponentPressureInheritanceState(
        q=q,
        p=p,
        lower_exponent=lower_exponent,
        upper_exponent=upper_exponent,
        exponent_ratio=k,
        mode=mode,
        lower_component=low,
        upper_component=high,
        quotient_component=quotient,
        quotient_residual=qres,
        overlap_factor=gamma,
        lower_ratio=low_ratio,
        upper_ratio=high_ratio,
        inheritance_multiplier=multiplier,
        lower_indices=lower_indices,
        upper_indices=upper_indices,
        new_indices=new_indices,
        transport_class=transport,
    )


def inheritance_cocycle_holds(
    q: int,
    p: int,
    first_exponent: int,
    middle_exponent: int,
    final_exponent: int,
    mode: str,
) -> bool:
    """Verify Lambda(m->r)=Lambda(m->n)*Lambda(n->r) on an admissible chain."""
    first = exponent_pressure_inheritance_state(
        q, p, first_exponent, middle_exponent, mode
    )
    second = exponent_pressure_inheritance_state(
        q, p, middle_exponent, final_exponent, mode
    )
    direct = exponent_pressure_inheritance_state(
        q, p, first_exponent, final_exponent, mode
    )
    if direct.inheritance_multiplier != (
        first.inheritance_multiplier * second.inheritance_multiplier
    ):
        raise AssertionError("pressure inheritance multiplier lost cocycle law")
    return True
