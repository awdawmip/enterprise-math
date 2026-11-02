#!/usr/bin/env python3
"""Exact six-horizon lower-bound screening of 7-horizon 4-key 4-matrix schedules."""
import EC49EW_S4_SEARCH as a
import json,subprocess,time,re
from pathlib import Path
from MODEL_EC49EU import BASE,P0,PAID_BASE,path,T4
ROOT=Path(__file__).parent
ss=list(a.schedules()); prefixes=sorted({s[:5] for s in ss});assert len(ss)==752
print('H7 schedules',len(ss),'distinct H6 prefixes',len(prefixes),flush=True)
def six_trie(ps):
 node={():0};parent=[-1];paid=[1];masks=[0]
 def insert(seq,mask=0):
  pre=()
  for step in seq:
   nxt=pre+(step,)
   if nxt not in node:
    node[nxt]=len(node);parent.append(node[pre]);paid.append(int(nxt in PAID_BASE));masks.append(0)
   pre=nxt
  masks[node[pre]]|=mask
 for w in BASE:insert(path(w))
 for h in range(3,7):
  for k,s in enumerate(a.SIG):
   bit=1<<((h-3)*4+k)
   for w,seq in a.KEYWORDS[(h,ps[h-2])][s]:insert(seq,bit)
 N=len(node);K=16
 return f'{N} {K}\n'+''.join(f'{parent[i]} {paid[i]} {masks[i]}\n' for i in range(N)),N
exe=ROOT/'ec49ew_dp';rows={};t=time.monotonic()
for i,ps in enumerate(prefixes):
 data,n=six_trie(ps)
 r=subprocess.run([str(exe)],input=data,capture_output=True,text=True,check=True)
 mm=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',r.stdout.strip());assert mm
 extra,total,nodes,colors,largest,conv=map(int,mm.groups());assert total==28+extra and nodes==n and colors==16
 rows[ps]=total
 if i%50==0:print('H6 DP',i,'/',len(prefixes),'seconds',round(time.monotonic()-t,3),flush=True)
summary={'h7_4key_4sig_schedules':len(ss),'distinct_h6_prefix_schedules':len(prefixes),'h6_exact_costs':{str(e):sum(v==e for v in rows.values()) for e in sorted(set(rows.values()))},'h7_screen_by_h6plus4':{str(cap):sum(rows[s[:5]]+4<=cap for s in ss) for cap in [76,80,84,88,90,92]},'minimum_h6':min(rows.values()),'minimum_h6_reusable_p7':min(rows[s[:5]] for s in ss),'runs':len(rows),'time_seconds':round(time.monotonic()-t,3)}
(ROOT/'EC49EW_H6_PREFIX_SCREEN_EXECUTED.json').write_text(json.dumps(summary,indent=2)+'\n')
print('SUMMARY',json.dumps(summary,indent=2))
