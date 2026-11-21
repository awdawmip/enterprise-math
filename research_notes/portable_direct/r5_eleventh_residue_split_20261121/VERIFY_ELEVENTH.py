#!/usr/bin/env python3
"""Exact primitive-eleventh-root coefficient certificate for frozen R5.
Ring Q[z]/Phi_11(z); integer-only cyclotomic arithmetic, no dependencies.
"""
from functools import lru_cache
import json

D=10
ZERO=(0,)*D
ONE=(1,)+(0,)*(D-1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))

@lru_cache(None)
def zpow(k):
    k%=11
    if k==10:return (-1,)*D
    return tuple(int(j==k) for j in range(D))

def mul(a,b):
    v=[0]*19
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    # Phi_11(z)=1+z+...+z^10, z^k=-sum_{j=0}^9 z^(k-10+j).
    for k in range(18,9,-1):
        for j in range(10):v[k-10+j]-=v[k]
    return tuple(v[:10])

def main():
    limit=44
    coeff=[ONE]+[ZERO]*(limit-1)
    # 1/(1-t) times five geometric series in residues 5..9 modulo 11.
    for r in (0,5,6,7,8,9):
        out=[]
        for n in range(limit):
            out.append(add(coeff[n],mul(zpow(r),out[-1]) if n else ZERO))
        coeff=out

    # Entire threshold sequence is periodic mod 11, proved by factorization
    # into (1-t^11)^-1 times the five missing cyclotomic factors.
    assert all(coeff[i]==coeff[i+11] for i in range(33))
    assert all(v!=ZERO for v in coeff[:6])
    assert all(v==ZERO for v in coeff[6:11])

    # Independent bounded enumeration, not generating-function recurrence.
    for m in range(1,13):
        total=ZERO
        for a in range(m):
            for b in range(m-a):
                for c in range(m-a-b):
                    for d in range(m-a-b-c):
                        for e in range(m-a-b-c-d):
                            total=add(total,zpow(5*a+6*b+7*c+8*d+9*e))
        assert total==coeff[m-1],m

    result=dict(
        status="PASS",
        coefficient_basis="Q[z]/(1+z+...+z^10)",
        m1_to_m11=[list(x) for x in coeff[:11]],
        period11_verified=33,
        nonzero_residues_mod11=[1,2,3,4,5,6],
        zero_residues_mod11=[7,8,9,10,0],
        independent_enumeration=list(range(1,13)),
        formal_admission="NOT_REVIEWED"
    )
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
