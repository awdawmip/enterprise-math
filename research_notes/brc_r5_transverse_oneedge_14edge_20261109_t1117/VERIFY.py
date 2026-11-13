#!/usr/bin/env python3
"""Exact one-edge transverse lift of an R5 seven-LR-node Blackwell coupling.
All checks use Python standard library Fraction, including both end points.
"""
from fractions import Fraction as F
R=tuple(map(F,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
X=tuple(map(F,'999/1000 1/6 999/1000 1/20 29/240 11/160 1/120'.split()))
Y=tuple(map(F,'1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200'.split()))
S=((0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),(2,3),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
E0=tuple(map(F,'33553/432000 3997/432000 3997/540000 0 510479933/29442744000 2893155797/8178540000 6636239129/147213720000 222511289/4089270000 318755011/3680343000 222511289/4089270000 172449787/1363090000 219439/545236000 172449787/2180944000 38053/432000'.split()))
D=tuple(map(F,'-247/1620 3211/14580 -22477/36450 3211/8100 -247/3645 494/2025 -3211/18225 -494/2025 3211/4050 -494/2025 494/2025 -3211/8100 247/1620 -247/1620'.split()))
HI=F(17774559,17507527960)
SA={(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5)}
SB={(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5)}
ATLAS=SA|SB

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def x(e):return (*X[:6],X[6]+e)
def weights(e):return tuple(a+e*d for a,d in zip(E0,D))
def check(e):
    src=x(e);nu=mass(src);mu=mass(Y);W=weights(e)
    assert len(S)==len(set(S))==14 and len(W)==14
    assert src[0]==src[2] and Y[0]==1 and Y[6]==Y[1]/10
    assert min(slack(src)+slack(Y))>=0
    assert times(src)==times(Y)==(F(17609,6000),F(33857,12000))
    assert sum(nu)==sum(mu)==1 and min(nu+mu)>=0
    assert min(W)>=0
    for i in range(7):
        assert sum((v for (ii,j),v in zip(S,W) if ii==i),F(0))==mu[i]
    for j in range(7):
        assert sum((v for (i,jj),v in zip(S,W) if jj==j),F(0))==nu[j]
        assert sum((R[i]*v for (i,jj),v in zip(S,W) if jj==j),F(0))==R[j]*nu[j]
    Phi=F(23,5)*(mu[0]-nu[0])+3*(mu[1]-nu[1])+2*(mu[2]-nu[2])+mu[3]-nu[3]
    assert Phi==F(3211,8100)*e==W[S.index((5,1))]
    gap=sum((v for edge,v in zip(S,W) if edge not in ATLAS),F(0))
    assert gap==F(8555233477,73606860000)-F(51623,72900)*e
    return sum(v>0 for v in W),gap,Phi

assert HI<F(1,120)
assert -E0[S.index((5,5))]/D[S.index((5,5))]==HI
assert all(w>0 for w in E0 if w!=0) and E0[S.index((5,1))]==0
assert all(w+HI*d>=0 for w,d in zip(E0,D))
assert all(w+HI*d>0 for e,w,d in zip(S,E0,D) if e!=(5,5))
for e,n in ((F(0),13),(F(1,100000),14),(F(1,1000),14),(HI,13)):
    count,_,_=check(e)
    assert count==n
print('PASS_BOTH_ENDPOINTS_21_LR_COUPLING_EQUATIONS_AND_ALL_PHYSICAL_SLACKS')
print('PASS_AFFINE_IDENTITY_THEREFORE_ALL_REAL_EPSILON_IN_CLOSED_INTERVAL')
print('PASS_UNIQUE_TRANSVERSE_BRIDGE_EDGE_(5,1)_PHI_EXACT')
print('PASS_14_POSITIVE_EDGES_OPEN_INTERVAL_AND_13_AT_ENDPOINTS')
print('MAXIMAL_EPSILON_FOR_THIS_NONNEGATIVE_14_EDGE_AFFINE_CHART',HI)
print('EXACT_ATLAS_ESCAPE_COST','8555233477/73606860000 - (51623/72900)*epsilon')
print('EPSILON_1/1000',check(F(1,1000)))
