#!/usr/bin/env python3
"""Finite diagnostic ONLY, no universal CM parity claim; exact prime/field arithmetic."""
from d25_gh129_blind_band_check import add,div,fact_tables,coefficient_prediction

def isprime(n):
    if n<2:return False
    return all(n%k!=0 for k in range(2,int(n**.5)+1))

def run():
    primes=[p for p in range(11,400,8) if isprime(p)]
    cases=0
    for p in primes:
        N=(p-1)//2
        B=div(add((1,0),div((0,2),(3,0),p),p),(8,0),p)
        fac,ifac=fact_tables(p)
        for s in range(1,N+1):
            v,_=coefficient_prediction(p,B,s,fac,ifac)
            assert (s%2 and v[1]==0) or (s%2==0 and v[0]==0),(p,s,v)
            cases+=1
    print('FINITE_ONLY GH130 marked-conjugation parity tested primes',primes)
    print('FINITE_ONLY GH130 pairs',cases,'violations',0)
    print('PASS_GH130_FINITE_PARITY_DIAGNOSTIC')

if __name__=='__main__':run()
