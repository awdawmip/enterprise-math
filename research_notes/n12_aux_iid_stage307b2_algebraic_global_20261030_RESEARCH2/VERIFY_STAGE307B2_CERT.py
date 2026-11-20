#!/usr/bin/env python3
"""Independent exact check of regenerated Stage307-B.2 dyadic path certificate."""
from fractions import Fraction as Q
from math import comb
import json
D=json.load(open('CERT_STAGE307B2.json',encoding='utf8'))
bases=((Q(0),Q(23,100),Q(0),Q(1)),(Q(24,100),Q(1),Q(0),Q(1)),
 (Q(23,100),Q(24,100),Q(0),Q(55,100)),
 (Q(23,100),Q(24,100),Q(56,100),Q(1)))
assert D['schema']=='EM_STAGE307B2_RATIONAL_EXTERIOR_COVER_V1'
assert D['base_rectangles']==[[str(v) for v in row] for row in bases]
U=Q(15116534475889766921898005231381567,1250000000000000000000000000000000000)
assert Q(D['strict_lower_bound_threshold'])==U
def b(k,z): return z**k*(1-z)**(3-k)
def rng(k,a,c):
    vals=[b(k,a),b(k,c)]
    if k in (1,2) and a<=Q(k,3)<=c:vals.append(b(k,Q(k,3)))
    return min(vals),max(vals)
def split(rect,bit):
    a,c,d,e=rect
    if c-a>=e-d:
        m=(a+c)/2
        return (a,m,d,e) if bit=='0' else (m,c,d,e)
    m=(d+e)/2
    return (a,c,d,m) if bit=='0' else (a,c,m,e)
def lower(rect):
    a,c,d,e=rect
    p=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
    total=Q(0)
    for k in range(4):
        lo1,hi1=rng(k,a,c);lo2,hi2=rng(k,d,e)
        lo=Q(4,5)*lo1+Q(1,5)*lo2-p[k]
        hi=Q(4,5)*hi1+Q(1,5)*hi2-p[k]
        v=lo if lo>0 else (-hi if hi<0 else Q(0))
        total+=Q(comb(3,k),2)*v
    return total
for j,paths in enumerate(D['leaf_paths']):
    s=set(paths)
    assert len(s)==len(paths) and all(set(z)<=set('01') for z in s)
    assert sum((Q(1,2**len(z)) for z in s),Q(0))==1
    for z in s:
        assert all(z[:i] not in s for i in range(len(z)))
        rect=bases[j]
        for bit in z: rect=split(rect,bit)
        assert lower(rect)>U
    print('REGION_COVER_VERIFIED',j,len(s))
print('STAGE307B2_INDEPENDENT_EXTERIOR_CERT_PASS')
