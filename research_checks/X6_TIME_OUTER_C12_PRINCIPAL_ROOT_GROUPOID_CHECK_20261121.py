#!/usr/bin/env python3
"""Independent exact check of the conditional native OUTER C12 groupoid transport."""
from itertools import product
from math import gcd
from pathlib import Path
import json

def carry(q,k):
    assert 0<=q<12
    return 3*((q+k)//6-q//6)

def local(q,d):
    assert d in (-1,1)
    return carry(q,d)

def walk(q,ds):
    total=0
    p=q
    for d in ds:
        total+=local(p,d)
        p=(p+d)%12
    return p,total

checks=0
for q in range(12):
    for k in range(-36,37):
        for ell in range(-18,19):
            assert carry(q,k+ell)==carry(q,k)+carry((q+k)%12,ell)
            checks+=1
    for k in (-24,-12,-6,6,12,24):
        if k%6==0:
            assert carry(q,k)==k//2
            checks+=1
    for depth in range(0,7):
        modulus=6*(2**depth)
        holonomy_order=(modulus//gcd(modulus,6))
        assert holonomy_order==2**depth
        assert len({(6*w)%modulus for w in range(holonomy_order)})==holonomy_order
        assert (6*holonomy_order)%modulus==0
        checks+=3

walk_checks=0
for length in range(9):
    for ds in product((-1,1), repeat=length):
        k=sum(ds)
        for q in range(12):
            p,total=walk(q,ds)
            assert p==(q+k)%12
            assert total==carry(q,k)
            walk_checks+=1

# Any phase gauge h(q) with even q endpoints h(q)=h(q+6) respects
# the actual native Cell-start oriented half-turn source constraints.
h=[0,5,0,-2,0,11,0,7,0,3,0,-4]
old=[carry(q,1) for q in range(12)]
new=[old[q]+h[(q+1)%12]-h[q] for q in range(12)]
assert old!=new
for q in range(0,12,2):
    assert sum(new[(q+j)%12] for j in range(6))==3
    assert sum(old[(q+j)%12] for j in range(6))==3
assert sum(new)==sum(old)==6
checks+=2*6+1

# Mod C6: no homogeneous one-step increment can yield half-turn root 3.
for a in range(6):
    assert 6*a%6!=3
    checks+=1

report={
    'schema':'X6_TIME_C12_GROUPOID_ROOT_TRANSPORT_CHECK_V1',
    'scope':'conditional principal-root transport along frozen OUTER C12 native microcycle; NOT accepted global physical precision dynamics',
    'frozen_source_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'cocycle_equation_checks':12*73*37,
    'signed_microstep_walk_checks':walk_checks,
    'other_exact_checks':checks-12*73*37,
    'total_checks':checks+walk_checks,
    'mismatches':0,
    'principal_forward_half_turn':3,
    'principal_reverse_half_turn':-3,
    'full_cycle_holonomy':6,
    'canonical_forward_edge_weights':old,
    'alternate_source_compatible_edge_weights':new,
    'modular_winding_distinctions':{str(m):2**m for m in range(7)},
    'source_cell_starts':[0,2,4,6,8,10]
}
print(json.dumps(report,ensure_ascii=False,indent=2))
with Path(__file__).with_name('groupoid_cocycle_results.json').open('w',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2,sort_keys=True)
