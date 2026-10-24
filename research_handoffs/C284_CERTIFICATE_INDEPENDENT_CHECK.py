#!/usr/bin/env python3
"""C284 independent verifier: read saved 187 records, do NOT run bisection."""
import json
import hashlib
from fractions import Fraction
import C284_C275_FROZEN_SOURCE as c

d=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf-8'))
assert d['schema']=='C284_DYADIC_THRESHOLD_BRACKETS_V1'
assert d['n']==12 and d['denominator']==4096
rows=d['records']
packed=json.dumps(rows,ensure_ascii=False,separators=(',',':')).encode('utf-8')
assert hashlib.sha256(packed).hexdigest()==d['certificate_sha256']
assert d['certificate_sha256']=='fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576'
hulls=c.classify()
weights,_=c.fixed_data()
all_mixed={(pair,kind) for pair,(lo,hi,kind) in hulls.items()
    if kind!='safe' and any(c.inside(w,lo,hi) for w in c.P)}
assert len(all_mixed)==187
found=set()
for i,j,s,k in rows:
    pair=(i,j)
    lo,hi,kind=hulls[pair]
    assert (pair,kind) in all_mixed and pair not in found
    assert isinstance(k,int) and 0<=k<4096 and s in (1,2)
    w=c.P[s-1]
    h=c.positive_point(lo,hi)
    assert c.inside(w,lo,hi) and c.inside(h,lo,hi)
    def point(t):
        return tuple(x+t*(y-x) for x,y in zip(w,h))
    a=point(Fraction(k,4096))
    b=point(Fraction(k+1,4096))
    assert c.admissible(a) and c.admissible(b)
    assert c.inside(a,lo,hi) and c.inside(b,lo,hi)
    assert c.direct(a,weights)<c.Q<c.direct(b,weights)
    found.add(pair)
assert found=={pair for pair,_ in all_mixed}
assert d['touch']==111 and d['cross']==76
print('C284_INDEPENDENT_EXACT_CERTIFICATE_PASS',len(found),d['certificate_sha256'])
