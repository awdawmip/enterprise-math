#!/usr/bin/env python3
"""R762JS exact six-axis Port–Euler parity/rainbow verification.
Python standard library only. Source is author-side, not independent review.
"""
from itertools import combinations, product
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import json, random

AX=tuple(range(6)); PORTS=tuple(combinations(AX,2))
SUP=tuple(combinations(AX,3))
def ports(s): return tuple(combinations(s,2))
def sides(s): return tuple(combinations(ports(s),2))
def basis(vec):
    b={}
    for i,v in enumerate(vec):
        w=1<<i
        while v:
            k=v.bit_length()-1
            if k in b: v^=b[k][0];w^=b[k][1]
            else: b[k]=(v,w);break
    return b
def solve(v,b):
    coeff=0
    for k in sorted(b,reverse=True):
        if v>>k&1:v^=b[k][0];coeff^=b[k][1]
    return coeff if not v else None
def reduce(v,b):
    for k in sorted(b,reverse=True):
        if v>>k&1:v^=b[k][0]
    return v

class PortCase:
    def __init__(self,missing):
        self.M=frozenset(missing)
        self.V=tuple(p for p in PORTS if p not in self.M)
        self.ix={p:i for i,p in enumerate(self.V)}
        self.F=tuple(s for s in SUP if all(p in self.ix for p in ports(s)))
        self.G=tuple(s for s in SUP if s not in self.F)
        self.GE={s:tuple(p for p in ports(s) if p in self.ix) for s in self.G}
        assert all(len(e)==2 for e in self.GE.values())
        self.E={s:sides(s) for s in self.F}
        self.vec={s:tuple(self.bit(e) for e in self.E[s]) for s in self.F}
        self.comp=self.components(self.GE.values())
        self.part={p:i for i,comp in enumerate(self.comp) for p in comp}
        assert len(self.G)==4*len(self.M)
        assert len(self.F)==(12 if len(self.M)==2 else 8)
        assert len(self.comp)==(6 if len(self.M)==2 else 3)
        assert all(len({self.part[p] for p in ports(s)})==3 for s in self.F)
    def bit(self,e):return (1<<self.ix[e[0]])^(1<<self.ix[e[1]])
    def components(self,links):
        par={p:p for p in self.V}
        def root(p):
            while par[p]!=p:p=par[p]
            return p
        for p,q in links:par[root(p)]=root(q)
        out={}
        for p in self.V:out.setdefault(root(p),set()).add(p)
        return tuple(sorted((frozenset(v) for v in out.values()),key=min))
    def parity(self,D):
        D=set(D)
        flexible=[v for s in self.F if s not in D for v in self.vec[s]]
        B=basis(flexible)
        residues={0}
        for s in sorted(D):
            residues={reduce(r^v,B) for r in residues for v in self.vec[s]}
        needed=1<<(len(self.V)-1-len(B))
        assert len(residues)==needed
        reachable={0}
        for s in self.F:
            options=self.vec[s] if s in D else (0,)+self.vec[s]
            reachable={a^v for a in reachable for v in options}
        assert len(reachable)==(1<<(len(self.V)-1))
        return len(B),len(residues)
    def rainbow(self,D):
        available=[s for s in self.F if s not in D]
        ncomp=len(self.comp)
        def norm(p):
            d={};q=[]
            for v in p:
                if v not in d:d[v]=len(d)
                q.append(d[v])
            return tuple(q)
        @lru_cache(maxsize=None)
        def search(i,state):
            if len(set(state))==1:return ()
            if i==len(available):return None
            s=available[i]
            for edge in self.E[s]:
                a,b=(self.part[p] for p in edge)
                if state[a]==state[b]:continue
                nxt=norm(tuple(state[b] if x==state[a] else x for x in state))
                t=search(i+1,nxt)
                if t is not None:return ((s,edge),)+t
            return search(i+1,state)
        t=search(0,tuple(range(ncomp)))
        assert t is not None and len(t)==ncomp-1
        assert len({s for s,_ in t})==len(t)
        return dict(t)
    def witness(self,n):
        assert Counter(n.values())==Counter({1:3,2:12,3:5}) and set(n)==set(SUP)
        events=[];parity=0
        for s in self.G:
            e=self.GE[s]
            events.extend((s,e) for _ in range(n[s]))
            if n[s]%2:parity^=self.bit(e)
        D=tuple(s for s in self.F if n[s]==1)
        generators=[(s,v) for s in self.F if s not in D for v in self.vec[s]]
        B=basis([v for _,v in generators])
        pair=None
        for js in product(range(3),repeat=len(D)):
            v=0
            for s,j in zip(D,js):v^=self.vec[s][j]
            sol=solve(parity^v,B)
            if sol is not None:pair=(dict(zip(D,js)),sol);break
        assert pair is not None
        singleton,coeff=pair
        target={s:0 for s in self.F}
        for i,(s,v) in enumerate(generators):
            if coeff>>i&1:target[s]^=v
        designated=self.rainbow(D)
        for s in self.F:
            e=self.E[s]
            if n[s]==1:events.append((s,e[singleton[s]]))
            elif n[s]==2:
                if target[s]==0:
                    chosen=designated.get(s,e[0])
                    events.extend([(s,chosen),(s,chosen)])
                else:
                    others=[x for x in e if self.bit(x)!=target[s]]
                    assert len(others)==2
                    events.extend((s,x) for x in others)
            else:
                if target[s]==0:events.extend((s,x) for x in e)
                else:
                    side=next(x for x in e if self.bit(x)==target[s])
                    extra=next(x for x in e if x!=side)
                    events.extend([(s,side),(s,extra),(s,extra)])
        assert len(events)==42 and Counter(s for s,e in events)==Counter(n)
        deg=Counter()
        for s,(a,b) in events:
            assert a!=b and a in self.ix and b in self.ix
            assert a in ports(s) and b in ports(s)
            deg[a]+=1;deg[b]+=1
        assert all(deg[p]>0 and deg[p]%2==0 for p in self.V)
        assert len(self.components(e for s,e in events))==1
        return events

def main():
    rng=random.Random(76211123)
    result={'schema':'R762JS_MATCHING_INACTIVE_GF2_RAINBOW_V1',
            'status':'AUTHOR_PROVED_EXACT_FINITE / NOT_REVIEWED',
            'science_pin':'PR #2985 @47504c177ac2b318f5419a5fdb1304fafccf21fc',
            'models':[]}
    digest=sha256()
    for M in (((0,1),(2,3)),((0,1),(2,3),(4,5))):
        c=PortCase(M); histogram=Counter();patterns=0
        for k in range(4):
            for d in combinations(c.F,k):
                rank,cosets=c.parity(d)
                assert len(c.rainbow(d))==len(c.comp)-1
                histogram[(k,rank,cosets)]+=1
                patterns+=1
        assert patterns==(299 if len(M)==2 else 93)
        sample=0
        for single in combinations(SUP,3):
            sel=set(single)
            triple=set(rng.sample([s for s in SUP if s not in sel],5))
            n={s:(1 if s in sel else 3 if s in triple else 2) for s in SUP}
            for s,(a,b) in c.witness(n):
                digest.update(bytes((SUP.index(s),PORTS.index(a),PORTS.index(b))))
            sample+=1
        result['models'].append({'matching':list(M),'active_ports':len(c.V),
            'forced_labels':len(c.G),'full_labels':len(c.F),
            'forced_components':len(c.comp),'pattern_count':patterns,
            'rank_cosets':[{'k':k,'rank':rank,'cosets':cosets,'count':n}
                          for (k,rank,cosets),n in sorted(histogram.items())],
            'failed_patterns':0,'sample_42_event_witnesses':sample})
    result['exact_patterns_total']=sum(x['pattern_count'] for x in result['models'])
    result['sample_witnesses_total']=sum(x['sample_42_event_witnesses'] for x in result['models'])
    result['sample_event_stream_sha256']=digest.hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
