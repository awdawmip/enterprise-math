#!/usr/bin/env python3
"""Exact rational certificate and high-precision checks; universal proof in PROOF.md."""
from fractions import Fraction as Q
from itertools import zip_longest

V=Q(1,21)
R=1-V*V
C_PSI=1/(6*R)+1/(7*R)+1/(15*R*R)+1/(81*R**3)
C_DELTA=1+Q(7,45)*Q(2,3)+(Q(1,6)+Q(7,45)*V*V)*2/(5*R)
E_MAX=Q(9,8)*V**12/R**2
assert C_PSI==Q(33190017,85184000) and C_PSI<Q(1,2)
assert C_DELTA==Q(347687,297000) and C_DELTA<Q(3,2)
assert E_MAX==Q(1,6508893842035200) and E_MAX<Q(1,10**15)
assert V/Q(6)+V**3/Q(20)<Q(1,125)

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out
def sub(a,b):
    return [x-y for x,y in zip_longest(a,b,fillvalue=Q(0))]
D0=[Q(1),Q(1)]
D2=[Q(1,3),Q(0),Q(0),Q(1,3)]
d1=[Q(1,6),Q(-1,6)]
d3=[Q(9,180),Q(1,180),Q(-1,180),Q(-9,180)]
A=[Q(1,6),Q(0),Q(-1,6)]
B=[Q(19,180),Q(0),Q(0),Q(0),Q(-19,180)]
assert all(x==0 for x in sub(mul(D0,d1),A))
assert all(x==0 for x in sub([x+y for x,y in zip_longest(mul(D0,d3),mul(D2,d1),fillvalue=Q(0))],B))
print('EXACT_PSI_REMAINDER_COEFFICIENT=',C_PSI)
print('EXACT_OPTIMIZER_ERROR_COEFFICIENT=',C_DELTA)
print('MAX_GLOBAL_INFORMATION_ERROR=',E_MAX)
print('EXACT_POLYNOMIAL_IDENTITY=PASS')

import mpmath as m
m.mp.dps=90
maxratio=m.mpf(0)
count=0
for vden in (21,42,100):
    v=m.mpf(1)/vden
    for sn,sd in ((1,1000),(1,32),(1,16),(1,10),(1,4),(1,2),(3,4),(19,20),(999,1000),(1,1)):
        s=m.mpf(sn)/sd
        k=s/(2-s)
        proxy=(1-k)*v/6+(1-k)*(9*k*k+10*k+9)*v**3/180
        alpha=m.atanh(v)
        gamma=m.atanh(k*v)
        def psi(x):
            return m.log(m.sqrt(1-x*x)*m.atanh(x)/x) if x else m.mpf(0)
        star=(psi(k*v)-psi(v))/(alpha+gamma)
        X=s*m.sqrt(1-v*v)/2
        Y=(2-s)*m.sqrt(1-k*k*v*v)/2
        def Z(d): return X*m.exp(alpha*d)+Y*m.exp(-gamma*d)
        gain=m.log(Z(proxy))-m.log(Z(star))
        cert=m.mpf(9)/8*v**12/(1-v*v)**2
        assert abs(star-proxy)<m.mpf(3)/2*v**5
        assert -m.mpf('1e-77')<gain<cert
        assert 0<=proxy<m.mpf(1)/125
        maxratio=max(maxratio,gain/cert)
        count+=1
print('INDEPENDENT_HIGH_PRECISION_CASES=',count)
print('PRECISION_DIGITS=',m.mp.dps)
print('MAX_OBSERVED_RATIO_TO_GLOBAL_V_BOUND=',m.nstr(maxratio,15))
print('PASS_BRC_S23_TWELFTH_ORDER_RATIONAL_CHERNOFF_PROXY_20261104')
