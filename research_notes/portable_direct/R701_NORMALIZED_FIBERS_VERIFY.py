#!/usr/bin/env python3
"""R701 exact finite proof certificate: normalized BRC contextual observer fibers."""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import json
N=(24,18,6,12)
F=defaultdict(list);G=defaultdict(list)
for e in range(25):
 for t in range(19):
  for c in range(7):
   for z in range(13):
    s=e+t+c+z
    if not s:continue
    U=4*e+5*t+z;V=2*e+2*c+z;W=U+46*V
    a=gcd(U,s);b=gcd(V,s);g=gcd(W,s)
    F[(U//a,s//a,V//b,s//b)].append((e,t,c,z))
    G[(W//g,s//g)].append((e,t,c,z))
assert sum(map(len,F.values()))==sum(map(len,G.values()))==43224
assert len(F)==36688 and len(G)==29153
assert max(map(len,F.values()))==30 and max(map(len,G.values()))==44
assert [k for k,v in F.items() if len(v)==30]==[(3,1,1,1)]
assert set(k for k,v in G.items() if len(v)==44)=={(59,1),(62,1)}
assert all(len({sum(x) for x in fiber})==len(fiber) for fiber in F.values())
assert all(len({sum(x) for x in fiber})==len(fiber) for fiber in G.values())
by_e=Counter()
for e in range(25):
 for z in range(13):
  c=3*e-2*z;t=4*e-2*z
  if 0<=c<=6 and 0<=t<=18 and e+t+c+z>0:by_e[e]+=1
assert sum(by_e.values())==30
assert dict(sorted(by_e.items()))=={1:2,2:4,3:3,4:4,5:3,6:4,7:3,8:4,9:2,10:1}
def native_count(lam):
 count=0
 for e in range(25):
  for t in range(19):
   for c in range(7):
    numerator=(96-lam)*e+(5-lam)*t+(92-lam)*c
    den=lam-47
    if numerator%den==0:
     z=numerator//den
     if 0<=z<=12 and e+t+c+z>0:count+=1
 return count
assert native_count(59)==native_count(62)==44
result={
 "domain":"R699 static E* four-group histogram, nonzero v<=N",
 "N":N,"histograms":43224,
 "two_probe":{"distinct":len(F),"max_fiber":30,"extra_bits":5,"max_key":(3,1,1,1),
              "max_fiber_states":F[(3,1,1,1)],
              "distribution":dict(sorted(Counter(map(len,F.values())).items()))},
 "single_fusion":{"distinct":len(G),"max_fiber":44,"extra_bits":6,
                  "max_keys":[(59,1),(62,1)],
                  "max_states":{str(k):G[(k,1)] for k in [59,62]},
                  "distribution":dict(sorted(Counter(map(len,G.values())).items()))},
 "native_event_realization":"NOT_ATTEMPTED"}
Path("R701_NORMALIZED_FIBER_RESULTS.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print("R701_NORMALIZED_FIBER_EXACT_PASS",len(F),len(G),30,44)
