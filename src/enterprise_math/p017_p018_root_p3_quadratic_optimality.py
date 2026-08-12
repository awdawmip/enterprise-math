"""Optimality of the Generation-4 quadratic support lower weight.

Consider normalized quadratic weights in the binomial support basis

    w(c) = 1 - A*c + B*C(c,2),    c=0,1,2,3.

To be a pointwise lower bound for the prime indicator on the fourth-root P3
support spectrum, it is necessary and sufficient that

    w(1)<=0, w(2)<=0, w(3)<=0,

or equivalently

    A>=1,
    B<=2A-1,
    B<=A-1/3.

Under an independent local model with total first-order medium-prime mass
lambda and pair mass lambda^2/2, the normalized main coefficient is

    M(A,B;lambda)=1-A*lambda+(B/2)*lambda^2.

For 0<lambda<2, M is maximized over the feasible region uniquely at

    A=1, B=2/3.

Proof: for fixed A, maximize B, hence B=A-1/3 (since A>=1).  Then

    M = 1-lambda^2/6 + A*(-lambda+lambda^2/2),

and the coefficient of A is negative for 0<lambda<2, so A is minimized at 1.

Thus the project weight

    w_2(c)=1-c+(2/3)C(c,2)

is not an ad hoc truncation: it is the unique locally-main-term-optimal
quadratic pointwise lower weight on the P3 support spectrum whenever lambda<2.
At the fourth-root square interval lambda->log 2, its local coefficient is

    1-log 2+(log 2)^2/3 ~ 0.467003824.

This is a finite optimization statement.  It does not control the correlated
short-interval remainder required to turn the local main coefficient into a
pointwise prime theorem.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, log


def feasible_quadratic_weight(A: Fraction, B: Fraction) -> bool:
    """Return whether 1-Ac+B*C(c,2) is <=1_{c=0} for c=0..3."""
    return all(
        Fraction(1) - A * c + B * comb(c, 2) <= (1 if c == 0 else 0)
        for c in range(4)
    )


def optimal_quadratic_weight() -> tuple[Fraction, Fraction]:
    """Return the unique optimum (A,B) valid for every local mass 0<lambda<2."""
    return Fraction(1), Fraction(2, 3)


def quadratic_weight_values(A: Fraction, B: Fraction) -> tuple[Fraction, ...]:
    """Return w(c), c=0..3."""
    return tuple(Fraction(1) - A * c + B * comb(c, 2) for c in range(4))


def local_main_coefficient(lam: float, A: Fraction | None = None, B: Fraction | None = None) -> float:
    """Return 1-A*lambda+(B/2)*lambda^2 for a selected feasible weight."""
    if not 0 < lam < 2:
        raise ValueError("lambda must lie in (0,2)")
    if A is None or B is None:
        A, B = optimal_quadratic_weight()
    if not feasible_quadratic_weight(A, B):
        raise ValueError("weight is not pointwise feasible")
    return 1.0 - float(A) * lam + 0.5 * float(B) * lam * lam


def fourth_root_log2_margin() -> dict[str, float]:
    """Return first-order and optimal quadratic local margins at lambda=log 2."""
    lam = log(2.0)
    return {
        "lambda": lam,
        "first_order_margin": 1.0 - lam,
        "optimal_quadratic_margin": local_main_coefficient(lam),
        "pair_overlap_gain": local_main_coefficient(lam) - (1.0 - lam),
    }
