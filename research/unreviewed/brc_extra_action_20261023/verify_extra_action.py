#!/usr/bin/env python3
"""Independent exact 16-mask vs inclusion-exclusion BRC checker; standard library only."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json

z = F(31,32)
q = {
    "0": (F(0), (1+z)/3, (1-z)/3, F(1,3)),
    "2": (F(1,3), F(1,3), F(0), F(1,3)),
    "X": (F(0), F(1), F(0), F(0)),
}
pairs = ((0,1),(1,2),(1,3),(2,3))
good = {sum(1<<i for i in pair) for pair in pairs}

def dp(word):
    state={0:F(1)}
    ds=[F(0)]
    for a in word:
        nxt=defaultdict(F)
        for mask,mass in state.items():
            for i,pi in enumerate(q[a]):
                if pi: nxt[mask | (1<<i)] += mass*pi
        state=dict(nxt)
        assert sum(state.values(),F(0))==1
        ds.append(sum((mass for mask,mass in state.items() if mask in good),F(0)))
    return ds

def incl_excl(word):
    ds=[F(0)]
    for t in range(1,len(word)+1):
        total=F(0)
        for i,j in pairs:
            both,only_i,only_j=F(1),F(1),F(1)
            for a in word[:t]:
                both *= q[a][i]+q[a][j]
                only_i *= q[a][i]
                only_j *= q[a][j]
            total += both-only_i-only_j
        ds.append(total)
    return ds

def residual(ds):
    maximum=F(0)
    positive_sum=F(0)
    rr=[F(0)]
    for i in range(1,len(ds)):
        positive_sum += max(ds[i]-ds[i-1],F(0))
        maximum = max(maximum,ds[i])
        rr.append(positive_sum-maximum)
    return rr

def growth_rounds(rr):
    return [i for i in range(1,len(rr)) if rr[i]>rr[i-1]]

def groups(rounds):
    return sum(i==0 or t!=rounds[i-1]+1 for i,t in enumerate(rounds))

counts={}
witnesses=[]
for n in range(1,8):
    count=0
    for letters in product("02X",repeat=n):
        w="".join(letters)
        ds=dp(w)
        assert ds==incl_excl(w),(w,"occupancy mismatch")
        rr=residual(ds)
        assert all(x>=0 for x in rr)
        steps=growth_rounds(rr)
        if groups(steps)>1:
            count+=1
            witnesses.append({"word":w,"growth_rounds":steps})
    counts[n]={"total":3**n,"split_episodes":count}

assert [counts[n]["split_episodes"] for n in range(1,8)]==[0,0,0,0,0,0,2]
assert witnesses==[
    {"word":"000200X","growth_rounds":[5,7]},
    {"word":"000202X","growth_rounds":[5,7]},
]
ds=dp("000200X")
rr=residual(ds)
assert ds==[
    F(0),F(0),F(2111,4608),F(2,3),F(53039,82944),
    F(81507137,127401984),F(485279705,764411904),
    F(15556924031,24461180928)
]
assert rr[5]-rr[4]==F(39233,127401984)
assert rr[6]-rr[5]==0
assert rr[7]-rr[6]==F(27973471,24461180928)
assert ds[7]-ds[6]==(2-(2-z)**5)/3**6
assert max(ds[:8])==ds[3]==F(2,3)
print(json.dumps({"PASS":True,"words_checked":sum(3**n for n in range(1,8)),
                  "counts":counts,"minimal_n":7,"witnesses":witnesses,
                  "growth_5":str(rr[5]-rr[4]),
                  "growth_7":str(rr[7]-rr[6])},ensure_ascii=False))
