"""Numerical diagnostic for the exact P017 P2 linear-sieve parity functional.

The proof is in
`docs/P017_P2_CHEN_CARRY_BRIDGE_SUPPLEMENT_02_20260824.md`.
This script reconstructs the standard dimension-one sieve functions from their
differential-delay equations and checks the predicted sign/scalar identities.
It is supporting numerical evidence, not the proof.
"""

from __future__ import annotations

from math import exp, log


EULER_GAMMA = 0.5772156649015328606
TWO_E_GAMMA = 2.0 * exp(EULER_GAMMA)


def build_linear_sieve_functions(
    step: float = 0.0002,
    maximum: float = 9.0,
) -> tuple[list[float], list[float], list[float]]:
    if not (0.0 < step <= 0.01 and maximum >= 5.0):
        raise ValueError("invalid grid")
    count = int(round(maximum / step)) + 1
    grid = [index * step for index in range(count)]
    lower = [0.0] * count
    upper = [0.0] * count
    lower_product = [0.0] * count
    upper_product = [0.0] * count

    def index_of(value: float) -> int:
        return int(round(value / step))

    def interpolate(values: list[float], value: float) -> float:
        if value <= 0.0:
            return values[0]
        position = value / step
        left = int(position)
        if left >= len(values) - 1:
            return values[-1]
        fraction = position - left
        return values[left] * (1.0 - fraction) + values[left + 1] * fraction

    for index, value in enumerate(grid):
        if 1.0 <= value <= 3.0:
            upper[index] = TWO_E_GAMMA / value
            upper_product[index] = TWO_E_GAMMA

    start_two = index_of(2.0)
    for index in range(start_two + 1, count):
        value = grid[index]
        previous = grid[index - 1]
        lower_product[index] = lower_product[index - 1] + 0.5 * step * (
            interpolate(upper, previous - 1.0)
            + interpolate(upper, value - 1.0)
        )
        lower[index] = lower_product[index] / value

        if value > 3.0:
            upper_product[index] = upper_product[index - 1] + 0.5 * step * (
                interpolate(lower, previous - 1.0)
                + interpolate(lower, value - 1.0)
            )
            upper[index] = upper_product[index] / value

    return grid, lower, upper


def interpolate(grid: list[float], values: list[float], value: float) -> float:
    step = grid[1] - grid[0]
    position = value / step
    left = int(position)
    if left >= len(values) - 1:
        return values[-1]
    fraction = position - left
    return values[left] * (1.0 - fraction) + values[left + 1] * fraction


def trapezoid(values: list[float], step: float) -> float:
    if len(values) < 2:
        return 0.0
    return step * (sum(values) - 0.5 * values[0] - 0.5 * values[-1])


def parity_functional(
    s: float,
    grid: list[float],
    lower: list[float],
    upper: list[float],
    integration_step: float = 0.0005,
) -> float:
    if not (2.0 < s < grid[-1]):
        raise ValueError("s outside the computed grid")
    pieces = max(2, int(round((s - 2.0) / integration_step)) + 1)
    actual_step = (s - 2.0) / (pieces - 1)
    integrand: list[float] = []
    for index in range(pieces):
        u = 1.0 + index * actual_step
        integrand.append(interpolate(grid, upper, s - u) / u)
    return interpolate(grid, lower, s) - 0.5 * trapezoid(integrand, actual_step)


def affine_functional_direct(
    s: float,
    t: float,
    grid: list[float],
    lower: list[float],
    upper: list[float],
    integration_step: float = 0.0005,
) -> float:
    if not (0.0 <= t <= 1.0):
        raise ValueError("t must lie in [0,1]")
    pieces = max(2, int(round((s - 2.0) / integration_step)) + 1)
    actual_step = (s - 2.0) / (pieces - 1)
    integrand: list[float] = []
    for index in range(pieces):
        u = 1.0 + index * actual_step
        penalty = (1.0 + t) / 2.0 - t * u / s
        integrand.append(
            penalty * interpolate(grid, upper, s - u) / u
        )
    return interpolate(grid, lower, s) - trapezoid(integrand, actual_step)


def verify() -> None:
    grid, lower, upper = build_linear_sieve_functions()

    # Basic reconstruction checks.
    assert abs(interpolate(grid, lower, 3.0) - TWO_E_GAMMA * log(2.0) / 3.0) < 2e-6
    assert abs(interpolate(grid, lower, 4.0) - TWO_E_GAMMA * log(3.0) / 4.0) < 2e-6

    equality_samples = (2.1, 2.5, 3.0, 3.5, 4.0)
    strict_samples = (4.25, 5.0, 6.0, 7.0, 8.0)

    for s in equality_samples:
        assert abs(parity_functional(s, grid, lower, upper)) < 2e-6

    for s in strict_samples:
        assert parity_functional(s, grid, lower, upper) < -1e-5

    for s in equality_samples + strict_samples:
        base = parity_functional(s, grid, lower, upper)
        for t in (0.0, 0.2, 0.5, 0.8, 1.0):
            direct = affine_functional_direct(s, t, grid, lower, upper)
            assert abs(direct - (1.0 + t) * base) < 3e-6


if __name__ == "__main__":
    verify()
    print("P017 P2 linear-sieve parity functional diagnostic: PASS")
