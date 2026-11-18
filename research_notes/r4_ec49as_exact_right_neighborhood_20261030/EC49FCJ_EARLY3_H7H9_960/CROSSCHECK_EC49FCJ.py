#!/usr/bin/env python3
"""Independent literal native-signed-prefix-set crosscheck of sampled quintets."""
from pathlib import Path
from itertools import combinations
import json,sys
from frozen_model import REQ,W,observe,candidates,primpref
BASE=Path(__file__).resolve().parent
INDEX=[0,39,40,119,120,239,240,359,360,479,480,599,600,719,720,839,840,959]
def main():
    rows={}
    for f in sorted(BASE.glob('EC49FCJ_H7H9_*_*.json')):
        for r in json.loads(f.read_text())['rows']:rows[tuple(r['slots'])]=r
    assert len(rows)==960
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    pairs=[(f'7:{s}',f'9:{t}') for s in REQ[7] for t in REQ[9]]
    combos=[(*e,*p) for e in combinations(early,3) for p in pairs]
    cache={};checked=[]
    for i in INDEX:
        group=combos[i]
        fixed=set().union(*(set(primpref(w)) for s,w in chosen.items() if s not in group))
        d=158-len(fixed)
        entries=[]
        for slot in group:
            if slot not in cache:
                h,s=map(int,slot.split(':'))
                cache[slot]=candidates(h)[s]
            residuals={frozenset(set(primpref(word))-fixed) for word in cache[slot]}
            allowed=[r for r in residuals if len(r)<d]
            entries.append((slot,allowed))
        entries.sort(key=lambda e:(len(e[1]),sum(len(s) for s in e[1])))
        states={frozenset()};stage=[]
        for slot,allowed in entries:
            states={u|s for u in states for s in allowed if len(u|s)<d}
            stage.append(len(states))
            if not states:break
        value=min([158]+[len(fixed)+len(s) for s in states])
        reference=rows[group]
        assert value==reference['minimum'] and len(fixed)==reference['fixed_edges']
        checked.append({'index':i,'slots':list(group),'minimum':value,
                        'fixed_edges':len(fixed),'direct_stage_counts':stage})
        print('CROSSCHECK',i,value,flush=True)
    (BASE/'EC49FCJ_DIRECT_TUPLE_CROSSCHECK.json').write_text(
        json.dumps({'sample_count':len(INDEX),'rows':checked},indent=2)+'\n')
    print('SAMPLES_OK',len(INDEX),flush=True)
if __name__=='__main__':main()
