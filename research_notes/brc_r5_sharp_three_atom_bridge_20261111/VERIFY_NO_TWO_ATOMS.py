#!/usr/bin/env python3
"""Exact Farkas check for 144 A->B two-atom candidate families.
Run alongside VERIFY_BRIDGES.py and FARKAS_CERTS.b85.
Only Python standard library; observer and certificates exact.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import base64,zlib,json
from VERIFY_BRIDGES import R,OBS,b,V,idx

JA=frozenset((1,3,4,6))
N=28
def atom(other,targets,positive_target):
    assert other in (1,2,5)
    i,j,k=sorted(targets)
    v={i:R[j]-R[k],j:R[k]-R[i],k:R[i]-R[j]}
    assert positive_target in v and v[positive_target]!=0
    if v[positive_target]<0:v={i:-x for i,x in v.items()}
    h=[0]*N
    for i,x in v.items():
        h[idx[(i,3)]]=x
        h[idx[(i,other)]]=-x
    assert all(sum(a*z for a,z in zip(row,h))==0 for row in OBS)
    return h
def all_cases():
    for first in (2,5):
        other=5 if first==2 else 2
        for pair in combinations(sorted(JA),2):
            for j in (1,2,5):
                for k in (1,2,5):
                    yield (f'OLD:{first}:{pair[0]}{pair[1]}:{j}{k}',
                           atom(j,(first,)+pair,first),atom(k,(other,1,6),other))
    for u in (3,4):
        for j in (1,2,5):
            for k in (1,2,5):
                yield (f'DOUBLE:{u}:{j}{k}',
                       atom(j,(2,5,u),2),atom(k,(1,6,u),u))
    for first in (2,5):
        other=5 if first==2 else 2
        for j in (1,2,5):
            for k in (1,2,5):
                yield (f'TRANSIENT:{first}:{j}{k}',
                       atom(j,(0,1,first),first),atom(k,(0,other,6),other))
def matrix(h1,h2):
    # Nonnegative z=(25 initial allowed masses, t1,t2, 28 W slacks, 28 Y slacks).
    allowed=[k for k,(i,source) in enumerate(V) if source!=3 or i in JA]
    count=len(allowed)
    n=count+2+28+28
    B=[[0]*n for _ in range(15+28+28+3)]
    d=b+[F(0)]*(len(B)-len(b))
    for p,k in enumerate(allowed):
        for r in range(15):B[r][p]=OBS[r][k]
        B[15+k][p]=1
        B[15+28+k][p]=1
    for k in range(28):
        B[15+k][count]=h1[k]
        B[15+k][count+2+k]=-1
        B[15+28+k][count]=h1[k]
        B[15+28+k][count+1]=h2[k]
        B[15+28+k][count+2+28+k]=-1
    for r,i in enumerate((0,1,6)):
        B[15+56+r][count+2+28+idx[(i,3)]]=1
    return B,d
def main():
    encoded=Path(__file__).with_name('FARKAS_CERTS.b85').read_text(encoding='ascii')
    raw=zlib.decompress(base64.b85decode(''.join(encoded.split()).encode('ascii')))
    certs=json.loads(raw)
    cases=list(all_cases())
    assert len(cases)==144 and len(certs)==144
    seen=set();sizes=[]
    for name,h1,h2 in cases:
        assert name in certs and name not in seen
        seen.add(name)
        B,d=matrix(h1,h2)
        y=[0]*len(B)
        for r,val in certs[name]:
            assert 0<=r<len(B) and isinstance(val,int)
            y[r]=val
        for k in range(len(B[0])):
            assert sum(row[k]*yi for row,yi in zip(B,y))>=0,(name,k)
        gap=sum(yi*rhs for yi,rhs in zip(y,d))
        assert gap<0,(name,gap)
        sizes.append(sum(z!=0 for z in y))
    assert seen==set(certs)
    print('SOURCE_FROZEN_7_RATIOS',R)
    print('EXACT_FARKAS_CERTIFICATE_CASES',len(cases))
    print('SPLIT_CASE_COUNTS','OLD=108 DOUBLE=18 TRANSIENT=18')
    print('MAX_CERTIFICATE_NONZERO_ENTRIES',max(sizes))
    print('LARGEST_INTEGER_COEFFICIENT',max(abs(v) for cert in certs.values() for _,v in cert))
    print('ALL_B_TRANSPOSE_Y_NONNEGATIVE_AND_DOT_B_NEGATIVE',True)
    print('A_TO_B_TWO_ATOM_PATHS_EXCLUDED',True)
    print('A_TO_B_ATOMIC_MINIMUM_WITH_SOURCE3_PEAK_5',3)
    print('PASS_R5_EXACT_144_TWO_ATOM_FARKAS_CERTIFICATES')
if __name__=='__main__':main()
