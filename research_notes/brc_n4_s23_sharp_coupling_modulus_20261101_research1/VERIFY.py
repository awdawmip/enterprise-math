#!/usr/bin/env python3
"""Exact rational checks for the sharp three-stage causal coupling modulus (BRC N4 S23)."""
from fractions import Fraction as Q
from itertools import product

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
SPECS=('34 24 34 24','34 23 34 34','34 34 34 23',
       '24 24 12 12','12 12 24 34','12 13 23 24',
       '23 34 12 13','24 34 12 14','13 12 13 13')
Q10=((Q(1,2),Q(0),Q(1,4),Q(1,4)),
     (Q(1,2),Q(0),Q(1,2),Q(0)),
     (Q(1,2),Q(0),Q(0),Q(1,2)),
     (Q(1,2),Q(1,2),Q(0),Q(0)))

def stopped(a,b,c):
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),Q(0))/2

def coupling(a,b,c,ap,bp,cp):
    s1=1-max(a,ap)
    s2=1-max(b,bp)
    return abs(a-ap)+s1*abs(b-bp)+s1*s2*abs(c-cp)

def prep(theta):
    laws=[stopped(theta[A[x]],theta[B[x]],theta[C[x]]) for x in range(6)]
    return tuple(tuple(sum((Q(M20[i][x],20)*laws[x][t] for x in range(6)),Q(0))
                       for t in range(4)) for i in range(6))

def prep_bound(theta,phi):
    vals=[coupling(theta[A[x]],theta[B[x]],theta[C[x]],
                   phi[A[x]],phi[B[x]],phi[C[x]]) for x in range(6)]
    return max(sum((Q(M20[i][x],20)*vals[x] for x in range(6)),Q(0))
               for i in range(6))

def decode(rows):
    return tuple(tuple(sum((Q(M20[i][x],20)*rows[GROUP[x]][t]
                            for x in range(6)),Q(0)) for t in range(4))
                 for i in range(6))

def parse_spec(spec):
    rows=[]
    for token in spec.split():
        v=[Q(0)]*4
        for t in token: v[int(t)-1]+=Q(1,2)
        rows.append(tuple(v))
    return tuple(rows)

BANK=tuple(decode(parse_spec(spec)) for spec in SPECS)+(decode(Q10),)

def risk(theta):
    p=prep(theta)
    return min(max(tv(p[i],q[i]) for i in range(6)) for q in BANK)

# Exhaustive rational check of all 5^3 x 5^3 pairs of latent stopping laws.
grid=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
triples=list(product(grid,repeat=3))
checked=0
for u in triples:
    for v in triples:
        delta=tuple(abs(x-y) for x,y in zip(u,v))
        coupling_bound=coupling(*u,*v)
        product_bound=1-(1-delta[0])*(1-delta[1])*(1-delta[2])
        assert tv(stopped(*u),stopped(*v))<=coupling_bound<=product_bound<=1
        checked+=1
assert checked==15625
print('ALL_5^3_BY_5^3_EXACT_LATENT_PAIRS=',checked)

# Attainment for every epsilon, including strict interior rational values.
for epsilon in (Q(1,7),Q(1,3),Q(1,2),Q(3,4),Q(1)):
    theta=(Q(0),)*11
    phi=(epsilon,)*11
    expected=1-(1-epsilon)**3
    assert coupling(0,0,0,epsilon,epsilon,epsilon)==expected
    assert all(tv(x,y)==expected for x,y in zip(prep(theta),prep(phi)))
    assert prep_bound(theta,phi)==expected
    print('SHARP_EPS=',epsilon,'EXACT_TV=',expected)

# Fixed ten-label bank: both source-aware and uniform continuity bounds.
examples=(( (Q(0),)*11,(Q(1,2),)*11),
          ( tuple(Q(k,20) for k in range(11)),
            tuple(Q(k+2,20) for k in range(11))),
          ( tuple(Q(k%3,3) for k in range(11)),
            tuple(Q((k+1)%3,3) for k in range(11))))
for n,(theta,phi) in enumerate(examples,1):
    d=max(abs(x-y) for x,y in zip(theta,phi))
    strong=prep_bound(theta,phi)
    uniform=1-(1-d)**3
    true=max(tv(p,q) for p,q in zip(prep(theta),prep(phi)))
    diff=abs(risk(theta)-risk(phi))
    assert diff<=true<=strong<=uniform
    print('TEN_BANK_PAIR',n,'|DELTA|=',d,'|RISK_DIFF|=',diff,
          '|PREP_TV|=',true,'|SOURCE_BOUND|=',strong,'|UNIFORM|=',uniform)

# Nearest-vertex grid certificate: a uniform cell width h=1/2 or 1/10.
for h in (Q(1,2),Q(1,10)):
    new=1-(1-h/2)**3
    old=3*h/2
    assert 0<new<old
    print('MESH_WIDTH=',h,'SHARP_SOURCE_MODULUS_GAP=',new,
          'PREVIOUS_LINEAR_GAP=',old)
print('PASS_BRC_N4_S23_SHARP_COUPLING_MODULUS_20261101')
