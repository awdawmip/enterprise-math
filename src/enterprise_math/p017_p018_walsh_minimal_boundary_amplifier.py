"""Pointwise-minimal boundary-only orientation-Walsh prime amplifier.

The hard Walsh upper-prime detector on a surviving mirror radius is

    2^|L| * 1_{U empty},

where L,U are the disjoint lower/upper transverse prime supports.  The factor
2^|L| is stronger than necessary: its purpose is to cancel the continuous
floor term of every nonconstant orientation column, but a selected squarefree
modulus D>k-1 already has zero floor in the radius window 1..k-1.

Let K=k-1.  For a finite transverse support S write rad(S)=product(S) and define

    h_K(S) = 2^|S|  if rad(S)<=K,
             1      if rad(S)>K.

Then

    W_min,+ = h_K(L) 1_{U empty}

is still positive exactly when the upper mirror side is prime (and symmetrically
for the lower side), but it is pointwise no larger than hard Walsh.

There is an exact Boolean-lattice proof that every nonconstant column remains
boundary-only.  For a general support weight h let beta(T) be the orientation-
summed continuous-floor coefficient of a selected prime set T.  The two Boolean
transforms satisfy

    h(S) = sum_{T subseteq S} 2^(|S|-|T|) beta(T),

hence

    beta(S) = sum_{T subseteq S} (-2)^(|S|-|T|) h(T).

If rad(S)<=K, every subset T of S is also low-product and h_K(T)=2^|T|, so
beta(S)=0 for nonempty S.  If rad(S)>K, no cancellation is required because the
one-class floor count already vanishes: its modulus exceeds the radius-window
length.  Thus every nonconstant column is boundary-only.

This construction is also pointwise minimal under the natural normalization
h(S)>=1.  Indeed the zero-floor constraints beta(T)=0 for every nonempty
low-product T recursively force h(S)=2^|S| on every support with rad(S)<=K.
On high-product supports the floor imposes no constraint, so the least positive
normalized value is exactly one.

Let J_perp(k)=max{j:P_perp(k,j)<k}.  Every low-product support has size at most
J_perp, hence

    1 <= h_K(S) <= 2^J_perp.

The compiler therefore removes every hard-Walsh amplification attached solely
to high-product/single-use support while preserving exact prime detection and
zero floor bulk.  It is a proof-precision minimization theorem, not a Legendre
proof and not a short-window boundary estimate.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports
from .p017_p018_transverse_primorial import transverse_primorial_depth


def _support_tuple(support: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")
    if any(p < 3 or p % 2 == 0 for p in normalized):
        raise ValueError("support entries must be odd integers >=3")
    return normalized


def support_radical(support: tuple[int, ...]) -> int:
    return prod(_support_tuple(support), start=1)


def minimal_boundary_amplifier_weight(k: int, support: tuple[int, ...]) -> int:
    """Return h_K(S)=2^|S| below the reusable-product cutoff and 1 above it."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    normalized = _support_tuple(support)
    radical = prod(normalized, start=1)
    return 2 ** len(normalized) if radical <= k - 1 else 1


def orientation_floor_coefficient(k: int, selected_support: tuple[int, ...]) -> dict[str, object]:
    """Return beta(S), the orientation-summed continuous-floor coefficient."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    selected = _support_tuple(selected_support)
    if not selected:
        raise ValueError("selected_support must be nonempty")
    beta = 0
    rows: list[dict[str, object]] = []
    n = len(selected)
    for size in range(n + 1):
        for subset in combinations(selected, size):
            h = minimal_boundary_amplifier_weight(k, tuple(subset))
            coefficient = ((-2) ** (n - size)) * h
            beta += coefficient
            rows.append({"subset": subset, "h": h, "term": coefficient})
    radical = prod(selected)
    low_product = radical <= k - 1
    if low_product and beta != 0:
        raise AssertionError("low-product selected set retained continuous floor bulk")
    coarse_floor_zero = radical > k - 1
    if not (beta == 0 or coarse_floor_zero):
        raise AssertionError("nonconstant selected column is not boundary-only")
    return {
        "k": k,
        "selected_support": selected,
        "selected_radical": radical,
        "orientation_floor_coefficient": beta,
        "low_product_requires_cancellation": low_product,
        "coarse_floor_zero_by_product": coarse_floor_zero,
        "nonconstant_column_boundary_only": True,
        "boolean_transform_rows": tuple(rows),
    }


def verify_pointwise_minimality(k: int, support: tuple[int, ...]) -> dict[str, object]:
    """Expose the forced/free dichotomy behind pointwise minimality."""
    normalized = _support_tuple(support)
    radical = prod(normalized, start=1)
    weight = minimal_boundary_amplifier_weight(k, normalized)
    if radical <= k - 1:
        forced = 2 ** len(normalized)
        if weight != forced:
            raise AssertionError("low-product weight is not forced hard-Walsh value")
        reason = "ZERO_FLOOR_CONSTRAINT_FORCES_HARD_WALSH"
    else:
        forced = 1
        if weight != forced:
            raise AssertionError("high-product normalized weight is not minimal positive value")
        reason = "FLOOR_ALREADY_ZERO_MINIMAL_POSITIVE_WEIGHT_ONE"
    return {
        "k": k,
        "support": normalized,
        "radical": radical,
        "minimal_weight": weight,
        "pointwise_lower_bound_under_normalization": forced,
        "minimality_reason": reason,
        "pointwise_minimal_boundary_only": True,
    }


def minimal_boundary_walsh_profile(k: int) -> dict[str, object]:
    """Evaluate the minimal boundary-only detector across all surviving mirror radii."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    depth = int(transverse_primorial_depth(k)["transverse_primorial_depth"])
    rows: list[dict[str, object]] = []
    hard_total = 0
    minimal_total = 0
    prime_exists = False
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        lower = tuple(int(p) for p in lower_support)
        upper = tuple(int(p) for p in upper_support)
        upper_prime = len(upper) == 0
        lower_prime = len(lower) == 0
        upper_hard = 2 ** len(lower) if upper_prime else 0
        lower_hard = 2 ** len(upper) if lower_prime else 0
        upper_min = minimal_boundary_amplifier_weight(k, lower) if upper_prime else 0
        lower_min = minimal_boundary_amplifier_weight(k, upper) if lower_prime else 0
        if upper_min > upper_hard or lower_min > lower_hard:
            raise AssertionError("minimal amplifier exceeded hard Walsh")
        hard_total += upper_hard + lower_hard
        minimal_total += upper_min + lower_min
        prime = upper_prime or lower_prime
        prime_exists = prime_exists or prime
        rows.append(
            {
                "radius": radius,
                "lower_support": lower,
                "upper_support": upper,
                "upper_prime": upper_prime,
                "lower_prime": lower_prime,
                "hard_pair_weight": upper_hard + lower_hard,
                "minimal_pair_weight": upper_min + lower_min,
            }
        )
    if (minimal_total > 0) != prime_exists:
        raise AssertionError("minimal boundary-only detector lost prime-existence equivalence")
    max_weight = 2 ** depth
    for row in rows:
        if int(row["minimal_pair_weight"]) > 2 * max_weight:
            raise AssertionError("minimal pair weight exceeded support-depth cap")
    return {
        "k": k,
        "transverse_primorial_depth": depth,
        "one_side_weight_ceiling": max_weight,
        "surviving_radius_count": len(rows),
        "hard_walsh_weighted_prime_observable": hard_total,
        "minimal_boundary_weighted_prime_observable": minimal_total,
        "minimal_to_hard_ratio": (minimal_total / hard_total) if hard_total else 1.0,
        "prime_mirror_side_exists": prime_exists,
        "minimal_detector_positive_iff_prime_exists": (minimal_total > 0) == prime_exists,
        "rows": tuple(rows),
    }
