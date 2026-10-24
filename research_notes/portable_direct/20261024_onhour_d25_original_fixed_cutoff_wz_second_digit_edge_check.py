#!/usr/bin/env python3
"""Original-source fixed-cut WZ exact bridge and p^2 column-edge certificate.

Author-only verification. No native CM benchmark, Source run, or formal review.
All arithmetic uses Python standard library Fraction and integer modular inverses.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, gcd

@lru_cache(None)
def fact(k):
    return factorial(k)

@lru_cache(None)
def A(r):
    return F(fact(6*r), 3**(6*r)*fact(2*r)**3)

@lru_cache(None)
def R(r,n):
    return F(fact(4*r+2*n)*fact(2*r)**2*fact(3*n),
             216**n * fact(2*r+n)**2 * fact(4*r+n)*fact(n)**2)

def T(r,n):
    return A(r)*(6*n+12*r+1)*R(r,n)

def P(r,n):
    return (27*n**4+(324*r+180)*n**3
            +(1836*r*r+1746*r+429)*n*n
            +(4320*r**3+5940*r*r+2706*r+412)*n
            +3456*r**4+6336*r**3+4128*r*r+1184*r+128)

def wg(r,n):
    return F(4*n*P(r,n),9*(n+2*r+1)*(n+4*r+1)
             *(n+4*r+2)*(n+4*r+3)*(6*n+12*r+1))

def frmod(x,mod):
    x=F(x)
    assert gcd(x.denominator,mod)==1, (mod,x)
    return (x.numerator*pow(x.denominator,-1,mod))%mod

def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)),F(0))

def edge_p2(p,r):
    """Proved EDGE-P2 right side, normalized E_(p,r)/p mod p^2."""
    q=(pow(216,p-1,p*p)-1)//p
    D=harmonic(4*r)-2*harmonic(2*r)-q
    L=sum((F(1,d) for d in (2*r+1,4*r+1,4*r+2,4*r+3)),F(0))
    P0=P(r,0)
    P1=4320*r**3+5940*r*r+2706*r+412
    return frmod(A(r)*F(P0+p*(P1+P0*(D-L)),
                      81*(2*r+1)**2*(4*r+1)*(4*r+3)),p*p)

def R_edge_p2(p,r):
    q=(pow(216,p-1,p*p)-1)//p
    return frmod(F(1,18)*(1+p*(harmonic(4*r)-2*harmonic(2*r)-q)),p*p)

def source_edge(p,r):
    return T(r,p)*wg(r,p)

def test():
    primes=(7,13,19,31,37,43,61,67,73,79,97,103,109,127,211)
    ranks=0
    resonance=[]
    for p in primes:
        m=(p-1)//6
        assert p==6*m+1
        for r in range(m):
            ranks+=1
            assert frmod(R(r,p),p*p)==R_edge_p2(p,r),('R',p,r)
            e=source_edge(p,r)
            assert frmod(e/p,p*p)==edge_p2(p,r),('EDGE',p,r)
            assert frmod(A(r)*R(r,p),p)!=0,(p,r)
            if P(r,p)%p==0:
                assert frmod(e/p,p)==0
                resonance.append((p,r,(P(r,p)//p)%p))
    print('PASS independent original Fraction vs universal p^2 edge:',ranks,'rank/prime pairs')
    print('Exact source resonant ranks:',resonance)

    bridge=(13,19,37,43,61,67,73,79)
    for p in bridge:
        m=(p-1)//6
        W=sum((T(0,n) for n in range(p)),F(0))
        S=sum((T(m,n) for n in range(4*m+1)),F(0))
        C=sum((T(m,n) for n in range(4*m+1,p)),F(0))
        B=sum((source_edge(p,r) for r in range(m)),F(0))
        assert W-S==C-B,('RECT',p)
        for n in range(4*m+1,p):
            val=frmod(T(m,n)/p,p)
            assert (val==0)==(n==5*m+1),(p,n,val)
        assert ((frmod((W-S)/p,p*p)-frmod(C/p,p*p)
                 +sum(edge_p2(p,r) for r in range(m)))%(p*p))==0
        print('RECT',p,'(W-S)/p modulo p^2 =',frmod((W-S)/p,p*p))
    print('PASS exact original rectangular bridge:',len(bridge),'source primes')

    for p,r in ((409,4),(1993,5),(2027,11)):
        assert r<(p-1)//6 and P(r,p)%p==0 and P(r,p)%(p*p)!=0
        print('P-RESONANCE',p,r,'P/p modulo p=',(P(r,p)//p)%p)

if __name__=='__main__':
    test()
