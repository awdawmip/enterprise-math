"""Canonical Prime-BRC shadow depth for anchor-surviving composite endpoints.

For an anchor-surviving mirror endpoint n=M+-r let p=spf(n), q=n/p.  Then
q>k.  Hence q has at most two strict square-basin hits.

For k>=10, if q has two hits, the canonical state is automatically a high
semiprime p*q with k/2<p<=k<q<2k.  The other q-hit has multiplier p+-1,
is even, and therefore has least factor 2.  Its canonical cofactor exceeds
2k, so it has a unique basin hit.  Thus the canonical cofactor-shadow graph
has depth at most one: no recursive shadow tree and no shadow cycle are needed
for this interface.
"""

from __future__ import annotations

from math import gcd

from .legendre import square_carry
from .prime_brc_phase import square_basin_frame, square_midpoint_defect
from .prime_brc_silent_core import _is_prime, least_prime_factor


def _strict_multiples(k: int, divisor: int) -> tuple[int, ...]:
    frame = square_basin_frame(k)
    L = int(frame["lower"])
    U = int(frame["upper"])
    first = (L // divisor + 1) * divisor
    return tuple(range(first, U, divisor))


def canonical_cofactor_shadow(k: int, radius: int, side: int) -> dict[str, object]:
    """Classify the canonical cofactor q=n/spf(n) as singleton or paired-shadow.

    Preconditions: k>=10, 1<=r<k, gcd(r,M)=1, n=M+-r composite.
    """
    if k < 10:
        raise ValueError("requires k>=10")
    frame = square_basin_frame(k)
    M = int(frame["center"])
    if not 1 <= radius < k or gcd(radius, M) != 1:
        raise ValueError("require an anchor-surviving mirror radius")
    if side not in (-1, 1):
        raise ValueError("side must be -1 or +1")
    n = M + side * radius
    p = least_prime_factor(n)
    if p == n:
        raise ValueError("endpoint is prime")
    q = n // p
    if q <= k:
        raise AssertionError("canonical complementary cofactor failed q>k")
    if gcd(q, M) != 1:
        raise AssertionError("anchor-surviving endpoint acquired anchor cofactor")

    hits = _strict_multiples(k, q)
    if n not in hits or len(hits) not in (1, 2):
        raise AssertionError("large canonical cofactor must have one or two basin hits")
    kappa_q = square_carry(k, q)
    chi_q = square_midpoint_defect(k, q)
    if kappa_q != len(hits):
        raise AssertionError("q>k carry amount disagrees with strict hit count")

    if len(hits) == 1:
        if chi_q not in (-1, 1):
            raise AssertionError("singleton large cofactor lost directional polarity")
        return {
            "k": k,
            "radius": radius,
            "side": side,
            "n": n,
            "p": p,
            "q": q,
            "q_hit_count": 1,
            "q_kappa": kappa_q,
            "q_chi": chi_q,
            "shadow": None,
            "shadow_depth": 0,
            "classification": "CANONICAL_SINGLETON_COFACTOR",
        }

    # Two q hits have consecutive multipliers because q>k and total basin
    # length is 2k.  Since n's multiplier p is its least prime factor and the
    # state is anchor-surviving, p is an odd prime and the other multiplier is
    # p+-1, hence even.
    if chi_q != 0 or kappa_q != 2:
        raise AssertionError("double-hit q failed (kappa,chi)=(2,0)")
    other = hits[0] if hits[1] == n else hits[1]
    if other == n:
        raise AssertionError("failed to locate distinct q-shadow")
    m = other // q
    if abs(m - p) != 1:
        raise AssertionError("double-hit q multipliers are not consecutive")
    if not (2 * p > k and p <= k):
        raise AssertionError("canonical double-hit multiplier failed p>k/2")
    if not (k < q <= 2 * k - 1):
        raise AssertionError("double-hit cofactor failed k<q<=2k-1")
    if not _is_prime(q):
        # q is p-rough by least-factor provenance.  But q<p^2 because
        # q<=2k-1<p^2 for k>=10 and p>k/2, so composite q is impossible.
        raise AssertionError("canonical double-hit cofactor is not prime")
    if m % 2:
        raise AssertionError("shadow multiplier adjacent to odd p is not even")
    if least_prime_factor(other) != 2:
        raise AssertionError("even shadow failed least factor 2")
    q_shadow = other // 2
    if q_shadow <= 2 * k:
        raise AssertionError("shadow canonical cofactor failed q_shadow>2k")
    shadow_hits = _strict_multiples(k, q_shadow)
    if shadow_hits != (other,):
        raise AssertionError("shadow canonical cofactor is not singleton")

    return {
        "k": k,
        "radius": radius,
        "side": side,
        "n": n,
        "p": p,
        "q": q,
        "q_hit_count": 2,
        "q_kappa": 2,
        "q_chi": 0,
        "shadow": other,
        "shadow_multiplier": m,
        "shadow_least_factor": 2,
        "shadow_canonical_cofactor": q_shadow,
        "shadow_canonical_hit_count": 1,
        "shadow_depth": 1,
        "classification": "CANONICAL_PAIRED_SEMIPRIME_ONE_SHADOW_THEN_SINGLETON",
    }


def canonical_shadow_depth_bound(k: int) -> dict[str, object]:
    """Exhaustively replay all anchor-surviving composite mirror endpoints."""
    if k < 10:
        raise ValueError("requires k>=10")
    frame = square_basin_frame(k)
    M = int(frame["center"])
    records = []
    max_depth = 0
    paired = 0
    for r in range(1, k):
        if gcd(r, M) != 1:
            continue
        for side in (-1, 1):
            n = M + side * r
            if least_prime_factor(n) == n:
                continue
            data = canonical_cofactor_shadow(k, r, side)
            depth = int(data["shadow_depth"])
            max_depth = max(max_depth, depth)
            paired += int(depth == 1)
            records.append(data)
    if max_depth > 1:
        raise AssertionError("canonical shadow graph exceeded depth one")
    return {
        "k": k,
        "composite_records": tuple(records),
        "paired_shadow_count": paired,
        "max_shadow_depth": max_depth,
        "status": "EXACT_DEPTH_ONE_REPLAY_NOT_PRIME_EXISTENCE",
    }
