"""R65 reproducible compact exact-rational verifier: python check_r65_min.py"""
from fractions import Fraction as F
from math import floor,ceil
from bisect import bisect_right

def frac(a): return a-floor(a)
def order(th,m):
    h=sorted((frac(v*th),v) for v in range(m))
    assert len(set(x for x,v in h))==m
    return h
def label(th,m,j,x,t):
    h=order(th,m)
    k=bisect_right([v for v,z in h],frac(x+(t-j)*th))-1
    return h[k][1]
def winner(th,m,j,x,ts,z):
    return max((t for t in ts if label(th,m,j,x,t)==z),default=None)
def noninteger(a,b,L,U):
    v,w=a+b*L,a+b*U
    return floor(v)==floor(w) and v.denominator!=1 and w.denominator!=1
def excluded(th0,L,U,m,j,x,z,times):
    assert 0<L<=th0<=U<1
    h=order(th0,m); labs=[z0 for v,z0 in h]
    if not all(noninteger(F(0),F(a-b),L,U)
        for a,b in zip(labs,labs[1:]+labs[:1])): return False
    nxt=labs[(labs.index(z)+1)%m]
    ph=[frac(t*th0) for t in times]
    lo,hi,tmin,tmax=min(ph),max(ph),min(times),max(times)
    dL,dU=L-th0,U-th0
    ds=[t*d for t in (tmin,tmax) for d in (dL,dU)]
    slo,shi=lo+min(ds),hi+max(ds)
    a0=frac((j+z)*th0-x)
    b0=frac((j+nxt)*th0-x)
    if b0<=a0:b0+=1
    a=[a0+(j+z)*d for d in (dL,dU)]
    b=[b0+(j+nxt)*d for d in (dL,dU)]
    if not all(0<bb-aa<1 for aa,bb in zip(a,b)):return False
    return ceil(slo-max(b))>floor(shi-min(a))

theta0=F(1,30)
theta1=F(1003,30000)
m,z=13,12
assert winner(theta0,m,10000,F(8,15),(9,15,6042),z)==6042
assert winner(theta1,m,10000,F(8,15),(9,15,6042),z)==15
assert excluded(theta0,theta0,theta0+F(1,1000000),m,10000,F(8,15),z,[390])
assert not excluded(theta0,theta0,theta1,m,10000,F(8,15),z,[6042])

# Two members of a whole immutable subtree swap phase order yet stay excluded.
assert frac(390*theta0)<frac(theta0)
assert frac(390*theta1)>frac(theta1)
x=F(13,15)
assert excluded(theta0,theta0,theta1,m,500,x,z,[1,390])
for k in range(513):
    th=theta0+(theta1-theta0)*F(k,512)
    assert all(label(th,m,500,x,t)!=z for t in (1,390))
    assert winner(th,m,500,x,(1,15,390),z)==15

# Fixed finite grid: no false positive exclusion on exact rational samples.
models=checks=certs=0
for mm in (3,4,5):
 for den in (13,17):
  base=F(2,den)
  for jj in (17,41):
   for xx in (F(0),F(1,7),F(3,11)):
    for zz in range(mm):
     for delta in (F(1,10000),F(1,500)):
      for ts in ((1,2,3),(3,7,11),(jj-4,jj-3,jj-2),(1,jj-1)):
       models+=1
       if excluded(base,base,base+delta,mm,jj,xx,zz,ts):
        certs+=1
        for k in range(17):
         th=base+delta*F(k,16)
         for t in ts:
          checks+=1
          assert label(th,mm,jj,xx,t)!=zz
assert (models,certs,checks)==(1152,458,21335)
print("R65_MIN_PASS",models,certs,checks)
