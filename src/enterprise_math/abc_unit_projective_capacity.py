"""Exact projective-capacity structure of unit abc relations ``1+b=c``.

For a unit relation, Supplement 47 simplifies further:

    sigma_proj = max(m(c)/C(b), m(b)/C(c)),

where

    C(n)=sum_{p|n} v_p(n) rad(n)/p

is the normalized block derivative capacity.

Small capacity forces low prime support.  If ``omega(n)=k``, then

    C(n) >= min over k distinct primes of sum R/p,

and the minimum is attained by the first k primes with exponent one.  Thus the
capacity shells grow rapidly (1 for one prime with exponent 1, at least 5 for
two distinct primes, at least 31 for three distinct primes, ...).

This module makes the unit PCC hard region an explicit cross condition between
large multiplicity residual on one consecutive integer and low derivative
capacity on the other.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import multiplicity_residual, prime_factorization, radical


@dataclass(frozen=True)
class UnitProjectiveCapacityState:
    b: int
    c: int
    capacities: tuple[int, int]
    residuals: tuple[int, int]
    cross_ratios: tuple[Fraction, Fraction]
    sigma_projective: Fraction
    dominant_side: str


def _first_primes(count: int) -> tuple[int, ...]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a non-negative integer")
    result: list[int] = []
    candidate = 2
    while len(result) < count:
        prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            result.append(candidate)
        candidate += 1
    return tuple(result)


def minimum_capacity_for_support_count(count: int) -> int:
    """Return the exact minimum ``C(n)`` among integers with omega(n)=count."""
    if count == 0:
        return 0
    primes = _first_primes(count)
    R = 1
    for prime in primes:
        R *= prime
    return sum(R // prime for prime in primes)


def capacity_support_lower_bound_holds(n: int) -> bool:
    """Verify ``C(n)>=C_min(omega(n))`` for one positive integer."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    omega = len(prime_factorization(n))
    capacity = normalized_block_capacity(n)
    lower = minimum_capacity_for_support_count(omega)
    if capacity < lower:
        raise AssertionError("normalized derivative capacity fell below support minimum")
    return True


def unit_projective_capacity_state(b: int, c: int) -> UnitProjectiveCapacityState:
    """Return exact unit relation cross-capacity state for ``1+b=c``."""
    if isinstance(b, bool) or not isinstance(b, int) or b <= 1:
        raise ValueError("b must be an integer > 1")
    if isinstance(c, bool) or not isinstance(c, int) or c != b + 1:
        raise ValueError("require c=b+1")
    C_b = normalized_block_capacity(b)
    C_c = normalized_block_capacity(c)
    m_b = multiplicity_residual(b)
    m_c = multiplicity_residual(c)
    ratios = (Fraction(m_c, C_b), Fraction(m_b, C_c))
    sigma = max(ratios)
    independent = projective_capacity_condition_state(1, b, c).sigma_projective
    if sigma != independent:
        raise AssertionError("unit cross-capacity formula disagrees with projective state")
    if ratios[0] > ratios[1]:
        side = "c_residual_over_b_capacity"
    elif ratios[1] > ratios[0]:
        side = "b_residual_over_c_capacity"
    else:
        side = "tie"
    return UnitProjectiveCapacityState(
        b=b,
        c=c,
        capacities=(C_b, C_c),
        residuals=(m_b, m_c),
        cross_ratios=ratios,
        sigma_projective=sigma,
        dominant_side=side,
    )


def unit_sqrt_bound_counterexamples() -> tuple[UnitProjectiveCapacityState, ...]:
    """Return exact counterexamples to the naive nonexceptional ``sigma<=sqrt(c)`` guess."""
    examples = (
        unit_projective_capacity_state(288, 289),
        unit_projective_capacity_state(239**2, 2 * 13**4),
    )
    for data in examples:
        if data.sigma_projective * data.sigma_projective <= data.c:
            raise AssertionError("stored unit sqrt-bound counterexample ceased to violate")
    return examples
