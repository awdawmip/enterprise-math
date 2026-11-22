"""Finite-cutoff effective-anchor refinement of the uniform Rankin bound.

The original uniform Rankin bridge uses every odd prime divisor of M in the
anchor normalization.  For the truncated core sum S<x this is unnecessarily
coarse: a prime p>=x cannot divide any positive S<x.  Hence

    gcd(S,M)=1  (S<x)

is equivalent to coprimality with the squarefree *effective anchor radical*

    R_M(x) = prod_{odd p|M, p<x} p.

Put

    delta_{M,x} = prod_{odd p|M, p<x} (1-1/p).

The same local Rankin inequality used in ``p017_p018_core_mass_rankin`` then
multiplies only the effective anchor ratios, giving

    delta_{M,x}^(-2) F_{M,x}(sigma)
       <= R_M(x)^sigma F_1(sigma).

Thus the moving-parameter upper bound sharpens from the old ``(xM)^sigma`` to
``(x R_M(x))^sigma``.  With sigma=1/log(x R_M(x)) this yields the symbolic
uniform estimate

    delta_{M,x}^(-2) A_M(x)
      <= (e*pi^2/8) [1+log(x R_M(x))]^2,

whenever the logarithmic choice is in range.  The executable functions below
prove the finite coprimality reduction and expose the exact radical/density; they
do not numerically approximate e, pi, logarithms or zeta.

For P017 x=k and M=k(k+1).  On the anchor-critical families classified in
``p017_p018_effective_anchor`` one has R_M(k)=1, so the uniform Rankin scale is
``log k`` rather than ``log(kM)``.  This is a finite-cutoff improvement, not an
asymptotic claim and not a Legendre proof.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to


def effective_anchor_radical(center: int, cutoff: int) -> dict[str, object]:
    if isinstance(center, bool) or not isinstance(center, int) or center <= 0:
        raise ValueError("center must be a positive integer")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff <= 1:
        raise ValueError("cutoff must be an integer > 1")

    primes = tuple(
        p
        for p in primes_up_to(cutoff - 1)
        if p % 2 == 1 and center % p == 0
    )
    radical = 1
    density_numerator = 1
    density_denominator = 1
    for prime in primes:
        radical *= prime
        density_numerator *= prime - 1
        density_denominator *= prime
    common = gcd(density_numerator, density_denominator)
    density = (
        density_numerator // common,
        density_denominator // common,
    )
    return {
        "center": center,
        "cutoff": cutoff,
        "effective_odd_anchor_primes": primes,
        "effective_anchor_radical": radical,
        "effective_odd_anchor_density": density,
    }


def truncated_coprimality_equivalence(center: int, cutoff: int, value: int) -> dict[str, object]:
    """Certify gcd(value,center)=1 iff gcd(value,R_M(cutoff))=1 for value<cutoff."""
    if isinstance(value, bool) or not isinstance(value, int) or not (1 <= value < cutoff):
        raise ValueError("value must satisfy 1 <= value < cutoff")
    data = effective_anchor_radical(center, cutoff)
    radical = int(data["effective_anchor_radical"])
    full = gcd(value, center) == 1
    reduced = gcd(value, radical) == 1

    # The missing factor 2 is intentional: residual core products S are odd.
    # For a general value, evenness can distinguish the two predicates.
    if value % 2 == 1 and full != reduced:
        raise AssertionError("odd truncated coprimality depends on a prime >= cutoff")
    return {
        **data,
        "value": value,
        "value_is_odd": value % 2 == 1,
        "coprime_to_center": full,
        "coprime_to_effective_odd_radical": reduced,
        "equivalent_on_odd_core_domain": (value % 2 == 0) or (full == reduced),
    }


def p017_effective_rankin_parameters(k: int) -> dict[str, object]:
    """Return x=k, M=k(k+1), R_M(k) and delta_{M,k} for the hard-core sum."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    center = k * (k + 1)
    data = effective_anchor_radical(center, k)
    return {
        "k": k,
        **data,
        "old_rankin_scale_product": k * center,
        "effective_rankin_scale_product": k * int(data["effective_anchor_radical"]),
    }
