"""Exact X6 Unit159 frozen derived-carrier finite difference checker."""
from collections import defaultdict
from itertools import product
from math import gcd, factorial
import json

WEIGHTS = ((1,2),(2,1),(1,3),(3,1),(2,3),(3,2),(1,5),(5,1),(-1,2),(2,-1))

def directions(seed):
    a,b,c = seed
    return ((a-c,b-c),(c-b,a-b),(b-a,c-a))

def trace_cube(seed):
    ds = directions(seed)
    out = []
    for mask in product((0,1),repeat=3):
        p = tuple(sum(mask[j]*ds[j][i] for j in range(3)) for i in range(2))
        out.append((mask,p,(-1)**(3-sum(mask))))
    return out

def kernel(seed):
    coeffs = defaultdict(int)
    for _,p,sgn in trace_cube(seed):
        coeffs[p] += sgn
    return {p:v for p,v in coeffs.items() if v}

def convolve(a,b):
    coeffs = defaultdict(int)
    for x,cx in a.items():
        for y,cy in b.items():
            coeffs[(x[0]+y[0],x[1]+y[1])] += cx*cy
    return {p:v for p,v in coeffs.items() if v}

def first_exposed(k):
    for q in WEIGHTS:
        scores = {p:q[0]*p[0]+q[1]*p[1] for p in k}
        maximum = max(scores.values())
        maxima = [p for p,v in scores.items() if v==maximum]
        if len(maxima)==1:
            p = maxima[0]
            return q,p,k[p]
    return None

def check():
    total = 0
    for a,b,c in product(range(9),repeat=3):
        seed=(a,b,c)
        if min(seed)!=0 or max(seed)==0 or gcd(abs(a-c),abs(b-c))!=1:
            continue
        ds=directions(seed)
        if sum(x for x,_ in ds)!=0 or sum(y for _,y in ds)!=0 or (0,0) in ds or len(set(ds))!=3:
            raise AssertionError(("frame",seed))
        entries=trace_cube(seed)
        k=kernel(seed)
        zeros=[p for _,p,_ in entries if p==(0,0)]
        if len(entries)!=8 or len(zeros)!=2 or len(k)!=6 or sum(k.values())!=0:
            raise AssertionError(("trace",seed))
        if sum(abs(v) for v in k.values())!=6 or any(abs(v)!=1 for v in k.values()):
            raise AssertionError(("coefficient",seed))
        total+=1
    k1=kernel((1,0,0))
    k2=kernel((2,1,0))
    k12=convolve(k1,k2)
    exposed=first_exposed(k12)
    if exposed!=((1,2),(2,3),1) or len(k12)!=12 or sum(k12.values())!=0:
        raise AssertionError(("exposed",exposed))
    z=(0,0,0,0,0,0)
    d=(1,1,1,0,0,0)
    carrier=lambda v:(v[0]-v[2],v[1]-v[2])
    b1=factorial(sum(abs(x) for x in d))
    for x in d:
        b1//=factorial(abs(x))
    if carrier(z)!=carrier(d) or sum(x*x for x in z)!=0 or sum(x*x for x in d)!=3 or b1!=6:
        raise AssertionError("native common-depth witness")
    return {
       "schema":"X6_UNIT159_EXACT_CHECK_V1",
       "frozen_comparison_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
       "primitive_minzero_seed_range":"0..8 each coordinate, gcd primitive",
       "enumerated_frame_count":total,
       "all_eight_trace_vs_six_signed_endpoints_verified":True,
       "convolution_family":{"seed_pair":[[1,0,0],[2,1,0]],"nonzero_kernel_positions":len(k12),"coefficient_sum":sum(k12.values()),"first_exposing_q":list(exposed[0]),"exposed_point":list(exposed[1]),"exposed_coefficient":exposed[2]},
       "x6_native_hidden_depth_pair":{"carrier":[0,0],"G":[0,3],"N":[0,3],"positive_N_BRC":[1,b1]},
       "classification":"SIGNED_Z2_FINITE_DIFFERENCE_NOT_POSITIVE_X6_N_BRC; EXPOSED_KERNEL_VERTEX_NOT_NATIVE_AXIS_ARGMAX",
       "status":"PASS"
    }

if __name__=="__main__":
    print(json.dumps(check(),ensure_ascii=False,sort_keys=True,separators=(",",":")))
