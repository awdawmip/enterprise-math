#!/usr/bin/env python3
"""Exact rational regression for PREFIX-782 shared-reflection-defect theorem.
No external packages; does not recompute the 189-layer original coefficients.
"""
from fractions import Fraction as F
from itertools import product
import json


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def parameter_window(A1, A2, B1, B2, S1, S2, c, delta):
    assert 0 < B1 < B2 and min(S1, S2, c, delta) >= 0
    d = min(delta, 2*c)
    intervals = [
        ((A1-S1-c)/B1, (A1+S1+c)/B1),
        ((A2-S2-c)/B2, (A2+S2+c)/B2),
        ((A2-A1-S1-S2-d)/(B2-B1),
         (A2-A1+S1+S2+d)/(B2-B1)),
    ]
    lo = max(F(0), *(left for left, _ in intervals))
    hi = min(right for _, right in intervals)
    return intervals, (lo, hi) if hi >= lo and hi > 0 else None


def geometric_witness(x1, x2, S1, S2, c, delta):
    """Return exact base and reflected shared errors and private aggregates."""
    d = min(delta, 2*c)
    if (abs(x1) > S1+c or abs(x2) > S2+c
            or abs(x1-x2) > S1+S2+d):
        return None
    r = max(F(0), abs(x1-x2)-S1-S2)
    lo = max(-c+r/2, -x1-S1-r/2, -x2-S2-r/2)
    hi = min(c-r/2, -x1+S1+r/2, -x2+S2+r/2)
    assert lo <= hi
    s = lo
    u1 = clamp(-x1-s, -S1, S1)
    u2 = clamp(-x2-s, -S2, S2)
    h = s+r/2
    h_ref = s-r/2
    increments = (x1+h+u1, x2+h+u2,
                  -(x1+h_ref+u1), -(x2+h_ref+u2))
    assert abs(h) <= c and abs(h_ref) <= c
    assert abs(h-h_ref) <= delta
    assert abs(u1) <= S1 and abs(u2) <= S2
    assert all(v >= 0 for v in increments)
    return dict(h=h, h_ref=h_ref, u1=u1, u2=u2, increments=increments,
                r=r, s=s)


def distribute_private(total, budgets, signs=(1,-1,-1)):
    """Split signed mixed-difference total into three private corner errors."""
    assert len(budgets) == len(signs) == 3 and abs(total) <= sum(budgets)
    remaining = abs(total)
    vals = []
    direction = 1 if total >= 0 else -1
    for budget, coefficient in zip(budgets, signs):
        amount = min(remaining, budget)
        vals.append(direction*coefficient*amount)
        remaining -= amount
    assert remaining == 0 and sum(a*b for a,b in zip(vals, signs)) == total
    return tuple(vals)


def rational_json(v):
    if isinstance(v, F):
        return [v.numerator, v.denominator]
    if isinstance(v, (tuple, list)):
        return [rational_json(x) for x in v]
    if isinstance(v, dict):
        return {k: rational_json(x) for k, x in v.items()}
    return v


def main():
    sample = dict(A1=F(1), A2=F(2), B1=F(2), B2=F(3),
                  S1=F(1,5), S2=F(3,20), c=F(1,10), delta=F(1,10))
    old = parameter_window(**{**sample, 'delta': F(0)})[1]
    now = parameter_window(**sample)[1]
    assert old == (F(13,20), F(13,20))
    assert now == (F(7,12), F(13,20))
    q = F(3,5)
    w = geometric_witness(F(1)-q*F(2), F(2)-q*F(3),
                          sample['S1'], sample['S2'], sample['c'], sample['delta'])
    assert w is not None
    assert w['increments'] == (0, F(1,20), F(1,20), 0)
    private1 = distribute_private(w['u1'], (F(1,10), F(1,20), F(1,20)))
    private2 = distribute_private(w['u2'], (F(1,20), F(1,20), F(1,20)))
    assert geometric_witness(F(1)-q*F(2), F(2)-q*F(3),
                             sample['S1'], sample['S2'], sample['c'], F(0)) is None
    total = good = bad = 0
    for A1,A2,B1,B2,S1,S2,c,delta,q in product(
            (F(-1),F(0),F(1),F(2)), (F(0),F(1),F(2),F(3)),
            (F(1),), (F(2),F(3)), (F(0),F(1,5),F(3,5)),
            (F(0),F(1,5),F(3,5)), (F(0),F(1,10),F(3,10)),
            (F(0),F(1,10),F(1,2)), (F(1,5),F(1,2),F(3,5),F(4,5),F(1))):
        x1, x2 = A1-q*B1, A2-q*B2
        witness = geometric_witness(x1,x2,S1,S2,c,delta)
        _, interval = parameter_window(A1,A2,B1,B2,S1,S2,c,delta)
        feasible = interval is not None and interval[0] <= q <= interval[1]
        assert (witness is not None) == feasible
        total += 1
        if feasible:
            good += 1
        else:
            bad += 1
    result = {
        'theorem': 'PREFIX782_SHARED_ONLY_REFLECTION_DEFECT_FIXED_Q',
        'arithmetic': 'exact Python Fraction, no floating point',
        'finite_regression': {'cases': total, 'feasible': good, 'infeasible': bad},
        'example': {'parameters': sample, 'q': F(3,5), 'equivariant_window': old,
                    'defective_window': now, 'witness': w,
                    'private_corners_base_and_reflected': [private1, private2]},
        'scope': '4 auxiliary gamma cells; 3 private errors per cell; reflected private errors exactly equal; only shared pair may differ',
        'status': 'AUTHOR_UNREVIEWED_NOT_ADMITTED',
        'regression': 'ALL_CHECKS_PASS PREFIX782 SHARED_DEFECT_POINTWISE_WINDOW',
    }
    print(json.dumps(rational_json(result), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
