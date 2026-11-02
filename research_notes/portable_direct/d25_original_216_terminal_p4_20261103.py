#!/usr/bin/env python3
"""Checks the proved original-216 universal p^4 terminal correction."""
from math import comb
import json
def primes(N):
    b=[True]*(N+1); b[:2]=[False,False]
    for d in range(2,int(N**.5)+1):
        if b[d]:
            for k in range(d*d,N+1,d):b[k]=False
    return [p for p in range(5,N+1) if b[p]]
def terminal(p):
    k=p-1; m=p**4
    B=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)%m
    assert B%p**3==0
    assert B//p**3==p-1, (p,B)
    assert (6*k+1)*B%m == (5*p**3)%m
def W(p):
    m=p**4; b=1; total=0; short=0
    for k in range(p):
        total=(total+(6*k+1)*b)%m
        if k==p-2:short=total
        if k<p-1:
            b=b*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m
    assert (total-short)%m==5*p**3%m
    return [total,short,(total-p)%m//p**3]
if __name__=="__main__":
    P=primes(1000)
    for p in P:terminal(p)
    samples=[13,19,37,43,61,67,109,139,181,373,1171]
    out={str(p):W(p) for p in samples}
    print(json.dumps({"schema":"D25_ORIGINAL_216_TERMINAL_P4_CHECK_V1",
       "all_primes_5_to_1000_checked":len(P),
       "sample_triplets_W_full_W_minus2_third_digit":out,
       "native_H0_B0_executed":False,
       "status":"AUTHOR_FINITE_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED"},sort_keys=True,indent=2))
