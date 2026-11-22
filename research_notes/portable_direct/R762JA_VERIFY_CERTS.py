#!/usr/bin/env python3
"""R762JA: stdlib-only 300-certificate independent Port-Euler verifier.
Run in same directory as R762JA_CERTS.b64: python R762JA_VERIFY_CERTS.py
"""
from itertools import combinations,permutations
from hashlib import sha256
from pathlib import Path
from collections import Counter
import base64,zlib
P=list(combinations(range(6),2));S=list(combinations(range(6),3))
pi={p:i for i,p in enumerate(P)};si={s:i for i,s in enumerate(S)}
Tr=[tuple(pi[p] for p in combinations(s,2)) for s in S]
E=[tuple(combinations(t,2)) for t in Tr]
M=[m for r in range(4) for m in combinations(range(15),r)
   if len(set(a for i in m for a in P[i]))==2*r]
assert len(M)==76

def cc(ts):
    par=list(range(15))
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for s in ts:
        a,b,c=Tr[s];par[find(b)]=find(a);par[find(c)]=find(a)
    return len({find(i) for i in range(15)})

def reps():
    essential=[]
    for t in combinations(range(20),8):
        z=cc(t)
        if all(cc(t[:i]+t[i+1:])>z for i in range(8)):
            essential.append(sum(1<<i for i in t))
    assert len(essential)==4920
    maps=[tuple(si[tuple(sorted(perm[a] for a in s))] for s in S)
          for perm in permutations(range(6))]
    left=set(essential);out=[]
    while left:
        n=min(left)
        orbit={sum(1<<p[i] for i in range(20) if n>>i&1) for p in maps}
        assert orbit<=set(essential)
        out.append((n,len(orbit)));left-=orbit
    assert len(out)==16 and sum(k for _,k in out)==4920
    return out

def check(counts,missing,x):
    assert len(x)==60 and all(type(v)==int and 0<=v<=3 for v in x)
    assert sum(x)==45
    active=set(range(15))-set(missing)
    degree=[0]*15;g=[set() for _ in range(15)]
    for s in range(20):
        assert sum(x[3*s:3*s+3])==counts[s]
        for j,(u,v) in enumerate(E[s]):
            k=x[3*s+j]
            if k:
                assert u in active and v in active
                degree[u]+=k;degree[v]+=k
                g[u].add(v);g[v].add(u)
    assert all(degree[p]>0 and degree[p]%2==0 for p in active)
    assert all(degree[p]==0 for p in set(range(15))-active)
    seen={min(active)};q=list(seen)
    for u in q:
        for v in g[u]:
            if v not in seen:seen.add(v);q.append(v)
    assert seen==active

if __name__=='__main__':
    comp=base64.b64decode(Path(__file__).with_name('R762JA_CERTS.b64').read_text())
    assert sha256(comp).hexdigest()=='808000aeed1e01de0d9ff3c0336be6c22b80f92b6a467b8d204f79aacff741f5'
    raw=zlib.decompress(comp)
    assert len(raw)==4500 and sha256(raw).hexdigest()=='6b30b9be0cea2a021f894c2e5b3d82fec736b910faf52a0409a6145aa6b21980'
    ix=0;by_missing=Counter();by_uncovered=Counter()
    for mask,orbit_size in reps():
        t=[s for s in range(20) if mask>>s&1]
        uncovered=set(range(15))-{p for s in t for p in Tr[s]}
        j=t[0]
        for m in M:
            if not set(m)<=uncovered:continue
            for lone in range(20):
                if lone in t:continue
                c=[3 if s in t else 1 if s==lone else 2 for s in range(20)]
                c[j]=1
                assert sum(c)==45
                block=raw[15*ix:15*(ix+1)]
                x=[(b>>(2*k))&3 for b in block for k in range(4)]
                check(c,m,x)
                ix+=1;by_missing[len(m)]+=1;by_uncovered[len(uncovered)]+=1
    assert ix==300
    assert dict(by_missing)=={0:192,1:96,2:12}
    assert dict(by_uncovered)=={0:120,1:96,2:84}
    print('PASS R762JA 4920 all-essential sets / 16 S6 orbits / 300 exact 45-event witnesses')
    print('inactive-size counts:',dict(sorted(by_missing.items())))
    print('raw certificate sha256:',sha256(raw).hexdigest())
