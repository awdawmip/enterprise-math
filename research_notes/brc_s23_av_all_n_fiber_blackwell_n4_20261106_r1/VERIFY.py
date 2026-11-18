#!/usr/bin/env python3
"""Exact rational checks for S23 n>=1 fiber extremum and n=4 deficiency bounds.
Source pin: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
This program checks finite identities/examples; continuous theorem is in PROOF.md.
"""
from fractions import Fraction as F
from math import factorial

p0=(F(1,2), F(1,4), F(1,4))
p1=(F(5,7), F(1,4), F(1,28))
z0=F(7,64)
zmin=F(1,16)
zmax=F(7,16)

def law(a,z):
    return (a,z,1-a-z)

def ends(z):
    return law(max(F(1,2),1-2*z),z),law(min(F(7,8),1-8*z/7),z)

def interpolate(p,q,t):
    return tuple(t*x+(1-t)*y for x,y in zip(p,q))

def tv_power(p,q,n):
    total=F(0)
    for i in range(n+1):
        for j in range(n+1-i):
            k=n-i-j
            w=factorial(n)//(factorial(i)*factorial(j)*factorial(k))
            total+=w*abs(p[0]**i*p[1]**j*p[2]**k-q[0]**i*q[1]**j*q[2]**k)
    return total/2

assert sum(p0)==sum(p1)==1
assert ends(F(1,4))==(p0,p1)
checkcount=0
for i in range(1,100):
    z=zmin+(zmax-zmin)*F(i,100)
    left,right=ends(z)
    if z <= z0:
        lam=(z-zmin)/(z0-zmin)
        l0,h0=ends(z0)
        c=law(F(7,8),zmin)
        pred=(interpolate(l0,c,lam),interpolate(h0,c,lam))
    elif z<=F(1,4):
        lam=4*z
        e=(F(1),F(0),F(0))
        pred=(interpolate(p0,e,lam),interpolate(p1,e,lam))
    else:
        lam=(zmax-z)/(zmax-F(1,4))
        c=law(F(1,2),zmax)
        pred=(interpolate(p0,c,lam),interpolate(p1,c,lam))
    assert (left,right)==pred
    checkcount+=2
for n in range(1,9):
    actual=tv_power(p0,p1,n)
    if n<=6:
        assert actual==F(27,28)**n-F(3,4)**n

assert tv_power(p0,p1,3)==F(5211,10976)
assert tv_power(p0,p1,4)==F(5265,9604)
assert tv_power(p0,p1,7)==F(4369158699,6746464256)
assert tv_power(p0,p1,7)-(F(27,28)**7-F(3,4)**7)==F(176457,30118144)
assert F(5265,19208) < F(801,2401)

for i in range(1,40):
    z=zmin+(zmax-zmin)*F(i,40)
    lo,hi=ends(z)
    L,H=lo[0],hi[0]
    if L==H: continue
    N=1-z
    for alpha,beta in ((F(0),F(0)),(F(0),F(1)),(F(1),F(1)),(F(1,3),F(2,3)),(F(1,4),F(3,4))):
        x=L+alpha*(H-L); y=L+beta*(H-L)
        t=(y-x)/(H-L)
        v=(x-t*L)/N; u=v+t
        assert 0<=v<=1 and 0<=u<=1
        assert t*L+v*N==x and t*H+v*N==y
        checkcount+=4

print('PASS_S23_ALL_N_FIBER_BLACKWELL_AND_N4_EXACT_20261106')
print('continuous theorem proof: three affine common-channel reductions + within-fiber channel')
print('exact channel/range checks:',checkcount)
for n in range(1,9):
    print('n=',n,'D_n=',tv_power(p0,p1,n))
print('delta4_lower=',F(5265,19208),'delta4_constructive_upper=',F(801,2401))
