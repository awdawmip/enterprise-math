#!/usr/bin/env python3
"""Standalone exact check of effect-aware BRC control-state lower bound.
No native Enterprise Math runtime or P000 dynamics are claimed.
"""
from collections import defaultdict
from fractions import Fraction
import json

EDGES = {0: ((2, -1, -1), (2, 1, -1)),
         1: ((0, -1, -1), (0, 1, -1)),
         2: ((1, 1, 1), (2, 1, -1))}
DELTA = ((1, 0), (2, 0), (2, 2))
P = 1000003


def counts_through_depth(n):
    counts = {(0, 0, 1, 0): 1}
    scalar = []
    totals = []
    for m in range(n + 1):
        scalar.append(sum(Fraction(c * (2**k), 1) if k >= 0 else Fraction(c, 2**(-k))
                          for (q, r, eps, k), c in counts.items() if q == 0 and r == 2 and eps == 1))
        totals.append(sum(counts.values()))
        assert totals[-1] == 2**m, (m, totals[-1])
        if m == n:
            break
        nxt = defaultdict(int)
        for (q, r, eps, k), c in counts.items():
            for a, (q2, eta, b) in enumerate(EDGES[q]):
                nxt[q2, DELTA[r][a], eta * eps, eta * k + b] += c
        counts = nxt
    return scalar, totals


def det_mod(matrix, p):
    a = [[int(z.numerator % p) * pow(int(z.denominator % p), -1, p) % p
          for z in row] for row in matrix]
    n = len(a); det = 1
    for i in range(n):
        pivot = next((j for j in range(i, n) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            det = -det
        d = a[i][i]
        det = det * d % p
        invd = pow(d, -1, p)
        for j in range(i+1, n):
            if a[j][i]:
                f = a[j][i] * invd % p
                for k in range(i+1, n):
                    a[j][k] = (a[j][k] - f*a[i][k]) % p
                a[j][i] = 0
    return det % p


def run():
    s, totals = counts_through_depth(24)
    h = [[s[i+j] for j in range(13)] for i in range(13)]
    det = det_mod(h, P)
    assert det != 0, '13x13 scalar Hankel minor vanished mod p'
    # independently compare evaluated path counts against exact 2x2 matrix lifts
    # for every depth 0..24, via 14-dimensional rational vector at x=2
    pairs = ((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2))
    slot = {pair:i for i,pair in enumerate(pairs)}
    v = [Fraction(0) for _ in range(14)]
    v[2*slot[(0,0)]] = Fraction(1)
    scalar_lift = []
    for m in range(25):
        scalar_lift.append(v[2*slot[(0,2)]])
        if m == 24:
            break
        w = [Fraction(0) for _ in range(14)]
        for (q,r),idx in slot.items():
            u0, u1 = v[2*idx], v[2*idx+1]
            for a,(t,eta,b) in enumerate(EDGES[q]):
                j=slot[(t,DELTA[r][a])]
                x = Fraction(2**b, 1) if b>=0 else Fraction(1,2**(-b))
                if eta==1:
                    w[2*j]+=x*u0
                    w[2*j+1]+=u1/x
                else:
                    w[2*j]+=x*u1
                    w[2*j+1]+=u0/x
        v=w
    assert scalar_lift == s, 'path enumeration and matrix lift disagree'
    report={
        'schema':'EM_R265_EFFECT_AWARE_CONTROL_LOWER_BOUND_V1',
        'model':'R260-R263 formal positive two-choice affine BRC with source DFA, nonnative',
        'precision':'exact rational arithmetic; modular certificate over prime 1000003',
        'prime':P,'hankel_shape':[13,13],
        'hankel_determinant_mod_prime':det,
        'source_scalar':'s_m(x)=sum_{q=0,r=2,eps=+1} x^k, x=2',
        'observed_depths':[0,24],
        'total_paths_at_last_depth':str(totals[-1]),
        'matrix_lift_dimensions':14,
        'lower_bound_on_affine_control_states':7,
        'upper_bound_by_reachable_product_automaton':7,
        'status':'PASS',
        'boundaries':['Does not verify native Enterprise Math imports',
                      'No P000 dynamics or R193 real provenance correspondence',
                      'No unqualified claim on arbitrary nonlinear/time-varying/effect-to-state side-channel readout',
                      'No Source CLAIM/Driver acceptance'],
    }
    return report

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
