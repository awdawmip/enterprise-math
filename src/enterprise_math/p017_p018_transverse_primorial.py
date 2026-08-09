"""Anchor-sensitive transverse primorial barriers for Bonferroni defect.

The universal residual Bonferroni localization uses the first odd primes.  The
actual P017 hard core is stronger: every prime appearing in an anchor-surviving
full core is transverse to the center

    M = k(k+1).

For j>=1 let P_perp(k,j) be the product of the first j odd primes p<=k with
p not dividing M.  If an odd order-m Bonferroni defect occurs in a residual
S=ab<k pair, one mirror core contains at least m+1 distinct transverse primes
and the other contains at least one further distinct transverse prime.  Hence

    S >= P_perp(k,m+2).

Consequently a residual order-m defect is impossible whenever fewer than m+2
transverse odd primes are available, or whenever

    P_perp(k,m+2) >= k.

This yields an exact residual proof-precision ceiling.  Define J_perp(k) as the
largest j for which P_perp(k,j)<k.  Any residual product S<k has at most
J_perp(k) distinct core primes in total.  Since both mirror cores are nonempty,
each individual side has support size at most J_perp(k)-1.  Therefore the least
positive odd m satisfying

    m >= J_perp(k)-1

has zero Bonferroni defect on *every* residual hard-core state.  At that order
the Bonferroni row value is the exact nonempty-support indicator, not merely an
upper approximation.

This is a genuinely joint finite-boundary effect: independent one-prime local
marginals are exactly calibrated, but the requirement that many distinct
transverse primes coexist in one residual core product can be too expensive.

For the first order-three defect band one may also use P_perp(k,4) as the
minimum possible four-prime defect-side core.  This can greatly exceed the
universal 3*5*7*11=1155 when small primes divide the anchor.
"""

from __future__ import annotations

from .legendre import primes_up_to
from .p017_p018_bonferroni_primorial import distinct_prime_count
from .p017_p018_hard_core_partition import residual_hard_core_record


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")


def _require_count(count: int) -> None:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a nonnegative integer")


def transverse_odd_prime_prefix(k: int, count: int) -> tuple[int, ...]:
    """Return up to the first ``count`` odd primes <=k transverse to M."""
    _require_k(k)
    _require_count(count)
    center = k * (k + 1)
    result: list[int] = []
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0:
            continue
        result.append(prime)
        if len(result) == count:
            break
    return tuple(result)


def transverse_odd_primorial(k: int, count: int) -> dict[str, object]:
    """Return the anchor-sensitive product of the first ``count`` usable odd primes."""
    primes = transverse_odd_prime_prefix(k, count)
    product = 1
    for prime in primes:
        product *= prime
    return {
        "k": k,
        "count": count,
        "transverse_primes": primes,
        "complete": len(primes) == count,
        "product": product,
    }


def transverse_primorial_depth(k: int) -> dict[str, object]:
    """Return J_perp(k)=max{j:P_perp(k,j)<k} and the first blocking prime.

    Products increase strictly with every newly included prime, so once the next
    transverse prime would make the product reach or exceed k, no longer prefix
    can fit below the residual product cutoff.
    """
    _require_k(k)
    center = k * (k + 1)
    product = 1
    used: list[int] = []
    blocking_prime: int | None = None
    blocking_product: int | None = None
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0:
            continue
        candidate = product * prime
        if candidate >= k:
            blocking_prime = prime
            blocking_product = candidate
            break
        product = candidate
        used.append(prime)

    return {
        "k": k,
        "transverse_primorial_depth": len(used),
        "fitting_transverse_primes": tuple(used),
        "largest_fitting_product": product,
        "blocking_prime": blocking_prime,
        "first_blocking_product": blocking_product,
    }


def residual_exact_bonferroni_order(k: int) -> dict[str, object]:
    """Return the least positive odd order guaranteed defect-free on S<k.

    If J=J_perp(k), each residual side has at most J-1 distinct core primes.
    Thus any odd order m>=J-1 is pointwise exact on every residual state.
    """
    depth = transverse_primorial_depth(k)
    j = int(depth["transverse_primorial_depth"])
    target = max(1, j - 1)
    if target % 2 == 0:
        target += 1
    return {
        **depth,
        "max_total_distinct_core_primes": j,
        "max_side_support_size": max(0, j - 1),
        "least_guaranteed_exact_odd_order": target,
    }


def residual_transverse_defect_barrier(k: int, order: int) -> dict[str, object]:
    """Return the joint transverse-prime barrier for residual order-m defect."""
    _require_k(k)
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    required = order + 2
    data = transverse_odd_primorial(k, required)
    complete = bool(data["complete"])
    barrier = int(data["product"])
    impossible = (not complete) or barrier >= k
    return {
        **data,
        "order": order,
        "required_total_distinct_core_primes": required,
        "residual_defect_impossible": impossible,
    }


def residual_transverse_defect_localization(k: int, radius: int, order: int) -> dict[str, object]:
    """Certify S>=P_perp(k,m+2) whenever one residual side has order-m defect."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    record = residual_hard_core_record(k, radius)
    a = int(record["lower_core"])
    b = int(record["upper_core"])
    lower_support = distinct_prime_count(a)
    upper_support = distinct_prime_count(b)
    lower_defect = lower_support >= order + 1
    upper_defect = upper_support >= order + 1
    defect = lower_defect or upper_defect

    barrier = residual_transverse_defect_barrier(k, order)
    if defect:
        if not bool(barrier["complete"]):
            raise AssertionError("actual defect exists without enough transverse odd primes")
        required = order + 2
        if lower_support + upper_support < required:
            raise AssertionError("residual defect lost the required disjoint support count")
        if int(record["core_product"]) < int(barrier["product"]):
            raise AssertionError("residual defect fell below its transverse primorial barrier")
        if bool(barrier["residual_defect_impossible"]):
            raise AssertionError("actual residual defect exists despite an impossible transverse barrier")

    return {
        **record,
        "order": order,
        "lower_support_size": lower_support,
        "upper_support_size": upper_support,
        "lower_defect_possible": lower_defect,
        "upper_defect_possible": upper_defect,
        "defect_possible": defect,
        "transverse_primorial_barrier": int(barrier["product"]),
        "transverse_primorial_primes": tuple(barrier["transverse_primes"]),
        "residual_defect_impossible_at_scale": bool(barrier["residual_defect_impossible"]),
    }


def residual_exactness_check(k: int, radius: int) -> dict[str, object]:
    """Audit the guaranteed exact odd Bonferroni order on one residual pair."""
    record = residual_hard_core_record(k, radius)
    a = int(record["lower_core"])
    b = int(record["upper_core"])
    lower_support = distinct_prime_count(a)
    upper_support = distinct_prime_count(b)
    ceiling = residual_exact_bonferroni_order(k)
    order = int(ceiling["least_guaranteed_exact_odd_order"])
    if lower_support > order or upper_support > order:
        raise AssertionError("residual support escaped the transverse-primorial exactness ceiling")
    return {
        **record,
        "lower_support_size": lower_support,
        "upper_support_size": upper_support,
        "exact_odd_order": order,
        "lower_point_defect": 0,
        "upper_point_defect": 0,
        "residual_pair_defect": 0,
        "transverse_primorial_depth": int(ceiling["transverse_primorial_depth"]),
    }
