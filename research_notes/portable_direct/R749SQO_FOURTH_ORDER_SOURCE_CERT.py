#!/usr/bin/env python3
"""R749SQO: exact labeled-source fourth-order mean certificate.
Finite integer/Fraction checks; the universal asymptotics use the paper proof.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, prod
from functools import lru_cache
from itertools import combinations
import json

A = (1, 1, 2, 3, 7)
B = (1, 1, 1, 5, 6)

def mul(a, b, m):
    o = [F(0)]*(m+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j <= m: o[i+j] += x*y
    return o

def factor(s, m=4):
    # s*w/[1-(1-w)**s] with constant coefficient 1.
    q=[F((-1)**j*comb(s,j+1),s) if j+1<=s else F(0)
       for j in range(m+1)]
    assert q[0]==1
    f=[F(1)]
    for k in range(1,m+1):
        f.append(-sum(q[j]*f[k-j] for j in range(1,k+1)))
    return f

def raw_poly(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    return o

def P(k, div=False):
    # P_k(r)=r(r+1)...(r+k-1)/k!
    p=[F(1)]
    for j in range(k):p=raw_poly(p,[F(j),F(1)])
    p=[v/factorial(k) for v in p]
    if div:
        assert p[0]==0
        p=p[1:]
    return p

def expansion(weights, marked=0, order=4):
    d=len(weights);h=weights[marked]
    assert d>=order
    f=[F(1)]+[F(0)]*order
    for s in weights: f=mul(f,factor(s,order),order)
    # h*w*z**h/(1-z**h) = factor(h)*(1-w)**h
    powh=[F((-1)**j*comb(h,j)) if j<=h else F(0)
          for j in range(order+1)]
    b=mul(f,mul(factor(h,order),powh,order),order)
    C=[F(0)]*(d+1);N=[F(0)]*(d+1)
    for j in range(order+1):
        for i,v in enumerate(P(d-j)):C[i]+=f[j]*v
        for i,v in enumerate(P(d+1-j,True)):N[i]+=b[j]*v
    c=[C[d-j] for j in range(order+1)]
    n=[N[d-j] for j in range(order+1)]
    ratio=[]
    for k in range(order+1):
        ratio.append((n[k]-sum(c[i]*ratio[k-i] for i in range(1,k+1)))/c[0])
    return ratio

def dp(weights, R, marked=0):
    c=[0]*R;m=[0]*R;c[0]=1
    for i,s in enumerate(weights):
        for q in range(s,R):
            c[q]+=c[q-s]
            m[q]+=m[q-s]+(c[q-s] if i==marked else 0)
    C=[0];M=[0]
    for q in range(R):
        C.append(C[-1]+c[q]);M.append(M[-1]+m[q])
    return C,M

def independent(weights, r, marked=0):
    @lru_cache(None)
    def go(i,left):
        if i==len(weights):return (1,0)
        total=moment=0
        for k in range(left//weights[i]+1):
            c,m=go(i+1,left-k*weights[i])
            total+=c;moment+=m+(k*c if i==marked else 0)
        return total,moment
    return go(0,r-1)

def signature(weights):
    return dict(d=len(weights),D=sum(s-1 for s in weights),
                Q=sum(s*s-1 for s in weights),
                S4=sum(s**4-1 for s in weights),W=prod(weights))

def run():
    sa=signature(A);sb=signature(B)
    assert (sa['d'],sa['D'],sa['Q'])==(5,9,59)
    assert (sb['d'],sb['D'],sb['Q'])==(5,9,59)
    assert sa['S4']-sb['S4']==576
    for ww in (A,B):
        nonunit=[s for s in ww if s>1]
        assert all(gcd(x,y)==1 for x,y in combinations(nonunit,2))
    ea=expansion(A);eb=expansion(B)
    assert ea[:4]==eb[:4]
    assert ea[4]-eb[4]==8
    deletion=enumeration=0
    for ww in (A,B):
        C,M=dp(ww,1024)
        for r in range(1,1025):
            assert M[r]==sum(C[r-k] for k in range(1,r))
            deletion+=1
        for r in range(1,31):
            assert (C[r],M[r])==independent(ww,r)
            enumeration+=1
    ca,ma=dp(A,4000);cb,mb=dp(B,4000)
    samples=[]
    for r in (100,210,420,840,1000,1680,2100,4000):
        scaled=F(r**4)*(F(ma[r],r*ca[r])-F(mb[r],r*cb[r]))
        assert abs(scaled-8)<3  # finite diagnostic window only
        samples.append(dict(r=r,scaled_decimal=format(float(scaled),'.12f'),
                            scaled_exact=str(scaled)))
    phase=[]
    U=(1,1,1,2)
    for j,amp in ((0,F(-3,10)),(3,F(6,5))):
        c,m=dp(U,4001,j)
        coeff=expansion(U,j)
        for r in (1000,1001,2000,2001,4000,4001):
            ex=F(U[j]*m[r],r*c[r])
            smooth=sum(coeff[k]/r**k for k in range(5))
            observed=r**4*(ex-smooth)
            target=amp*(1 if r%2 else -1)
            assert abs(observed-target)<F(1,20)
            phase.append(dict(h=U[j],r=r,target=str(target),
                              absolute_error_decimal=format(float(abs(observed-target)),'.9f')))
    return dict(status='PASS',model='auxiliary positive labeled weighted-source multiset',
                frozen_pin='a72226e2430ffa4786321ac86e7f0c599d5f0389',
                A=A,B=B,signature_A=sa,signature_B=sb,
                mean_coefficients_A=list(map(str,ea)),
                mean_coefficients_B=list(map(str,eb)),
                predicted_r4_difference='8',
                deletion_checks=deletion,independent_enumerations=enumeration,
                max_r=4001,samples=samples,periodic_phase_tests=phase,
                evidence_scope='finite exact arithmetic only; infinite claims from rational pole proof; not independently reviewed')

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
