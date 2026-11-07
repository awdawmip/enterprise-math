"""EC49FCH: exact five-slot replacement search on frozen signed X6/BRC nine-window 158-edge witness.

Run: python VERIFY_EC49FCH.py --family six_earliest
     python VERIFY_EC49FCH.py --family early_five [--start 0 --stop 252]
Standard-library only; model is source-faithful frozen_model.py from EC49FCF.
"""
from __future__ import annotations
import sys
from pathlib import Path
sibling=Path(__file__).resolve().parent.parent/'EC49FCF_EARLY1_LATE3_150'
if sibling.exists():
    sys.path.insert(0,str(sibling))
from frozen_model import build
from itertools import combinations
from time import perf_counter
import argparse,json

PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BASELINE=158

def exact(slots,pools,single):
    assert len(slots)==5 and len(set(slots))==5
    fixed=0
    for key,bit in single.items():
        if key not in slots:fixed|=bit
    base=fixed.bit_count(); cut=BASELINE-base
    data=[]; raw=1
    for k in slots:
        raw*=len(pools[k])
        residual={b & ~fixed for b in pools[k]}
        valid=sorted((b for b in residual if b.bit_count()<cut),key=lambda b:(b.bit_count(),b))
        data.append((k,valid,len(residual)))
    # Minimize intermediate-state growth without changing the search domain.
    data.sort(key=lambda item:(len(item[1]),sum(b.bit_count() for b in item[1])))
    counts=[];state={0};strict_witness=None
    for depth,(k,valid,_) in enumerate(data,1):
        next_state=set()
        for prefix in state:
            for residual in valid:
                joined=prefix|residual
                if joined.bit_count()<cut:
                    next_state.add(joined)
        counts.append(len(next_state))
        state=next_state
        if not state:break
    if state:
        # If a strictly smaller cost is possible, this contains all exact completed residual unions.
        strict_witness=min(base+q.bit_count() for q in state)
    return {'slots':list(slots),'fixed_edges':base,'improvement_cut':cut,'candidate_product':raw,
            'ordering':[v[0] for v in data], 'valid_residual_counts':[len(v[1]) for v in data],
            'distinct_residual_counts':[v[2] for v in data], 'state_counts':counts,
            'strict_improvement_minimum':strict_witness,
            'minimum':min(BASELINE,strict_witness) if strict_witness is not None else BASELINE}

def main():
    a=argparse.ArgumentParser();a.add_argument('--family',choices=['six_earliest','early_five','early4_h7'],default='six_earliest')
    a.add_argument('--start',type=int,default=0);a.add_argument('--stop',type=int,default=None)
    args=a.parse_args(); t=perf_counter()
    chosen,early,late,pools,single=build()
    if args.family=='early4_h7':
        h7=[k for k in late if k.startswith('7:')]
        groups=[(*a,b) for a in combinations(early,4) for b in h7]
    else:
        keys=early[:6] if args.family=='six_earliest' else early
        groups=list(combinations(keys,5))
    stop=len(groups) if args.stop is None else args.stop
    assert 0<=args.start<stop<=len(groups)
    reports=[]
    for i in range(args.start,stop):
        row=exact(groups[i],pools,single)
        reports.append(row)
        if (i+1)%20==0: print('PROGRESS',i+1,'seconds',round(perf_counter()-t,2),flush=True)
    summary={'schema':'EC49FCH_EXACT_FIVE_SLOT_V1','family':args.family,'range':[args.start,stop],
             'frozen_pin':PIN,'witness':BASELINE,'groups':len(reports),
             'all_rigid':all(r['minimum']==BASELINE for r in reports),
             'minimum':min(r['minimum'] for r in reports),
             'raw_candidates':sum(r['candidate_product'] for r in reports),
             'elapsed_seconds':round(perf_counter()-t,3),'rows':reports}
    path=Path(__file__).with_name(f'EC49FCH_{args.family}_{args.start}_{stop}.json')
    with open(path,'w') as f:json.dump(summary,f,indent=2,sort_keys=True)
    print('COMPLETE',summary['groups'],'minimum',summary['minimum'],'total raw',summary['raw_candidates'],'time',summary['elapsed_seconds'],'output',path)

if __name__=='__main__': main()
