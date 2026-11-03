#!/usr/bin/env python3
"""Exact H7 finite prefix-tree screen at 86-edge cutoff for H8 M4/S<=6.
Every complete low-cost H7 configuration (<86) is retained exactly; an
INFEASIBLE below 86 is a rigorous bound, using nonnegative integer edge costs.
"""
from SCREEN_H5_EC49EXJ import schedules, build_input, HERE
from collections import Counter
import json,subprocess,re,time

def mkdict(source,key):
    return {tuple((tuple(q[0]),q[1]) for q in e['key_family']):e[key] for e in source['per_prefix_exact_results'].values()}

def main():
    start=time.monotonic(); j5=json.loads((HERE/'EC49EXJ_H5_EXECUTED.json').read_text());j6=json.loads((HERE/'EC49EXJ_H6_EXECUTED.json').read_text())
    e5=mkdict(j5,'E5');e6=mkdict(j6,'E6')
    ss=[s for s in schedules() if e5[s[:4]]+sum(2*t for k,t in s[4:])<90 and e6[s[:5]]+sum(2*t for k,t in s[5:])<90]
    assert len(ss)==536
    pref=sorted({s[:6] for s in ss})
    print('H7 bounded DP instances',len(pref),flush=True)
    e7={};rows={}
    for i,p in enumerate(pref):
        inp,nn,nw=build_input(p)
        proc=subprocess.run([str(HERE/'exact_dp'),'86'],input=inp,encoding='utf-8',capture_output=True,timeout=60)
        if proc.returncode!=0:raise RuntimeError((p,proc.returncode,proc.stdout,proc.stderr))
        m=re.search(r'total=(\d+)',proc.stdout)
        if m:
            v=int(m.group(1));assert v<86
        else:
            assert 'minimum_total_at_least=86' in proc.stdout,proc.stdout
            v=86
        e7[p]=v
        rows[str(i)]={'key_family':[[list(k),t] for k,t in p],
                      'E7_exact_if_less_than_86_otherwise_lower_bound':v,
                      'E7_is_exact':bool(m),
                      'nodes':nn, 'eligible_words':nw, 'solver_output':proc.stdout.strip()}
        if (i+1)%100==0:print('H7 progress',i+1,'/',len(pref), 'seconds',round(time.monotonic()-start,1),flush=True)
    screened=[s for s in ss if e7[s[:6]]+2*s[6][1]>=90]
    final=[s for s in ss if e7[s[:6]]+2*s[6][1]<90]
    out={'status':'PASS', 'H5_screened':j5['screened_by_H5_bound'], 'H6_additional_screened':j6['H6_screened_additional'],
         'H7_tested_schedules':len(ss),'H7_unique_prefixes':len(pref),
         'H7_additional_screened':len(screened),'H7_residual_schedules':len(final),
         'total_screened':j5['screened_by_H5_bound']+j6['H6_screened_additional']+len(screened),
         'h7_exact_under_cutoff':sum(v<86 for v in e7.values()),
         'h7_at_least_cutoff':sum(v==86 for v in e7.values()),
         'H7_residual_costs':sorted(Counter((e7[s[:6]],s[6][1]) for s in final).items()),
         'per_prefix_exact_results':rows,
         'H7_residual_cases':[[[list(k),t] for k,t in s] for s in final],
         'elapsed_seconds':round(time.monotonic()-start,2)}
    (HERE/'EC49EXJ_H7_EXECUTED.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','H7_tested_schedules','H7_unique_prefixes','H7_additional_screened','H7_residual_schedules','total_screened','h7_exact_under_cutoff','h7_at_least_cutoff','H7_residual_costs','elapsed_seconds')},indent=2))
if __name__=='__main__':main()
