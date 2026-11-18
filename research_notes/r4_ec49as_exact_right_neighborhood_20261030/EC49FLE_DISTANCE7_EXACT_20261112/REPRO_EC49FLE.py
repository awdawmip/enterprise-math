#!/usr/bin/env python3
"""EC49FLE: exact matched-distance-7 two-key cover and 810 signed-native optima.
Run beside EXACT_REPORT_EC49FLE.json and sibling canonical EC49FJD + EC49FKY.
Default validates the complete coverage census and the committed costs digest;
--solve compiles the unchanged EC49FKY C++17 trie optimizer and reruns all 810.
"""
import base64, collections, hashlib, itertools, json, subprocess, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,raw_key,pref,STEPS
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
K0={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
cat=list(all_words());labels=sorted({lab for lab,_ in cat});labid={x:i for i,x in enumerate(labels)}
assert len(cat)==178850 and len(labels)==24
support=collections.defaultdict(int);bykey=collections.defaultdict(list);rts=collections.defaultdict(set)
for lab,w in cat:
 k=raw_key(w);support[k]|=1<<labid[lab];rts[k].add(STEPS[w[0]][0]);bykey[k].append((labid[lab],pref(w)[-1].hex()))
allkeys=sorted(support);outside=sorted(set(allkeys)-K0);assert len(allkeys)==94 and len(outside)==87
full=(1<<24)-1
counts=collections.defaultdict(lambda: [0,0]);d7=[]
L1=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
for old in itertools.combinations(sorted(K0),2):
 remain=K0-set(old);oldmask=0
 for k in remain:oldmask|=support[k]
 for new in itertools.combinations(outside,2):
  dist=min(L1(old[0],new[0])+L1(old[1],new[1]),L1(old[0],new[1])+L1(old[1],new[0]))
  can=int(oldmask|support[new[0]]|support[new[1]]==full)
  counts[dist][can]+=1
  if dist==7 and can:
   keys=tuple(sorted(remain|set(new)));roots=set().union(*(rts[k] for k in keys))
   d7.append((len(roots),old,new,keys))
d7.sort()
assert sum(sum(x) for x in counts.values())==78561
assert sum(x[1] for x in counts.values())==6315
assert counts[7]==[4417,810] and len(d7)==810
assert collections.Counter(row[0] for row in d7)=={3:328,4:482}
expected=json.loads((HERE/'EXACT_REPORT_EC49FLE.json').read_text())
costbytes=base64.b64decode(expected['costs_u8_base64'],validate=True)
assert len(costbytes)==810 and hashlib.sha256(costbytes).hexdigest()==expected['costs_sha256']
assert min(costbytes)==98 and sum(x==98 for x in costbytes)==25
assert dict(sorted((int(k),v) for k,v in expected['distance_7'].items()))=={7:{'coverable':810,'uncoverable':4417}}
print('EC49FLE_EXACT_COVERAGE_AND_COST_DIGEST_PASS',len(cat),len(allkeys),len(labels),len(d7),flush=True)
if '--solve' in sys.argv:
 cpp=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp'
 binary=HERE/'EC49FLE_CXX_SOLVER'
 subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(binary)],check=True)
 checked=[]
 for lo in range(0,810,50):
  chunk=d7[lo:min(lo+50,810)]
  lines=[str(len(chunk))]
  for _,_,_,keys in chunk:
   rows=[p for key in keys for p in bykey[key]]
   lines.append(str(len(rows)))
   lines.extend(str(i)+' '+w for i,w in rows)
  r=subprocess.run([str(binary)],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
  out=r.stdout.splitlines();assert len(out)==len(chunk)
  for i,ln in enumerate(out):
   q=ln.split();assert int(q[0])==i
   checked.append(int(q[1]))
  print('PASS',lo,len(checked),flush=True)
 assert bytes(checked)==costbytes
 print('EC49FLE_ALL_810_EXACT_NATIVE_PREFIX_OPTIMA_PASS',min(checked))
