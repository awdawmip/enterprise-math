#!/usr/bin/env python3
"""EC49FCJ exact signed-native X6 BRC prefix cardinality, frozen source pin.
Example: python VERIFY_EC49FCJ.py --latepair 7,9 --start 0 --stop 40 --output out.json
"""
import json, argparse, hashlib, time
from itertools import combinations
from pathlib import Path
from frozen_model import build
BOUND=158
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def exact(slots,pools,single):
    selected=set(slots)
    fixed=0
    for name,mask in single.items():
        if name not in selected: fixed|=mask
    fixed_size=fixed.bit_count()
    strict_capacity=BOUND-fixed_size
    entries=[]; raw=1
    for k in slots:
        raw*=len(pools[k])
        residues={m & ~fixed for m in pools[k]}
        vals=sorted((r for r in residues if r.bit_count()<strict_capacity),
                    key=lambda x:(x.bit_count(),x))
        entries.append((k,vals,len(residues)))
    entries.sort(key=lambda v:(len(v[1]),sum(m.bit_count() for m in v[1])))
    states={0}; stage_counts=[]
    for _,values,_ in entries:
        if not values: states=set()
        else:
            states={x|v for x in states for v in values
                    if (x|v).bit_count()<strict_capacity}
        stage_counts.append(len(states))
        if not states: break
    best=fixed_size+min(s.bit_count() for s in states) if states else BOUND
    assert best<=BOUND
    return {'slots':list(slots),'fixed_edges':fixed_size,
            'strict_capacity':strict_capacity,'candidate_cartesian':raw,
            'order':[a for a,_,_ in entries],
            'distinct_residual_counts':[n for _,_,n in entries],
            'eligible_residual_counts':[len(v) for _,v,_ in entries],
            'stage_counts':stage_counts,'minimum':best}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--latepair',default='7,9',
                    choices=['7,7','7,8','7,9','8,8','8,9','9,9'])
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=None)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); start=time.perf_counter()
    chosen,early,late,pools,single=build()
    a,b=map(int,args.latepair.split(','))
    A=[v for v in late if v.startswith(str(a)+':')]
    B=[v for v in late if v.startswith(str(b)+':')]
    late_pairs=list(combinations(A,2)) if a==b else [(x,y) for x in A for y in B]
    slots=[(*es,*ls) for es in combinations(early,3) for ls in late_pairs]
    stop=len(slots) if args.stop is None else args.stop
    assert 0<=args.start<stop<=len(slots)
    rows=[]
    for i in range(args.start,stop):
        rows.append(exact(slots[i],pools,single))
        if (i-args.start+1)%20==0:
            print('PROGRESS',args.latepair,i+1,'of',len(slots),
                  'seconds',round(time.perf_counter()-start,2),flush=True)
    v=json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    summary={'schema':'EC49FCJ_FIVE_SLOT_DP_V1','science_pin':PIN,
       'source':'EC49FCF_EARLY1_LATE3_150/frozen_model.py',
       'latepair':args.latepair,'range':[args.start,stop],
       'available_groups':len(slots),'groups_computed':len(rows),
       'minimum':min(x['minimum'] for x in rows),
       'max_state_count':max(max(x['stage_counts']) for x in rows),
       'strict_improvement_groups':sum(x['minimum']<BOUND for x in rows),
       'candidate_cartesian_total':sum(x['candidate_cartesian'] for x in rows),
       'rows_sha256':hashlib.sha256(v).hexdigest(),
       'elapsed_s':round(time.perf_counter()-start,3)}
    Path(args.output).write_text(json.dumps({'summary':summary,'rows':rows},
                                     indent=2,ensure_ascii=False)+'\n')
    print('COMPLETE',json.dumps(summary,sort_keys=True),flush=True)
if __name__=='__main__': main()
