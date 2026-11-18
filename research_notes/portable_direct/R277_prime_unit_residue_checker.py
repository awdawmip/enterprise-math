#!/usr/bin/env python3
"""R277 exact prime-uniform residue controllability (stdlib Fraction)."""
from fractions import Fraction as F
import json

primes=(2,3,5,7,11,13,17)
counts={}
def vp(x,p):
    x=F(x); n,d=abs(x.numerator),x.denominator; v=0
    if not x: return None
    while n%p==0: n//=p; v+=1
    while d%p==0: d//=p; v-=1
    return v

def unit_mod(x,p):
    x=F(x); assert vp(x,p)>=0
    n,d=x.numerator,x.denominator
    while n%p==0 and d%p==0: n//=p; d//=p
    return n%p*pow(d%p,-1,p)%p

for p in primes:
    count=0
    for t in range(1,5):
        for h in range(1,5):
            residues=set()
            for c in range(1,p):
                P=p**t; M=1+c*p**h
                u=F(P,M*(1+P))
                b=F(2,1+P)
                assert b+u<1 and F(1,2)<1
                D=1-F(1,1+P)-u/F(1+P)-u*u
                exact=F(P*(M-1)*(M+P*(M+1)),M*M*(1+P)**2)
                assert D==exact and vp(D,p)==t+h
                S=(1-u*u)/D
                assert vp(S,p)==-(t+h)
                residue=unit_mod(p**(t+h)*S,p)
                assert residue==pow(c,-1,p)
                residues.add(residue)
                count+=1
            assert residues==set(range(1,p))
    counts[str(p)]=count
print(json.dumps({'status':'PASS','primes':list(primes),'t_range':[1,4],
 'h_range':[1,4],'unit_residues':'ALL_NONZERO',
 'cases_by_prime':counts,'cases_total':sum(counts.values())},sort_keys=True,indent=2))
