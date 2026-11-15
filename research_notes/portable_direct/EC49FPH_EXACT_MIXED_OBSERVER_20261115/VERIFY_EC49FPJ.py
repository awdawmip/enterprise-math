#!/usr/bin/env python3
"""Exact uniform expected adaptive scalar-query optimum with max depth THREE.

Run: python VERIFY_EC49FPJ.py PATH_TO_EC49FPG_EVIDENCE_DIR
EC49FPH predecessor reconstructs/validates every frozen input SHA256 and
all 228 original native scalar queries first.
"""
from functools import lru_cache
from collections import Counter
from pathlib import Path
import itertools
import json
import runpy

SRC = runpy.run_path(str(Path(__file__).with_name('VERIFY_EC49FPH.py')), run_name='verified_base')
reps=SRC['rooted_reps']; actions=SRC['actions']; coords=SRC['coords']
profile=SRC['costs']; terminal=SRC['terminal_vectors']
labels=[('T',q) for q in range(len(actions))]+[('P',r,s) for r,s in coords]
responses=[tuple(terminal[c][q] for c in reps) for q in range(len(actions))]
responses.extend(tuple(profile[c][r,s][2] for c in reps) for r,s in coords)
assert len(reps)==141 and len(responses)==228
partitions=[]
for row in responses:
    groups={}
    for i,v in enumerate(row):groups[v]=groups.get(v,0)|(1<<i)
    partitions.append(groups)

@lru_cache(None)
def depth1_cost(mask):
    n=mask.bit_count()
    if n<=1:return (0, -1)
    for q,groups in enumerate(partitions):
        if all((mask&value_mask).bit_count()<=1 for value_mask in groups.values()):
            return (n,q)
    return (None,None)

@lru_cache(None)
def depth2_cost(mask):
    n=mask.bit_count()
    if n<=1:return (0,-1)
    c,q=depth1_cost(mask)
    if c is not None:return c,q
    best_cost,best_q=None,None
    for q,groups in enumerate(partitions):
        children=[mask&group_mask for group_mask in groups.values()]
        if sum(x!=0 for x in children)<2:continue
        total=n
        feasible=True
        for child in children:
            if child.bit_count()<=1:continue
            cc,_=depth1_cost(child)
            if cc is None:
                feasible=False;break
            total+=cc
            if best_cost is not None and total>=best_cost:break
        if feasible and (best_cost is None or total<best_cost):
            best_cost,best_q=total,q
    return best_cost,best_q

scores=[]
for root_query,groups in enumerate(partitions):
    subtotal=len(reps)
    for fiber in groups.values():
        c,_=depth2_cost(fiber)
        if c is None:
            subtotal=None;break
        subtotal+=c
    if subtotal is not None:scores.append((subtotal,root_query))
assert len(scores)==63
best_cost=min(s for s,q in scores)
assert best_cost==296
optimal_first=[labels[q] for s,q in scores if s==best_cost]
assert optimal_first==[('T',32),('T',34)]
assert next(s for s,q in scores if q==0)==322

# Witness tree and exact per-original-rooted-profile decision path.
selected_q=32
paths=[]
tree=[]
for first_response, fiber in sorted(partitions[selected_q].items()):
    n=fiber.bit_count()
    if n==1:
        i=fiber.bit_length()-1
        tree.append({'first_response':first_response,'profile':reps[i]})
        paths.append([('T',selected_q,first_response)])
        continue
    _,second_q=depth2_cost(fiber)
    assert second_q is not None and second_q >=0
    branches=[]
    for value, second_block in sorted(partitions[second_q].items()):
        sub=fiber&second_block
        if not sub:continue
        if sub.bit_count()==1:
            i=sub.bit_length()-1
            branches.append({'second_response':value,'profile':reps[i]})
            paths.append([('T',selected_q,first_response),(*labels[second_q],value)])
        else:
            _,third_q=depth1_cost(sub)
            assert third_q is not None and third_q>=0
            leaves=[]
            for i in range(len(reps)):
                if sub>>i&1:
                    val=responses[third_q][i]
                    leaves.append({'third_response':val,'profile':reps[i]})
                    paths.append([('T',selected_q,first_response),(*labels[second_q],value),(*labels[third_q],val)])
            assert len({x['third_response'] for x in leaves})==len(leaves)
            branches.append({'second_response':value,'third_query':labels[third_q], 'leaves':leaves})
    tree.append({'first_response':first_response,'second_query':labels[second_q],'branches':branches})
assert len(paths)==141
path_keys={json.dumps(x) for x in paths}
assert len(path_keys)==141
counts=Counter(len(x) for x in paths)
assert sum(d*n for d,n in counts.items())==best_cost
assert max(counts)==3

result={
 'schema':'EC49FPJ_OPTIMAL_UNIFORM_EXPECTED_MIXED_BRC_DEPTH3_CERTIFICATE_V1',
 'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'original_rooted_class_representative':16943,
 'native_original_source_configurations':310,
 'equally_likely_distinct_rooted_states':141,
 'allowed_native_scalar_queries':len(labels),
 'maximum_query_depth':3,
 'all_first_queries_evaluated':len(partitions),
 'first_queries_with_feasible_depth3_trees':len(scores),
 'best_total_observation_count_across_all_141_states':best_cost,
 'exact_optimal_uniform_expected_observations':{'numerator':best_cost,'denominator':141},
 'all_optimal_initial_scalar_queries':optimal_first,
 'chosen_initial_query':labels[selected_q],
 'first_response_fibers':len(tree),
 'exact_leaf_paths':len(paths),
 'path_depth_histogram':{str(k):v for k,v in sorted(counts.items())},
 'baseline_T0_total_observations':322,
 'all_feasible_first_query_totals':[(labels[q],s) for s,q in sorted(scores,key=lambda x:x[1])],
 'tree':tree,
 'scope':'Minimum uniform expectation conditional on worst-case depth<=3, equally likely among all 141 distinct rooted profiles, unit query costs; exact native frozen 228-query menu. Unrestricted expected-cost optimum not asserted.'
}
print('EC49FPJ_UNIFORM_DEPTH3_EXPECTATION_EXACT_PASS')
print(json.dumps(result,ensure_ascii=False,indent=2))
