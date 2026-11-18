#!/usr/bin/env python3
"""Reconcile R5 NEW20 historical SHA256 by a slot permutation.
Args: frozen-table.json historical-RESULTS_R5_NINE_NEW20.json.
No new claim of 20 Bellman replays is made by this test.
"""
import hashlib, json, sys
from pathlib import Path
L=25845652773852463277015040000
U=58182461585441404127941754880
PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'

def maximal(masks):
 s=set(masks)
 return tuple(sorted(m for m in s if not any(m!=v and m&v==m for v in s)))

def fam(c,tau):
 return maximal(sum(1<<i for i,v in enumerate(c) if a<=v<=a+tau) for a in c)

def stdin(D,H):
 seen={}
 for k in range(214,315):
  signature=fam([int(D[str(k)]['counts'][h]) for h in H],U-1)
  seen[signature]=min(k,seen.get(signature,k))
 actions=sorted((k,sig) for sig,k in seen.items())
 return ('\n'.join(['9 8',str(len(actions))]+[' '.join(map(str,(k,len(sig),*sig))) for k,sig in actions])+'\n').encode(),len(actions)

def main():
 raw=Path(sys.argv[1]).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==PIN
 D=json.loads(raw)['counts_and_cohorts']
 runs=json.loads(Path(sys.argv[2]).read_bytes())['runs']
 assert len(runs)==20
 for row in runs:
  x,y=row['x'],row['y']
  historical=(18,24,82,34,17,x,y,144,208)
  documentation=(18,24,82,34,17,x,144,208,y)
  b,n=stdin(D,historical)
  b2,n2=stdin(D,documentation)
  assert hashlib.sha256(b).hexdigest()==row['input_sha256'],(x,y)
  assert hashlib.sha256(b2).hexdigest()!=row['input_sha256'],(x,y)
  assert n==n2==row['action_families'],(x,y)
  for k in range(214,315):
   c=[int(D[str(k)]['counts'][h]) for h in historical]
   d=[int(D[str(k)]['counts'][h]) for h in documentation]
   for tau in (L,U-1):
    def perm(m):
     index=lambda i: 8 if i==6 else 6 if i==7 else 7 if i==8 else i
     return sum(1<<index(i) for i in range(9) if m&(1<<i))
    assert tuple(sorted(map(perm,fam(c,tau))))==fam(d,tau),(x,y,k,tau)
 print('PASS_R5_NEW20_SLOT_BINDING: 20/20 source hashes, 4040 support families, no math rerun')
if __name__=='__main__':main()
