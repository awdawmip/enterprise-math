#!/usr/bin/env python3
"""Exact rational checker: R5 variance/time cost and seedless LR tube."""
from fractions import Fraction as F
from itertools import product
from random import Random

q2 = (F(1,2),F(1,2))
r2 = (F(3,4),F(5,4))
q3 = ((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
r3 = (F(1,2),F(1),F(3,2))
side = {0:(F(509,900),F(382,900),F(9,900)),
        2:(F(9,900),F(382,900),F(509,900))}
middle = ((F(47,180),F(43,90),F(47,180)),
          (F(67,162),F(14,81),F(67,162)))
r4 = (F(1,10),F(1),F(19,10))
def q4(i,j):
    return middle[i] if j==1 else side[j]

c2=sum(p*(r-1)**2 for p,r in zip(q2,r2))
c3=tuple(sum(p*(r-r2[i])**2 for p,r in zip(q3[i],r3)) for i in range(2))
c4=tuple(tuple(sum(p*(r-r3[j])**2 for p,r in zip(q4(i,j),r4))
           for j in range(3)) for i in range(2))
assert c2 == F(1,16)
assert c3 == (F(11,80),F(3,40))
assert c4 == ((F(1081,5000),F(423,1000),F(1081,5000)),
              (F(1081,5000),F(67,100),F(1081,5000)))
assert all(c >= F(1,16) for c in (c2,)+c3+sum(c4,()))
assert sum(q2)==1 and sum(p*r for p,r in zip(q2,r2))==1
for i in range(2):
    assert sum(q3[i])==1
    assert sum(p*r for p,r in zip(q3[i],r3))==r2[i]
    for j in range(3):
        assert sum(q4(i,j))==1
        assert sum(p*r for p,r in zip(q4(i,j),r4))==r3[j]

def profile(g,a,z):
    masses={r:F(0) for r in (F(1,10),F(1,2),F(3,4),F(1),
                             F(5,4),F(3,2),F(19,10))}
    masses[F(1)]+=1-g
    tq=F(1)+g
    qv=g*c2
    for i in range(2):
        ui=g*a[i]
        masses[r2[i]]+=q2[i]*g*(1-a[i])
        tq+=q2[i]*ui
        qv+=q2[i]*ui*c3[i]
        for j in range(3):
            bij=q2[i]*ui*q3[i][j]
            masses[r3[j]]+=bij*(1-z[j])
            tq+=bij*z[j]
            qv+=bij*z[j]*c4[i][j]
            for k in range(3):
                masses[r4[k]]+=bij*z[j]*q4(i,j)[k]
    var=sum(m*(r-1)**2 for r,m in masses.items())
    assert sum(masses.values())==1
    assert sum(r*m for r,m in masses.items())==1
    assert var==qv
    assert var>=F(1,16)*(tq-1)
    tp=F(1)+g+sum(q2[i]*r2[i]*g*a[i] for i in range(2))
    tp+=sum(q2[i]*g*a[i]*q3[i][j]*r3[j]*z[j]
            for i in range(2) for j in range(3))
    return masses,tp,tq,var

def tube(tq,masses,var,theta,eta):
    assert abs(eta)<=F(5,72)*(tq-1)*min(theta,1-theta)
    b=F(0) if var==0 else -eta/var
    if var==0: assert tq==1 and eta==0
    assert abs(b)<=F(10,9)*min(theta,1-theta)
    t={r:theta+b*(r-1) for r in masses}
    assert all(0<=p<=1 for p in t.values())
    eq=sum(masses[r]*t[r] for r in masses)
    ep=sum(r*masses[r]*(1-t[r]) for r in masses)
    assert eq==theta and ep==1-theta+eta
    return t

num=0
for bits in product((F(0),F(1)),repeat=6):
    masses,tp,tq,var=profile(bits[0],bits[1:3],bits[3:])
    assert 1<=tp<=4 and 1<=tq<=4
    assert (var==F(1,16)*(tq-1))==(bits[0]==0 or
           (bits[1]==0 and bits[2]==0))
    num+=1
assert num==64

rng=Random(202611060744)
for k in range(640):
    q=lambda:F(rng.randrange(21),20)
    masses,tp,tq,var=profile(q(),(q(),q()),(q(),q(),q()))
    theta=q()
    eta=F(rng.randrange(-20,21),20)*F(5,72)*(tq-1)*min(theta,1-theta)
    tube(tq,masses,var,theta,eta)
M,tp,tq,var=profile(F(1),(F(0),F(0)),(F(0),F(0),F(0)))
assert (tp,tq,var)==(F(2),F(2),F(1,16))
t=tube(tq,M,var,F(1,2),F(5,144))
assert t[F(3,4)]==F(23,36) and t[F(5,4)]==F(13,36)
print('VARIANCE_NODE_VALUES',c2,c3,c4)
print('EXPLICIT_BOUNDARY_POINT','eP=',F(77,144),'eQ=',F(1,2),'TP=',tp,'TQ=',tq)
print('VERIFY_TIMING_PROFILES',num,'complete deterministic +',640,'random rational')
print('PASS_EXACT_R5_LR_VARIANCE_TIME_TUBE')
