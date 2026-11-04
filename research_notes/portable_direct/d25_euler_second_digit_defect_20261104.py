#!/usr/bin/env python3
"""Exact p^2 Euler truncation-defect validation in F_p[z]/(z^p)."""
from math import comb
from d25_frobenius_euler_descent_20261104 import primes

def coefficients(p, a, b, end, modulus):
    out=[1]
    for n in range(1,end+1):
        out.append(out[-1]*(8*n-8+a)*(8*n-8+b)*pow(576*n*n,-1,modulus)%modulus)
    return out

def conv(A,B,limit,p):
    out=[0]*limit
    for i,aa in enumerate(A[:limit]):
        if aa:
            for j,bb in enumerate(B[:limit-i]):
                out[i+j]=(out[i+j]+aa*bb)%p
    return out

def verify(p):
    assert p%8==5
    q=(p-5)//8; N=(p+1)//2; L=5*q+3
    mod=p*p
    v=coefficients(p,1,3,p-1,mod)
    c=coefficients(p,5,7,p-1,mod)
    alpha=-pow(9,-1,mod)%mod
    gp=[comb(N,k)*pow(alpha,k,mod)%mod for k in range(N+1)]
    h=conv(c[:q+1],gp,p,mod)
    E=[(v[k]-h[k])%mod for k in range(p)]
    assert all(t%p==0 for t in E), (p,'base congruence')
    E=[x//p for x in E]
    # The first p-divisible parameter occurs at k=q+1, the second at k=3q+2.
    assert all(c[k]%mod==0 for k in range(3*q+2,p))
    R=[0]*p
    for j in range(q+1,3*q+2):
        assert c[j]%p==0
        R[j]=(c[j]//p)%p
    gamma=c[q]//1 * pow(288*(q+1)**2,-1,p)%p
    assert R[q+1]==gamma
    log=[0]*p
    inv9=pow(9,-1,p)
    pow9=1
    for k in range(1,p):
        pow9=pow9*inv9%p
        log[k]=-pow9*pow(k,-1,p)%p
    half=pow(2,-1,p)
    cL=conv([x%p for x in c[:q+1]],log,p,p)
    Q=[(R[k]-half*cL[k])%p for k in range(p)]
    sqrt=[1]
    for k in range(1,p):
        sqrt.append(sqrt[-1]*(2*k-3)*pow(18*k,-1,p)%p)
    result=conv(sqrt,Q,p,p)
    assert result==E, (p,next((i,result[i],E[i]) for i in range(p) if result[i]!=E[i]))
    # Source-preserving observer values in the truncated polynomial ring.
    return p,q,sum(E)%p,sum(k*E[k] for k in range(p))%p

if __name__=='__main__':
    allp=primes(2000)
    rows=[verify(p) for p in allp]
    print('PASS second_digit_Euler_defect primes=%d coefficient_checks=%d' % (len(rows), sum(p for p,*_ in rows)))
    for row in rows:
        if row[0] in (5,13,29,37,53,61,373): print('CASE',*row)
