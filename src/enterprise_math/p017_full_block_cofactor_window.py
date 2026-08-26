"""Exact cofactor-window form of P017 canonical full-block token incidence.

Let M=k(k+1), let A be an odd transverse full prime-power token block, and put
D=rad(A), p0=min p|D.  Every token state has n=A*q in the open square basin, so

    floor(k^2/A)+1 <= q <= floor(k(k+2)/A).

The remaining token conditions become transparent on q:

* anchor survival:
      gcd(M-Aq,M)=gcd(q,M)=1,
  because gcd(A,M)=1;
* exact selected valuations:
      v_p(n)=v_p(A) for p|D
  iff gcd(q,D)=1;
* p0 is the least transverse small support prime of n iff q has no prime divisor
  below p0 (anchor primes below p0 are already excluded by gcd(q,M)=1).

Hence the exact CG14 incidence is

    I_k^{min,exact}(A)
      = #{ q in W_A(k) :
             gcd(q,M)=1,
             gcd(q,rad(A))=1,
             q is p0-rough },

where

    W_A(k)=[floor(k^2/A)+1, floor(k(k+2)/A)].

The two canonical unpaired composite states at M and M+k are automatically
removed by gcd(q,M)=1 when A is transverse.

This is the quotient-window interpretation of the CG14 Möbius/p-adic formula.
It does not use the separate WIP theorem that distinct same-parity quotient
windows are disjoint; only the exact one-divisor window is needed here.
"""

from __future__ import annotations

from math import gcd, prod

from .cutoff_pairing import distinct_prime_factors
from .p017_cofactor_window import is_p_rough
from .p017_full_block_token_incidence import canonical_full_block_incidence_mobius


def _validated_full_block(k: int, full_block: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if (
        isinstance(full_block, bool)
        or not isinstance(full_block, int)
        or full_block < 3
        or full_block % 2 == 0
    ):
        raise ValueError("full_block must be an odd integer >=3")
    primes = tuple(distinct_prime_factors(full_block))
    if not primes:
        raise ValueError("full_block must contain a prime")
    center = k * (k + 1)
    if any(prime > k or center % prime == 0 for prime in primes):
        raise ValueError("full_block primes must be transverse and <=k")
    return primes


def full_block_cofactor_window(k: int, full_block: int) -> dict[str, int | tuple[int, ...]]:
    """Return the exact integer q-window for n=Aq in the open square basin."""
    primes = _validated_full_block(k, full_block)
    q_min = (k * k) // full_block + 1
    q_max = (k * (k + 2)) // full_block
    return {
        "k": k,
        "full_block": full_block,
        "radical": prod(primes),
        "least_token_prime": primes[0],
        "q_min": q_min,
        "q_max": q_max,
        "raw_window_size": max(0, q_max - q_min + 1),
    }


def canonical_full_block_cofactors(k: int, full_block: int) -> dict[str, object]:
    """Enumerate exact canonical token cofactors and verify the CG14 formula."""
    data = full_block_cofactor_window(k, full_block)
    center = k * (k + 1)
    radical = int(data["radical"])
    least = int(data["least_token_prime"])
    cofactors = tuple(
        q
        for q in range(int(data["q_min"]), int(data["q_max"]) + 1)
        if gcd(q, center) == 1
        and gcd(q, radical) == 1
        and is_p_rough(q, least)
    )

    owner = canonical_full_block_incidence_mobius(k, full_block)
    if len(cofactors) != int(owner["exact_full_block_incidence"]):
        raise AssertionError("cofactor-window count disagrees with CG14 exact incidence")

    signed_points = tuple(sorted(center - full_block * q for q in cofactors))
    if signed_points != tuple(owner["canonical_signed_points"]):
        raise AssertionError("cofactor window and CG14 signed points disagree")
    for point in signed_points:
        if point == 0 or abs(point) > k:
            raise AssertionError("canonical cofactor escaped the mirror/full-basin boundary")

    return {
        **data,
        "canonical_cofactors": cofactors,
        "canonical_signed_points": signed_points,
        "canonical_incidence": len(cofactors),
        "cg14_exact_incidence": int(owner["exact_full_block_incidence"]),
    }
