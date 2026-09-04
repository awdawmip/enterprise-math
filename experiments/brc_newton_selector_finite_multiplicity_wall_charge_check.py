#!/usr/bin/env python3
"""Exact regression for finite-multiplicity selector wall charges."""
from __future__ import annotations

from fractions import Fraction
from math import factorial
from itertools import product

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def trim(poly) -> Poly:
    values = [Q(value) for value in poly]
    if not values:
        return (Q(0),)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def padd(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else Q(0))
        + (right[i] if i < len(right) else Q(0))
        for i in range(n)
    ))


def pscale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def derivative_n(poly: Poly, order: int) -> Poly:
    out = trim(poly)
    for _ in range(order):
        out = derivative(out)
    return out


def peval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def shifted_power(center: Fraction, degree: int) -> Poly:
    out: Poly = (Q(1),)
    factor: Poly = (-center, Q(1))
    for _ in range(degree):
        out = pmul(out, factor)
    return out


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def cauchy_bound(poly: Poly) -> Fraction:
    poly = trim(poly)
    if len(poly) <= 1:
        return Q(0)
    leading = abs(poly[-1])
    return Q(1) + max((abs(value) / leading for value in poly[:-1]), default=Q(0))


def rank_lt(poly: Poly, probe: Fraction) -> int:
    poly = trim(poly)
    if peval(poly, probe) == 0:
        raise ValueError("probe must not be a root")
    left = -max(cauchy_bound(poly) + 1, abs(probe) + 2)
    while peval(poly, left) == 0:
        left -= 1
    return cd._root_count(cd._sturm_sequence(poly), left, probe)


def interval_count(poly: Poly, left: Fraction, right: Fraction) -> int:
    poly = trim(poly)
    if not left < right:
        raise ValueError("left must be smaller than right")
    if peval(poly, left) == 0 or peval(poly, right) == 0:
        raise ValueError("interval endpoints must not be roots")
    return cd._root_count(cd._sturm_sequence(poly), left, right)


def event_polynomial(
    multiplicity: int,
    kappa: Fraction,
    parameter: Fraction,
    center: Fraction,
    mixed: tuple[Fraction, ...] = (),
) -> Poly:
    """(x-center)^m - kappa*t + t*sum_j mixed[j-1]*(x-center)^j."""
    poly = padd(shifted_power(center, multiplicity), (-kappa * parameter,))
    for degree, coefficient in enumerate(mixed, start=1):
        if coefficient:
            poly = padd(poly, pscale(shifted_power(center, degree), parameter * coefficient))
    return trim(poly)


def event_pt_polynomial(
    kappa: Fraction,
    center: Fraction,
    mixed: tuple[Fraction, ...],
) -> Poly:
    out: Poly = (-kappa,)
    for degree, coefficient in enumerate(mixed, start=1):
        if coefficient:
            out = padd(out, pscale(shifted_power(center, degree), coefficient))
    return trim(out)


def ordinary_event_kappa(
    pt_at_event: Fraction,
    pxm_at_event: Fraction,
    multiplicity: int,
) -> Fraction | None:
    if multiplicity < 1 or pt_at_event == 0 or pxm_at_event == 0:
        return None
    return -Q(factorial(multiplicity)) * pt_at_event / pxm_at_event


def expected_rank_jump(
    multiplicity: int,
    kappa: Fraction | None,
    center: Fraction,
    probe: Fraction,
) -> int | None:
    if kappa is None:
        return None
    orientation = sign(kappa)
    if center < probe:
        return 2 * orientation if multiplicity % 2 == 0 else 0
    if center == probe:
        return ((-1) ** multiplicity) * orientation
    return 0


def expected_interval_jump(
    multiplicity: int,
    kappa: Fraction | None,
    center: Fraction,
    left: Fraction,
    right: Fraction,
) -> int | None:
    if kappa is None or not left < right:
        return None
    orientation = sign(kappa)
    if left < center < right:
        return 2 * orientation if multiplicity % 2 == 0 else 0
    if center == left:
        return orientation
    if center == right:
        return ((-1) ** multiplicity) * orientation
    return 0


def verify_event_derivatives(
    multiplicity: int,
    kappa: Fraction,
    center: Fraction,
    mixed: tuple[Fraction, ...],
) -> int:
    event = event_polynomial(multiplicity, kappa, Q(0), center, mixed)
    checks = 0
    for order in range(multiplicity):
        assert peval(derivative_n(event, order), center) == 0
        checks += 1
    pxm = peval(derivative_n(event, multiplicity), center)
    assert pxm == factorial(multiplicity)
    pt = peval(event_pt_polynomial(kappa, center, mixed), center)
    assert pt == -kappa
    assert ordinary_event_kappa(pt, pxm, multiplicity) == kappa
    return checks + 3


def local_observer_checks(
    multiplicity: int,
    kappa: Fraction,
    center: Fraction,
    mixed: tuple[Fraction, ...],
    epsilon: Fraction,
) -> int:
    before = event_polynomial(multiplicity, kappa, -epsilon, center, mixed)
    after = event_polynomial(multiplicity, kappa, epsilon, center, mixed)
    checks = verify_event_derivatives(multiplicity, kappa, center, mixed)

    for probe in (center - 1, center, center + 1):
        observed = rank_lt(after, probe) - rank_lt(before, probe)
        predicted = expected_rank_jump(multiplicity, kappa, center, probe)
        assert observed == predicted
        checks += 1

    intervals = (
        (center - 1, center + 1),
        (center, center + 1),
        (center - 1, center),
        (center + 1, center + 2),
    )
    for left, right in intervals:
        observed = interval_count(after, left, right) - interval_count(before, left, right)
        predicted = expected_interval_jump(multiplicity, kappa, center, left, right)
        assert observed == predicted
        checks += 1
    return checks


def canonical_normal_form_regression():
    epsilon = Q(1, 4096)
    samples = checks = 0
    for multiplicity, kappa, center in product(
        range(1, 9),
        (Q(-3), Q(-1), Q(1), Q(2)),
        (Q(-1), Q(0), Q(1), Q(2), Q(3)),
    ):
        checks += local_observer_checks(multiplicity, kappa, center, (), epsilon)
        samples += 1
    assert samples == 160
    return samples, checks


def mixed_term_regression():
    epsilon = Q(1, 4096)
    templates = (
        (Q(1),),
        (Q(-1), Q(2)),
        (Q(2), Q(-1), Q(1)),
    )
    samples = checks = 0
    for multiplicity, kappa, center, template in product(
        range(2, 9),
        (Q(-2), Q(-1), Q(1), Q(2)),
        (Q(-1), Q(0), Q(1), Q(2), Q(3)),
        templates,
    ):
        mixed = tuple(
            template[index] if index < len(template) else Q(0)
            for index in range(multiplicity - 1)
        )
        checks += local_observer_checks(multiplicity, kappa, center, mixed, epsilon)
        samples += 1
    assert samples == 420
    return samples, checks


def linear_factor(parameter: Fraction) -> Poly:
    return (-parameter, Q(1))


def shifted_fold_factor(parameter: Fraction) -> Poly:
    return (Q(4) - parameter, Q(-2), Q(1))


def additive_wall_ledger_regression():
    epsilon = Q(1, 4096)

    def family(parameter: Fraction) -> Poly:
        return pmul(linear_factor(parameter), shifted_fold_factor(parameter))

    initial = family(-epsilon)
    final = family(Q(3) + epsilon)
    interval_global = interval_count(final, Q(0), Q(2)) - interval_count(initial, Q(0), Q(2))
    rank_global = rank_lt(final, Q(2)) - rank_lt(initial, Q(2))

    interval_charges = (
        expected_interval_jump(1, Q(1), Q(0), Q(0), Q(2)),
        expected_interval_jump(1, Q(1), Q(2), Q(0), Q(2)),
        expected_interval_jump(2, Q(1), Q(1), Q(0), Q(2)),
    )
    rank_charges = (
        expected_rank_jump(1, Q(1), Q(0), Q(2)),
        expected_rank_jump(1, Q(1), Q(2), Q(2)),
        expected_rank_jump(2, Q(1), Q(1), Q(2)),
    )
    assert interval_charges == (1, -1, 2)
    assert rank_charges == (0, -1, 2)
    assert interval_global == sum(interval_charges) == 2
    assert rank_global == sum(rank_charges) == 1

    local_checks = 0
    for t0, expected_interval, expected_rank in (
        (Q(0), 1, 0),
        (Q(2), -1, -1),
        (Q(3), 2, 2),
    ):
        before = family(t0 - epsilon)
        after = family(t0 + epsilon)
        assert interval_count(after, Q(0), Q(2)) - interval_count(before, Q(0), Q(2)) == expected_interval
        assert rank_lt(after, Q(2)) - rank_lt(before, Q(2)) == expected_rank
        local_checks += 2
    return 12 + local_checks


def simultaneous_spatially_separated_folds():
    epsilon = Q(1, 4096)

    def family(parameter: Fraction) -> Poly:
        first = (-parameter, Q(0), Q(1))
        second = (Q(1) - parameter, Q(-2), Q(1))
        return pmul(first, second)

    before = family(-epsilon)
    after = family(epsilon)
    observed_interval = interval_count(after, Q(0), Q(2)) - interval_count(before, Q(0), Q(2))
    observed_rank = rank_lt(after, Q(2)) - rank_lt(before, Q(2))
    interval_sum = (
        expected_interval_jump(2, Q(1), Q(0), Q(0), Q(2))
        + expected_interval_jump(2, Q(1), Q(1), Q(0), Q(2))
    )
    rank_sum = (
        expected_rank_jump(2, Q(1), Q(0), Q(2))
        + expected_rank_jump(2, Q(1), Q(1), Q(2))
    )
    assert observed_interval == interval_sum == 3
    assert observed_rank == rank_sum == 4
    return 6


def refusal_boundaries():
    checks = 0
    for multiplicity in range(1, 7):
        assert ordinary_event_kappa(Q(0), Q(factorial(multiplicity)), multiplicity) is None
        epsilon = Q(1, 64)
        before = padd(shifted_power(Q(0), multiplicity), (-(epsilon * epsilon),))
        after = padd(shifted_power(Q(0), multiplicity), (-(epsilon * epsilon),))
        assert rank_lt(after, Q(1)) - rank_lt(before, Q(1)) == 0
        checks += 2

    for multiplicity in range(1, 7):
        event = shifted_power(Q(0), multiplicity + 1)
        pxm = peval(derivative_n(event, multiplicity), Q(0))
        assert pxm == 0
        assert ordinary_event_kappa(Q(-1), pxm, multiplicity) is None
        checks += 2

    assert expected_interval_jump(2, Q(1), Q(0), Q(1), Q(1)) is None
    assert ordinary_event_kappa(Q(-1), Q(1), 0) is None
    checks += 2
    return checks


def main() -> int:
    canonical_samples, canonical_checks = canonical_normal_form_regression()
    mixed_samples, mixed_checks = mixed_term_regression()
    ledger_checks = additive_wall_ledger_regression()
    simultaneous_checks = simultaneous_spatially_separated_folds()
    refusals = refusal_boundaries()

    print("BRC finite-multiplicity selector wall-charge checker: PASS")
    print(f"canonical_monomial_event_samples={canonical_samples}")
    print(f"canonical_observer_checks={canonical_checks}")
    print(f"mixed_ordinary_event_samples={mixed_samples}")
    print(f"mixed_observer_checks={mixed_checks}")
    print(f"additive_wall_ledger_checks={ledger_checks}")
    print(f"simultaneous_separated_event_checks={simultaneous_checks}")
    print(f"typed_refusal_checks={refusals}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
