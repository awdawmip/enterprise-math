"""Aggregate low-product Walsh blocks through a reciprocal-Mobius quotient kernel.

Let P be the finite set of odd transverse primes for the pronic center M=k(k+1).
For squarefree P-products q,e with gcd(q,e)=1, let B(q,e) be the self-dual
bi-primitive tent block.  Consider the ordered low-product aggregate

    S_k = sum_(q*e<=k) mu(q) B(q,e).

By self-duality, the corresponding two-orientation nontrivial Walsh aggregate is
twice this ordered form (after the usual coarse term is separated).

Fix q and perform the second-axis primitive inversion only.  If P(q,f) denotes
the block primitive in q but still physical in the f-axis, then

    B(q,e)=1/e * sum_(f|e) mu(e/f) f P(q,f).

Write e=f*l.  Squarefreeness makes f and l coprime, and the transverse prime
family keeps every factor coprime to M.  Switching the finite sums gives the
exact aggregate compiler

    S_k
      = sum_(q*f<=k) mu(q) P(q,f)
          H_(qf)( floor(k/(qf)) ),

where

    H_A(L)
      = sum_(l<=L, l squarefree transverse, gcd(l,A)=1) mu(l)/l.

Thus the entire second conductor axis is compressed to a reciprocal-Mobius
kernel whose precision is the small quotient

    a=floor(k/(q*f)).

For a=1 the kernel is exactly 1; with only odd transverse primes the same is
true for a=2.  Large quotient strips acquire ordinary reciprocal-Mobius
cancellation, while the first few quotient strips remain unsmoothed.  This is
an exact algebraic localization, not a quantitative Mertens estimate.

The theorem identifies a new aggregate hard core: the low quotient strips,
especially a=1, rather than the full conductor plane.  It does not prove these
strips are small or prove Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .legendre import primes_up_to
from .p017_p018_euclidean_biprimitive import biprimitive_block
from .p017_p018_poisson_conductor_mobius import primitive_conductor_block


def _mobius_squarefree_product(value: int, primes: tuple[int, ...]) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    if value == 1:
        return 1
    remaining = value
    count = 0
    for p in primes:
        if remaining % p == 0:
            remaining //= p
            count += 1
            if remaining % p == 0:
                return 0
    if remaining != 1:
        raise ValueError("value uses a prime outside the declared transverse family")
    return -1 if count % 2 else 1


def _transverse_primes(k: int) -> tuple[int, ...]:
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def _squarefree_products(primes: tuple[int, ...], cutoff: int) -> tuple[int, ...]:
    values = [1]
    for p in primes:
        additions = []
        for value in values:
            if value <= cutoff // p:
                additions.append(value * p)
        values.extend(additions)
    return tuple(sorted(set(values)))


def reciprocal_mobius_kernel(k: int, A: int, L: int) -> Fraction:
    """Return H_A(L) over odd squarefree transverse products exactly."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(A, bool) or not isinstance(A, int) or A < 1:
        raise ValueError("A must be positive")
    if isinstance(L, bool) or not isinstance(L, int) or L < 1:
        raise ValueError("L must be positive")
    primes = _transverse_primes(k)
    total = Fraction(0, 1)
    for ell in _squarefree_products(primes, L):
        if gcd(ell, A) != 1:
            continue
        mu = _mobius_squarefree_product(ell, primes)
        total += Fraction(mu, ell)
    return total


def ordered_low_product_biprimitive_sum(k: int) -> Fraction:
    """Return S_k=sum_(q e<=k)mu(q)B(q,e) by direct bounded enumeration."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    primes = _transverse_primes(k)
    products = _squarefree_products(primes, k)
    total = Fraction(0, 1)
    for q in products:
        mu_q = _mobius_squarefree_product(q, primes)
        for e in products:
            if q > k // e or gcd(q, e) != 1:
                continue
            total += mu_q * biprimitive_block(M, k, q, e)
    return total


def mobius_harmonic_aggregate(k: int) -> dict[str, object]:
    """Verify the exact quotient-kernel compiler on a bounded scale."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    primes = _transverse_primes(k)
    products = _squarefree_products(primes, k)
    direct = ordered_low_product_biprimitive_sum(k)
    transformed = Fraction(0, 1)
    rows: list[dict[str, object]] = []

    for q in products:
        mu_q = _mobius_squarefree_product(q, primes)
        for f in products:
            if q > k // f or gcd(q, f) != 1:
                continue
            quotient = k // (q * f)
            kernel = reciprocal_mobius_kernel(k, q * f, quotient)
            primitive_q = primitive_conductor_block(M, k, q, f)
            term = mu_q * primitive_q * kernel
            transformed += term
            rows.append(
                {
                    "q": q,
                    "f": f,
                    "product_qf": q * f,
                    "quotient_strip": quotient,
                    "mu_q": mu_q,
                    "primitive_q_axis_block": primitive_q,
                    "reciprocal_mobius_kernel": kernel,
                    "term": term,
                }
            )

    if transformed != direct:
        raise AssertionError("Mobius-harmonic aggregate compiler failed exact reconstruction")
    quotient_one = sum(row["term"] for row in rows if int(row["quotient_strip"]) == 1)
    quotient_two = sum(row["term"] for row in rows if int(row["quotient_strip"]) == 2)
    return {
        "k": k,
        "center": M,
        "transverse_primes": primes,
        "direct_ordered_low_product_sum": direct,
        "transformed_ordered_low_product_sum": transformed,
        "rows": tuple(rows),
        "quotient_one_contribution": quotient_one,
        "quotient_two_contribution": quotient_two,
        "mobius_harmonic_aggregate_identity": True,
    }
