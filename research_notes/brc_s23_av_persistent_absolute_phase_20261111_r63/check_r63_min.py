"""Compact independently runnable R63 persistent phase-index check (exact rational)."""
from fractions import Fraction as F
from bisect import bisect_right
from math import gcd
from random import Random

class N:
    def __init__(self,k,prio,l=None,r=None):
        self.k,self.prio,self.l,self.r=k,prio,l,r
        self.mx=max(k[1],l.mx if l else k[1],r.mx if r else k[1])

def split(n,k):
    if not n:return None,None
    if n.k<k:
        a,b=split(n.r,k);return N(n.k,n.prio,n.l,a),b
    a,b=split(n.l,k);return a,N(n.k,n.prio,b,n.r)

def merge(a,b):
    if not a:return b
    if not b:return a
    if a.prio>b.prio:return N(a.k,a.prio,a.l,merge(a.r,b))
    return N(b.k,b.prio,merge(a,b.l),b.r)

def add(n,k,prio):
    if not n:return N(k,prio)
    if k==n.k:raise ValueError('duplicate timestamp')
    if prio>n.prio:
        a,b=split(n,k);return N(k,prio,a,b)
    if k<n.k:return N(n.k,n.prio,add(n.l,k,prio),n.r)
    return N(n.k,n.prio,n.l,add(n.r,k,prio))

def erase(n,k):
    if not n:raise KeyError(k)
    if k==n.k:return merge(n.l,n.r)
    if k<n.k:return N(n.k,n.prio,erase(n.l,k),n.r)
    return N(n.k,n.prio,n.l,erase(n.r,k))

def mx(a,b):
    return b if a is None else (a if b is None else max(a,b))

def query(n,lo,hi):
    if lo>=hi:return None
    while n and not lo<=n.k[0]<hi:
        n=n.r if n.k[0]<lo else n.l
    if not n:return None
    res=n.k[1];a=n.l
    while a:
        if a.k[0]>=lo:
            res=max(res,a.k[1]);res=mx(res,a.r.mx if a.r else None);a=a.l
        else:a=a.r
    b=n.r
    while b:
        if b.k[0]<hi:
            res=max(res,b.k[1]);res=mx(res,b.l.mx if b.l else None);b=b.r
        else:b=b.l
    return res

class Index:
    def __init__(self,p,q):
        self.p,self.q=p,q;self.rand=Random(63011);self.prios={};self.arcs={}
    def key(self,t):return ((t*self.p)%self.q,t)
    def insert(self,root,t):
        if t not in self.prios:self.prios[t]=self.rand.getrandbits(128)
        return add(root,self.key(t),self.prios[t])
    def delete(self,root,t):return erase(root,self.key(t))
    def age(self,root,m,z,j,x):
        if m not in self.arcs:
            assert m<=self.q//gcd(self.p,self.q)
            bs=sorted(((h*self.p)%self.q,h) for h in range(m))
            arr=[None]*m
            for i,(a,h) in enumerate(bs):arr[h]=(a,bs[(i+1)%m][0])
            self.arcs[m]=arr
        a,b=self.arcs[m][z]
        offset=(x-F((j*self.p)%self.q,self.q))%1
        lo=(F(a,self.q)-offset)%1*self.q
        hi=(F(b,self.q)-offset)%1*self.q
        if lo<hi:t=query(root,lo,hi)
        elif lo>hi:t=mx(query(root,lo,self.q),query(root,0,hi))
        else:t=root.mx if root else None # single history arc
        return None if t is None else j-t

def direct(p,q,active,m,z,j,x):
    bs=sorted(((h*p)%q,h) for h in range(m))
    for t in sorted(active,reverse=True):
        ph=(x+F(((t-j)*p)%q,q))%1
        label=bs[(bisect_right([F(a,q) for a,_ in bs],ph)-1)%m][1]
        if label==z:return j-t
    return None

def run():
    rand=Random(20261111);checks=updates=old_checks=0
    for case in range(100):
        q=rand.randrange(5,61);p=rand.choice([i for i in range(1,q) if gcd(i,q)==1]);m=rand.randrange(1,min(q,8)+1)
        ix=Index(p,q);r=None;S=set();hist=[(r,frozenset(S))];base=10**18*rand.randrange(1,100)
        for step in range(30):
            if S and rand.randrange(2):
                t=rand.choice(sorted(S));r=ix.delete(r,t);S.remove(t)
            else:
                t=base+rand.randrange(-q,3*q)
                if t not in S:r=ix.insert(r,t);S.add(t)
            updates+=1;hist.append((r,frozenset(S)))
            j=base+10*q+step;x=F(rand.randrange(71),rand.randrange(2,53))
            for z in range(m):
                assert ix.age(r,m,z,j,x)==direct(p,q,S,m,z,j,x);checks+=1
            if step%4==0:
                old,os=rand.choice(hist)
                for z in range(m):
                    assert ix.age(old,m,z,j+10**24,x+F(1,7))==direct(p,q,os,m,z,j+10**24,x+F(1,7));old_checks+=1
        t=base-q;old=ix.insert(ix.insert(None,t),t+q)
        assert old.mx==t+q and ix.delete(old,t+q).mx==t
    for p in [262204504569236716045286,262204504569236716045287]:
        q=10**24;m=128;H=225;j=10**12+128
        ix=Index(p,q);r=None;S=set(range(j-H,j))
        for t in sorted(S):r=ix.insert(r,t)
        for x,jj in [(F(0),j),(F(1,3),j),(F(2,7),j+10**18)]:
            for z in range(m):
                assert ix.age(r,m,z,jj,x)==direct(p,q,S,m,z,jj,x);checks+=1
    print({'status':'PASS','dynamic_updates':updates,'exact_current_queries':checks,
           'historical_version_queries':old_checks,'frozen_endpoint_labels':2*128*3})

if __name__=='__main__':run()
