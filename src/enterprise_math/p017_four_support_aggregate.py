"""Anchor-surviving four-support aggregation for the P017 Legendre pressure test.

Historical L025 described an exact four-transverse-support basin aggregation but
inherited an omitted hypothesis from its historical L024 wording.  Supplement
02 shows that the large transverse Mobius region is evaluated only after the
anchor transform, i.e. over states coprime to the anchor product k(k+1).

This module states that scope explicitly and uses the reconstructed
``p017_four_support_tail`` graph theorem.  It is an exact finite reindexing of
the anchor-surviving large-region contribution; it is not a proof of
Legendre's conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, prod

from .cutoff_pairing import distinct_prime_factors
from .legendre import primes_up_to
from .p017_four_support_tail import (
    four_support_direct_mobius_tail,
    four_support_tail_certificate,
)


def transverse_primes(k: int) -> list[int]:
    """Return primes p<=k that do not divide the centered anchor k(k+1)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    anchor = k * (k + 1)
    return [p for p in primes_up_to(k) if anchor % p != 0]


def unique_large_support_hit(k: int, modulus: int) -> dict[str, int] | None:
    """Return the unique square-basin multiple of ``modulus>2k``, if any."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 2 * k:
        raise ValueError("modulus must be an integer greater than 2k")

    center = k * (k + 1)
    residue = center % modulus
    if residue < k:
        offset = -residue
    elif residue >= modulus - k:
        offset = modulus - residue
    else:
        return None

    state = center + offset
    if not (k * k < state < (k + 1) * (k + 1)):
        raise AssertionError("centered hit escaped the square basin")
    if state % modulus != 0:
        raise AssertionError("constructed hit is not divisible by modulus")

    cofactor = state // modulus
    half_scale = (k + 1) // 2
    if cofactor > half_scale:
        raise AssertionError("large-modulus hit violated the half-scale bound")
    return {
        "residue": residue,
        "offset": offset,
        "state": state,
        "cofactor": cofactor,
        "half_scale": half_scale,
    }


def anchor_surviving_exact_four_support_hit(
    k: int, support: list[int] | tuple[int, ...]
) -> dict[str, object] | None:
    """Return the unique anchor-surviving basin state with exact support P.

    ``support`` must consist of four distinct transverse primes at most k with
    product G>2k.  The common-anchor residue first selects the unique possible
    G-hit.  That hit is retained only if it survives the anchor sieve and its
    half-scale cofactor introduces no transverse prime outside P.

    On an anchor-surviving hit every prime divisor of the half-scale cofactor is
    transverse, so ``PrimeSupp(h) subseteq P`` is then exactly the full-support
    closure condition.  This is the qualifier omitted by historical L024/L025.
    """
    values = tuple(sorted(support))
    if len(values) != 4 or len(set(values)) != 4:
        raise ValueError("support must contain exactly four distinct primes")
    allowed = set(transverse_primes(k))
    if any(p not in allowed for p in values):
        raise ValueError("every support prime must be transverse and at most k")

    support_product = prod(values)
    if support_product <= 2 * k:
        raise ValueError("support product must exceed 2k")

    hit = unique_large_support_hit(k, support_product)
    if hit is None:
        return None

    state = int(hit["state"])
    anchor = k * (k + 1)
    if gcd(state, anchor) != 1:
        return None

    cofactor = int(hit["cofactor"])
    cofactor_factors = distinct_prime_factors(cofactor)
    if any(p not in values for p in cofactor_factors):
        return None

    return {
        **hit,
        "support": values,
        "support_product": support_product,
        "cofactor_prime_factors": tuple(cofactor_factors),
        "anchor_surviving": True,
    }


def four_support_anchor_surviving_mass(k: int) -> dict[str, object]:
    """Aggregate exact four-support large tails by support sets, not basin scan."""
    contributions: list[dict[str, object]] = []
    total = 0
    for support in combinations(transverse_primes(k), 4):
        support_product = prod(support)
        if support_product <= 2 * k:
            continue
        hit = anchor_surviving_exact_four_support_hit(k, support)
        if hit is None:
            continue
        tail_data = four_support_tail_certificate(k, support)
        tail = int(tail_data["tail"])
        total += tail
        contributions.append(
            {
                "support": support,
                "support_product": support_product,
                "state": hit["state"],
                "cofactor": hit["cofactor"],
                "dual_threshold": tail_data["dual_threshold"],
                "negative_rank": tail_data["negative_rank"],
                "positive_cycle_rank": tail_data["positive_cycle_rank"],
                "empty_dual_correction": tail_data["empty_dual_correction"],
                "tail": tail,
            }
        )
    return {
        "k": k,
        "scope": "anchor-surviving exact four-transverse-support large region",
        "total_four_support_large_tail": total,
        "contributions": contributions,
    }


def direct_anchor_surviving_four_support_mass(k: int) -> dict[str, object]:
    """Independently scan basin states and sum the same transformed subfamily.

    This deliberately does not use the support-indexed hit construction.  It is
    a finite regression oracle for the corrected L025 reindexing.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    anchor = k * (k + 1)
    transverse = transverse_primes(k)
    contributions: list[dict[str, object]] = []
    total = 0

    for state in range(k * k + 1, (k + 1) * (k + 1)):
        if gcd(state, anchor) != 1:
            continue
        support = tuple(p for p in transverse if state % p == 0)
        if len(support) != 4:
            continue
        support_product = prod(support)
        tail = (
            four_support_direct_mobius_tail(k, support)
            if support_product > 2 * k
            else 0
        )
        total += tail
        contributions.append(
            {
                "state": state,
                "support": support,
                "support_product": support_product,
                "tail": tail,
            }
        )

    return {
        "k": k,
        "scope": "direct anchor-surviving exact four-transverse-support basin scan",
        "total_four_support_large_tail": total,
        "contributions": contributions,
    }
