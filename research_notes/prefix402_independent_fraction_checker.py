#!/usr/bin/env python3
"""Independent rational complex-pair arithmetic for PREFIX-402 witnesses."""
from fractions import Fraction as F

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]*a[0]+a[1]*a[1]
def amp(a,b,c,u,v):return add(add(a,mul(b,u)),mul(c,v))

b4=(F(3,2),F(7,2)); a4=(F(5,2),F(9,2)); c4=(F(0),F(4))
b5=(F(11,4),F(15,8)); a5=b5; c5=(F(5,4),F(9,4))
u0=(F(59,63),F(0)); h=F(1,10000)
u=(u0[0],h); vp=(F(1),F(1)); vm=(F(1),F(-1))
obs=lambda a,b,c,u,v:norm2(amp(a,b,c,u,v))
assert norm2(u)-norm2(u0)==h*h
assert norm2(add((F(1),F(0)),u))-norm2(add((F(1),F(0)),u0))==h*h
assert norm2(vp)==2 and norm2(add((F(1),F(0)),vp))==5
j4=obs(a4,b4,c4,u0,vp)
j4m=obs(a4,b4,c4,u0,vm)
j4h=obs(a4,b4,c4,u,vp)
assert j4==F(550600,3969) and j4m==F(798568,3969)
assert j4h-j4==F(720029,200000000)
assert j4h-j4m==-F(262384879391,4200000000)
assert obs(a5,b5,c5,u0,vp)==F(4417309,63504)
assert obs(a5,b5,c5,u,vp)-obs(a5,b5,c5,u0,vp)==F(14720709,6400000000)

# Independently recompute the algebraic separation from the declared rational errors.
xi2=F(1,10**8); rho=F(1,5000); di3=F(1,10)
assert (1+2*u0[0])*xi2 < rho*rho
assert 120*rho+16*rho*rho<F(1,40)
D=F(63,16)*(F(1,10)+F(1,40))+63*di3
M=F(75154)*(2-di3)-(122+D)**2
assert M>355*355
Z=(F(75154)*di3+(244+D)*D)/(355+368)
H=di3+F(2,75154)*(245*D+123*Z)
gap=F(90528,37577)-2*(H+1)
assert gap==F(68790132351,1854680473600)>0
print('PASS_PREFIX402_INDEPENDENT_PURE_FRACTION_ORIGINAL_PORT_WITNESS_AND_GAP')
