#!/usr/bin/env python3
"""R132: full-integer Port-10 dominance + exact 16-corner chamber certificate.
All numerical comparisons use integers or Fraction. No external packages.
"""
from fractions import Fraction as Q
from itertools import product

BANK = [(1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),
        (1,3,-1),(3,-4,1),(4,-1,0),(3,2,-1),(4,-4,1),
        (5,-1,0),(5,-4,1),(6,-1,0),(3,-7,2),(6,-4,1),
        (7,-1,0),(7,2,-1),(9,-5,1)]
ANCHOR = (6,-1,0)
PAIRS = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def port(a):
    return max(sum(max(v,0) for v in a), sum(max(-v,0) for v in a))

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

def capacities(w):
    return tuple(w[i]+w[j] for i,j in PAIRS)

def score(a,w):
    return max(Q(v,s) for v,s in zip(gaps(a),capacities(w)))

def check(w0,rad,anchor_pair,expected_names):
    w0=tuple(map(Q,w0))
    rr=Q(1,rad)
    corners=[tuple(w0[i]*(1+rr*t[i]) for i in range(4))
             for t in product((-1,1),repeat=4)]
    bank_witnesses={}
    for b in BANK:
        choices=[j for j in range(6) if all(
             gaps(b)[j]*capacities(w)[anchor_pair]
             >=3*capacities(w)[j] for w in corners)]
        assert choices, ("bank lower bound", b)
        bank_witnesses[b]=choices[0]
    assert all(all(gaps(ANCHOR)[j]*capacities(w)[anchor_pair]
                   <=3*capacities(w)[j] for j in range(6))
               for w in corners)
    eta0=Q(3,capacities(w0)[anchor_pair])
    near=[a for a in E if 2*score(a,w0)<3*eta0]
    assert set(near)==set(expected_names) and len(near)==8
    out_witnesses={}
    equalities=[]
    for a in E:
        if a in near:
            for t,w in zip(product((-1,1),repeat=4),corners):
                for j in range(6):
                    gap=9*capacities(w)[j]-2*gaps(a)[j]*capacities(w)[anchor_pair]
                    assert gap>=0,("near condition",a,j,t,gap)
                    if gap==0:equalities.append((a,j,t))
        else:
            choices=[j for j in range(6) if all(
                 2*gaps(a)[j]*capacities(w)[anchor_pair]
                 >=9*capacities(w)[j] for w in corners)]
            assert choices, ("out lower bound",a)
            out_witnesses[a]=choices[0]
    assert equalities, "radius was not shown sharp"
    print('BASE',tuple(map(int,w0)), 'eta',eta0,
          'sharp-open-radius',rr,'bank',len(bank_witnesses),
          'envelope',len(E),'near',len(near),'outside',len(out_witnesses),
          '16 corners PASS')
    print(' first equality',equalities[0],
          'bank witnesses',list(bank_witnesses.values()),
          'outside witnesses',list(out_witnesses.values()))

V=[]
for a in product(range(-10,11),repeat=3):
    if not any(a) or next(t for t in a if t<0 or t>0)<0 or port(a)>10:
        continue
    V.append(a)
assert len(V)==1935
B=set(BANK)
assert len(B)==18
assert all(any(all(u<=v for u,v in zip(gaps(b),gaps(a))) for b in B)
           for a in V)
E=[a for a in V if not any(all(2*u>=3*v for u,v in zip(gaps(a),gaps(b))) for b in B)]
assert len(E)==20 and len(V)-len(E)==1915
print('FULL FINITE INPUT: 1935 directions; B18 dominance PASS; E20 exclusion PASS')

check((136,8,176,185),369,0,
      [(1,0,0),(1,3,-1),(4,-4,1),(5,-4,1),
       (5,-1,0),(6,-1,0),(7,-1,0),(9,-5,1)])
check((722,465,240,48),721,5,
      [(1,0,0),(3,-4,1),(3,3,-1),(4,-4,1),
       (6,-1,0),(7,-8,2),(7,-1,0),(9,-5,1)])
print('ALL PASS')
