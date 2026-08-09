"""Exact CRT/Mobius evaluation of the P017 mirror-incidence first moment.

The formulas here do not inspect primality inside the consecutive-square basin.
They use only primes <= k, the anchor k(k+1), square-free inclusion-exclusion,
modular inverses, and floor-division counts of two residue channels per
transverse prime.
"""

from __future__ import annotations

from .legendre import primes_up_to, squarefree_divisors_with_mu


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _anchor_primes(k: int) -> list[int]:
    _require_k(k)
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p == 0]


def residue_class_count(limit: int, modulus: int, residue: int) -> int:
    """Count 1<=r<=limit with r=residue mod modulus for 1<=residue<modulus."""
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a non-negative integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be an integer >= 2")
    if isinstance(residue, bool) or not isinstance(residue, int) or not (1 <= residue < modulus):
        raise ValueError("residue must satisfy 1 <= residue < modulus")
    if residue > limit:
        return 0
    return 1 + (limit - residue) // modulus


def surviving_radius_count_formula(k: int) -> int:
    """L049 formula for |S_k| by Mobius inclusion-exclusion over anchor primes."""
    _require_k(k)
    limit = k - 1
    return sum(
        mu * (limit // a)
        for a, mu in squarefree_divisors_with_mu(_anchor_primes(k))
    )


def transverse_prime_incidence_formula(k: int, prime: int) -> int:
    """L049 formula for N_p(k), the surviving mirror incidences of one transverse p."""
    _require_k(k)
    if isinstance(prime, bool) or not isinstance(prime, int):
        raise ValueError("prime must be an integer")
    if prime not in primes_up_to(k):
        raise ValueError("prime must be prime and <= k")
    center = k * (k + 1)
    if center % prime == 0:
        raise ValueError("prime must be transverse to k(k+1)")

    limit = k - 1
    total = 0
    for a, mu in squarefree_divisors_with_mu(_anchor_primes(k)):
        inverse = pow(a, -1, prime)
        plus_t = (center * inverse) % prime
        minus_t = (-center * inverse) % prime
        if plus_t == 0 or minus_t == 0:
            raise AssertionError("transverse mirror residue unexpectedly vanished")
        modulus = a * prime
        plus_residue = a * plus_t
        minus_residue = a * minus_t
        if not (1 <= plus_residue < modulus and 1 <= minus_residue < modulus):
            raise AssertionError("CRT representative escaped canonical positive range")
        total += mu * (
            residue_class_count(limit, modulus, plus_residue)
            + residue_class_count(limit, modulus, minus_residue)
        )
    if total < 0:
        raise AssertionError("incidence count cannot be negative")
    return total


def mirror_incidence_formula(k: int) -> dict[str, object]:
    """Evaluate L049 and the L050 sufficient prime-existence certificate."""
    _require_k(k)
    center = k * (k + 1)
    surviving = surviving_radius_count_formula(k)
    per_prime: dict[int, int] = {}
    for p in primes_up_to(k):
        if center % p == 0:
            continue
        count = transverse_prime_incidence_formula(k, p)
        if count:
            per_prime[p] = count
    incidence = sum(per_prime.values())
    threshold = 2 * surviving
    return {
        "k": k,
        "center": center,
        "surviving_radius_count": surviving,
        "per_prime_incidence": per_prime,
        "incidence": incidence,
        "hypothetical_failure_minimum": threshold,
        "prime_certificate": incidence < threshold,
        "slack": threshold - incidence,
    }
