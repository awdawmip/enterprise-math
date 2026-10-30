#!/usr/bin/env python3
"""Exact author-side auxiliary checks: shared-label BRC descent, 2-copy rigidity,
and proper-subset parity obstruction. No native X6 or Source execution."""
from collections import Counter, defaultdict
from itertools import product, combinations
from hashlib import sha256
import json
from pathlib import Path

X = tuple(product((0, 1), repeat=2))  # (hidden h, visible q)
C = lambda x: x[1]
colors = (0, 1)

def transition(x, label):
    h, q = x
    return h, q ^ h ^ label

def outgoing_one(x):
    return dict(sorted(Counter(C(transition(x, t)) for t in colors).items()))

def outgoing_two(x, y):
    return dict(sorted(Counter((C(transition(x,t)), C(transition(y,t))) for t in colors).items()))

one_groups = defaultdict(set)
two_groups = defaultdict(set)
for x in X:
    one_groups[C(x)].add(tuple(sorted(outgoing_one(x).items())))
for x, y in product(X, repeat=2):
    two_groups[(C(x), C(y))].add(tuple(sorted(outgoing_two(x,y).items())))
assert all(len(g)==1 for g in one_groups.values())
assert any(len(g)>1 for g in two_groups.values())
a, b = (0,0), (1,0)
pair_diag = outgoing_two(a, a)
pair_cross = outgoing_two(a, b)
assert pair_diag == {(0,0):1,(1,1):1}, pair_diag
assert pair_cross == {(0,1):1,(1,0):1}, pair_cross
assert outgoing_one(a) == outgoing_one(b) == {0:1, 1:1}

# Exhaust every pair of deterministic 2-label maps on four states (4^4)^2.
# Independently compute true 2-copy lumpability instead of using the proof's shortcut.
all_maps = tuple(product(range(4), repeat=4))
C4 = tuple(x[1] for x in X)
def labelwise(f, g):
    for f1 in (f,g):
        for j in range(4):
            for k in range(4):
                if C4[j]==C4[k] and C4[f1[j]]!=C4[f1[k]]:
                    return False
    return True

def one_lumped(f, g):
    for j in range(4):
        for k in range(4):
            if C4[j]==C4[k]:
                if (C4[f[j]]+C4[g[j]]) != (C4[f[k]]+C4[g[k]]):
                    return False
    return True

def pair_lumped(f, g):
    signatures={}
    for j in range(4):
        for k in range(4):
            src=(C4[j],C4[k])
            dst=tuple(sorted(((C4[f[j]],C4[f[k]]), (C4[g[j]],C4[g[k]]))))
            old=signatures.setdefault(src,dst)
            if old!=dst:
                return False
    return True

maps_total=0
one_count=pair_count=label_count=one_not_pair=0
for f in all_maps:
    for g in all_maps:
        maps_total += 1
        one=one_lumped(f,g)
        pair=pair_lumped(f,g)
        lbl=labelwise(f,g)
        assert pair==lbl, (f,g)
        assert (not pair) or one
        one_count+=one
        pair_count+=pair
        label_count+=lbl
        one_not_pair+=(one and not pair)
assert maps_total==65536 and one_not_pair>0

# Higher-arity designated-source parity construction: m-1 independent label bits,
# output bits b_1..b_{m-1}=u, b_m=theta XOR parity(u).
def bits_for(m,theta,word):
    assert len(word)==m-1
    out=tuple(word)+(theta ^ (sum(word)%2),)
    return out

one_step_cases=0
one_step_subsets=0
records=[]
for m in range(2,9):
    labels=tuple(product((0,1),repeat=m-1))
    for k in range(m):
        for ids in combinations(range(m),k):
            counts=[]
            for theta in (0,1):
                table=Counter(tuple(bits_for(m,theta,u)[i] for i in ids) for u in labels)
                counts.append(table)
            assert counts[0]==counts[1]
            assert len(counts[0])==2**k
            assert all(n==2**(m-1-k) for n in counts[0].values())
            one_step_subsets+=1
            one_step_cases+=2*len(labels)
    full0=Counter(bits_for(m,0,u) for u in labels)
    full1=Counter(bits_for(m,1,u) for u in labels)
    assert not (set(full0) & set(full1))
    assert sum(full0.values())==sum(full1.values())==2**(m-1)
    records.append({"m":m,"labels":len(labels),"proper_subsets":2**m-1,
                    "per_full_parity_support":len(full0),"full_support_disjoint":True,
                    "proper_subset_k_m1_each_output_count":1})

# Direct history test: each fresh tick draws one new shared label independently.
# For a fixed proper subset, the entire visible path law is theta-independent.
multistep_cases=0
for m in range(2,6):
    labels=tuple(product((0,1),repeat=m-1))
    for ids_mask in range((1<<m)-1):
        ids=tuple(i for i in range(m) if ids_mask & (1<<i))
        for horizon in range(1,4):
            tables=[]
            for theta in (0,1):
                table=Counter()
                for words in product(labels,repeat=horizon):
                    q=[0]*m
                    observed=[]
                    for word in words:
                        step=bits_for(m,theta,word)
                        q=[q[i]^step[i] for i in range(m)]
                        observed.append(tuple(q[i] for i in ids))
                    table[tuple(observed)]+=1
                    multistep_cases+=1
                tables.append(table)
            assert tables[0]==tables[1], (m,ids,horizon)
            assert len(tables[0])==2**(horizon*len(ids))
            assert set(tables[0].values())=={2**((m-1-len(ids))*horizon)}

result={
 "classification":"AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
 "date":"2026-10-30",
 "model":"finite integer-weight deterministic branch family; shared label across copies",
 "four_state_counterexample":{
  "X":[list(x) for x in X],"visible":"q","labels":[0,1],
  "F_label":"(h,q) -> (h,q XOR h XOR label)",
  "one_copy_lumpable":True,"two_copy_lumpable":False,
  "single_source_output_count":outgoing_one(a),
  "paired_initial_diag":[list(a),list(a)],
  "paired_initial_cross":[list(a),list(b)],
  "common_label_pair_outputs_diag":[{"output":list(k),"count":v} for k,v in pair_diag.items()],
  "common_label_pair_outputs_cross":[{"output":list(k),"count":v} for k,v in pair_cross.items()]},
 "exhaustive_all_two_label_four_state_map_pairs":{
  "maps_tested":maps_total,"single_lumped":one_count,
  "two_lumped":pair_count,"labelwise_lumped":label_count,
  "single_lumped_but_two_not":one_not_pair,
  "two_iff_labelwise":True},
 "parity_hierarchy":{
  "m_range":[2,8],"single_step_proper_subsets_tested":one_step_subsets,
  "single_step_label_outputs_checked":one_step_cases,
  "records":records,
  "all_proper_subset_single_step_counts_exact":True,
  "full_parity_support_disjoint":True,
  "m_range_multistep":[2,5],"max_horizon":3,
  "multistep_raw_label_history_evaluations":multistep_cases,
  "proper_subset_entire_history_law_same":True},
 "all_assertions":"PASS"
}
out=Path(__file__).with_name('d25_brc_shared_label_two_copy_rigidity_author_check_20261030.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
print(json.dumps({"pass":result["all_assertions"],"maps_tested":maps_total,
 "single_lumped_but_not_two":one_not_pair,"parity_subsets":one_step_subsets,
 "label_histories_checked":multistep_cases,"json_path":str(out)},ensure_ascii=False))
