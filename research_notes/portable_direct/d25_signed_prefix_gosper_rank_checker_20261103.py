#!/usr/bin/env python3
"""Exact independent arithmetic checks for the scoped D25 Gosper/rank lemmas.
Standard library only; neither these finite checks nor the integer polynomial
comparisons replace the written characteristic-zero proof.
"""
from math import comb, isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c

def scale(a,t):return [t*x for x in a]

def check_affine_residual():
    # a(k)=(2k+1)(3k+1)(3k+2), b(k)=36(k+1)^3.
    a=mul(mul([1,2],[1,3]),[2,3]); b=scale(mul(mul([1,1],[1,1]),[1,1]),36)
    # coefficient comparison forces A=-2*alpha, B=alpha-2*beta.
    # k^2 and k^1 coefficients then require -53*alpha+54*beta=0
    # and -89*alpha+82*beta=0. Determinant  (54*(-89)-82*(-53))=-460.
    assert 54*(-89)-82*(-53)==-460
    # For the physical signed weight 6k+1, A=-12, B=4.
    R=[4,-12]; R_next=[-8,-12]
    residual=add(add(mul(a,R_next),scale(mul(b,R),-1)),scale(mul(b,[1,6]),-1))
    assert residual==[-196,-452,-264,0,0],residual
    return residual

def case(p):
    r=(p-1)//6
    a=[1]
    for t in range(1,r+1):
        a.append(a[-1]*(2*t-1)*(3*t-2)*(3*t-1)*pow(18*t**3,-1,p)%p)
    b=[(x*pow(2,-t,p))%p for t,x in enumerate(a)]
    assert all(a) and all(b)
    ell=[comb(r,j)*comb(2*r,j)%p for j in range(r+1)]
    inv=[pow(j*j*a[j],-1,p) if j else 0 for j in range(r+1)]
    def K_of(q):
        K=[0]*r; tail=0
        for t in range(r-1,-1,-1):
            tail=(tail+q[t+1]*inv[t+1])%p
            K[t]=(-a[t]*tail*pow(3,-1,p))%p
        return K
    def observer(q,weight):
        K=K_of(q)
        direct=(pow(2,-1,p)*sum(weight(t)*pow(2,-t,p)*K[t] for t in range(r)))%p
        pref=0; alt=0
        for j in range(1,r+1):
            pref=(pref+weight(j-1)*b[j-1])%p
            alt=(alt-q[j]*inv[j]*pref*pow(6,-1,p))%p
        assert direct==alt,(p,direct,alt)
        return direct
    for q in (ell, [0]+[(j*j+3*j+1)%p for j in range(1,r+1)]):
        for weight in (lambda t: 6*t+1, lambda t:1, lambda t:t): observer(q,weight)
    # Signed scalar map's first two source coefficients, an explicit kernel fiber.
    T1=1; T2=(T1+7*b[1])%p
    c1=(-pow(6*a[1],-1,p))%p
    c2=(-T2*pow(24*a[2],-1,p))%p
    q=[0]*(r+1);q[1]=c2;q[2]=(-c1)%p
    assert (c1*q[1]+c2*q[2])%p==0
    assert observer(q,lambda t:6*t+1)==0
    assert any(K_of(q))  # Nontrivial source changes invisible to signed scalar.
    # Vandermonde and diagonal factors for full polynomial observer readback.
    assert all(i%p for i in range(1,r+1)) and r<p
    return dict(p=p,r=r,c1=c1,c2=c2,k0=K_of(q)[0])

if __name__=='__main__':
    res=check_affine_residual()
    cases=[case(p) for p in range(13,2001) if prime(p) and p%24 in (13,19)]
    assert len(cases)==77,len(cases)
    print('AFFINE_GOSPER_RESIDUAL =',res)
    print('MODULAR_SCOPED_CHECK = PASS; target primes =',len(cases))
    for wanted in (13,19,37,373):
        print('WITNESS',next(x for x in cases if x['p']==wanted))
    print('RESULT = PASS')
