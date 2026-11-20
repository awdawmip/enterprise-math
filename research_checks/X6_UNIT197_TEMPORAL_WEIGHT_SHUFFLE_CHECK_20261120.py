#!/usr/bin/env python3
"""Unit197: exact time-slot weighted signed X6 bridge and rank obstruction.
All calculations are integer; this checks a model extension, not a native benchmark.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial
import hashlib
import json

Z = (0,)*6


def exact_static_endpoint(length, z, u, v):
    if sum(z) or length < sum(map(abs,z)) or (length-sum(map(abs,z)))%2:
        return 0
    a=[max(q,0) for q in z]; b=[max(-q,0) for q in z]
    K=(length-sum(map(abs,z)))//2
    out=0
    def recurse(i,remaining,ks):
        nonlocal out
        if i==5:
            ks=ks+[remaining]
            denominator=1; weighted=1
            for j,k in enumerate(ks):
                denominator *= factorial(a[j]+k)*factorial(b[j]+k)
                weighted *= u[j]**(a[j]+k)*v[j]**(b[j]+k)
            numerator=factorial(length)*weighted
            assert numerator%denominator==0
            out+=numerator//denominator
        else:
            for k in range(remaining+1): recurse(i+1,remaining-k,ks+[k])
    recurse(0,K,[])
    return out


def temporal_distribution(u_slots, v_slots):
    dist={Z:1}
    for U,V in zip(u_slots,v_slots):
        nxt=defaultdict(int)
        for z, mass in dist.items():
            for axis in range(6):
                p=list(z); p[axis]+=1
                m=list(z); m[axis]-=1
                nxt[tuple(p)]+=mass*U[axis]
                nxt[tuple(m)]+=mass*V[axis]
        dist=dict(nxt)
    return {z:w for z,w in dist.items() if sum(z)==0}


def shuffle_coefficient(a,b):
    T=len(a); n=T//2
    return sum(
        __import__('math').prod(a[t] if t in S else b[t] for t in range(T))
        for tup in combinations(range(T),n) for S in [set(tup)]
    )


def main():
    profiles=[
        ((1,1,1,1,1,1),(1,1,1,1,1,1)),
        ((2,3,5,7,11,13),(17,19,23,29,31,37)),
    ]
    alpha=(2,3,5,7,11,13)
    beta=(17,19,23,29,31,37)
    counts=[]
    for u,v in profiles:
        for n in range(4):
            a=alpha[:2*n]; b=beta[:2*n]
            dist=temporal_distribution([tuple(a_t*x for x in u) for a_t in a],
                                       [tuple(b_t*x for x in v) for b_t in b])
            H=shuffle_coefficient(a,b)
            for z,val in dist.items():
                static=exact_static_endpoint(2*n,z,u,v)
                assert val*comb(2*n,n)==H*static, (n,z,val,static,H)
            counts.append({'profile': 'unit' if u[0]==1 else 'nonuniform',
                           'n':n, 'balanced_endpoints':len(dist),'H':str(H)})
    u1=(1,2,1,1,1,1); u2=(2,1,1,1,1,1)
    v1=(1,1,1,1,1,1); v2=(1,1,1,2,1,1)
    M=[[u1[i]*v2[j]+u2[i]*v1[j] for j in range(6)] for i in range(6)]
    offdiag={}
    two=temporal_distribution([u1,u2],[v1,v2])
    for i in (0,1):
        for j in (2,3):
            z=[0]*6;z[i]+=1;z[j]-=1
            assert two[tuple(z)]==M[i][j]
            offdiag[f'{i+1},{j+1}']=M[i][j]
    delta=M[0][2]*M[1][3]-M[0][3]*M[1][2]
    assert delta==3
    out={
        'unit':197,
        'schema':'X6_UNIT197_TEMPORAL_SHUFFLE_EXACT_V1',
        'profiles':counts,
        'matched_endpoint_layer_pairs':sum(x['balanced_endpoints'] for x in counts),
        'violations':0,
        'source_comparison':'pinned signed_brc endpoint_weight formula, independently reimplemented',
        'counterexample':{'u_slot_1':u1,'u_slot_2':u2,'v_slot_1':v1,'v_slot_2':v2,
                          'offdiagonal_M':offdiag,'minor':delta,
                          'balanced_zero_weight':two[Z]},
        'original_R063_native_benchmark_rerun':False,
        'native_original_module_imported':False,
        'claim_status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED'
    }
    blob=(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
    print(blob.decode())
    print('SHA256',hashlib.sha256(blob).hexdigest())

if __name__=='__main__': main()
