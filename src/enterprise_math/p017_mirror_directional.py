"""Directional refinement of the P017 mirror aggregate certificate.

MC01-MC06 collapse the lower/upper first moments into J=J_-+J_+.  This
module keeps those two directions separate without introducing a new sieve
layer.  Under hypothetical prime-free behavior, with

    U_- = J_- - |S| = sum_r (a_r-1),
    U_+ = J_+ - |S| = sum_r (b_r-1),
    V   = sum_r (a_r-1)(b_r-1),

one has U_-,U_+,V >= 0 and the sharper product envelope

    V <= U_- * U_+.

The certificate is finite and uses the same CRT/Mobius observables already
present in the mirror annex.
"""

from __future__ import annotations

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_mirror_certificate import residue_class_count, surviving_radius_count_formula
from .p017_mirror_cross import cross_side_incidence_formula


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _anchor_primes(k: int) -> list[int]:
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p == 0]


def directional_prime_incidence_formula(k: int, prime: int) -> dict[str, int]:
    """Split the MC01 incidence of one transverse prime into lower/upper sides.

    `lower` counts surviving radii with p | M-r.
    `upper` counts surviving radii with p | M+r.
    """
    _require_k(k)
    primes = set(primes_up_to(k))
    if prime not in primes:
        raise ValueError("prime must be prime and <= k")

    center = k * (k + 1)
    if center % prime == 0:
        raise ValueError("prime must be transverse to k(k+1)")

    limit = k - 1
    lower = 0
    upper = 0
    for a, mu in squarefree_divisors_with_mu(_anchor_primes(k)):
        inverse = pow(a, -1, prime)
        lower_t = (center * inverse) % prime
        upper_t = (-center * inverse) % prime
        if lower_t == 0 or upper_t == 0:
            raise AssertionError("transverse mirror residue unexpectedly vanished")
        modulus = a * prime
        lower += mu * residue_class_count(limit, modulus, a * lower_t)
        upper += mu * residue_class_count(limit, modulus, a * upper_t)

    if lower < 0 or upper < 0:
        raise AssertionError("directional incidence count cannot be negative")
    return {"prime": prime, "lower": lower, "upper": upper}


def directional_first_moments(k: int) -> dict[str, object]:
    """Return J_-, J_+ and their per-prime exact CRT/Mobius decomposition."""
    _require_k(k)
    center = k * (k + 1)
    lower = 0
    upper = 0
    per_prime: dict[int, tuple[int, int]] = {}
    for p in primes_up_to(k):
        if center % p == 0:
            continue
        data = directional_prime_incidence_formula(k, p)
        lo = data["lower"]
        hi = data["upper"]
        if lo or hi:
            per_prime[p] = (lo, hi)
        lower += lo
        upper += hi

    return {
        "k": k,
        "lower_incidence": lower,
        "upper_incidence": upper,
        "total_incidence": lower + upper,
        "per_prime": per_prime,
    }


def directional_mirror_certificate(k: int) -> dict[str, object]:
    """Evaluate the directional MC07 necessary conditions for prime-free behavior."""
    _require_k(k)
    first = directional_first_moments(k)
    cross = cross_side_incidence_formula(k)
    surviving = surviving_radius_count_formula(k)

    lower = int(first["lower_incidence"])
    upper = int(first["upper_incidence"])
    total = lower + upper
    cross_incidence = int(cross["cross_incidence"])

    if total != int(cross["first_incidence"]):
        raise AssertionError("directional first moments do not sum to canonical J")

    lower_slack = lower - surviving
    upper_slack = upper - surviving
    simultaneous_excess = cross_incidence - total + surviving
    if simultaneous_excess != int(cross["simultaneous_excess_slack"]):
        raise AssertionError("directional V disagrees with canonical MC03 value")

    lower_certificate = lower_slack < 0
    upper_certificate = upper_slack < 0
    negative_v_certificate = simultaneous_excess < 0
    product_violation = (
        lower_slack >= 0
        and upper_slack >= 0
        and simultaneous_excess > lower_slack * upper_slack
    )

    certificate = (
        lower_certificate
        or upper_certificate
        or negative_v_certificate
        or product_violation
    )

    return {
        "k": k,
        "surviving_radius_count": surviving,
        "lower_incidence": lower,
        "upper_incidence": upper,
        "total_incidence": total,
        "cross_incidence": cross_incidence,
        "lower_slack": lower_slack,
        "upper_slack": upper_slack,
        "simultaneous_excess_slack": simultaneous_excess,
        "product_capacity": (
            lower_slack * upper_slack
            if lower_slack >= 0 and upper_slack >= 0
            else None
        ),
        "lower_channel_certificate": lower_certificate,
        "upper_channel_certificate": upper_certificate,
        "negative_v_certificate": negative_v_certificate,
        "product_violation_certificate": product_violation,
        "directional_certificate": certificate,
        "mc06_certificate": bool(cross["three_channel_certificate"]),
    }
