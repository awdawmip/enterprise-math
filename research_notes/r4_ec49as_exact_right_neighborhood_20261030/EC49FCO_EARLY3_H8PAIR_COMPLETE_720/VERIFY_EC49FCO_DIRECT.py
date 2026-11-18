#!/usr/bin/env python3
"""Exact five-slot local rigidity via full residual signed-prefix sets.
The evidence is exhaustive for each selected group; no antichain reduction is needed.
"""
import json,hashlib,argparse,time
from itertools import combinations
from frozen_model import build,REQ
SCIENCE_PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def check(slots,pools,default):
    selected=set(slots);fixed=0
    for key,val in default.items():
        if key not in selected:fixed|=val
    fixed_edges=fixed.bit_count();capacity=158-fixed_edges
    raw_cartesian=1
    for key in slots:raw_cartesian*=len(pools[key])
    early=[]
    for key in slots[:3]:
        early.append({m&~fixed for m in pools[key] if (m&~fixed).bit_count()<capacity})
    # All possible early-three residual unions below the improvement threshold.
    triples={a|b|c for a in early[0] for b in early[1] for c in early[2] if (a|b|c).bit_count()<capacity}
    late_a={m&~fixed for m in pools[slots[3]] if (m&~fixed).bit_count()<capacity}
    late_b={m&~fixed for m in pools[slots[4]] if (m&~fixed).bit_count()<capacity}
    checks=0; possible_witness=None
    for e in triples:
        for a in late_a:
            ea=e|a
            if ea.bit_count()>=capacity:continue
            for b in late_b:
                checks+=1
                v=ea|b
                if v.bit_count()<capacity:
                    possible_witness=v.bit_count();break
            if possible_witness is not None:break
        if possible_witness is not None:break
    return {'slots':list(slots), 'fixed_edges':fixed_edges,
            'minimum':158 if possible_witness is None else fixed_edges+possible_witness,
            'strict_improvement_exists': possible_witness is not None,
            'early_triple_residual_count':len(triples),'late_counts':[len(late_a),len(late_b)],
            'last_stage_union_checks':checks,'raw_cartesian':str(raw_cartesian)}

def main(start,stop,out):
    t=time.monotonic(); chosen,early,late,pools,defaults=build()
    h8=[key for key in late if key.startswith('8:')]
    groups=[(*e,*b) for e in combinations(early,3) for b in combinations(h8,2)]
    assert len(groups)==720 and len(chosen)==24 and len(h8)==4
    rows=[]
    for i in range(start,stop):
        x=check(groups[i],pools,defaults);x['index']=i; rows.append(x)
        if (i+1)%60==0:print('PROGRESS',i+1,'seconds',round(time.monotonic()-t,3),flush=True)
    summ={'schema':'EC49FCO_EXACT_DIRECT_FIVE_PATH_V1','pin':SCIENCE_PIN, 'family':'early3_H8pair', 'groups_total':720, 'range':[start,stop], 'groups_checked':len(rows), 'strict_improvements':sum(x['strict_improvement_exists'] for x in rows),'observed_minima':sorted(set(x['minimum'] for x in rows)), 'raw_cartesian_total':str(sum(int(x['raw_cartesian']) for x in rows)), 'total_last_stage_union_checks':sum(x['last_stage_union_checks'] for x in rows), 'max_early_triple_residuals':max(x['early_triple_residual_count'] for x in rows), 'seconds':round(time.monotonic()-t,3)}
    b=(json.dumps({'summary':summ,'rows':rows},ensure_ascii=False,separators=(',',':'),sort_keys=True)+'\n').encode()
    open(out,'wb').write(b)
    print('SUMMARY',json.dumps({**summ,'sha256':hashlib.sha256(b).hexdigest()},sort_keys=True),flush=True)
    return summ
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=720);ap.add_argument('--output',required=True);a=ap.parse_args();main(a.start,a.stop,a.output)
