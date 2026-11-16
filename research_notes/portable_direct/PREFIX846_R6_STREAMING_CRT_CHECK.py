#!/usr/bin/env python3
"""Exact verifier of the PREFIX-846 periodic time-multiplexed modular BRC observer.
Only Python integers; no approximations. Usage: python PREFIX846_R6_STREAMING_CRT_CHECK.py
"""
from math import gcd, lcm
from itertools import combinations_with_replacement, product
import json

def cp_part(m, C):
    while True:
        d=gcd(m,C)
        if d==1: return m
        m//=d

def fiber_mod(moduli, cvals):
    ans=1
    for m,c in zip(moduli,cvals):
        ans=lcm(ans,m//gcd(m,c))
    return ans

def brute_opt(N,C,k):
    for B in range(0,10):
        avail=[m for m in range(1,(1<<B)+1) if gcd(m,C)==1]
        for sel in combinations_with_replacement(avail,k):
            if lcm(*sel)>=N:
                return B,sel
    raise RuntimeError('bound insufficient')

def prime_powers(limit,C):
    out=[]
    for prime in range(2,limit+1):
        if any(prime%d==0 for d in range(2,int(prime**.5)+1)): continue
        if gcd(prime,C)!=1: continue
        powers=[]
        q=prime
        while q<=limit:
            powers.append(q)
            q*=prime
        out.append(powers)
    return out

def primepack_max(B,C,k):
    cap=1<<B
    states={(1,)*k}
    for powers in prime_powers(cap,C):
        new=set(states)
        for state in states:
            for q in powers:
                for j in range(k):
                    if state[j]*q<=cap:
                        s=list(state);s[j]*=q
                        new.add(tuple(sorted(s)))
        states=new
    return max(lcm(*s) for s in states)

def check_fibers():
    cases=0;pairs=0
    for a,b,moduli in product((1,2,3),(1,2,3),product(range(1,9), repeat=3)):
        C=a*b
        for t in (1,2,4):
            c=[a**((t+j)//2)*b**((t+j-1)//2) for j in range(3)]
            L=fiber_mod(moduli,c)
            observations={}
            for U in range(13):
                v=tuple(c[j]*(7+U)%moduli[j] for j in range(3))
                observations[U]=v
            for U in range(13):
                for V in range(13):
                    assert (observations[U]==observations[V]) == ((U-V)%L==0)
                    pairs+=1
            cases+=1
    return cases,pairs

def main():
    cases,pairs=check_fibers()
    exact=[]; windows=0; rep_tests=0; pack_tests=0
    for C,N,k in product((2,6,30),(4,16,64),(1,2,3)):
        B,sel=brute_opt(N,C,k)
        if B<=5:
            assert primepack_max(B,C,k)>=N
            if B>0: assert primepack_max(B-1,C,k)<N
            pack_tests+=1
        # Period-k sequence, all windows of length k see each modulus once.
        # Use (a,b)=(C,1), so operation weights remain positive.
        for t in range(1,12):
            c=[C**((t+j)//2) for j in range(k)]
            ms=[sel[(t+j-1)%k] for j in range(k)]
            assert fiber_mod(ms,c)==lcm(*sel)
            readouts=set()
            for U in range(N):
                readouts.add(tuple(c[j]*(7+U)%ms[j] for j in range(k)))
            assert len(readouts)==N
            windows+=1
        exact.append({'C':C,'N':N,'window':k,'min_bits':B,'periodic_moduli':list(sel),'lcm':lcm(*sel)})
    print(json.dumps({'status':'ALL_EXACT_ASSERTIONS_PASSED','scope':'bounded finite checks only; general theorems by proof', 'fiber_cases':cases,'fiber_pair_comparisons':pairs,'exact_optima':len(exact),'window_checks':windows,'primepack_optimum_crosschecks':pack_tests,'exact_table':exact},indent=2))

if __name__=='__main__':main()
