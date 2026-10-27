#!/usr/bin/env python3
"""R37: independent exact-Fraction p=37 rank-jet source certificate."""
from fractions import Fraction as Q
from math import factorial, gcd

p=37; m=6; modulus=p*p

def poch(t,n):
    z=Q(1)
    for k in range(n):z*=t+k
    return z

def ar(r):
    return poch(Q(2,3),r)**3/(poch(Q(7,6),r)*poch(Q(4,3),r)*factorial(r))

def hr(r):
    return poch(Q(4,3),r)*factorial(r)/(poch(Q(11,12),r)*poch(Q(17,12),r))

def red(q,mod=modulus):
    q=Q(q); assert gcd(q.denominator,mod)==1
    return q.numerator*pow(q.denominator,-1,mod)%mod

C=Q(3*216**(2*m)*factorial(2*m)**5,factorial(4*m+1))
D=Q(2*2304**(2*m)*factorial(2*m)**4,factorial(2*m+2))
a=[ar(r) for r in range(m)]
h=[hr(r) for r in range(m)]
v=[C*(2*r+1)*2**r-D*(Q(13,3)+8*r)*9**r*h[r] for r in range(m)]
qs=[red(sum((r**j)*v[r]*a[r] for r in range(m))) for j in range(5)]
c=red(-(Q(m)-Q(1,3))**3*a[-1]); betas=[t*pow(c,-1,modulus)%modulus for t in qs]
assert qs==[37,1184,931,789,1029],qs
assert betas==[1258,555,278,1037,1316],betas
for r in range(1,m):
    At=Q(r)*(Q(r)+Q(1,6))*(Q(r)+Q(1,3))
    Bt=(Q(r)-Q(1,3))**3
    assert At*a[r] - Bt*a[r-1] == 0
assert red(-(Q(m)-Q(1,3))**3*a[-1])==678
print('PASS: p=37, m=6, exact original W/S observer plus theta^j, j=0..4')
print('Q_j modulo 37^2:',qs,'and modulo 37:',[x%37 for x in qs])
print('endpoint coefficients Q_j/c modulo 37^2:',betas)
print('first nonzero rank-jet moment modulo 37 is j=2, value 6; endpoint coefficient 19')
