#!/usr/bin/env python3
"""Exact finite certificate: central-ratio stability of sharp K4+double-edge census.

Frozen 7 ratio numerators (2,10,15,20,25,30,38). Replace index 3
by a variable t; no floating point, no LP, no external package. Exactly
2520 unordered F/G target assignments are enumerated per low-source pair.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations

SOURCES = (1, 2, 3, 5)
R0 = (2, 10, 15, 0, 25, 30, 38)
R1 = (2, 10, 15, 1, 25, 30, 38)
FROZEN = (2, 10, 15, 20, 25, 30, 38)


def high_pair_flux(R, labels):
    """Integer coefficients on the two high-high edges F and G."""
    a, b, c, d, e, f, g = (R[i] for i in labels)
    ub = (c - a) * (d - e)
    ud = -(b - c) * (e - a)
    return (-ub * (b - g) - ud * (d - g),
            -ub * (f - b) - ud * (f - d))


def opposite_reflection(labels):
    """Reflected K4 opposite edges, with label 3 on one high-high copy."""
    if 3 not in labels[5:]:
        return False
    other_high = labels[6] if labels[5] == 3 else labels[5]
    return (labels[0] + other_high == 6
            and labels[1] + labels[4] == 6
            and labels[2] + labels[3] == 6)


def main():
    assignments = [p for p in permutations(range(7)) if p[5] < p[6]]
    assert len(assignments) == 2520
    permanent, at_frozen = [], []
    finite_roots = defaultdict(list)
    for labels in assignments:
        a = high_pair_flux(R0, labels)
        b = high_pair_flux(R1, labels)
        frozen = high_pair_flux(FROZEN, labels)
        assert frozen == tuple(a[i] + 20 * (b[i] - a[i])
                               for i in range(2))
        for arc in range(2):
            intercept, slope = a[arc], b[arc] - a[arc]
            if intercept == slope == 0:
                permanent.append((labels, arc))
                assert opposite_reflection(labels)
            elif slope:
                finite_roots[Fraction(-intercept, slope)].append(
                    (labels, arc))
            if frozen[arc] == 0:
                at_frozen.append((labels, arc))
        assert not (frozen[0] == frozen[1] == 0)

    assert len(permanent) == 48
    assert set(at_frozen) == set(permanent)
    assert all(opposite_reflection(p) for p, _ in permanent)
    assert len(set(p for p, _ in permanent)) == 48
    assert len(finite_roots) == 84
    assert sum(map(len, finite_roots.values())) == 4320
    assert Fraction(20) not in finite_roots
    domain = sorted(r for r in finite_roots if 15 < r < 25)
    assert len(domain) == 18
    lower = max(r for r in domain if r < 20)
    upper = min(r for r in domain if r > 20)
    assert (lower, upper) == (Fraction(4730, 249), Fraction(5230, 249))
    assert all(len(finite_roots[r]) in (48, 96) for r in domain)
    assert len(finite_roots[lower]) == len(finite_roots[upper]) == 48
    lows = list(combinations(SOURCES, 2))
    assert len(lows) == 6
    print('FROZEN_SOURCE_PAIRS', len(lows))
    print('LABEL_ASSIGNMENTS_PER_LOW_PAIR', len(assignments))
    print('PERSISTENT_SYMMETRY_DEGENERACIES_PER_LOW_PAIR', len(permanent))
    print('SYMMETRY_MATCHINGS 3! * 2^3 = 48')
    print('CANDIDATE_TOTAL', len(lows) * len(assignments))
    print('FROZEN_DEGENERACIES', len(lows) * len(at_frozen))
    print('FROZEN_FULL_SUPPORT',
          len(lows) * (len(assignments) - len(at_frozen)))
    print('VARIABLE_t_AFFINE_CRITICAL_VALUES_ALL_REAL', len(finite_roots))
    print('CRITICAL_EVENTS_WITH_MULTIPLICITY_PER_LOW_PAIR',
          sum(map(len, finite_roots.values())))
    print('CRITICAL_t_VALUES_IN_DISTINCT_ORDER_INTERVAL_15_TO_25',
          len(domain))
    print('CRITICAL_t_VALUES_WITH_EVENT_COUNTS',
          [(str(r), len(finite_roots[r])) for r in domain])
    print('NEAREST_LEFT_CRITICAL_RATIO_NUMERATOR', str(lower))
    print('NEAREST_RIGHT_CRITICAL_RATIO_NUMERATOR', str(upper))
    print('EXACT_STABILITY_HALF_WIDTH', str(Fraction(20) - lower))
    print('EXACT_STABLE_OPEN_INTERVAL', str(lower), str(upper))
    print('PERSISTENT_DEGENERACIES_TOTAL', len(lows) * len(permanent))
    print('DEGENERACIES_AT_EITHER_INTERVAL_ENDPOINT',
          len(lows) * (len(permanent) + 48))
    print('FULL_SUPPORT_AT_EITHER_INTERVAL_ENDPOINT',
          len(lows) * (len(assignments) - len(permanent) - 48))
    print('PASS_EXACT_CENTER_RATIO_CIRCUIT_CENSUS_STABILITY')


if __name__ == '__main__':
    main()
