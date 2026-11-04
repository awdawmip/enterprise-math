#!/usr/bin/env python3
"""R543 exact rational Rouché certificate, frozen R462 signed BRC k=5."""
from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations
def z(a=0,b=0):return F(a),F(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]**2+a[1]**2
def sqrt_floor(q,scale=1000000):
    assert q>=0
    return F(isqrt(q.numerator*scale*scale//q.denominator),scale)
def LB(a):return sqrt_floor(norm2(a))
def UB(a):
    t=LB(a)
    return t if t*t==norm2(a) else t+F(1,1000000)
def cat(k):return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q)
        for q in range(min((t-1)//2,k)+1))
def taylor(P,c):
    out=[z(0)]
    for v in P:
        nxt=[z(0)]*(len(out)+1)
        for j,a in enumerate(out):
            nxt[j]=add(nxt[j],mul(c,a))
            nxt[j+1]=add(nxt[j+1],a)
        nxt[0]=add(nxt[0],z(v))
        out=nxt
    assert out[-1]==z(0)
    return out[:-1]
k=5;r=2*k+1;d=2*k-1
p={t:F(H(k,t),cat(k)) for t in range(2,r+1)}
a=[(-1)**(j-1)*p[j+2]*p[2]**(j-1) for j in range(1,d+1)]
P=[F(1)]+[-v for v in a]
centers=[
 z('1904.077'),z('315.999','123.424'),z('315.999','-123.424'),
 z('403.439','226.540'),z('403.439','-226.540'),
 z('584.710','455.222'),z('584.710','-455.222'),
 z('1247.313','1468.117'),z('1247.313','-1468.117')]
eps=F(1,10)
assert len(centers)==d
ratios=[]
for c in centers:
    b=taylor(P,c)
    left=UB(b[0])+sum(UB(b[j])*eps**j for j in range(2,d+1))
    right=LB(b[1])*eps
    assert right>0 and 100*left<right,(c,left,right)
    ratios.append(left/right)
assert all(LB(sub(centers[i],centers[j]))>2*eps
    for i,j in combinations(range(d),2))
dominant_lb=min(LB(centers[i])-eps for i in (7,8))
remainder_ub=max(UB(centers[i])+eps for i in range(7))
assert dominant_lb==F(1926336411,1000000)
assert remainder_ub==F(1904177,1000)
assert dominant_lb>1926 and remainder_ub<1905
assert centers[7][1]>eps and centers[8][1]<-eps
# Two simple nonreal conjugate dominant roots => nonzero residues.
# Cesaro means of cos(m theta+phi), cos^2 are 0,1/2 (theta not in pi Z).
# Each sign exceeds +/-1/4 on infinitely many m; smaller-root remainder decays.
seq=[F(1)]
for m in range(1,129):
    seq.append(sum(a[j-1]*seq[m-j] for j in range(1,min(d,m)+1)))
assert seq[42]>0 and seq[43]<0 and seq[44]>0
assert seq[50]<0 and seq[52]>0
print('R543_EXACT_CERT_PASS')
print('degree',d,'disks',len(centers),'max_rouche_ratio',format(float(max(ratios)),'.7f'))
print('dominant_modulus_lower',str(dominant_lb),'remainder_modulus_upper',str(remainder_ub))
print('Ck',cat(k),'coefficients',','.join(map(str,P)))
print('witness m42/43/44',*(('+' if seq[m]>0 else '-' if seq[m]<0 else '0') for m in (42,43,44)))
print('signchanges to128',sum(seq[i]*seq[i-1]<0 for i in range(1,len(seq))))
