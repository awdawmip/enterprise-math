#!/usr/bin/env python3
"""Exact finite fixed-kappa penultimate bad-seed projective counts; standard library."""
import json
from math import isqrt
PRIMES = (17, 31, 59, 73, 101)
EXPECTED_OLD = {17:36, 31:1144}
def is_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def qmax_for(p):
    q=0
    while 42**3 * (q+1)**3 < p**5:
        q+=1
    assert (42**3*q**3 < p**5) if q else True
    assert 42**3*(q+1)**3>=p**5
    return q
def count(p):
    assert is_prime(p) and p%7 in (3,5)
    qmax=qmax_for(p)
    choices=tuple((v,v*v) for v in range(-isqrt(qmax),isqrt(qmax)+1))
    signed=0
    signatures=set()
    def visit(depth, rem, vector):
        nonlocal signed
        if depth==0:
            if not any(vector):return
            signed+=1
            residue=tuple(v%p for v in vector)
            pivot=next(v for v in residue if v)
            inv=pow(pivot,-1,p)
            signatures.add(tuple((v*inv)%p for v in residue))
            return
        for v,sq in choices:
            if sq<=rem:
                visit(depth-1,rem-sq,vector+(v,))
    visit(6,qmax,())
    assert signed%2==0 and len(signatures)<=signed//2
    if p in EXPECTED_OLD:assert len(signatures)==EXPECTED_OLD[p]
    den=sum(p**j for j in range(6))
    return dict(p=p,f=6,s=5,kappa='1/sqrt(42)',max_Q=qmax,
       signed_witnesses=signed,distinct_projective_atoms=len(signatures),
       dual_seed_atoms=den,bad_fraction_exact=f'{len(signatures)}/{den}')
if __name__=='__main__':
    print(json.dumps({'schema':'X6CM_FIXED_KAPPA_PENULTIMATE_V1',
      'scope':'Finite results; infinite r-independence is proven separately in the note',
      'data':[count(p) for p in PRIMES]},indent=2))
