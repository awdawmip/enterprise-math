#!/usr/bin/env python3
"""Exact rational checks: nested two-collision signed-support no-go."""
from fractions import Fraction as F
from itertools import product

s=(F(1,2),F(1),F(2),F(3))
t=(F(1),F(2),F(4),F(5))
r1=F(3,2); r2=F(3)
weights=(F(1,4),F(1,4))
zA=(F(3,8),F(1,8),F(1,8),F(3,8))
zB=(F(1,8),F(3,8),F(3,8),F(1,8))

def kernels(g):
    c=(3*g/2,F(1,5)-5*g/4,F(1,5)-5*g/4,g)
    a=(F(9,25),F(0),F(0),F(6,25))
    b=(F(0),F(3,10),F(3,10),F(0))
    return (tuple(c[i]+a[i] for i in range(4)),
            tuple(c[i]+b[i] for i in range(4)))

def check(k, sig, parent):
    assert all(p>0 for p in k)
    assert sum(k)==1 and sum(p*v for p,v in zip(k,sig))==parent
    assert sum(p*v/parent for p,v in zip(k,sig))==1

def phi(u,lam):
    return min(lam[0]*u,lam[1])

def expected(k,sig,lam):
    return sum(p*phi(v,lam) for p,v in zip(k,sig))

def opt(qA,qB,lam):
    for q in (qA,qB):check(q,s,r1)
    for z in (zA,zB):check(z,t,r2)
    be1=r1*lam[2]+lam[3]
    be2=r2*lam[2]+lam[3]
    d1=tuple(be1+expected(q,s,lam)-phi(r1,lam) for q in (qA,qB))
    d2=tuple(be2+expected(z,t,lam)-phi(r2,lam) for z in (zA,zB))
    qstar=(qA[3],qB[3])
    base=sum(weights[i]*phi(r1,lam) for i in range(2)) + F(1,2)*phi(F(1,2),lam)+lam[2]+lam[3]
    def value(a):
        return base+sum(weights[i]*a[i]*(d1[i]+qstar[i]*a[i+2]*d2[i]) for i in range(2))
    full=min(value(x) for x in product((0,1),repeat=4))
    lr=min(value((x,x,y,y)) for x,y in product((0,1),repeat=2))
    return base,d1,d2,full,lr,lr-full

lam=(F(1),F(1),F(1),-F(27,20))
for i in range(1,160):
    g=F(i,1000)
    out=opt(*kernels(g),lam)
    gap=min(F(3,400)+3*g/16,F(3,80)-3*g/16)
    assert out[1]==(-F(3,100)-3*g/4,F(3,20)-3*g/4)
    assert out[2]==(F(33,20),F(33,20))
    assert out[3]==F(2,5)-F(3,400)-3*g/16
    assert out[4]==F(2,5)+min(F(0),F(3,100)-3*g/8)
    assert out[5]==gap and gap>F(3,400)

for g in (F(1,10000),F(2,25),F(23,200),F(159,1000)):
    a=opt(*kernels(g),lam)
    print("FIXED-LAMBDA","g="+str(g),"Vfull",a[3],"VLR",a[4],"gap",a[5])
g=F(2,25)
qA,qB=kernels(g)
assert qA[0]==F(12,25) and qB[0]==F(3,25)
witness=(F(31,100),F(19,50),F(11,8),F(5,4))
assert sum(x*y for x,y in zip(lam,witness))==F(151,400)
a=opt(qA,qB,lam)
assert a[3]==F(151,400) and a[4]==F(2,5) and a[5]==F(9,400)
print("PEAK-WITNESS",witness,"L",F(151,400),"distance_lower_bound",F(3,580))
print("UNIFORM-STRICT-GAP",F(3,400),"UNIFORM-distance-inf-lower",F(1,580))

qA,qB=kernels(F(23,200))
q=tuple((a+b)/2 for a,b in zip(qA,qB))
lam2=(F(1),F(2),F(3,2),-F(17,4))
a=opt(q,q,lam2)
assert q[3]==F(47,200)
assert a[1]==(-F(2)-q[3],)*2
assert a[2]==(-F(1,8),F(1,8))
assert a[3]==-F(18399,6400) and a[4]==-F(1147,400)
assert a[5]==F(47,6400)
print("SECOND-ONLY","qstar",q[3],"Vfull",a[3],"VLR",a[4],"gap",a[5])
print("PASS_EXACT_R5_NESTED_TWO_COLLISION_NO_GO")
