#!/usr/bin/env python3
"""Exact reduced-phase height-density from four prime-local projective certificates.

Imports the frozen EC49FVJ stdlib verifier in the same directory.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, prod
from EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_VERIFY import prime_certificate

P = (11,17,19,31)
Q = 720
MASKS = (26112,24768,32256,16704,9600,17280,5760,10368,
         26496,38976,28800,36288,11520,24960,6912,14976)

def main():
    certs={p:prime_certificate(p) for p in P}
    counts=Counter()
    for h in range(Q):
        for n in range(Q):
            if gcd(gcd(h,n),Q)>1:
                continue
            mask=sum(1<<i for i,p in enumerate(P)
                     if (h%(p-1),n%(p-1)) in certs[p]['patterns'])
            counts[mask]+=1
    assert tuple(counts[i] for i in range(16))==MASKS
    assert sum(counts.values())==331776
    def density(primes):
        total=Fraction(0)
        for mask,count in counts.items():
            active=(p for i,p in enumerate(P) if p in primes and mask&(1<<i))
            total += count*(1-Fraction(1,prod(p+1 for p in active)))
        return total/331776
    assert density((11,17))==Fraction(11473,15552)
    assert density((11,17,19))==Fraction(168091,207360)
    assert density(P)==Fraction(36018427,39813120)
    assert density(P)>Fraction(421142,550715)
    for H in (100,300,600):
        forbidden=number=0
        for k in range(2,H+1):
            for h in range(1,k):
                if gcd(h,k)>1:
                    continue
                n=k-h
                number+=1
                forbidden+=int(any(certs[p]['valid'](h,n) for p in P))
        print('finite-height',H,'certified',forbidden,'reduced',number,
              'proportion',round(forbidden/number,9))
    print('primitive mod-720 base count:',sum(counts.values()))
    print('primitive mask counts:',','.join(str(counts[i]) for i in range(16)))
    print('certified density among reduced phases (11,17):',density((11,17)))
    print('certified density among reduced phases (11,17,19):',density((11,17,19)))
    print('certified density among reduced phases (11,17,19,31):',density(P))
    print('decimal:',format(float(density(P)),'.12f'))
    print('ALL PASS')

if __name__=='__main__':
    main()
