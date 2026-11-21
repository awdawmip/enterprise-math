#!/usr/bin/env python3
"""R90 finite corroboration for the exact one-channel anisotropy theorem.
The full-lattice result follows from the arithmetic proof in the companion note.
"""
from fractions import Fraction
from itertools import product
import json

MAX_Q = 40
WEIGHTS = [Fraction(1,2), Fraction(1), Fraction(11), Fraction(22), Fraction(23), Fraction(24), Fraction(100)]

def port(a):
    return max(sum(max(0, v) for v in a), sum(max(0, -v) for v in a))

def half_gaps(a):
    x, y, z = a
    u, v, h = x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z
    return (abs(u), abs(v), abs(h), abs(v-u), abs(h-u), abs(h-v))

def objective(a, t):
    d = (2,2,1+t,2,1+t,1+t)
    return max(Fraction(g,1)/s for g,s in zip(half_gaps(a),d))

def optimum(t):
    return min(max(Fraction(1,2), Fraction(1,1)/(1+t)), Fraction(12,1)/(1+t))

def expected_ties(t):
    if t < 23:
        return [(10,-5,1)]
    if t == 23:
        return [(4,-1,0),(6,-4,1),(10,-5,1)]
    return [(6,-4,1)]

def run():
    records = {str(t): {'expected_value': str(optimum(t)), 'below': 0, 'ties': []} for t in WEIGHTS}
    n = 0
    for a in product(range(-MAX_Q,MAX_Q+1), repeat=3):
        if a == (0,0,0) or port(a) > MAX_Q or next(v for v in a if v) < 0:
            continue
        n += 1
        for t in WEIGHTS:
            f = objective(a,t)
            r = optimum(t)
            key=str(t)
            if f<r:
                records[key]['below'] +=1
            elif f == r:
                records[key]['ties'].append(a)
    assert n == 110740, n
    for t in WEIGHTS:
        rec=records[str(t)]
        assert rec['below']==0, (t,rec)
        assert sorted(rec['ties'])==expected_ties(t), (t,rec)
        rec['tie_count']=len(rec['ties'])
    return {'schema':'EM_X6_R90_AUTHOR_FINITE_CHECK_V1','q_enumeration_limit':MAX_Q,
            'unoriented_directions':n,'exact_weight_parameters':[str(t) for t in WEIGHTS],
            'direction_parameter_checks':n*len(WEIGHTS),'results':records,
            'scope':'Finite exact Python Fraction crosscheck only; full-lattice result proven symbolically in companion theorem.'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
