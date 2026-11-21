#!/usr/bin/env python3
"""Exact finite checks for conditional OUTER-C12 shift/reflection edge-field theorem."""
import json
from itertools import product
from pathlib import Path

def plus(*v): return tuple(sum(x) for x in zip(*v))
def neg(v): return tuple(-x for x in v)
def mul(n,v): return tuple(n*x for x in v)
E=((1,0,0),(0,1,0),(0,0,1))
a=[E[0],E[1],E[2],neg(E[0]),neg(E[1]),neg(E[2])]
v=[x for i in range(6) for x in (a[i],plus(a[i],a[(i+1)%6]))]
def S(x): return (x[0],-x[2],-x[1])
def R(x): return (-x[2],x[0],x[1])
checks=0
for q in range(12):
    assert R(v[q])==v[(q+2)%12];checks+=1
    assert S(v[q])==v[(-q)%12];checks+=1
    edge=tuple(v[(q+1)%12][i]-v[q][i] for i in range(3))
    assert sum(abs(t) for t in edge)==1;checks+=1
    assert S(edge)==tuple(v[(-q-1)%12][i]-v[(-q)%12][i] for i in range(3));checks+=1
# For a shift-invariant field, w_{2r}=a, w_{2r+1}=b. For θ = ±id,
# reflection consistency is θ(w_q) = -w_{-q-1}.
res={}
for N in (6,12,24,48,96):
    res[str(N)]={}
    for s in (+1,-1):
        actual=set(); predicted=set(); valid=0
        for aa,bb in product(range(N),repeat=2):
            weights=[aa if q%2==0 else bb for q in range(12)]
            is_covariant=all((s*weights[q]+weights[(-q-1)%12])%N==0 for q in range(12))
            assert is_covariant == ((bb+s*aa)%N==0);checks+=1
            if not is_covariant: continue
            valid+=1
            H=sum(weights)%N
            assert H==(6*(aa+bb))%N;checks+=1
            assert H==(6*(aa-s*aa))%N;checks+=1
            assert (s*H+H)%N==0;checks+=1
            actual.add(H)
        for aa in range(N):predicted.add((6*(1-s)*aa)%N)
        assert actual==predicted;checks+=1
        res[str(N)]['theta_id' if s==1 else 'theta_neg_id']={
            'valid_fields':valid,'holonomy_set':sorted(actual),
            'holonomy_contains_6':6%N in actual
        }
        assert valid==N;checks+=1
        if N>=12: assert 6%N not in actual;checks+=1
# Independent conditional escapes: break one symmetry, keep reversibility.
for N in (12,24,48,96):
    # Macro-phase shift respected, reflection-sign covariance broken.
    shifted=[1 if q%2==0 else 0 for q in range(12)]
    assert sum(shifted)%N==6%N;checks+=1
    assert all(shifted[q]==shifted[(q+2)%12] for q in range(12));checks+=1
    assert any(shifted[q]!=shifted[(-q-1)%12] for q in range(12));checks+=1
    # Reflection-sign covariance respected, macro-shift broken.
    reflected=[3 if q in (5,6) else 0 for q in range(12)]
    assert sum(reflected)%N==6%N;checks+=1
    assert all(reflected[q]==reflected[(-q-1)%12] for q in range(12));checks+=1
    assert any(reflected[q]!=reflected[(q+2)%12] for q in range(12));checks+=1
result={'schema' :'X6_TIME_OUTER_C12_SYMMETRY_OBSTRUCTION_CHECK_V1',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model':'conditional shift-by-2 equivariant additive C12 edge-field and one reflection theta=+/-identity',
        'native_graph_vertices':v,'checks':checks,'mismatches':0,'cyclic_modulus_results':res}
path=Path(__file__).with_name('x6_c12_symmetry_holonomy_results.json')
path.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print(json.dumps({'checks':checks,'mismatches':0,'results':res},ensure_ascii=False))
