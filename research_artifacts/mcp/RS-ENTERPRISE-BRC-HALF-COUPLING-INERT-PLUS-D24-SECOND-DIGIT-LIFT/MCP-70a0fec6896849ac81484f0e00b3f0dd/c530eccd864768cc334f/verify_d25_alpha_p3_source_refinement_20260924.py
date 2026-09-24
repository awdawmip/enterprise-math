#!/usr/bin/env python3
"""Regression/falsification only for the D25 p^3 raw coefficient refinement."""
def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d == 0: return False
        d += 2
    return True

def inv(a,m): return pow(a % m,-1,m)

class Q2:
    __slots__=("a","b","m")
    def __init__(self,a,b,m): self.a=a%m; self.b=b%m; self.m=m
    def co(self,o): return o if isinstance(o,Q2) else Q2(o,0,self.m)
    def __add__(self,o):
        o=self.co(o); return Q2(self.a+o.a,self.b+o.b,self.m)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b,self.m)
    def __sub__(self,o): return self+(-self.co(o))
    def __rsub__(self,o): return self.co(o)-self
    def __mul__(self,o):
        o=self.co(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a,self.m)
    __rmul__=__mul__
    def __eq__(self,o):
        o=self.co(o)
        return self.m==o.m and self.a==o.a and self.b==o.b

def red(x,m): return Q2(x.a,x.b,m)

def divp(x,p,m):
    assert x.a%p==0 and x.b%p==0
    return Q2(x.a//p,x.b//p,m)

def check(p):
    assert p%24 in (13,19)
    p2,p3=p*p,p*p*p
    r=(p-1)//6; n=2*r
    t3=Q2(2*inv(4,p3),-inv(4,p3),p3)
    lam3=Q2(inv(2,p3),0,p3)
    assert 4*t3*(1-t3)==lam3

    H1=[0]*p; H2=[0]*p
    for q in range(1,p):
        H1[q]=(H1[q-1]+inv(q,p2))%p2
        H2[q]=(H2[q-1]+inv(q*q,p))%p

    H=Q2(0,0,p3); F=Q2(0,0,p3); G=Q2(0,0,p3)
    D=Q2(0,0,p2); M=Q2(0,0,p)
    tp3=Q2(1,0,p3); lp3=Q2(1,0,p3)
    tp2=Q2(1,0,p2); tp1=Q2(1,0,p)
    C=A=B=1; A2=A1=1

    for j in range(n+1):
        H += tp3*C
        F += tp3*A
        G += lp3*B
        h1=(H1[3*j]-H1[j])%p2
        D += tp2*(A2*h1%p2)
        h2=(H2[3*j]-H2[j])%p
        mcoef=A1*((h1%p)*(h1%p)-h2)%p*inv(2,p)%p
        M += tp1*mcoef
        if j<n:
            C=C*(p-1-3*j)*(p-2-3*j)*(p-3-3*j)*inv(27*(p-1-j)*(j+1)*(j+1),p3)%p3
            A=A*(3*j+1)*(3*j+2)*inv(9*(j+1)*(j+1),p3)%p3
            B=B*(6*j+1)*(3*j+1)*inv(18*(j+1)*(j+1),p3)%p3
            A2=A2*(3*j+1)*(3*j+2)*inv(9*(j+1)*(j+1),p2)%p2
            A1=A1*(3*j+1)*(3*j+2)*inv(9*(j+1)*(j+1),p)%p
            tp3=tp3*t3; lp3=lp3*lam3
            tp2=tp2*red(t3,p2); tp1=tp1*red(t3,p)

    assert H == F-p*Q2(D.a,D.b,p3)+p*p*Q2(M.a,M.b,p3)
    T=G-F
    assert T.a%p==0 and T.b%p==0
    E=divp(T,p,p2)
    assert H == G-p*Q2((D+E).a,(D+E).b,p3)+p*p*Q2(M.a,M.b,p3)
    assert H.a%p==0 and H.b%p==0 and G.a%p==0 and G.b%p==0
    alphaHat=divp(H,p,p2)
    GThat=divp(G,p,p2)
    assert alphaHat == GThat-(D+E)+p*Q2(M.a,M.b,p2)

targets=[p for p in range(5,5000) if prime(p) and p%24 in (13,19)]
assert len(targets)==166
for p in targets: check(p)
print("PASS",len(targets),"target primes: p^3 source coefficient refinement")
