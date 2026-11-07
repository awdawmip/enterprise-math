"""R433 finite PF4 certificate for signed BRC auxiliary model at r=17.

No claim of native X6 correspondence or independent formal admission.
The C++ 4x4 engine may be run separately after compiling R433_FULL_PF4.cpp.
"""
from __future__ import annotations
from math import comb, gcd
from functools import reduce
import json, itertools, pathlib

R=17
N=R-2
HERE=pathlib.Path(__file__).resolve().parent

def coefficient(q, r, s):
    return sum(comb(2*s,q-2*j)*comb(r-s,j) for j in range(r-s+1) if 0 <= q-2*j <= 2*s)

def original_H(r,s):
    return comb(r+s,2*s)*(coefficient(r,r,s)-coefficient(r-1,r,s)) if 2 <= s <=r else 0

def cat(n):
    return comb(2*n,n)//(n+1) if n>=0 else 0

def catalan_H(r,s):
    if not 2<=s<=r:return 0
    k=r//2
    if r%2:
        d=sum(comb(s-1,2*t)*2**(2*t)*cat(k-t) for t in range((s-1)//2+1))
    else:
        d=sum(comb(s-1,2*t+1)*2**(2*t+1)*cat(k-1-t) for t in range((s-2)//2+1))
    return comb(r+s,2*s)*d

def at(a,j):
    return a[j] if 0<=j<len(a) else 0

def determinant(m):
    """Independent exact Leibniz formula, used for h<=3 and 4x4 spot checks."""
    h=len(m)
    t=0
    for p in itertools.permutations(range(h)):
        s=1
        for i in range(h):s *=m[i][p[i]]
        for i in range(h):
            for j in range(i+1,h):
                if p[i]>p[j]:s=-s
        t+=s
    return t

def minors(a,h):
    """All indecomposable sorted-matchable minors under finite support lemma."""
    n=len(a)-1
    if h==1:
        for j in range(n+1):
            yield (0,), (j,),a[j]
        return
    def row_grow(r):
        if len(r)==h:
            yield tuple(r);return
        for d in range(1,n+1):
            yield from row_grow(r+[r[-1]+d])
    def col_grow(rows,cols):
        j=len(cols)
        if j==h:
            M=[[at(a,cols[v]-rows[u]) for v in range(h)] for u in range(h)]
            yield tuple(cols),determinant(M)
            return
        start=max(rows[j],cols[-1]+1 if cols else 0)
        for c in range(start,rows[j]+n+1):
            yield from col_grow(rows,cols+[c])
    for rows in row_grow([0]):
        for cols,d in col_grow(rows,[]):
            yield rows,cols,d

A=[original_H(R,R-h) for h in range(N+1)]
assert all(A[h]==catalan_H(R,R-h) for h in range(N+1))
assert all(v>0 for v in A)
g=reduce(gcd,A)
A0=[v//g for v in A]
for i in range(N+1):
    assert original_H(R,R-i)==g*A0[i]
counts={}
for h in (1,2,3):
    npos=nzero=nneg=0
    firstneg=None
    for rows,cols,d in minors(A0,h):
        npos+=(d>0);nzero+=(d==0);nneg+=(d<0)
        if d<0 and firstneg is None:firstneg=[rows,cols,str(d)]
    counts[str(h)]={'positive':npos,'zero':nzero,'negative':nneg,'total':npos+nzero+nneg,'first_negative':firstneg}
print('R433_R17_LOWER_EXACT',json.dumps(counts,separators=(',',':')),flush=True)
assert all(counts[str(i)]['negative']==0 and counts[str(i)]['zero']==0 for i in (1,2,3))

spot_count=0
for gaps in itertools.product([1,2,3,4],repeat=3):
    rows=(0,gaps[0],gaps[0]+gaps[1],sum(gaps))
    for offsets in [(0,1,2,3),(1,3,5,7),(2,4,6,8),(5,7,9,11),(11,12,13,14),(12,14,15,16),(14,15,16,17)]:
        if max(offsets)>N:continue
        cols=tuple(x+rows[i] for i,x in enumerate(offsets))
        if not all(cols[i]<cols[i+1] for i in range(3)):continue
        d=determinant([[at(A0,cols[v]-rows[u]) for v in range(4)]for u in range(4)])
        assert d>0,(rows,cols,d)
        spot_count+=1

a4=[original_H(4,4-h) for h in range(3)]
assert determinant([[at(a4,1+j-i) for j in range(3)]for i in range(3)])==-1568
a6=[original_H(6,6-h) for h in range(5)]
assert determinant([[at(a6,c-i) for c in (1,4,5,6)]for i in (0,1,2,3)])==-4117994496

m=max(A0)
assert 6*m**3 < 2**127 and 24*m**4 < 2**255

result={'model':'signed_BRC_auxiliary_scalar','r':R,'n':N,'gcd':str(g),
        'a_unscaled_decimal':[str(v) for v in A],
        'a_normalized_decimal':[str(v) for v in A0],
        'coefficient_checks':N+1,'minors_h1_h2_h3':counts,
        'independent_positive_4x4_spots':spot_count,
        'negative_control_r4_3x3':-1568,
        'negative_control_r6_4x4':-4117994496,
        'bound_i128_3x3_bits':(6*m**3).bit_length(),
        'bound_int256_4x4_bits':(24*m**4).bit_length(),
        'numeric_semantics':'all integer, no floats',
        'coverage':'all indecomposable sorted-matchable minors of order <=3; separate C++ exhaustive order4',
        'status':'AUTHOR_SIDE_EXACT, UNREVIEWED, NOT_ADMITTED'}
path=HERE/'R433_LOWER_EVIDENCE.json'
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('R433_EXACT_LOWER_PASS',sum(z['total'] for z in counts.values()),'spot',spot_count,'gcd',g,flush=True)
