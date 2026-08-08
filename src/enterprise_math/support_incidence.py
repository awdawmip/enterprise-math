"""Large transverse-support incidence tools for the Legendre pressure test.

These functions isolate two exact facts for a square basin centered at M=k(k+1):

1. a transverse support product G>2k can hit the 2k-state basin at most once;
2. among anchor-surviving hits, exact transverse support P is equivalent to the
   remaining cofactor being P-smooth.

The anchor-survival qualifier is essential: a raw hit may have the requested
transverse support while also carrying an anchor-prime factor.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import anchor_product, primes_up_to


def _validate_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _validated_support(k: int, support: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    _validate_k(k)
    values = tuple(sorted(support))
    if not values or len(values) != len(set(values)):
        raise ValueError("support must contain distinct primes")
    prime_set = set(primes_up_to(k))
    center = k * (k + 1)
    for p in values:
        if p not in prime_set:
            raise ValueError("support entries must be primes <= k")
        if center % p == 0:
            raise ValueError("support primes must be transverse to k(k+1)")
    return values


def transverse_prime_support(k: int, n: int) -> list[int]:
    """Return the distinct transverse prime divisors p<=k of n."""
    _validate_k(k)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p != 0 and n % p == 0]


def support_product(k: int, support: list[int] | tuple[int, ...]) -> int:
    """Return the square-free product of a validated transverse support."""
    return prod(_validated_support(k, support))


def support_unique_basin_hit(
    k: int, support: list[int] | tuple[int, ...]
) -> dict[str, object] | None:
    """Return the unique square-basin multiple of the support product, if it exists.

    The theorem scope requires G=prod(support)>2k.  Writing M=k(k+1) and
    a=M mod G, the unique admissible centered offset is

        -a        when a<k,
        G-a       when a>=G-k,

    and otherwise no basin state is divisible by G.
    """
    values = _validated_support(k, support)
    G = prod(values)
    if G <= 2 * k:
        raise ValueError("support product must satisfy G > 2k")

    center = k * (k + 1)
    residue = center % G
    if residue < k:
        offset = -residue
    elif residue >= G - k:
        offset = G - residue
    else:
        return None

    state = center + offset
    if not (k * k < state < (k + 1) * (k + 1)):
        raise AssertionError("residue criterion produced a state outside the basin")
    if state % G != 0:
        raise AssertionError("residue criterion produced a nonmultiple")

    cofactor = state // G
    if cofactor > (k + 1) // 2:
        raise AssertionError("large-support cofactor escaped the half-scale bound")

    return {
        "k": k,
        "center": center,
        "support": list(values),
        "support_product": G,
        "residue": residue,
        "offset": offset,
        "state": state,
        "cofactor": cofactor,
    }


def anchor_surviving_exact_support_hit(
    k: int, support: list[int] | tuple[int, ...]
) -> dict[str, object] | None:
    """Return the unique anchor-surviving hit with exact transverse support P.

    For G>2k, the raw support-product hit is unique when it exists.  Its cofactor
    h is at most floor((k+1)/2), hence every prime factor of h is <=k.  Among
    anchor-surviving states, the transverse support is exactly P iff every prime
    factor of h already belongs to P (equivalently, h is P-smooth).
    """
    values = _validated_support(k, support)
    raw = support_unique_basin_hit(k, values)
    if raw is None:
        return None

    cofactor = int(raw["cofactor"])
    factor_support = [p for p in primes_up_to(cofactor) if cofactor % p == 0]
    if any(p not in values for p in factor_support):
        return None

    state = int(raw["state"])
    anchor = anchor_product(k)
    if gcd(state, anchor) != 1:
        raise AssertionError("P-smooth transverse hit unexpectedly contains an anchor prime")
    actual = transverse_prime_support(k, state)
    if actual != list(values):
        raise AssertionError("exact transverse support reconstruction failed")

    return {
        **raw,
        "cofactor_prime_support": factor_support,
        "anchor_product": anchor,
        "anchor_surviving": True,
        "exact_transverse_support": actual,
    }
