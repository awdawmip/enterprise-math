"""Independent direct per-root set-cover check for the double-W templates."""
import json
from math import gcd,lcm
from random import Random
from itertools import combinations
from functools import lru_cache
from pathlib import Path
base=Path(__file__).parent
D=json.loads((base/'templates.json').read_text())
shapes=[set(map(tuple,s)) for s in D['shapes']]
pool={int(h):qs for h,qs in D['by_h'].items()}
period={int(q):r['f'] for r in json.loads((base/'low_inventory.json').read_text()) for q in r['primeFactors']}
A={0,3,5,8,10,15,21,23,26,28,30,31,33}
P=lcm(35,2,*pool)
ws=tuple(w for w in range(P) if w%35 in A)
slots={(h,b) for h,qs in pool.items() for b in range(h)}|{(2,1)}
bit={k:sum(1<<i for i,w in enumerate(ws) if w%k[0]==k[1]) for k in slots}
full=(1<<len(ws))-1
def merge(masks):
    x=0
    for m in masks:x|=m
    return x
for s in shapes:
    assert merge(bit[k] for k in s)==full
    assert all(merge(bit[k] for k in s if k!=x)!=full for x in s)
    for h in pool:
        assert sum(k[0]==h for k in s)<=len(pool[h])
def direct(active,k):
    M=tuple(bit[x] for x in active if bit[x])
    if merge(M)!=full:return False
    @lru_cache(None)
    def recur(m,k):
        if not m:return True
        if not k:return False
        b=m&-m
        return any(recur(m&~v,k-1) for v in M if b&v)
    return recur(full,k)
rng=Random(20261125); cases=[]
for s in shapes:
    state={};used=set()
    for h,b in sorted(s):
        if h==2:continue
        q=rng.choice(tuple(q for q in pool[h] if q not in used))
        state[q]=(2+3*b)%period[q];used.add(q)
    cases.append(state)
    cases.append(dict(list(state.items())[1:]))
for _ in range(140):
    state=rng.choice(cases).copy()
    state.update(rng.choice(cases))
    for q in rng.sample(sorted(period),rng.randrange(7)):
        state[q]=rng.randrange(period[q])
    cases.append(state)
p_to_h={q:h for h,qs in pool.items() for q in qs}
counts={}
for k in (3,4,5):
    yes=0
    for r in cases:
        occ={(2,1)}
        for q,b in r.items():
            if q not in p_to_h:continue
            f=period[q];h=p_to_h[q];g=gcd(f,3)
            if (b-2)%g:continue
            w=((b-2)//g*pow(3//g,-1,h))%h
            occ.add((h,w))
        v=any(len(s)<=k and s<=occ for s in shapes)
        assert v==direct(occ,k)
        yes+=int(v)
    counts[k]=yes
print(json.dumps({'root_category_vectors':len(cases),'literal_tests':len(cases)*3,'positive':counts},indent=2))
