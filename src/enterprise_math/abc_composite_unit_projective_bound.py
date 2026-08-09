"""Elementary projective bound on Pasten-nonexceptional unit triples.

For every composite integer n>1,

    S(n)=sum v_p(n)/p >= 2/sqrt(n).

Proof: if n=p^e with e>=2 then e/p>=2/sqrt(n); otherwise choose two
distinct support primes p,q and use

    1/p+1/q >= 2/sqrt(pq) >= 2/sqrt(n).

Thus for a unit relation ``1+b=c`` with both b,c composite,

    sigma_proj = max(m(c)/C(b), m(b)/C(c))
               <= c^(3/2)/(2*rad(abc)).

The implementation checks the equivalent exact squared inequality

    (2*R*sigma_proj)^2 <= c^3.

Consequently an Oesterle bound ``c<R^M`` directly implies PCC at every
exponent eta>3/2-1/M on this slice.  No geometry-of-numbers reverse theorem is
needed for this projective implication.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import (
    projective_capacity_condition_state,
    support_log_derivative_load,
)
from .abc_support import prime_factorization


@dataclass(frozen=True)
class CompositeUnitProjectiveBound:
    b: int
    c: int
    radical_product: int
    loads: tuple[Fraction, Fraction]
    sigma_projective: Fraction
    squared_bound_left: Fraction
    squared_bound_right: int


def _is_composite(n: int) -> bool:
    factors = prime_factorization(n)
    return n > 1 and not (len(factors) == 1 and factors[0] == (n, 1))


def composite_support_load_bound_holds(n: int) -> bool:
    """Verify exact ``S(n)^2*n >= 4`` for a composite integer."""
    if not _is_composite(n):
        raise ValueError("n must be composite")
    S = support_log_derivative_load(n)
    if S * S * n < 4:
        raise AssertionError("composite support-load square-root bound failed")
    return True


def composite_unit_projective_bound(b: int, c: int) -> CompositeUnitProjectiveBound:
    """Verify ``sigma<=c^(3/2)/(2R)`` for ``1+b=c`` with b,c composite."""
    if c != b + 1 or b <= 1:
        raise ValueError("require unit relation 1+b=c")
    if not _is_composite(b) or not _is_composite(c):
        raise ValueError("both nonunit entries must be composite")
    composite_support_load_bound_holds(b)
    composite_support_load_bound_holds(c)
    state = projective_capacity_condition_state(1, b, c)
    R = state.radical_product
    sigma = state.sigma_projective
    left = (2 * R * sigma) ** 2
    right = c**3
    if left > right:
        raise AssertionError("composite-unit projective radical bound failed")
    return CompositeUnitProjectiveBound(
        b=b,
        c=c,
        radical_product=R,
        loads=(state.support_loads[1], state.support_loads[2]),
        sigma_projective=sigma,
        squared_bound_left=left,
        squared_bound_right=right,
    )


def oesterle_to_composite_unit_projective_eta_threshold(M: Fraction) -> Fraction:
    """Return ``3/2-1/M`` from Oesterle exponent M in (1,2)."""
    if not isinstance(M, Fraction) or not Fraction(1, 1) < M < Fraction(2, 1):
        raise ValueError("M must lie strictly between one and two")
    return Fraction(3, 2) - Fraction(1, 1) / M
