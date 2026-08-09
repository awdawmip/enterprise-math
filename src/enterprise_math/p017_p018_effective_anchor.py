"""Effective odd-anchor classification for the finite P017 radius window.

For P017 put M=k(k+1) and 1<=r<k.  An odd prime divisor p|M affects the
finite anchor-survival condition only when p<k; if p>=k, no positive radius in
the window is divisible by p.  Call the odd primes

    p | M,  p < k

*effective odd anchors*.

There is an exact classification of the zero-effective-anchor case.

* If k is even and has no effective odd anchor, k has no odd prime divisor and
  is therefore a power of two.  The odd number k+1 must be prime, because any
  proper odd prime divisor of a composite k+1 is <k.
* If k is odd and has no effective odd anchor, k itself must be prime.  The even
  number k+1 can have no odd prime divisor, so it is a power of two.

Thus the only anchor-critical scales are

    k = 2^m with k+1 prime,

or

    k prime with k+1 = 2^m.

On these scales anchor survival inside 1<=r<k is exactly odd parity: the endpoint
prime is outside the open radius window.  Hence the surviving-radius count is
``k/2`` in the even case and ``(k-1)/2`` in the odd case.

This finite classification explains why asymptotic Euler factors from a large
anchor prime near k must not be interpreted as an actual finite-radius density
loss.  It is an exact routing theorem, not a Legendre proof.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime, primes_up_to


def is_power_of_two(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return False
    return value & (value - 1) == 0


def effective_odd_anchor_primes(k: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    center = k * (k + 1)
    return tuple(
        p for p in primes_up_to(k - 1) if p % 2 == 1 and center % p == 0
    )


def anchor_surviving_radius_count(k: int) -> int:
    """Return the exact finite count #{1<=r<k:gcd(r,k(k+1))=1}."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    center = k * (k + 1)
    return sum(1 for radius in range(1, k) if gcd(radius, center) == 1)


def anchor_critical_classification(k: int) -> dict[str, object]:
    """Classify whether the finite radius window has no effective odd anchor."""
    anchors = effective_odd_anchor_primes(k)
    surviving = anchor_surviving_radius_count(k)
    if anchors:
        return {
            "k": k,
            "critical": False,
            "kind": "HAS_EFFECTIVE_ODD_ANCHOR",
            "effective_odd_anchors": anchors,
            "surviving_radius_count": surviving,
        }

    if k % 2 == 0:
        if not is_power_of_two(k):
            raise AssertionError("even zero-anchor scale is not a power of two")
        if not is_prime(k + 1):
            raise AssertionError("even zero-anchor scale has composite odd successor")
        kind = "POWER_OF_TWO_WITH_PRIME_SUCCESSOR"
        expected = k // 2
    else:
        if not is_prime(k):
            raise AssertionError("odd zero-anchor scale is not prime")
        if not is_power_of_two(k + 1):
            raise AssertionError("odd zero-anchor scale does not precede a power of two")
        kind = "PRIME_BEFORE_POWER_OF_TWO"
        expected = (k - 1) // 2

    if surviving != expected:
        raise AssertionError("critical anchor survival did not reduce exactly to odd parity")
    return {
        "k": k,
        "critical": True,
        "kind": kind,
        "effective_odd_anchors": (),
        "surviving_radius_count": surviving,
        "parity_only_count": expected,
    }
