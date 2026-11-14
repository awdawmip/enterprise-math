#!/usr/bin/env python3
"""EC49FCK exact signed-native X6 5-slot DP, same algorithm run on local 240 groups."""
import sys, json, argparse, hashlib, time
from itertools import combinations
from pathlib import Path
from frozen_model import build
BOUND=158
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
def exact(slots,pools,single):
    selected=set(slots)
    fixed=0
    for name,mask in single.items():
        if name not in selected: fixed |= mask
    fixed_size=fixed.bit_count()
    strict_capacity=BOUND-fixed_size
    entries=[]; raw=1
    for k in slots:
        raw*=len(pools[k])
        residues={m & ~fixed for m in pools[k]}
        vals=sorted((r for r in residues if r.bit_count()<strict_capacity),key=lambda x:(x.bit_count(),x))
        entries.append((k,vals,len(residues)))
    entries.sort(key=lambda v:(len(v[1]),sum(m.bit_count() for m in v[1])))
    states={0};stage_counts=[]
    for _,values,_ in entries:
        if not values: states=set()
        else: states={x|v for x in states for v in values if (x|v).bit_count()<strict_capacity}
        stage_counts.append(len(states))
        if not states: break
    best=(fixed_size+min(s.bit_count() for s in states)) if states else BOUND
    assert best<=BOUND
    return {'slots':list(slots),'fixed_edges':fixed_size,'strict_capacity':strict_capacity,
      'candidate_cartesian':raw,'order':[x for x,_,_ in entries],
      'distinct_residual_counts':[n for _,_,n in entries],
      'eligible_residual_counts':[len(v) for _,v,_ in entries],
      'stage_counts':stage_counts,'minimum':best}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=240)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    t=time.perf_counter()
    chosen,early,late,pools,single=build()
    h7=[s for s in late if s.startswith('7:')]
    h8=[s for s in late if s.startswith('8:')]
    quintets=[(*e,x,y) for e in combinations(early,3) for x in h7 for y in h8]
    assert len(quintets)==1920
    assert 0<=a.start<a.stop<=len(quintets)
    rows=[exact(quintets[i],pools,single) for i in range(a.start,a.stop)]
    raw=json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    summary={'schema':'EC49FCK_EARLY3_H7H8_FIVE_DP_V1','science_pin':PIN,
      'source':'EC49FCJ_EARLY3_H7H9_960/frozen_model.py (immutable Git blob c21336...)',
      'range':[a.start,a.stop],'available_groups':len(quintets),
      'groups_computed':len(rows),'minimum':min(r['minimum'] for r in rows),
      'max_state_count':max(max(r['stage_counts']) for r in rows),
      'strict_improvement_groups':sum(r['minimum']<BOUND for r in rows),
      'candidate_cartesian_total':sum(r['candidate_cartesian'] for r in rows),
      'rows_sha256':hashlib.sha256(raw).hexdigest(),
      'elapsed_s':round(time.perf_counter()-t,3)}
    Path(a.output).write_text(json.dumps({'summary':summary,'rows':rows},indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
