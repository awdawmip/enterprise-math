#!/usr/bin/env python3
"""Exact rational N4 crossed-arrival occupancy and terminal-observer repair."""
from fractions import Fraction as F
import json

Q1 = {'A': F(1, 2), 'B': F(1, 2)}
R1 = {'A': F(1, 2), 'B': F(3, 2)}
Q2 = {'AU': F(1, 6), 'AV': F(1, 3), 'BU': F(1, 4), 'BV': F(1, 4)}
R2 = {'AU': F(1), 'AV': F(1, 4), 'BU': F(1), 'BV': F(2)}
SLOT = [(t, a) for t in range(1, 5) for a in ('P', 'Q')]


def output(sa, sb, p):
    """All 16 (law,time,decision) coordinates, with no continuation at t=2."""
    result = {}
    for law in ('Q', 'P'):
        weights1 = {h: Q1[h] * (R1[h] if law == 'P' else 1) for h in Q1}
        weights2 = {h: Q2[h] * (R2[h] if law == 'P' else 1) for h in Q2}
        v = {key: F(0) for key in SLOT}
        v[(1, 'Q')] = weights1['A'] * (1 - sa) + weights1['B'] * (1 - sb)
        for h in Q2:
            arrival = sa if h[0] == 'A' else sb
            prob_p = p if h in ('AU', 'BU') else F(0)
            v[(2, 'P')] += weights2[h] * arrival * prob_p
            v[(2, 'Q')] += weights2[h] * arrival * (1 - prob_p)
        assert sum(v.values()) == 1
        result[law] = v
    return result


def combine(v0, v1, theta):
    return {law: {k: (1 - theta) * v0[law][k] + theta * v1[law][k]
                  for k in SLOT} for law in ('Q', 'P')}


def tv(v0, v1, law):
    return sum((abs(v0[law][k] - v1[law][k]) for k in SLOT), F(0)) / 2


def check(delta, theta):
    a = 1 - theta * delta
    b = 1 - (1 - theta) * delta
    a_p, b_p = 1 - theta, (1 - theta) * (1 - delta)
    a_q, b_q = theta * (1 - delta), theta
    defect = a_p * b - b_p * a
    formula = theta * (1 - theta) * delta * (2 - delta)
    assert defect == formula
    assert a_q * b - b_q * a == -formula
    assert a_p + a_q == a and b_p + b_q == b
    pooled = (a_p + b_p) / (a + b)
    occupancy_l1 = sum((abs(z) for z in (
        a_p - a * pooled, a_q - a * (1 - pooled),
        b_p - b * pooled, b_q - b * (1 - pooled))), F(0))
    assert pooled == 1 - theta
    assert occupancy_l1 == 4 * theta * (1 - theta) * delta
    q_arrival = Q2['AU'] * a + Q2['BU'] * b
    weighted = (Q2['AU'] * a_p + Q2['BU'] * b_p) / q_arrival
    assert F(0) <= weighted <= F(1)
    target = combine(output(F(1), 1 - delta, F(1)),
                     output(1 - delta, F(1), F(0)), theta)
    repaired = output(a, b, weighted)
    assert target == repaired
    pooled_output = output(a, b, pooled)
    assert tv(target, pooled_output, 'Q') == tv(target, pooled_output, 'P')
    return {'delta': str(delta), 'theta': str(theta),
            'cross_defect_P': str(defect), 'pooled_occupancy_l1': str(occupancy_l1),
            'weighted_P': str(weighted), 'pooled_tv': str(tv(target, pooled_output, 'Q'))}


def main():
    grid = [check(d, t) for d in (F(0), F(1, 5), F(1, 2), F(3, 4), F(1))
            for t in (F(0), F(1, 6), F(1, 2), F(5, 6), F(1))]
    witness = check(F(1, 2), F(1, 2))
    assert witness == {'delta': '1/2', 'theta': '1/2',
                       'cross_defect_P': '3/16', 'pooled_occupancy_l1': '1/2',
                       'weighted_P': '7/15', 'pooled_tv': '1/96'}
    print(json.dumps({'status': 'PASS_EXACT_N4_CROSSED_ARRIVAL_OBSERVER_REPAIR',
                      'grid_count': len(grid), 'witness': witness,
                      'scope': 'finite rational grid; all-real theorem proved algebraically'},
                     ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
