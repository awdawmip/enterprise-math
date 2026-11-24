#!/usr/bin/env python3
"""Recompute endpoint independent support sweeps for deterministic samples,
and verify entire 30,876-pair class partition. Needs frozen table and TSV files.
"""
import csv,hashlib,json,random
from pathlib import Path
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L=25845652773852463277015040000
U=58182461585441404127941754880
BASE=(18,24,82,34,17,144,208)
def maximal(ms):
 s=set(ms)
 return tuple(sorted(m for m in s if not any(m!=n and (m&n)==m for n in s)))
def windows(c,t):
 return maximal(sum(1<<i for i,x in enumerate(c) if a<=x<=a+t) for a in c)
def sweep(c,t):
 endpoints=sorted(set(z for x in c for z in (2*x-t,2*x+t)))
 masks=[sum(1<<i for i,x in enumerate(c) if abs(z-2*x)<=t) for z in endpoints]
 masks.extend(sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*t)
              for a,b in zip(endpoints,endpoints[1:]))
 return maximal(masks)
raw=Path("EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()==PIN
data=json.loads(raw)["counts_and_cohorts"]
counts={k:tuple(map(int,data[str(k)]["counts"])) for k in range(214,315)}
allpairs={(x,y) for x in range(256) if x not in BASE
          for y in range(x+1,256) if y not in BASE}
assert len(allpairs)==30876
rng=random.Random(2026111821)
for tag,tau,classes in (("L",L,1460),("U",U-1,2026)):
 rows=list(csv.DictReader(open(f"R5_NINE_PAIRS_{tag}.tsv"),delimiter="\t"))
 assert len(rows)==classes
 groups=[];seen=set()
 for row in rows:
  members=[tuple(map(int,p.split(":"))) for p in row["members"].split(",")]
  assert len(members)==int(row["count"])
  assert members[0]==(int(row["representative_x"]),int(row["representative_y"]))
  assert not (seen & set(members))
  seen.update(members);groups.append(members)
 assert seen==allpairs
 tested=0
 pairs=rng.sample(sorted(allpairs),100)
 pairs.extend(g[0] for g in rng.sample(groups,100))
 pairs.extend(g[1] for g in rng.sample([g for g in groups if len(g)>1],100))
 for x,y in pairs:
  h=(18,24,82,34,17,x,144,208,y)
  for k,c in counts.items():
   centers=[c[a] for a in h]
   assert windows(centers,tau)==sweep(centers,tau),(tag,x,y,k)
   tested+=1
 same=0
 for g in rng.sample([g for g in groups if len(g)>1],80):
  a,b=g[0],g[-1]
  for k,c in counts.items():
   v=windows([c[i] for i in (18,24,82,34,17,a[0],144,208,a[1])],tau)
   w=windows([c[i] for i in (18,24,82,34,17,b[0],144,208,b[1])],tau)
   assert v==w
   same+=1
 print(tag, "classes",classes,"pairs",len(seen),"window_sweep_checks",tested,"same_group_checks",same)
c=counts[294]
assert windows([c[i] for i in (18,24,82,34,17,0,144,208,1)],L)==(511,)
assert windows([c[i] for i in (18,24,82,34,17,48,144,208,1)],L)==(255,479)
print("PASS_R5_NINE_PAIR_ENDPOINT_QUOTIENT_CROSSCHECK")
