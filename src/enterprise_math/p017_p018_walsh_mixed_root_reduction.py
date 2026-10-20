"""Pure-positive / mixed-root reduction for even-conductor symmetric Walsh boundary.

For a nontrivial even-support squarefree conductor q, the symmetric reusable
Walsh coefficient on an orientation split q=a*b is mu(b) (equivalently mu(a)),
where a collects lower/+ roots and b upper/- roots.  The two pure splits are

    (a,b)=(q,1), (1,q).

Since omega(q) is even, both pure coefficients are +1.  Their physical
incidences are ordinary nonnegative same-orientation counts.  Therefore any
lower bound for the total even-conductor boundary may discard the pure roots;
all potentially harmful signed mass is carried by mixed splits a,b>1.

For every mixed split, unordered reciprocity allows the smaller factor to be
named b.  Then

    1 < b <= sqrt(q) <= sqrt(C),

where C=floor((k-1)/2) is the reusable-floor conductor cutoff.  Thus the harmful
mixed-root language has one forced square-root-scale denominator even though q
itself ranges to O(k).

Combined with p017_p018_walsh_mixed_farey, every such mixed root is a
Determinant-1/Farey phase

    e(-h M (x/b+t/a)),      a*x-b*t=1,

with the smaller denominator b<=sqrt(C).  This is an exact analytic-dimension
reduction.  It does not bound the mixed-root discrepancy and does not prove
Legendre's conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import isqrt, prod

from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def even_conductor_orientation_splits(k: int, primes: tuple[int, ...]) -> dict[str, object]:
    """Enumerate pure/mixed splits of one positive even-degree conductor."""
    normalized = tuple(sorted(int(p) for p in primes))
    if len(normalized) < 2 or len(normalized) % 2:
        raise ValueError("primes must have positive even cardinality")
    if len(set(normalized)) != len(normalized):
        raise ValueError("primes must be distinct")
    q = prod(normalized)
    C = reusable_floor_product_cutoff(k)
    if q > C:
        raise ValueError("conductor must lie in the reusable-floor range")

    pure: list[dict[str, int | bool]] = []
    mixed: list[dict[str, int | bool]] = []
    for size in range(len(normalized) + 1):
        for negative_subset in combinations(normalized, size):
            b = prod(negative_subset, start=1)
            a = q // b
            coefficient = -1 if size % 2 else 1
            row = {
                "positive_product_a": a,
                "negative_product_b": b,
                "coefficient": coefficient,
                "pure_split": a == 1 or b == 1,
            }
            if row["pure_split"]:
                if coefficient != 1:
                    raise AssertionError("even conductor pure root did not have positive coefficient")
                pure.append(row)
            else:
                mixed.append(row)

    if len(pure) != 2:
        raise AssertionError("even conductor must have exactly two pure orientation roots")
    if any(int(row["coefficient"]) != 1 for row in pure):
        raise AssertionError("pure even-conductor roots are not both positive")

    unordered: dict[tuple[int, int], dict[str, int | bool]] = {}
    for row in mixed:
        a = int(row["positive_product_a"])
        b = int(row["negative_product_b"])
        key = tuple(sorted((a, b)))
        if key not in unordered:
            small, large = key
            if small > isqrt(q):
                raise AssertionError("mixed split smaller factor exceeded sqrt(q)")
            unordered[key] = {
                "small_factor": small,
                "large_factor": large,
                "product": q,
                "small_factor_at_most_sqrt_conductor": True,
                "small_factor_at_most_sqrt_floor_cutoff": small <= isqrt(C),
            }

    return {
        "k": k,
        "conductor": q,
        "support_degree": len(normalized),
        "reusable_floor_cutoff": C,
        "pure_splits": tuple(pure),
        "mixed_ordered_splits": tuple(mixed),
        "mixed_unordered_factor_pairs": tuple(unordered.values()),
        "pure_root_contribution_nonnegative": True,
        "harmful_boundary_reduces_to_mixed_roots": True,
        "mixed_small_denominator_ceiling": isqrt(C),
    }


def mixed_denominator_horizon(k: int) -> dict[str, int | bool]:
    """Return the universal square-root denominator horizon for harmful mixed roots."""
    C = reusable_floor_product_cutoff(k)
    return {
        "k": k,
        "reusable_floor_cutoff": C,
        "mixed_small_denominator_ceiling": isqrt(C),
        "one_mixed_denominator_is_square_root_scale": True,
    }
