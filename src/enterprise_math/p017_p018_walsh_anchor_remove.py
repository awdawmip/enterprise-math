"""Exact anchor removal for orientation-Walsh root columns.

Let A be the effective odd anchor product dividing M=k(k+1), let q be an odd
squarefree conductor transverse to M, and let chi_q(r;M) be the signed root
character on odd positive radii:

    sigma_p(r;M)=+1 if p|M-r, -1 if p|M+r, 0 otherwise,
    chi_q=prod_(p|q) sigma_p.

The anchor-surviving column is

    A_q^surv(K,M)=sum_{1<=r<=K, r odd, gcd(r,A)=1} chi_q(r;M).

Mobius-expand gcd(r,A)=1 and write r=a*t for a|A.  Since a is odd and a|M,
for every p|q one has gcd(a,p)=1 and

    p|M +/- a*t  iff  p|M/a +/- t.

Therefore

    A_q^surv(K,M)
      = sum_(a|A) mu(a) A_q^raw(floor(K/a), M/a),

where the raw column has no anchor condition.  Thus any uniform raw mixed-root
estimate loses at most the subpolynomial anchor divisor multiplicity
2^omega(A); the anchor does not need to be entangled with the spectral root
problem.

After normalizing t by (M/a)^(-1) mod q the root equation is always the fixed
u^2=1 mod q.  The moving square-basin center appears only as a frequency
multiplier in Fourier space, not as a growing quadratic discriminant.

This is an exact reduction, not a root-discrepancy estimate and not a Legendre
proof.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, prod

from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _squarefree_mu(value: int) -> int:
    if value < 1 or value % 2 == 0:
        raise ValueError("value must be a positive odd squarefree integer")
    remaining = value
    omega = 0
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            omega += 1
            if remaining % p == 0:
                raise ValueError("value must be squarefree")
        p += 2
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def raw_orientation_sigma(center: int, radius: int, prime: int) -> int:
    lower = (center - radius) % prime == 0
    upper = (center + radius) % prime == 0
    if lower and upper:
        raise ValueError("prime must be transverse to center")
    return 1 if lower else -1 if upper else 0


def raw_signed_root_column(limit: int, center: int, conductor_primes: tuple[int, ...]) -> int:
    """Return the unanchored positive-odd signed root column."""
    normalized = tuple(sorted(int(p) for p in conductor_primes))
    if len(set(normalized)) != len(normalized):
        raise ValueError("conductor primes must be distinct")
    if any(p < 3 or p % 2 == 0 or center % p == 0 for p in normalized):
        raise ValueError("conductor primes must be odd and transverse to center")
    total = 0
    for radius in range(1, limit + 1, 2):
        value = 1
        for p in normalized:
            sigma = raw_orientation_sigma(center, radius, p)
            if sigma == 0:
                value = 0
                break
            value *= sigma
        total += value
    return total


def anchor_mobius_rows(k: int) -> tuple[tuple[int, int], ...]:
    """Return squarefree divisors a|A with mu(a)."""
    primes = tuple(effective_odd_anchor_primes(k))
    rows: list[tuple[int, int]] = []
    for size in range(len(primes) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(primes, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(rows)


def anchor_removed_root_column(k: int, conductor_primes: tuple[int, ...]) -> dict[str, object]:
    """Verify anchor-surviving signed column equals the Mobius sum of raw rescaled columns."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    K = k - 1
    normalized = tuple(sorted(int(p) for p in conductor_primes))
    if not normalized:
        raise ValueError("conductor_primes must be nonempty")
    if any(M % p == 0 for p in normalized):
        raise ValueError("conductor primes must be transverse to M")

    anchors = tuple(effective_odd_anchor_primes(k))
    A = prod(anchors, start=1)
    direct = 0
    for r in range(1, K + 1, 2):
        if gcd(r, A) != 1:
            continue
        value = 1
        for p in normalized:
            sigma = raw_orientation_sigma(M, r, p)
            if sigma == 0:
                value = 0
                break
            value *= sigma
        direct += value

    mobius_total = 0
    rows: list[dict[str, int]] = []
    for a, mu in anchor_mobius_rows(k):
        if M % a:
            raise AssertionError("anchor divisor does not divide center")
        center = M // a
        limit = K // a
        raw = raw_signed_root_column(limit, center, normalized)
        mobius_total += mu * raw
        rows.append(
            {
                "anchor_divisor": a,
                "anchor_mu": mu,
                "rescaled_limit": limit,
                "rescaled_center": center,
                "raw_signed_column": raw,
                "weighted_term": mu * raw,
            }
        )

    if direct != mobius_total:
        raise AssertionError("anchor removal identity failed")
    return {
        "k": k,
        "center": M,
        "limit": K,
        "effective_anchor_product": A,
        "conductor_primes": normalized,
        "direct_anchor_surviving_column": direct,
        "mobius_rescaled_raw_sum": mobius_total,
        "anchor_removal_identity": True,
        "rows": tuple(rows),
    }
