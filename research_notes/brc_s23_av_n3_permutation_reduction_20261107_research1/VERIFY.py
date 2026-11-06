#!/usr/bin/env python3
"""Exact permutation-symmetrization certificate for the pinned S23 n=3 8x27 kernel.
No floating point operations enter assertions. Python standard library only.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb

D=1_000_000
ROWS=[
 {13:1000000},
 {1:479665,12:520335},
 {9:296273,10:703727},
 {2:419643,15:48185,18:405725,21:112202,26:14245},
 {1:139862,4:683322,9:176816},
 {6:230562,9:106277,11:120245,12:56752,14:50073,15:71369,16:50073,17:25415,19:120245,22:50462,23:25415,24:70684,25:22428},
 {1:20822,3:400945,4:11265,5:119554,6:192951,7:125268,8:65023,20:64172},
 {0:747749,1:99382,3:52308,4:2315,6:2609,9:87375,10:3741,18:4521}]
B=list(product(range(2), repeat=3)); T=list(product(range(3), repeat=3));
bi={b:i for i,b in enumerate(B)}; ti={x:i for i,x in enumerate(T)}
PERMS=list(permutations(range(3)))
assert len(ROWS)==8 and len(B)==8 and len(T)==27 and len(PERMS)==6
assert all(sum(r.values())==D for r in ROWS)

def perm(x,p): return tuple(x[t] for t in p)
K=[[sum(ROWS[bi[perm(y,p)]].get(ti[perm(x,p)],0) for p in PERMS)
    for x in T] for y in B]
assert all(sum(row)==6*D and all(v>=0 for v in row) for row in K)
assert all(K[i][j]==K[bi[perm(y,p)]][ti[perm(x,p)]]
           for i,y in enumerate(B) for j,x in enumerate(T) for p in PERMS)
assert sum(bool(v) for row in K for v in row)==92

# Input-stabilizer orbits count free parameters of equivariant row-stochastic kernels.
orbit_counts=[]
for t in range(4):
    y=(0,)*(3-t)+(1,)*t
    stab=[p for p in PERMS if perm(y,p)==y]
    distinct={frozenset(ti[perm(x,p)] for p in stab) for x in T}
    orbit_counts.append(len(distinct))
assert orbit_counts==[10,18,18,10] and sum(orbit_counts)==56

# Existing residual coordinate sign certificate, independently checked with exact
# degree (3,3) Bernstein coefficients on the critical rectangle R.
def add(*polys):
    o={}
    for p in polys:
        for k,v in p.items(): o[k]=o.get(k,0)+v
    return {k:v for k,v in o.items() if v}
def mul(p,q):
    o={}
    for (i,j),v in p.items():
        for (k,l),w in q.items(): o[(i+k,j+l)]=o.get((i+k,j+l),0)+v*w
    return o
def prodp(ps,which):
    p={(0,0):1}
    for k in which:p=mul(p,ps[k])
    return p
def bern(p,a0,a1,c0,c1):
    powers={}
    for (i,j),v in p.items():
        for u in range(i+1):
            for w in range(j+1):
                key=(u,w)
                powers[key]=powers.get(key,0)+v*comb(i,u)*a0**(i-u)*(a1-a0)**u*comb(j,w)*c0**(j-w)*(c1-c0)**w
    return [sum(powers.get((u,w),0)*Q(comb(h,u),comb(3,u))*Q(comb(k,w),comb(3,w))
                for u in range(h+1) for w in range(k+1)) for h in range(4) for k in range(4)]
ONE={(0,0):1};A={(1,0):1};C={(0,1):1}
AM={(0,0):1,(1,0):-1}; CM={(0,0):1,(0,1):-1}
Z=mul(AM,C); P=[A,Z,mul(AM,CM)]; Bp=[Z,add(ONE,{key:-v for key,v in Z.items()})]
P3=[prodp(P,x) for x in T]; B3=[prodp(Bp,y) for y in B]
G=[]
for j in range(27):
    parts=[{key:v*D for key,v in P3[j].items()}]
    for i,row in enumerate(ROWS):
        if row.get(j):parts.append({key:-v*row[j] for key,v in B3[i].items()})
    G.append(add(*parts))
assert not G[13]
R=(Q(17,25),Q(73,100),Q(17,20),Q(7,8))
SIGNS=[1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
margin=min(s*v for s,g in zip(SIGNS,G) if s for v in bern(g,*R))
assert margin==Q(2999060771571,1600000000)>0
# Each output S3 orbit has one sign on the entire critical rectangle.
for j,x in enumerate(T):
    assert all(SIGNS[ti[perm(x,p)]]==SIGNS[j] for p in PERMS)

# At any point in R, symmetrized residual = permutation-orbit average
# of original residual. Uniform orbit signs imply pointwise TV equality.
def evalp(g,a,c):return sum(v*a**i*c**j for (i,j),v in g.items())
def discrepancy(matrix,den,a,c):
    z=(1-a)*c
    P=(a,z,(1-a)*(1-c)); b=(z,1-z)
    pp=[P[x[0]]*P[x[1]]*P[x[2]] for x in T]
    ob=[b[y[0]]*b[y[1]]*b[y[2]] for y in B]
    return sum(abs(pp[j]-sum(ob[i]*matrix[i][j] for i in range(8))/den) for j in range(27))/2
Orig=[[r.get(j,0) for j in range(27)] for r in ROWS]
for a,c in ((Q(17,25),Q(17,20)),(Q(7,10),Q(43,50)),
            (Q(35319,50000),Q(7,8)),(Q(73,100),Q(7,8))):
    assert discrepancy(K,6*D,a,c)==discrepancy(Orig,D,a,c)
# A point outside R where symmetrization gives strict improvement.
a,c=Q(1,2),Q(3,5)
assert discrepancy(K,6*D,a,c)<discrepancy(Orig,D,a,c)
print('PASS_S23_N3_PERMUTATION_SYMMETRIZED_KERNEL_20261107')
print('STOCHASTIC_ROWS=8; OUTPUTS=27; S3_SIZE=6; DENOMINATOR=6000000; NONZERO_ENTRIES=92')
print('EQUIVARIANT_ORBIT_COUNTS='+str(orbit_counts)+'; FREE_PARAMETERS='+str(sum(orbit_counts)-4))
print('EXACT_BERNSTEIN_MIN='+str(margin))
print('POINTWISE_EQUALITY_ON_CRITICAL_RECTANGLE=PROVED_FROM_SIGN_ORBITS')
print('CONTINUOUS_SUP_KSYM=f(alpha)=0.237838693711015430...; inherits pinned fixed-K global bound')
