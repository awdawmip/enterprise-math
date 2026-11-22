"""Exact p-adic lift of canonical P017 token incidences.

CG13 converts the state-dependent least-support condition of a squarefree token
D into a pure signed-divisor Möbius sum.  This module retains prime-power
multiplicity as well.

Let

    D = product_i p_i

be a squarefree transverse token and prescribe a complete selected block

    A = product_i p_i^{e_i},   e_i>=1,

so rad(A)=D.  We want signed states n=M-x for which:

1. every selected prime block has *exactly* exponent e_i;
2. p0=min p_i is the least transverse small prime of n.

For exact valuations, after requiring A|n use inclusion--exclusion over one
additional copy of each selected prime.  For the least-prime condition, use the
CG13 Möbius exclusion over smaller transverse primes.  Writing I_k(E) for the
CG12 anchor-filtered signed incidence count of an arbitrary odd transverse
E gives

    I_k^{min,exact}(A)
      = sum_Q mu(Q)
          sum_{J subset supp(D)} (-1)^|J|
              I_k(A * Q * product_{p in J} p).

This is finite and exact.

For a fixed squarefree D, the canonical CG13 mass partitions by complete block:

    I_k^min(D)
      = sum_{rad(A)=D} I_k^{min,exact}(A),

where only A<=k(k+2) can divide an open square-basin state.  Splitting the right
side at A<=k-1 versus A>k-1 gives the multiplicity-preserving reusable/single-use
token mass required by the product-adaptive Bonferroni bridge.

All formulas are elementary valuation inclusion--exclusion plus CG12/CG13.  No
canonical L-number or Legendre proof is claimed.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .cutoff_pairing import distinct_prime_factors
from .legendre import squarefree_divisors_with_mu
from .p017_canonical_token_incidence import (
    canonical_least_support_incidence_mobius,
    canonical_least_support_signed_points,
    smaller_transverse_primes,
)
from .p017_core_divisor_capacity import signed_divisor_capacity


def _factor_with_exponents(value: int) -> tuple[tuple[int, int], ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    result: list[tuple[int, int]] = []
    remaining = value
    for prime in distinct_prime_factors(value):
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        result.append((prime, exponent))
    if remaining != 1:
        raise AssertionError("factorization did not exhaust value")
    return tuple(result)


def _valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def exact_full_block_signed_points(k: int, full_block: int) -> tuple[int, ...]:
    """Directly filter canonical rad(A)-token points to exact selected valuations."""
    factors = _factor_with_exponents(full_block)
    if not factors:
        raise ValueError("full_block must contain at least one prime")
    radical = prod(prime for prime, _exponent in factors)
    canonical = canonical_least_support_signed_points(k, radical)
    center = k * (k + 1)
    points = tuple(
        point
        for point in canonical
        if all(
            _valuation(center - int(point), prime) == exponent
            for prime, exponent in factors
        )
    )
    return points


def canonical_full_block_incidence_mobius(k: int, full_block: int) -> dict[str, object]:
    """Evaluate the exact least-support + exact-valuation divisor formula."""
    factors = _factor_with_exponents(full_block)
    if not factors:
        raise ValueError("full_block must contain at least one prime")
    primes = tuple(prime for prime, _exponent in factors)
    radical = prod(primes)

    # Reuse CG13 validation of the squarefree radical and its least-prime rule.
    squarefree = canonical_least_support_incidence_mobius(k, radical)
    least = primes[0]
    smaller = smaller_transverse_primes(k, least)

    total = 0
    terms: list[tuple[int, int, int, int, int]] = []
    for q_product, mu_q in squarefree_divisors_with_mu(list(smaller)):
        for mask in range(1 << len(primes)):
            next_power = 1
            selected_count = 0
            for index, prime in enumerate(primes):
                if mask & (1 << index):
                    next_power *= prime
                    selected_count += 1
            sign = mu_q * (-1 if selected_count % 2 else 1)
            augmented = full_block * q_product * next_power
            incidence = int(signed_divisor_capacity(k, augmented)["anchor_count"])
            total += sign * incidence
            terms.append((q_product, next_power, sign, augmented, incidence))

    direct = exact_full_block_signed_points(k, full_block)
    if total != len(direct):
        raise AssertionError("full-block Möbius/valuation formula disagrees with direct incidence")
    if total < 0:
        raise AssertionError("exact full-block token incidence cannot be negative")

    return {
        "k": k,
        "full_block": full_block,
        "radical": radical,
        "prime_exponents": factors,
        "least_token_prime": least,
        "canonical_squarefree_incidence": int(squarefree["canonical_incidence"]),
        "formula_terms": tuple(terms),
        "canonical_signed_points": direct,
        "exact_full_block_incidence": total,
        "full_block_cg12_capacity": int(signed_divisor_capacity(k, full_block)["universal_capacity"]),
        "full_block_single_use": full_block > k - 1,
    }


def _full_blocks_for_radical(k: int, radical: int) -> tuple[int, ...]:
    """Enumerate A with rad(A)=radical and A<=k(k+2), for reference auditing."""
    squarefree = canonical_least_support_incidence_mobius(k, radical)
    primes = tuple(int(p) for p in squarefree["token_primes"])
    limit = k * (k + 2)
    values: list[int] = []

    def extend(index: int, current: int) -> None:
        if index == len(primes):
            values.append(current)
            return
        prime = primes[index]
        power = prime
        while current * power <= limit:
            extend(index + 1, current * power)
            power *= prime

    extend(0, 1)
    return tuple(sorted(values))


def canonical_full_block_partition(k: int, radical: int) -> dict[str, object]:
    """Partition I_min(radical) exactly by full prime-power block A."""
    squarefree = canonical_least_support_incidence_mobius(k, radical)
    rows: list[dict[str, object]] = []
    total = 0
    reusable = 0
    single_use = 0
    for full_block in _full_blocks_for_radical(k, radical):
        data = canonical_full_block_incidence_mobius(k, full_block)
        count = int(data["exact_full_block_incidence"])
        if count == 0:
            continue
        rows.append(data)
        total += count
        if full_block <= k - 1:
            reusable += count
        else:
            single_use += count

    if total != int(squarefree["canonical_incidence"]):
        raise AssertionError("full-block partition did not reconstruct CG13 squarefree incidence")
    if total != reusable + single_use:
        raise AssertionError("full-block product-cutoff split failed")

    return {
        "k": k,
        "radical": radical,
        "canonical_squarefree_incidence": int(squarefree["canonical_incidence"]),
        "full_block_rows": tuple(rows),
        "full_block_incidence": total,
        "reusable_full_block_incidence": reusable,
        "single_use_full_block_incidence": single_use,
    }
