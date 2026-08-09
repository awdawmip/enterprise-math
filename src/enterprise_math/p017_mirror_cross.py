"""Cross-side mirror incidence and factorized aggregate certificates for P017.

L051 evaluates ordered lower/upper transverse-prime incidences by exact CRT.
L052 factors prime-free behavior into U=J-2|S| and V=E-J+|S|. L054 adds the
aggregate quadratic bound 4V<=U^2. L055 certifies a basin prime whenever any
of these necessary prime-free constraints is violated.
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
    """L051 formula for N_{p->q}(k) with p on M-r and q on M+r."""
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
    """Evaluate L051 and all L052-L055 aggregate slacks/certificates."""
    _require_k(k)
    trans = _transverse_primes(k)
    per_pair: dict[tuple[int, int], int] = {}
    cross_incidence = 0
    for p in trans:
        for q in trans:
            if p == q:
                continue
            count = ordered_cross_incidence_formula(k, p, q)
            if count:
                per_pair[(p, q)] = count
                cross_incidence += count

    first = mirror_incidence_formula(k)
    surviving = int(first["surviving_radius_count"])
    first_incidence = int(first["incidence"])
    first_slack = first_incidence - 2 * surviving
    simultaneous_excess_slack = cross_incidence - first_incidence + surviving
    raw_cross_slack = cross_incidence - surviving

    if raw_cross_slack != first_slack + simultaneous_excess_slack:
        raise AssertionError("factorization E-|S| = U+V failed")

    quadratic_violation = (
        first_slack >= 0
        and simultaneous_excess_slack >= 0
        and 4 * simultaneous_excess_slack > first_slack * first_slack
    )
    first_certificate = first_slack < 0
    simultaneous_certificate = simultaneous_excess_slack < 0

    return {
        "k": k,
        "surviving_radius_count": surviving,
        "first_incidence": first_incidence,
        "cross_incidence": cross_incidence,
        "per_ordered_pair": per_pair,
        "first_slack": first_slack,
        "simultaneous_excess_slack": simultaneous_excess_slack,
        "raw_cross_slack": raw_cross_slack,
        "first_channel_certificate": first_certificate,
        "simultaneous_excess_certificate": simultaneous_certificate,
        "quadratic_violation_certificate": quadratic_violation,
        "raw_cross_certificate": raw_cross_slack < 0,
        "three_channel_certificate": (
            first_certificate or simultaneous_certificate or quadratic_violation
        ),
    }


def aggregate_mirror_certificate(k: int) -> dict[str, object]:
    """Compact L055 three-channel certificate output."""
    data = cross_side_incidence_formula(k)
    return {
        "k": k,
        "surviving_radius_count": data["surviving_radius_count"],
        "first_incidence": data["first_incidence"],
        "cross_incidence": data["cross_incidence"],
        "first_slack": data["first_slack"],
        "simultaneous_excess_slack": data["simultaneous_excess_slack"],
        "raw_cross_slack": data["raw_cross_slack"],
        "first_channel_certificate": data["first_channel_certificate"],
        "simultaneous_excess_certificate": data["simultaneous_excess_certificate"],
        "quadratic_violation_certificate": data["quadratic_violation_certificate"],
        "three_channel_certificate": data["three_channel_certificate"],
    }
