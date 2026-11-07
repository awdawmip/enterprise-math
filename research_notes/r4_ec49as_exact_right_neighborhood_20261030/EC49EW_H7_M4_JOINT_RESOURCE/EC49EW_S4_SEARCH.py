#!/usr/bin/env python3
"""Exploratory exact seven-window BRC prefix resource optimization for M=4,S=4.
Finite complete fibers and full signed native paths from immutable EC49EU mathematical model.
"""
import json,subprocess,itertools,sys,time,re
from collections import defaultdict
from pathlib import Path
from MODEL_EC49EU import BASE,P0,PAID_BASE,T4,T2,words,signature,path,T4_fibers,rank_mod
ROOT=Path(__file__).parent
ALL={h:list(T4_fibers(h)) for h in range(2,8)}
SIG=sorted(T4)
# Precompute eligible words and paths for every horizon/p/sig
KEYWORDS={}
for h in range(2,8):
 for p in ALL[h]:
  ws=defaultdict(list)
  for w in words(h,p):
   s=signature(w)
   if s in T4:ws[s].append((w,path(w)))
  assert all(ws[s] for s in SIG)
  KEYWORDS[(h,p)]=ws

def schedules():
 for ps in itertools.product(*(ALL[h] for h in range(3,8))):
  if len(set((P0,)+ps))==4:yield (P0,)+ps

def trie(ps):
 node={():0}; parent=[-1];paid=[1];masks=[0]
 def insert(sequence,mask=0):
  pre=()
  for step in sequence:
   nxt=pre+(step,)
   if nxt not in node:
    node[nxt]=len(node);parent.append(node[pre]);paid.append(int(nxt in PAID_BASE));masks.append(0)
   pre=nxt
  masks[node[pre]]|=mask
 for w in BASE:insert(path(w))
 for h in range(3,8):
  for k,s in enumerate(SIG):
   bit=1<<((h-3)*4+k)
   for w,seq in KEYWORDS[(h,ps[h-2])][s]:insert(seq,bit)
 N=len(node);K=20
 data=f'{N} {K}\n'+''.join(f'{parent[i]} {paid[i]} {masks[i]}\n' for i in range(N))
 return data,N

def greedy(ps):
 # Each horizon has to select one per signature; greedily choose minimum added native prefix edges.
 selected=[(w,path(w)) for w in BASE]
 paid=set(PAID_BASE)
 for h in range(3,8):
  pending=[(h,s) for s in SIG]
  while pending:
   choices=[]
   for _,s in pending:
    for w,seq in KEYWORDS[(h,ps[h-2])][s]:
     cost=sum(seq[:i] not in paid for i in range(1,len(seq)+1))
     choices.append((cost,len(seq),w,s,seq))
   cost,ln,w,s,seq=min(choices)
   selected.append((w,seq));paid.update(seq[:i] for i in range(1,len(seq)+1));pending.remove((h,s))
 return len(paid),[w for w,_ in selected]

def main():
 ss=list(schedules()); assert len(ss)==752,len(ss)
 rough=[]
 start=time.monotonic()
 for sid,ps in enumerate(ss):
  e,ws=greedy(ps);rough.append((e,sid,ps,ws))
 print('schedule_count',len(ss),'greedy min',min(x[0] for x in rough),'greedy_seconds',time.monotonic()-start,flush=True)
 rough.sort()
 for e,sid,ps,ws in rough[:12]:print('GREEDY',e,sid,[p[:3] for p in ps],ws,flush=True)
 # Exact solver limited to first N lowest greedy candidates for initial feasibility; can extend later.
 limit=int(sys.argv[1]) if len(sys.argv)>1 else 10
 exe=ROOT/'ec49ew_dp'; subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'VERIFY_EC49EU_EXACT_DP.cpp'),'-o',str(exe)],check=True)
 best=999;results=[]
 for e,sid,ps,ws in rough[:limit]:
  data,N=trie(ps);t=time.monotonic()
  res=subprocess.run([str(exe)],input=data,text=True,capture_output=True,check=True)
  mm=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',res.stdout.strip());assert mm,res.stdout
  d,total,n,k,states,conv=map(int,mm.groups());assert k==20 and total==d+28
  best=min(best,total);result={'schedule_id':sid,'p':[p[:3] for p in ps],'E_exact':total,'nodes':n,'color_masks':states,'convolutions':conv,'time_seconds':round(time.monotonic()-t,3),'greedy_cost':e,'greedy_words':ws}
  results.append(result)
  print('EXACT',result,flush=True)
 (ROOT/'EC49EW_S4_INITIAL.json').write_text(json.dumps({'status':'PARTIAL_EXACT','model':'EC49EU frozen','all_four_key_schedules':len(ss),'exact_schedules_done':len(results),'best_exact_case':min(results,key=lambda x:x['E_exact']) if results else None,'cases':results},ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
