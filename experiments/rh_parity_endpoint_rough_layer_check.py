#!/usr/bin/env python3
"""Finite diagnostic for the parity-endpoint rough-layer decomposition.

For the generalized Dickman carrier R_t(u), put epsilon=1-t.  The exact
positive layer decomposition is

    R_(1-epsilon)(u) = sum_{h>=0} epsilon^h P_h(u),

where P_0=rho and

    Laplace(P_h) = exp(-E1(s))/s * E1(s)^h/h!.

Equivalently P_h = rho * k^{*h}/h!, k(u)=1_{u>=1}/u.

The checker integrates the exact delay system

    u P_0' = -P_0(u-1),
    u P_h' = -P_h(u-1)+P_(h-1)(u-1),

and verifies the first interval, positivity, the endpoint leakage inequality,
and numerical approach of u P_1(u) to exp(gamma).

This is a numerical regression only, not an asymptotic proof and not evidence
for the Riemann hypothesis.
"""

from __future__ import annotations

from math import exp, log

EULER_GAMMA = 0.5772156649015328606


def integrate_layers(
    max_u: float = 80.0,
    step: float = 0.002,
    max_layer: int = 24,
) -> tuple[list[list[float]], int]:
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

        old_derivative = [0.0] * (max_layer + 1)
        new_derivative = [0.0] * (max_layer + 1)

        old_derivative[0] = -layers[0][old_delay] / u0
        new_derivative[0] = -layers[0][new_delay] / u1

        for layer in range(1, max_layer + 1):
            old_derivative[layer] = (
                -layers[layer][old_delay]
                + layers[layer - 1][old_delay]
            ) / u0
            new_derivative[layer] = (
                -layers[layer][new_delay]
                + layers[layer - 1][new_delay]
            ) / u1

        for layer in range(max_layer + 1):
            layers[layer][index + 1] = (
                layers[layer][index]
                + 0.5 * step
                * (old_derivative[layer] + new_derivative[layer])
            )

    return layers, delay


def at(layers: list[list[float]], u: float, step: float) -> list[float]:
    index = int(round(u / step))
    return [layer[index] for layer in layers]


def verify_first_interval(
    layers: list[list[float]],
    step: float,
) -> None:
    for u in (1.1, 1.25, 1.5, 1.75, 2.0):
        values = at(layers, u, step)
        assert abs(values[0] - (1.0 - log(u))) < 3e-3
        assert abs(values[1] - log(u)) < 3e-3
        assert max(abs(value) for value in values[2:]) < 3e-3


def verify_positivity_and_leakage(
    layers: list[list[float]],
    step: float,
) -> None:
    for u in (2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        values = at(layers, u, step)
        assert min(values) > -5e-7
        rho = values[0]
        for epsilon in (0.001, 0.01, 0.05, 0.1):
            regularized = sum(
                epsilon**layer * value
                for layer, value in enumerate(values)
            )
            assert regularized + 1e-12 >= rho + epsilon * values[1]


def verify_one_arm_asymptotic(
    layers: list[list[float]],
    step: float,
) -> None:
    target = exp(EULER_GAMMA)
    errors = []
    for u in (10.0, 20.0, 40.0, 80.0):
        one_arm = at(layers, u, step)[1]
        errors.append(abs(u * one_arm - target))
    assert errors[-1] < 0.25
    assert errors[-1] < errors[0]


def print_boundary_layer_table(
    layers: list[list[float]],
    step: float,
) -> None:
    target_mass = exp(EULER_GAMMA)
    print("u      u*P1(u)       target e^gamma")
    for u in (5.0, 10.0, 20.0, 40.0, 80.0):
        one_arm = at(layers, u, step)[1]
        print(f"{u:<6.1f} {u * one_arm:<14.10f} {target_mass:.10f}")

    print("\ntau    u     u log(u) [R_(1-tau/logu)-rho]    target")
    for tau in (0.5, 1.0, 2.0):
        target = target_mass * tau * exp(tau)
        for u in (20.0, 40.0, 80.0):
            epsilon = tau / log(u)
            values = at(layers, u, step)
            difference = sum(
                epsilon**layer * values[layer]
                for layer in range(1, len(values))
            )
            scaled = u * log(u) * difference
            print(f"{tau:<6.2f} {u:<5.1f} {scaled:<31.10f} {target:.10f}")


def main() -> None:
    step = 0.002
    layers, _ = integrate_layers(step=step)
    verify_first_interval(layers, step)
    verify_positivity_and_leakage(layers, step)
    verify_one_arm_asymptotic(layers, step)
    print_boundary_layer_table(layers, step)
    print("parity-endpoint rough-layer regression passed")


if __name__ == "__main__":
    main()
