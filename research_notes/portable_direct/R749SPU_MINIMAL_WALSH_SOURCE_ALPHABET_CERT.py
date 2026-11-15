#!/usr/bin/env python3
"""Exact lattice certificate: two and three source sums for R749SPR K.
No external modules, floating point, symbolic approximations, or network.
R749SPT's unimodular-triangulation theorem supplies the universal IDP premise.
"""
from itertools import product, combinations_with_replacement
from collections import Counter, defaultdict
import json

FACETS = (
    ((-1,-1,-1),-2), ((-1,-1,1),-2),
    ((-1,1,-1),-2), ((-1,1,1),-2),
    ((1,-1,-1),-2), ((1,-1,1),-4),
    ((1,1,-1),-4), ((1,1,1),-2),
)

def dot(a, b):
    return sum(x*y for x, y in zip(a,b))

def within(x, n=1):
    return all(dot(normal,x) >= n*offset for normal,offset in FACETS)

def points(n):
    # All K coordinates are between -2 and 2; scaled coordinate bounds are exact.
    return {x for x in product(range(-2*n,2*n+1), repeat=3) if within(x,n)}

def multisets(A,n):
    F = defaultdict(list)
    for ids in combinations_with_replacement(A,n):
        x = tuple(sum(a[k] for a in ids) for k in range(3))
        F[x].append(ids)
    return F

P = tuple(sorted(points(1)))
assert len(P) == 33
full2 = multisets(P,2)
full3 = multisets(P,3)
K2, K3 = points(2), points(3)
assert len(full2)==len(K2)==179 and set(full2)==K2
assert len(full3)==len(K3)==531 and set(full3)==K3
assert sum(map(len,full2.values()))==561

unique2 = {x: reps[0] for x,reps in full2.items() if len(reps)==1}
forced = frozenset(a for rep in unique2.values() for a in rep)
optional = frozenset(P)-forced
assert len(unique2)==46 and len(forced)==25 and len(optional)==8
F2 = multisets(sorted(forced),2)
holes2 = sorted(K2 - set(F2))
assert holes2 == [(-2,-1,1),(-2,1,-1)]

# Each 26-type alphabet containing the 25 forced types adds just one optional type.
minima=[]
for added in sorted(optional):
    A=tuple(sorted(forced|{added}))
    F2A=multisets(A,2)
    if set(F2A) != K2:
        continue
    F3A=multisets(A,3)
    assert set(F3A)==K3, ('3K hole',added,sorted(K3-set(F3A)))
    assert len(F2A)==179 and len(F3A)==531
    minima.append((added,A,F2A,F3A))
assert sorted(x[0] for x in minima)==[(-1,0,0),(0,0,0)]

# Direct finite evidence independent of the inherited all-n IDP proof.
# In fact, any candidate with <26 letters misses at least one 2K point:
# 46 unique pair-sums force all 25 members of forced; those alone miss two sums.
assert all(any(y not in forced for rep in full2[h] for y in rep) for h in holes2)

results=[]
for added,A,F2A,F3A in minima:
    c2=Counter(map(len,F2A.values()))
    c3=Counter(map(len,F3A.values()))
    results.append({
        'extra_source':list(added),
        'alphabet': [list(p) for p in A],
        'sum2_distinct':len(F2A),
        'sum3_distinct':len(F3A),
        'sum2_unordered_multisets':sum(map(len,F2A.values())),
        'sum3_unordered_multisets':sum(map(len,F3A.values())),
        'sum2_max_provenance_fiber':max(c2),
        'sum3_max_provenance_fiber':max(c3),
        'sum2_unique_readouts':c2[1],
        'sum3_unique_readouts':c3[1],
    })

out={
    'status':'PASS',
    'unit':'R749SPU',
    'model':'frozen auxiliary signed 16-atom Walsh source fiber; R749SPR K',
    'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'inherited_theorem':'R749SPT regular unimodular triangulation of K implies IDP for every n>=1',
    'new_theorem':'Minimum number of first-grid optimal-center types generating all nK lattice readouts for every n>=2 is exactly 26, with exactly two minimal alphabet choices.',
    'one_grid_size': len(P),
    'two_grid_size':len(K2),
    'three_grid_size':len(K3),
    'two_grid_unique_pair_targets':len(unique2),
    'forced_types': [list(x) for x in sorted(forced)],
    'forced_type_count':len(forced),
    'optional_types': [list(x) for x in sorted(optional)],
    'uncovered_two_grid_with_forced_only':[list(x) for x in holes2],
    'minimum_universal_alphabet_size_for_all_n_ge_2':26,
    'minimal_alphabets':results,
    'universal_proof':'IDP decomposes X in nK into n P points; n=2a+3b for n>=2; replace each 2/3 group by an equal-sum group in either 26-type alphabet.',
    'review':'AUTHOR_EXACT_NOT_REVIEWED',
    'native_X6_transfer':'NOT_ESTABLISHED',
    'numeric_mode':'exact integers only, complete 1K, 2K, 3K and finite type check'
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
