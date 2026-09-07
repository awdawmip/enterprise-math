#!/usr/bin/env python3
"""Finite diagnostic for the rough-arm probability law and Gamma residue.

For the positive layers P_h(u) of

    R_(1-epsilon)(u) = sum_h P_h(u) epsilon^h,

the exact identities are

    sum_h P_h(u) = 1,
    E H_u = log u  (u>=1),

and the generalized Dickman asymptotic is the mod-Poisson profile

    E epsilon^H_u
      ~ u^(epsilon-1) exp(gamma(1-epsilon))/Gamma(epsilon).

The script integrates the exact delay system, checks normalization and the
first two moments, prints fixed-epsilon profile diagnostics, and verifies the
finite Gamma-log cumulant residue exp(-sum_{m=2}^M zeta(m)/m) ~ 1/M.

This is a numerical regression only, not an asymptotic proof and not evidence
for the Riemann hypothesis.
"""

from __future__ import annotations

from math import exp, gamma, lgamma, log, pi

EULER_GAMMA = 0.5772156649015328606


def integrate_layers(
    max_u: float = 80.0,
    step: float = 0.002,
    max_layer: int = 40,
) -> list[list[float]]:
    count = int(round(max_u / step))
    delay = int(round(1.0 / step))
    assert abs(delay * step - 1.0) < 1e-12

    layers = [[0.0] * (count + 1) for _ in range(max_layer + 1)]
    for index in range(delay + 1):
        layers[0][index] = 1.0

    for index in range(delay, count):
        u0 = index * step
        u1 = (index + 1) * step
        old_delay = index - delay
        new_delay = index + 1 - delay

        for layer in range(max_layer + 1):
            old_in = (
                layers[layer - 1][old_delay] if layer > 0 else 0.0
            )
            new_in = (
                layers[layer - 1][new_delay] if layer > 0 else 0.0
            )
            old_derivative = (
                -layers[layer][old_delay] + old_in
            ) / u0
            new_derivative = (
                -layers[layer][new_delay] + new_in
            ) / u1
            layers[layer][index + 1] = (
                layers[layer][index]
                + 0.5 * step * (old_derivative + new_derivative)
            )

    return layers


def values_at(
    layers: list[list[float]], u: float, step: float
) -> list[float]:
    index = int(round(u / step))
    return [layer[index] for layer in layers]


def dilogarithm_series(value: float, terms: int = 200_000) -> float:
    """Li_2(value) for 0<=value<1, sufficient for finite diagnostics."""
    total = 0.0
    power = value
    for index in range(1, terms + 1):
        contribution = power / (index * index)
        total += contribution
        power *= value
        if abs(contribution) < 1e-16:
            break
    return total


def exact_second_factorial_moment(u: float) -> float:
    if u < 2.0:
        return 0.0
    return (
        log(u) * log(u - 1.0)
        - dilogarithm_series(1.0 - 1.0 / u)
        + dilogarithm_series(1.0 / u)
    )


def verify_probability_and_moments(
    layers: list[list[float]], step: float
) -> None:
    for u in (2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        values = values_at(layers, u, step)
        mass = sum(values)
        mean = sum(index * value for index, value in enumerate(values))
        factorial_second = sum(
            index * (index - 1) * value
            for index, value in enumerate(values)
        )
        exact_second = exact_second_factorial_moment(u)

        assert abs(mass - 1.0) < 5e-4
        assert abs(mean - log(u)) < 5e-3
        assert abs(factorial_second - exact_second) < 2e-2

        variance = factorial_second + mean - mean * mean
        if u >= 20.0:
            target = log(u) - pi * pi / 6.0
            assert abs(variance - target) < 0.25


def riemann_zeta_integer(order: int, cutoff: int = 500_000) -> float:
    assert order >= 2
    total = 1.0
    for integer in range(2, cutoff + 1):
        term = integer ** (-order)
        total += term
        if term < 1e-17:
            break
    if order == 2:
        total += 1.0 / cutoff
    return total


def verify_gamma_log_partial_residue() -> None:
    running = 0.0
    products = []
    for order in range(2, 161):
        running += riemann_zeta_integer(order) / order
        if order in (10, 20, 40, 80, 160):
            products.append((order, order * exp(-running)))

    assert abs(products[-1][1] - 1.0) < 0.03
    assert abs(products[-1][1] - 1.0) < abs(products[0][1] - 1.0)

    print("M      M*exp(-sum_(m=2)^M zeta(m)/m)")
    for order, value in products:
        print(f"{order:<6d} {value:.12f}")


def print_mod_poisson_table(
    layers: list[list[float]], step: float
) -> None:
    print("\nu      eps    exact PGF        mod-Poisson      ratio")
    for u in (10.0, 20.0, 40.0, 80.0):
        values = values_at(layers, u, step)
        for epsilon in (0.25, 0.50, 0.75):
            exact = sum(
                epsilon**index * value
                for index, value in enumerate(values)
            )
            residue = exp(
                EULER_GAMMA * (1.0 - epsilon) - lgamma(epsilon)
            )
            model = u ** (epsilon - 1.0) * residue
            print(
                f"{u:<6.1f} {epsilon:<6.2f} {exact:<16.10e} "
                f"{model:<16.10e} {exact / model:.8f}"
            )


def main() -> None:
    step = 0.002
    layers = integrate_layers(step=step)
    verify_probability_and_moments(layers, step)
    verify_gamma_log_partial_residue()
    print_mod_poisson_table(layers, step)
    print("rough-arm mod-Poisson regression passed")


if __name__ == "__main__":
    main()
