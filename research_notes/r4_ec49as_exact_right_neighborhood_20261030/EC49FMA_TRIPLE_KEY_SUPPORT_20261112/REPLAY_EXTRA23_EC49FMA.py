#!/usr/bin/env python3
"""Exact replay of all 23 three-key swaps in EC49FMA removed-key classes #29, #30.
Requires Python 3 stdlib, g++ (C++17), original frozen source files at PR checkout.
"""
import sys, itertools, collections, subprocess, base64, hashlib, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref, REQ
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
B64='j3Bml3RscJ9wdHyPl5/CimySbICKkqw='
DIGEST='456e1ba997c73ab876dedf2b288484a1e120e270ecf1e82ae8a1cddc25c3247e'

def main():
 labs=sorted((h,s) for h,ss in REQ.items() for s in ss)
 lid={x:i for i,x in enumerate(labs)}
 bykey=collections.defaultdict(list);sup=collections.defaultdict(int);n=0
 for label,word in all_words():
  k=raw_key(word);sup[k] |= 1<<lid[label]
  bykey[k].append((lid[label],pref(word)[-1].hex()));n+=1
 assert n==178850 and len(sup)==94 and len(labs)==24
 outside=sorted(set(sup)-BASE)
 assert len(outside)==87
 drops=list(itertools.combinations(sorted(BASE),3))
 cases=[]
 for ci in (29,30):
  kept=BASE-set(drops[ci]);missing=(1<<24)-1
  for k in kept:missing&=~sup[k]
  additions=[pair for pair in itertools.combinations(outside,3)
             if ((sup[pair[0]]|sup[pair[1]]|sup[pair[2]])&missing)==missing]
  assert len(additions)==({29:15,30:8}[ci])
  cases += [(ci,tuple(sorted(kept|set(add)))) for add in additions]
 assert len(cases)==23
 inp=[str(len(cases))]
 for _,keys in cases:
  words=[entry for key in keys for entry in bykey[key]]
  inp.append(str(len(words)))
  inp.extend(f'{label} {word}' for label,word in words)
 original=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112'/'SCAN_7KEY_GENERAL.cpp'
 with tempfile.TemporaryDirectory(prefix='ec49fma23_') as d:
  exe=Path(d)/'solver'
  subprocess.run(['g++','-O3','-std=c++17',str(original),'-o',str(exe)],check=True)
  out=subprocess.run([str(exe)],input='\n'.join(inp)+'\n',text=True,
                     capture_output=True,check=True).stdout.splitlines()
 assert len(out)==23
 costs=[]
 for i,row in enumerate(out):
  v=row.split();assert int(v[0])==i
  costs.append(int(v[1]))
 expected=base64.b64decode(B64,validate=True)
 assert len(expected)==23 and hashlib.sha256(expected).hexdigest()==DIGEST
 assert bytes(costs)==expected
 assert min(costs)==102 and max(costs)==194
 print('EC49FMA_EXTRA23_NATIVE_PREFIX_EXACT_PASS',len(costs),min(costs),max(costs))
if __name__=='__main__':main()
