#!/usr/bin/env python3
"""Independent Python direct all-101-action, doubled-interval, f=0 census."""
import hashlib,json,sys
from functools import lru_cache
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
H=(0,16,32,48,1,64)
p,sp=sys.argv[1:3]
b=open(p,"rb").read()
assert hashlib.sha256(b).hexdigest()==PIN
j=json.loads(b)
cen={k:tuple(map(int,j["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
tau=int(json.load(open(sp))["U"])-1
def masks(k,labels):
    a=[cen[k][h] for h in labels]
    candidates={sum(1<<i for i,c in enumerate(a) if 2*c-tau<=z<=2*c+tau)
                for z in {2*x-tau for x in a}}
    return tuple(s for s in candidates if not any(s!=q and (s&q)==s for q in candidates))
results={}
for h in range(256):
    if h in H:continue
    families={k:masks(k,H+(h,)) for k in cen}
    @lru_cache(None)
    def v(live):
        if live.bit_count()<=1:return 0
        options=[]
        for k,ss in families.items():
            if any((s&live)==live for s in ss):continue
            options.append(k+max(v(live&s) for s in ss))
        return min(options)
    exact=v(127)
    expected=733 if 16<=h%64<=47 else 732
    assert exact==expected,(h,exact,expected)
    results[h]=exact
print("PASS_R5_INDEPENDENT_F0",len(results),"v732",sum(x==732 for x in results.values()),
      "v733",sum(x==733 for x in results.values()))
