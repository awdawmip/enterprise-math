#!/usr/bin/env python3
"""Exact optimal 3-depth adaptive mixed BRC sensing, native class 16943.

Run: python VERIFY_EC49FPI.py PATH_TO_EC49FPG_EVIDENCE_DIR
VERIFY_EC49FPH.py in the same directory is required and first revalidates all
frozen source hashes and the fixed-observer 228-query exhaustive proof.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import itertools
import json
import runpy
import sys

PREV=Path(__file__).with_name('VERIFY_EC49FPH.py')
source=runpy.run_path(str(PREV),run_name='ec49fph_verified_source')
reps=source['rooted_reps']; actions=source['actions']; coords=source['coords']
costs=source['costs']; terminal=source['terminal_vectors']
assert len(reps)==141 and len(actions)==144 and len(coords)==84
labels=[('T',q) for q in range(144)]+[('P',r,s) for r,s in coords]
response=[tuple(terminal[k][q] for k in reps) for q in range(144)] + [tuple(costs[k][r,s][2] for k in reps) for r,s in coords]
assert len(response)==228
partitions=[]
for row in response:
    groups={}
    for j,value in enumerate(row):
        groups[value]=groups.get(value,0)|(1<<j)
    partitions.append(groups)
ALL=(1<<len(reps))-1

@lru_cache(None)
def separate_one(mask):
    if mask.bit_count()<=1:return -1
    for q,groups in enumerate(partitions):
        if all((mask & part).bit_count()<=1 for part in groups.values()):return q
    return None

@lru_cache(None)
def separate_two(mask):
    if mask.bit_count()<=1:return (-1,{})
    q=separate_one(mask)
    if q is not None:return (q,{})
    for q,groups in enumerate(partitions):
        children=[mask&part for part in groups.values()]
        if sum(bool(child) for child in children)<2:continue
        third={}
        for child in children:
            if child.bit_count()<=1:continue
            q3=separate_one(child)
            if q3 is None:break
            third[child]=q3
        else:return (q,third)
    return None

# Lower bound: after ANY of 228 first queries, at least one response fiber
# cannot be resolved by a single further query (including named-root costs).
failures=[]
for q,groups in enumerate(partitions):
    bad=next((mask for mask in groups.values() if mask.bit_count()>1 and separate_one(mask) is None),None)
    assert bad is not None, ('adaptive two-depth upper witness',labels[q])
    failures.append({'first_query':labels[q], 'unresolved_fiber_size':bad.bit_count()})
assert len(failures)==228

# Upper bound: fixed first terminal observation T(0), followed by one
# adaptive 2-decision suffix for each exact integer response fiber.
tree=[]; max_depth=1; allpaths=[]
for first_value,first_mask in sorted(partitions[0].items()):
    suffix=separate_two(first_mask)
    assert suffix is not None
    second_q,_=suffix
    first_states=[j for j in range(len(reps)) if first_mask>>j&1]
    if second_q==-1:
        assert len(first_states)==1
        tree.append({'first_response':first_value,'profile':reps[first_states[0]]})
        allpaths.append((first_value,));continue
    branches=[]
    for second_value,second_group in sorted(partitions[second_q].items()):
        second_mask=first_mask&second_group
        if not second_mask:continue
        second_states=[j for j in first_states if second_mask>>j&1]
        if len(second_states)==1:
            branches.append({'second_response':second_value,'profile':reps[second_states[0]]})
            allpaths.append((first_value,second_value))
            max_depth=max(max_depth,2)
        else:
            third_q=separate_one(second_mask)
            assert third_q is not None
            leaves=[{'third_response':response[third_q][j],'profile':reps[j]} for j in second_states]
            assert len(set(v['third_response'] for v in leaves))==len(leaves)
            branches.append({'second_response':second_value,'third_query':labels[third_q],'leaves':sorted(leaves,key=lambda v:v['third_response'])})
            allpaths.extend((first_value,second_value,response[third_q][j]) for j in second_states)
            max_depth=3
    tree.append({'first_response':first_value,'second_query':labels[second_q],'branches':branches})
assert len(allpaths)==141 and len(set(allpaths))==141
assert max_depth==3
report={
  'schema':'EC49FPI_EXACT_ADAPTIVE_MIXED_NATIVE_BRC_OBSERVER_V1',
  'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
  'original_class_representative':16943,
  'rooted_states':141,'possible_scalar_queries':228,
  'candidate_first_queries_excluded_at_depth_2':len(failures),
  'exact_minimum_adaptive_worst_case_depth':3,
  'constructive_first_query':labels[0],
  'first_response_fibers':len(tree),
  'unique_terminal_decision_paths':len(set(allpaths)),
  'decision_tree':tree,
  'lower_bound_fiber_witnesses':failures,
  'verification_scope':'Fixed frozen native legal-root-domain class16943; allowed subsequent queries depend on prior exact responses; scalar query menu = 144 legal terminals +84 original named-root subset costs.'}
print('EC49FPI_ADAPTIVE_EXACT_FINITE_PROOF_PASS')
print(json.dumps(report,ensure_ascii=False,indent=2))
