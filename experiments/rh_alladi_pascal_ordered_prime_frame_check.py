#!/usr/bin/env python3
"""Exact finite checks for the Alladi-Pascal / ordered-prime BRC frame.

No third-party dependencies are required.  The checker verifies:

1. the collective Alladi polynomial identity;
2. the factorial-jet / ordered-factor Pascal transform and exact inverse;
3. the integer Pascal inverse;
4. the exact Hardy/Parseval energy identity after averaging over n <= X;
5. the (k,p) table column law and support light cone;
6. ordered-prime edge continuity and the path telescoping identity.

These are finite identity checks only, not evidence for RH.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import comb


def distinct_prime_factors(n: int) -> list[int]:
    """Return the distinct prime factors of n in increasing order."""
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append(n)
    return factors


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return [p for p in range(2, limit + 1) if is_prime[p]]


def collective_alladi_coefficients(
    prime_support: list[int],
    prime_weight,
) -> list[int]:
    """Coefficients of sum mu(d)(1+z)^(omega(d)-1)f(p1(d))."""
    r = len(prime_support)
    coefficients = [0] * r
    for arity in range(1, r + 1):
        mu = -1 if arity % 2 else 1
        for indices in combinations(range(r), arity):
            least_prime = prime_support[min(indices)]
            weight = mu * prime_weight(least_prime)
            for degree in range(arity):
                coefficients[degree] += weight * comb(arity - 1, degree)
    return coefficients


def ordered_factor_coefficients(
    prime_support: list[int],
    prime_weight,
) -> list[int]:
    """Coefficients of -sum_k (-z)^(k-1) f(P_k(n))."""
    descending = prime_support[::-1]
    return [
        (-1) ** (degree + 1) * prime_weight(prime)
        for degree, prime in enumerate(descending)
    ]


def divisor_arity_jets(
    prime_support: list[int],
    prime_weight,
) -> list[int]:
    """j_m=sum_{omega(d)=m+1}mu(d)f(p1(d))."""
    r = len(prime_support)
    jets: list[int] = []
    for m in range(r):
        total = 0
        arity = m + 1
        mu = -1 if arity % 2 else 1
        for indices in combinations(range(r), arity):
            total += mu * prime_weight(prime_support[min(indices)])
        jets.append(total)
    return jets


def ordered_to_jets(ordered: list[int]) -> list[int]:
    """j_m=(-1)^(m+1) sum_{k>=m} C(k,m)u_k."""
    r = len(ordered)
    return [
        (-1) ** (m + 1)
        * sum(comb(k, m) * ordered[k] for k in range(m, r))
        for m in range(r)
    ]


def jets_to_ordered(jets: list[int]) -> list[int]:
    """u_k=(-1)^(k+1) sum_{m>=k} C(m,k)j_m."""
    r = len(jets)
    return [
        (-1) ** (k + 1)
        * sum(comb(m, k) * jets[m] for m in range(k, r))
        for k in range(r)
    ]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows = len(a)
    middle = len(b)
    cols = len(b[0]) if b else 0
    return [
        [sum(a[i][k] * b[k][j] for k in range(middle)) for j in range(cols)]
        for i in range(rows)
    ]


def check_pascal_inverse(max_rank: int = 12) -> None:
    for rank in range(1, max_rank + 1):
        p = [
            [comb(k, m) if m <= k else 0 for k in range(rank)]
            for m in range(rank)
        ]
        p_inv = [
            [((-1) ** (k - m)) * comb(k, m) if m <= k else 0 for k in range(rank)]
            for m in range(rank)
        ]
        product = matmul(p, p_inv)
        identity = [
            [1 if i == j else 0 for j in range(rank)]
            for i in range(rank)
        ]
        assert product == identity


def check_local_alladi_identities(max_rank: int = 9) -> None:
    support = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    prime_weight = lambda p: p * p + 3 * p + 1
    for rank in range(1, max_rank + 1):
        primes = support[:rank]
        assert collective_alladi_coefficients(primes, prime_weight) == (
            ordered_factor_coefficients(primes, prime_weight)
        )

        ordered = [prime_weight(p) for p in primes[::-1]]
        jets = divisor_arity_jets(primes, prime_weight)
        assert jets == ordered_to_jets(ordered)
        assert jets_to_ordered(jets) == ordered


def check_global_tables(limit: int = 600) -> None:
    prime_weight = lambda p: p + 2
    primes = primes_up_to(limit)

    # Exact averaged Hardy/Parseval identity.
    left_energy = 0
    for n in range(2, limit + 1):
        coefficients = ordered_factor_coefficients(
            distinct_prime_factors(n),
            prime_weight,
        )
        left_energy += sum(value * value for value in coefficients)

    right_energy = sum(
        prime_weight(p) ** 2 * (limit // p)
        for p in primes
    )
    assert left_energy == right_energy

    # Ordered-prime vertex, edge and terminal tables.
    vertex: defaultdict[tuple[int, int], int] = defaultdict(int)
    edge: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    terminal: defaultdict[tuple[int, int], int] = defaultdict(int)
    direct_source = 0

    for n in range(2, limit + 1):
        ordered_primes = distinct_prime_factors(n)[::-1]
        rank = len(ordered_primes)
        direct_source += sum(prime_weight(p) for p in ordered_primes)

        for k, p in enumerate(ordered_primes, start=1):
            vertex[k, p] += 1
        for k in range(1, rank):
            edge[k, ordered_primes[k - 1], ordered_primes[k]] += 1
        terminal[rank, ordered_primes[-1]] += 1

    # Column conservation and the support light cone p^k <= X.
    column_total: defaultdict[int, int] = defaultdict(int)
    for (k, p), count in vertex.items():
        assert count > 0
        assert p**k <= limit
        column_total[p] += count
    for p in primes:
        assert column_total[p] == limit // p

    # Path continuity.
    incoming: defaultdict[tuple[int, int], int] = defaultdict(int)
    outgoing: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (k, p, q), count in edge.items():
        assert p > q
        outgoing[k, p] += count
        incoming[k + 1, q] += count

    for (k, p), count in vertex.items():
        if k >= 2:
            assert incoming[k, p] == count
        assert outgoing[k, p] + terminal.get((k, p), 0) == count

    # Exact path integration by parts.
    path_source = sum(
        k * prime_weight(p) * count
        for (k, p), count in terminal.items()
    )
    path_source += sum(
        k * (prime_weight(p) - prime_weight(q)) * count
        for (k, p, q), count in edge.items()
    )
    assert path_source == direct_source


def main() -> None:
    check_pascal_inverse()
    check_local_alladi_identities()
    check_global_tables()
    print("all exact Alladi-Pascal / ordered-prime BRC checks passed")


if __name__ == "__main__":
    main()
