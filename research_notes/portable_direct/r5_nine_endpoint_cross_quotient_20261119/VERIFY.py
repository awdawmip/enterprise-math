#!/usr/bin/env python3
"""Exact nine-state endpoint-crossing census. No third-party modules.
Usage: python VERIFY.py EXACT_R5_ALL_101_BUDGETS.json [partition_2026.json]
The 30,876-pair exhaustive scan may take longer than a short tool time limit;
its computation can be split with the separately archived chunk verifier.
"""
import collections
import hashlib
import itertools
import json
import random
import sys
from pathlib import Path

SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
H = (18,24,82,34,17,144,208)
L = 25845652773852463277015040000
U1 = 58182461585441404127941754879

def maximal(masks):
    v = set(masks)
    return tuple(sorted(s for s in v if not any(s != t and (s & t) == s for t in v)))

def window_support(centers, tau):
    return maximal(sum(1 << i for i, c in enumerate(centers) if v <= c <= v+tau)
                   for v in centers)

def independent_sweep(centers, tau):
    ends = sorted({q for c in centers for q in (2*c-tau,2*c+tau)})
    masks = [sum(1<<i for i,c in enumerate(centers) if abs(z-2*c) <= tau) for z in ends]
    masks.extend(sum(1<<i for i,c in enumerate(centers)
                     if abs(a+b-4*c) <= 2*tau) for a,b in zip(ends,ends[1:]))
    return maximal(masks)

def sig(matrices, pair, tau, support=window_support):
    x,y=pair
    h=(18,24,82,34,17,x,144,208,y)
    return tuple(support([row[j] for j in h],tau) for row in matrices)

def main():
    if len(sys.argv) not in (2,3):
        raise SystemExit("usage: python VERIFY.py FROZEN.json [partition_2026.json]")
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA, "frozen table SHA mismatch"
    d=json.loads(raw)["counts_and_cohorts"]
    matrices=[[int(c) for c in d[str(k)]["counts"]] for k in range(214,315)]
    cand=[i for i in range(256) if i not in H]
    pairs=list(itertools.combinations(cand,2))
    assert len(pairs)==30876
    left=collections.defaultdict(list)
    right=collections.defaultdict(list)
    for p in pairs:
        left[sig(matrices,p,L)].append(p)
        right[sig(matrices,p,U1)].append(p)
    lg=sorted(left.values(),key=lambda v:v[0])
    rg=sorted(right.values(),key=lambda v:v[0])
    assert len(lg)==1460 and len(rg)==2026
    if len(sys.argv)==3:
        old=json.loads(Path(sys.argv[2]).read_text())
        assert [(i,g[0][0],g[0][1],len(g)) for i,g in enumerate(rg)] == [
            (v["group_id"],v["x"],v["y"],v["size"]) for v in old]
    lm={p:i for i,g in enumerate(lg) for p in g}
    rm={p:i for i,g in enumerate(rg) for p in g}
    inter=collections.defaultdict(list)
    lr=collections.defaultdict(set)
    rl=collections.defaultdict(set)
    for p in pairs:
        a,b=lm[p],rm[p]
        inter[a,b].append(p)
        lr[a].add(b)
        rl[b].add(a)
    choose2=lambda sets:sum(len(g)*(len(g)-1)//2 for g in sets)
    both=choose2(inter.values())
    counts={
        "pair_instances":len(pairs),
        "left_classes":len(lg),
        "upper_classes":len(rg),
        "joint_classes":len(inter),
        "left_classes_split_by_upper":sum(len(v)>1 for v in lr.values()),
        "upper_classes_split_by_left":sum(len(v)>1 for v in rl.values()),
        "max_upper_classes_per_left":max(map(len,lr.values())),
        "max_left_classes_per_upper":max(map(len,rl.values())),
        "left_equivalent_unordered_pair_pairs":choose2(lg),
        "upper_equivalent_unordered_pair_pairs":choose2(rg),
        "both_endpoint_equivalent_unordered_pair_pairs":both,
        "left_only_equivalences":choose2(lg)-both,
        "upper_only_equivalences":choose2(rg)-both
    }
    expected={
        "pair_instances":30876,"left_classes":1460,"upper_classes":2026,
        "joint_classes":2563,"left_classes_split_by_upper":508,
        "upper_classes_split_by_left":509,"max_upper_classes_per_left":8,
        "max_left_classes_per_upper":3,
        "left_equivalent_unordered_pair_pairs":2399087,
        "upper_equivalent_unordered_pair_pairs":1447239,
        "both_endpoint_equivalent_unordered_pair_pairs":1364220,
        "left_only_equivalences":1034867,"upper_only_equivalences":83019
    }
    assert counts==expected,(counts,expected)
    a,b,c=(0,3),(0,5),(0,4)
    assert lm[a]==lm[b] and rm[a]!=rm[b]
    assert rm[a]==rm[c] and lm[a]!=lm[c]
    assert sig(matrices,a,U1)[7]==(45,192,274)
    assert sig(matrices,b,U1)[7]==(18,45,192,256)
    assert sig(matrices,a,L)[7]==(13,18,32,192,256)
    assert sig(matrices,c,L)[7]==(13,32,192,274)
    random.seed(20261119)
    test=[a,b,c]+random.sample(pairs,64)
    checks=0
    for pair in test:
        h=(18,24,82,34,17,pair[0],144,208,pair[1])
        for tau in (L,U1):
            for row in matrices:
                centers=[row[z] for z in h]
                assert window_support(centers,tau)==independent_sweep(centers,tau)
                checks+=1
    assert sig(matrices,a,L,independent_sweep)==sig(matrices,b,L,independent_sweep)
    assert sig(matrices,a,U1,independent_sweep)==sig(matrices,c,U1,independent_sweep)
    assert checks==13534
    counts["independent_interval_sweep_checks"]=checks
    print("PASS_R5_NINE_ENDPOINT_CROSS",json.dumps(counts,sort_keys=True))

if __name__=="__main__":
    main()
