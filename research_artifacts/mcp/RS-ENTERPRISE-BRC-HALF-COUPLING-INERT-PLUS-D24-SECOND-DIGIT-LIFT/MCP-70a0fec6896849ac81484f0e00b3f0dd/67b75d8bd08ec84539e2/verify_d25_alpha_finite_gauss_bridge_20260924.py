#!/usr/bin/env python3
"""Regression/falsification only for the exact alpha_p finite-Gauss bridge.
The accompanying note carries the all-prime proof.
"""
from math import isqrt

def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def inv(a,m): return pow(a % m,-1,m)

class Q2:
    # a+b*s in (Z/mZ)[s]/(s^2-2)
    __slots__=('a','b','m')
    def __init__(self,a,b,m): self.a=a%m; self.b=b%m; self.m=m
    def __add__(self,o):
        if isinstance(o,int): o=Q2(o,0,self.m)
        return Q2(self.a+o.a,self.b+o.b,self.m)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b,self.m)
    def __sub__(self,o): return self + (-o if not isinstance(o,int) else Q2(-o,0,self.m))
    def __rsub__(self,o): return Q2(o,0,self.m)-self
    def __mul__(self,o):
        if isinstance(o,int): o=Q2(o,0,self.m)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a,self.m)
    __rmul__=__mul__
    def __eq__(self,o):
        if isinstance(o,int): return self.a == o%self.m and self.b == 0
        return self.m==o.m and self.a==o.a and self.b==o.b

def divp(x,p):
    assert x.m==p*p and x.a%p==0 and x.b%p==0
    return Q2(x.a//p,x.b//p,p)

def check(p):
    assert p % 24 in (13,19) and p % 6 == 1
    p2=p*p; r=(p-1)//6; n=2*r
    t=Q2(2*inv(4,p2),-inv(4,p2),p2) # (2-sqrt(2))/4
    lam=Q2(inv(2,p2),0,p2)
    assert 4*t*(1-t) == lam

    hp=[0]*p
    for q in range(1,p): hp[q]=(hp[q-1]+inv(q,p))%p

    H=Q2(0,0,p2); F=Q2(0,0,p2); S=Q2(0,0,p2); D=Q2(0,0,p)
    tp=Q2(1,0,p2); lp=Q2(1,0,p2); tp1=Q2(1,0,p)
    C=A=B=1
    for j in range(n+1):
        H += tp*C
        F += tp*A
        D += tp1*((A%p)*((hp[3*j]-hp[j])%p))
        S += lp*B

        # B_k has valuation zero through r and exactly one on r<k<=2r.
        if j <= r: assert B % p != 0
        else: assert B % p == 0 and B % p2 != 0

        if j < n:
            C = C*(p-1-3*j)*(p-2-3*j)*(p-3-3*j)*inv(27*(p-1-j)*(j+1)*(j+1),p2)%p2
            A = A*(3*j+1)*(3*j+2)*inv(9*(j+1)*(j+1),p2)%p2
            B = B*(6*j+1)*(3*j+1)*inv(18*(j+1)*(j+1),p2)%p2
            tp = tp*t; lp = lp*lam
            tp1 = tp1*Q2(t.a%p,t.b%p,p)

    # BOX 1: exact d=3 coefficient deformation through p^2.
    assert H == F-Q2(p*D.a,p*D.b,p2)

    # Supersingular source and finite-Gauss unit band are p-divisible.
    assert H.a%p==0 and H.b%p==0
    assert S.a%p==0 and S.b%p==0

    # Finite quadratic truncation tail is p-divisible.
    T=S-F
    assert T.a%p==0 and T.b%p==0

    alpha=divp(H,p)
    GT=divp(S,p)
    E=divp(T,p)
    # BOX 3: alpha_p = G_T-D_p-E_p.
    assert alpha == GT-D-E
    return alpha,GT,D,E

targets=[p for p in range(5,5000) if prime(p) and p%24 in (13,19)]
assert len(targets)==166
for p in targets: check(p)
print('PASS',len(targets),'target primes: exact H deformation, valuation band, quadratic tail, alpha/G_T bridge')
