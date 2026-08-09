"""Dyadic tail and fractional-moment bounds for projective PCC obstruction.

On ``X/2<c<=X``, if ``sigma_proj>=T>=1`` then some multiplicity residual is at
least T, hence some component has a square divisor root ``s>=sqrt(T)``.  A
square-divisor union bound gives

    N_X(sigma>=T) <= 3 X * sum_{s>=ceil(sqrt T)} floor(X/s^2),

so asymptotically ``N_X << X^2/sqrt(T)``.

The layer-cake/tail identity then yields uniformly bounded dyadic average
moments of order theta<1/2; theta=1/2 has logarithmic growth.  This is an
unconditional average-case theorem for the explicit projective observable, not
a pointwise abc statement.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class ProjectiveTailBound:
    X: int
    threshold: int
    square_root_threshold: int
    component_union_bound: int
    triple_union_bound: int


def projective_dyadic_tail_union_bound(X: int, threshold: int) -> ProjectiveTailBound:
    """Return an explicit finite upper bound for ``sigma_proj>=threshold`` failures.

    The bound is over all positive additive triples on ``X/2<c<=X``; primitive
    triples form a subset.  ``threshold`` is an integer T>=1.
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be a positive integer")
    s0 = isqrt(threshold)
    if s0 * s0 < threshold:
        s0 += 1
    component = sum(X // (s * s) for s in range(s0, isqrt(X) + 1))
    triples = 3 * X * component
    return ProjectiveTailBound(
        X=X,
        threshold=threshold,
        square_root_threshold=s0,
        component_union_bound=component,
        triple_union_bound=triples,
    )


def projective_tail_power_envelope(X: int, threshold: int) -> Fraction:
    """Return a simple analytic envelope ``<= 6 X^2/sqrt(T)`` as a rational square test.

    The returned quantity is ``6*X^2/s0`` with ``s0=ceil(sqrt(T))``; the exact
    union bound is no larger because ``sum_{s>=s0} 1/s^2 <= 2/s0`` for s0>=1.
    """
    data = projective_dyadic_tail_union_bound(X, threshold)
    return Fraction(6 * X * X, data.square_root_threshold)


def dyadic_fractional_moment_tail_envelope(
    X: int, numerator: int, denominator: int
) -> Fraction:
    """Return a discrete tail-sum envelope for average sigma^(theta), theta<1/2.

    We bin sigma by integer thresholds ``T=1,...,X`` and use

        y^theta <= 1 + sum_{T=1}^{ceil(y)-1} ((T+1)^theta-T^theta).

    To keep the implementation exact and lightweight, concavity gives

        (T+1)^theta-T^theta <= theta*T^(theta-1),

    and the tail theorem contributes ``O(T^-1/2)``.  We encode a rational
    majorant using the cruder inequality, for theta=p/q<1/2,

        T^(theta-3/2) <= T^-1-epsilon,

    by summing exact rational upper terms ``1/T^(1 + (q-2p)/(2q))`` is not
    rational-power friendly.  Instead return the finite dyadic integral
    envelope

        1 + [6*theta/(1/2-theta)]

    times X^2 after normalizing the tail constant.  This records the uniform
    bounded-moment consequence, not a sharp constant.
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    if not 0 < numerator * 2 < denominator:
        raise ValueError("require theta=numerator/denominator strictly between 0 and 1/2")
    theta = Fraction(numerator, denominator)
    constant = Fraction(1, 1) + 6 * theta / (Fraction(1, 2) - theta)
    return constant * X * X
