"""Second-order cross-side mirror incidence for P017.

L052 evaluates ordered lower/upper transverse-prime incidences by exact CRT
residue classes. L053 uses their sum E_k as a second sufficient prime-existence
certificate, and L054 combines it with the L051 first-moment certificate.
"""

from __future__ import annotations

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_mirror_certificate import mirror_incidence_formula, residue_class_count


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _anchor_primes(k: int) -> list[int]:
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p == 0]


def _transverse_primes(k: int) -> list[int]:
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p != 0]


def ordered_cross_incidence_formula(k: int, lower_prime: int, upper_prime: int) -> int:
    """L052 formula for N_{p->q}(k) with p on M-r and q on M+r."""
    _require_k(k)
    trans = set(_transverse_primes(k))
    if lower_prime not in trans or upper_prime not in trans:
        raise ValueError("both primes must be transverse and <= k")
    if lower_prime == upper_prime:
        raise ValueError("L043 forbids the same transverse prime on both mirror sides")

    p = lower_prime
    q = upper_prime
    center = k * (k + 1)
    limit = k - 1
    total = 0

    for a, mu in squarefree_divisors_with_mu(_anchor_primes(k)):
        cp = (center * pow(a, -1, p)) % p
        cq = (-center * pow(a, -1, q)) % q
        if cp == 0 or cq == 0:
            raise AssertionError("transverse CRT channel unexpectedly has zero residue")

        step = ((cq - cp) * pow(p, -1, q)) % q
        t = cp + p * step
        if not (1 <= t < p * q):
            raise AssertionError("ordered-pair CRT representative escaped canonical range")

        modulus = a * p * q
        residue = a * t
        total += mu * residue_class_count(limit, modulus, residue)

    if total < 0:
        raise AssertionError("ordered cross-side incidence cannot be negative")
    return total


def cross_side_incidence_formula(k: int) -> dict[str, object]:
    """Evaluate L052 and the L053 cross-side prime-existence certificate."""
    _require_k(k)
    trans = _transverse_primes(k)
    per_pair: dict[tuple[int, int], int] = {}
    total = 0
    for p in trans:
        for q in trans:
            if p == q:
                continue
            count = ordered_cross_incidence_formula(k, p, q)
            if count:
                per_pair[(p, q)] = count
                total += count

    first = mirror_incidence_formula(k)
    surviving = int(first["surviving_radius_count"])
    return {
        "k": k,
        "surviving_radius_count": surviving,
        "cross_incidence": total,
        "per_ordered_pair": per_pair,
        "cross_prime_certificate": total < surviving,
        "cross_slack": surviving - total,
    }


def two_moment_certificate(k: int) -> dict[str, object]:
    """L054 combined certificate using either the L051 or L053 moment."""
    first = mirror_incidence_formula(k)
    second = cross_side_incidence_formula(k)
    first_certificate = bool(first["prime_certificate"])
    second_certificate = bool(second["cross_prime_certificate"])
    return {
        "k": k,
        "surviving_radius_count": first["surviving_radius_count"],
        "first_incidence": first["incidence"],
        "cross_incidence": second["cross_incidence"],
        "first_certificate": first_certificate,
        "cross_certificate": second_certificate,
        "combined_certificate": first_certificate or second_certificate,
    }
