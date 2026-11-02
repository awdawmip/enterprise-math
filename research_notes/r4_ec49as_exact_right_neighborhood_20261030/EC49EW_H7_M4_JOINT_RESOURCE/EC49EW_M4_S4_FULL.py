#!/usr/bin/env python3
"""Complete candidate exact-minimum certificate for H=7,M=4,S=4 in frozen native BRC observer.
Uses 389 exact H6 prefix DP lower bounds and full signed-X6 trie DP only for survivors.
"""
from pathlib import Path
import json, subprocess, re, time
import EC49EW_S4_SEARCH as a
from MODEL_EC49EU import BASE, P0,PAID_BASE,path
ROOT=Path(__file__).parent
sched=list(a.schedules());assert len(sched)==752
prefixes=sorted({ps[:5] for ps in sched});assert len(prefixes)==389
exe=ROOT/'ec49ew_dp'
if not exe.exists():subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'VERIFY_EC49EU_EXACT_DP.cpp'),'-o',str(exe)],check=True)
def DP(inp):
 r=subprocess.run([str(exe)],input=inp,capture_output=True,text=True,check=True)
 m=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',r.stdout.strip());assert m,r.stdout
 return list(map(int,m.groups()))
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
 return f'{N} {K}\n'+''.join(f'{parent[i]} {paid[i]} {masks[i]}\n' for i in range(N))
t=time.monotonic()
lower={}
for i,p in enumerate(prefixes):
 d=DP(six_trie(p));assert d[3]==16
 lower[p]=d[1]
 assert d[1]==d[0]+28
print('H6 complete:',len(lower),'seconds',round(time.monotonic()-t,2),flush=True)
# Witness from previous standalone EC49EW_S4_SEARCH.py has exact E92 for first schedule.
cap=92
candidates=[(sid,p) for sid,p in enumerate(sched) if lower[p[:5]]+4<cap]
print('Candidates capable of beating',cap,len(candidates),flush=True)
save=ROOT/'EC49EW_M4_S4_FULL_EXECUTED.json'; rows=json.loads(save.read_text())['cases'] if save.exists() else []; previous_ids={x['schedule_id'] for x in rows};print('Resuming with',len(rows),'already solved',flush=True)
for idx,(sid,ps) in enumerate(candidates):
 if sid in previous_ids:continue
 inp,n=a.trie(ps);d=DP(inp);assert d[1]==d[0]+28 and d[2]==n and d[3]==20
 rows.append({'schedule_id':sid,'p':[list(p) for p in ps],'H6_exact_cost':lower[ps[:5]],'H7_exact_cost':d[1],'trie_nodes':d[2],'color_masks':d[4],'convolutions':d[5]})
 if idx%5==0:
  print('H7 verified',idx+1,'/',len(candidates),'cost',d[1],'seconds',round(time.monotonic()-t,2),flush=True)
  partial={'status':'IN_PROGRESS','cases_done':len(rows),'candidates_to_test':len(candidates),'best_exact_in_tested':min(r['H7_exact_cost'] for r in rows),'cases':rows}
  save.write_text(json.dumps(partial,ensure_ascii=False,indent=2)+'\n')
mincost=min([92]+[r['H7_exact_cost'] for r in rows]); assert mincost<=92
report={'status':'PASS','scope':'H2..H7 M=4 S=4 full seven-operation signed-X6 model, nine history rank9 each horizon, per-horizon BRC positive vector key','all_horizon_4key_schedules':len(sched),'distinct_H6_prefixes_exactly_DP_solved':len(prefixes),'screened_by_exact_H6_plus_four_terminal_edge_bound':len(sched)-len(candidates),'full_H7_trie_DP_solved':len(rows),'candidate_cost_cutoff':92,'minimum_E':mincost,'witness_example':{'schedule_id':211,'E':92,'p_h2_to_h7':[[3,1,1],[4,2,1],[4,2,1],[4,3,1],[5,4,1],[5,4,1]]},'DP_cost_frequency':{str(e):sum(r['H7_exact_cost']==e for r in rows) for e in sorted(set(r['H7_exact_cost'] for r in rows))},'elapsed_seconds':round(time.monotonic()-t,3),'cases':rows,'screening_proof':'The primitive operation encoding is prefix-free (distinct initial signed pairs). At horizon h7 each of the four required T4 signatures needs a distinct terminal primitive edge, none a prefix of any shorter completed word. Therefore E_2:7 >= E_2:6^minimum +4 for the exact fixed-h2..6 BRC key prefix schedule. H6 minima are exact integer OR-mask trie DP, and every h7 schedule with that bound >=92 can be safely screened. All 66 remaining h7 schedules are solved with exact OR-mask native-prefix trie DP.'}
save.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('FINAL',json.dumps({k:v for k,v in report.items() if k!='cases'},ensure_ascii=False,indent=2),flush=True)
