"""Square-diagonal Generation 3: exact parity endpoint at the minimal P2 cutoff.

Let

    U_k = k^2+2k,
    z2 = floor(U_k^(1/3)),
    I_k = {k^2+1,...,U_k}.

Every z2-rough state has at most two prime factors counted with multiplicity.
No composite rough state can be p^2, because there is no perfect square
strictly between k^2 and (k+1)^2.  Hence the rough set is a disjoint union of

    primes             (mu=-1),
    squarefree pq       (mu=+1).

If

    R_2(k) = # {n in I_k : gcd(n,P_z2)=1}
    M_2(k) = sum_{same n} mu(n),

then exactly

    pi((k+1)^2)-pi(k^2) = (R_2(k)-M_2(k))/2,
    H_z2(k)              = (R_2(k)+M_2(k))/2.

Thus a Legendre failure is equivalent to complete positive Möbius polarization
on the minimal-P2 rough set:

    M_2(k) = R_2(k).

This is a parity endpoint, not a proof.  It states precisely which information
is absent from unsigned rough-count control: one must force a negative Möbius
contribution, equivalently a prime state.
"""

from __future__ import annotations

from math import isqrt

from .legendre import direct_square_interval_prime_count, is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
    square_interval_upper,
)


def p2_parity_endpoint(k: int) -> dict[str, object]:
    """Evaluate the exact restricted-Möbius decomposition at z2."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")

    upper = square_interval_upper(k)
    cutoff = int(almost_prime_cutoff(k, 2)["cutoff"])
    offsets = rough_survivor_offsets(k, cutoff)
    small_factor_primes = tuple(p for p in primes_up_to(k) if p > cutoff)

    prime_offsets: list[int] = []
    semiprime_rows: list[tuple[int, int, int, int]] = []
    mobius_sum = 0
    high_prime_incidence = 0

    for r in offsets:
        value = k * k + r
        if is_prime(value):
            prime_offsets.append(r)
            mobius_sum -= 1
            continue

        p = next((p for p in small_factor_primes if value % p == 0), None)
        if p is None:
            raise AssertionError("P2 rough composite lost its least factor above z2")
        q = value // p
        if not is_prime(q):
            raise AssertionError("minimal-P2 rough state exceeded Omega=2")
        if p == q:
            raise AssertionError("perfect square appeared strictly between consecutive squares")
        if not (cutoff < p <= k < q):
            raise AssertionError("P2 rough semiprime left the one-low-one-high factor strip")
        if isqrt(value) ** 2 == value:
            raise AssertionError("squarefree endpoint encountered a square")

        semiprime_rows.append((p, q, value, r))
        mobius_sum += 1
        high_prime_incidence += 1

    rough_count = len(offsets)
    prime_count = len(prime_offsets)
    semiprime_count = len(semiprime_rows)
    if rough_count != prime_count + semiprime_count:
        raise AssertionError("P2 rough partition failed")
    if rough_count - mobius_sum != 2 * prime_count:
        raise AssertionError("restricted Möbius prime identity failed")
    if rough_count + mobius_sum != 2 * semiprime_count:
        raise AssertionError("restricted Möbius semiprime identity failed")
    if prime_count != direct_square_interval_prime_count(k):
        raise AssertionError("P2 parity endpoint lost the direct interval prime count")
    if high_prime_incidence != semiprime_count:
        raise AssertionError("each semiprime should have exactly one divisor in (z2,k]")
    if prime_count != rough_count - high_prime_incidence:
        raise AssertionError("high-prime incidence selector lost the prime count")

    return {
        "k": k,
        "upper": upper,
        "p2_cutoff": cutoff,
        "rough_offsets": offsets,
        "rough_count": rough_count,
        "restricted_mobius_sum": mobius_sum,
        "prime_offsets": tuple(prime_offsets),
        "prime_count": prime_count,
        "semiprime_rows": tuple(sorted(semiprime_rows)),
        "semiprime_count": semiprime_count,
        "high_prime_incidence": high_prime_incidence,
        "prime_from_mobius": (rough_count - mobius_sum) // 2,
        "semiprime_from_mobius": (rough_count + mobius_sum) // 2,
        "complete_positive_polarization": mobius_sum == rough_count,
        "legendre_failure_equivalent": (mobius_sum == rough_count) == (prime_count == 0),
        "status": "P2_PARITY_ENDPOINT",
    }
