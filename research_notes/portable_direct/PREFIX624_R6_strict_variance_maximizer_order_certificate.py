#!/usr/bin/env python3
"""PREFIX624 R6 exact BRC signed-label survivor shape and comparison certificate."""
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

D=1<<18
MAX_N=189
checks={'dyadic':0,'shape':0,'symmetry':0,'positive_alpha':0}

def inside(n,k,a):
    checks['dyadic']+=1
    return 40*(n+1)*comb(n,k)*a**k*(D-a)**(n-k)>D**n

def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*D//n
    assert inside(n,k,mid)
    if k==0:
        l0=l1=0
    else:
        lo,hi=0,mid
        assert not inside(n,k,lo)
        while hi-lo>1:
            z=(lo+hi)//2
            if inside(n,k,z): hi=z
            else: lo=z
        l0,l1=lo,hi
    lo,hi=mid,D
    assert not inside(n,k,hi)
    while hi-lo>1:
        z=(lo+hi)//2
        if inside(n,k,z): lo=z
        else: hi=z
    r0,r1=lo,hi
    if 4*(r0-l1)>D: return True
    if 4*(r1-l0)<D: return False
    raise AssertionError((n,k,'unresolved dyadic gap'))

A={0:1}
rows=[A.copy()]
for n in range(1,MAX_N+1):
    B=defaultdict(int)
    for k,count in A.items():
        B[k]+=count
        B[k+1]+=count
    A={k:v for k,v in B.items() if wide(n,k)}
    rows.append(A)

assert not rows[MAX_N]
assert all(rows[24].get(k,0)==comb(24,k) for k in range(25))
assert all(rows[25].get(k,0)==(comb(25,k) if 1<=k<=24 else 0)
           for k in range(26))
for n,row in enumerate(rows):
    for k in range(n//2+1):
        a=row.get(k,0)
        assert a==row.get(n-k,0),(n,k,'symmetry')
        checks['symmetry']+=1
        if k<n//2:
            b=row.get(k+1,0)
            assert a*comb(n,k+1)<=b*comb(n,k),(n,k,'shape')
            checks['shape']+=1

for n in range(MAX_N):
    mass=sum((F(comb(m+n,m),2**(m+n+1)) for m in range(25)),F(0))
    assert 0<1-mass<=1,n
    checks['positive_alpha']+=1

# Finite-certified b[n,k] symmetry and unimodality give monotone s_n(p)
# via an exact nonnegative mixture of centered-binomial-band probabilities.
# s_25(p)=1-p**25-(1-p)**25 is STRICTLY increasing for 0<p<1/2.
# Thus mu(p)=25+sum(alpha_n*s_n(p)) strictly increases.
# Previously certified V24=4*V12+24*mu, and endpoint comparisons,
# imply every global V24 maximizer on [0,1/2] exceeds every V12 one.

out={'schema':'PREFIX624_R6_STRICT_EDGE_VARIANCE_MAXIMIZER_ORDER_V1',
     'date':'2026-11-09',
     'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'model':'two signed BRC directions p1=0 p2 in [0,1/2], q=12/24, beta=1/40, width=1/4',
     'theorem':'Every V24 edge global maximizer lies strictly right of every V12 edge global maximizer',
     'variance_identity':'V24=4*V12+24*mu',
     'proof_ingredients':['symmetric central unimodal survivor coefficients for n<=189',
                          'strictly positive alpha_n',
                          's25=1-p**25-(1-p)**25',
                          'PREFIX623 strict interior endpoint comparison'],
     'checks':checks,'verification':'ALL_CHECKS_PASS',
     'status':'AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX624_R6_RESULTS.json').write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',checks)
