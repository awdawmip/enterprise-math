#!/usr/bin/env python3
"""Exact five named-hypothesis lower Bellman for fifth chamber, arbitrary f.
Requires exact frozen count table and previously saved VERIFY_R5_FIFTH_F2_ALL256.py.
"""
import json,sys
from functools import lru_cache
from pathlib import Path
from VERIFY_R5_FIFTH_F2_ALL256 import table_from,response_family,L,U,H

def solve(masks,tau,f,budgets):
    tab=table_from(Path(__file__).parent/'EXACT_R5_ALL_101_BUDGETS.json')
    n=len(masks); all_mask=(1<<n)-1
    uniq={}
    for k in budgets:
        fam=response_family(tab[k],masks,tau)
        uniq.setdefault(fam,k)
    queries=sorted(((v,k) for v,k in uniq.items()),key=lambda x:(x[1] not in (216,223,296),x[1]))
    actions=[(k,a,tuple(all_mask^b for b in a)) for a,k in queries]
    @lru_cache(maxsize=None)
    def V(*layers):
        agg=0
        for a in layers:agg|=a
        if agg.bit_count()<=1:return 0
        best=1<<35
        for k,answers,complements in actions:
            worst=0
            for answer,no in zip(answers,complements):
                next_layers=(layers[0]&answer,)+tuple((layers[j]&answer)|(layers[j-1]&no) for j in range(1,len(layers)))
                if next_layers==layers:break
                child=V(*next_layers)
                if child>worst:worst=child
                if k+worst>=best:break
            else:best=min(best,k+worst)
        if best>=1<<35: raise ValueError('no resolving query')
        return best
    res=V(*([all_mask]+[0]*f))
    return {'f':f,'cost':res,'state_count':V.cache_info().currsize,'actions':[k for k,*_ in actions]}
if __name__=='__main__':
    for f in map(int,sys.argv[1:] or ['8']):
        print(json.dumps(solve(H,L,f,range(214,315))))
