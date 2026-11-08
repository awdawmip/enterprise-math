#!/usr/bin/env python3
"""Exact author-side W/V third-digit source comparison; not a native H0/B0 run."""
from math import comb
import json
from d25_source68_crosswalk_exact_check_20261109 import exact_rising

def v_full(p):
    modulus=p**3
    inverse=pow(2304,-1,modulus)
    scale=1
    total=0
    for n in range(p):
        total=(total+(8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*scale)%modulus
        scale=(scale*inverse)%modulus
    return total

def legendre(a,p):
    t=pow(a%p,(p-1)//2,p)
    return -1 if t==p-1 else 1

if __name__ == '__main__':
    results=[]
    for p in (5,7,11,13,17,19,23,29,31,41,47,71,97,157,163):
        w=exact_rising(p)
        v=v_full(p)
        chi=legendre(-3,p)
        assert (w-v)%(p**3)==0
        assert v==p*chi%(p**3)
        results.append({'p':p,'chi_minus3':chi,'W_p':w,'V_p':v,'difference_mod_p3':(w-v)%(p**3)})
    print(json.dumps({'scope':'AUTHOR_SIDE_FINITE_COMPARISON_NOT_UNIFORM_PROOF_NOT_NATIVE','results':results},indent=2))
