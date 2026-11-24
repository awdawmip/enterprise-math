#!/usr/bin/env python3
"""Exact R5 fixed-schedule third-rank classification verifier.

Input: frozen derived-scalar 256x101 table EXACT_R5_ALL_101_BUDGETS.json,
sha256 50e87...; integer values only. Place in the same directory or pass path.
Proof of exhaustive all-f statement is in RESEARCH.md; finite test checks the
witness/slack sets and all 32,640 pairs for each replacement triple.
"""
import hashlib, itertools, json, sys
from collections import Counter
from pathlib import Path
P = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('EXACT_R5_ALL_101_BUDGETS.json')
EXPECTED='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
data=P.read_bytes()
assert hashlib.sha256(data).hexdigest()==EXPECTED
D=json.loads(data)['counts_and_cohorts']
N={k:tuple(map(int,D[str(k)]['counts'])) for k in range(214,315)}
assert len(N)==101 and all(len(x)==256 for x in N.values())
L=25845652773852463277015040000
U=58182461585441404127941754880
PAIRS=list(itertools.combinations(range(256),2))
assert len(PAIRS)==32640
W=[((0,64),223),((1,2),1),((2,8),215),((16,32),296)]
WSETS=[set(range(223,291)), {214}|set(range(216,222)), set(range(215,222)),set(range(296,313))]
def separates(k,a,b,tau): return abs(N[k][a]-N[k][b])>tau
for ((a,b),_),expected in zip(W,WSETS):
    for tau in (L,U-1):
        assert {k for k in N if separates(k,a,b,tau)}==expected
s={k:k-sum(weight for ((a,b),weight) in W if separates(k,a,b,L)) for k in N}
assert min(s.values())==0
assert {k for k in N if s[k]==0}=={215,216,223,296}
assert {k for k in N if s[k]==1}=={217,224,297}
assert {k for k in N if s[k]==2}=={218,225,298}
BASE=(216,223,296)
# One price-two replacement; or two price-one replacements, in distinct groups.
ONE_LAYER_TWO=[(218,223,296),(216,225,296),(216,223,298),
               (217,224,296),(217,223,297),(216,224,297)]
ONE_LAYER_ONE=[(217,223,296),(216,224,296),(216,223,297)]
for tri in [BASE]+ONE_LAYER_ONE+ONE_LAYER_TWO:
    assert len(tri)==3 and all(k in N for k in tri)
    assert all(any(separates(k,a,b,U-1) for k in tri) for a,b in PAIRS),tri
assert all(sum(tri)==737 for tri in ONE_LAYER_TWO)
assert all(sum(tri)==736 for tri in ONE_LAYER_ONE)
# At t=1 there is only one triple, so only six gap-two multisets.
# At odd t>=3: additionally replace the same coordinate in two independent layers.
def classification(t):
    assert t>=1 and t%2==1
    base=Counter({216:t,223:t,296:t})
    candidates=[]
    for triple in ONE_LAYER_TWO:
        r=base.copy()
        for old,new in zip(BASE,triple):
            if old!=new:r[old]-=1;r[new]+=1
        candidates.append(r)
    if t>=3:
        for old,new in zip(BASE,(217,224,297)):
            r=base.copy();r[old]-=2;r[new]+=2;candidates.append(r)
    keys={tuple(sorted((k,v) for k,v in r.items() if v>0)) for r in candidates}
    assert len(keys)==(6 if t==1 else 9)
    for r in candidates:
        assert all(v>=0 for v in r.values())
        assert sum(k*v for k,v in r.items())==735*t+2
        # Integer full-hypothesis pairwise criterion.
        assert all(sum(v for k,v in r.items() if v>0 and separates(k,a,b,U-1))>=t for a,b in PAIRS)
    return keys
for t in (1,3,5,17):classification(t)
print('PASS_R5_FIXED_COST_GAP2_ALL_F')
print('frozen_sha256',EXPECTED,'budgets',len(N),'pairs',len(PAIRS))
print('dual_zero',sorted(k for k in s if s[k]==0))
print('dual_one',sorted(k for k in s if s[k]==1))
print('dual_two',sorted(k for k in s if s[k]==2))
print('gap_two_one_layer_triples',ONE_LAYER_TWO)
print('number_gap_two_multisets_f0',len(classification(1)))
print('number_gap_two_multisets_fge1',len(classification(3)))
print('exact_rank_values','735t','735t+1','735t+2','t=2f+1')
