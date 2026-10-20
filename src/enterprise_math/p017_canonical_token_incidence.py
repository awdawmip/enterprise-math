"""Canonical least-support incidence formula for P017 multi-prime tokens.

CG12 counts signed incidences of an arbitrary odd transverse divisor D.  A
Bonferroni/cutoff token needs one further condition: D contains the *least*
transverse small prime of the signed state.

Let p0 be the least prime divisor of a squarefree transverse token D.  Among
anchor-surviving signed points x with D | M-x, the token is canonical exactly
when no transverse odd prime q<p0 also divides M-x.

Write I_k(E) for the CG12 anchor-filtered signed incidence count of E.  Ordinary
Möbius exclusion over the smaller transverse primes gives the exact formula

    I_k^min(D)
      = sum_{Q squarefree, q|Q => q<p0, q transverse} mu(Q) I_k(DQ).

This converts the state-dependent "contains the least support prime" rule into a
pure signed-divisor sum.  For any positive odd order m, the total canonical
order-m defect-token mass is therefore

    sum_{D squarefree transverse, omega(D)=m+1} I_k^min(D),

with D automatically restricted to at most k(k+2) when it actually divides a
state in the open square basin.

Splitting the same sum at D<=k-1 versus D>k-1 gives an exact squarefree
product-cutoff decomposition into reusable and CG12-single-use token mass.  A
separate P017×P018 bridge may further sharpen this by complete prime-power block
products; this owner module intentionally stays at the squarefree support level.

All identities are finite CRT/Möbius arithmetic.  No canonical L-number or
Legendre proof is claimed.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .cutoff_pairing import distinct_prime_factors
from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_core_divisor_capacity import signed_divisor_capacity


def _validated_squarefree_token(k: int, divisor: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor < 3 or divisor % 2 == 0:
        raise ValueError("divisor must be an odd integer >=3")
    factors = tuple(distinct_prime_factors(divisor))
    if not factors or prod(factors) != divisor:
        raise ValueError("divisor must be squarefree")
    center = k * (k + 1)
    if any(prime > k or center % prime == 0 for prime in factors):
        raise ValueError("every token prime must be transverse and <=k")
    return factors


def smaller_transverse_primes(k: int, least_prime: int) -> tuple[int, ...]:
    """Return odd transverse primes below the declared least token prime."""
    if isinstance(least_prime, bool) or not isinstance(least_prime, int) or least_prime < 3:
        raise ValueError("least_prime must be an odd integer >=3")
    center = k * (k + 1)
    return tuple(
        prime
        for prime in primes_up_to(least_prime - 1)
        if prime != 2 and center % prime != 0
    )


def canonical_least_support_signed_points(k: int, divisor: int) -> tuple[int, ...]:
    """Directly filter CG12 incidences to those where min transverse support is in D."""
    factors = _validated_squarefree_token(k, divisor)
    least = factors[0]
    center = k * (k + 1)
    smaller = smaller_transverse_primes(k, least)
    points = tuple(
        point
        for point in signed_divisor_capacity(k, divisor)["anchor_signed_points"]
        if all((center - int(point)) % prime != 0 for prime in smaller)
    )
    return points


def canonical_least_support_incidence_mobius(k: int, divisor: int) -> dict[str, object]:
    """Evaluate I_min(D)=sum_Q mu(Q) I(DQ) and verify the direct token set."""
    factors = _validated_squarefree_token(k, divisor)
    least = factors[0]
    smaller = smaller_transverse_primes(k, least)

    total = 0
    terms: list[tuple[int, int, int]] = []
    for q_product, mu in squarefree_divisors_with_mu(list(smaller)):
        augmented = divisor * q_product
        incidence = int(signed_divisor_capacity(k, augmented)["anchor_count"])
        total += mu * incidence
        terms.append((q_product, mu, incidence))

    direct = canonical_least_support_signed_points(k, divisor)
    if total != len(direct):
        raise AssertionError("least-support Möbius formula disagrees with direct signed incidences")
    if total < 0:
        raise AssertionError("canonical least-support incidence cannot be negative")

    return {
        "k": k,
        "divisor": divisor,
        "token_primes": factors,
        "least_token_prime": least,
        "smaller_transverse_primes": smaller,
        "mobius_terms": tuple(terms),
        "canonical_signed_points": direct,
        "canonical_incidence": total,
        "cg12_capacity": int(signed_divisor_capacity(k, divisor)["universal_capacity"]),
        "single_use_by_squarefree_product": divisor > k - 1,
    }


def canonical_order_token_incidence(k: int, divisor: int, order: int) -> dict[str, object]:
    """Return the canonical incidence of one order-m token with omega(D)=m+1."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    factors = _validated_squarefree_token(k, divisor)
    if len(factors) != order + 1:
        raise ValueError("order-m token must contain exactly m+1 distinct primes")
    return {
        **canonical_least_support_incidence_mobius(k, divisor),
        "order": order,
    }


def canonical_token_incidence_profile(k: int, order: int) -> dict[str, object]:
    """Enumerate the exact squarefree order-m token divisor sum for bounded auditing.

    This is a reference enumerator, not an intended large-k algorithm.  Products
    above k(k+2) cannot divide any state in the open square basin and are skipped.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    center = k * (k + 1)
    transverse = [
        prime
        for prime in primes_up_to(k)
        if prime != 2 and center % prime != 0
    ]
    max_state = k * (k + 2)
    rows: list[dict[str, object]] = []
    total = 0
    reusable = 0
    single_use = 0
    for subset in combinations(transverse, order + 1):
        divisor = prod(subset)
        if divisor > max_state:
            continue
        data = canonical_order_token_incidence(k, divisor, order)
        count = int(data["canonical_incidence"])
        if count == 0:
            continue
        rows.append(data)
        total += count
        if divisor <= k - 1:
            reusable += count
        else:
            single_use += count

    if total != reusable + single_use:
        raise AssertionError("token product-cutoff split failed")
    return {
        "k": k,
        "order": order,
        "token_rows": tuple(rows),
        "canonical_token_mass": total,
        "reusable_squarefree_token_mass": reusable,
        "single_use_squarefree_token_mass": single_use,
    }
