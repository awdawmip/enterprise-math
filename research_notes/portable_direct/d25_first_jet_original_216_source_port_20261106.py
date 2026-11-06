#!/usr/bin/env python3
"""D25 original-216/first-tangent coefficient bridge: exact modular verifier.

No native experiment, no Source checkpoint, no third-party dependencies.
"""
from math import isqrt

def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            sieve[d*d:limit+1:d] = b'\x00' * ((limit-d*d)//d+1)
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]

def check(p):
    m = (p-1)//6
    a,b,c = 2*m,3*m,4*m
    P = p*p
    h = 1      # original 216 coefficient modulo p^2
    U = 1      # lifted finite binomial coefficient
    D = 0      # p-adic parameter-shift correction
    u,e = 1,0  # finite-field base and directional tangent
    W = Utot = regular_correction = Z = S = single_carry = 0
    for j in range(p):
        w = 6*j+1
        W = (W+w*h)%P
        if j<=a:
            Utot = (Utot+w*U)%P
            regular_correction = (regular_correction+w*(U%p)*D)%p
            assert h%p==U%p==u
            assert (h-U)%P == p*(U%p)*D%P
        if a<j<=b:
            assert h%p==0 and u==0
            assert (h//p)%p == -e*pow(3,-1,p)%p
            single_carry = (single_carry+w*e)%p
        if j==m:
            assert w==p and h%p==u
            assert (w*e)%p==0
        if j==5*m:
            assert h%P==u==e==0
        Z=(Z+u)%p
        S=(S+w*e)%p
        if j==p-1: break
        # Two independent base recurrences; no inverse of a zero term.
        h=h*((2*j+1)*(3*j+1)*(3*j+2))*pow(36*(j+1)**3,-1,P)%P
        T=(a-j,b-j,c-j)
        triple=T[0]*T[1]*T[2]
        pairs=T[0]*T[1]+T[0]*T[2]+T[1]*T[2]
        fac=pow(-2*(j+1)**3,-1,p)
        cc=triple*fac%p
        dd=(pairs+3*triple*pow(j+1,-1,p))*fac%p
        e=(cc*e+dd*u)%p
        u=cc*u%p
        if j<a:
            U=U*(-triple)*pow(2*(j+1)**3,-1,P)%P
            D=(D+pow(3,-1,p)*pow(j-a,-1,p)
                 +pow(2,-1,p)*pow(j-b,-1,p)
                 +2*pow(3,-1,p)*pow(j-c,-1,p))%p
    port=(Utot+p*(regular_correction-single_carry*pow(3,-1,p)))%P
    assert port==W, (p,"signed whole-sum p^2 bridge")
    # First-digit and Theta checks are exact FINITE evidence, not a proof
    # of a universal first digit or a universal Theta conjecture.
    assert W%p==Utot%p==0
    theta=(W//p-Z+S*pow(6,-1,p))%p
    return p,m,W//p,Z,S,single_carry,theta

if __name__=='__main__':
    rows=[check(p) for p in primes(3000)]
    assert len(rows)==207
    for p in (7,13,19,37,373,1009):
        print(check(p))
    print("PASS 207/207: independent original p^2 and source-first-jet checks")
    print("FINITE Theta==0:",sum(row[-1]==0 for row in rows),"/207")
