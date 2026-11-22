"""Pointwise-minimal boundary-only orientation-Walsh prime amplifier.

The hard Walsh upper-prime detector on a surviving mirror radius is

    2^|L| * 1_{U empty},

where L,U are the disjoint lower/upper transverse prime supports.  The factor
2^|L| is stronger than necessary: its purpose is to cancel the continuous floor
term of every nonconstant orientation column.

For a selected transverse squarefree product D, odd-radius parity and an
effective-anchor divisor a make one root class live modulo 2*a*D.  After anchor
Mobius the complete continuous bulk is

    sum_{a|A} mu(a) floor((k-1)/(2*a*D))
      = #{1<=q<=(k-1)/(2D) : gcd(q,A)=1}.

Because q=1 is always anchor-coprime, this bulk is nonzero if and only if

    2D <= k-1.

Thus the exact reusable-floor cutoff is

    C_k = floor((k-1)/2),

not k-1.  For a finite transverse support S write rad(S)=product(S) and define

    h_min(S) = 2^|S|  if rad(S)<=C_k,
               1      if rad(S)>C_k.

Then

    W_min,+ = h_min(L) 1_{U empty}

is still positive exactly when the upper mirror side is prime (and symmetrically
for the lower side), but it is pointwise no larger than hard Walsh.

There is an exact Boolean-lattice proof that every nonconstant column remains
boundary-only.  For a general support weight h let beta(T) be the orientation-
summed continuous-floor coefficient of a selected prime set T.  The two Boolean
transforms satisfy

    h(S) = sum_{T subseteq S} 2^(|S|-|T|) beta(T),

hence

    beta(S) = sum_{T subseteq S} (-2)^(|S|-|T|) h(T).

If rad(S)<=C_k, every subset T of S is also reusable-floor and
h_min(T)=2^|T|, so beta(S)=0 for nonempty S.  If rad(S)>C_k, no cancellation is
required because the parity/anchor floor bulk already vanishes.  Thus every
nonconstant column is boundary-only.

This construction is pointwise minimal under the natural normalization h(S)>=1.
The zero-floor constraints beta(T)=0 for every nonempty reusable-floor T
recursively force h(S)=2^|S| whenever rad(S)<=C_k.  Above the cutoff the floor
imposes no constraint, so the least positive normalized value is exactly one.

Let J_floor(k) be the largest j for which the first j transverse odd primes have
product <=C_k.  Then every amplified support has size at most J_floor and

    1 <= h_min(S) <= 2^J_floor.

The compiler therefore removes every hard-Walsh amplification attached solely
to a support whose column is already boundary-only by finite-window geometry.
It is a proof-precision minimization theorem, not a Legendre proof and not a
short-window boundary estimate.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports


def _support_tuple(support: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")
    if any(p < 3 or p % 2 == 0 for p in normalized):
        raise ValueError("support entries must be odd integers >=3")
    return normalized


def reusable_floor_product_cutoff(k: int) -> int:
    """Return C_k=floor((k-1)/2), the exact parity-aware floor cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    return (k - 1) // 2


def reusable_floor_support_depth(k: int) -> dict[str, object]:
    """Return max j whose first j transverse odd primes fit below C_k."""
    cutoff = reusable_floor_product_cutoff(k)
    M = k * (k + 1)
    product_value = 1
    chosen: list[int] = []
    for prime in primes_up_to(k):
        if prime == 2 or M % prime == 0:
            continue
        if product_value > cutoff // prime:
            break
        product_value *= prime
        chosen.append(prime)
    return {
        "k": k,
        "reusable_floor_product_cutoff": cutoff,
        "reusable_floor_support_depth": len(chosen),
        "transverse_prime_prefix": tuple(chosen),
        "prefix_product": product_value,
    }


def support_radical(support: tuple[int, ...]) -> int:
    return prod(_support_tuple(support), start=1)


def minimal_boundary_amplifier_weight(k: int, support: tuple[int, ...]) -> int:
    """Return hard Walsh only below the exact reusable-floor cutoff; otherwise one."""
    normalized = _support_tuple(support)
    radical = prod(normalized, start=1)
    cutoff = reusable_floor_product_cutoff(k)
    return 2 ** len(normalized) if radical <= cutoff else 1


def orientation_floor_coefficient(k: int, selected_support: tuple[int, ...]) -> dict[str, object]:
    """Return beta(S), the orientation-summed continuous-floor coefficient."""
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
    cutoff = reusable_floor_product_cutoff(k)
    reusable = radical <= cutoff
    if reusable and beta != 0:
        raise AssertionError("reusable-floor selected set retained continuous bulk")
    floor_zero = radical > cutoff
    if not (beta == 0 or floor_zero):
        raise AssertionError("nonconstant selected column is not boundary-only")
    return {
        "k": k,
        "selected_support": selected,
        "selected_radical": radical,
        "reusable_floor_product_cutoff": cutoff,
        "orientation_floor_coefficient": beta,
        "reusable_floor_requires_cancellation": reusable,
        "coarse_floor_zero_by_parity_product": floor_zero,
        "nonconstant_column_boundary_only": True,
        "boolean_transform_rows": tuple(rows),
    }


def verify_pointwise_minimality(k: int, support: tuple[int, ...]) -> dict[str, object]:
    """Expose the forced/free dichotomy behind pointwise minimality."""
    normalized = _support_tuple(support)
    radical = prod(normalized, start=1)
    cutoff = reusable_floor_product_cutoff(k)
    weight = minimal_boundary_amplifier_weight(k, normalized)
    if radical <= cutoff:
        forced = 2 ** len(normalized)
        if weight != forced:
            raise AssertionError("reusable-floor weight is not forced hard-Walsh value")
        reason = "ZERO_FLOOR_CONSTRAINT_FORCES_HARD_WALSH"
    else:
        forced = 1
        if weight != forced:
            raise AssertionError("floor-free normalized weight is not minimal positive value")
        reason = "PARITY_ANCHOR_FLOOR_ALREADY_ZERO_MINIMAL_POSITIVE_WEIGHT_ONE"
    return {
        "k": k,
        "support": normalized,
        "radical": radical,
        "reusable_floor_product_cutoff": cutoff,
        "minimal_weight": weight,
        "pointwise_lower_bound_under_normalization": forced,
        "minimality_reason": reason,
        "pointwise_minimal_boundary_only": True,
    }


def minimal_boundary_walsh_profile(k: int) -> dict[str, object]:
    """Evaluate the minimal boundary-only detector across all surviving mirror radii."""
    depth_data = reusable_floor_support_depth(k)
    depth = int(depth_data["reusable_floor_support_depth"])
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
            raise AssertionError("minimal pair weight exceeded reusable-floor support cap")
    return {
        **depth_data,
        "one_side_weight_ceiling": max_weight,
        "surviving_radius_count": len(rows),
        "hard_walsh_weighted_prime_observable": hard_total,
        "minimal_boundary_weighted_prime_observable": minimal_total,
        "minimal_to_hard_ratio": (minimal_total / hard_total) if hard_total else 1.0,
        "prime_mirror_side_exists": prime_exists,
        "minimal_detector_positive_iff_prime_exists": (minimal_total > 0) == prime_exists,
        "rows": tuple(rows),
    }
