#!/usr/bin/env python3
"""Exact rational coupled-envelope reduction and two-witness toy certificate.

General theorem uses the PREFIX-713/716 BRC Gamma-coupling hypotheses.
Toy parameters are independent rational test data, not frozen-189-row measurements.
"""
from fractions import Fraction as Q

ZERO, HALF = Q(0), Q(1, 2)


def upper(t, mu, variance, C, B, delta):
    assert ZERO <= t <= HALF and mu >= 0 and C > 0 and B >= 0 and delta >= 0
    cap = min(delta, B / C)
    d = min(cap, max(ZERO, (C - 2 * mu - t) / 2))
    return variance - t * mu + min(B, C * d) - (2 * mu + t) * d - d * d


def exhaustive_candidates(t, mu, variance, C, B, delta):
    cap = min(delta, B / C)
    candidates = [ZERO, cap, delta]
    vertex = (C - 2 * mu - t) / 2
    if ZERO <= vertex <= cap:
        candidates.append(vertex)
    return variance - t * mu + max(
        min(B, C * d) - (2 * mu + t) * d - d * d for d in candidates
    )


def witness_a(t):
    return Q(21, 2) - Q(7, 2) * t


def witness_b(t):
    return Q(51, 5) - Q(2) * t


def main():
    mu, variance, C, B, delta = Q(2), Q(10), Q(5), Q(5), Q(1)
    def E(t):
        return upper(t, mu, variance, C, B, delta)

    for i in range(101):
        t = Q(i, 200)
        assert E(t) == exhaustive_candidates(t, mu, variance, C, B, delta)
        assert max(witness_a(t), witness_b(t)) - E(t) >= Q(1, 25)

    crossing = Q(1, 5)
    endpoints = {
        'A_0': witness_a(ZERO) - E(ZERO),
        'A_cross': witness_a(crossing) - E(crossing),
        'B_cross': witness_b(crossing) - E(crossing),
        'B_half': witness_b(HALF) - E(HALF),
        'A_half': witness_a(HALF) - E(HALF),
        'B_0': witness_b(ZERO) - E(ZERO),
    }
    assert endpoints == {
        'A_0': Q(1, 4), 'A_cross': Q(1, 25),
        'B_cross': Q(1, 25), 'B_half': Q(11, 80),
        'A_half': -Q(5, 16), 'B_0': -Q(1, 20),
    }
    print('ALL_CHECKS_PASS PREFIX717-R6')
    print('crossing', str(crossing), 'universal_margin',
          str(min(endpoints[k] for k in ('A_0', 'A_cross', 'B_half'))))
    print('endpoint_gaps', {k: str(v) for k, v in endpoints.items()})
    print('exact_rational_grid_evaluations', 101)

if __name__ == '__main__':
    main()
