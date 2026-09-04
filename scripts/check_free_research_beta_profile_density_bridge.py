#!/usr/bin/env python3
"""Exact finite checks for the V14 clipped-Beta density bridge.

The analytic input |A(x)-log x| <= C is proved in the research note. This
checker verifies the algebraic identities that do not involve real-log
approximation:
  * pair-energy / mass-variance identity;
  * endpoint-disintegration (law of total variance);
  * positive mixture-variance identity;
  * monotonicity under pointwise measure domination on finite samples;
  * the K=4 clipped-Beta mass and 5/8 mean coefficient;
  * the affine cube-root recurrence closed form.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

Q = Fraction


def qsum(values: Iterable[Q]) -> Q:
    return sum(values, Q(0))


def mass(weights: Sequence[Q]) -> Q:
    return qsum(weights)


def mean(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal length")
    total = mass(weights)
    if total <= 0:
        raise ValueError("positive total mass required")
    return qsum(w * x for w, x in zip(weights, values)) / total


def mass_variance(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    """Unnormalized variance: inf_c sum_i w_i (x_i-c)^2."""
    total = mass(weights)
    if total == 0:
        return Q(0)
    center = mean(weights, values)
    return qsum(w * (x - center) ** 2 for w, x in zip(weights, values))


def pair_energy(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    return qsum(
        wi * wj * (xi - xj) ** 2
        for wi, xi in zip(weights, values)
        for wj, xj in zip(weights, values)
    )


def check_pair_identity() -> None:
    weights = [Q(1, 2), Q(3, 2), Q(5, 3), Q(7, 4)]
    values = [Q(2), Q(-1, 3), Q(7, 4), Q(-5, 2)]
    lhs = pair_energy(weights, values)
    rhs = 2 * mass(weights) * mass_variance(weights, values)
    assert lhs == rhs


def check_endpoint_disintegration() -> None:
    fiber_weights = [
        [Q(1), Q(2), Q(1, 2)],
        [Q(3), Q(1)],
        [Q(5, 4), Q(7, 3), Q(2)],
    ]
    fiber_values = [
        [Q(0), Q(3), Q(-1)],
        [Q(-2), Q(5)],
        [Q(4, 3), Q(-7, 5), Q(9, 2)],
    ]

    all_weights = [w for fiber in fiber_weights for w in fiber]
    all_values = [x for fiber in fiber_values for x in fiber]
    global_mean = mean(all_weights, all_values)

    within = qsum(
        mass_variance(weights, values)
        for weights, values in zip(fiber_weights, fiber_values)
    )
    between = qsum(
        mass(weights) * (mean(weights, values) - global_mean) ** 2
        for weights, values in zip(fiber_weights, fiber_values)
    )
    total = mass_variance(all_weights, all_values)

    assert total == within + between
    assert within <= total


def check_positive_mixture_identity() -> None:
    mu = [Q(2), Q(1), Q(0), Q(3, 2)]
    rho = [Q(1), Q(4), Q(3), Q(1, 2)]
    values = [Q(-1), Q(2), Q(5), Q(-7, 3)]
    nu = [a + b for a, b in zip(mu, rho)]

    m_mu = mass(mu)
    m_rho = mass(rho)
    lhs = mass_variance(nu, values)
    rhs = (
        mass_variance(mu, values)
        + mass_variance(rho, values)
        + m_mu
        * m_rho
        / (m_mu + m_rho)
        * (mean(mu, values) - mean(rho, values)) ** 2
    )
    assert lhs == rhs
    assert mass_variance(mu, values) <= lhs


def check_measure_domination() -> None:
    mu = [Q(1), Q(3, 2), Q(2), Q(1, 3)]
    nu = [Q(2), Q(2), Q(5, 2), Q(1)]
    values = [Q(-5), Q(2, 3), Q(7, 2), Q(1)]
    lam = Q(7, 5)

    assert all(a <= b for a, b in zip(mu, nu))
    assert mass_variance(mu, values) <= mass_variance(nu, values)
    scaled_nu = [lam * w for w in nu]
    assert mass_variance(scaled_nu, values) == lam * mass_variance(nu, values)


def clipped_beta(t: Q, length: Q, kappa: Q = Q(4)) -> Q:
    """K-clipped Beta profile max(t^2/2, L^2/(2K))."""
    if not (Q(0) <= t <= length):
        raise ValueError("0 <= t <= length required")
    if kappa < 1:
        raise ValueError("K >= 1 required")
    return max(t * t / 2, length * length / (2 * kappa))


def check_k4_profile() -> None:
    # For K=4 the clipping point is L/2.
    length = Q(12)
    floor = length * length / 8
    assert clipped_beta(Q(0), length) == floor
    assert clipped_beta(length / 2, length) == floor
    assert clipped_beta(length, length) == length * length / 2

    # Exact continuum mass:
    # floor * (L/2) + integral_{L/2}^L t^2/2 dt = (5/24)L^3.
    profile_mass = floor * (length / 2) + (
        length**3 - (length / 2) ** 3
    ) / 6
    assert profile_mass == Q(5, 24) * length**3

    # Three colors convert this branch-profile mass into mean coefficient 5/8.
    full_packet_lead = Q(9, 2) * length**3
    one_color_high_low_lead = Q(9, 2) * profile_mass
    total_mean_lead = 3 * one_color_high_low_lead
    assert total_mean_lead / full_packet_lead == Q(5, 8)

    # The profile-to-canonical pointwise condition number is exactly 4.
    samples = [Q(0), length / 4, length / 2, 3 * length / 4, length]
    profile_values = [clipped_beta(t, length) for t in samples]
    assert max(profile_values) / min(profile_values) == 4


def check_domination_absorbs_discrepancy() -> None:
    # Abstract atomwise form of
    # Q <= beta + err <= (1+delta) max(beta, floor).
    beta = [Q(0), Q(1, 8), Q(1, 2), Q(9, 8), Q(2)]
    floor = Q(1, 4)
    err_bound = Q(1, 10)
    profile = [max(b, floor) for b in beta]
    delta = err_bound / floor

    # Sample nonnegative actual masses within the analytic error interval.
    errors = [Q(1, 20), Q(1, 10), Q(0), Q(1, 25), Q(1, 12)]
    actual = [b + e for b, e in zip(beta, errors)]
    assert all(a <= (1 + delta) * p for a, p in zip(actual, profile))

    weights = [Q(1), Q(2), Q(3), Q(4), Q(5)]
    mu = [w * a for w, a in zip(weights, actual)]
    envelope = [(1 + delta) * w * p for w, p in zip(weights, profile)]
    values = [Q(-3), Q(0), Q(7, 4), Q(5), Q(-2, 3)]
    assert all(a <= b for a, b in zip(mu, envelope))
    assert mass_variance(mu, values) <= mass_variance(envelope, values)


def check_affine_cube_root_recurrence() -> None:
    # B_{k+1} = q B_k + A rho^k, q=5/8, rho=1/3.
    q = Q(5, 8)
    rho = Q(1, 3)
    forcing = Q(7, 11)
    initial = Q(13, 5)

    def closed(k: int) -> Q:
        return q**k * initial + forcing * (q**k - rho**k) / (q - rho)

    assert closed(0) == initial
    for k in range(12):
        assert closed(k + 1) == q * closed(k) + forcing * rho**k


def main() -> None:
    checks = [
        check_pair_identity,
        check_endpoint_disintegration,
        check_positive_mixture_identity,
        check_measure_domination,
        check_k4_profile,
        check_domination_absorbs_discrepancy,
        check_affine_cube_root_recurrence,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS all V14 clipped-Beta density-bridge checks")


if __name__ == "__main__":
    main()
