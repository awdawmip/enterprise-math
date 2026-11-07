#!/usr/bin/env python3
"""Independent literal signed-prefix antichain audit of all EC49FCL quintets."""
import json,sys,time
from itertools import combinations
from frozen_model import REQ,W,observe,primpref,candidates
BOUND=158
INDEX=range(1920)
def pareto_min(sets):
    results=[]
    for s in sorted(set(sets),key=lambda x:(len(x),tuple(sorted(x)))):
        if not any(m<=s for m in results):
            results.append(s)
    return set(results)
def run():
    chosen={f'{h}:{observe(w)}':w for h,ws in W.items() for w in ws}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    combos=[(*es,f'7:{p}',f'8:{q}') for es in combinations(early,3) for p in REQ[7] for q in REQ[8]]
    assert len(combos)==1920
    pool={};rows=[]
    for idx in INDEX:
        slots=combos[idx];t=time.perf_counter()
        fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in slots))
        c=BOUND-len(fixed);residuals=[]
        for k in slots:
            if k not in pool:
                h,s=map(int,k.split(':'));pool[k]=candidates(h)[s]
            vals={frozenset(set(primpref(w))-fixed) for w in pool[k]}
            residuals.append((k,[v for v in vals if len(v)<c],len(vals)))
        residuals.sort(key=lambda v:(len(v[1]),sum(len(s) for s in v[1])))
        states={frozenset()};sizes=[]
        for k,vals,_ in residuals:
            states=pareto_min((a|b for a in states for b in vals if len(a|b)<c))
            sizes.append(len(states))
            if not states:break
        minimum=min([BOUND]+[len(fixed)+len(s) for s in states])
        assert minimum==158,(idx,minimum)
        row={'index':idx,'slots':slots,'fixed_edges':len(fixed),'cap':c,'minimum':minimum,'antichain_stage_counts':sizes,'seconds':round(time.perf_counter()-t,3)}
        print('ANTICHAIN',idx,'min',minimum,'stage',sizes,'secs',row['seconds'],flush=True)
        rows.append(row)
    result={'schema':'EC49FCL_INDEPENDENT_LITERAL_PREFIX_ANTICHAIN_V1','science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','indices':list(INDEX),'rows':rows}
    with open('EC49FCL_ANTICHAIN_FULL_1920.json','w') as f:json.dump(result,f,indent=2)
    print('SUCCESS',len(rows),flush=True)
if __name__=='__main__':run()
