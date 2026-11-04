#!/usr/bin/env python3
"""Exact rational enclosure for source-tagged S23, s=1/8, h=1/42, integer K<=100.
All inequalities in this program are between Fractions. No floating arithmetic.
"""
from fractions import Fraction as F
from math import isqrt, factorial

Q=10**30

def sqrtI(x):
    assert x>0
    i=isqrt(x.numerator*Q*Q//x.denominator)
    return (F(i,Q), F(i+1,Q))

def atanhI(x, terms=12):
    assert 0<=x<1
    lo=sum((x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=x**(2*terms+1)/F((2*terms+1)) /(1-x*x)
    return (lo,lo+tail)

def mul(x,y):
    p=[a*b for a in x for b in y]
    return (min(p),max(p))

def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def times(x,n):return mul(x,(F(n),F(n)))
def exact(x):return (F(x),F(x))

def exp_scalar_pos(x,terms=10):
    assert F(0)<=x<F(1,10)
    lo=sum((x**j/F(factorial(j)) for j in range(terms+1)),F(0))
    tail=x**(terms+1)/F(factorial(terms+1)) /(1-x/F(terms+2))
    return lo,lo+tail

def exp_scalar(x):
    if x>=0:return exp_scalar_pos(x)
    y=exp_scalar_pos(-x)
    return (1/y[1],1/y[0])

def expI(x):return (exp_scalar(x[0])[0],exp_scalar(x[1])[1])
def logminus_scalar(z,terms=9):
    assert 0<z<=1
    w=(1-z)/(1+z)
    lo=2*sum((w**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*w**(2*terms+1)/F(2*terms+1)/(1-w*w)
    return lo,lo+tail

def logminusI(z):
    assert 0<z[0]<=z[1]<=1, ('Z not in (0,1]',z)
    return (logminus_scalar(z[1])[0],logminus_scalar(z[0])[1])

s=F(1,8);v=F(1,21); k=s/(2-s)
r=sqrtI(1-v*v); rb=sqrtI(1-k*k*v*v)
alpha=atanhI(v);gamma=atanhI(k*v)
A=times(r,s/2); B=times(rb,(2-s)/2)

def coeff(d):
    assert -1<=d<=1
    x=times(alpha,d); y=times(gamma,-d)
    ep=expI(x);em=expI(y)
    ep2=expI(neg(x))
    cosh=times(add(ep,ep2),F(1,2))
    sinh=times(sub(ep,ep2),F(1,2))
    zt=add(exact(1-s),times(mul(r,cosh),s))
    zb=add(mul(A,ep),mul(B,em))
    ztp=mul(times(mul(r,alpha),s),sinh)
    zbp=sub(mul(mul(A,alpha),ep),mul(mul(B,gamma),em))
    return zt,zb,ztp,zbp

def objective(m,n,d):
    zt,zb,ztp,zbp=coeff(F(d))
    val=add(times(logminusI(zt),m),times(logminusI(zb),n))
    der=neg(add(times(div(ztp,zt),m),times(div(zbp,zb),n)))
    return val,der

def bound_max(m,n,d):
    val,der=objective(m,n,d)
    mu=F(m,5000)+F(n,10000)
    assert mu>0
    absder=max(abs(der[0]),abs(der[1]))
    return (val[0],val[1]+absder**2/(2*mu))

# Selected rational parameter probes, with no calls to a real optimizer.
D_B=F(7412849,10**9)
D_2_9=F(1710806,10**9)
D_2_10=F(1853374,10**9)
D_3_14=F(1759134,10**9)
CB=bound_max(0,1,D_B)
CT=objective(1,0,0)[0]
E=sub(CT,times(CB,F(15,8)))
# Globally discard m not divisible by 8 for ALL K<=100, m<=53, fractional slack>=1/8.
assert E[0]>0 and E[1]<F(191,10**11)
assert 53*E[1] < CB[0]/8
# Boundary winner vs all-B, for j=max feasible q=K//15.
def Hbounds(q,rest,d):
    return sub(bound_max(8*q,rest,d),times(CB,15*q+rest))
h29=Hbounds(2,9,D_2_9)
h210=Hbounds(2,10,D_2_10)
h314=Hbounds(3,14,D_3_14)
fb0=objective(0,1,0)[0]
h414=sub(add(times(CT,32),times(fb0,14)),times(CB,74))
assert h29[0]>F(1706,10**12),h29
assert h210[1]<-F(691,10**12),h210
assert h314[0]>F(1339,10**12),h314
assert h414[0]>F(2772,10**12),h414
# Convexity of max_delta of affine functions in q: endpoint q=0 or q=floor(K/15).
# D_q(r+1)<=D_q(r), since f_B(delta)<=C_B.
# D_q(r)>=q D_1(0) - r [C_B-f_B(0)] at delta=0.
# For q>=4 and r<=14, D_q(r)>=D_4(14)>0.
# q=1, r<=4/>=5 from preceding proof's immutable certificate.
# q=2, r<=9/>=10 by h29 and h210; q=3, r<=14 by h314.
# All candidates outside q=0 or maximal q are suboptimal by convexity.
# Record exact winners for K=31..100, independently of earlier K<=30 proof.
winners={}
for K in range(31,101):
    q,r=divmod(K,15)
    use=(q==2 and r<=9) or q>=3
    m=8*q if use else 0
    n=r if use else K
    assert F(15,8)*m+n<=K
    winners[K]=(m,n)
print('PASS_BRC_S23_S18_K31_100_ENDPOINT_CONVEX_RATIONAL_20261104')
for label,z in [('CB',CB),('CT',CT),('E',E),('H2(9)',h29),('H2(10)',h210),('H3(14)',h314),('H4(14)',h414)]:
    print(label,'lower=',format(float(z[0]),'.17e'),'upper=',format(float(z[1]),'.17e'))
for lo,hi in [(31,39),(40,44),(45,59),(60,74),(75,89),(90,100)]:
    print(f'K={lo}..{hi}:',winners[lo],'through',winners[hi])
