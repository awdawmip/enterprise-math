"""Incremental component observer for fixed capacities and independent base U."""
from collections import Counter
from itertools import combinations
from random import Random
from time import perf_counter
import json, hashlib
from incremental_tight import Dynamic
from reverse_tight import banks
from unit_slack import reduce_bank
from exchange_components import components,rank,part

class Observer:
    def __init__(self,u,c):
        self.d=Dynamic(c);self.c=c;self.parent={};self.basis=set();self.circuits={};self.visits=0
        for t,w in u.items():self.d.insert(t,w)
        assert self.d.h==len(u)
    def root(self,t):
        while self.parent[t]!=t:
            self.parent[t]=self.parent[self.parent[t]];t=self.parent[t]
        return t
    def insert(self,t,w):
        self.parent[t]=t;old=self.d.h;self.d.insert(t,w)
        if self.d.h>old:
            self.basis.add(t);return
        todo=w;reach=0;circ={t}
        while todo:
            b=todo&-todo;todo^=b
            if reach&b:continue
            reach|=b;self.visits+=1;j=b.bit_length()-1
            assert len(self.d.owners[j])==self.c[j]
            for y in self.d.owners[j]:
                if y in self.basis:circ.add(y)
                todo|=self.d.opts[y]&~reach
        for y in circ:self.parent[self.root(y)]=self.root(t)
        self.circuits[t]=sorted(circ)
    def groups(self):
        g={}
        for t in self.parent:g.setdefault(self.root(t),[]).append(t)
        return sorted(sorted(v) for v in g.values())

def build(u,c,x):
    d=Observer(u,c)
    for t,w in x.items():d.insert(t,w)
    return d

def compressed(u,c,x,d):
    # Store labels with explicit rank law, or full masks for unsupported components.
    out=[]
    for g in d.groups():
        k=len(set(g)&d.basis);n=len(g)
        if k<=1 or n-k<=1:
            out.append((g,k,'uniform',None))
        elif k==2:
            # Simple or parallel rank-two: classify pair dependence by exact rank.
            classes=[]
            for t in g:
                for a in classes:
                    if rank(u,c,part(x,[t,a[0]]))==1:a.append(t);break
                else:classes.append([t])
            out.append((g,k,'rank2',classes))
        else:out.append((g,k,'raw',part(x,g)))
    return out

def query(u,c,rep,Q):
    ans=0
    for g,k,kind,extra in rep:
        if kind=='uniform':ans+=min(k,len(Q&set(g)))
        elif kind=='rank2':ans+=min(2,sum(bool(Q&set(a)) for a in extra))
        else:ans+=rank(u,c,part(extra,Q&set(g)))
    return ans

def random_checks():
    rng=Random(492611270931);st=Counter()
    for _ in range(1600):
        m=rng.randrange(1,8);c=[rng.randrange(1,4) for _ in range(m)]
        u={f'u{i}':rng.randrange(1<<m) for i in range(rng.randrange(12))}
        _,_,u,c,_=reduce_bank(u,c)
        x={f'x{i}':rng.randrange(1<<len(c)) for i in range(rng.randrange(9))}
        for xx in (x,dict(reversed(list(x.items())))):
            d=Observer(u,c);p={}
            for t,w in xx.items():
                d.insert(t,w);p[t]=w
                g,B,cs,v=components(u,c,p)
                assert (g,B,cs)==(d.groups(),d.basis,d.circuits)
                assert len(B)==rank(u,c,p)
                st['prefix_checks']+=1
            rep=compressed(u,c,xx,d);keys=list(xx)
            for mask in range(1<<len(keys)):
                Q={t for j,t in enumerate(keys) if mask>>j&1}
                assert query(u,c,rep,Q)==rank(u,c,part(xx,Q))
                st['subset_checks']+=1
            st['orders']+=1
    return st

def load_cases():
    for r in json.load(open('witness_records.json')):
        c=r['caps'];opts=r['opts'];w=len(c)//2;active=sum(1<<j for j,v in enumerate(c) if v);u={};p={};rc=[];keep=[]
        for j,(a,bc) in enumerate(banks(opts,c,[w,w])):
            bw,h,rp,bc2,kp=reduce_bank(a,bc);off=len(rc)
            u.update({t:v<<(j*w) for t,v in a.items()});p.update({t:v<<off for t,v in rp.items()});rc.extend(bc2);keep.extend(j*w+k for k in kp)
        sh={t:sum(1<<j for j,k in enumerate(keep) if v>>k&1) for t,v in opts.items() if t not in u and v&active}
        yield p,rc,sh

def frozen():
    cases=list(load_cases());st=Counter();positive=[];dig=hashlib.sha256()
    for i,(u,c,x) in enumerate(cases):
        d=Observer(u,c);p={}
        for t,w in x.items():
            d.insert(t,w);p[t]=w
            g,B,cs,v=components(u,c,p)
            assert (g,B,cs)==(d.groups(),d.basis,d.circuits)
            st['prefix_checks']+=1;st['static_prefix_visits']+=v
        assert len(d.basis)==rank(u,c,x)
        rep=compressed(u,c,x,d)
        for g,k,kind,extra in rep:
            st['kind_'+kind]+=1;st['elements_'+kind]+=len(g)
            if len(g)>k:
                positive.append([i,g,k,kind,extra]);st['dependent_components']+=1
                st['core_elements']+=len(g)
                # Exhaust all subsets within dependent components only.
                for mask in range(1<<len(g)):
                    Q={t for j,t in enumerate(g) if mask>>j&1}
                    assert query(u,c,[(g,k,kind,extra)],Q)==rank(u,c,part(x,Q))
                    st['core_subset_checks']+=1
        st['records']+=1;st['dynamic_visits']+=d.visits;st['shared']+=len(x)
        assert query(u,c,rep,set(x))==len(d.basis)
        dig.update((json.dumps([i,rep],sort_keys=True)+'\n').encode())
    times=[]
    for j in range(3):
        row={}
        for name in (('dynamic','static') if j%2==0 else ('static','dynamic')):
            start=perf_counter()
            for u,c,x in cases:
                if name=='dynamic':build(u,c,x)
                else:components(u,c,x)
            row[name]=perf_counter()-start
        times.append(row)
    return dict(stats=st,dependent=positive,digest=dig.hexdigest(),timings=times)
if __name__=='__main__': print(json.dumps(dict(random=random_checks(),frozen=frozen(),mismatches=0),sort_keys=True))
