#!/usr/bin/env python3
"""EC49FRU exact original-BRC four-named-query full Bellman + tree replay.

Place this file in code/ inside the unmodified extracted
EC49FRS_EC49FRT_ORIGINAL_BRC_PRICE_PHASE_FULL_EVIDENCE_20261117
archive. Run: python code/EC49FRU_FOUR_INDEPENDENT_NAMED_SURCHARGES_VERIFY.py
Each integer delta d represents a selected-query surcharge (d/141)*t.
The integer objective is 141 times the aggregate path cost over 141 states.
"""
from __future__ import annotations
import sys, hashlib, json, time
from functools import cache
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
sys.path.insert(0,str(HERE))
from EC49FRQ_INDEPENDENT_ALL228 import (
    PARTS, OBS, ALL, subset_keys, representatives, multiplicities)
from EC49FQI_NATIVE_DATA import V,keys,PIN,MASTER,CSV,reps,weights
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((BASE/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((BASE/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert representatives==reps and multiplicities==weights
assert len(reps)==141 and sum(weights)==310
assert len(OBS)==len(V)==len(PARTS)==228
assert all(OBS[q]==V[q] for q in range(144))
assert len(keys)==len(subset_keys)==84 and set(keys)==set(subset_keys)
assert all(OBS[144+i]==V[144+keys.index(k)] for i,k in enumerate(subset_keys))
CHARGED=(32,34,140,142)

def native(q):
    return q if q<144 else 144+keys.index(subset_keys[q-144])

def check(deltas,witness_roots=()):
    assert len(deltas)==4 and all(isinstance(d,int) and d>=0 for d in deltas)
    prices=dict(zip(CHARGED,deltas))
    @cache
    def opt(mask):
        if mask.bit_count()==1:return (0,())
        best=10**50;opts=[]
        for q,parts in enumerate(PARTS):
            ch=[mask&p for p in parts if mask&p]
            if len(ch)<2:continue
            val=(141+prices.get(q,0))*mask.bit_count()+sum(opt(y)[0] for y in ch)
            if val<best:best=val;opts=[q]
            elif val==best:opts.append(q)
        return best,tuple(opts)
    started=time.monotonic()
    value,choices=opt(ALL)
    a,b,c,d=deltas
    predicted=min(296*141+141*a,296*141+141*b,
                  298*141+141*c,298*141+141*d,299*141)
    assert value==predicted,(deltas,value,predicted)
    out={'deltas_over_141':list(deltas),'exact_integer_value':value,
         'candidate_integer_value':predicted,
         'all_optimal_first_native_ids':sorted(native(q) for q in choices),
         'bellman_subsets':opt.cache_info().currsize,
         'seconds':round(time.monotonic()-started,3)}
    witnesses={}
    for orig_q in witness_roots:
        q=orig_q if orig_q<144 else 144+subset_keys.index(keys[orig_q-144])
        assert q in choices,(orig_q,out)
        def build(mask,force=None):
            if mask.bit_count()==1:return {'leaf':mask.bit_length()-1}
            z=force if force is not None else opt(mask)[1][0]
            branches={}
            for p in PARTS[z]:
                sub=p&mask
                if not sub:continue
                state=(sub&-sub).bit_length()-1
                branches[str(OBS[z][state])]=build(sub)
            assert len(branches)>1
            return {'query':native(z),'branches':branches}
        tree=build(ALL,q)
        counts=Counter();max_depth=0
        for state in range(141):
            node=tree;depth=0
            while 'leaf' not in node:
                j=node['query'];counts[j]+=1;depth+=1
                node=node['branches'][str(V[j][state])]
            assert node['leaf']==state
            max_depth=max(depth,max_depth)
        actual_cost=141*sum(counts.values())+sum(prices.get(z,0)*counts[z] for z in CHARGED)
        assert actual_cost==value,(orig_q,actual_cost,value)
        witnesses[str(orig_q)]={
            'total_uses':sum(counts.values()),
            'named_incidence':{str(j):counts[j] for j in CHARGED},
            'worst_depth':max_depth,'replayed_states':141,
            'tree_sha256':hashlib.sha256(json.dumps(tree,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'tree':tree}
    if witnesses:out['complete_witness_trees']=witnesses
    print(deltas,value,out['all_optimal_first_native_ids'],
          out['bellman_subsets'],out['seconds'],flush=True)
    return out

if __name__=='__main__':
    tests=[
       ((0,0,0,0),()),((2,2,0,0),()),((3,3,1,1),()),
       ((0,8,8,8),(32,)),((8,0,8,8),(34,)),
       ((8,8,0,8),(140,)),((8,8,8,0),(142,)),
       ((8,8,8,8),(46,93)),((0,7,3,6),()),
       ((7,0,6,3),()),((3,6,1,8),()),((5,5,2,3),())]
    data={'schema':'EC49FRU_FOUR_NAMED_COST_PARETO_V1','source_pin':PIN,
          'raw_master_sha256':MASTER,'raw_profile_sha256':CSV,
          'named_states':141,'original_configurations':310,
          'original_queries':228,'price_units':'delta/141 times terminal base t',
          'tests':[check(ds,roots) for ds,roots in tests]}
    target=Path(sys.argv[1]) if len(sys.argv)>1 else BASE/'evidence/EC49FRU_FOUR_NAMED_SURCHARGES_CERTIFICATE.json'
    target.parent.mkdir(exist_ok=True,parents=True)
    target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('CERTIFICATE',target,len(target.read_bytes()),flush=True)
