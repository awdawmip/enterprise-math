"""Exact four-coordinate lift and one-template exchange test for the 56-class certificate."""
from collections import Counter, deque
from itertools import combinations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
POINTS=list(product(range(5),repeat=4))

def project(p):
    a,b,c,d=p
    return 25*((a-d)%5)+5*((b-d)%5)+(c-d)%5

FIBRES=[[i for i,p in enumerate(POINTS) if project(p)==s]for s in range(125)]

def forbidden(p,q,r):
    # Distinct isolated singleton types in two coordinates are exactly three L-corners.
    types=set()
    for a,b,c in zip(POINTS[p],POINTS[q],POINTS[r]):
        if a==b!=c:
            types.add(2)
        elif a==c!=b:
            types.add(1)
        elif b==c!=a:
            types.add(0)
    return len(types)>=2

def reference_family():
    data=json.loads((ROOT/'certificate.json').read_text())
    return tuple(sorted(tuple(sorted(project(POINTS[i]) for i in g)) for g in data['templates']))

def audit():
    from functools import lru_cache
    @lru_cache(None)
    def allowed(a,b,s):
        return sum(1<<i for i,c in enumerate(FIBRES[s]) if not forbidden(a,b,c))
    @lru_cache(None)
    def feasible(orbit):
        if len(orbit)>12:
            return False
        if not orbit:
            return True
        def extend(sel,remaining):
            if not remaining:
                return True
            s,m=min(remaining.items(),key=lambda item:item[1].bit_count())
            if not m:
                return False
            rem=remaining.copy()
            del rem[s]
            if not sel:
                # Translation in the kernel makes the first lift uniquely normalizable.
                m &= 1
            for i,p in enumerate(FIBRES[s]):
                if not (m>>i)&1:continue
                next_rem=rem.copy()
                for v in next_rem:
                    for x in sel:
                        next_rem[v]&=allowed(min(x,p),max(x,p),v)
                if extend(sel+[p],next_rem):
                    return True
            return False
        return extend([],{s:31 for s in orbit})

    allsyndromes=set(range(125))
    init=reference_family()
    todo=deque([init])
    visited={init}
    complete=set()
    while todo:
        state=todo.pop()
        holes=allsyndromes.difference(*(set(t) for t in state))
        assert len(holes)==1
        h=next(iter(holes))
        for j,template in enumerate(state):
            enlarged=tuple(sorted((*template,h)))
            if feasible(enlarged):
                complete.add(tuple(sorted((*state[:j],*state[j+1:],enlarged))))
            for p in template:
                replacement=tuple(x for x in enlarged if x!=p)
                other=tuple(sorted((*state[:j],*state[j+1:],replacement)))
                if other not in visited and feasible(replacement):
                    visited.add(other)
                    todo.append(other)
    return dict(reachable_partial_partitions=len(visited),full_partitions=len(complete),tested_lift_sets=feasible.cache_info().misses)

if __name__=='__main__':
    print(json.dumps(audit(),indent=2))
