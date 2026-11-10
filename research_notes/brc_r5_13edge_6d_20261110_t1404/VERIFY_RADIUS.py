#!/usr/bin/env python3
"""Exact uniform six-dimensional 13-edge-support chamber radius.

Requires sibling VERIFY_13.py and its immutable parent frozen verifier.
Computes all 26 physical-slack, 13 positive-edge, 10 forced-dual and 190
quotient-pair margins with rational arithmetic. Reproduction is independent
of any floating-point optimizer.
"""
from pathlib import Path
from itertools import combinations
import sympy as S

local=Path(__file__).resolve().parent
context={'__file__':str(local/'VERIFY_13.py')}
exec(compile((local/'VERIFY_13.py').read_text(),str(local/'VERIFY_13.py'),'exec'),context)
M13,T,n,m,A,z13,center,w14=(context[k] for k in ('M13','T','n','m','A','z13','center','w14'))
C,E,force,L,V,other,q,qr,DUAL,K=(context[k] for k in ('C','E','force','L','V','other','q','qr','DUAL','K'))
KT=S.Matrix.hstack(*K)
assert KT.shape==(8,6)
assert S.Matrix.vstack(n.T,m)*KT==S.zeros(2,6)
coeff=S.Matrix.hstack(*(M13.gauss_jordan_solve(T*v)[0] for v in K))
assert M13*coeff==T*KT
phys=center+A*z13
physical=[];mass=[];forcing=[];separation=[]
for i in range(26):
    gradient=A.row(i)*KT
    if phys[i]<=0:
        assert phys[i]==0 and all(a==0 for a in gradient)
        continue
    slope=sum(abs(a) for a in gradient)
    if slope:physical.append((phys[i]/slope,i))
for i in range(13):
    slope=sum(abs(a) for a in coeff.row(i))
    if slope:mass.append((w14[i]/slope,i))
for e,items in DUAL.items():
    y=S.zeros(15,1)
    for item in items.split():
        j,v=item.split(':');y[int(j)]=S.Rational(v)
    assert all((y.T*C[:,j])[0]<=int(E[j]==e) for j in range(30))
    bound=(y.T*q(z13))[0]
    assert bound>0
    slope=sum(abs(a) for a in y.T*T*KT)
    if slope:forcing.append((bound/slope,e))
for pair in combinations(range(20),2):
    sub=V[:,pair]
    assert sub.row_join(qr).rank()>sub.rank()
    candidates=[]
    for y in sub.T.nullspace():
        gap=abs((y.T*qr)[0])
        if gap:
            slope=sum(abs(a) for a in y.T*L*T*KT)
            if slope:candidates.append((gap/slope,pair))
    # Every one of the 190 pairs has a finite positive separator radius.
    assert candidates
    separation.append(max(candidates))
assert len(separation)==190
vals=[('PHYSICAL',physical),('COUPLING',mass),('FORCED_DUAL',forcing),('PAIR_SEPARATION',separation)]
for label,items in vals:
    bound,index=min(items)
    print('MIN_RADIUS',label,bound,'WITNESS',index,'CHECKED',len(items))
bound=min(v for _,items in vals for v,_ in items)
assert bound==S.Rational(13788487966680799653,5443551776305983665000000)
assert bound>S.Rational(1,1000000)
print('SIX_DIMENSIONAL_RATIONAL_K_BASIS')
for v in K: print('K',tuple(v))
print('EXACT_UNIFORM_SAFE_CLOSED_CUBE_RADIUS',S.Rational(1,1000000))
print('EXACT_MIN_FULL_CERTIFICATE_MARGIN',bound)
print('PASS_ALL_26_PHYSICAL_13_MASS_10_DUAL_190_PAIR_CERTIFICATES_FOR_EVERY_REAL_POINT_IN_6D_CUBE')
