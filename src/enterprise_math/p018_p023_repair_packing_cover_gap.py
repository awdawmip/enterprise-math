"""Finite certificate for a strict canonical packing-to-cover gap.

At high root order, state bound ``N=490`` and horizon ``h=3``, the prime-hard
semantic target family has:

    maximum divisor-incompatibility packing number = 4,
    minimum divisor-cover number                  = 5.

This module certifies both equalities without relying on an optimizer result.
It is a theorem-discovery/regression artifact for the Lean-side repair packing
hierarchy.

The two sides use deliberately different certificates:

* cover: an explicit 5-type cover and a 7-target lower-bound core;
* packing: an explicit 4-target packing and a 4-class compatibility coloring.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True


def _omega(n: int) -> int:
    x = n
    total = 0
    d = 2
    while d * d <= x:
        while x % d == 0:
            x //= d
            total += 1
        d += 1
    if x > 1:
        total += 1
    return total


def _is_composite(n: int) -> bool:
    return n >= 4 and not _is_prime(n)


def hard_targets_490_h3() -> tuple[int, ...]:
    """High-root prime-hard semantic targets for ``N=490,h=3``."""
    return tuple(n for n in range(4, 491) if _is_composite(n) and _omega(n) > 3)


def candidate_hits(candidate: int, target: int) -> bool:
    return _is_composite(candidate) and target % candidate == 0


def targets_are_divisor_incompatible(a: int, b: int) -> bool:
    """No admissible composite can divide both targets."""
    common = gcd(a, b)
    return common == 1 or _is_prime(common)


COVER_WITNESS = (4, 9, 14, 15, 25)

# A finite subproblem whose cover number is already five.
COVER_LOWER_CORE = (250, 294, 330, 351, 375, 416, 490)
CYCLE_CORE = (250, 294, 330, 375, 490)

# Explicit maximum packing witness.
PACKING_WITNESS = (81, 328, 375, 490)

# After peeling common-divisor compatibility classes 4, 9, and 14, the
# remaining hard targets are exactly this pairwise-compatible residual class.
RESIDUAL_COMPATIBILITY_CLASS = (150, 250, 330, 375, 390)


def cover_witness_covers_all_hard_targets() -> bool:
    return all(
        any(target % g == 0 for g in COVER_WITNESS)
        for target in hard_targets_490_h3()
    )


def cycle_core_needs_three_cover_types() -> bool:
    """Check the 5-target coordination core has cover number exactly three.

    Candidate divisors are generated from the targets themselves, so this is a
    tiny exhaustive certificate rather than a general optimizer call.
    """
    candidates = sorted(
        {
            g
            for target in CYCLE_CORE
            for g in range(4, target + 1)
            if target % g == 0 and _is_composite(g)
        }
    )
    # explicit upper bound
    upper = (10, 14, 25)
    if not all(any(t % g == 0 for g in upper) for t in CYCLE_CORE):
        return False
    # exhaustive two-type exclusion
    return not any(
        all(t % g == 0 or t % k == 0 for t in CYCLE_CORE)
        for g, k in combinations(candidates, 2)
    )


def cover_lower_core_needs_five_types() -> bool:
    """Seven-target lower certificate for cover >= 5.

    Targets 351 and 416 cannot share a candidate with each other or with any
    target in ``CYCLE_CORE`` because every corresponding gcd is 1 or prime.
    They therefore consume two distinct types outside the three types forced by
    the cycle core.
    """
    if not cycle_core_needs_three_cover_types():
        return False
    anchors = (351, 416)
    if not targets_are_divisor_incompatible(*anchors):
        return False
    return all(
        targets_are_divisor_incompatible(anchor, target)
        for anchor in anchors
        for target in CYCLE_CORE
    )


def packing_witness_is_pairwise_incompatible() -> bool:
    return all(
        targets_are_divisor_incompatible(a, b)
        for a, b in combinations(PACKING_WITNESS, 2)
    )


def compatibility_color(target: int) -> int:
    """Four-color certificate for every hard target.

    Color 0: divisible by 4.
    Color 1: not color 0, divisible by 9.
    Color 2: neither prior color, divisible by 14.
    Color 3: the residual five-target class.
    """
    if target % 4 == 0:
        return 0
    if target % 9 == 0:
        return 1
    if target % 14 == 0:
        return 2
    if target in RESIDUAL_COMPATIBILITY_CLASS:
        return 3
    raise AssertionError(f"unclassified hard target: {target}")


def four_class_coloring_is_valid() -> bool:
    hard = hard_targets_490_h3()
    groups: dict[int, list[int]] = {0: [], 1: [], 2: [], 3: []}
    for target in hard:
        groups[compatibility_color(target)].append(target)
    for targets in groups.values():
        for a, b in combinations(targets, 2):
            # Same color means there exists a composite divisor shared by the
            # two targets, equivalently their gcd is composite.
            if targets_are_divisor_incompatible(a, b):
                return False
    return tuple(groups[3]) == RESIDUAL_COMPATIBILITY_CLASS


def certified_packing_number() -> int:
    assert packing_witness_is_pairwise_incompatible()
    assert four_class_coloring_is_valid()
    return 4


def certified_cover_number() -> int:
    assert cover_witness_covers_all_hard_targets()
    assert cover_lower_core_needs_five_types()
    return 5


def canonical_gap_certificate() -> tuple[int, int]:
    """Return ``(packing, cover)=(4,5)`` after checking all certificates."""
    return certified_packing_number(), certified_cover_number()


assert canonical_gap_certificate() == (4, 5)
