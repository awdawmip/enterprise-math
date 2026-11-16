#!/usr/bin/env python3
"""Independent exact validation for R418: no import of certificate generator.
Original signed branch coefficient extraction and Catalan series via different combinatorial loops.
Tests every (s,parity) at x=0,1,2 and full interpolation counts at s=31,64,128.
This is secondary checking; the symbolic construction + ALL coefficient sign test is the proof.
"""
from pathlib import Path
from math import comb
import json,hashlib
here=Path(__file__).parent
full_bytes=(here/'R418_INTERVAL_EVIDENCE.json').read_bytes()
full=json.loads(full_bytes)
manifest=json.loads((here/'R418_INTERVAL_MANIFEST.json').read_text())
assert hashlib.sha256(full_bytes).hexdigest()==manifest['full_evidence_sha256']
assert len(full['rows'])==196

def cat(n):return comb(2*n,n)//(n+1)
def raw_delta(r,q):
    # Independent coefficient extraction without sign loop in the generator:
    # (1-t) changes c_r-c_(r-1).
    top=2*q; half=r-q
    def coeff(k):
        return sum(comb(top,k-2*j)*comb(half,j) for j in range(half+1) if 0<=k-2*j<=top)
    return coeff(r)-coeff(r-1)
def kernel(r,q):
    # [z^(r-1)](1+2z)^(q-1) C(z^2)
    return sum(comb(q-1,k)*2**k*cat((r-k-1)//2)
               for k in range(q) if r-k-1>=0 and (r-k-1)%2==0)
def polyval(c,x):
    v=0
    for z in reversed(c): v=v*x+int(z)
    return v

count=kernel_count=full_deg_points=0
for data in full['rows']:
    s=data['s'];eps=data['epsilon'];r0=data['r0'];d=data['dmax'];
    a=data['A_coefficients_ascending'];b=data['B_coefficients_ascending']
    assert d==(s-1+eps)//2
    assert len(a)==len(b)==2*d+3
    assert min(map(int,a))>0 and min(map(int,b))>0
    def sha(lst):return hashlib.sha256(','.join(lst).encode()).hexdigest()
    assert sha(a)==data['A_sha256'] and sha(b)==data['B_sha256']
    x_values=range(len(a)) if s in (31,64,128) else range(3)
    if s in (31,64,128):full_deg_points+=len(a)
    for x in x_values:
        r=r0+2*x
        weighted=[]
        for q in (s-1,s,s+1):
            z=raw_delta(r,q)
            assert z==kernel(r,q),(s,eps,x,q,'Catalan mismatch')
            weighted.append(comb(r+q,2*q)*z)
            kernel_count+=1
        D=weighted[1]*weighted[1]-weighted[0]*weighted[2]
        C=cat((r-eps)//2-1+eps)
        W=comb(r+s,2*s)*C
        assert polyval(b,x)*D==polyval(a,x)*W*W, (s,eps,x,'polynomial identity mismatch')
        assert D>0
        count+=1
print('R418_INDEPENDENT_PASS', 'pairs',196,'Turan',count,'Catalan',kernel_count,'full_degree_points',full_deg_points)
