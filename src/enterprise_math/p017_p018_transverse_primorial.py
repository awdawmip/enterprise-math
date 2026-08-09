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

This is a genuinely joint finite-boundary effect: independent one-prime local
marginals are exactly calibrated, but the requirement that *m+2 distinct*
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
