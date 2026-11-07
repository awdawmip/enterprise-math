"""Exact frozen-schedule five-slot search: 4 H4-H6 slots + 1 H8/H9 slot.
Uses EC49FCF frozen_model.py Git blob d262d4a06da862823cce2e34684a59bb081f20c2.
Scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from __future__ import annotations
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FCF_EARLY1_LATE3_150'))
from frozen_model import build
from itertools import combinations
from time import perf_counter
import argparse,json,hashlib

PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
B=158

def exact(slots,pools,single):
    fixed=0
    for key,bit in single.items():
        if key not in slots: fixed|=bit
    n=fixed.bit_count(); cutoff=B-n
    entries=[]; raw=1
    for slot in slots:
        wordmasks=pools[slot]
        raw*=len(wordmasks)
        residuals={x&~fixed for x in wordmasks}
        allowed=[x for x in residuals if x.bit_count()<cutoff]
        allowed.sort(key=lambda x:(x.bit_count(),x))
        entries.append((slot,allowed,len(residuals)))
    entries.sort(key=lambda e:(len(e[1]),sum(x.bit_count() for x in e[1])))
    states={0}; counts=[]
    for _,v,_ in entries:
        states={x|y for x in states for y in v if (x|y).bit_count()<cutoff}
        counts.append(len(states))
        if not states: break
    minimum=min([B]+[n+z.bit_count() for z in states])
    return dict(slots=list(slots),fixed=n,strict_cutoff=cutoff,
        raw=raw,ordering=[k for k,_,_ in entries],
        distinct_residual_counts=[z for _,_,z in entries],
        allowed_residual_counts=[len(v) for _,v,_ in entries],
        state_counts=counts,minimum=minimum)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--late',type=int,choices=[8,9],required=True)
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--stop',type=int)
    args=p.parse_args(); t=perf_counter()
    chosen,early,late,pools,single=build()
    assert len(chosen)==24 and len(early)==10
    latekeys=[k for k in late if k.startswith(str(args.late)+':')]
    groups=[(*e,l) for e in combinations(early,4) for l in latekeys]
    assert len(groups)==(840 if args.late==8 else 420)
    stop=len(groups) if args.stop is None else args.stop
    assert 0<=args.start<stop<=len(groups)
    rows=[]
    for i in range(args.start,stop):
        rows.append(exact(groups[i],pools,single))
        if (i+1)%100==0:
            print('PROGRESS',args.late,i+1,'elapsed',round(perf_counter()-t,2),flush=True)
    canonical=json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    summary={
        'schema':'EC49FCI_EARLY4_H8H9_EXACT_V1','frozen_pin':PIN,
        'fixed_source_blob_sha1':'d262d4a06da862823cce2e34684a59bb081f20c2',
        'late_h':args.late,'range':[args.start,stop],'groups':len(rows),
        'raw_product_total':sum(r['raw'] for r in rows),
        'all_rigid':all(r['minimum']==B for r in rows),
        'minimum':min(r['minimum'] for r in rows),
        'max_state_count':max(max(r['state_counts'],default=0) for r in rows),
        'termination_stage_histogram':{str(s):sum(len(r['state_counts'])==s and r['state_counts'][-1]==0 for r in rows) for s in range(1,6)},
        'full_rows_sha256':hashlib.sha256(canonical).hexdigest(),
        'elapsed_s':round(perf_counter()-t,4)
    }
    outdir=Path(__file__).resolve().parent
    (outdir/f'EC49FCI_H{args.late}_{args.start}_{stop}.json').write_text(
        json.dumps({'summary':summary,'rows':rows},indent=2,ensure_ascii=False)+'\n')
    print('COMPLETE',json.dumps(summary,sort_keys=True),flush=True)
if __name__=='__main__': main()
