"""Offset-divisor normal form for direct p-2-root half-defect incidences.

Suppose p is in the target p=5 or 23 (mod 24) family, m=(p-1)/2, and a
canonical A-support candidate comes directly from an odd prime q dividing p-2.
If d=m-j is its companion offset, then exactly one of the following holds:

  plus side:  j=(q+1)/2, q|d,     p=2d+q+2;
  minus side: j=(q-1)/2, q|(d-1), p=2d+q.

Writing d=tq or d-1=tq recovers p-2=(2t+1)q.  Since target p=2 mod3 and
q!=3, necessarily t=1 mod3.  The q=3 candidates are indices 2 and 1 and are
harmless for p>5.

Thus direct-root cancellation at offset d can be tested from the prime divisors
of d and d-1 alone.  The remaining condition is p|H_d for the universal integer
midpoint companion.
"""

from __future__ import annotations

from .p022_barlow_franel_integer_companion import midpoint_integer_companion
from .p022_barlow_low_order_defect_reduction import _factor_integer, _is_prime


def _require_offset(offset: int) -> None:
    if isinstance(offset, bool) or not isinstance(offset, int) or offset <= 0:
        raise ValueError("offset must be a positive integer")


def odd_prime_divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    return tuple(prime for prime, _ in _factor_integer(value) if prime != 2)


def plus_root_prime_from_offset(offset: int, root_prime: int) -> int:
    """p=2d+q+2 when q is the direct root and q|d."""
    _require_offset(offset)
    if root_prime not in odd_prime_divisors(offset):
        raise ValueError("root_prime must be an odd prime divisor of offset")
    return 2 * offset + root_prime + 2


def minus_root_prime_from_offset(offset: int, root_prime: int) -> int:
    """p=2d+q when q is the direct root and q|(d-1)."""
    _require_offset(offset)
    if offset <= 1 or root_prime not in odd_prime_divisors(offset - 1):
        raise ValueError("root_prime must be an odd prime divisor of offset-1")
    return 2 * offset + root_prime


def target_direct_root_candidates(offset: int) -> tuple[tuple[str, int, int], ...]:
    """Return (side,q,p) candidates satisfying target AP and t=1 mod3.

    q=3 is omitted: direct q=3 A-indices are 2 and 1, both p-units for target
    p>5 and hence cannot cause a Franel support-zero cancellation.
    """
    _require_offset(offset)
    candidates = []
    for q in odd_prime_divisors(offset):
        if q == 3:
            continue
        t = offset // q
        if t % 3 != 1:
            continue
        p = plus_root_prime_from_offset(offset, q)
        if p > 5 and p % 24 in (5, 23) and _is_prime(p):
            candidates.append(("plus", q, p))
    if offset > 1:
        for q in odd_prime_divisors(offset - 1):
            if q == 3:
                continue
            t = (offset - 1) // q
            if t % 3 != 1:
                continue
            p = minus_root_prime_from_offset(offset, q)
            if p > 5 and p % 24 in (5, 23) and _is_prime(p):
                candidates.append(("minus", q, p))
    return tuple(sorted(candidates))


def direct_root_companion_incidents(offset: int) -> tuple[tuple[str, int, int], ...]:
    """Target direct-root candidates whose p also divides H_d."""
    companion = midpoint_integer_companion(offset)
    return tuple(
        candidate
        for candidate in target_direct_root_candidates(offset)
        if companion % candidate[2] == 0
    )


def direct_root_candidate_product(offset: int) -> int:
    """Product of distinct target candidate primes at one offset."""
    result = 1
    for prime in sorted({candidate[2] for candidate in target_direct_root_candidates(offset)}):
        result *= prime
    return result


def direct_root_incidence_gcd(offset: int) -> int:
    """gcd(|H_d|, product of direct-root target candidate primes)."""
    from math import gcd

    product = direct_root_candidate_product(offset)
    return gcd(abs(midpoint_integer_companion(offset)), product)
