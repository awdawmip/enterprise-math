#!/usr/bin/env python3
"""Independent literal-prefix subset-minimal antichain cross-check for EC49FCM."""
import json,time,argparse
from itertools import combinations
from frozen_model import REQ,W,observe,primpref,candidates
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BOUND=158
def antichain(items):
    kept=[]
    for s in sorted(set(items),key=len):
        if not any(k.issubset(s) for k in kept):kept.append(s)
    return kept
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    p.add_argument('--step',type=int,default=20)
    a=p.parse_args()
    chosen={f'{h}:{observe(w)}':w for h,ws in W.items() for w in ws}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    slots=[(*e,f'8:{x}',f'9:{y}') for e in combinations(early,3) for x in REQ[8] for y in REQ[9]]
    assert len(slots)==960
    pools={}
    def pool(k):
        if k not in pools:
            h,s=map(int,k.split(':'))
            pools[k]=[frozenset(primpref(w)) for w in candidates(h)[s]]
        return pools[k]
    rows=[];t=time.monotonic()
    indices=sorted(set([0,959]+list(range(0,960,a.step))))
    for i in indices:
        ss=slots[i]
        fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in ss))
        cap=BOUND-len(fixed)
        values=[]
        for k in ss:
            r={w-fixed for w in pool(k)}
            values.append((k,[v for v in r if len(v)<cap]))
        values.sort(key=lambda kv:len(kv[1]))
        states=[frozenset()];stages=[]
        for k,vals in values:
            states=antichain(x|y for x in states for y in vals if len(x|y)<cap)
            stages.append(len(states))
            if not states:break
        best=min([BOUND]+[len(fixed)+len(s) for s in states])
        rows.append({'index':i,'slots':ss,'fixed_edges':len(fixed),'min':best,'stages':stages})
        assert best==158,(i,best)
    obj={'schema':'EC49FCM_INDEPENDENT_LITERAL_PREFIX_ANTICHAIN_V1','science_pin':PIN,
        'indices':indices,'groups_checked':len(rows),
        'minima':sorted(set(r['min'] for r in rows)),
        'seconds':round(time.monotonic()-t,3),'rows':rows}
    open(a.output,'w').write(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in obj.items() if k!='rows'},sort_keys=True))
if __name__=='__main__':main()
