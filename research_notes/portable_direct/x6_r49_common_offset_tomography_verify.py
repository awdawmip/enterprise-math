#!/usr/bin/env python3
"""Exact Q-arithmetic verification of conditional R49 common-offset BRC inversion."""
import json
from fractions import Fraction as Q
from itertools import product

WEIGHTS = (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3))
OFFSETS = (Q(-7), Q(-2), Q(0), Q(5, 3), Q(11))

def coefficients(p, a, b, offset=Q(0)):
    s, t = a + b, a * b
    return (p*s + offset, (p-1)*s + offset,
            2*(p*p-1)*t + offset, 2*p*t + offset)

def infer_candidates(data, ceiling=30):
    x, y, d, h = map(Q, data)
    s, k, e = x-y, x-h, d-h
    if s <= 0:
        return []
    out = []
    for q in range(1, ceiling+1):
        t = (q*s-k)/(2*q)
        if t <= 0 or 4*t > s*s:
            continue
        if e != 2*(q*q-q-1)*t:
            continue
        offset = x-q*s
        # independent reconstruction, no floating-point root extraction
        assert (q*s+offset, (q-1)*s+offset,
                2*(q*q-1)*t+offset, 2*q*t+offset) == (x,y,d,h)
        out.append((q,s,t,offset))
    return out

def recover_exact(data):
    """Terminating exact inverse, no prior upper bound on Port count."""
    x, y, d, h = map(Q, data)
    s, k, e = x-y, x-h, d-h
    if s <= 0 or e == 0:
        return None
    if e < 0:
        q = 1
    else:
        q = max(2, int(k // s) + 1 if k > 0 else 2)
        while (q*q-q-1)*(s-k/q) < e:
            q += 1
    t = (q*s-k)/(2*q)
    if t <= 0 or 4*t > s*s:
        return None
    off = x-q*s
    if (q*s+off, (q-1)*s+off,
        2*(q*q-1)*t+off, 2*q*t+off) != (x,y,d,h):
        return None
    return (q,s,t,off)

def run():
    tested = 0
    negative = zero = positive = 0
    for p, a, b, off in product(range(1,13), WEIGHTS, WEIGHTS, OFFSETS):
        data = coefficients(p,a,b,off)
        candidates = infer_candidates(data)
        assert len(candidates) == 1, (p,a,b,off,candidates)
        assert recover_exact(data) == candidates[0]
        q,s,t,got_off = candidates[0]
        assert q == p and s == a+b and t == a*b and got_off == off
        e = data[2]-data[3]
        assert (e < 0) == (p == 1)
        assert e != 0
        tested += 1
        if off < 0: negative += 1
        elif off == 0: zero += 1
        else: positive += 1
    # Removing D makes p=2 and p=3 indistinguishable after common offset.
    a = coefficients(3,Q(1),Q(2),Q(0))
    b = coefficients(2,Q(3,2),Q(3,2),Q(3))
    assert (a[0],a[1],a[3]) == (b[0],b[1],b[3]) == (Q(9),Q(6),Q(12))
    assert a[2] == Q(32) and b[2] == Q(33,2)
    return {
        'schema':'X6_R49_COMMON_ADDITIVE_OFFSET_TOMOGRAPHY_V1',
        'status':'PASS',
        'candidate_port_range':'1..30',
        'true_port_range':'1..12',
        'weight_set':[str(v) for v in WEIGHTS],
        'offset_set':[str(v) for v in OFFSETS],
        'exact_parameter_combinations':tested,
        'offset_sign_counts':{'negative':negative,'zero':zero,'positive':positive},
        'unique_port_and_weight_pair_and_offset':True,
        'three_channel_alias':{'observed_channels':['X','Y','H'], 'common_values':['9','6','12'],
            'model_a':{'p':3,'weights':['1','2'],'offset':'0','D':'32'},
            'model_b':{'p':2,'weights':['3/2','3/2'],'offset':'3','D':'33/2'}},
        'arithmetic':'Python 3 standard-library fractions.Fraction, no floating point',
        'scope':'Conditional R44/R47 positive-weighted two-source BRC graph; exact shared additive bias; not a native P000 operation',
        'proof_basis':'Sign of E for p=1 versus p>=2 and strict monotonicity of E_q over positive-product feasible q>=2',
        'review_status':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED'
    }

if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
