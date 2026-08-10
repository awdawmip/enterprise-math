"""Exact centered boundary carry for P017 signed divisor incidences.

Fix k>=2, M=k(k+1), K=k-1 and a positive odd divisor D transverse to M.
Signed incidences satisfy

    -K <= x <= K,
    x odd,
    D | M-x.

Parity and divisibility give one residue class modulo 2D.  Write

    K = qD+s,  0<=s<D,

and let y be the unique odd representative of M modulo D in the centered range

    -D < y < D.

Explicitly, if r=M mod D then

    y=r      when r is odd,
    y=r-D    when r is even.

The exact number F_D of signed incidences is

    F_D = q + eta_D,

where eta_D is one boundary bit:

    eta_D=1  iff |y|<=s       when q is even,
    eta_D=1  iff |y|>=D-s     when q is odd.

The proof is direct interval geometry.  When q=2h, the interior indices
`-h+1,...,h-1` contribute q-1 points and the two endpoints are both present
exactly for |y|<=s; otherwise exactly one endpoint is present.  When q=2h+1,
the central q points are always present and exactly one additional endpoint is
present precisely when y lies within s of either +/-D boundary.

Therefore the CG12 universal value q+1 differs from the exact fiber by exactly
one minus this bit.  More importantly, every transverse support moment has the
exact divisor expansion

    S_j(k) = sum_{D squarefree, omega(D)=j, p|D => p<=k,p∤M}
               [ floor((k-1)/D) + eta_D ].

This splits each moment into a bulk floor-density term plus a finite 0/1
boundary-carry term.  It is an exact identity, not an asymptotic sieve estimate.
Classical inclusion-exclusion owns the general combinatorics; the project value
is the centered square-basin carry coordinate and its interface to the adaptive
Bonferroni pressure test.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to


def signed_divisor_boundary_carry(k: int, divisor: int) -> dict[str, int | bool]:
    """Return F_D=floor((k-1)/D)+eta_D with the exact centered carry bit."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if (
        isinstance(divisor, bool)
        or not isinstance(divisor, int)
        or divisor <= 0
        or divisor % 2 == 0
    ):
        raise ValueError("divisor must be a positive odd integer")

    center = k * (k + 1)
    from math import gcd

    if gcd(divisor, center) != 1:
        raise ValueError("divisor must be transverse to M=k(k+1)")

    limit = k - 1
    coarse, remainder = divmod(limit, divisor)
    raw = center % divisor
    if raw == 0:
        raise AssertionError("transverse divisor unexpectedly divides the center")
    centered = raw if raw % 2 else raw - divisor
    if not (-divisor < centered < divisor) or centered % 2 == 0:
        raise AssertionError("failed to construct centered odd residue")

    if coarse % 2 == 0:
        carry = int(abs(centered) <= remainder)
        branch = "EVEN_COARSE"
    else:
        carry = int(abs(centered) >= divisor - remainder)
        branch = "ODD_COARSE"

    exact = coarse + carry
    universal = coarse + 1
    boundary_savings = universal - exact
    if carry not in (0, 1) or boundary_savings not in (0, 1):
        raise AssertionError("signed boundary carry left the binary range")

    return {
        "k": k,
        "center": center,
        "divisor": divisor,
        "coarse_quotient": coarse,
        "boundary_remainder": remainder,
        "raw_center_residue": raw,
        "centered_odd_residue": centered,
        "coarse_parity_even": coarse % 2 == 0,
        "branch": branch,
        "boundary_carry": carry,
        "exact_signed_fiber_size": exact,
        "cg12_universal_capacity": universal,
        "boundary_savings": boundary_savings,
    }


def transverse_support_moment_from_boundary_carries(k: int, order: int) -> dict[str, object]:
    """Reconstruct S_order exactly from squarefree divisor bulk plus carry bits.

    This executable enumerator is intended for bounded regression.  The formula
    itself is finite and exact for every k.
    """
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k) if p % 2 == 1 and center % p != 0
    )

    bulk = 0
    carries = 0
    term_count = 0
    rows: list[dict[str, object]] = []
    for subset in combinations(transverse, order):
        divisor = prod(subset)
        data = signed_divisor_boundary_carry(k, divisor)
        bulk += int(data["coarse_quotient"])
        carries += int(data["boundary_carry"])
        term_count += 1
        rows.append(
            {
                "primes": subset,
                "divisor": divisor,
                "coarse": int(data["coarse_quotient"]),
                "carry": int(data["boundary_carry"]),
                "exact_fiber": int(data["exact_signed_fiber_size"]),
            }
        )

    return {
        "k": k,
        "order": order,
        "transverse_prime_count": len(transverse),
        "squarefree_divisor_term_count": term_count,
        "bulk_floor_mass": bulk,
        "boundary_carry_mass": carries,
        "exact_support_moment": bulk + carries,
        "rows": tuple(rows),
    }
