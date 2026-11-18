#!/usr/bin/env python3
"""Replay exact signed-native prefix optima for all 91 triple swaps in 3 small classes.
Run in the same PR checkout; requires C++17 and original frozen sources.
"""
import sys, itertools, collections, math, json, base64, hashlib, subprocess, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref, REQ

BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
B64='dH6WdHSOdHR0dHR0dHRsdHR0dHR0dHR0dHR0bHRmdHR0bnR0dHR0dHR0dHR0dG50dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dA=='
EXPECTED_SHA='f5ac7bb47e2a838e02dbb1403864279184d7a213104ea10342652620e0e44c8d'

def main():
 assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
 lab=sorted((h,s) for h,ss in REQ.items() for s in ss)
 lid={v:i for i,v in enumerate(lab)}
 bykey=collections.defaultdict(list); support=collections.defaultdict(int); count=0
 for label,word in all_words():
  k=raw_key(word);support[k] |= 1<<lid[label]
  bykey[k].append((lid[label],pref(word)[-1].hex()))
  count+=1
 assert count==178850 and len(support)==94 and len(lab)==24
 outside=sorted(set(support)-BASE)
 assert len(outside)==87
 dropped=list(itertools.combinations(sorted(BASE),3))
 covers=[]
 for classid in (25,26,28):
  removed=set(dropped[classid]);kept=BASE-removed
  missing=(1<<24)-1
  for k in kept:missing &=~support[k]
  adds=[a for a in itertools.combinations(outside,3) if (
    support[a[0]]|support[a[1]]|support[a[2]])&missing == missing]
  assert len(adds)==({25:3,26:3,28:85}[classid])
  for a in adds:covers.append((classid,tuple(sorted(kept|set(a)))))
 assert len(covers)==91
 lines=[str(len(covers))]
 for _class,keys in covers:
  words=[pair for key in keys for pair in bykey[key]]
  lines.append(str(len(words)))
  lines.extend(f'{i} {w}' for i,w in words)
 cpp=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112'/'SCAN_7KEY_GENERAL.cpp'
 with tempfile.TemporaryDirectory(prefix='ec49fma_') as td:
  exe=Path(td)/'exact_solver'
  subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(exe)],check=True)
  r=subprocess.run([str(exe)],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
 rows=r.stdout.splitlines()
 assert len(rows)==91
 got=[]
 for i,row in enumerate(rows):
  parts=row.split();assert int(parts[0])==i
  got.append(int(parts[1]))
 expected=base64.b64decode(B64,validate=True)
 assert len(expected)==91 and hashlib.sha256(expected).hexdigest()==EXPECTED_SHA
 assert bytes(got)==expected,[(i,a,b) for i,(a,b) in enumerate(zip(got,expected)) if a!=b]
 grouped=collections.defaultdict(list)
 for (classid,_),v in zip(covers,got):grouped[classid].append(v)
 print(json.dumps({k:{'count':len(v),'minimum':min(v),'maximum':max(v),'histogram':dict(sorted(collections.Counter(v).items()))} for k,v in grouped.items()},indent=2))
 print('EC49FMA_NINETY_ONE_SIGNED_PREFIX_EXACT_PASS')
if __name__=='__main__':main()
