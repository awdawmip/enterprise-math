"""Primorial localization of Bonferroni precision defects in the residual hard core.

In a residual hard-core pair

    M-r=a*q_-,  M+r=b*q_+,  S=ab<k,

the tails are primes >k, so the transverse support sizes of the two states are
exactly the numbers of distinct prime factors of the coprime odd full cores a
and b.  Both cores are nontrivial and their prime supports are disjoint.

An odd Bonferroni truncation of order m has point defect only when one support
size is at least m+1.  The other mirror core still contributes at least one
distinct odd prime, hence such a residual pair would force

    omega(S) >= m+2.

Therefore

    S >= P_odd(m+2),

where P_odd(h) is the product of the first h odd primes.  Consequently, if

    k <= P_odd(m+2),

no state inside the residual S<k hard core can carry any order-m Bonferroni
defect.  All high-support precision defect is pushed outside the repeated hard
core into the S>=k region, where canonical L053 already gives singleton
full-core progressions.

Reference thresholds:

    m=3: P_odd(5)=15015,
    m=5: P_odd(7)=4,849,845.

This does not prove that the S>=k singleton region is empty.  It isolates where
high support complexity can live and shows that repeated residual cells have a
strictly lower proof-precision burden.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_p018_hard_core_partition import residual_hard_core_record


def first_odd_primes(count: int) -> tuple[int, ...]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a nonnegative integer")
    result: list[int] = []
    candidate = 3
    while len(result) < count:
        if is_prime(candidate):
            result.append(candidate)
        candidate += 2
    return tuple(result)


def odd_primorial(count: int) -> int:
    value = 1
    for prime in first_odd_primes(count):
        value *= prime
    return value


def distinct_prime_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    remaining = value
    count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            count += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        count += 1
    return count


def residual_bonferroni_defect_localization(k: int, radius: int, order: int) -> dict[str, object]:
    """Certify the primorial barrier for one exact residual hard-core pair."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    data = residual_hard_core_record(k, radius)
    a = int(data["lower_core"])
    b = int(data["upper_core"])
    s = a * b
    lower_support = distinct_prime_count(a)
    upper_support = distinct_prime_count(b)
    barrier = odd_primorial(order + 2)

    lower_defect_possible = lower_support >= order + 1
    upper_defect_possible = upper_support >= order + 1
    if (lower_defect_possible or upper_defect_possible) and s < barrier:
        raise AssertionError("high-support residual core fell below its odd primorial barrier")
    if k <= barrier and (lower_defect_possible or upper_defect_possible):
        raise AssertionError("order-m Bonferroni defect survived below the residual primorial threshold")

    return {
        **data,
        "order": order,
        "lower_support_size": lower_support,
        "upper_support_size": upper_support,
        "odd_primorial_barrier": barrier,
        "lower_defect_possible": lower_defect_possible,
        "upper_defect_possible": upper_defect_possible,
        "residual_defect_free": not (lower_defect_possible or upper_defect_possible),
    }


def residual_defect_free_threshold(order: int) -> dict[str, object]:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    barrier = odd_primorial(order + 2)
    return {
        "order": order,
        "required_total_distinct_core_primes": order + 2,
        "odd_primorial_barrier": barrier,
        "defect_free_for_residual_k_at_most": barrier,
    }
