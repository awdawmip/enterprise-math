#!/usr/bin/env python3
"""EC49FCM frozen model, early3+H8+H9 exact five-slot strict optimality search."""
import json,time,hashlib,argparse
from itertools import combinations
from pathlib import Path
from frozen_model import build
BOUND=158
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
def exact(slots,masks,single):
    sel=set(slots)
    fixed=0
    for key,mask in single.items():
        if key not in sel:fixed|=mask
    b=BOUND-fixed.bit_count()
    if b<=0:return {'slots':slots,'fixed_edges':fixed.bit_count(),'min':BOUND,'stage_counts':[0],'raw':0,'status':'fixed_bound'}
    entries=[];raw=1
    for k in slots:
        raw*=len(masks[k]);vals={m&~fixed for m in masks[k]}
        vals={v for v in vals if v.bit_count()<b}
        if not vals:return {'slots':slots,'fixed_edges':fixed.bit_count(),'min':BOUND,'stage_counts':[0],'raw':raw,'status':'no_eligible_slot'}
        entries.append((k,tuple(vals)))
    entries.sort(key=lambda kv:len(kv[1]))
    states={0};stages=[]
    for name,values in entries:
        states={v|m for v in values for m in states if (v|m).bit_count()<b}
        stages.append(len(states))
        if not states:break
    return {'slots':slots,'fixed_edges':fixed.bit_count(),'min':BOUND if not states else fixed.bit_count()+min(x.bit_count() for x in states),'stage_counts':stages,'raw':raw,'status':'exact'}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=48)
    ap.add_argument('--output',required=True)
    a=ap.parse_args();t=time.time()
    chosen,early,late,masks,single=build()
    h8=[x for x in late if x.startswith('8:')]
    h9=[x for x in late if x.startswith('9:')]
    qs=[(*e,x,y) for e in combinations(early,3) for x in h8 for y in h9]
    assert len(qs)==960 and 0<=a.start<a.stop<=960
    rows=[]
    for i in range(a.start,a.stop):
        row=exact(qs[i],masks,single);row['index']=i;rows.append(row)
        if (i+1)%40==0:print('progress',i+1,round(time.time()-t,2),flush=True)
    summary={'schema':'EC49FCM_EARLY3_H8H9_EXACT_V1','science_pin':PIN,
     'groups_total':960,'indices':[a.start,a.stop],'checked':len(rows),
     'minima':sorted(set(r['min'] for r in rows)),
     'strict_improvements':sum(r['min']<158 for r in rows),
     'max_states':max(max(r['stage_counts']) for r in rows),
     'candidate_cartesian_total':str(sum(r['raw'] for r in rows)),
     'seconds':round(time.time()-t,3)}
    s=json.dumps({'summary':summary,'rows':rows},ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'
    Path(a.output).write_text(s)
    summary['rows_sha256']=hashlib.sha256(s.encode()).hexdigest()
    print(json.dumps(summary,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=='__main__':main()
