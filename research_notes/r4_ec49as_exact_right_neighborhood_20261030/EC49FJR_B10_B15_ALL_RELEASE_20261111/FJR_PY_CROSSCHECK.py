from ec49fjd_shared import *
from pathlib import Path
from collections import Counter
import json,sys,time
P=Path(__file__).parent

def antichain(xs):
 out=[]
 for m in sorted(set(xs),key=lambda x:(x.bit_count(),x)):
  if not any((s&m)==s for s in out):out.append(m)
 return out

def run(v):
 profile,Q,labels,allowed,full=v
 F=frozenset(bytes.fromhex(x) for x in full.split(';'))
 budget=93-len(F)
 KEYSETS=[frozenset(tuple(map(int,k.split(','))) for k in ks.split(';')) for ks in allowed.split('|')]
 parsed=[tuple(map(int,lab.split(','))) for lab in labels.split(';')]
 best=budget+1
 for allowed_keys in KEYSETS:
  allopts=[]
  for label in parsed:
   options=[]
   for k in allowed_keys:
    for word in bykey[k][label]:
     new=frozenset(pref(word))-F
     if len(new)<=budget:options.append(new)
   options=list(set(options));options.sort(key=len)
   opts=[]
   for f in options:
    if not any(s.issubset(f) for s in opts):opts.append(f)
   allopts.append(opts)
  if not all(allopts):continue
  universe={p for opts in allopts for o in opts for p in o}
  ix={p:i for i,p in enumerate(sorted(universe))}
  masks=[[sum(1<<ix[p] for p in o) for o in opts] for opts in allopts]
  masks.sort(key=len)
  states=[0]
  for mi in masks:
   nxt=[]
   for s in states:
    for m in mi:
     u=s|m
     if u.bit_count()<=budget:nxt.append(u)
   states=antichain(nxt)
   if not states:break
  if states:best=min(best,min(s.bit_count() for s in states))
 return best

def main():
 global bykey
 bykey=globals()['bykey']
 rows=(P/'FJR_CASES.tsv').read_text().splitlines()
 samples=[(a,tuple(map(int,r.split('\t')[1].split(','))),r) for a,r in enumerate(rows) if r.split('\t')[1] in ['0,1,2,3,8,22','0,1,2,3,9,23','0,1,2,3,22,23']]
 print('SAMPLES',len(samples),flush=True)
 for i,q,row in samples:
  st=time.time();res=run(row.split('\t'));print('PYTHON_EXACT',i,q,res,round(time.time()-st,2),flush=True)
if __name__=='__main__':main()
