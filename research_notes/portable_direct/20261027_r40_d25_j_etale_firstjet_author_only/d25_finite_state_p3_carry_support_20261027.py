#!/usr/bin/env python3
"""Exact author-side p^3 coefficient support selector; not a native H0/B0 run."""
from collections import defaultdict
from math import comb
import json

CARRY = ((0, 0), (0, 1), (1, 1))

def ceil_div(a, b):
    return -(-a // b)

def valuation_legendre(n, p):
    """Independent factorial Legendre oracle."""
    power, v = p, 0
    while power <= 3 * n:
        v += 3*n//power + 2*n//power - 5*(n//power)
        power *= p
    return v

def valuation_carries(n, p):
    """Actual signed-index source keeps separate 2n and 3n carry channels."""
    a = b = v = 0
    while n:
        d, n = n % p, n // p
        a, b = (2*d+a)//p, (3*d+b)//p
        v += a+b
    return v

def matrix_counts(p):
    assert p >= 5 and p % 6 in (1, 5)
    r = (p+1)//6 if p%6 == 5 else (p-1)//6
    delta = int(p%6 == 1)
    q, z, t = 2*r+delta, 2*r, r+delta
    return ((q,r,r),(z,t,r-1+delta),(z,r-1+delta,t))

def count_below(N,p):
    """Exact # indices n<N with valuation <3; O(log_p(N+1)) digit intervals."""
    assert p>=5 and p%6 in (1,5) and N>=0
    if N==0: return 0
    digits=[]
    while N:
        digits.append(N%p); N//=p
    # (old carry state, accumulated valuation, LSD-first bound comparison)
    dp={(0,0,0):1}
    by_pair={pair:i for i,pair in enumerate(CARRY)}
    for digit in digits:
        ndp=defaultdict(int)
        for (state,v,cmp),ways in dp.items():
            a,b=CARRY[state]
            cuts={0,p,digit,min(p,digit+1),
                  ceil_div(p-a,2),ceil_div(p-b,3),
                  ceil_div(2*p-b,3)}
            cuts=sorted(x for x in cuts if 0<=x<=p)
            for lo,hi in zip(cuts,cuts[1:]):
                if lo>=hi: continue
                a1,b1=(2*lo+a)//p,(3*lo+b)//p
                v1=v+a1+b1
                if v1>=3:continue
                cmp1=-1 if lo<digit else (1 if lo>digit else cmp)
                ndp[by_pair[(a1,b1)],v1,cmp1]+=ways*(hi-lo)
        dp=ndp
    return sum(ways for (state,v,cmp),ways in dp.items() if cmp==-1)

def closed_power_count(p,e):
    assert p>=5 and p%6 in (1,5) and e>=0
    if e==0:return 1
    r=(p+1)//6 if p%6==5 else (p-1)//6
    if p%6==5:
        return (2*r)**e*(e*e+7*e+8)//8
    q,z,t=2*r+1,2*r,r+1
    if e==1:return q+2*r
    tail=0 if e<4 else (e-2)*(e-3)//2*r*r*z*z*q**(e-4)
    return (q**e+2*r*(q**(e-1)+(e-1)*z*q**(e-2))
            +r*(t+(e-2)*z)*q**(e-2)+tail)

def cmod(k,p):
    mod=p**3
    return comb(3*k,k)*comb(2*k,k)**2*pow(216,-k,mod)%mod

def umod(j,p):
    mod=p**3
    return comb(2*j,j)*pow(8,-j,mod)%mod

def signed_check(p,N):
    mod=p**3
    C=[cmod(k,p) for k in range(N)]
    U=[umod(j,p) for j in range(N)]
    keep=[valuation_carries(k,p)<3 for k in range(N)]
    assert sum(keep)==count_below(N,p)
    assert all(C[k]==0 for k in range(N) if not keep[k])
    W=sum((6*k+1)*C[k] for k in range(N))%mod
    W2=sum((6*k+1)*C[k] for k in range(N) if keep[k])%mod
    S=sum((3*(j+k)-1)*U[j]*C[k]
          for k in range(N) for j in range(N-k))%mod
    S2=sum((3*(j+k)-1)*U[j]*C[k]
           for k in range(N) if keep[k] for j in range(N-k))%mod
    assert (W,S)==(W2,S2)
    return {'p':p,'N':N,'active':sum(keep),'W_mod_p3':W,'S_mod_p3':S}

def main():
    ps=(5,7,11,13,19,31,37,43)
    checked=0
    for p in ps:
        M=matrix_counts(p)
        for i,(a,b) in enumerate(CARRY):
            row=[0,0,0]
            for d in range(p):
                pair=((2*d+a)//p,(3*d+b)//p)
                if sum(pair)<3:
                    assert pair in CARRY
                    row[CARRY.index(pair)]+=1
            assert tuple(row)==M[i]
        for e in range(8):
            assert count_below(p**e,p)==closed_power_count(p,e)
        for N in (1,p-1,p,p+1,2*p+3,p**2-1,p**2+7):
            oracle=sum(valuation_legendre(n,p)<3 for n in range(N))
            assert count_below(N,p)==oracle
            checked+=N
        for n in range(min(p**3,2000)):
            assert valuation_carries(n,p)==valuation_legendre(n,p)
        if p<=19:
            for e in (1,2,3):
                N=p**e
                assert count_below(N,p)==sum(valuation_legendre(n,p)<3 for n in range(N))
                checked+=N
    examples=[signed_check(p,2*p+3) for p in (5,7,11,13,19)]
    large=[{'p':p,'e':e,'active':closed_power_count(p,e),'total':p**e}
           for p,e in ((5,8),(7,8),(13,6),(19,6),(43,5),(373,4))]
    print(json.dumps({'status':'PASS','scope':'AUTHOR_EXACT_CHECK_NOT_NATIVE',
                      'checked_primes':ps,'oracle_indices_at_least':checked,
                      'signed_examples':examples,'large_counts':large,
                      'review':'UNREVIEWED_NOT_ADMITTED'},indent=2))

if __name__=='__main__':
    main()
