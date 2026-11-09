#!/usr/bin/env python3
"""Exact D25 AF4 first-grade second jet + independent high-prime scan.
All computations use integers, factorials and finite-ring inverses, never floats.
Author-side regression only; NOT a native H0/B0 experiment.
"""
from math import factorial

GRADE_PRIMES = (5, 7, 11, 13, 19, 37, 43, 73, 109, 157, 163, 373)

def first_grade(p):
    M, Q = p**4, p**3
    w = ((factorial(p-1)+1)//p) % (p*p)
    fact = [1]*p
    for i in range(1,p):
        fact[i] = fact[i-1]*i % M
    i216, i2304 = pow(216,-1,M),pow(2304,-1,M)
    W=[0]*4; V=[0]*4
    WB=[0]*3; VB=[0]*3
    def unitfac(k):
        x=factorial(k)
        while x%p==0:
            x//=p
        return x%M
    def h(r,q):
        return sum(pow(i,-1,q) for i in range(1,r+1))%q
    def h2(r):
        return sum(pow(i,-2,p) for i in range(1,r+1))%p
    for n in range(p):
        gW=(2*n)//p+(3*n)//p
        gV=(4*n)//p
        an=unitfac(2*n)*unitfac(3*n)*pow(fact[n],-5,M)*pow(i216,n,M)%M
        cn=unitfac(4*n)*pow(fact[n],-4,M)*pow(i2304,n,M)%M
        W[gW]=(W[gW]+(6*n+1)*an*p**gW)%M
        V[gV]=(V[gV]+(8*n+1)*cn*p**gV)%M
        if gW==1:
            r=3*n-p
            base=(-fact[2*n]*fact[r]*pow(fact[n],-5,Q)*pow(i216,n,Q))%Q
            hr=h(r,p*p); j1=(hr-w)%(p*p)
            j2=((hr*hr-h2(r))*pow(2,-1,p)-w*hr)%p
            assert an%Q == base*(1+p*j1+p*p*j2)%Q, ("W",p,n)
            for k,t in enumerate((base,base*j1,base*j2)):
                WB[k]=(WB[k]+(6*n+1)*t)%(Q,p*p,p)[k]
        if gV==1:
            r=4*n-p
            base=(-fact[r]*pow(fact[n],-4,Q)*pow(i2304,n,Q))%Q
            hr=h(r,p*p); j1=(hr-w)%(p*p)
            j2=((hr*hr-h2(r))*pow(2,-1,p)-w*hr)%p
            assert cn%Q == base*(1+p*j1+p*p*j2)%Q, ("V",p,n)
            for k,t in enumerate((base,base*j1,base*j2)):
                VB[k]=(VB[k]+(8*n+1)*t)%(Q,p*p,p)[k]
    chi=1 if pow(-3%p,(p-1)//2,p)==1 else -1
    low=(sum(W[:3])-2*sum(V[:3])+chi*p)%M
    aff=(sum(W)-2*sum(V)+chi*p)%M
    assert low%Q==0 and aff==0, ("AF4",p,aff)
    assert (WB[0]+p*WB[1]+p*p*WB[2])%Q==W[1]//p
    assert (VB[0]+p*VB[1]+p*p*VB[2])%Q==V[1]//p
    L=(W[3]//Q-2*(V[3]//Q))%p
    assert (low//Q+L)%p==0
    return (W,V,WB,VB,low//Q,L)

def af4_residue(p):
    M=p**4
    a=c=1
    W=V=0
    x=pow(216,-1,M); y=pow(2304,-1,M)
    for n in range(p):
        W=(W+(6*n+1)*a)%M
        V=(V+(8*n+1)*c)%M
        if n+1<p:
            u=pow(n+1,-1,M)
            a=a*(2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)*pow(u,5,M)*x % M
            c=c*(4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)*pow(u,4,M)*y % M
    chi=1 if pow(-3%p,(p-1)//2,p)==1 else -1
    return (W-2*V+chi*p)%M

def is_prime(x):
    if x<2:return False
    for d in range(2,int(x**0.5)+1):
        if x%d==0:return False
    return True

if __name__=="__main__":
    for p in GRADE_PRIMES:
        w,v,wb,vb,low,L=first_grade(p)
        if p==373:
            print("p373 grade1 jets",wb,vb,"low/373^3",low,"L",L)
            print("p373 four source grades",w,v)
    ps=[p for p in range(1002,4001) if is_prime(p)]
    assert len(ps)==382,len(ps)
    assert all(af4_residue(p)==0 for p in ps)
    print("PASS exact grade-one jets:",len(GRADE_PRIMES),"primes;",
          "AF4 full-cutoff high-prime scan:",len(ps),"primes")
