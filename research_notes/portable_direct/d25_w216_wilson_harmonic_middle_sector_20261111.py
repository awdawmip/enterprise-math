#!/usr/bin/env python3
"""Exact D25 W216 middle-band Wilson/harmonic certificate.
Author-side / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
"""
from math import factorial, isqrt

def is_prime(n):
    return n >= 2 and all(n % j for j in range(2, isqrt(n)+1))

def verify(p):
    assert p>=7 and p%6==1 and is_prime(p)
    m,n,pp,M=(p-1)//6,(p-1)//2,p*p,p**3
    fact=[factorial(k) for k in range(p)]
    Q=((fact[p-1]+1)//p)%p
    a=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2) *
                 pow(36*(k+1)**3,-1,M)%M)
    S0=sum((6*k+1)*a[k] for k in range(2*m+1))%M
    C0=A=J=0
    for k in range(2*m+1,n+1):
        r=3*k-p
        assert 0<r<p and 2*k<p
        C=(fact[2*k]*fact[r]*pow(216,-k,pp)*pow(fact[k],-5,pp))%pp
        H=sum(pow(j,-1,p) for j in range(1,r+1))%p
        b=(-C*(1+p*(H-Q)))%pp
        assert b==(a[k]//p)%pp,(p,k)
        C0=(C0+(6*k+1)*C)%pp
        A=(A+(6*k+1)*(C%p)*H)%p
        J=(J+(6*k+1)*(C%p))%p
    C1=(A-Q*J)%p
    L=(S0-p*C0-pp*C1)%M
    assert L==sum((6*k+1)*a[k] for k in range(n+1))%M
    chi=pow(6,(p-1)//2,p)
    chi=-1 if chi==p-1 else 1
    q=1;D=0
    for j in range(m):
        D=(D+(6*j+4)*q)%p
        if j+1<m:
            q=q*(j+1)*(6*j+5)*(6*j+7)*pow(9*(2*j+3)**3,-1,p)%p
    tail=chi*D*pow(9,-1,p)%p
    W=(L+pp*tail)%M
    assert W==sum((6*k+1)*a[k] for k in range(p))%M
    if p==373:
        assert (Q,J,A,C1)==(224,346,20,100)
        assert (S0,C0,L,D,tail,W)==(28094360,137237,14887176,217,266,373)
        wrong=(S0-p*C0-pp*A+pp*tail)%M
        assert wrong==(373+80*pp)%M
    return p,Q,J,A,C1,L,tail,W

if __name__=="__main__":
    primes=[7,13,19,31,37,43,61,67,73,79,97,109,139,157,163,181,
            193,211,229,277,283,307,331,349,373,379,397,421,499,541,733]
    for p in primes:
        print("p=%-3d Q=%-4d J=%-4d A=%-4d C1=%-4d L=%-9d tail=%-4d W=%-8d"%verify(p))
    print("PASS: 31 independent-band exact W216 comparisons")
