#!/usr/bin/env python3
"""Exact finite checks for the Kubilius suffix / rough-prefix shift BRC.

The script verifies finite algebraic identities only:

1. global ordered-factor polynomial = rough-prefix monomial shift times
   the suffix-reindexed polynomial;
2. the corresponding factorial-jet binomial convolution;
3. exact expectation of the suffix Alladi polynomial in the independent
   Bernoulli(1/p) model;
4. closed formulas for independent ordered-prime vertex, edge and terminal
   carriers;
5. continuity, column conservation and path integration by parts.

It does not numerically verify the asymptotic Kubilius total-variation theorem
and is not evidence for RH.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def distinct_prime_factors(n: int) -> list[int]:
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


def polynomial_multiply(a, b):
    output = [0 for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i + j] += x * y
    return output


def ordered_alladi_coefficients(weights_descending):
    """Coefficients of -sum_j (-z)^j u_j."""
    return [
        (-1) ** (degree + 1) * weight
        for degree, weight in enumerate(weights_descending)
    ]


def factorial_jets_at_minus_one(coefficients):
    """Return A^(m)(-1)/m! for all possible m."""
    rank = len(coefficients)
    return [
        sum(
            coefficients[degree]
            * comb(degree, m)
            * (-1) ** (degree - m)
            for degree in range(m, rank)
        )
        for m in range(rank)
    ]


def check_prefix_shift(limit: int = 500) -> None:
    for n in range(2, limit + 1):
        ordered_primes = distinct_prime_factors(n)[::-1]
        for cutoff in (3, 5, 7, 11, 19):
            high_depth = sum(p > cutoff for p in ordered_primes)
            global_weights = [
                p + 1 if p <= cutoff else 0
                for p in ordered_primes
            ]
            suffix_weights = [
                p + 1 for p in ordered_primes if p <= cutoff
            ]

            global_poly = ordered_alladi_coefficients(global_weights)
            while global_poly and global_poly[-1] == 0:
                global_poly.pop()

            suffix_poly = ordered_alladi_coefficients(suffix_weights)
            if suffix_poly:
                monomial = [0] * high_depth + [(-1) ** high_depth]
                shifted = polynomial_multiply(monomial, suffix_poly)
            else:
                shifted = []
            assert global_poly == shifted

            global_jets = factorial_jets_at_minus_one(global_poly)
            suffix_jets = factorial_jets_at_minus_one(suffix_poly)
            predicted = []
            for m in range(len(global_poly)):
                value = 0
                for a in range(min(high_depth, m) + 1):
                    if m - a < len(suffix_jets):
                        value += (
                            (-1) ** a
                            * comb(high_depth, a)
                            * suffix_jets[m - a]
                        )
                predicted.append(value)
            assert global_jets == predicted

            # Multiplication by a monomial is an exact H^2 isometry.
            assert sum(x * x for x in global_poly) == sum(
                x * x for x in suffix_poly
            )


def collective_alladi_coefficients(prime_support, prime_weight):
    rank = len(prime_support)
    coefficients = [0] * rank
    for arity in range(1, rank + 1):
        mu = -1 if arity % 2 else 1
        for indices in combinations(range(rank), arity):
            least_prime = prime_support[min(indices)]
            contribution = mu * prime_weight(least_prime)
            for degree in range(arity):
                coefficients[degree] += (
                    contribution * comb(arity - 1, degree)
                )
    return coefficients


def bernoulli_polynomial(primes):
    """Product of ((p-1)/p + z/p)."""
    poly = [Fraction(1)]
    for p in primes:
        poly = polynomial_multiply(
            poly,
            [Fraction(p - 1, p), Fraction(1, p)],
        )
    return poly


def enumerate_expected_suffix_alladi(primes, prime_weight):
    output = [Fraction(0)] * len(primes)
    for bits in product((0, 1), repeat=len(primes)):
        probability = Fraction(1)
        support = []
        for p, bit in zip(primes, bits):
            if bit:
                probability *= Fraction(1, p)
                support.append(p)
            else:
                probability *= Fraction(p - 1, p)
        if support:
            coefficients = collective_alladi_coefficients(
                support,
                prime_weight,
            )
            for degree, coefficient in enumerate(coefficients):
                output[degree] += probability * coefficient
    return output


def product_expected_suffix_alladi(primes, prime_weight):
    """-sum_p f(p)/p prod_{q>p}(1-(1+z)/q)."""
    output = [Fraction(0)] * len(primes)
    for index, p in enumerate(primes):
        poly = [Fraction(1)]
        for q in primes[index + 1 :]:
            poly = polynomial_multiply(
                poly,
                [Fraction(q - 1, q), Fraction(-1, q)],
            )
        scale = -Fraction(prime_weight(p), p)
        for degree, coefficient in enumerate(poly):
            output[degree] += scale * coefficient
    return output


def enumerate_independent_path_tables(primes):
    vertex = defaultdict(Fraction)
    edge = defaultdict(Fraction)
    terminal = defaultdict(Fraction)

    for bits in product((0, 1), repeat=len(primes)):
        probability = Fraction(1)
        support = []
        for p, bit in zip(primes, bits):
            if bit:
                probability *= Fraction(1, p)
                support.append(p)
            else:
                probability *= Fraction(p - 1, p)

        ordered = support[::-1]
        rank = len(ordered)
        for k, p in enumerate(ordered, start=1):
            vertex[k, p] += probability
        for k in range(1, rank):
            edge[k, ordered[k - 1], ordered[k]] += probability
        if rank:
            terminal[rank, ordered[-1]] += probability

    return vertex, edge, terminal


def formula_independent_path_tables(primes):
    vertex = defaultdict(Fraction)
    edge = defaultdict(Fraction)
    terminal = defaultdict(Fraction)

    for index, p in enumerate(primes):
        larger = primes[index + 1 :]
        larger_count_poly = bernoulli_polynomial(larger)

        for degree, coefficient in enumerate(larger_count_poly):
            vertex[degree + 1, p] = Fraction(1, p) * coefficient

        no_smaller = Fraction(1)
        for q in primes[:index]:
            no_smaller *= Fraction(q - 1, q)
        for degree, coefficient in enumerate(larger_count_poly):
            terminal[degree + 1, p] = (
                Fraction(1, p) * no_smaller * coefficient
            )

        for q_index, q in enumerate(primes[:index]):
            no_between = Fraction(1)
            for middle in primes[q_index + 1 : index]:
                no_between *= Fraction(middle - 1, middle)
            for degree, coefficient in enumerate(larger_count_poly):
                edge[degree + 1, p, q] = (
                    Fraction(1, p * q)
                    * no_between
                    * coefficient
                )

    return vertex, edge, terminal


def check_independent_carrier() -> None:
    primes = [2, 3, 5, 7, 11]
    prime_weight = lambda p: p + 1

    assert enumerate_expected_suffix_alladi(
        primes,
        prime_weight,
    ) == product_expected_suffix_alladi(
        primes,
        prime_weight,
    )

    vertex, edge, terminal = enumerate_independent_path_tables(primes)
    vertex_formula, edge_formula, terminal_formula = (
        formula_independent_path_tables(primes)
    )
    assert vertex == vertex_formula
    assert edge == edge_formula
    assert terminal == terminal_formula

    # Column conservation.
    for p in primes:
        assert sum(
            probability
            for (k, q), probability in vertex.items()
            if q == p
        ) == Fraction(1, p)

    # Continuity.
    incoming = defaultdict(Fraction)
    outgoing = defaultdict(Fraction)
    for (k, p, q), probability in edge.items():
        assert p > q
        outgoing[k, p] += probability
        incoming[k + 1, q] += probability

    for (k, p), probability in vertex.items():
        if k >= 2:
            assert incoming[k, p] == probability
        assert (
            outgoing[k, p] + terminal.get((k, p), Fraction(0))
            == probability
        )

    # Expected path integration-by-parts source equals sum_p f(p)/p.
    path_source = sum(
        k * prime_weight(p) * probability
        for (k, p), probability in terminal.items()
    )
    path_source += sum(
        k * (prime_weight(p) - prime_weight(q)) * probability
        for (k, p, q), probability in edge.items()
    )
    assert path_source == sum(
        Fraction(prime_weight(p), p)
        for p in primes
    )


def main() -> None:
    check_prefix_shift()
    check_independent_carrier()
    print("all exact Kubilius suffix / prefix-shift BRC checks passed")


if __name__ == "__main__":
    main()
