#!/usr/bin/env python3
"""Independent exact doubled-endpoint f0 census / twelve f1 checks.
This verifier reads the raw byte-pinned counts, not window_adj.bin.
"""
import json,hashlib,functools
from pathlib import Path
p=Path("EXACT_R5_ALL_101_BUDGETS.json");raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
counts={k:[int(x) for x in data["counts_and_cohorts"][str(k)]["counts"]] for k in range(214,315)}
tau=58182461585441404127941754879
seed=(0,16,32,48,1,64,17,80,18,24)
full=(1<<11)-1
def actions(t):
    labels=seed+(t,); d={}
    for k,allvals in counts.items():
        v=[allvals[h] for h in labels]
        endpoints=[2*z-tau for z in v]
        candidates={sum(1<<j for j,z in enumerate(v) if abs(2*z-x)<=tau) for x in endpoints}
        fam=tuple(sorted(m for m in candidates if all(m==n or m&n!=m for n in candidates)))
        if fam!=(full,): d.setdefault(fam,k)
    return sorted((k,masks) for masks,k in d.items())
def f0(actions):
    values=[0]*(full+1)
    for mask in range(1,full+1):
        if mask.bit_count()<=1:continue
        opts=[k+max(values[mask&m] for m in fam) for k,fam in actions
              if all(mask&m!=mask for m in fam)]
        assert opts
        values[mask]=min(opts)
    return values[full]
def f1(actions):
    @functools.lru_cache(None)
    def solve(e):
        live=sum((1<<j) for j,v in enumerate(e) if v<=1)
        if live.bit_count()<=1:return 0
        best=10**9
        for k,fam in actions:
            if any((m&live)==live for m in fam):continue
            worst=0
            for m in fam:
                nxt=tuple(min(2,v+(not (m>>j&1))) for j,v in enumerate(e))
                worst=max(worst,solve(nxt))
                if k+worst>=best:break
            best=min(best,k+worst)
        assert best<10**9
        return best
    return solve((0,)*11)
selected={2,3,5,7,9,10,14,35,40,82,95,100}
all_labels=[t for t in range(256) if t not in seed]
assert len(all_labels)==246
for t in all_labels:
    acts=actions(t)
    assert f0(acts)==733,("f0",t)
    if t in selected:assert f1(acts)==1681,("f1",t)
print("PASS_ELEVEN_INDEPENDENT_F0",len(all_labels),"F1",len(selected))
