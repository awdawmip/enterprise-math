#!/usr/bin/env python3
"""EC49FRU second, separately implemented full 228-native-query Bellman anchors.

Reads the independently reconstructed original 94-family native responses V
from EC49FQI_NATIVE_DATA.py, not the primary DP's PARTS/OBS/ordering.
Run in extracted EC49FRS-FRT original evidence bundle's code/ folder.
"""
from pathlib import Path
from collections import defaultdict
from functools import cache
import sys,json,hashlib
BASE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(BASE/'code'))
from EC49FQI_NATIVE_DATA import V,PIN,MASTER,CSV
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((BASE/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((BASE/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(V[0])==141
PARTS=[]
for v in V:
    d=defaultdict(int)
    for i,output in enumerate(v):d[output] |= 1<<i
    PARTS.append(tuple(d.values()))
ALL=(1<<141)-1

def anchor(a,b,c,d):
    prices=dict(zip((32,34,140,142),(a,b,c,d)))
    @cache
    def F(mask):
        if mask.bit_count()==1:return 0,()
        best=10**50;first=[]
        for q,parts in enumerate(PARTS):
            children=[mask&p for p in parts if mask&p]
            if len(children)<2:continue
            cost=(141+prices.get(q,0))*mask.bit_count()+sum(F(z)[0] for z in children)
            if cost<best:best=cost;first=[q]
            elif cost==best:first.append(q)
        return best,tuple(first)
    value,first=F(ALL)
    expected=min(296*141+141*a,296*141+141*b,
                 298*141+141*c,298*141+141*d,299*141)
    assert value==expected
    assert F.cache_info().currsize==13063
    return {'deltas_over_141':[a,b,c,d],'integer_value':value,
            'all_optimal_native_first':first,'subsets':F.cache_info().currsize}

if __name__=='__main__':
    actual=[anchor(*x) for x in ((0,0,0,0),(2,2,0,0),(3,3,1,1))]
    assert [i['integer_value'] for i in actual]==[41736,42018,42159]
    assert [i['all_optimal_native_first'] for i in actual]==[
        (32,34),(32,34,140,142),(32,34,46,93,140,142)]
    print(json.dumps({'pin':PIN,'independent_anchors':actual},
                     ensure_ascii=False,indent=2))
