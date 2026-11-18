#!/usr/bin/env python3
"""R5 all 72 eleven-action representatives: pinned class validation & exact checks.
Usage: python VERIFY_ALL72.py FROZEN_TABLE.json RESULTS_ALL72.csv partition_2026.json [--solve]
If --solve: compile EXACT_NINE_V2.cpp in this directory to EXACT_NINE_V2 first.
"""
import csv,hashlib,itertools,json,sys,subprocess,re
from pathlib import Path
P=Path(__file__).parent;L=25845652773852463277015040000;U=58182461585441404127941754880
FROZEN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
H=(18,24,82,34,17,144,208)

def maximal(z):
 z=set(z);return tuple(sorted(m for m in z if not any(m!=q and m&q==m for q in z)))

def windows(c,t):return maximal(sum(1<<i for i,x in enumerate(c) if v<=x<=v+t) for v in c)

def sweep(c,t):
 e=sorted(set(z for x in c for z in (2*x-t,2*x+t)))
 z=[sum(1<<i for i,x in enumerate(c) if abs(p-2*x)<=t) for p in e]
 z += [sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*t) for a,b in zip(e,e[1:])]
 return maximal(z)

def main():
 if len(sys.argv)<4:raise SystemExit(__doc__)
 raw=Path(sys.argv[1]).read_bytes();assert len(raw)==1549048 and hashlib.sha256(raw).hexdigest()==FROZEN
 D=json.loads(raw)['counts_and_cohorts'];M=[[int(z) for z in D[str(k)]['counts']] for k in range(214,315)]
 partition=json.loads(Path(sys.argv[3]).read_text())
 assert len(partition)==2026 and sum(int(r['size']) for r in partition)==30876
 assert {int(r['group_id']) for r in partition}==set(range(2026))
 pmap={int(r['group_id']):r for r in partition}
 records=list(csv.DictReader(open(sys.argv[2],newline='')))
 assert len(records)==72 and len({int(r['gid']) for r in records})==72
 stats={'pairs':0,'support_comparisons':0,'eleven_classes':0,'solver_rechecks':0}
 for r in records:
  g=int(r['gid']);x=int(r['x']);y=int(r['y']);mult=int(r['multiplicity'])
  assert (int(pmap[g]['x']),int(pmap[g]['y']))==(x,y) and int(pmap[g]['size'])==mult
  assert int(r['C8'])==8335
  h=(18,24,82,34,17,x,144,208,y);fams={}
  for k,row in zip(range(214,315),M):
   c=[row[i] for i in h]
   for t in (L,U-1):
    assert windows(c,t)==sweep(c,t),(g,k,t)
    stats['support_comparisons']+=1
   fams.setdefault(windows(c,U-1),k)
  actions=sorted((k,s) for s,k in fams.items());assert len(actions)==11
  lines=['9 8',str(len(actions))]+[' '.join(map(str,[k,len(s),*s])) for k,s in actions]
  inp=('\n'.join(lines)+'\n').encode('ascii')
  assert hashlib.sha256(inp).hexdigest()==r['input_sha256']
  if '--solve' in sys.argv:
   p=subprocess.run([str(P/'EXACT_NINE_V2')],input=inp,capture_output=True,timeout=90)
   m=re.fullmatch(rb'EXACT cost=(\d+) states=(\d+) actions=(\d+) time=([\d.]+)\s*',p.stdout)
   assert p.returncode==0 and m and int(m[1])==8335 and int(m[2])==int(r['memo']) and int(m[3])==11
   stats['solver_rechecks']+=1
  stats['eleven_classes']+=1;stats['pairs']+=mult
 assert stats['eleven_classes']==72 and stats['pairs']==288 and stats['support_comparisons']==14544
 print('PASS_R5_ALL72',stats)
if __name__=='__main__':main()
