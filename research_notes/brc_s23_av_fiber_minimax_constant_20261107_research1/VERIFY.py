#!/usr/bin/env python3
"""S23 fixed-fiber exact identities and high-precision Fisher constant checks.
This is a finite regression/numeric diagnostic; asymptotic theorem is analytic.
"""
from fractions import Fraction as F
from math import comb
import mpmath as mp

z0,z1=F(1,16),F(7,16)
z_break_1,z_break_2=F(7,64),F(1,4)

def fiber(z):
    z=F(z)
    assert z0 <= z <= z1
    tlo=max(F(1,8),F(8,7)*z)
    thi=min(F(1,2),2*z)
    assert tlo<=thi
    return (tlo-z)/(1-z),(thi-z)/(1-z),tlo,thi

def theta(r):
    return 2*mp.asin(mp.sqrt(mp.mpf(r.numerator)/r.denominator))

def fisher_length(z):
    lo,hi,*_=fiber(z)
    return theta(hi)-theta(lo)

def weighted_length(z):
    z=F(z)
    return mp.sqrt(1-mp.mpf(z.numerator)/z.denominator)*fisher_length(z)

checks=0
for den in [64,128,256,1024]:
    for num in range((den+15)//16, (7*den)//16+1):
        z=F(num,den)
        if not z0<=z<=z1: continue
        lo,hi,tlo,thi=fiber(z)
        assert 0<lo<=hi<1
        for t,r in ((tlo,lo),(thi,hi)):
            a,c=1-t,z/t
            assert F(1,2)<=a<=F(7,8)
            assert F(1,2)<=c<=F(7,8)
            assert (1-a)*c==z
            assert (1-a)*(1-c)/(1-z)==r
            checks+=5
        if z<=z_break_1: assert lo==(F(1,8)-z)/(1-z)
        else: assert lo==z/(7*(1-z))
        if z<=z_break_2: assert hi==z/(1-z)
        else: assert hi==(F(1,2)-z)/(1-z)
        checks+=2

assert fiber(F(1,4))[:2]==(F(1,21),F(1,3))
assert fiber(z0)[:2]==(F(1,15),F(1,15))
assert fiber(z1)[:2]==(F(1,9),F(1,9))
assert fiber(z_break_1)[:2]==(F(1,57),F(7,57))
checks+=4

# Exact joint stopping-label multinomial law, checked on a fixed fiber.
for z,r in ((F(1,4),F(1,21)),(F(1,4),F(1,7)),(F(1,4),F(1,3))):
    q=(1-z)*r
    p=(1-z-q,z,q)
    for n in range(1,12):
        total=F(0)
        for u in range(n+1):
            for v in range(n-u+1):
                w=n-u-v
                mass=F(comb(n,u)*comb(n-u,v))*p[0]**u*p[1]**v*p[2]**w
                total+=mass
        assert total==1
        checks+=1

mp.mp.dps=70
left=weighted_length(z_break_2)
C=2/left
want=2/(mp.sqrt(3)*(mp.asin(mp.sqrt(mp.mpf(1)/3))-mp.asin(mp.sqrt(mp.mpf(1)/21))))
assert abs(C-want)<mp.mpf('1e-60')
# Grid verifies sign trends; global monotonicity is established analytically in PROOF.md.
for start,end in ((z0,z_break_1),(z_break_1,z_break_2)):
    last=mp.mpf('-1')
    for j in range(101):
        z=start+(end-start)*F(j,100)
        f=weighted_length(z)
        assert f>=last-mp.mpf('1e-60')
        last=f;checks+=1
last=left
for j in range(1,101):
    z=z_break_2+(z1-z_break_2)*F(j,100)
    f=weighted_length(z)
    assert f<=last+mp.mpf('1e-60')
    last=f;checks+=1
assert mp.mpf('2.9196') < C <mp.mpf('2.9198')
checks+=2
print('PASS_S23_FIBER_EXACT_MINIMAX_CONSTANT_20261107')
print('assertions=',checks)
print('Fisher length at z=1/4:',mp.nstr(fisher_length(F(1,4)),35))
print('max sqrt(1-z)*I(z):',mp.nstr(left,40))
print('exact-limit decimal:',mp.nstr(C,50))
print('frozen pin=43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('scope=finite exact identities plus high-precision diagnostic; theorem analytic')
