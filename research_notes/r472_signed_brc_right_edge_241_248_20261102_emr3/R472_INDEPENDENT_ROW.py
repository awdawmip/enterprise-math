#!/usr/bin/env python3
"""Exact independent Catalan/raw finite-row signed BRC minor checks for r=265,267,269,271."""
from math import comb
import json
from hashlib import sha256

def cat(n): return comb(2*n,n)//(n+1)
def pos(r,s):
    k=(r-1)//2
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*cat(k-q) for q in range(min(k,(s-1)//2)+1))
def raw(r,s):
    h=r-s
    def c(n,i):return comb(n,i) if 0<=i<=n else 0
    return comb(r+s,2*s)*sum(comb(h,q)*(c(2*s,r-2*q)-c(2*s,r-2*q-1)) for q in range(h+1))
def alt(r,s):
    h=r-s
    return comb(2*r-h,h)*sum(comb(h,q)*(-2)**q*cat(r-q) for q in range(h+1))
def pack(sha,n):
    assert n>0
    b=n.to_bytes(max(1,(n.bit_length()+7)//8),'big')
    sha.update(len(b).to_bytes(4,'big'));sha.update(b)

ca, mi=sha256(),sha256()
stats=[]
for r in (265,267,269,271):
    a=[pos(r,s) for s in range(r,1,-1)]
    def z(j):return a[j] if 0<=j<len(a) else 0
    for j in range(r-1):
        A=z(j);B=z(j-1);C=z(j+1);D=z(j-2);E=z(j+2)
        p2=A*A-B*C
        p3=A**3-2*A*B*C+D*C*C+B*B*E-D*A*E
        assert A>0 and p2>0 and p3>0,(r,j)
        pack(ca,A);pack(mi,p2);pack(mi,p3)
    for s in sorted(set((2,3,4,(r+1)//2,r-3,r-2,r-1,r))):
        assert pos(r,s)==raw(r,s)==alt(r,s),(r,s)
    stats.append({'r':r,'strict_positive_each_of_a_D2_D3':r-1})
result={'schema':'R472_SIGNED_BRC_ROW_INTEGER_CERT_V1','status':'AUTHOR_EXACT_PASS',
        'rows':stats,'per_quantity_positive_counts':1068,'total_integer_positive_signs':3204,
        'raw_crosschecks':32,'alternating_catalan_crosschecks':32,
        'a_stream_sha256':ca.hexdigest(),'D2_D3_stream_sha256':mi.hexdigest(),
        'scope':'r=265,267,269,271 finite row; further PF3 inference conditional on R450'}
with open('R472_INDEPENDENT_ROW_EVIDENCE.json','w') as f:json.dump(result,f,indent=2)
print('R472_ROW_PASS',json.dumps(result,sort_keys=True))
