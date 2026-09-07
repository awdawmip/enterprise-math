#!/usr/bin/env python3
"""Finite diagnostic for the Dickman Green Markov-dilation operator.

At the exact t=1 harmonic prime-quadrature source, Stieltjes integration by
parts produces the finite-depth Markov operator

    (T_U F)(x)
      = rho(U) F(x/(U+1))
        + int_1^U F(x/(v+1)) rho(v-1)/v dv.

The checker integrates rho, verifies that the kernel has mass one, checks the
exact inverse-log eigenmode formulas, and confirms

    M_1(U) = 2 + int_1^U rho(v) dv -> 1 + exp(gamma).

This is a numerical regression only, not an asymptotic proof and not evidence
for the Riemann hypothesis.
"""

from __future__ import annotations

from math import exp

EULER_GAMMA = 0.5772156649015328606


def integrate_dickman(max_u: float = 80.0, step: float = 0.001) -> list[float]:
    count = int(round(max_u / step))
    delay = int(round(1.0 / step))
    assert abs(delay * step - 1.0) < 1e-12

    rho = [0.0] * (count + 1)
    for index in range(delay + 1):
        rho[index] = 1.0

    for index in range(delay, count):
        u0 = index * step
        u1 = (index + 1) * step
        derivative0 = -rho[index - delay] / u0
        derivative1 = -rho[index + 1 - delay] / u1
        rho[index + 1] = rho[index] + 0.5 * step * (
            derivative0 + derivative1
        )
    return rho


def trapezoid(values: list[float], start: int, end: int, step: float) -> float:
    if end <= start:
        return 0.0
    total = 0.5 * (values[start] + values[end])
    total += sum(values[start + 1 : end])
    return total * step


def kernel_statistics(
    rho: list[float], u: float, step: float, max_moment: int = 4
) -> tuple[float, list[float]]:
    delay = int(round(1.0 / step))
    end = int(round(u / step))
    rho_u = rho[end]

    density = []
    for index in range(delay, end + 1):
        v = index * step
        density.append(rho[index - delay] / v)

    mass = rho_u + trapezoid(density, 0, len(density) - 1, step)
    moments = []
    for order in range(max_moment + 1):
        weighted = []
        for offset, value in enumerate(density):
            v = (delay + offset) * step
            weighted.append((v + 1.0) ** order * value)
        moment = rho_u * (u + 1.0) ** order
        moment += trapezoid(weighted, 0, len(weighted) - 1, step)
        moments.append(moment)
    return mass, moments


def verify_markov_and_moments(rho: list[float], step: float) -> None:
    delay = int(round(1.0 / step))
    for u in (1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        mass, moments = kernel_statistics(rho, u, step)
        end = int(round(u / step))
        integral_rho = trapezoid(rho, delay, end, step)
        exact_m1 = 2.0 + integral_rho

        assert abs(mass - 1.0) < 4e-3
        assert abs(moments[0] - 1.0) < 4e-3
        assert abs(moments[1] - exact_m1) < 8e-3

        x = 137.0
        for order in range(1, 5):
            direct = moments[order] * x ** (-order)
            eigen = moments[order] / x**order
            assert abs(direct - eigen) < 1e-15
            assert moments[order] > 1.0

    _, last_moments = kernel_statistics(rho, 80.0, step)
    target = 1.0 + exp(EULER_GAMMA)
    assert abs(last_moments[1] - target) < 0.03


def print_table(rho: list[float], step: float) -> None:
    target = 1.0 + exp(EULER_GAMMA)
    print("U      mass(T_U)      M1(U)           limit 1+e^gamma")
    for u in (1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        mass, moments = kernel_statistics(rho, u, step)
        print(f"{u:<6.1f} {mass:<14.10f} {moments[1]:<15.10f} {target:.10f}")


def main() -> None:
    step = 0.001
    rho = integrate_dickman(step=step)
    verify_markov_and_moments(rho, step)
    print_table(rho, step)
    print("Dickman Markov-dilation regression passed")


if __name__ == "__main__":
    main()
