"""Odd-prime equal-exponent cyclotomic pressure and congruence compression.

For an odd prime exponent ell and distinct odd primes p>q, the equal-exponent
P025 projective atoms are

    rho_{ell,+} = m(p^ell+q^ell) / (ell*(p+q)),
    rho_{ell,-} = m(p^ell-q^ell) / (ell*(p+q)).

Writing the active component as a linear factor times Phi_{2ell} or Phi_ell,
respectively, gives the exact residual recomposition

    m(active) = gcd(linear, ell) * m(linear) * m(cyclotomic).

Hence threshold-one activation forces the non-linear cyclotomic factor to be
nonsquarefree. Every repeated prime r has r == 1 (mod 2*ell), and modulo each
full repeated prime power the labelled ratio p/q lies in one of ell-1 exact
root-of-unity classes. This module records those exact project-specific
compilers; the cyclotomic/order/Hensel ingredients are classical mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, prod

from .abc_support import multiplicity_residual, prime_factorization, radical
from .legendre import is_prime


@dataclass(frozen=True)
class OddPrimeCyclotomicConstraint:
    prime: int
    exponent: int
    modulus: int
    root_order: int
    observed_ratio: int
    local_root_count: int


@dataclass(frozen=True)
class OddPrimeExponentCyclotomicState:
    q: int
    p: int
    exponent: int
    mode: str
    active_component: int
    linear_factor: int
    cyclotomic_factor: int
    linear_cyclotomic_gcd: int
    active_residual: int
    linear_residual: int
    cyclotomic_residual: int
    projective_ratio: Fraction
    constraints: tuple[OddPrimeCyclotomicConstraint, ...]
    repeated_modulus: int
    repeated_prime_count: int
    crt_root_choice_count: int


def _require_inputs(q: int, p: int, ell: int, mode: str) -> None:
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, p, ell)):
        raise ValueError("q, p, ell must be integers")
    if not (3 <= q < p and is_prime(q) and is_prime(p)):
        raise ValueError("require distinct odd primes 3 <= q < p")
    if ell < 3 or ell % 2 == 0 or not is_prime(ell):
        raise ValueError("ell must be an odd prime")
    if mode not in {"sum", "difference"}:
        raise ValueError("mode must be 'sum' or 'difference'")


def _proper_order_checks(order: int, ell: int) -> tuple[int, ...]:
    if order == ell:
        return (1,)
    if order == 2 * ell:
        return (1, 2, ell)
    raise AssertionError("unexpected odd-prime cyclotomic root order")


def odd_prime_exponent_cyclotomic_state(
    q: int, p: int, ell: int, mode: str
) -> OddPrimeExponentCyclotomicState:
    """Return the exact equal-exponent cyclotomic pressure/congruence state."""
    _require_inputs(q, p, ell, mode)

    if mode == "sum":
        active = p**ell + q**ell
        linear = p + q
        factor = active // linear
        order = 2 * ell
    else:
        active = p**ell - q**ell
        linear = p - q
        factor = active // linear
        order = ell

    if linear * factor != active:
        raise AssertionError("cyclotomic factorization failed")
    if factor % 2 == 0:
        raise AssertionError("odd-prime cyclotomic factor should be odd")

    g = gcd(linear, ell)
    if g not in (1, ell):
        raise AssertionError("linear/cyclotomic overlap escaped the prime exponent")

    active_residual = multiplicity_residual(active)
    linear_residual = multiplicity_residual(linear)
    cyclotomic_residual = multiplicity_residual(factor)
    if active_residual != g * linear_residual * cyclotomic_residual:
        raise AssertionError("exact residual recomposition failed")

    factorization = prime_factorization(factor)
    ell_valuation = next((e for r, e in factorization if r == ell), 0)
    if ell_valuation > 1:
        raise AssertionError("exceptional cyclotomic prime ell must not repeat")

    repeated = tuple((r, e) for r, e in factorization if e >= 2)
    constraints: list[OddPrimeCyclotomicConstraint] = []
    for r, e in repeated:
        if r == ell or r % (2 * ell) != 1:
            raise AssertionError("repeated cyclotomic prime escaped 1 mod 2ell")
        modulus = r**e
        x = (p * pow(q, -1, modulus)) % modulus
        if pow(x, order, modulus) != 1:
            raise AssertionError("observed prime ratio lost cyclotomic order")
        if any(pow(x, d, modulus) == 1 for d in _proper_order_checks(order, ell)):
            raise AssertionError("observed prime ratio order collapsed")
        constraints.append(
            OddPrimeCyclotomicConstraint(
                prime=r,
                exponent=e,
                modulus=modulus,
                root_order=order,
                observed_ratio=x,
                local_root_count=ell - 1,
            )
        )

    repeated_modulus = prod((item.modulus for item in constraints), start=1)
    k = len(constraints)
    choices = (ell - 1) ** k

    repeated_radical = prod((item.prime for item in constraints), start=1)
    if cyclotomic_residual != repeated_modulus // repeated_radical:
        raise AssertionError("repeated modulus lost cyclotomic residual")

    ratio = Fraction(active_residual, ell * (p + q))
    return OddPrimeExponentCyclotomicState(
        q=q,
        p=p,
        exponent=ell,
        mode=mode,
        active_component=active,
        linear_factor=linear,
        cyclotomic_factor=factor,
        linear_cyclotomic_gcd=g,
        active_residual=active_residual,
        linear_residual=linear_residual,
        cyclotomic_residual=cyclotomic_residual,
        projective_ratio=ratio,
        constraints=tuple(constraints),
        repeated_modulus=repeated_modulus,
        repeated_prime_count=k,
        crt_root_choice_count=choices,
    )


def activation_pressure_bounds(
    state: OddPrimeExponentCyclotomicState,
    threshold: Fraction = Fraction(1, 1),
) -> dict[str, Fraction | int | bool]:
    """Return exact consequences when ``rho >= threshold >= 1``.

    The returned inequalities use only integer/rational arithmetic.  In
    particular activation forces a nontrivial repeated cyclotomic signature and
    bounds its modulus/class density from the projective pressure.
    """
    if threshold < 1:
        raise ValueError("threshold must be at least one")
    active = state.projective_ratio >= threshold
    if not active:
        return {
            "active": False,
            "cyclotomic_repetition_forced": False,
        }

    ell = state.exponent
    L = state.linear_factor
    g = state.linear_cyclotomic_gcd
    # rho = g*m(L)*m(F)/(ell*(p+q)).
    exact_lower = threshold * ell * (state.p + state.q) / (g * state.linear_residual)
    if state.cyclotomic_residual < exact_lower:
        raise AssertionError("activation failed exact cyclotomic residual lower bound")

    # L is even, so rad(L)>=2.  For the difference mode L<p+q; in either mode
    # the exact lower bound is at least 2*threshold (strict in difference mode).
    universal_lower = 2 * threshold
    if state.mode == "sum":
        if state.cyclotomic_residual < universal_lower:
            raise AssertionError("sum activation lost universal 2T residual bound")
    else:
        if not state.cyclotomic_residual > universal_lower:
            raise AssertionError("difference activation lost strict 2T residual bound")

    k = state.repeated_prime_count
    if k < 1:
        raise AssertionError("threshold-one activation must force cyclotomic repetition")
    repeated_radical_min = (2 * ell + 1) ** k
    modulus_lower = state.cyclotomic_residual * repeated_radical_min
    if state.repeated_modulus < modulus_lower:
        raise AssertionError("repeated modulus lost 1 mod 2ell support lower bound")

    # choice_density = choices / M <= ((ell-1)/(2ell+1))^k / m(F)
    lhs = Fraction(state.crt_root_choice_count, state.repeated_modulus)
    rhs = Fraction((ell - 1) ** k, (2 * ell + 1) ** k * state.cyclotomic_residual)
    if lhs > rhs:
        raise AssertionError("CRT ratio density exceeded support/residual envelope")
    pressure_rhs = Fraction((ell - 1) ** k, (2 * ell + 1) ** k) / universal_lower
    if lhs > pressure_rhs:
        raise AssertionError("activation pressure failed congruence-density bound")

    return {
        "active": True,
        "cyclotomic_repetition_forced": True,
        "exact_cyclotomic_residual_lower_bound": exact_lower,
        "universal_cyclotomic_residual_lower_bound": universal_lower,
        "repeated_modulus_lower_bound": modulus_lower,
        "actual_class_density": lhs,
        "pressure_class_density_upper_bound": pressure_rhs,
    }
