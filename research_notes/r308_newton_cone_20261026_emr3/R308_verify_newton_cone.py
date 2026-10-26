#!/usr/bin/env python3
"""Exact R308 Newton-cone positivity certificate; Python standard library only."""
import argparse
import json
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sub(a, b):
    out = a + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        out[i] -= x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def numerator_coefficient(s):
    return [int(s == 0), -choose(3,s-1), -choose(6,s-1), choose(8,s-2)]


def denominator_coefficient(i):
    return [0, -choose(4,i)+choose(2,i-1),
            2*choose(5,i-1)-choose(6,i-1),
            choose(7,i-2), -choose(9,i-3)]


def original_q(max_d):
    """Independent R306 denominator recurrence (not the R308 N_s recurrence)."""
    q = [[0,0,0,1], [0,0,0,0,0,0,1]]
    multipliers = (((1,1),(2,-1),(3,1)),
                   ((3,1),(4,-3),(5,2)),
                   ((6,-1),(7,2),(8,-1)),
                   ((8,1),(9,-3),(10,3),(11,-1)))
    for d in range(2,max_d+1):
        row = [0] * (3*d+4)
        for i, terms in enumerate(multipliers,1):
            if d-i >= 0:
                for shift, coeff in terms:
                    for k, x in enumerate(q[d-i]):
                        row[k+shift] += coeff*x
        if d == 2: row[6] -= 1; row[7] += 1
        if d == 3: row[8] += 1; row[9] -= 2; row[10] += 1
        q.append(row)
    return q


def run(smax, cross_dmax):
    assert 6 <= smax <= 1024 and 6 <= cross_dmax <= min(smax+1,100)
    power = [[1]]
    for s in range(1,smax+1):
        power.append(mul(power[-1],[1,-1]))
    kernels = [None] + [mul(denominator_coefficient(i),power[i-1]) for i in range(1,13)]
    polynomials = [[1]]
    rows = []
    global_min = None
    samples = []
    select = {0,1,2,3,4,5,6,7,8,32,64,128,256,smax}
    for s in range(smax+1):
        if s:
            p = mul(numerator_coefficient(s),power[s])
            for i in range(1,min(s,12)+1):
                p = sub(p,mul(kernels[i],polynomials[s-i]))
            assert len(p)-1 <= 2*s+1, ('degree',s)
            polynomials.append(p)
        p = polynomials[s]
        c = [sum(v*choose(2*s+1-k,s-j) for k,v in enumerate(p)) for j in range(s+1)]
        assert all(v > 0 for v in c), ('nonpositive coefficient',s)
        assert c[-1] == 2**s
        if s >= 1:
            assert 4*c[-2] == (5*s+1)*2**s
        if s >= 2:
            assert 32*c[-3] == (25*s*s-5*s-26)*2**s
        rows.append(c)
        value = min(c)
        global_min = value if global_min is None else min(global_min,value)
        if s in select:
            samples.append({'s':s,'K_at_d_s_plus_1':str(c[0]),
                'first_two':[str(t) for t in c[:2]],
                'last_three':[str(t) for t in c[-3:]],
                'minimum':str(value), 'numerator_degree':len(p)-1})
    q = original_q(cross_dmax)
    exact_crosschecks = 0
    for d in range(2,cross_dmax+1):
        for s in range(d):
            old = sum(v*choose(5*d+3-k,s) for k,v in enumerate(q[d]))
            h = d-s-1
            new = sum(choose(h,j)*v for j,v in enumerate(rows[s]))
            assert old == new, ('crosscheck',d,s)
            exact_crosschecks += 1
    return {
        'schema':'EM_R308_NEWTON_CONE256_EXACT_V1','status':'PASS',
        'arithmetic':'Python arbitrary-precision integers; no floating point or network',
        's_range':[0,smax], 'all_d':'every integer d >= s+1 for each certified s',
        'all_n':'every integer n >= 4*d+4 for each d if all 0<=s<d are certified',
        'positive_Newton_basis_coefficients_checked':(smax+1)*(smax+2)//2,
        'global_minimum':str(global_min),
        'universal_edges':['c(s,s)=2^s', '4*c(s,s-1)=(5s+1)*2^s (s>=1)',
            '32*c(s,s-2)=(25s^2-5s-26)*2^s (s>=2)'],
        'independent_R306_Q_recurrence_crosscheck_d':[2,cross_dmax],
        'independent_exact_crosschecks':exact_crosschecks,
        'selected_rows':samples,
        'scope':'Finite s strip 0..smax; unbounded d via degree-s polynomial identity. No all-s theorem.',
        'native_x6_correspondence':'NOT_ESTABLISHED',
        'independent_Driver_review':'NOT_PERFORMED'
    }


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--smax',type=int,default=256)
    parser.add_argument('--cross-dmax',type=int,default=60)
    args=parser.parse_args()
    print(json.dumps(run(args.smax,args.cross_dmax),ensure_ascii=False,indent=2))
