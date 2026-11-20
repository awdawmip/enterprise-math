#!/usr/bin/env python3
"""Exact rational R48 certificate for conditional source-labelled BRC masses."""
import json
from fractions import Fraction as Q
from itertools import product

def interval(z, err):
    assert err >= 0
    lo, hi = max(Q(0), z - err), z + err
    return (lo, hi) if lo <= hi else None

def meet(a, b):
    if a is None or b is None:
        return None
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    return (lo, hi) if lo <= hi else None

def infer(p, readings, errors):
    """Exact existential inverse (p,S,P), equivalent to alpha,beta>0."""
    assert p >= 1 and len(readings) == len(errors) == 4
    i = [interval(Q(z), Q(e)) for z, e in zip(readings, errors)]
    if any(v is None for v in i):
        return None
    x, y, d, h = i
    S = (x[0] / p, x[1] / p)
    if p == 1:
        if y[0] != 0:
            return None
    else:
        S = meet(S, (y[0] / (p - 1), y[1] / (p - 1)))
    if S is None:
        return None
    P = (h[0] / (2 * p), h[1] / (2 * p))
    if p == 1:
        if d[0] != 0:
            return None
    else:
        P = meet(P, (d[0] / (2 * (p * p - 1)),
                     d[1] / (2 * (p * p - 1))))
    if P is None:
        return None
    if S[1] <= 0 or P[1] <= 0 or P[0] > S[1] * S[1] / 4:
        return None
    return S, P

def candidate_upper_bound(readings, errors):
    x, y, d, h = [interval(Q(z), Q(e))
                  for z, e in zip(readings, errors)]
    if any(i is None for i in (x, y, d, h)):
        return 0
    bounds = []
    slow = x[0] - y[1]
    if slow > 0:
        bounds.append(int(x[1] // slow))
    if h[0] > 0:
        rmax = d[1] / h[0]
        p = 1
        while Q(p * p - 1, p) <= rmax:
            p += 1
        bounds.append(p - 1)
    return min(bounds) if bounds else None

def roots_data(p, a, b):
    S, P = a + b, a * b
    return (p * S, (p - 1) * S, 2 * (p * p - 1) * P, 2 * p * P)

def stringify(x):
    return str(x.numerator) + ('/' + str(x.denominator) if x.denominator != 1 else '')

def main():
    weights = [Q(1, 2), Q(1), Q(2), Q(3)]
    errors = [Q(0), Q(1, 20), Q(1, 5), Q(1, 2), Q(1), Q(2), Q(4)]
    total = 0
    for p, a, b, e in product(range(1, 9), weights, weights, errors):
        base = roots_data(p, a, b)
        for signs in product((-1, 1), repeat=4):
            observed = [x + s * e for x, s in zip(base, signs)]
            valid = infer(p, observed, [e] * 4)
            assert valid is not None, (p, a, b, e, signs)
            upper = candidate_upper_bound(observed, [e] * 4)
            if upper is not None:
                assert upper >= p
            total += 1
    case = roots_data(3, Q(1), Q(2))
    ambiguities = {}
    for e in errors:
        candidates = [p for p in range(1, 15)
                      if infer(p, case, [e] * 4) is not None]
        ambiguities[stringify(e)] = candidates
    assert case == (Q(9), Q(6), Q(32), Q(12))
    assert ambiguities['2'] == [3]
    assert ambiguities['4'] == [3, 4]
    sharp_cases = 0
    for p, S in product(range(1, 13), range(1, 11)):
        vals = []
        for other in range(1, 25):
            if other == p:
                continue
            t = Q(2 * p - 1, 2 * other - 1) * S
            residual = max(abs(p * S - other * t),
                           abs((p - 1) * S - (other - 1) * t))
            vals.append(residual)
        assert min(vals) == Q(S, 2 * p + 1)
        sharp_cases += 1
    return {
        'schema': 'X6_R48_FINITE_RESOLUTION_BRC_ROOT_CERTIFICATE_V1',
        'status': 'PASS',
        'tested_parameter_tuples': 8 * 16 * len(errors),
        'signed_readout_enclosures_checked': total,
        'adjacent_ray_checks': sharp_cases,
        'exact_r47_example': [stringify(v) for v in case],
        'r47_example_candidate_ports_by_equal_absolute_error': ambiguities,
        'sharp_XY_minimax_error_p3_S3': '3/14',
        'proof_scope': 'Exact conditional R44/R47 positive weighted BRC root coefficients; no physical calibration',
        'methods': 'Fraction arithmetic, interval intersection, positivity and discriminant feasibility'
    }

if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2, sort_keys=True))
