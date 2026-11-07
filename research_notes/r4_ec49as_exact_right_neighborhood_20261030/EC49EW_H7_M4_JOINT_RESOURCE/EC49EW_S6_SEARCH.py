#!/usr/bin/env python3
"""H7 4 BRC cache keys and up to six global observer matrices, exact candidate enumeration, native path witnesses and selected case exact DP."""
import itertools,subprocess,re,time,json,sys
from pathlib import Path
from collections import defaultdict
from MODEL_EC49EU import BASE,P0,PAID_BASE,T4,T2,words,signature,path,T4_fibers,rank_mod
ROOT=Path(__file__).parent; TYPES={'4':sorted(T4),'2':sorted(T2)}
FIBERS={};FWORDS={}
for h in range(2,8):
 f={}
 for e in range(1,(h+2)//2+1):
  for p1 in range(2*h+1):
   for p2 in range(h+1):
    p=(p1,p2,e,0,0,0);ws=words(h,p)
    if not ws:continue
    bysig=defaultdict(list)
    for w in ws:
     s=signature(w)
     if s in T4 or s in T2:bysig[s].append((w,path(w)))
    typ='4' if all(s in bysig for s in T4) else ('2' if all(s in bysig for s in T2) else None)
    if typ:
     f[p]=typ; FWORDS[(h,p)]={s:bysig[s] for s in TYPES[typ]}
 FIBERS[h]=f
 print('H',h,'T4',sum(v=='4' for v in f.values()),'T2',sum(v=='2' for v in f.values()),flush=True)

def schedules():
 def rec(h,ps,used):
  if h==8:
   if len(used)==4:yield ps
   return
  for p in FIBERS[h]:
   if len(used|{p})<=4:yield from rec(h+1,ps+(p,),used|{p})
 yield from rec(3,(P0,),{P0})

def greedy(ps):
 paid=set(PAID_BASE); chosen={2:list(BASE)}
 for h in range(3,8):
  p=ps[h-2]; typ=FIBERS[h][p];todo=list(TYPES[typ]);chosen[h]=[]
  while todo:
   choices=[]
   for s in todo:
    for w,seq in FWORDS[(h,p)][s]:
     cost=sum(seq[:i] not in paid for i in range(1,len(seq)+1))
     choices.append((cost,len(seq),w,s,seq))
   cost,ln,w,s,seq=min(choices)
   chosen[h].append(w);todo.remove(s);paid.update(seq[:i] for i in range(1,len(seq)+1))
 return len(paid),chosen

def trie(ps):
 node={():0};parent=[-1];paid=[1];masks=[0]
 def insert(seq,bit=0):
  pre=()
  for step in seq:
   nxt=pre+(step,)
   if nxt not in node:
    node[nxt]=len(node);parent.append(node[pre]);paid.append(int(nxt in PAID_BASE));masks.append(0)
   pre=nxt
  masks[node[pre]]|=bit
 for w in BASE:insert(path(w))
 labels=[]
 for h in range(3,8):
  p=ps[h-2]
  for s in TYPES[FIBERS[h][p]]:labels.append((h,s))
 pos={entry:i for i,entry in enumerate(labels)}
 for h in range(3,8):
  p=ps[h-2]; sigs=TYPES[FIBERS[h][p]]
  for s in sigs:
   for w,seq in FWORDS[(h,p)][s]:insert(seq,1<<pos[(h,s)])
 N=len(node);K=len(labels)
 return f'{N} {K}\n'+''.join(f'{parent[i]} {paid[i]} {masks[i]}\n' for i in range(N)),N,K

def main():
 start=time.monotonic();all_ss=list(schedules());ss=[ps for ps in all_ss if sum(FIBERS[h][ps[h-2]]=='4' for h in range(3,8))<=2 and FIBERS[7][ps[5]]=='2'];print('schedule_count_filtered',len(ss),'out_of',len(all_ss),flush=True)
 rough=[]
 for sid,ps in enumerate(ss):
  e,chosen=greedy(ps);rough.append((e,sid,ps,chosen))
 rough.sort();print('greedy_seconds',time.monotonic()-start,'best',rough[0][0],flush=True)
 for e,sid,ps,ws in rough[:20]:print('GREEDY',e,sid,[p[:3] for p in ps], ''.join(FIBERS[h][ps[h-2]] for h in range(3,8)),ws,flush=True)
 limit=int(sys.argv[1]) if len(sys.argv)>1 else 10
 exe=ROOT/'ec49ew_dp';subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'VERIFY_EC49EU_EXACT_DP.cpp'),'-o',str(exe)],check=True)
 results=[]
 for e,sid,ps,ws in rough[:limit]:
  data,N,K=trie(ps);t=time.monotonic()
  r=subprocess.run([str(exe)],input=data,text=True,capture_output=True,check=True)
  mm=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',r.stdout.strip());assert mm,r.stdout
  d,total,n,k,states,conv=map(int,mm.groups());assert k==K and total==d+28
  result={'schedule_id':sid,'E_exact':total,'p':[p[:3] for p in ps],'types':''.join(FIBERS[h][ps[h-2]] for h in range(3,8)),'nodes':n,'colors':K,'largest_states':states,'convolutions':conv,'time_seconds':round(time.monotonic()-t,3),'greedy_E':e,'greedy_words':ws}
  results.append(result);print('EXACT',result,flush=True)
 report={'status':'PARTIAL_EXACT','model':'EC49EU frozen','all_M4_Sle6_schedules':len(ss),'exact_cases':len(results),'min_tested_case':min(results,key=lambda r:r['E_exact']) if results else None,'cases':results}
 (ROOT/'EC49EW_S6_INITIAL.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
