#!/usr/bin/env python3
"""Exact rational BRC N=4 five-symbol bound verification, author-side only.

No network, no float, no native Source admission. Python standard library only.
"""
from fractions import Fraction as F
from itertools import product

W = {
    'AU': {'Q': (10,10), 'P': (9,11)},
    'AV': {'Q': (20,20), 'P': (5,5)},
    'BU': {'Q': (15,15), 'P': (3,27)},
    'BV': {'Q': (15,15), 'P': (30,30)},
}
# Each W entry is weight per K leaf with denominator 240.
for b in ('P','Q'):
    leaves=[F(W[s][b][j],240) for s in W for j in (0,1) for k in (0,1)]
    assert len(leaves)==16 and all(x>0 for x in leaves)
    assert sum(leaves)==1

p = {(s,b):F(W[s][b][1], sum(W[s][b])) for s in W for b in ('P','Q')}
assert [p['AU','Q'],p['AU','P'],p['BU','Q'],p['BU','P']]==[F(1,2),F(11,20),F(1,2),F(9,10)]

rows=[('AU','Q'),('AU','P'),('AV','Q'),('BU','Q'),('BU','P'),('BV','Q')]
cols=['AU','AV','BU','BV','AU1','BU1']
def event_probability(s,b,h,rate=None):
    a=p[s,b] if rate is None else rate
    if h in W: return F(int(s==h))
    if h=='AU1': return a if s=='AU' else F(0)
    if h=='BU1': return a if s=='BU' else F(0)
    raise ValueError(h)
A=[[event_probability(s,b,h) for h in cols] for s,b in rows]

# Exact Gauss-Jordan, simultaneous determinant & inverse.
def inverse_det(M):
    n=len(M); D=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    det=F(1)
    for col in range(n):
        piv=next(i for i in range(col,n) if D[i][col]!=0)
        if piv!=col:
            D[col],D[piv]=D[piv],D[col];det=-det
        q=D[col][col];det*=q
        D[col]=[x/q for x in D[col]]
        for i in range(n):
            if i!=col:
                f=D[i][col];D[i]=[x-f*y for x,y in zip(D[i],D[col])]
    return det,[row[n:] for row in D]
det,inv=inverse_det(A)
assert det==F(1,50)
assert inv==[[F(11),F(-10),0,0,0,0],
             [0,0,1,0,0,0],
             [0,0,0,F(9,4),F(-5,4),0],
             [0,0,0,0,0,1],
             [-20,20,0,0,0,0],
             [0,0,0,F(-5,2),F(5,2),0]]
# The norm ||A^{-T}||_{infinity -> 1} is attained at a sign vector.
maxnorm=F(-1); maximizer=None
for sg in product((-1,1),repeat=6):
    w=[sum(inv[j][i]*sg[j] for j in range(6)) for i in range(6)]
    nrm=sum(map(abs,w))
    if nrm>maxnorm:
        maxnorm=nrm;maximizer=sg
assert maxnorm==F(143,2)
lower=1/maxnorm
assert lower==F(2,143)
# The unrestricted rank-five perturbation witness saturates this bound.
y=(-1,-1,-1,-1,1,1)
w=[sum(inv[j][i]*y[j] for j in range(6)) for i in range(6)]
assert w==[F(-31),F(30),F(-1),F(-19,4),F(15,4),F(-1)]
assert sum(map(abs,w))==maxnorm
u=[F(1 if x>0 else -1,maxnorm) for x in w]
assert sum(w[i]*u[i] for i in range(6))==1
B=[[A[i][j]-u[i]*y[j] for j in range(6)] for i in range(6)]
assert max(abs(A[i][j]-B[i][j]) for i in range(6) for j in range(6))==lower
assert all(sum(w[i]*B[i][j] for i in range(6))==0 for j in range(6))

# Five alphabet states: AU* / AV / BU_Q / BU_P / BV. Its internal J law:
rate={(s,b): (F(21,40) if s=='AU' else p[s,b]) for s in W for b in ('P','Q')}
assert max(abs(rate[s,b]-p[s,b]) for s in W for b in ('P','Q'))==F(1,40)

# Fully lawful stage-three S23 deterministic terminal policies use the six
# contemporaneous likelihood-ratio classes. Exhaust all 64, with the typed
# BU-only Z readout for each chosen epsilon. This is an exact subset check;
# the all-policy bound is analytic by data processing.
classes=['AU0','AU1','AV','BU0','BU1','BV']
cls=lambda s,j: (s if s in ('AV','BV') else s+str(j))

def public_distribution(s,b,decisions,epsilon,rate_J):
    d={}
    for j in (0,1):
        mass=rate_J if j else 1-rate_J
        choice=decisions[cls(s,j)]
        if s=='BU':
            for z in (0,1):
                pe=(1-epsilon) if z==j else epsilon
                key=('T3',choice,z)
                d[key]=d.get(key,F(0))+mass*pe
        else:
            key=('T3',choice,'absent')
            d[key]=d.get(key,F(0))+mass
    assert sum(d.values())==1
    return d

def tv(a,b):
    return sum(abs(a.get(t,F(0))-b.get(t,F(0))) for t in set(a)|set(b))/2

max_gap=F(0)
checks=0
for epsilon in (F(0),F(1,8),F(1,4),F(1,2)):
    for bits in product((0,1),repeat=6):
        dec=dict(zip(classes,bits))
        for s in W:
            for b in ('P','Q'):
                a=public_distribution(s,b,dec,epsilon,p[s,b])
                c=public_distribution(s,b,dec,epsilon,rate[s,b])
                gap=tv(a,c)
                assert gap <= F(1,40)
                max_gap=max(max_gap,gap); checks+=1
assert checks==4*64*8 and max_gap==F(1,40)
print('LEAF_LAWS=2x16 STRICT_POSITIVE NORMALIZED')
print('RANK_WITNESS_DET=',det)
print('INVERSE_LINF_TO_L1=',maxnorm)
print('ROBUST_FIVE_STATE_LOWER=',lower)
print('UNRESTRICTED_RANK_RELAXATION_ATTAINS_LOWER=True')
print('CONSTRUCTIVE_FIVE_STATE_UPPER=',F(1,40))
print('EXACT_S23_DETERMINISTIC_T3_CHECKS=',checks)
print('MAX_CONSTRUCTED_T3_TV=',max_gap)
print('PASS_BRC_N4_FIVE_SYMBOL_QUANTITATIVE_SANDWICH_20261031')
