#!/usr/bin/env python3
"""R544 exact rational Rouché certificate for frozen R462 signed BRC, k=6.
No floating point in certification assertions.
"""
from fractions import Fraction as F
from math import comb,isqrt
from itertools import combinations
def Z(a=0,b=0):return F(a),F(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]**2+a[1]**2
def lb(z,scale=10**7):
 q=norm2(z)
 return F(isqrt(q.numerator*scale*scale//q.denominator),scale)
def ub(z,scale=10**7):
 q=norm2(z);x=lb(z,scale)
 return x if x*x==q else x+F(1,scale)
def cat(k):return comb(2*k,k)//(k+1)
def H(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
def polynomial(k):
 p={t:F(H(k,t),cat(k)) for t in range(2,2*k+2)}
 d=2*k-1
 a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
 return [F(1)]+[-v for v in a],a,p
def taylor(P,c):
 out=[Z(0)]
 for v in P:
  nx=[Z(0)]*(len(out)+1)
  for j,a in enumerate(out):
   nx[j]=add(nx[j],mul(c,a))
   nx[j+1]=add(nx[j+1],a)
  nx[0]=add(nx[0],Z(v))
  out=nx
 assert out[-1]==Z(0)
 return out[:-1]
k=6;d=11;P,a,p=polynomial(k)
centers=[Z('4136.891'),
 Z('3292.954','3962.354'),Z('3292.954','-3962.354'),
 Z('1458.174','1171.622'),Z('1458.174','-1171.622'),
 Z('956.047','591.474'),Z('956.047','-591.474'),
 Z('729.470','351.188'),Z('729.470','-351.188'),
 Z('594.910','207.712'),Z('594.910','-207.712')]
eps=F(1,10)
assert len(centers)==d
ratios=[]
for idx,c in enumerate(centers):
 b=taylor(P,c)
 left=ub(b[0])+sum(ub(b[j])*eps**j for j in range(2,d+1))
 right=lb(b[1])*eps
 assert 0<left<right,(idx,left,right)
 ratios.append(left/right)
assert all(lb(sub(centers[i],centers[j]))>2*eps for i,j in combinations(range(d),2))
dom=min(lb(centers[i])-eps for i in (1,2))
rem=max(ub(centers[i])+eps for i in [0,3,4,5,6,7,8,9,10])
assert dom>5151 and rem<4138,(dom,rem)
assert centers[1][1]>eps and centers[2][1]<-eps
seq=[F(1)]
for m in range(1,257):
 seq.append(sum(a[j-1]*seq[m-j] for j in range(1,min(m,d)+1)))
changes=[m for m in range(1,len(seq)) if seq[m]*seq[m-1]<0]
assert changes
assert max(ratios)<F(57,10000)
print('R544_EXACT_ROUCHE_PASS')
print('k',k,'degree',d,'Catalan',cat(k),'p2',p[2])
print('coefficients P:', ','.join(map(str,P)))
print('max_ratio',float(max(ratios)))
print('dominant_lower',dom,'other_upper',rem)
print('recurrence signchanges_0_to256',len(changes),'first_changes',changes[:20])
print('signs_m0_to40',''.join('+' if s>0 else '-' if s<0 else '0' for s in seq[:41]))
