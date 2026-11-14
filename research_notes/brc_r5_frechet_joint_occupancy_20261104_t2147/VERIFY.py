"""Exact finite checks for R5 joint-coupling occupancy lift.
Auxiliary model with non-absorbing sequential decisions, not original R5 stops.
Python standard library, exact Fraction only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

def compositions(n,m):
    if m==1:
        yield (n,)
    else:
        for a in range(n+1):
            for tail in compositions(n-a,m-1):
                yield (a,)+tail

def extract(prob,k):
    row0,row1=prob
    x=sum(row1)
    y=tuple(row0[i]+row1[i] for i in range(1,k+1))
    z=tuple(row1[i] for i in range(1,k+1))
    return x,y,z

def full_constraints(x,y,z):
    if len(y)!=len(z):return False
    return (all(v>=0 for v in y+z)
            and all(z[i]<=y[i] for i in range(len(y)))
            and sum(y)<=1 and sum(z)<=x<=1-sum(y)+sum(z))

def reconstruct(x,y,z):
    p00=1-x-sum(y)+sum(z)
    p10=x-sum(z)
    row0=(p00,)+tuple(y[i]-z[i] for i in range(len(y)))
    row1=(p10,)+tuple(z)
    assert min(row0+row1)>=0
    assert sum(row0+row1)==1
    return row0,row1

def phi(x,y,z,A,B,C):
    return tuple(x*A[t]+sum(y[i]*B[i][t]+z[i]*C[i][t]
            for i in range(len(y))) for t in range(len(A)))

def test(k,n):
    seen=0
    for masses in compositions(n,2*(k+1)):
        entries=tuple(F(c,n) for c in masses)
        p=(entries[:k+1],entries[k+1:])
        x,y,z=extract(p,k)
        assert full_constraints(x,y,z)
        assert reconstruct(x,y,z)==p
        assert sum(entries)==1
        seen+=1
    assert seen==comb(n+2*(k+1)-1,2*(k+1)-1)
    independent=0
    for ix,*iy in product(range(n+1),repeat=k+1):
        x=F(ix,n)
        y=tuple(F(a,n) for a in iy)
        if sum(y)>1:continue
        z=tuple(x*v for v in y)
        assert full_constraints(x,y,z)
        p=reconstruct(x,y,z)
        for i in range(k+1):
            marginal=1-sum(y) if i==0 else y[i-1]
            assert p[0][i]==(1-x)*marginal
            assert p[1][i]==x*marginal
        independent+=1
    return seen,independent

assert test(1,6)==(84,49)
assert test(2,6)==(462,196)
A=(F(1),F(0),F(0),F(0))
B=[(F(0),F(1),F(0),F(0))]
C=[(F(0),F(0),F(1),F(0))]
W=phi(F(1,2),(F(1,2),),(F(1,2),),A,B,C)
assert W==(F(1,2),F(1,2),F(1,2),F(0))
assert full_constraints(F(1,2),(F(1,2),),(F(1,2),))
assert F(1,2)!=F(1,2)*F(1,2)
E0=phi(F(0),(F(0),),(F(0),),A,B,C)
E1=phi(F(1),(F(1),),(F(1),),A,B,C)
assert tuple((a+b)/2 for a,b in zip(E0,E1))==W
poly=lambda d:d*d+2*d-F(1,4)
assert poly(F(118,1000))<0<poly(F(119,1000))
vertices=[E0,phi(F(0),(F(1),),(F(0),),A,B,C),
          phi(F(1),(F(0),),(F(0),),A,B,C),E1]
directions=0
for coeff in product(range(-2,3),repeat=4):
    h=max(sum(c*v for c,v in zip(coeff,point)) for point in vertices)
    assert all(sum(c*v for c,v in zip(coeff,point))<=h for point in vertices)
    directions+=1
assert directions==625
print('k=1: 84 exact joint distributions (denominator 6), 49 independent policies')
print('k=2: 462 exact joint distributions (denominator 6), 196 independent policies')
print('W=(1/2,1/2,1/2,0) in FULL and conv(LR), not in LR')
print('Exact infinity-distance to LR: sqrt(5)/2 - 1, strictly between 118/1000 and 119/1000')
print('625 integer signed directions on four coordinates checked against endpoint support')
print('PASS_EXACT_R5_FRECHET_COUPLING_LIFT')
