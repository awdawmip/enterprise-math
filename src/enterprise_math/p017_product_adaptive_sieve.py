"""Pure signed-divisor formula for the product-adaptive P017 sieve majorant.

CG12--CG14 provide all ingredients needed to remove state factorization from the
product-adaptive Bonferroni correction.

For squarefree transverse D let I_k(D) be the CG12 anchor-filtered signed
incidence count.  The j-th support moment is exactly

    S_j(k) = sum_{omega(D)=j} I_k(D),

because every signed state with support size c contributes one incidence for
each j-subset of its support.

For positive odd m define

    B_m = S_1-S_2+...+S_m.

CG13 gives the ordinary Bonferroni defect-token mass

    E_m = sum_{omega(D)=m+1} I_k^min(D).

CG14 partitions every canonical squarefree token incidence by the exact full
prime-power block A.  Let

    R_m = sum_{A<=k-1, omega(rad(A))=m+1} I_k^{min,exact}(A).

Then the product-adaptive majorant is the pure divisor-side quantity

    B~_m = B_m - E_m + R_m.

Pointwise token cancellation proves independently that

    B~_m = U + R_m,

where U is the true nonempty-support/composite signed-state union.  Hence B~_m
is a valid upper majorant and its complete excess is supported on exact full
blocks A<=k-1.

The implementation below is a bounded reference enumerator, not a proposed
large-k algorithm.  The formulas themselves are finite identities.  In
particular, the reusable block candidate set can often be enumerated much more
cheaply from the product cutoff alone.

No Legendre proof or canonical L-number is claimed.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to
from .p017_canonical_token_incidence import canonical_token_incidence_profile
from .p017_core_divisor_capacity import signed_divisor_capacity
from .p017_full_block_token_incidence import canonical_full_block_partition


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _transverse_odd_primes(k: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    center = k * (k + 1)
    return tuple(
        prime
        for prime in primes_up_to(k)
        if prime != 2 and center % prime != 0
    )


def squarefree_token_candidates_below_cutoff(
    k: int,
    order: int,
    cutoff: int | None = None,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Enumerate squarefree (m+1)-prime transverse products <=cutoff.

    The recursion stops as soon as the minimum completion product exceeds the
    cutoff, so high-order low-product candidate sets can remain very small even
    when k itself is large.
    """
    _require_order(order)
    if cutoff is None:
        cutoff = k - 1
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    primes = _transverse_odd_primes(k)
    depth = order + 1
    rows: list[tuple[int, tuple[int, ...]]] = []

    def extend(start: int, remaining: int, current: int, chosen: tuple[int, ...]) -> None:
        if remaining == 0:
            rows.append((current, chosen))
            return
        for index in range(start, len(primes)):
            prime = primes[index]
            candidate = current * prime
            if candidate > cutoff:
                break
            if remaining > 1:
                if index + remaining - 1 >= len(primes):
                    break
                minimum_completion = candidate
                for step in range(1, remaining):
                    minimum_completion *= primes[index + step]
                    if minimum_completion > cutoff:
                        break
                if minimum_completion > cutoff:
                    break
            extend(index + 1, remaining - 1, candidate, chosen + (prime,))

    extend(0, depth, 1, ())
    return tuple(rows)


def support_moment_divisor_sum(k: int, degree: int) -> dict[str, object]:
    """Return S_degree as a finite sum of CG12 signed divisor incidences."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    transverse = _transverse_odd_primes(k)
    max_state = k * (k + 2)
    rows: list[tuple[int, int]] = []
    total = 0
    for subset in combinations(transverse, degree):
        divisor = prod(subset)
        if divisor > max_state:
            continue
        count = int(signed_divisor_capacity(k, divisor)["anchor_count"])
        if count:
            rows.append((divisor, count))
            total += count
    return {
        "k": k,
        "degree": degree,
        "incidence_rows": tuple(rows),
        "support_moment": total,
    }


def ordinary_bonferroni_divisor_sum(k: int, order: int) -> dict[str, object]:
    """Return B_m from pure CG12 support-moment divisor sums."""
    _require_order(order)
    moments = tuple(
        int(support_moment_divisor_sum(k, degree)["support_moment"])
        for degree in range(1, order + 1)
    )
    value = sum(
        moment if index % 2 == 0 else -moment
        for index, moment in enumerate(moments)
    )
    return {
        "k": k,
        "order": order,
        "moments": moments,
        "ordinary_bonferroni": value,
    }


def product_adaptive_divisor_majorant(k: int, order: int) -> dict[str, object]:
    """Assemble B~_m=B_m-E_m+R_m entirely from CG12--CG14 sums."""
    _require_order(order)
    ordinary = ordinary_bonferroni_divisor_sum(k, order)
    token_profile = canonical_token_incidence_profile(k, order)
    ordinary_defect = int(token_profile["canonical_token_mass"])

    reusable_full = 0
    full_rows: list[dict[str, object]] = []
    for token_row in token_profile["token_rows"]:
        radical = int(token_row["divisor"])
        partition = canonical_full_block_partition(k, radical)
        reusable = int(partition["reusable_full_block_incidence"])
        reusable_full += reusable
        if reusable:
            full_rows.append(partition)

    adjusted = int(ordinary["ordinary_bonferroni"]) - ordinary_defect + reusable_full
    if reusable_full > ordinary_defect:
        raise AssertionError("full-block reusable mass exceeded ordinary token defect")
    return {
        **ordinary,
        "ordinary_token_defect": ordinary_defect,
        "reusable_squarefree_token_mass": int(token_profile["reusable_squarefree_token_mass"]),
        "single_use_squarefree_token_mass": int(token_profile["single_use_squarefree_token_mass"]),
        "reusable_full_block_token_mass": reusable_full,
        "full_block_reusable_rows": tuple(full_rows),
        "product_adaptive_majorant": adjusted,
        "high_full_block_correction": ordinary_defect - reusable_full,
    }
