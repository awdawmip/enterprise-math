#!/usr/bin/env python3
"""Exact 96-port all-source two-step observer-fiber classification for frozen X6-BRC.
Requires the published PREFIX565 native edge (science pin f42f2906d77f24085c123f3ccfe9667d41caa96d).
"""
from collections import Counter
from fractions import Fraction as F
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, ZERO_ROOT, ACTIONS, edge
import json

assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(ACTIONS) == 6

def pair(w):
    ans=(w[0]+w[1], w[2]+w[3], w[4]+w[5])
    assert ans in ((1,0,0),(0,1,0),(0,0,1))
    return ans

def H(w):
    # integer numerator of residual Y: H=192Y
    return 192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]

def mean(values):
    return sum(map(F,values),F())/len(values)

profiles=Counter()
pair_sources=Counter()
port0=None
M=((0,1,-1),(1,-1,0),(-1,0,1))
for initial in range(96):
    paths=[]; first_pairs=set()
    for a in ACTIONS:
        mid,w=edge(initial,a,ZERO_ROOT)
        first_pairs.add(pair(w))
        for b in ACTIONS:
            end,v=edge(mid,b,ZERO_ROOT)
            paths.append((pair(v),H(w)+H(v)))
    assert len(paths)==36 and len(first_pairs)==1
    support=sorted(set(p for p,h in paths))
    assert len(support)==2
    u,v=support
    d=tuple(u[i]-v[i] for i in range(3))
    X=[int(p==u) for p,h in paths]
    Y=[F(h,192) for p,h in paths]
    EX=mean(X); EY=mean(Y)
    EXY=mean([x*y for x,y in zip(X,Y)])
    # cum(Y,X,X)=E[YX]-E[Y]E[X]-2E[X]E[YX]+2E[Y]E[X]^2
    scalar=EXY-EY*EX-2*EX*EXY+2*EY*EX*EX
    matrix=tuple(tuple(scalar*d[i]*d[j] for j in range(3)) for i in range(3))
    assert scalar != 0
    assert all(sum(row)==0 for row in matrix)
    assert matrix != tuple(tuple(matrix[0][1]*M[i][j] for j in range(3)) for i in range(3))
    profiles[matrix]+=1
    pair_sources[(u,v)]+=1
    if initial==0:
        port0={'atom_table':[
            {'pair':list(p),'H':h,'count':count}
            for (p,h),count in sorted(Counter(paths).items())],
            'scalar':str(scalar),
            'matrix':[[str(e) for e in row] for row in matrix]}
        assert Counter(paths)==Counter({((0,1,0),-4):12,((0,0,1),-1):24})
        assert scalar==F(-1,864)
        assert matrix == ((F(0),F(0),F(0)),(F(0),F(-1,864),F(1,864)),(F(0),F(1,864),F(-1,864)))

assert len(profiles)==15
assert sum(profiles.values())==96
assert sum(pair_sources.values())==96
result={
 'schema':'PREFIX586_R6_NATIVE_PURE_PORT_TWO_STEP_V1',
 'status':'ALL_CHECKS_PASS', 'science_pin':SCIENCE_PIN,
 'initial_port_count':96,'native_labeled_actions':576,
 'native_length_two_paths_examined':96*36,
 'first_pair_deterministic_per_port':True,
 'second_pair_support_cardinality_all_ports':2,
 'all_96_local_cumulant_matrices_rank_one_nonzero':True,
 'nonproportional_to_uniform_M_count':96,
 'distinct_exact_local_matrices':len(profiles),
 'local_matrix_multiplicities':sorted(profiles.values()),
 'port0':port0,
 'scope':'zero root, each of 96 deterministic initial ports, six equiprobable native actions at each of two steps',
 'proof':'finite exhaustive enumeration of 96 x 6 x 6 native ordered action paths, exact Fraction cumulants; two-point pair support yields rank-one tensor factorization',
}
print(json.dumps(result,ensure_ascii=False,indent=2))
