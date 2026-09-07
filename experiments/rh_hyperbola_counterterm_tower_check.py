#!/usr/bin/env python3
"""Finite pilot for the fixed-order hyperbola-budget counterterm tower.

For uniform n<=X, Y=floor((log X)^2), and f(q)=sqrt(q), define

    C_X(t)=Cov((1-t)^H, A_suffix(t-1)),

where H counts distinct prime factors above Y and A_suffix is the collective
Alladi polynomial on prime factors at most Y.  The script computes the first
three Taylor coefficients directly from the integer population and compares
those values with the fixed-order continuum counterterm

    (-1)^m A_X L_X^(m-1)/(m-1)!,
    A_X=2 sqrt(Y)/log X,
    L_X=log(log X/log Y).

The asymptotic argument is in the accompanying research note.  This finite
pilot is diagnostic only and is not evidence for RH.
"""

from __future__ import annotations

from math import comb, factorial, log, sqrt


def smallest_prime_factor_sieve(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, int(limit**0.5) + 1):
        if spf[prime] == prime:
            for multiple in range(prime * prime, limit + 1, prime):
                if spf[multiple] == multiple:
                    spf[multiple] = prime
    return spf


def distinct_prime_factors(integer: int, spf: list[int]) -> list[int]:
    factors = []
    while integer > 1:
        prime = spf[integer]
        factors.append(prime)
        while integer % prime == 0:
            integer //= prime
    return factors


def covariance_coefficients(limit: int, order: int = 3):
    cutoff = int(log(limit) ** 2)
    spf = smallest_prime_factor_sieve(limit)

    rough_phase_sums = [0.0] * (order + 1)
    suffix_jet_sums = [0.0] * (order + 1)
    product_sums = [0.0] * (order + 1)

    for integer in range(1, limit + 1):
        factors = distinct_prime_factors(integer, spf)
        rough_depth = sum(prime > cutoff for prime in factors)
        small_descending = [
            prime for prime in factors[::-1] if prime <= cutoff
        ]

        rough_phase = [
            (-1) ** degree * comb(rough_depth, degree)
            for degree in range(min(rough_depth, order) + 1)
        ]

        suffix_jets = [0.0] * (order + 1)
        for position, prime in enumerate(small_descending, start=1):
            for degree in range(min(position - 1, order) + 1):
                suffix_jets[degree] += (
                    (-1) ** (degree + 1)
                    * comb(position - 1, degree)
                    * sqrt(prime)
                )

        for degree, value in enumerate(rough_phase):
            rough_phase_sums[degree] += value
        for degree, value in enumerate(suffix_jets):
            suffix_jet_sums[degree] += value
        for total_degree in range(order + 1):
            product_sums[total_degree] += sum(
                rough_phase[rough_degree]
                * suffix_jets[total_degree - rough_degree]
                for rough_degree in range(total_degree + 1)
                if rough_degree < len(rough_phase)
            )

    rough_means = [value / limit for value in rough_phase_sums]
    suffix_means = [value / limit for value in suffix_jet_sums]
    product_means = [value / limit for value in product_sums]

    covariance = []
    for degree in range(order + 1):
        covariance.append(
            product_means[degree]
            - sum(
                rough_means[index] * suffix_means[degree - index]
                for index in range(degree + 1)
            )
        )
    return cutoff, covariance


def continuum_coefficients(limit: int, order: int = 3):
    cutoff = int(log(limit) ** 2)
    amplitude = 2.0 * sqrt(cutoff) / log(limit)
    depth = log(log(limit) / log(cutoff))
    return [
        0.0,
        *[
            (-1) ** degree
            * amplitude
            * depth ** (degree - 1)
            / factorial(degree - 1)
            for degree in range(1, order + 1)
        ],
    ]


def main() -> None:
    print("X          Y        c1              c2              c3")
    last_first_error = None
    for limit in (10_000, 100_000, 1_000_000):
        cutoff, observed = covariance_coefficients(limit)
        predicted = continuum_coefficients(limit)

        assert abs(observed[0]) < 1e-9
        assert observed[1] < 0
        assert observed[2] > 0
        assert observed[3] < 0

        first_error = abs(observed[1] - predicted[1])
        if last_first_error is not None:
            assert first_error < last_first_error
        last_first_error = first_error

        print(
            f"{limit:<10d} {cutoff:<8d} "
            f"{observed[1]: .10f}  "
            f"{observed[2]: .10f}  "
            f"{observed[3]: .10f}"
        )
        print(
            " " * 20
            + "model: "
            + "  ".join(
                f"{predicted[degree]: .10f}" for degree in (1, 2, 3)
            )
        )

    assert last_first_error is not None and last_first_error < 0.1
    print("finite coefficient pilot is consistent with the counterterm tower")


if __name__ == "__main__":
    main()
