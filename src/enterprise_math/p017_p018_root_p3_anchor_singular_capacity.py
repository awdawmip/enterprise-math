"""P017/P018 Generation 3: root-P3 anchor-singular capacity is O(sqrt(k)).

Let

    U = k^2+2k,
    z3 = floor(U^(1/4)),
    M = k(k+1).

Every z3-rough state has no prime factor <=z3.  Therefore an anchor-singular
z3-rough state (gcd(n,M)>1) must be divisible by a prime p>z3 dividing M.

There are at most two such distinct anchor primes in total: at most one can
divide k and at most one can divide k+1.  Indeed, if two distinct primes both
exceed z3 and divide k, their product is at least (z3+1)^2>sqrt(U)>k.  For
k+1, the integer inequality (z3+1)^2>=k+1 holds; equality forces
k+1=(z3+1)^2, so two distinct factors >z3 are still impossible.

For one odd anchor prime p, a z3-rough shell state is odd and the signed
coordinate x=M-n is therefore odd.  The conditions p|M and p|n are equivalent
to p|x.  Parity plus divisibility is one residue class modulo 2p, exactly the
P017 signed-capacity geometry.  Across the signed basin it has at most

    floor((k-1)/p)+1

incidences.

Hence the total number of anchor-singular z3-rough shell states, and in
particular the number of root-P3 triple contaminants among them, is at most

    sum_{p|M, p>z3} (floor((k-1)/p)+1)

and therefore

    <= 2*(floor((k-1)/(z3+1))+1) = O(sqrt(k)).

This is an exact finite capacity theorem.  It does not provide a lower bound
for the total root-P3 rough mass; that analytic input remains separate.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff, rough_survivor_offsets


def _distinct_prime_divisors(value: int) -> tuple[int, ...]:
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    factors: list[int] = []
    for p in primes_up_to(value):
        if remaining % p:
            continue
        factors.append(p)
        while remaining % p == 0:
            remaining //= p
        if remaining == 1:
            break
        if p * p > remaining:
            if remaining > 1:
                factors.append(remaining)
            break
    return tuple(sorted(set(factors)))


def large_anchor_primes_at_p3_root(k: int) -> dict[str, object]:
    """Return the distinct anchor primes above the exact P3 root cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    left = tuple(p for p in _distinct_prime_divisors(k) if p > z3)
    right = tuple(p for p in _distinct_prime_divisors(k + 1) if p > z3)

    if len(left) > 1:
        raise AssertionError("k acquired two distinct prime divisors above z3")
    if len(right) > 1:
        raise AssertionError("k+1 acquired two distinct prime divisors above z3")
    if len(set(left + right)) != len(left) + len(right):
        raise AssertionError("consecutive anchors shared a prime divisor")

    return {
        "k": k,
        "p3_cutoff": z3,
        "large_anchor_primes_dividing_k": left,
        "large_anchor_primes_dividing_k_plus_1": right,
        "large_anchor_primes": tuple(sorted(left + right)),
        "large_anchor_prime_count": len(left) + len(right),
    }


def root_p3_anchor_singular_capacity(k: int) -> dict[str, object]:
    """Certify the signed-capacity bound for anchor-singular root-P3 rough rows."""
    data = large_anchor_primes_at_p3_root(k)
    z3 = int(data["p3_cutoff"])
    anchor_primes = tuple(int(p) for p in data["large_anchor_primes"])

    column_bounds = tuple(
        (p, (k - 1) // p + 1)
        for p in anchor_primes
    )
    capacity = sum(bound for _, bound in column_bounds)
    uniform = 2 * ((k - 1) // (z3 + 1) + 1)
    if capacity > uniform:
        raise AssertionError("exact anchor-prime capacity exceeded the two-column uniform bound")

    # Bounded direct reconstruction is evidence that every singular rough state
    # is covered by one of these columns.  The theorem itself is the arithmetic
    # inclusion plus the signed-capacity bound above.
    center = k * (k + 1)
    direct_singular_offsets: list[int] = []
    for r in rough_survivor_offsets(k, z3):
        state = k * k + r
        if gcd(state, center) == 1:
            continue
        if not any(state % p == 0 for p in anchor_primes):
            raise AssertionError("anchor-singular root-rough row had no large anchor-prime witness")
        direct_singular_offsets.append(r)

    if len(direct_singular_offsets) > capacity:
        raise AssertionError("direct singular root-rough count exceeded signed column capacity")

    return {
        **data,
        "signed_column_bounds": column_bounds,
        "exact_capacity_bound": capacity,
        "uniform_two_column_bound": uniform,
        "direct_anchor_singular_rough_offsets": tuple(direct_singular_offsets),
        "direct_anchor_singular_rough_count": len(direct_singular_offsets),
        "status": "ROOT_P3_ANCHOR_SINGULAR_CAPACITY",
    }
