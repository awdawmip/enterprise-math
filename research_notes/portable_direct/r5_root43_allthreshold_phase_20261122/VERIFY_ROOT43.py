#!/usr/bin/env python3
"""Exact integer verification for R5 primitive-43 period classification.
No floating point: cyclic Z[x]/(x^43-1) and cyclotomic reduction.
"""
from math import comb
from pathlib import Path
import json

D=43
PRICES=tuple(range(214,315))
SUPPORTS=(set(range(214,219)),set((214,216,217,218,219,220,221)),set(range(215,222)),set(range(223,291)),set(range(296,313)))
assert [sorted(s & set(p for p in PRICES if p%D==0)) for s in SUPPORTS] == [[215],[],[215],[258],[301]]
assert [p for p in PRICES if p%D==0]==[215,258,301]
weights=[p%D for p in sorted(SUPPORTS[1])]
assert weights==[42,1,2,3,4,5,6]

def shift(v,k):
    k%=D
    return v[-k:]+v[:-k] if k else v[:]

def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def one():return [1]+[0]*(D-1)
def zero():return [0]*D

def mul(a,b):
    z=zero()
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[(i+j)%D]+=x*y
    return z

def reduce(v):return tuple(v[i]-v[D-1] for i in range(D-1))

NMAX=2*D
h=[zero() for _ in range(NMAX)]
h[0]=one()
# H_r = [u^r] product (1-u*x^a)^(-1)
for a in weights:
    for r in range(1,NMAX):
        h[r]=add(h[r],shift(h[r-1],a))
P=one()
for a in weights:P=mul(P,sub(one(),shift(one(),a)))
Q=zero()
phase=[]
first=[]
for m in range(1,NMAX+1):
    Q=add(Q,h[m-1])
    q=reduce(Q)
    r=reduce(mul(P,Q))
    expected=1<=((m-1)%D)+1<=36
    assert (any(q)==expected),(m,'Q nonzero mismatch')
    assert (any(r)==expected),(m,'R nonzero mismatch')
    if m<=D:
        phase.append(m if expected else 0)
        first.append([m,int(q[0]),int(r[0]),int(sum(Q)%D)])
        if m<=36:assert sum(Q)%D==comb(m+6,7)%D!=0

Q=zero(); vectors=[]
for m in range(1,NMAX+1):
    Q=add(Q,h[m-1]);vectors.append(reduce(Q))
for m in range(1,D+1): assert vectors[m-1]==vectors[m-1+D], m
assert [m for m in range(1,D+1) if m not in phase] == list(range(37,44))
# m4 previous saved cert coordinate at root43 = 1
r4=reduce(mul(P, add(add(add(h[0],h[1]),h[2]),h[3])))
assert r4[0]==1,('previous m4 witness disagrees',r4[0])
certificate={
  'schema':'R5_PRIMITIVE43_ALL_THRESHOLD_CERT_V1',
  'model':'R5 frozen true five-event scalar, prices 214..314',
  'root_order':43,
  'denominator_pole_order':3,
  'price_multiples':[215,258,301],
  'five_supports_multiple43':[[215],[],[215],[258],[301]],
  'unique_surviving_event':1,
  'event1_residue_weights':weights,
  'event1_count':7,
  'threshold_phase_period':43,
  'nonzero_mod43':list(range(1,37)),
  'zero_mod43':[0,37,38,39,40,41,42],
  'verified_m_range':[1,86],
  'verification':'exact Z[x]/(x^43-1), Phi43 projection; complete 86 threshold checks and 43 phase comparisons',
  'm4_first_coordinate':r4[0],
  'sample_numerator_first_coordinate':{str(m):first[m-1][2] for m in [1,5,36,37,43]},
  'comparison_scope':'AUTHOR_EXACT_PROOF; NOT_REVIEWED'
}
print(json.dumps(certificate,ensure_ascii=False,indent=2))
Path(__file__).with_name('CERTIFICATE.json').write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print('ALL CHECKS PASS')
