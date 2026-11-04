#!/usr/bin/env python3
"""Direct original finite truncations and exact modular scalar-map test (not native H0/B0)."""
from fractions import Fraction as F
from math import comb, isqrt
def prime(p): return p>=5 and all(p%d for d in range(2,isqrt(p)+1))
def coeff(p,d):
 m=p**3
 return [comb(2*k,k)*comb(d*k,(d-2)*k)*pow({3:27,4:64}[d],-k,m)%m for k in range(p)]
def obs(p,c,r):
 j=p+r;m=p**3
 u=sum(c[i]*c[j-i] for i in range(max(0,j-p+1),min(j,p-1)+1))
 v=sum((-1)**(j-k)*comb(k,j-k)*comb(2*k,k)*c[k] for k in range((j+1)//2,min(j,p-1)+1))
 w=(u-v)%m;assert w%p**2==0;return w//p**2
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p
N=0;exceptions=[]
for p in range(5,1001):
 if not prime(p):continue
 N+=1;rows={}
 for d,C in [(3,F(2,9)),(4,F(3,16))]:
  a=coeff(p,d);z=[obs(p,a,r) for r in (1,2)]
  assert z==[mod((2-6*C)*C,p),mod(C*(F(3,2)-F(11,4)*C-F(39,8)*C*C),p)],(p,d,z)
  rows[d]=z
 if (rows[3][0]*rows[4][1]-rows[4][0]*rows[3][1])%p==0:exceptions.append(p)
assert N==166 and exceptions==[5,139]
p=139; a=[obs(p,coeff(p,3),r) for r in (1,2,3)]
b=[obs(p,coeff(p,4),r) for r in (1,2,3)]
assert (a,b)==([134,138,95],[36,35,84])
lam=a[0]*pow(b[0],-1,p)%p
assert lam==135 and (a[2]-lam*b[2])%p==14
m=p**3;AA=BB=MA=MB=0
for k in range(p):
 x=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)%m
 y=comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,m)%m
 AA=(AA+x)%m;BB=(BB+y)%m;MA=(MA+k*x)%m;MB=(MB+k*y)%m
assert ((AA,BB,MA,MB)==(1024013,1004692,1619767,881538))
assert (AA+6*MA)%m==(BB+8*MB)%m==139
assert ((AA-BB)%m)//p**2==1 and ((6*MA-8*MB)%m)//p**2==138
print('checked_primes',N,'coefficient_tests',N*4,'exceptions',exceptions,'p139',a,b,'weighted=139','failures=0')
