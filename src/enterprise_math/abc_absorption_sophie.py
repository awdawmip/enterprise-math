"""Squarefree unit-relation calibration using Sophie Germain prime pairs.

For an odd prime q with c=2q+1 prime, the primitive triple

    1 + 2q = c

is completely squarefree, so ``eta_min=1``.  Nevertheless the exact radius for
attaining that floor is the minimum L-infinity Bezout radius of

    q*x_2 + 2*x_q = 1,

namely ``(q-1)/2``.  The first nondegenerate witness radius is only 2 for
q>=5.  This cleanly separates arithmetic-floor content from access geometry.

The Sophie Germain prime terminology and Bezout arithmetic are classical.  No
infinitude claim is made.
"""

from __future__ import annotations

from .abc_absorption_formula import minimum_absorption_redundancy_support_formula
from .abc_absorption_two_variable import minimum_linf_diophantine_solution
from .abc_support import prime_factorization


def sophie_germain_absorption_access(q: int) -> dict[str, int | tuple[tuple[int, int], ...]]:
    """Return exact witness-access data for ``1+2q=2q+1`` with both primes."""
    if isinstance(q, bool) or not isinstance(q, int) or q < 3:
        raise ValueError("q must be an odd prime >= 3")
    if prime_factorization(q) != ((q, 1),):
        raise ValueError("q must be prime")
    c = 2 * q + 1
    if prime_factorization(c) != ((c, 1),):
        raise ValueError("2q+1 must be prime")

    eta = minimum_absorption_redundancy_support_formula(1, 2 * q, c)
    if eta != 1:
        raise AssertionError("squarefree Sophie triple must have eta_min=1")

    floor_solution = minimum_linf_diophantine_solution(q, 2, 1)
    expected_nu = (q - 1) // 2
    if floor_solution.radius != expected_nu:
        raise AssertionError("two-prime squarefree floor radius formula failed")

    if q == 3:
        mu = 1
    else:
        # x_2=0, x_q=1 gives W=2 and witness (0,1,2), so mu<=2.
        # Radius 1 cannot give nonzero W of magnitude <=1: with x_2=0,
        # W is even; with x_2=+/-1, |W|>=q-2>=3.
        mu = 2
    nu = expected_nu
    delta = nu - mu
    if delta < 0:
        raise AssertionError("floor access cannot precede first witness radius")

    if q == 3:
        frontier = ((1, 1),)
    elif q == 5:
        frontier = ((2, 1),)
    else:
        frontier = ((2, 2), (nu, 1))

    return {
        "q": q,
        "safe_prime": c,
        "eta_min": eta,
        "mu": mu,
        "nu": nu,
        "delta_abs": delta,
        "floor_witness_2_q_c": (floor_solution.u, floor_solution.v, 1),
        "pareto_frontier": frontier,
    }
