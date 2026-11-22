"""Precision Pareto / uncertainty law for boundary-only Walsh amplifiers.

Fix one opposite transverse support S and the exact reusable-floor down-set

    D_C(S)={T subseteq S : rad(T)<=C_k},
    C_k=floor((k-1)/2).

For any normalized one-sided boundary-only prime amplifier h, write its unique
incidence expansion

    h(S)=sum_{T subseteq S} alpha(T),       h(empty)=1.

The zero-floor constraints on every nonempty reusable set force

    alpha(T)=1        for every T in D_C(S).

Let

    N=|D_C(S)|,
    H=2^|S|-N.

Then the total high-product incidence mass is exactly

    sum_{T notin D_C(S)} alpha(T)=h(S)-N.

Hölder therefore gives, for every real p>=1 and H>0,

    sum_{T subseteq S} |alpha(T)|^p
      >= N + |h(S)-N|^p / H^(p-1).

For p=1 this becomes the exact pointwise/analytic uncertainty bound

    ||alpha||_1 >= N+|h(S)-N|.

In particular, when 1<=h(S)<=N,

    h(S)+||alpha||_1 >= 2N.

The two canonical compilers occupy different extrema.

* The pointwise-minimal compiler pushes h(S) down to one on high-product
  supports.  It must pay at least 2N-1 incidence L1 mass there, and nested
  consistency can force still more variation.
* The incidence-optimal compiler sets every high-product alpha(T) to zero.
  It has h(S)=N and simultaneously minimizes every finite-p incidence norm on
  every support S.

Thus semantic weight and incidence/instruction complexity form a genuine Pareto
tradeoff.  There is no single notion of ``minimal precision'': minimizing the
state-side observable can increase the coefficient complexity of its exact
boundary representation.

The theorem is a Boolean down-set fact packaged here in the P017/P018 Walsh
language.  It is a candidate for later Foundation backflow, but this WIP module
does not promote a new generic foundation theorem and does not prove Legendre.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import prod

from .p017_p018_walsh_incidence_optimal import incidence_optimal_weight
from .p017_p018_walsh_minimal_boundary_amplifier import (
    minimal_boundary_amplifier_weight,
    reusable_floor_product_cutoff,
)


def _support(support: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct entries")
    if any(p < 3 or p % 2 == 0 for p in normalized):
        raise ValueError("support entries must be odd integers >=3")
    return normalized


def reusable_downset_size(k: int, support: tuple[int, ...]) -> int:
    """Return N=#{T subseteq S:rad(T)<=C_k}."""
    normalized = _support(support)
    cutoff = reusable_floor_product_cutoff(k)
    count = 0
    for size in range(len(normalized) + 1):
        for subset in combinations(normalized, size):
            if prod(subset, start=1) <= cutoff:
                count += 1
    return count


def incidence_norm_lower_bound(
    k: int,
    support: tuple[int, ...],
    pointwise_weight: int,
    power: int,
) -> dict[str, object]:
    """Return the exact Holder lower bound for p=1 or p=2 incidence cost."""
    normalized = _support(support)
    if isinstance(pointwise_weight, bool) or not isinstance(pointwise_weight, int) or pointwise_weight < 1:
        raise ValueError("pointwise_weight must be a positive integer")
    if power not in (1, 2):
        raise ValueError("executable reference supports power 1 or 2")
    N = reusable_downset_size(k, normalized)
    total = 2 ** len(normalized)
    H = total - N
    delta = pointwise_weight - N
    if H == 0:
        if pointwise_weight != N:
            raise ValueError("all subsets are forced; pointwise weight must equal N")
        lower = Fraction(N, 1)
    elif power == 1:
        lower = Fraction(N + abs(delta), 1)
    else:
        lower = Fraction(N, 1) + Fraction(delta * delta, H)
    return {
        "k": k,
        "support": normalized,
        "reusable_floor_product_cutoff": reusable_floor_product_cutoff(k),
        "reusable_downset_size": N,
        "free_high_product_subset_count": H,
        "pointwise_weight": pointwise_weight,
        "power": power,
        "incidence_power_sum_lower_bound": lower,
        "l1_uncertainty_sum_lower_bound": (
            Fraction(N + abs(delta), 1) if H else Fraction(N, 1)
        ),
    }


def canonical_pareto_comparison(k: int, support: tuple[int, ...]) -> dict[str, object]:
    """Compare pointwise-minimal and incidence-optimal endpoints on one support."""
    normalized = _support(support)
    N = reusable_downset_size(k, normalized)
    pointwise = minimal_boundary_amplifier_weight(k, normalized)
    incidence = incidence_optimal_weight(k, normalized)
    if incidence != N:
        raise AssertionError("incidence-optimal weight is not the reusable down-set size")
    point_l1_floor = incidence_norm_lower_bound(k, normalized, pointwise, 1)[
        "incidence_power_sum_lower_bound"
    ]
    incidence_l1 = Fraction(N, 1)
    if pointwise > incidence:
        raise AssertionError("pointwise-minimal compiler exceeded incidence-optimal weight")
    return {
        "k": k,
        "support": normalized,
        "reusable_downset_size": N,
        "pointwise_minimal_weight": pointwise,
        "pointwise_minimal_l1_lower_bound": point_l1_floor,
        "incidence_optimal_weight": incidence,
        "incidence_optimal_l1_cost": incidence_l1,
        "semantic_weight_order": "POINTWISE_MIN_LE_INCIDENCE_OPT_LE_HARD_WALSH",
        "pareto_tradeoff": pointwise < incidence,
    }
