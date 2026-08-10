"""Exact finite compiler behind the P025 cube Eisenstein-tail bound.

For ell=3 the nonlinear factors

    Phi_6(p,q)=p^2-pq+q^2,
    Phi_3(p,q)=p^2+pq+q^2

are the positive-definite Eisenstein norm form x^2-xy+y^2 after the sign
change y=-q in the difference case.  Projective activation at a power threshold
P^tau forces the cyclotomic residual above that threshold times the radical of
the corresponding linear factor.  Supplement 81 combines this exact compiler
with de Bruijn's classical radical-count theorem and the Eisenstein
representation/divisor bound to obtain a global power saving.

This module stores only exact finite arithmetic and the small-/large-linear-
radical split; asymptotic estimates remain theorem prose.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_odd_prime_exponent_cyclotomic import (
    OddPrimeExponentCyclotomicState,
    odd_prime_exponent_cyclotomic_state,
)
from .abc_support import prime_factorization, radical


@dataclass(frozen=True)
class CubeEisensteinTailState:
    q: int
    p: int
    mode: str
    height: int
    threshold_numerator: int
    threshold_denominator: int
    projective_threshold_holds: bool
    linear_factor: int
    linear_radical: int
    cyclotomic_factor: int
    cyclotomic_residual: int
    eisenstein_norm_value: int
    eisenstein_divisor_representation_bound: int
    small_linear_radical_branch: bool


def divisor_count(n: int) -> int:
    """Return tau(n) exactly."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    result = 1
    for _prime, exponent in prime_factorization(n):
        result *= exponent + 1
    return result


def eisenstein_representation_upper_bound(n: int) -> int:
    """Return the classical elementary envelope ``6*tau(n)``."""
    return 6 * divisor_count(n)


def _power_threshold_holds(
    ratio: Fraction, height: int, numerator: int, denominator: int
) -> bool:
    # ratio >= height^(numerator/denominator), using exact integer powers.
    return (
        ratio.numerator**denominator
        >= ratio.denominator**denominator * height**numerator
    )


def _small_radical_branch(
    linear_radical: int, height: int, numerator: int, denominator: int
) -> bool:
    # H=P^((1-tau)/2) with tau=numerator/denominator.
    # rad(L) <= H iff rad(L)^(2*denominator) <= P^(denominator-numerator).
    return (
        linear_radical ** (2 * denominator)
        <= height ** (denominator - numerator)
    )


def cube_eisenstein_tail_state(
    q: int,
    p: int,
    height: int,
    mode: str,
    threshold_numerator: int = 0,
    threshold_denominator: int = 1,
) -> CubeEisensteinTailState:
    """Compile one cube atom for the Stage-81 balanced radical split.

    The threshold is ``P^(numerator/denominator)`` with ``0<=numerator<=denominator``.
    """
    if isinstance(height, bool) or not isinstance(height, int) or height < max(p, q):
        raise ValueError("height must be an integer at least max(p,q)")
    if (
        isinstance(threshold_numerator, bool)
        or not isinstance(threshold_numerator, int)
        or isinstance(threshold_denominator, bool)
        or not isinstance(threshold_denominator, int)
        or threshold_denominator <= 0
        or not 0 <= threshold_numerator <= threshold_denominator
    ):
        raise ValueError("require rational threshold exponent 0<=numerator<=denominator")

    state: OddPrimeExponentCyclotomicState = odd_prime_exponent_cyclotomic_state(
        q, p, 3, mode
    )
    threshold_holds = _power_threshold_holds(
        state.projective_ratio,
        height,
        threshold_numerator,
        threshold_denominator,
    )
    L = state.linear_factor
    R_L = radical(L)
    F = state.cyclotomic_factor

    if mode == "sum":
        norm = p * p - p * q + q * q
    elif mode == "difference":
        # Q(p,-q)=p^2+p q+q^2.
        norm = p * p + p * q + q * q
    else:
        raise ValueError("mode must be 'sum' or 'difference'")
    if norm != F:
        raise AssertionError("cube cyclotomic factor lost Eisenstein norm form")
    if F > 3 * height * height:
        raise AssertionError("cube Eisenstein value escaped O(P^2) height")

    if threshold_holds:
        # Stage 79 exact pressure implies m(F)>=T*rad(L) in the sum branch and
        # strictly more in the difference branch.  Check this without roots.
        exponent_power = threshold_denominator
        lhs = state.cyclotomic_residual**exponent_power
        rhs = (R_L**exponent_power) * (height**threshold_numerator)
        if mode == "sum":
            if lhs < rhs:
                raise AssertionError("cube-sum activation lost d>=T*rad(L)")
        else:
            if lhs <= rhs:
                raise AssertionError("cube-difference activation lost d>T*rad(L)")

    return CubeEisensteinTailState(
        q=q,
        p=p,
        mode=mode,
        height=height,
        threshold_numerator=threshold_numerator,
        threshold_denominator=threshold_denominator,
        projective_threshold_holds=threshold_holds,
        linear_factor=L,
        linear_radical=R_L,
        cyclotomic_factor=F,
        cyclotomic_residual=state.cyclotomic_residual,
        eisenstein_norm_value=norm,
        eisenstein_divisor_representation_bound=eisenstein_representation_upper_bound(norm),
        small_linear_radical_branch=_small_radical_branch(
            R_L,
            height,
            threshold_numerator,
            threshold_denominator,
        ),
    )
