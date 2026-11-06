#!/usr/bin/env python3
"""Exact rational checks for a same-B fiber diameter theorem, conditional S23 AV."""
from fractions import Fraction as F
from itertools import product

HALF=F(1,2); SEVEN_EIGHTHS=F(7,8)
ONE=F(1)
CHECKS=0

def check(ok, label):
    global CHECKS
    assert ok, label
    CHECKS+=1

def A(a,z):
    return (a,z,ONE-a-z)

def tensor(p,q):
    return tuple(x*y for x in p for y in q)

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def interval(z):
    return (max(HALF,ONE-2*z),min(SEVEN_EIGHTHS,ONE-F(8,7)*z))

def claimed_diameter(z):
    if z <= F(7,64):
        return (2*z-F(1,8))*F(15,8)
    if z <= F(1,4):
        return (F(6,7)*z)*(2-F(8,7)*z)
    return (HALF-F(8,7)*z)*(F(3,2)+F(6,7)*z)

for z in [F(1,16),F(7,64),F(1,4),F(7,16)]:
    x,y=interval(z)
    check(x<=y,'legal fiber endpoints')
    check(tv(tensor(A(x,z),A(x,z)),tensor(A(y,z),A(y,z)))==claimed_diameter(z),'breakpoint diameter')

# Exact legal indistinguishable binary observations.
z=F(1,4); a0=F(1,2); a1=F(5,7)
check(z==(1-a0)*F(1,2)==(1-a1)*F(7,8),'same binary observation')
p0=tensor(A(a0,z),A(a0,z))
p1=tensor(A(a1,z),A(a1,z))
check(tv(p0,p1)==F(18,49),'exact tensor TV')
check(tuple(j for j in range(9) if p1[j]>p0[j])==(0,1,3),'exact positive set')
check(tv(p0,p1)/2==F(9,49),'triangle lower')
check(F(9,49)>F(15383,83769),'strict prior improvement')
check(F(9,49)<F(387769986271,2048000000000),'current upper compatible')
check(F(9,49)-F(15383,83769)==F(22,586383),'improvement value')

# Piecewise exact arithmetic on 257 rational z values; proof uses monotonicity.
for j in range(257):
    zz=F(1,16)+(F(7,16)-F(1,16))*F(j,256)
    lo,hi=interval(zz)
    check(lo<=hi,'nonempty sampled fiber')
    check(tv(tensor(A(lo,zz),A(lo,zz)),tensor(A(hi,zz),A(hi,zz)))==claimed_diameter(zz),'sampled formula')
    check(claimed_diameter(zz)<=F(18,49),'sampled bound')

# Exact derivatives have the indicated signs on each interval.
# Region 1 derivative = 15/4.
check(F(15,4)>0,'region 1 increasing')
# Region 2 derivative = 12/7-96*z/49, positive even at its upper endpoint.
check(F(12,7)-F(96,49)*F(1,4)>0,'region 2 increasing')
# Region 3 derivative = -9/7-96*z/49, negative even at its lower endpoint.
check(-F(9,7)-F(96,49)*F(1,4)<0,'region 3 decreasing')

print('PASS_S23_AV_TWO_IID_EXACT_FIBER_DIAMETER_20261106')
print('CHECKS',CHECKS)
print('FROZEN_SCIENCE','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('MAX_FIBER_DIAMETER',F(18,49))
print('REVERSE_DEFICIENCY_LOWER',F(9,49))
print('PREVIOUS_LOWER',F(15383,83769))
print('IMPROVEMENT',F(22,586383))
print('CURRENT_UPPER',F(387769986271,2048000000000))
print('WITNESS',('a0='+str(a0),'c0=1/2','a1='+str(a1),'c1=7/8','z='+str(z)))
print('P0',','.join(map(str,p0)))
print('P1',','.join(map(str,p1)))
