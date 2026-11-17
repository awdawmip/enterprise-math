#!/usr/bin/env python3
"""Exact original-native EC49FRP parity Bellman and anchor calculation.
Run in extracted EC49FRP evidence folder with native code/ and frozen source/.
No network, no special numerical library, no inherited Bellman JSON needed.
"""
from functools import lru_cache
from pathlib import Path
import hashlib
from EC49FQI_NATIVE_DATA import V, weights, PIN, MASTER, CSV

root=Path(__file__).resolve().parent.parent
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((root/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((root/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(weights)==141 and sum(weights)==310

qs=[];seen={}
for q,outputs in enumerate(V):
    fibers={}
    for i,y in enumerate(outputs):fibers[y]=fibers.get(y,0)|(1<<i)
    part=tuple(fibers.values());sig=tuple(sorted(part))
    if sig in seen:assert (seen[sig]<144)==(q<144)
    else:seen[sig]=q;qs.append((q,part))
assert len(qs)==209
all_states=(1<<141)-1

def solve(weight,parity=False):
    @lru_cache(None)
    def mass(mask):
        total=0
        while mask:
            lo=mask&-mask;mask-=lo
            total+=weight[lo.bit_length()-1]
        return total
    @lru_cache(None)
    def bell(mask):
        if mask.bit_count()<2:return (0,10**90) if parity else (0,)
        best=[10**90,10**90] if parity else [10**90]
        for q,part in qs:
            branches=[mask&x for x in part if mask&x]
            if len(branches)<2:continue
            c=1 if q<144 else 3
            acc=[0,10**90] if parity else [0]
            for b in branches:
                if b.bit_count()<2:continue
                child=bell(b)
                if parity:
                    acc=[min(acc[0]+child[0],acc[1]+child[1]),
                         min(acc[1]+child[0],acc[0]+child[1])]
                else:acc=[acc[0]+child[0]]
            cost=c*mass(mask)
            if parity:
                shift=(c*mask.bit_count())&1
                for k in (0,1):best[k]=min(best[k],cost+acc[k^shift])
            else:best[0]=min(best[0],cost+acc[0])
        return tuple(best)
    result=bell(all_states)
    print('result',result,'reachable_subsets',bell.cache_info().currsize)
    return result

assert solve([19+2*m for m in weights],parity=True)==(7290,7311)
assert solve([1]*141)[0]==308
assert solve(weights)[0]==700
print('PASS EC49FRP original-native parity and endpoint anchors')
