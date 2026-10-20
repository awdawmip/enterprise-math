#!/usr/bin/env python3
"""Exact finite checker for filament dual-tangent exceptional-prime cutoffs."""

from __future__ import annotations

import itertools
import math


def prime_factors(n: int):
    n=abs(n); out=set(); p=2
    while p*p<=n:
        while n%p==0:
            out.add(p); n//=p
        p+=1
    if n>1: out.add(n)
    return out


def max_product(k: int):
    best=0
    for a,b in itertools.combinations(range(k),2):
        if (a-b)%2: continue
        for l in range(k):
            if l in (a,b) or (l-a)%2==0: continue
            best=max(best,abs((l-a)*(l-b)))
    return best


def obstruction_support(k: int):
    out=set()
    for a,b in itertools.combinations(range(k),2):
        if (a-b)%2: continue
        for l in range(k):
            if l in (a,b) or (l-a)%2==0: continue
            P=(l-a)*(l-b)
            out |= prime_factors(3*P+1)
            out |= prime_factors(3*P-1)
    return out


def alpha(j: int, chi: int):
    return (3*j*j + (chi if j%2 else 0))//2


def allowed(q: int,k: int,chi: int):
    n=0
    for r in range(q):
        for c in range(q):
            if all((c+3*j*r+alpha(j,chi))%q for j in range(k)):
                n+=1
    return n


def main():
    expected={5:(3,5),6:(15,23),7:(15,23),8:(35,53),9:(35,53)}
    actual_exceptional={
        5:{5},
        6:{7,11,23},
        7:{7,11,13,23},
        8:{11,13,23,31,53},
        9:{11,13,23,31,53},
    }
    for k,(M,Q) in expected.items():
        assert max_product(k)==M
        assert (3*M+1)//2==Q
        # Every obstruction odd prime is below the exact cutoff.
        assert all(p<=Q for p in obstruction_support(k) if p%2)

        got=set()
        # q>=k gives distinct slopes; scan all prime q through Q.
        for q in range(max(5,k),Q+1):
            if q<2 or any(q%d==0 for d in range(2,int(math.isqrt(q))+1)):
                continue
            generic=q*q-k*q+math.comb(k,2)
            if allowed(q,k,1)!=generic or allowed(q,k,-1)!=generic:
                got.add(q)
        assert got==actual_exceptional[k],(k,got)

        # A sample prime above cutoff must be generic in both chiralities.
        q=Q+1
        while True:
            q+=1
            if all(q%d for d in range(2,int(math.isqrt(q))+1)):
                break
        generic=q*q-k*q+math.comb(k,2)
        assert allowed(q,k,1)==generic
        assert allowed(q,k,-1)==generic

    print("FILAMENT_CUTOFF_STAIRCASE=PASS")
    print("K5=5; K6_K7=23; K8_K9=53")
    print("GENERIC_SURVIVOR=q^2-kq+C(k,2)")

if __name__=="__main__":
    main()
