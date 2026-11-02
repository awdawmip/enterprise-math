#!/usr/bin/env python3
"""R472 independent exact adjacent-minor PF3 certificates, signed BRC auxiliary scalar.
The mathematical reduction to PF3 is proved separately in R450_PROOF.zh-CN.md.
Only Python integers are used for all coefficients and determinant signs.
"""
from math import comb
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter

START, END = 265, 271

def catalan(k):
    return comb(2*k, k)//(k+1)

def row(r):
    assert r%2==1 and r>=5
    k=(r-1)//2
    cats=[catalan(j) for j in range(k+1)]
    # R441 positive Catalan representation, 2<=s<=r.
    return [comb(r+s,2*s)*sum(comb(s-1,2*q)*(4**q)*cats[k-q]
            for q in range(min(k,(s-1)//2)+1))
            for s in range(r,1,-1)]

def coefficient_raw(r,s):
    h=r-s
    return comb(r+s,2*s)*sum(comb(h,q)*(
        (comb(2*s,r-2*q) if 0<=r-2*q<=2*s else 0)
        -(comb(2*s,r-2*q-1) if 0<=r-2*q-1<=2*s else 0))
        for q in range(h+1))

def coefficient_alternating(r,s):
    h=r-s
    return comb(2*r-h,h)*sum(comb(h,q)*(-2)**q*catalan(r-q)
                                  for q in range(h+1))

def calc2(a,j):
    return a[j]*a[j] - (a[j-1] if j else 0)*(a[j+1] if j+1<len(a) else 0)

def calc3(a,j):
    def z(h):return a[h] if 0<=h<len(a) else 0
    x,y,z2=z(j),z(j+1),z(j+2)
    u,v,w=z(j-1),z(j),z(j+1)
    p,q,t=z(j-2),z(j-1),z(j)
    return x*(v*t-w*q)-y*(u*t-w*p)+z2*(u*q-v*p)

def put_number(dig,n):
    # Length-prefixed, unambiguous unsigned canonical binary integer stream.
    assert n>=0
    bb=n.to_bytes(max(1,(n.bit_length()+7)//8),'big')
    dig.update(len(bb).to_bytes(4,'big'))
    dig.update(bb)

raw_checks=0
alt_checks=0
positive_count=0
pair_count=0
triple_count=0
row_stats=[]
coefficient_sha=sha256()
minor_sha=sha256()
start=perf_counter()
for r in range(START,END+1,2):
    a=row(r)
    assert len(a)==r-1
    for h,v in enumerate(a):
        if v<=0:raise AssertionError(('negative coefficient',r,h,v))
        put_number(coefficient_sha,v)
        positive_count+=1
    # Every admissible shift j=0,...,r-2 including boundary zero padding.
    for j in range(r-1):
        p2=calc2(a,j)
        p3=calc3(a,j)
        if p2<=0:raise AssertionError(('negative 2x2',r,j,p2))
        if p3<=0:raise AssertionError(('negative 3x3',r,j,p3))
        put_number(minor_sha,p2)
        put_number(minor_sha,p3)
        pair_count+=1
        triple_count+=1
    if r in (265,267,269,271):
        for s in sorted(set([2,3,4,(r+1)//2,r-3,r-2,r-1,r])):
            expected=a[r-s]
            assert expected==coefficient_raw(r,s),(r,s,'raw')
            raw_checks+=1
            assert expected==coefficient_alternating(r,s),(r,s,'alt')
            alt_checks+=1
    row_stats.append({'r':r,'positive_coefficients':r-1,
                      'positive_adjacent_2x2':r-1,
                      'positive_adjacent_3x3':r-1,
                      'maximum_coefficient_bits':max(t.bit_length() for t in a)})

assert (positive_count,pair_count,triple_count)==(1068,1068,1068)
assert (raw_checks,alt_checks)==(32,32)
result={
 'schema':'R472_SIGNED_BRC_PF3_LOCAL_CERTIFICATE_V1',
 'checked_odd_r_from':START,'checked_odd_r_to':END,'rows':len(row_stats),
 'support_definition':'a_h=H(r,r-h) for 0<=h<=r-2; zero otherwise',
 'coefficient_count_strictly_positive':positive_count,
 'adjacent_2x2_count_strictly_positive':pair_count,
 'adjacent_3x3_count_strictly_positive':triple_count,
 'total_exact_integer_sign_checks':positive_count+pair_count+triple_count,
 'independent_signed_raw_checks':raw_checks,
 'independent_alternating_catalan_checks':alt_checks,
 'exact_arithmetic':'Python integer arithmetic; all signs exact',
 'coefficient_stream_sha256':coefficient_sha.hexdigest(),
 'adjacent_minor_stream_sha256':minor_sha.hexdigest(),
 'stream_encoding':'sequential 4-byte big-endian length followed by big-endian unsigned integer, each r then j ascending; adjacent minor stream D2,D3 interleaved',
 'proof_route':'strict positivity of adjacent 2x2 and 3x3 -> all contiguous-row minors by projective convexity -> all minors by R441-A Schur/Littlewood-Richardson',
 'scope':'four odd r, 265 through 271; full finite-support local minors; projective-convexity criterion in R450 needed for half-infinite PF3',
 'status':'AUTHOR_SIDE_EXACT_INTEGER_AND_ANALYTIC; DRIVER_UNREVIEWED; NOT_ADMITTED; REGISTER_PENDING',
 'row_statistics':row_stats,
}
Path('R472_ROW_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('R472_ROW_EXACT_PASS',json.dumps({k:v for k,v in result.items() if k!='row_statistics'},ensure_ascii=False,sort_keys=True))
print('elapsed_seconds',round(perf_counter()-start,2))
