"""Basin-level support aggregation for the Legendre pressure test.

The functions here transpose large-divisor hits into unique square-basin states
and half-scale cofactors.  They are exact finite tools, not a proof of
Legendre's conjecture.
"""

from __future__ import annotations

from itertools import combinations

from .alexander_descent import squarefree_product, square_basin_half_scale_bound
from .cutoff_pairing import distinct_prime_factors
from .four_support import four_support_square_tail
from .legendre import primes_up_to


def transverse_primes(k: int) -> list[int]:
    """Return primes p<=k that do not divide the centered anchor k(k+1)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    anchor = k * (k + 1)
    return [p for p in primes_up_to(k) if anchor % p != 0]


def unique_large_modulus_hit(k: int, modulus: int) -> dict[str, int] | None:
    """Return the unique square-basin multiple of a modulus >2k, if it exists.

    Center the basin at M=k(k+1):

        I_k = M + {1-k,...,k}.

    For a=M mod modulus and modulus>2k, at most one representative of -a can
    lie in this centered window.  The exact hit criterion is

        a<k  or  a>=modulus-k.

    The returned cofactor automatically lies at most floor((k+1)/2).
    """
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

    n = center + offset
    if not (k * k < n < (k + 1) * (k + 1)):
        raise AssertionError("centered hit escaped the square basin")
    if n % modulus != 0:
        raise AssertionError("constructed hit is not divisible by modulus")
    cofactor = n // modulus
    half_scale = square_basin_half_scale_bound(k)
    if cofactor > half_scale:
        raise AssertionError("large-modulus hit violated half-scale descent")
    return {
        "residue": residue,
        "offset": offset,
        "state": n,
        "cofactor": cofactor,
        "half_scale": half_scale,
    }


def exact_transverse_support_hit(k: int, primes: list[int]) -> dict[str, object] | None:
    """Return the unique state whose full transverse support is exactly primes.

    The support entries must be distinct transverse primes <=k and their
    square-free product must exceed 2k.  A unique modulus hit is accepted only
    if every prime factor of its half-scale cofactor already belongs to the
    support.  That condition is equivalent to saying that the hit introduces no
    additional transverse small-prime factor.
    """
    if len(primes) != len(set(primes)) or not primes:
        raise ValueError("primes must be a nonempty distinct support")
    support = sorted(primes)
    allowed = set(transverse_primes(k))
    if any(p not in allowed for p in support):
        raise ValueError("every support prime must be transverse and at most k")
    product = squarefree_product(support)
    if product <= 2 * k:
        raise ValueError("support product must exceed 2k")

    hit = unique_large_modulus_hit(k, product)
    if hit is None:
        return None
    cofactor = int(hit["cofactor"])
    extra = [p for p in distinct_prime_factors(cofactor) if p not in support]
    if extra:
        return None
    return {
        **hit,
        "support": support,
        "support_product": product,
        "cofactor_prime_factors": distinct_prime_factors(cofactor),
    }


def four_support_basin_mass(k: int) -> dict[str, object]:
    """Aggregate the large Mobius tail of exact four-transverse-support states.

    This does not scan basin states.  It enumerates four-prime support sets.
    Each product G>2k has at most one basin hit; the centered carry determines
    that hit, the half-scale cofactor test decides whether the support is exact,
    and ``four_support_square_tail`` supplies its graph-reduced tail.
    """
    supports = transverse_primes(k)
    contributions: list[dict[str, object]] = []
    total = 0
    for support_tuple in combinations(supports, 4):
        support = list(support_tuple)
        product = squarefree_product(support)
        if product <= 2 * k:
            continue
        hit = exact_transverse_support_hit(k, support)
        if hit is None:
            continue
        state = int(hit["state"])
        graph = four_support_square_tail(k, state, support)
        contribution = int(graph["tail"])
        total += contribution
        contributions.append(
            {
                "support": support,
                "support_product": product,
                "state": state,
                "cofactor": hit["cofactor"],
                "dual_threshold": graph["dual_threshold"],
                "negative_rank": graph["negative_rank"],
                "positive_cycle_rank": graph["positive_cycle_rank"],
                "tail": contribution,
            }
        )
    return {
        "k": k,
        "total_four_support_large_tail": total,
        "contributions": contributions,
    }
