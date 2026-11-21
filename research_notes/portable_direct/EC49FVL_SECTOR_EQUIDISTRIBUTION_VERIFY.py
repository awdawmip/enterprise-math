#!/usr/bin/env python3
"""EC49FVL: exact directional finite-height checks, under frozen BRC16943.
Only author-side test; the asymptotic theorem is proved analytically in the accompanying note.
"""
from fractions import Fraction
from math import gcd, prod
from collections import Counter

U = Fraction(4822040484, 8132285009)
GAMMA = Fraction(141024, 1653649)
PRIMES = (11, 17, 19, 31)
Q = 720
DELTA = Fraction(36018427, 39813120)
EXPECTED_MASKS = (26112,24768,32256,16704,9600,17280,5760,10368,
                  26496,38976,28800,36288,11520,24960,6912,14976)


def prime_certificate(p):
    def mod(q):
        assert q.denominator % p
        return q.numerator * pow(q.denominator, -1, p) % p
    u, gamma = mod(U), mod(GAMMA)
    inv637 = pow(637, -1, p)
    c, d = mod(Fraction(-3,637)), u*gamma % p
    assert c != d
    rows=[]
    for z in range(p):
        la=(637-3*z)*inv637%p
        lb=u*(1+gamma*z)%p
        a=(1-(1-z)*la)%p
        b=(1-(1-z)*lb)%p
        rows.append((z,a,b,la,lb))
    singular=[r for r in rows if r[3]==r[4]]
    assert len(singular)==1
    z,a,b,la,lb=singular[0]
    assert a==b and la==lb and a and la
    alpha,beta=-(1-z)*la%p,a%p
    assert alpha and beta
    finite=[r for r in rows if r[0]!=z]
    patterns=set()
    for hh in range(1,p):
        for nn in range(1,p):
            good=True
            for _,aa,bb,ll,mm in finite:
                v=(pow(aa,hh,p)*pow(ll,nn,p)-pow(bb,hh,p)*pow(mm,nn,p))*pow((ll-mm)%p,-1,p)%p
                if v==0:
                    good=False
                    break
            if good and (pow(c,hh+nn,p)-pow(d,hh+nn,p))%p:
                patterns.add((hh%(p-1),nn%(p-1)))
    assert len(patterns)=={11:44,17:96,19:66,31:402}[p]
    return patterns,alpha,beta


def main():
    certs={p:prime_certificate(p) for p in PRIMES}
    marks=Counter()
    for h in range(Q):
        for n in range(Q):
            if gcd(gcd(h,n),Q)!=1:
                continue
            mask=sum((1<<i) for i,p in enumerate(PRIMES)
                     if (h%(p-1), n%(p-1)) in certs[p][0])
            marks[mask]+=1
    assert tuple(marks[i] for i in range(16))==EXPECTED_MASKS
    calc=sum((Fraction(v)*(1-Fraction(1,prod(p+1 for i,p in enumerate(PRIMES)
                                                       if mask&(1<<i))))
              for mask,v in marks.items()),Fraction(0))/331776
    assert calc==DELTA
    print('CRT primitive mask verification: ALL PASS', 'density',DELTA)
    for H in (100,300,600,1000):
        local=[0,0,0]
        total=[0,0,0]
        seen=0
        hits=0
        for k in range(2,H+1):
            for h in range(1,k):
                if gcd(h,k)!=1:
                    continue
                n=k-h
                j=min(2,3*h//k)
                total[j]+=1
                seen+=1
                ok=any((h%(p-1),n%(p-1)) in certs[p][0] and
                       (certs[p][1]*h+certs[p][2]*n)%p!=0
                       for p in PRIMES)
                if ok:
                    local[j]+=1
                    hits+=1
        print('H',H,'primitive',seen,'certified',hits,'global_rate',
              format(hits/seen,'.9f'), 'sectors',
              [(a,b,format(a/b,'.9f') if b else 'NA') for a,b in zip(local,total)])
        assert sum(total)==seen and sum(local)==hits
    print('ALL PASS: finite exact residue counts; sector uniformity is asymptotic, not inferred from these tests.')


if __name__ == '__main__':
    main()
