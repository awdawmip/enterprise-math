#!/usr/bin/env python3
"""Exact 720-group five-path early3+H7pair signed primitive-prefix certificate."""
from frozen_model import REQ, W, observe, primpref, candidates
from itertools import combinations
import json, argparse

def minima(seq):
    kept=[]
    for value in sorted(set(seq), key=lambda v:(len(v), sorted(v))):
        if not any(k<=value for k in kept):
            kept.append(value)
    return kept

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=720)
    ap.add_argument('--output',default='EC49FCN_RECOMPUTED.json')
    arg=ap.parse_args()
    assert 0<=arg.start<arg.stop<=720
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    h7=[f'7:{s}' for s in REQ[7]]
    slots=[(*e,*l) for e in combinations(early,3) for l in combinations(h7,2)]
    assert len(slots)==720
    pools={name:candidates(int(name.split(':')[0]))[int(name.split(':')[1])]
           for name in early+h7}
    rows=[]
    for i in range(arg.start,arg.stop):
        pick=slots[i]
        fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in pick))
        budget=158-len(fixed)
        choices=[]
        for k in pick:
            options=(frozenset(set(primpref(w))-fixed) for w in pools[k])
            valid=(r for r in options if len(r)<budget)
            choices.append((k,minima(valid)))
        choices.sort(key=lambda kv:len(kv[1]))
        states=[frozenset()]; stage=[]
        for key,options in choices:
            states=minima(x|y for x in states for y in options if len(x|y)<budget)
            stage.append(len(states))
            if not states:break
        minimum=158 if not states else min(158,len(fixed)+min(map(len,states)))
        rows.append({'index':i,'slots':pick,'fixed_edges':len(fixed),
                     'stages':stage,'minimum':minimum})
    summary={'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
             'family':'early3+H7pair','total':720,'range':[arg.start,arg.stop],
             'checked':len(rows),'distinct_minima':sorted({r['minimum'] for r in rows}),
             'strict_improvements':sum(r['minimum']<158 for r in rows)}
    with open(arg.output,'w') as f:json.dump({'summary':summary,'rows':rows},f,sort_keys=True)
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
