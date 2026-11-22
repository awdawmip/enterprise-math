"""Prime-scale finite-difference descent for truncated squarefree Möbius sums.

Let R be squarefree with prime support P and define

    S_R(B)=sum_(d|R,d<=B) mu(d),      B>=0.

Choose any prime p|R and put R'=R/p.  Splitting divisors according to whether
p is present gives the exact recursion

    S_R(B)
      = S_R'(B) - S_R'(floor(B/p)).

Equivalently, pair every divisor d|R' with p*d.  Pairs with p*d<=B cancel, so
only the multiplicative boundary shell remains:

    S_R(B)
      = sum_(d|R', floor(B/p)<d<=B) mu(d).

Thus one support prime is deleted exactly while the budget branches into B and
floor(B/p).  Iterating over the support expresses the whole truncated Möbius
boundary as a commuting finite-difference tree

    S_R = product_(p|R) (I-T_p) 1_(B>=1),

where T_p f(B)=f(floor(B/p)).  This is a finite BRC precision descent, not an
asymptotic Möbius estimate.

A useful necessary condition for a positive non-unit mixed inner follows.  Write
p1<p2<...<pc and suppose

    S_R(B)-1 > 0.

Then c>=4.  Since B>=p1, the unit divisor is absent from the shell after peeling
p1.  To make the shell sum exceed one, at least two positive-sign nonunit
divisors of R/p1 must lie below B.  The two smallest such divisors are

    p2*p3,  p2*p4.

Hence necessarily

    B >= p2*p4.

The four-prime witness R=3*5*7*11, B=77 satisfies this and shows the support
threshold c>=4 is sharp.  The p2*p4 condition is only necessary, not sufficient.

This module packages exact finite combinatorics for the mixed-Walsh boundary; it
does not determine which sign is globally harmful in a chosen detector and does
not prove Legendre's conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import prod


def divisor_rows(primes: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    normalized = tuple(sorted(int(p) for p in primes))
    if len(set(normalized)) != len(normalized):
        raise ValueError("primes must be distinct")
    rows: list[tuple[int, int]] = []
    for size in range(len(normalized) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(normalized, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(sorted(rows))


def truncated_mobius(primes: tuple[int, ...], budget: int) -> int:
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    return sum(mu for divisor, mu in divisor_rows(primes) if divisor <= budget)


def prime_scale_difference(primes: tuple[int, ...], budget: int, prime: int | None = None) -> dict[str, object]:
    """Verify S_P(B)=S_(P\p)(B)-S_(P\p)(floor(B/p)) and the shell form."""
    normalized = tuple(sorted(int(p) for p in primes))
    if not normalized:
        raise ValueError("primes must be nonempty")
    if prime is None:
        prime = normalized[0]
    if prime not in normalized:
        raise ValueError("prime must belong to the declared support")
    reduced = tuple(p for p in normalized if p != prime)
    direct = truncated_mobius(normalized, budget)
    coarse = truncated_mobius(reduced, budget)
    refined_budget = budget // prime
    refined = truncated_mobius(reduced, refined_budget)
    difference = coarse - refined
    shell = sum(
        mu
        for divisor, mu in divisor_rows(reduced)
        if refined_budget < divisor <= budget
    )
    if not (direct == difference == shell):
        raise AssertionError("prime-scale Möbius finite difference failed")
    return {
        "support_primes": normalized,
        "peeled_prime": prime,
        "reduced_support": reduced,
        "budget_B": budget,
        "refined_budget_floor_B_over_p": refined_budget,
        "direct_truncated_sum": direct,
        "coarse_reduced_sum": coarse,
        "refined_reduced_sum": refined,
        "finite_difference": difference,
        "boundary_shell_sum": shell,
        "prime_scale_difference_identity": True,
    }


def positive_inner_necessary_barrier(primes: tuple[int, ...], budget: int) -> dict[str, object]:
    """If S_R(B)-1>0, certify c>=4 and B>=p2*p4."""
    normalized = tuple(sorted(int(p) for p in primes))
    inner = truncated_mobius(normalized, budget) - 1
    positive = inner > 0
    if not positive:
        return {
            "support_primes": normalized,
            "budget_B": budget,
            "mixed_inner": inner,
            "positive_inner": False,
        }
    if len(normalized) < 4:
        raise AssertionError("positive mixed inner appeared below support depth four")
    threshold = normalized[1] * normalized[3]
    if budget < threshold:
        raise AssertionError("positive mixed inner appeared before the second positive shell divisor")
    return {
        "support_primes": normalized,
        "support_size": len(normalized),
        "budget_B": budget,
        "mixed_inner": inner,
        "positive_inner": True,
        "necessary_budget_p2_times_p4": threshold,
        "budget_reaches_two_positive_nonunit_divisors": True,
    }


def four_prime_difference_witness() -> dict[str, object]:
    primes = (3, 5, 7, 11)
    budget = 77
    row = positive_inner_necessary_barrier(primes, budget)
    if int(row["mixed_inner"]) != 2:
        raise AssertionError("four-prime finite-difference witness changed")
    return {
        **row,
        "sharp_support_threshold_witness": True,
    }
