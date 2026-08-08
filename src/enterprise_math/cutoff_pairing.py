"""Sign-reversing cutoff pairings for the Legendre pressure test.

The identities here are exact finite Möbius cancellations on square-free divisor
lattices.  They do not prove Legendre's conjecture.  Their purpose is to isolate
the divisor terms that actually cross a chosen cutoff and to expose the integer
root hierarchy forced on negative boundary terms.
"""

from __future__ import annotations

from .core import integer_nth_root
from .legendre import squarefree_divisors_with_mu


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_distinct_primes(primes: list[int]) -> None:
    if len(primes) != len(set(primes)):
        raise ValueError("primes must be distinct")
    for p in primes:
        if isinstance(p, bool) or not isinstance(p, int) or p < 2:
            raise ValueError("primes must contain positive prime-like integers >= 2")


def mobius_divisor_tail(primes: list[int], threshold: int) -> int:
    """Return sum(mu(d)) over square-free divisors d above ``threshold``.

    ``primes`` is interpreted as the distinct prime support of a square-free
    product.  Primality is not rechecked here because this helper is also useful
    for abstract Boolean-lattice regression tests.
    """
    _require_distinct_primes(primes)
    _require_nonnegative("threshold", threshold)
    return sum(
        mu
        for d, mu in squarefree_divisors_with_mu(primes)
        if d > threshold
    )


def cutoff_crossing_boundary_sum(
    primes: list[int], distinguished_prime: int, threshold: int
) -> int:
    """Evaluate the cutoff-crossing side of the sign-reversing pairing.

    For a square-free product with distinguished factor p,

        sum_{d>T} mu(d)
        = - sum_{c | G/p, c<=T<pc} mu(c).

    Toggling p pairs all divisor terms that stay on the same side of the cutoff;
    only edges crossing the cutoff survive.
    """
    _require_distinct_primes(primes)
    _require_nonnegative("threshold", threshold)
    if distinguished_prime not in primes:
        raise ValueError("distinguished_prime must belong to primes")

    rest = [p for p in primes if p != distinguished_prime]
    return -sum(
        mu
        for c, mu in squarefree_divisors_with_mu(rest)
        if c <= threshold < distinguished_prime * c
    )


def cutoff_crossing_terms(
    primes: list[int], distinguished_prime: int, threshold: int
) -> list[tuple[int, int, int, int]]:
    """Return unpaired cutoff edges as ``(c, b, mu_c, mu_b)``.

    Here b=p*c, c<=T<b, and mu_b=-mu_c.  Every divisor strictly above T that
    is not represented by one of these edges is cancelled by toggling p.
    """
    _require_distinct_primes(primes)
    _require_nonnegative("threshold", threshold)
    if distinguished_prime not in primes:
        raise ValueError("distinguished_prime must belong to primes")

    rest = [p for p in primes if p != distinguished_prime]
    terms: list[tuple[int, int, int, int]] = []
    for c, mu_c in squarefree_divisors_with_mu(rest):
        b = distinguished_prime * c
        if c <= threshold < b:
            terms.append((c, b, mu_c, -mu_c))
    return terms


def distinct_prime_factors(n: int) -> list[int]:
    """Return the distinct prime factors of n in increasing order."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    factors: list[int] = []
    candidate = 2
    remaining = n
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append(remaining)
    return factors


def transverse_prime_support(n: int, k: int, anchor_product: int) -> list[int]:
    """Return prime factors p<=k of n that are not anchor primes."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(anchor_product, bool) or not isinstance(anchor_product, int) or anchor_product < 1:
        raise ValueError("anchor_product must be a positive integer")
    return [
        p
        for p in distinct_prime_factors(n)
        if p <= k and anchor_product % p != 0
    ]


def negative_boundary_root_bound(
    least_prime: int, boundary_divisor: int, threshold: int
) -> tuple[int, int, int]:
    """Return and verify the odd-depth integer-root bound for a negative edge.

    A negative square-free boundary divisor has odd prime depth 2m+1.  If
    ``least_prime`` is its least prime factor and removing that factor gives a
    divisor <= threshold, then

        least_prime <= R_{2m}(threshold).

    The return value is ``(m, root_bound, reduced_divisor)``.  Invalid inputs
    that do not describe such a negative cutoff edge raise ``ValueError``.
    """
    if isinstance(least_prime, bool) or not isinstance(least_prime, int) or least_prime < 2:
        raise ValueError("least_prime must be an integer >= 2")
    if isinstance(boundary_divisor, bool) or not isinstance(boundary_divisor, int) or boundary_divisor < 1:
        raise ValueError("boundary_divisor must be positive")
    _require_nonnegative("threshold", threshold)
    if boundary_divisor % least_prime != 0:
        raise ValueError("least_prime must divide boundary_divisor")

    factors = distinct_prime_factors(boundary_divisor)
    if factors[0] != least_prime:
        raise ValueError("least_prime must be the least prime factor")
    if len(factors) % 2 != 1:
        raise ValueError("a negative Mobius boundary divisor must have odd prime depth")
    if len(factors) < 3:
        raise ValueError("a cutoff-crossing negative edge here must have depth at least 3")

    reduced = boundary_divisor // least_prime
    if reduced > threshold or boundary_divisor <= threshold:
        raise ValueError("the divisor must cross the cutoff after toggling least_prime")

    m = (len(factors) - 1) // 2
    root_bound = integer_nth_root(threshold, 2 * m)
    if least_prime > root_bound:
        raise ValueError("inputs violate the integer-root boundary theorem")
    return m, root_bound, reduced
