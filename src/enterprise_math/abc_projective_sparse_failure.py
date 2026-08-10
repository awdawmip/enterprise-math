"""Elementary sparse-failure mechanism for the Projective Capacity Condition.

If ``sigma_proj >= c^eta`` then one cyclic term

    m(n_i) / K_jk >= c^eta

is large.  The denominator ``K_jk`` is a positive integer, so necessarily

    m(n_i) >= c^eta.

For ``n=prod p^e`` let

    q(n)=prod p^floor(e/2).

Then ``q(n)^2`` is the largest square divisor of n and satisfies

    q(n)^2 >= m(n)=n/rad(n).

Thus every PCC failure contains a component with a square divisor of size at
least ``c^(eta/2)`` in square-root scale.  On a dyadic interval ``X/2<c<=X``,
a union bound over square divisors gives O(X^(1-eta/2)) possible component
values and therefore O(X^(2-eta/2)) additive triples after choosing the other
additive coordinate.

This is an elementary power-saving sparsity mechanism.  It is not a pointwise
PCC theorem and not an abc proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import multiplicity_residual, prime_factorization


@dataclass(frozen=True)
class LargeResidualWitness:
    abc: tuple[int, int, int]
    component_index: int
    component_value: int
    multiplicity_residual: int
    square_root_divisor: int
    square_divisor: int


def largest_square_divisor_root(n: int) -> int:
    """Return ``prod p^floor(v_p(n)/2)`` exactly."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    result = 1
    for prime, exponent in prime_factorization(n):
        result *= prime ** (exponent // 2)
    return result


def square_divisor_dominates_residual(n: int) -> bool:
    """Verify ``largest_square_divisor >= multiplicity residual``."""
    root = largest_square_divisor_root(n)
    square = root * root
    residual = multiplicity_residual(n)
    if square < residual:
        raise AssertionError("largest square divisor failed to dominate multiplicity residual")
    return True


def projective_failure_large_residual_witness(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> LargeResidualWitness | None:
    """Return a component forced large when ``sigma_proj >= c^(p/q)``.

    The threshold test is exact.  ``None`` means PCC holds for this triple and
    exponent.  On failure, the returned component has

        m(component)^q >= c^p.
    """
    if not 0 < numerator < denominator:
        raise ValueError("require 0 < numerator < denominator")
    state = projective_capacity_condition_state(a, b, c)
    sigma = state.sigma_projective
    if sigma.numerator**denominator < sigma.denominator**denominator * c**numerator:
        return None

    residuals = tuple(multiplicity_residual(n) for n in (a, b, c))
    # The cyclic ratios are ordered c,b,a, with denominator integer >=1.
    cyclic_components = (2, 1, 0)
    candidates: list[int] = []
    for ratio, component_index in zip(state.cyclic_weighted_defects, cyclic_components, strict=True):
        if ratio.numerator**denominator >= ratio.denominator**denominator * c**numerator:
            candidates.append(component_index)
    if not candidates:
        raise AssertionError("projective max failed to expose a failing cyclic component")

    for index in candidates:
        residual = residuals[index]
        if residual**denominator >= c**numerator:
            n = (a, b, c)[index]
            root = largest_square_divisor_root(n)
            square = root * root
            if square < residual:
                raise AssertionError("square divisor failed residual domination")
            return LargeResidualWitness(
                abc=(a, b, c),
                component_index=index,
                component_value=n,
                multiplicity_residual=residual,
                square_root_divisor=root,
                square_divisor=square,
            )
    raise AssertionError("PCC failure did not force a component residual above threshold")


def dyadic_square_divisor_union_bound(X: int, numerator: int, denominator: int) -> int:
    """Return a finite union-bound count for possible large-residual components.

    For ``X/2 < c <= X`` and eta=p/q, any failure component has a square
    divisor root s satisfying

        s^(2q) >= (X/2)^p.

    We compute the smallest integer s0 with that property and return

        sum_{s=s0}^{floor(sqrt X)} floor(X/s^2),

    an explicit upper bound on the number of integers n<=X that can contain
    such a square divisor.  The asymptotic size is O(X^(1-p/(2q))).
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    if not 0 < numerator < denominator:
        raise ValueError("require 0 < numerator < denominator")
    # Need s^(2q) >= (X/2)^p.  Avoid fractions: 2^p s^(2q) >= X^p.
    s0 = 1
    while (2**numerator) * (s0 ** (2 * denominator)) < X**numerator:
        s0 += 1
    return sum(X // (s * s) for s in range(s0, isqrt(X) + 1))
