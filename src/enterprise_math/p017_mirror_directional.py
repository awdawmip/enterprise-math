"""Directional and finite-precision refinements of the P017 mirror certificate.

MC07 retains the two directions of the first moment instead of collapsing them
into J=J_-+J_+.  MC08 then treats the surviving-radius coordinate itself as a
finite precision axis: level m partitions 1<=r<k into 2^m nested blocks and
checks the same MC07 necessary inequalities inside each block.

This is deliberately not advertised as a Legendre proof.  At terminal precision
(2^m >= k-1) every nonempty block is a singleton, so MC08 becomes exact small-
prime detection.  The open problem is to bound the precision required for a
certificate strictly below that terminal resolution.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_mirror_certificate import residue_class_count, surviving_radius_count_formula
from .p017_mirror_cross import cross_side_incidence_formula


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _require_level(level: int) -> None:
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")


def _anchor_primes(k: int) -> list[int]:
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p == 0]


def _transverse_primes(k: int) -> list[int]:
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p != 0]


def directional_prime_incidence_formula(k: int, prime: int) -> dict[str, int]:
    """Split the MC01 incidence of one transverse prime into lower/upper sides."""
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


def _directional_certificate_from_moments(
    surviving: int,
    lower: int,
    upper: int,
    cross_incidence: int,
) -> dict[str, int | bool | None]:
    """Evaluate the MC07 inequalities from one finite set of radii."""
    lower_slack = lower - surviving
    upper_slack = upper - surviving
    simultaneous_excess = cross_incidence - lower - upper + surviving

    lower_certificate = lower_slack < 0
    upper_certificate = upper_slack < 0
    negative_v_certificate = simultaneous_excess < 0
    product_violation = (
        lower_slack >= 0
        and upper_slack >= 0
        and simultaneous_excess > lower_slack * upper_slack
    )

    return {
        "surviving_radius_count": surviving,
        "lower_incidence": lower,
        "upper_incidence": upper,
        "total_incidence": lower + upper,
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
        "directional_certificate": (
            lower_certificate
            or upper_certificate
            or negative_v_certificate
            or product_violation
        ),
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

    result = _directional_certificate_from_moments(
        surviving,
        lower,
        upper,
        cross_incidence,
    )
    if result["simultaneous_excess_slack"] != int(cross["simultaneous_excess_slack"]):
        raise AssertionError("directional V disagrees with canonical MC03 value")

    return {
        "k": k,
        **result,
        "mc06_certificate": bool(cross["three_channel_certificate"]),
    }


def dyadic_radius_block_index(k: int, radius: int, level: int) -> int:
    """Return the nested dyadic precision cell containing one radius.

    Level m has 2^m blocks across the integer coordinate 1<=r<k.  The indexing
    is nested: the level-(m+1) block maps back to its level-m parent by integer
    division by two.
    """
    _require_k(k)
    _require_level(level)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    bins = 1 << level
    return ((radius - 1) * bins) // (k - 1)


def terminal_radius_precision_level(k: int) -> int:
    """Smallest dyadic level whose blocks contain at most one integer radius."""
    _require_k(k)
    return (k - 2).bit_length()


def _surviving_radius_support_counts(k: int) -> list[tuple[int, int, int]]:
    """Return (r,a_r,b_r) without factoring mirror states.

    The implementation marks the two transverse residue classes for each prime.
    It therefore computes exactly the support-incidence observables used by the
    mirror certificates, rather than calling an integer-factorization routine.
    """
    _require_k(k)
    center = k * (k + 1)
    anchor_product = prod(_anchor_primes(k))
    lower = [0] * k
    upper = [0] * k

    for p in _transverse_primes(k):
        lower_residue = center % p
        upper_residue = (-center) % p
        if lower_residue == 0 or upper_residue == 0:
            raise AssertionError("transverse residue unexpectedly vanished")
        for r in range(lower_residue, k, p):
            if r >= 1:
                lower[r] += 1
        for r in range(upper_residue, k, p):
            if r >= 1:
                upper[r] += 1

    return [
        (r, lower[r], upper[r])
        for r in range(1, k)
        if gcd(r, anchor_product) == 1
    ]


def directional_precision_blocks(k: int, level: int) -> dict[str, object]:
    """Evaluate MC08 local directional moments at one radius precision level."""
    _require_k(k)
    _require_level(level)
    bins = 1 << level
    blocks = [
        {"size": 0, "lower": 0, "upper": 0, "cross": 0}
        for _ in range(bins)
    ]

    for r, a, b in _surviving_radius_support_counts(k):
        index = dyadic_radius_block_index(k, r, level)
        block = blocks[index]
        block["size"] += 1
        block["lower"] += a
        block["upper"] += b
        block["cross"] += a * b

    evaluated: list[dict[str, object]] = []
    certificate_blocks: list[int] = []
    for index, block in enumerate(blocks):
        size = block["size"]
        if size == 0:
            continue
        result = _directional_certificate_from_moments(
            size,
            block["lower"],
            block["upper"],
            block["cross"],
        )
        item = {"index": index, **result}
        evaluated.append(item)
        if result["directional_certificate"]:
            certificate_blocks.append(index)

    return {
        "k": k,
        "level": level,
        "bin_count": bins,
        "terminal_level": terminal_radius_precision_level(k),
        "blocks": evaluated,
        "certificate_blocks": tuple(certificate_blocks),
        "precision_certificate": bool(certificate_blocks),
    }


def minimum_directional_precision_level(k: int, max_level: int | None = None) -> int | None:
    """Return the first dyadic MC08 level producing a certificate, if searched.

    This is a diagnostic search, not a theorem that a certificate must exist.  By
    default the search stops at singleton precision.  Claiming existence of a
    certificate by that point for every k would be equivalent to proving the
    target prime-existence statement, so callers must not treat the return value
    as an a priori guarantee.
    """
    _require_k(k)
    if max_level is None:
        max_level = terminal_radius_precision_level(k)
    _require_level(max_level)
    for level in range(max_level + 1):
        if directional_precision_blocks(k, level)["precision_certificate"]:
            return level
    return None
