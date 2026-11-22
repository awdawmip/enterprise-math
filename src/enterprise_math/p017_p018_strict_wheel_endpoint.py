"""Strict-wheel endpoint correction at the moving square cutoff.

For k>=3 define the strict wheel

    P_<k = product_(p<k) p.

Then

    #{1<=r<=2k : gcd(k^2+r,P_<k)=1}
      = pi((k+1)^2)-pi(k^2)
        + 1_{k and k+2 are both prime}.

If k is composite, the strict wheel equals the full wheel P_k because k is not
a prime modulus.  If k is an odd prime, the only interior multiples of k are

    k(k+1) = k^2+k,
    k(k+2) = k^2+2k.

The first is already divisible by 2<k.  The second is coprime to P_<k exactly
when k+2 is prime.  Every other composite state has a least prime factor <k.

Thus inserting the new prime modulus at a prime cutoff removes at most one
strict-wheel survivor, the right-end twin semiprime k(k+2).  The self-cutoff
prime itself is not where the generic square-interval parity difficulty lives.
"""

from __future__ import annotations

from math import gcd

from .legendre import direct_square_interval_prime_count, is_prime, primes_up_to


def strict_prime_wheel(k: int) -> int:
    """Return the product of all primes strictly below k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 0:
        raise ValueError("k must be a nonnegative integer")
    wheel = 1
    for p in primes_up_to(k - 1):
        wheel *= p
    return wheel


def strict_wheel_square_survivors(k: int) -> dict[str, object]:
    """Evaluate the strict-wheel identity and its endpoint correction."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    wheel = strict_prime_wheel(k)
    offsets = tuple(
        r for r in range(1, 2 * k + 1) if gcd(k * k + r, wheel) == 1
    )
    prime_count = direct_square_interval_prime_count(k)
    endpoint_correction = int(is_prime(k) and is_prime(k + 2))
    if len(offsets) != prime_count + endpoint_correction:
        raise AssertionError("strict-wheel endpoint identity failed")

    endpoint = 2 * k
    if endpoint_correction:
        if endpoint not in offsets:
            raise AssertionError("twin endpoint correction is missing")
        if k * k + endpoint != k * (k + 2):
            raise AssertionError("twin endpoint factorization failed")

    nonprime_survivors = tuple(
        r for r in offsets if not is_prime(k * k + r)
    )
    expected_nonprime = (endpoint,) if endpoint_correction else ()
    if nonprime_survivors != expected_nonprime:
        raise AssertionError("strict wheel has an unexpected composite survivor")

    return {
        "k": k,
        "strict_wheel": wheel,
        "strict_survivor_offsets": offsets,
        "strict_survivor_count": len(offsets),
        "prime_count": prime_count,
        "twin_endpoint_correction": endpoint_correction,
        "composite_strict_survivor_offsets": nonprime_survivors,
        "strict_wheel_identity_exact": True,
    }
