"""Exact table-free short-step BRC tail predictor.

For an exact source state m*N = J^2 + R and a short forward step h in {1,2},
write x=h/m.  On 0<x<=1 the binomial series for sqrt(1+x)-1 is alternating
with decreasing terms.  Every even truncation is therefore a rigorous lower
bound and the next odd term bounds the truncation error.

This module uses that lower bound to predict the target root without any
precomputed sqrt((m+h)/m) table.  When the exact certificate returned by
``two_correction_certificate`` holds, at most two ordinary odd-width BRC basin
crossings recover the exact target root/remainder.

The surface is a storage/predictor-dependence research tool.  It does not claim
that high-order exact polynomial evaluation is faster than optimized isqrt.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import lcm
from typing import Protocol


class MultiplierStateLike(Protocol):
    n: int
    multiplier: int
    root: int
    remainder: int


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_even_degree(degree: int) -> None:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 2 or degree % 2:
        raise ValueError("degree must be an even integer >= 2")


@lru_cache(maxsize=None)
def binomial_half_coefficients(degree: int) -> tuple[Fraction, ...]:
    """Return binom(1/2,k), k=1..degree, exactly."""
    _require_positive("degree", degree)
    coeffs: list[Fraction] = []
    current = Fraction(1, 1)
    for k in range(1, degree + 1):
        current *= Fraction(3 - 2 * k, 2 * k)
        coeffs.append(current)
    return tuple(coeffs)


@lru_cache(maxsize=None)
def scaled_even_truncation(degree: int) -> tuple[int, tuple[int, ...], Fraction]:
    """Return common denominator, integer coefficients, and next positive term.

    For even degree K, the returned integers a_k satisfy
        sum a_k x^k / denominator = sum_{k=1}^K binom(1/2,k) x^k.
    The next coefficient binom(1/2,K+1) is positive and bounds the alternating
    remainder on 0<=x<=1.
    """
    _require_even_degree(degree)
    coeffs = binomial_half_coefficients(degree + 1)
    denominator = 1
    for coeff in coeffs[:degree]:
        denominator = lcm(denominator, coeff.denominator)
    scaled = tuple(int(coeff * denominator) for coeff in coeffs[:degree])
    next_coeff = coeffs[degree]
    if next_coeff <= 0:
        raise AssertionError("next binomial term must be positive after even truncation")
    return denominator, scaled, next_coeff


def lower_increment(root: int, multiplier: int, step: int, degree: int) -> int:
    """Return floor(J * L_K(h/m)) for the rigorous even lower truncation."""
    if isinstance(root, bool) or not isinstance(root, int) or root < 0:
        raise ValueError("root must be a non-negative integer")
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    _require_even_degree(degree)
    if step > 2:
        raise ValueError("table-free tail surface currently supports step 1 or 2")
    if multiplier < step:
        raise ValueError("alternating-tail certificate requires step/multiplier <= 1")

    denominator, scaled, _ = scaled_even_truncation(degree)

    # Homogeneous evaluation of D*m^K*L_K(h/m):
    #   sum_k a_k h^k m^(K-k).
    h_power = step
    numerator = scaled[0] * step
    for k in range(2, degree + 1):
        h_power *= step
        numerator = numerator * multiplier + scaled[k - 1] * h_power

    if numerator < 0:
        raise AssertionError("even binomial lower truncation became negative")
    exact_denominator = denominator * pow(multiplier, degree)
    return (root * numerator) // exact_denominator


def two_correction_certificate(root: int, multiplier: int, step: int, degree: int) -> bool:
    """Return whether the exact alternating-error bound certifies <=2 crossings.

    Let K be even and c=binom(1/2,K+1)>0.  A sufficient condition is

      c*J*(h/m)^(K+1) + h/(2m) <= 1.

    It is evaluated here by exact integer cross multiplication.
    """
    if isinstance(root, bool) or not isinstance(root, int) or root < 0:
        raise ValueError("root must be a non-negative integer")
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    _require_even_degree(degree)
    if step > 2:
        raise ValueError("table-free tail surface currently supports step 1 or 2")
    if multiplier < step:
        return False

    _, _, next_coeff = scaled_even_truncation(degree)
    p = next_coeff.numerator
    q = next_coeff.denominator
    left = 2 * multiplier * root * p * pow(step, degree + 1)
    right = (2 * multiplier - step) * q * pow(multiplier, degree + 1)
    return left <= right


@dataclass(frozen=True)
class TableFreeTailState:
    n: int
    multiplier: int
    root: int
    remainder: int
    source_multiplier: int
    degree: int
    correction_steps: int

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder


def transport_certified_tail(
    source: MultiplierStateLike,
    target_multiplier: int,
    *,
    degree: int = 4,
) -> TableFreeTailState:
    """Transport m->m+h, h in {1,2}, with no sqrt-ratio table.

    The call is accepted only when the exact two-correction certificate holds.
    """
    _require_positive("target_multiplier", target_multiplier)
    _require_even_degree(degree)
    n = source.n
    m = source.multiplier
    j = source.root
    r = source.remainder
    _require_positive("n", n)
    _require_positive("source multiplier", m)
    h = target_multiplier - m
    if h not in (1, 2):
        raise ValueError("certified tail transport currently supports forward steps 1 or 2")
    if j * j + r != m * n:
        raise ValueError("source state does not reconstruct m*n")
    if not 0 <= r <= 2 * j:
        raise ValueError("source remainder escaped its BRC basin")
    if not two_correction_certificate(j, m, h, degree):
        raise ValueError("declared degree does not certify the two-correction tail at this state")

    d = lower_increment(j, m, h, degree)
    candidate = j + d
    gap = r + h * n - d * (2 * j + d)
    if gap < 0:
        raise AssertionError("rigorous lower tail predictor overshot the target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 2:
            raise AssertionError("two-correction tail certificate failed")
        odd_width += 2

    state = TableFreeTailState(
        n=n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        source_multiplier=m,
        degree=degree,
        correction_steps=corrections,
    )
    if state.target_value != target_multiplier * n:
        raise AssertionError("table-free tail transport failed exact reconstruction")
    return state


__all__ = [
    "TableFreeTailState",
    "binomial_half_coefficients",
    "scaled_even_truncation",
    "lower_increment",
    "two_correction_certificate",
    "transport_certified_tail",
]
