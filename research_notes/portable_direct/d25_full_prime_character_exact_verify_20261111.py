#!/usr/bin/env python3
"""Exact finite character-pattern check for W_p; bounded computation only."""
import json
from math import isqrt

def primes(bound):
    for p in range(5,bound+1):
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def verify(p):
    M=p**3
    a=1; w=1
    for k in range(1,p):
        a=a*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,M)%M
        w=(w+(6*k+1)*a)%M
    character=1 if p%3==1 else -1
    expected=(character*p)%M
    assert w==expected,(p,w,expected)
    return {'p':p,'mod3':p%3,'W_mod_p3':w,'expected':expected}

def main():
    rows=[verify(p) for p in primes(10000)]
    assert len(rows)==1227
    out={'status':'EXACT_FINITE_CHECK_ONLY_NO_UNIVERSAL_PROOF',
         'science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
         'range':'all primes 5<=p<=10000','count':len(rows),
         'p_1_mod_3':sum(r['mod3']==1 for r in rows),
         'p_2_mod_3':sum(r['mod3']==2 for r in rows),
         'claim_tested':'W_p = p if p=1 mod3; W_p = -p if p=2 mod3; modulo p^3',
         'rows':rows}
    with open('d25_full_prime_character_exact_certificate_20261111.json','w') as f:
        json.dump(out,f,sort_keys=True,indent=2)
    print('PASS',out['count'],'split',out['p_1_mod_3'],out['p_2_mod_3'])

if __name__=='__main__':main()
