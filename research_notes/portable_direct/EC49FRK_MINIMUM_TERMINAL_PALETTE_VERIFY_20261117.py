#!/usr/bin/env python3
"""EC49FRK exact minimum fixed terminal observation palette certificate.

Standalone if placed in a directory with:
  code/EC49FQI_NATIVE_DATA.py
  source/frozen_original_master.txt
  source/EC49FPG_PROFILE.csv

Execute from that directory: python code/EC49FRK_MINIMUM_TERMINAL_PALETTE.py
Scientific input commit remains fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import defaultdict
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json, hashlib, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(HERE))
from EC49FQI_NATIVE_DATA import V, weights, reps, PIN, MASTER, CSV

assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((ROOT/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((ROOT/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(weights)==141 and sum(weights)==310

NT,NR,N=144,84,141
T=tuple(range(NT)); R=tuple(range(NT,NT+NR))

def classes(qs):
    bins={}
    for i in range(N):
        sig=tuple(V[q][i] for q in qs)
        bins.setdefault(sig,[]).append(i)
    return sorted((tuple(x) for x in bins.values()),key=lambda g:g[0])

original=classes(T)
collisions=[list(c) for c in original if len(c)>1]
assert len(original)==139 and collisions==[[8,139],[46,140]]
sep_pairs=[(i,j) for i in range(N) for j in range(i+1,N)
           if any(V[q][i]!=V[q][j] for q in T)]
assert len(sep_pairs)==9868
bits=[]
for q in T:
    mask=0
    for k,(i,j) in enumerate(sep_pairs):
        if V[q][i]!=V[q][j]:
            mask |= 1<<k
    bits.append(mask)
full=(1<<len(sep_pairs))-1

# Exact exhaustion, every C(144,3)=487344 distinct three-query palette.
count=0; best=0; best_examples=[]
for i in range(142):
    for j in range(i+1,143):
        mask=bits[i]|bits[j]
        for k in range(j+1,144):
            covered=(mask|bits[k]).bit_count()
            count+=1
            if covered>best:
                best=covered;best_examples=[(i,j,k)]
            elif covered==best:
                best_examples.append((i,j,k))
assert count==487344 and best==9866 and best<len(sep_pairs)

quad=(31,36,102,142)
assert (bits[quad[0]]|bits[quad[1]]|bits[quad[2]]|bits[quad[3]])==full
assert classes(quad)==original
assert classes(quad+(148,))==[(i,) for i in range(N)]

# Verify all 144 possible one-terminal deletions retain the full partition.
assert all(classes(tuple(v for v in T if v!=q))==original for q in T)
# Exact one-query re-pricing experiment: original root response becomes cheap.
upgraded=[q for q in R if len(classes(T+(q,)))==N]
assert upgraded==list(range(148,164))
assert all(len(classes(T+(q,)))==(N if q in upgraded else 139) for q in R)

# Weighted root-only Bellman on each indistinguishable terminal fiber.
def fiber_min_root_mass(cls, weight_vector):
    if len(cls)<=1:return 0
    patterns=set()
    for q in R:
        p=defaultdict(int)
        for k,i in enumerate(cls):
            p[V[q][i]] |= 1<<k
        parts=tuple(sorted(p.values()))
        if len(parts)>1:patterns.add(parts)
    @lru_cache(None)
    def cost(mask):
        if mask.bit_count()<=1:return 0
        W=sum(weight_vector[cls[k]] for k in range(len(cls)) if mask>>k&1)
        values=[]
        for p in patterns:
            subs=set((mask & part) for part in p)-{0}
            if len(subs)<2:continue
            children=[cost(s) for s in subs]
            if all(c is not None for c in children):
                values.append(W+sum(children))
        return min(values) if values else None
    return cost((1<<len(cls))-1)

uniform=sum(fiber_min_root_mass(c,[1]*N) for c in original)
weighted=sum(fiber_min_root_mass(c,weights) for c in original)
assert (uniform,weighted)==(4,4)
assert all(len(c)==1 or all(V[148][i]!=V[148][j]
           for i,j in combinations(c,2)) for c in classes(quad))

result={
  'schema':'EC49FRK_EXACT_MINIMUM_FIXED_TERMINAL_OBSERVER_PALETTE_V1',
  'scientific_frozen_commit':PIN,
  'master_sha256':MASTER,
  'profile_sha256':CSV,
  'named_profiles':N,
  'original_configurations':sum(weights),
  'terminal_physical_observations':NT,
  'root_physical_observations':NR,
  'full_terminal_signature_classes':len(original),
  'irreducible_pairs':collisions,
  'terminally_separated_profile_pairs':len(sep_pairs),
  'exhaustive_three_query_sets':count,
  'max_separated_pairs_by_any_three':best,
  'best_triple_examples':[list(t) for t in best_examples[:10]],
  'optimal_terminal_palette':list(quad),
  'minimum_fixed_terminal_palette_cardinality':4,
  'all_single_terminal_deletions_preserve_partition':True,
  'single_promoted_root_ids_yielding_full_terminal_identifiability':upgraded,
  'uniform_min_total_root_calls':uniform,
  'multiplicity_weighted_min_total_root_calls':weighted,
  'exact_four_terminal_one_conditional_root_strategy':{
    'terminal_ids':list(quad),
    'root_id':148,
    'root_only_if_terminal_signature_is_not_unique':True,
    'worst_case_total_query_count':5,
    'terminal_queries_on_every_path':4,
    'maximum_root_queries_per_path':1
  },
  'root_slope_for_mixture_prior':'4*((1-lambda)/141+lambda/310)',
  'constructive_price_upper_bound_in_terminal_cost_units':
    '4+x*4*((1-lambda)/141+lambda/310)',
  'mathematical_status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'
}
output=ROOT/'EC49FRK_MINIMUM_PALETTE_CERTIFICATE.json'
output.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
print('PASS: exact native 139 terminal classes, 2 pairs')
print('PASS: all',count,'triples, max covered',best,'/',len(sep_pairs))
print('PASS: minimum terminal palette',quad)
print('PASS: 144 removals, 84 root-price transfers')
print('PASS: five-query conditional identifier / weighted root floor',uniform,weighted)
print('SHA256 certificate',hashlib.sha256(output.read_bytes()).hexdigest())
