#!/usr/bin/env python3
"""Exact-rational cross-check of the EC49FUQ endpoint minimax algorithm.

The all-real-parameter endpoint reduction is proved analytically by
log-concave marginal / Prekopa, not by this finite checker.
"""
from fractions import Fraction as F
from math import comb

BETA = F(3, 637)
THETA_E = F(31597745, 1653649)
UA = F(21829245984)
UB = F(45529434409)
UC = F(456083905)

def signed_mass(n, x, theta):
    t = (1-x)*(1-BETA*x+BETA*x*theta)
    u = UA/(UB-UC*theta)
    p, q = 1-t, 1-u*t
    assert 0 <= p < q <= 1
    return [comb(n,k)*(q**k*(1-q)**(n-k)-p**k*(1-p)**(n-k))
            for k in range(n+1)]

def test_value(masses, j, gamma):
    return sum(masses[j+1:], F(0))+gamma*masses[j]

def exact_minimax(n, x):
    zero, high = signed_mass(n,x,F(0)), signed_mass(n,x,THETA_E)
    best = None
    for j in range(n+1):
        a0, ae = sum(zero[j+1:], F(0)), sum(high[j+1:], F(0))
        b0, be = zero[j], high[j]
        candidates = [F(0), F(1)]
        if b0 != be:
            crossing = (ae-a0)/(b0-be)
            if 0 < crossing < 1: candidates.append(crossing)
        for gamma in candidates:
            d0, de = a0+gamma*b0, ae+gamma*be
            score = min(d0,de)
            if best is None or score > best['value']:
                best = dict(value=score, j=j, gamma=gamma,
                            d0=d0, de=de, zero=zero, high=high)
    return best

def verify_case(n,x):
    b=exact_minimax(n,x)
    j,gamma,v=b['j'],b['gamma'],b['value']
    possible=[]
    if b['d0']==v: possible.append(F(0))
    if b['de']==v: possible.append(F(1))
    if b['d0']==b['de'] and b['high'][j]!=b['zero'][j]:
        weight=-b['zero'][j]/(b['high'][j]-b['zero'][j])
        if 0<=weight<=1: possible.append(weight)
    def bayes_ok(weight):
        mixed=[(1-weight)*z+weight*e for z,e in zip(b['zero'],b['high'])]
        for k,signed in enumerate(mixed):
            if k<j and signed>0: return False
            if k>j and signed<0: return False
            if k==j and 0<gamma<1 and signed!=0: return False
            if k==j and gamma==0 and signed>0: return False
            if k==j and gamma==1 and signed<0: return False
        return sum(mixed[j+1:],F(0))+gamma*mixed[j]==v
    valid=[w for w in possible if bayes_ok(w)]
    assert valid,(n,x,j,gamma,'no endpoint saddle')
    for i in range(17):
        theta=THETA_E*F(i,16)
        assert test_value(signed_mass(n,x,theta),j,gamma)>=v,(n,x,i)
    return j,gamma,v,valid[0]

def main():
    cases=[(1,F(1,2)),(15,F(7,25000)),(30,F(3,20)),
           (40,F(1,100)),(60,F(7,20))]
    for n,x in cases:
        j,gamma,value,lam=verify_case(n,x)
        print(f'n={n} x={x} j={j} gamma={float(gamma):.12g} '
              f'lambda_E={float(lam):.12g} risk={float((1-value)/2):.12g}')
    for x in [F(7,25000),F(3,20),F(7,20)]:
        c0,c1=(1-x)*(1-BETA*x),(1-x)*BETA*x
        assert c0>0 and c1>0 and c1*UB+UC*c0>0
    print('PASS: exact endpoint search, dual sign certificates and rational-grid checks')

if __name__=='__main__':
    main()
