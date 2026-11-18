#!/usr/bin/env python3
"""Verify 24 R5 nine-state endpoint certificates. Needs frozen EXACT_R5_ALL_101_BUDGETS.json
with SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
and this folder's RESULTS_AFTER40.csv. Optional --solve recompiles and solves exact Bellman.
The full 2026-class partition and class IDs have a separate exhaustive predecessor proof.
"""
import csv, hashlib, json, re, subprocess, sys
from pathlib import Path
P=Path(__file__).resolve().parent
PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
U=58182461585441404127941754880
def maximal(ms):
 s=set(ms)
 return tuple(sorted(m for m in s if not any(m!=v and (m&v)==m for v in s)))
def windows(c,t):
 return maximal(sum(1<<i for i,x in enumerate(c) if z<=x<=z+t) for z in c)
def sweep(c,t):
 endpoints=sorted(set(v for x in c for v in (2*x-t,2*x+t)))
 ms=[sum(1<<i for i,x in enumerate(c) if abs(z-2*x)<=t) for z in endpoints]
 ms += [sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*t)
        for a,b in zip(endpoints,endpoints[1:])]
 return maximal(ms)
def input_for(D,x,y):
 H=(18,24,82,34,17,x,144,208,y)
 families={}
 for k in range(214,315):
  c=[int(D[str(k)]['counts'][h]) for h in H]
  ss=windows(c,U-1)
  if ss not in families or k<families[ss]:families[ss]=k
 actions=sorted((k,s) for s,k in families.items())
 lines=['9 8',str(len(actions))]
 for k,s in actions:lines.append(' '.join(map(str,[k,len(s),*s])))
 return ('\n'.join(lines)+'\n').encode(),len(actions)
def main():
 raw=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()==PIN
 D=json.loads(raw)['counts_and_cohorts'];assert len(D)==101
 rows=list(csv.DictReader((P/'RESULTS_NEXT24.csv').open()))
 assert len(rows)==24 and len({r['group_id'] for r in rows})==24
 assert sum(int(r['size']) for r in rows)==1717
 if '--solve' in sys.argv:
  subprocess.run(['g++','-std=c++17','-O3','EXACT_NINE.cpp','-o','exact_nine'],cwd=P,check=True)
 count=0
 for r in rows:
  x,y=int(r['x']),int(r['y'])
  H=(18,24,82,34,17,x,144,208,y)
  assert len(set(H))==9 and x<y
  for k in range(214,315):
   centers=[int(D[str(k)]['counts'][h]) for h in H]
   assert windows(centers,U-1)==sweep(centers,U-1)
   count+=1
  inp,nact=input_for(D,x,y)
  assert hashlib.sha256(inp).hexdigest()==r['input_sha256']
  assert nact==int(r['action_families'])
  assert int(r['exact_cost'])==8335 and int(r['memo_states'])>0
  if '--solve' in sys.argv:
   proc=subprocess.run([str(P/'exact_nine')],input=inp,capture_output=True,cwd=P,check=True)
   m=re.fullmatch(r'EXACT cost=(\d+) states=(\d+) actions=(\d+) time=[0-9.]+',
                  proc.stdout.decode().strip())
   assert m and list(map(int,m.groups()))==[8335,int(r['memo_states']),nact]
 assert count==2424
 print('PASS_R5_NINE_AFTER40 classes=24 new_pairs=1717 cumulative_classes=110 cumulative_pairs=15203 supports_checked=2424')
if __name__=='__main__':main()
