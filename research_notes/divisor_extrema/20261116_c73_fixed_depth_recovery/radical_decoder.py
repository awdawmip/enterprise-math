"""Blind stock-and-center decoder for one original readout.

The public decoder takes only (r,c,g). It retrieves the dyadic center ratio,
scans one landing at a time and verifies a single candidate against the original g.
"""
from fractions import Fraction as Q
from math import gcd, isqrt, prod
import json
from blind_center_decoder import simulate, blind, rising


def linear_factors(r):
    rows=[]
    for i in range(r):
        k=2*(r-i)+1
        shifts={Q(k-1)}
        if i:
            shifts.add(Q(k-1,4))
            shifts.update(map(Q,range(k,4*k)))
        if i+1<r:
            shifts.update(map(Q,range(k-1,4*(k-2)+1)))
        else:
            shifts.update(map(Q,[2,3,4]))
        rows.append([(s.denominator,s.numerator) for s in sorted(shifts)])
    return rows


def sieve(limit):
    smallest=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if smallest[p]!=p: continue
        for n in range(p*p,limit+1,p):
            if smallest[n]==n: smallest[n]=p
    return smallest


def radical_factors(rows,y,smallest):
    prime_set=set()
    for a,b in rows:
        n=a*y+b
        while n>1:
            p=smallest[n]
            prime_set.add(p)
            while n%p==0: n//=p
    return prod(prime_set)


def prepare(r,c):
    rows=linear_factors(r)
    limit=max(1680,max(a*c+b for row in rows for a,b in row))
    smallest=sieve(limit)
    primes=[p for p in range(2,limit+1) if smallest[p]==p]
    data=[]
    for factors in rows:
        options=[(y,prod(a*y+b for a,b in factors),radical_factors(factors,y,smallest))
                 for y in range(2,c+1)]
        data.append(options)
    order=sorted(range(r),key=lambda i:len(rows[i]),reverse=True)
    return rows,primes,data,order


def decode(r,c,R,prepared=None):
    rows,primes,data,order=prepare(r,c) if prepared is None else prepared
    n=((R-1)/rising(c+2*r+2,3*(2*r+1))).numerator
    factors=[]
    for p in primes:
        if n%p: continue
        factors.append(p)
        while n%p==0: n//=p
    if n != 1:
        return None, []
    evidence=Q(prod(factors));land=[None]*r
    steps=[]
    for i in order:
        upper=next((v for v in reversed(land[:i]) if v is not None),c)
        lower=next((v for v in land[i+1:] if v is not None),2)
        pool=[(gcd(rad,evidence.numerator),y,w) for y,w,rad in data[i] if lower<=y<=upper]
        pool.sort(reverse=True)
        if len(pool)>1 and pool[0][0]==pool[1][0]: return None,steps
        winner,y,w=pool[0];land[i]=y
        steps.append((i+1,y,winner.bit_length(),pool[1][0].bit_length() if len(pool)>1 else 0))
        evidence/=w
    return land,steps


def verify_from_original(r,c,g):
    try:
        R,_=blind(r,c,g)
    except (ValueError, ZeroDivisionError):
        return dict(status='undecided')
    candidate,_=decode(r,c,R)
    if candidate is None: return dict(status='undecided')
    gaps=[a-b for a,b in zip([c]+candidate,candidate)]+[candidate[-1]-2]
    candidate_g,_=simulate(gaps)
    if candidate_g!=g: return dict(status='undecided')
    return dict(status='exact g matches',candidate=candidate)


if __name__=='__main__':
    cases=[]
    # Chosen finite controls, not a success-rate sample.
    for gaps in [(701,1991),(1201,1801,2201),(1301,1901,2441,2777),
                 (1900,2046,3553),(4466,2590,2754,4191)]:
        c=sum(gaps)+2;r=len(gaps)-1
        g,_=simulate(gaps)
        result=verify_from_original(r,c,g)
        expected=[];v=c
        for step in gaps[:-1]:v-=step;expected.append(v)
        if 'candidate' in result: assert result['candidate']==expected
        cases.append(dict(r=r,c=c,gaps=gaps,**result))
    print(json.dumps(cases,indent=2))
