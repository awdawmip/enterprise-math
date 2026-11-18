#!/usr/bin/env python3
"""Exact h6 predecessor-prefix screen after sound h5 bound for EC49EXJ.
Computation is exhaustive over current 4-key-by-h7 H8 family assignments.
"""
from SCREEN_H5_EC49EXJ import schedules, build_input, HERE
from collections import Counter
from pathlib import Path
import json,subprocess,re,time

def main():
    t0=time.monotonic();ss=schedules()
    old=json.loads((HERE/'EC49EXJ_H5_EXECUTED.json').read_text())
    e5={tuple((tuple(q[0]),q[1]) for q in e['key_family']):e['E5'] for e in old['per_prefix_exact_results'].values()}
    unscreened=[s for s in ss if e5[s[:4]]+sum(2*t for k,t in s[4:])<90]
    assert len(unscreened)==old['remaining_after_H5_bound']==4129
    h6prefixes=sorted({s[:5] for s in unscreened})
    print('H6 prefixes',len(h6prefixes),flush=True)
    e6={};rows={}
    for ix,p in enumerate(h6prefixes):
        inp,nn,nw=build_input(p)
        proc=subprocess.run([str(HERE/'exact_dp')],input=inp,encoding='utf-8',capture_output=True,timeout=60)
        if proc.returncode!=0:raise RuntimeError((p,proc.stdout,proc.stderr))
        m=re.search(r'total=(\d+)',proc.stdout); assert m,proc.stdout
        v=int(m.group(1));e6[p]=v
        rows[str(ix)]={'key_family':[[list(k),t] for k,t in p], 'E6':v,'nodes':nn,'eligible_words':nw, 'solver_output':proc.stdout.strip()}
        if (ix+1)%100==0:print('H6 progress',ix+1,'/',len(h6prefixes), 'seconds',round(time.monotonic()-t0,1),flush=True)
    remaining=[];screened=[];hist=Counter()
    for s in unscreened:
        lower=e6[s[:5]]+sum(2*t for k,t in s[5:])
        hist[lower]+=1
        (remaining if lower<90 else screened).append(s)
    out={'status':'PASS','M':4,'S_limit':6,'horizon':8,
         'H5_screened':old['screened_by_H5_bound'],
         'H6_input_schedules':len(unscreened),'H6_unique_prefixes':len(h6prefixes),
         'H6_screened_additional':len(screened),'remaining_after_H6':len(remaining),
         'combined_screened':old['screened_by_H5_bound']+len(screened),
         'remaining_H7_prefixes':len({s[:6] for s in remaining}),
         'H6_exact_range':[min(e6.values()),max(e6.values())],
         'bound_hist':dict(sorted(hist.items())),
         'per_prefix_exact_results':rows,
         'elapsed_seconds':round(time.monotonic()-t0,2),
         'first_remaining':None if not remaining else [[list(k),t] for k,t in remaining[0]]}
    dst=HERE/'EC49EXJ_H6_EXECUTED.json';dst.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','H5_screened','H6_unique_prefixes','H6_screened_additional','remaining_after_H6','combined_screened','remaining_H7_prefixes','H6_exact_range','elapsed_seconds')},indent=2))
if __name__=='__main__':main()
