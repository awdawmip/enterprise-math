#!/usr/bin/env python3
"""EC49FRV exact original-BRC five-query price redundancy full native tree replay.

Extract EC49FRS_EC49FRT_ORIGINAL_BRC_PRICE_PHASE_FULL_EVIDENCE_20261117;
place in code/ alongside EC49FRQ_INDEPENDENT_ALL228.py and EC49FQI_NATIVE_DATA.py.
Run: python code/EC49FRV_FIFTH_QUERY_REDUNDANCY_VERIFY_20261117.py
Every integer selected surcharge is additional cost /282 * t.
"""
import sys,json,hashlib
from collections import Counter
from functools import cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'code'))
from EC49FRQ_INDEPENDENT_ALL228 import PARTS,OBS,ALL,subset_keys
from EC49FQI_NATIVE_DATA import V,keys,PIN,MASTER,CSV
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((ROOT/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((ROOT/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(OBS)==len(V)==len(PARTS)==228
assert all(OBS[q]==V[q] for q in range(144))
assert all(OBS[144+i]==V[144+keys.index(k)] for i,k in enumerate(subset_keys))
native=lambda q:q if q<144 else 144+keys.index(subset_keys[q-144])
CHOSEN=(32,34,140,142,46)
# Integer baseline query price = 282. Price cases lie in the five strict
# four-price chambers; each adds 60/282 to original q46 price.
CASES=[
 {'label':'A','prices':(2,16,16,16,60),'root':32},
 {'label':'A_prime','prices':(16,2,16,16,60),'root':34},
 {'label':'B','prices':(16,16,1,16,60),'root':140},
 {'label':'B_prime','prices':(16,16,16,1,60),'root':142},
 {'label':'C','prices':(16,16,16,16,60),'root':93},
]

def run(spec):
    sur=dict(zip(CHOSEN,spec['prices']))
    @cache
    def solve(mask):
        if mask.bit_count()==1:return 0,()
        best=10**55;first=[]
        for q,part in enumerate(PARTS):
            kids=[mask&p for p in part if mask&p]
            if len(kids)<2:continue
            cost=(282+sur.get(q,0))*mask.bit_count()+sum(solve(k)[0] for k in kids)
            if cost<best:best=cost;first=[q]
            elif cost==best:first.append(q)
        return best,tuple(first)
    value,first=solve(ALL)
    assert spec['root'] in [native(q) for q in first]

    def tree(mask,forced=None):
        if mask.bit_count()==1:return {'leaf':mask.bit_length()-1}
        q=forced if forced is not None else solve(mask)[1][0]
        children={}
        for p in PARTS[q]:
            subset=mask&p
            if subset:
                i=(subset&-subset).bit_length()-1
                children[str(OBS[q][i])]=tree(subset)
        assert len(children)>1
        return {'q':native(q),'children':children}

    witness=tree(ALL,spec['root'])
    counts=Counter();max_depth=0
    for i in range(141):
        node=witness;depth=0
        while 'leaf' not in node:
            q=node['q'];counts[q]+=1;depth+=1
            node=node['children'][str(V[q][i])]
        assert node['leaf']==i
        max_depth=max(max_depth,depth)
    assert counts[46]==0
    assert value==282*sum(counts.values())+sum(sur.get(q,0)*counts[q] for q in CHOSEN)
    out={'label':spec['label'],'extra_integer_prices_over_282':list(spec['prices']),
         'first_native_id':spec['root'],'bellman_integer_cost':value,
         'optimal_first_original_ids':[native(q) for q in first],
         'reachable_masks':solve.cache_info().currsize,
         'total_uses':sum(counts.values()),
         'incidence':{str(q):counts[q] for q in CHOSEN},
         'max_depth':max_depth,'native_states_replayed':141,
         'tree_sha256':hashlib.sha256(json.dumps(witness,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
         'tree':witness}
    print(spec['label'],out['total_uses'],out['incidence'],value,flush=True)
    return out

if __name__=='__main__':
    data={'schema':'EC49FRV_Q46_REDUNDANT_FIVE_CHAMBER_CERTIFICATE_V1',
          'frozen_pin':PIN,
          'query_indices':'all original 228 physical observations',
          'selected_surcharged_queries':list(CHOSEN),
          'integer_baseline_price':282,
          'witnesses':[run(s) for s in CASES],
          'status':'AUTHOR_PROVED/EXACT_FINITE_BELLMAN_REPLAY/NOT_REVIEWED'}
    dest=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'evidence/EC49FRV_FIFTH_QUERY_REDUNDANCY.json'
    dest.parent.mkdir(exist_ok=True,parents=True)
    dest.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print('SAVED',dest,dest.stat().st_size)
