#!/usr/bin/env python3
"""PREFIX-792 exact integer regression: binary three-factor pairwise marginals.
Requires only the Python standard library. No floating-point arithmetic.
"""
from itertools import product
from collections import defaultdict
import json

CELLS = list(product(range(2), repeat=3))

def marginals(cube):
    p = (cube[0]+cube[1], cube[2]+cube[3], cube[4]+cube[5], cube[6]+cube[7])
    q = (cube[0]+cube[2], cube[1]+cube[3], cube[4]+cube[6], cube[5]+cube[7])
    r = (cube[0]+cube[4], cube[1]+cube[5], cube[2]+cube[6], cube[3]+cube[7])
    return p, q, r

def one_way_consistent(p,q,r):
    return (p[0]+p[1]==q[0]+q[1] and
            p[2]+p[3]==q[2]+q[3] and
            p[0]+p[2]==r[0]+r[1] and
            p[1]+p[3]==r[2]+r[3] and
            q[0]+q[2]==r[0]+r[2] and
            q[1]+q[3]==r[1]+r[3])

def bounds(p,q,r):
    return (max(0, q[0]-p[1], r[0]-p[2], r[0]-q[2]),
            min(p[0],q[0],r[0], p[3]-q[2]+r[0]))

def reconstruct(p,q,r,x):
    return (x,p[0]-x,q[0]-x,p[1]-q[0]+x,
            r[0]-x,p[2]-r[0]+x,q[2]-r[0]+x,
            p[3]-q[2]+r[0]-x)

def crt2_3_5(a,b,c):
    return next(n for n in range(30) if n%2==a and n%3==b and n%5==c)

def tables(total):
    # all 2x2 nonnegative integer tables summing to total
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield (a,b,c,total-a-b-c)

def main():
    checks=0
    groups=defaultdict(set)
    cubes=0
    maxN=6
    for entries in product(range(maxN+1),repeat=8):
        n=sum(entries)
        if n>maxN: continue
        cubes+=1
        p,q,r=marginals(entries)
        assert one_way_consistent(p,q,r); checks+=1
        lo,hi=bounds(p,q,r)
        assert lo<=entries[0]<=hi; checks+=1
        assert reconstruct(p,q,r,entries[0])==entries;checks+=1
        groups[(p,q,r)].add(entries[0])
    for (p,q,r),xs in groups.items():
        lo,hi=bounds(p,q,r)
        assert xs==set(range(lo,hi+1)); checks+=1
        for x in range(lo,hi+1):
            cube=reconstruct(p,q,r,x)
            assert min(cube)>=0 and marginals(cube)==(p,q,r);checks+=1
    # all one-way consistent 3 pairwise tables for N<=4: interval iff feasible
    consistent=feasible=infeasible=0
    for n in range(5):
        t=list(tables(n))
        for p in t:
            for q in t:
                if (p[0]+p[1],p[2]+p[3])!=(q[0]+q[1],q[2]+q[3]): continue
                for r in t:
                    if not one_way_consistent(p,q,r): continue
                    consistent+=1
                    lo,hi=bounds(p,q,r)
                    exists=(p,q,r) in groups
                    assert exists==(lo<=hi);checks+=1
                    if exists: feasible+=1
                    else: infeasible+=1
    # compatible pair margins not jointly realizable (A=B, A=C, B!=C)
    p=(1,0,0,1);q=(1,0,0,1);r=(0,1,1,0)
    assert one_way_consistent(p,q,r) and bounds(p,q,r)==(1,0);checks+=1
    # even / odd parity have identical 2-coordinate marginals but target count differs
    even=tuple(int((a+b+c)%2==0) for a,b,c in CELLS)
    odd=tuple(int((a+b+c)%2==1) for a,b,c in CELLS)
    assert marginals(even)==marginals(odd);checks+=1
    assert bounds(*marginals(even))==(0,1) and even[0]==1 and odd[0]==0; checks+=1
    assert len({crt2_3_5(*x) for x in CELLS})==8;checks+=1
    result=dict(status='ALL_CHECKS_PASS PREFIX792 BINARY_PAIRWISE_CRT_FIBER',
                exhaustive_total_paths_max=maxN,exhaustive_cubes=cubes,
                distinct_pairwise_margin_fibers=len(groups),
                one_way_consistent_marginal_triples_total_le_4=consistent,
                feasible_marginal_triples_total_le_4=feasible,
                incompatible_marginal_triples_total_le_4=infeasible,
                assertion_count=checks,
                parity_example={'even_target_count':even[0],'odd_target_count':odd[0],
                                'same_marginal_target_interval':list(bounds(*marginals(even)))},
                contradictory_cycle_interval=[1,0],
                method='Exact integer exhaustive enumeration, no floating-point operations')
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return result

if __name__=='__main__': main()
