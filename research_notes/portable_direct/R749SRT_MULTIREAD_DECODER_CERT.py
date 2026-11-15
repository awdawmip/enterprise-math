#!/usr/bin/env python3
"""R749SRT: exact rational nearest-phase certificates for multiple cutoff reads.

No floating arithmetic or external package dependencies. All-integer claims use
finite exhaustive checks and six polynomial certificates for the infinite tail.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
import json

WEIGHTS = (1, 1, 2, 3, 6)
SMOOTH = (Q(1, 6), Q(1, 2), -Q(115, 36), Q(115, 6), -Q(16315, 108))
PHASE = tuple(Q(v, 36) for v in (455, -295, -25, 185, -25, -295))
READ_SETS = ((0, 1), (0, 1, 2), (0, 1, 5), (0, 1, 2, 3),
             (0, 1, 2, 3, 4), (0, 1, 2, 3, 4, 5))
N = 600

def counts():
    c = [0] * N
    t = [0] * N
    c[0] = 1
    for j, s in enumerate(WEIGHTS):
        nc = [0] * N
        nt = [0] * N
        for v in range(N):
            if c[v] == 0 and t[v] == 0:
                continue
            for k in range((N - v - 1) // s + 1):
                nc[v + k * s] += c[v]
                nt[v + k * s] += t[v] + (k * c[v] if j == 0 else 0)
        c, t = nc, nt
    cum_c = [0]
    cum_t = [0]
    for i in range(N):
        cum_c.append(cum_c[-1] + c[i])
        cum_t.append(cum_t[-1] + t[i])
    return cum_c, cum_t

def brute(r):
    def rec(j, budget, first):
        if j == len(WEIGHTS):
            return 1, first
        A = B = 0
        for k in range(budget // WEIGHTS[j] + 1):
            c, t = rec(j + 1, budget - k * WEIGHTS[j], first + (k if j == 0 else 0))
            A += c
            B += t
        return A, B
    return rec(0, r - 1, 0)

def poly_add(a, b):
    return [(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
            for i in range(max(len(a), len(b)))]

def poly_mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

def poly_scale(a, k):
    return [x * k for x in a]

def poly_pow(a, k):
    v = [Q(1)]
    for _ in range(k):
        v = poly_mul(v, a)
    return v

def interpolate(y):
    d = list(map(Q, y))
    p = [Q(0)]
    for k in range(len(y)):
        f = [Q(1)]
        for j in range(k):
            f = poly_mul(f, [-Q(j), Q(1)])
        p = poly_add(p, poly_scale(f, d[0] / factorial(k)))
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    return p

def residual(r, c, t):
    return Q(r**3 * t[r], c[r]) - sum(h * r**(4 - j) for j, h in enumerate(SMOOTH))

def tail_certificate(c, t):
    rows = []
    for a in range(6):
        start = next(r for r in range(512, 518) if r % 6 == a)
        cp = interpolate([c[start + 6 * n] for n in range(6)])
        tp = interpolate([t[start + 6 * n] for n in range(7)])
        assert len(cp) == 6 and len(tp) == 7
        for n in range(8):
            assert sum(x * n**i for i, x in enumerate(cp)) == c[start + 6*n]
            assert sum(x * n**i for i, x in enumerate(tp)) == t[start + 6*n]
        rpoly = [Q(start), Q(6)]
        expected = [PHASE[a]]
        for i, h in enumerate(SMOOTH):
            expected = poly_add(expected, poly_scale(poly_pow(rpoly, 4-i), h))
        num = poly_add(poly_mul(poly_pow(rpoly, 3), tp),
                       poly_scale(poly_mul(cp, expected), -1))
        up = poly_add(poly_scale(cp, Q(35, 12)), poly_scale(num, -1))
        while num[-1] == 0:
            num.pop()
        while up[-1] == 0:
            up.pop()
        assert len(num) == 5 and len(up) == 6
        assert all(x > 0 for x in cp + num + up)
        rows.append({'phase':a,'first_r':start,'C_degree':len(cp)-1,
                     'positive_N_degree':len(num)-1,'positive_U_degree':len(up)-1,
                     'min_C_coefficient':str(min(cp)),
                     'min_N_coefficient':str(min(num)),
                     'min_U_coefficient':str(min(up))})
    return rows

def decode(shifts, c, t):
    signatures = [tuple(PHASE[(a+h)%6] for h in shifts) for a in range(6)]
    distinct = list(dict.fromkeys(signatures))
    assert len(distinct) == 6
    sep = min(max(abs(x-y) for x,y in zip(u,v)) for u,v in combinations(distinct,2))
    assert sep >= Q(15, 2) if len(shifts)>2 else sep == Q(35,6)
    bad = []
    margins = []
    for r in range(1, 512):
        observation = tuple(residual(r+h,c,t) for h in shifts)
        distances = {v:max(abs(x-y) for x,y in zip(observation,v)) for v in distinct}
        true = signatures[r%6]
        margin = min(v - distances[true] for key,v in distances.items() if key != true)
        if margin <= 0:
            min_dist = min(distances.values())
            winners = [a for a in range(6) if distances[signatures[a]] == min_dist]
            bad.append({'r':r,'gap':str(margin),'true_phase':r%6,
                        'minimum_distance':str(min_dist),'true_distance':str(distances[true]),
                        'winning_phases':winners})
        else:
            margins.append((margin,r))
    tau = bad[-1]['r'] + 1
    after = [(gap,r) for gap,r in margins if r >= tau]
    assert len(after) == 512-tau
    worst = min(after)
    return {'shifts':list(shifts), 'observation_count':len(shifts),
            'separation':str(sep), 'sharp_threshold':tau,
            'last_failure':bad[-1], 'failure_count_before_512':len(bad),
            'strict_positives_from_threshold_to_511':len(after),
            'minimum_margin_in_finite_bridge':str(worst[0]),
            'minimum_margin_at_r':worst[1]}

def run():
    c,t = counts()
    for r in range(1,25):
        assert (c[r],t[r]) == brute(r)
    tail = tail_certificate(c,t)
    results = [decode(s,c,t) for s in READ_SETS]
    assert [v['sharp_threshold'] for v in results] == [398,44,35,26,26,18]
    return {'status':'PASS', 'claim':'exact sharp all-r thresholds of max-norm nearest ideal phase decoder',
            'model':list(WEIGHTS), 'marked_index':0,
            'population':'nonnegative labeled vector of weighted sum <= r-1',
            'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'predecessor':'R749SRS@9d9a2915a44f6f481491ebd26ba8cd794763f3c5',
            'proof_tail':'r>=512: 0<R(r)-P(r)<35/12 via six positive-coefficient quasipolynomials',
            'tail_certificates':tail, 'direct_recursion_checks':24,
            'finite_precision_range':[1,511],
            'tested_decoder_evaluations':len(READ_SETS)*511,
            'results':results,'math_status':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
