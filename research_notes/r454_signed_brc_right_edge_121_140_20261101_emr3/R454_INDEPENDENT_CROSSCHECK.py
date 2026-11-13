#!/usr/bin/env python3
"""Independent exact integer checks at 121<=s<=140 and three legal boundary k values.
Only tests fixed integer inputs; infinite-k conclusion rests on separate polynomial coefficient certificate.
"""
from math import comb
from hashlib import sha256
import json
from pathlib import Path

def C(m):return comb(2*m,m)//(m+1)
def choose(n,j):return comb(n,j) if 0<=j<=n else 0

def H_signed(k,s):
    r=2*k+1
    if s<2 or s>r:return 0
    d=r-s
    z=sum(comb(d,q)*(choose(2*s,r-2*q)-choose(2*s,r-2*q-1)) for q in range(d+1))
    return comb(r+s,2*s)*z

def H_catalan(k,s):
    r=2*k+1
    if s<2 or s>r:return 0
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*C(k-q) for q in range((s-1)//2+1))

def d2(seq,s):return seq[s]*seq[s]-seq[s-1]*seq[s+1]
def d3(seq,s):
    a,b,c,d,e=[seq[s+t] for t in (0,-1,1,-2,2)]
    return a*a*a-2*a*b*c+d*c*c+b*b*e-d*a*e

rows=[]; raw_checks=0;minor_checks=0;stream=sha256()
for s in range(121,141):
    k0=(s+2)//2
    for k in (k0,k0+1,k0+2):
        a={}
        for t in range(s-2,s+3):
            x=H_signed(k,t);y=H_catalan(k,t)
            assert x==y and x>0,(s,k,t)
            raw_checks+=1;a[t]=x
            stream.update(f'input:{s}:{k}:{t}:{x}\n'.encode())
        u=d2(a,s);v=d3(a,s)
        assert u>0 and v>0,(s,k,u,v)
        minor_checks+=2
        stream.update(f'minor:{s}:{k}:{u}:{v}\n'.encode())
        rows.append({'s':s,'k':k,'r':2*k+1,'D2_positive':True,'D3_positive':True})
summary={'schema':'R454_INDEPENDENT_EXACT_INTEGER_CROSSCHECK_V1','status':'PASS',
         's_range':[121,140], 'k_values':'k0,k0+1,k0+2 per s; k0=(s+2)//2',
         'raw_signed_vs_positive_Catalan_equalities':raw_checks,
         'strict_positive_direct_integer_minors':minor_checks,
         'stream_sha256':stream.hexdigest(),
         'qualifier':'Finite evaluations only; do not replace infinite-k polynomial certificate.'}
Path(__file__).with_name('R454_CROSSCHECK_EVIDENCE.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
