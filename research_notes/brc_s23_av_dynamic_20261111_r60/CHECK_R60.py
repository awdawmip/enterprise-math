#!/usr/bin/env python3
"""R60 dynamic exact rational-circle index: absolute source times, circular maximum timestamp."""
from bisect import bisect_right
from random import Random
from math import gcd
from pathlib import Path
import json
from CHECK_R59 import sample_phases
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
class N:
    __slots__=('k','t','prio','l','r','mx','low','high')
    def __init__(self,k,t,prio):
        self.k=k;self.t=t;self.prio=prio;self.l=None;self.r=None
        self.mx=t;self.low=self.high=k[0]
def refresh(n):
    n.mx=n.t;n.low=n.high=n.k[0]
    for s in (n.l,n.r):
        if s:
            n.mx=max(n.mx,s.mx);n.low=min(n.low,s.low);n.high=max(n.high,s.high)
    return n
def rr(n):
    t=n.l;n.l=t.r;t.r=refresh(n);return refresh(t)
def rl(n):
    t=n.r;n.r=t.l;t.l=refresh(n);return refresh(t)
def insert(n,new):
    if n is None:return new
    if new.k<n.k:
        n.l=insert(n.l,new)
        if n.l.prio<n.prio:return rr(n)
    else:
        assert new.k!=n.k
        n.r=insert(n.r,new)
        if n.r.prio<n.prio:return rl(n)
    return refresh(n)
def merge(a,b):
    if a is None:return b
    if b is None:return a
    if a.prio<b.prio:
        a.r=merge(a.r,b);return refresh(a)
    b.l=merge(a,b.l);return refresh(b)
def erase(n,k):
    if n is None:raise KeyError(k)
    if k==n.k:return merge(n.l,n.r)
    if k<n.k:n.l=erase(n.l,k)
    else:n.r=erase(n.r,k)
    return refresh(n)
def range_max(n,l,r):
    if n is None or n.high<l or n.low>=r:return None
    if l<=n.low and n.high<r:return n.mx
    val=n.t if l<=n.k[0]<r else None
    for child in (n.l,n.r):
        u=range_max(child,l,r)
        if u is not None and (val is None or u>val):val=u
    return val
class Index:
    def __init__(self,p,q,m,seed=600011):
        assert 0<p<q and m>=1
        self.p=p;self.q=q;self.M=2*q;self.m=m;self.root=None;self.times=set()
        self.rng=Random(seed)
        self.boundaries=sorted((2*(z*p%q),z) for z in range(m))
        self.ops=0
    def key(self,t):return (2*(t*self.p%self.q),t)
    def add(self,t):
        assert t not in self.times
        self.root=insert(self.root,N(self.key(t),t,self.rng.getrandbits(64)))
        self.times.add(t);self.ops+=1
    def remove(self,t):
        assert t in self.times
        self.root=erase(self.root,self.key(t))
        self.times.remove(t);self.ops+=1
    def query(self,j,x):
        if self.root is not None and self.root.mx>=j:raise ValueError('sources must be past')
        M=self.M;xprime=(x-2*j*self.p)%M
        ans=[None]*self.m
        for h,(start,z) in enumerate(self.boundaries):
            end=self.boundaries[(h+1)%self.m][0]
            a=(start-xprime)%M;b=(end-xprime)%M
            if self.m==1 or a>=b:
                s1=range_max(self.root,a,M)
                s2=range_max(self.root,0,b)
                latest=max((t for t in (s1,s2) if t is not None),default=None)
            else:
                latest=range_max(self.root,a,b)
            ans[z]=None if latest is None else j-latest
        return ans

def direct(index,j,x):
    M=index.M;bs=[v for v,z in index.boundaries];labels=[z for v,z in index.boundaries]
    latest=[None]*index.m
    for t in index.times:
        y=(x+2*(t-j)*index.p)%M
        z=labels[bisect_right(bs,y)-1]
        if latest[z] is None or t>latest[z]:latest[z]=t
    return [None if t is None else j-t for t in latest]

def small():
    rng=Random(600031);cases=queries=updates=0
    for m in range(1,9):
        for H in range(1,13):
            for rep in range(5):
                p=rng.randrange(1,1009);q=1009;K=m+H-1
                j=rng.choice([-10**18,1000,10**18])
                ix=Index(p,q,m,seed=1000+cases)
                for r in range(1,H+1):ix.add(j-r)
                ks=[0,K,K//2,rng.randrange(K+1)]
                xs=sample_phases(p,q,m,H,ks)[2]
                for x in xs:
                    assert ix.query(j,x)==direct(ix,j,x),(m,H,p,rep,'initial')
                    queries+=1
                for _ in range(4):
                    if ix.times and rng.randrange(2)==0:
                        t=rng.choice(tuple(sorted(ix.times)));ix.remove(t);updates+=1
                    else:
                        t=j-rng.randrange(1,H+11)
                        if t not in ix.times:ix.add(t);updates+=1
                    x=rng.choice(xs)
                    assert ix.query(j,x)==direct(ix,j,x),(m,H,p,rep,'mutated')
                    queries+=1
                for t in sorted(ix.times):ix.remove(t);updates+=1
                for r in range(1,H+1):ix.add(j-r);updates+=1
                for _ in range(3):
                    old=j;j+=1
                    ix.remove(old-H);ix.add(j-1);updates+=2
                    for x in (xs[0],xs[-1]):
                        assert ix.query(j,x)==direct(ix,j,x),(m,H,p,rep,'rolling')
                        queries+=1
                cases+=1
    return {'cases':cases,'queries':queries,'post_init_updates':updates}

def frozen():
    out=[];q=10**24;m=128;H=225;J=10**12+128
    for p in (262204504569236716045286,262204504569236716045287):
        ks=[352,0,1,4,32,88,176,264,352,176,351,225,61,126,127,163,164]
        xs=sample_phases(p,q,m,H,ks)[2]
        ix=Index(p,q,m)
        for r in range(1,H+1):ix.add(J-r)
        got=[ix.query(J,x) for x in xs]
        assert got==[direct(ix,J,x) for x in xs]
        from CHECK_R59 import youngest_floor_sum
        assert got==[youngest_floor_sum(p,q,m,H,x) for x in xs]
        for r in (4,17,221):ix.remove(J-r)
        assert ix.query(J,xs[7])==direct(ix,J,xs[7])
        for r in (4,17,221):ix.add(J-r)
        assert ix.query(J,xs[7])==got[7]
        J2=J+10**6
        iy=Index(p,q,m)
        for r in range(1,H+1):iy.add(J2-r)
        assert iy.query(J2,xs[7])==got[7]
        out.append({'p':str(p),'q':str(q),'m':m,'H':H,'checkpoint_queries':len(ks),'youngest_fields':len(ks)*m,'checked_arbitrary_deletions':3,'temporal_shift':10**6})
    return out

def long():
    p,q,m,H=262204504569236716045286,10**24,5,100003
    j=10**12+128;ix=Index(p,q,m)
    for r in range(1,H+1):ix.add(j-r)
    ks=[0,H//2,H,H+3];xs=sample_phases(p,q,m,H,ks)[2]
    for x in xs:assert ix.query(j,x)==direct(ix,j,x)
    for _ in range(500):
        ix.remove(j-H);ix.add(j);j+=1
    for x in xs[:2]:assert ix.query(j,x)==direct(ix,j,x)
    return {'m':m,'H':H,'initial_sources':H,'window_shifts':500,'individual_mutations':1000,'queries_with_direct_oracle':6,'final_sources':len(ix.times)}

def main():
    result={'science_pin':PIN,'model':'finite rational-circle with absolute time keyed sources','theorem_status':'AUTHOR_PROOF_ONLY','small':small(),'frozen':frozen(),'large':long()}
    Path(__file__).with_name('R60_CERTIFICATE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS_R60',json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
