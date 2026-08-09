"""Closed absorption-access formulas for ``1+2*r=3^m`` with r prime.

If ``r=(3^m-1)/2`` is prime, then the P025 two-prime-block floor equation is

    r*u + 2*v = m*3^(m-1),  x_3 = 1.

Primality of the base-3 repunit forces m to be prime.  The parity constraint
makes u odd, and the nearest admissible odd integer to the real balance ratio
is explicit.  This yields a closed formula for the exact access radius.

The repunit factorization facts are classical; no claim is made about the
infinitude of such primes.
"""

from __future__ import annotations

from .abc_absorption_two_variable import minimum_linf_diophantine_solution
from .abc_support import prime_factorization


def base3_repunit_prime_access(exponent: int) -> dict[str, int | tuple[int, int, int]]:
    """Return the exact floor-access witness for ``1+2*r=3^exponent``.

    Requires ``r=(3^exponent-1)/2`` to be prime.  The returned witness is in
    coordinate order ``(2,r,3)``.
    """
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 2:
        raise ValueError("exponent must be an integer >= 2")
    T = 3**exponent
    r = (T - 1) // 2
    if prime_factorization(r) != ((r, 1),):
        raise ValueError("(3^exponent-1)/2 must be prime")
    if prime_factorization(exponent) != ((exponent, 1),):
        raise AssertionError("prime base-3 repunit implies prime exponent")

    m = exponent
    H = m * 3 ** (m - 1)
    if m == 3:
        u = 3
        v = -6
    elif m % 6 == 1:
        u = (2 * m + 1) // 3
        v = (2 * m + 1 - T) // 12
    elif m % 6 == 5:
        u = (2 * m - 1) // 3
        v = (T + 2 * m - 1) // 12
    else:
        raise AssertionError("prime exponent >3 must be congruent to 1 or 5 mod 6")

    if r * u + 2 * v != H:
        raise AssertionError("closed repunit witness escaped floor equation")
    nu = max(abs(u), abs(v), 1)

    # Independent generic exact solver audit.
    generic = minimum_linf_diophantine_solution(r, 2, H)
    if generic.radius != nu or r * generic.u + 2 * generic.v != H:
        raise AssertionError("closed repunit formula disagrees with exact Diophantine solver")

    return {
        "exponent": m,
        "repunit_prime": r,
        "eta_min": m,
        "target": H,
        "witness_2_r_3": (u, v, 1),
        "nu": nu,
    }


def repunit_access_closed_radius(exponent: int) -> int:
    """Return only the exact ``nu`` for the prime-repunit family."""
    return int(base3_repunit_prime_access(exponent)["nu"])
