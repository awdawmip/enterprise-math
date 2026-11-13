#!/usr/bin/env python3
"""R59 exact youngest-only circular RMQ; frozen S23/AV pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from bisect import bisect_left, bisect_right
from math import gcd
from random import Random
import json, time, statistics

PIN="43ec6098b1330ae86d0a7863be336c5d97f6ef34"
def cuts(p,q,K,count=None):
    if K==0:return []
    a,i,c,j=0,1,1,1
    while i+j<=K:
        if (a+c)*q<(i+j)*p:a,i=a+c,i+j
        else:c,j=c+a,j+i
    s=j; seq=[]
    for _ in range(K if count is None else min(K,count)):
        seq.append(s)
        s=s-i if s>i else (s+j if s+j<=K else s+j-i)
    return seq

def phases(p,q,m,H,ks):
    K=m+H-1; c=cuts(p,q,K,min(K,max(ks,default=0)+1))
    first=(c[0]*p)%q
    return [q+first if k==0 else ((c[-1]*p)%q if k==K else (c[k-1]*p)%q+(c[k]*p)%q) for k in ks]

class RMQ:
    def __init__(self,a):
        sz=1
        while sz<len(a):sz*=2
        self.sz=sz;self.T=[10**30]*(2*sz);self.T[sz:sz+len(a)]=a
        for i in range(sz-1,0,-1):self.T[i]=min(self.T[2*i],self.T[2*i+1])
        self.reads=0
    def minimum(self,l,r):
        v=10**30;l+=self.sz;r+=self.sz
        while l<r:
            if l&1:v=min(v,self.T[l]);self.reads+=1;l+=1
            if r&1:r-=1;v=min(v,self.T[r]);self.reads+=1
            l//=2;r//=2
        return v

class Index:
    def __init__(self,p,q,m,H):
        assert 0<p<q and m>=1 and H>=1 and q//gcd(p,q)>m+H-1
        self.p,self.q,self.m,self.H=p,q,m,H
        self.ages=cuts(p,q,H)
        self.Y=[2*((-r*p)%q) for r in self.ages]
        self.B=[0]+list(reversed(cuts(p,q,m-1)))
        self.b=[2*((z*p)%q) for z in self.B]
        assert all(x<y for x,y in zip(self.Y,self.Y[1:]))
        assert all(x<y for x,y in zip(self.b,self.b[1:]))
        self.R=RMQ(self.ages);self.arcs=0
    def query(self,x):
        if self.m==1:return [1]
        out=[None]*self.m
        for a,z in enumerate(self.B):
            start=(self.b[a]-x)%(2*self.q)
            end=(self.b[(a+1)%self.m]-x)%(2*self.q)
            l=bisect_left(self.Y,start);r=bisect_left(self.Y,end)
            if start<end:v=self.R.minimum(l,r);self.arcs+=1
            else:v=min(self.R.minimum(l,self.H),self.R.minimum(0,r));self.arcs+=2
            out[z]=v if v!=10**30 else None
        return out

def direct(p,q,m,H,x):
    b=sorted((2*((z*p)%q),z) for z in range(m))
    a=[t[0] for t in b];z=[t[1] for t in b];v=[None]*m
    for r in range(1,H+1):
        lab=z[bisect_right(a,(x-2*r*p)%(2*q))-1]
        if v[lab] is None:v[lab]=r
    return v

def grouped(p,q,m,H,ks):
    K=m+H-1;s=cuts(p,q,K)
    b=sorted(((z*p)%q,z) for z in range(m))
    phases_b=[2*x for x,z in b];B=[z for x,z in b];rank={z:i for i,z in enumerate(B)}
    x0=q+(s[0]*p)%q
    initial=[B[bisect_right(phases_b,(x0-2*r*p)%(2*q))-1] for r in range(1,H+1)]
    d=[0]*(H+2);ans={}
    for k in range(max(ks,default=0)+1):
        if k:
            u=s[k-1];lo=max(1,u-m+1);hi=min(H,u)
            d[lo]+=1;d[hi+1]-=1
        if k in ks:
            c=0;out=[None]*m
            for r in range(1,H+1):
                c+=d[r]
                z=B[(rank[initial[r-1]]-c)%m]
                if out[z] is None:out[z]=r
            ans[k]=out
    return [ans[k] for k in ks]

def evaluate(p,q,m,H,ks,with_group):
    idx=Index(p,q,m,H);xs=phases(p,q,m,H,ks)
    got=[idx.query(x) for x in xs]
    for x,v in zip(xs,got):assert direct(p,q,m,H,x)==v
    if with_group:assert got==grouped(p,q,m,H,ks)
    return idx,got

def small():
    rng=Random(590011); cases=queries=0
    for m in range(1,13):
        for H in range(1,16):
            K=m+H-1
            for rep in range(8):
                p=rng.randrange(1,1009)
                ks=[K,0,(rep*59+m*13+H*7)%(K+1),K//2,1,K]
                rng.shuffle(ks)
                evaluate(p,1009,m,H,ks,True)
                cases+=1;queries+=len(ks)
    assert (cases,queries)==(1440,8640)
    return {'cases':cases,'checkpoint_queries':queries,'all_exact':True}

def frozen():
    out=[]; q=10**24
    for p in (262204504569236716045286,262204504569236716045287):
        ks=[352,0,1,4,32,88,176,264,352,176,351,225,61,126,127,163,164]
        idx,v=evaluate(p,q,128,225,ks,True)
        assert v[0]==v[1]==v[8] and all(all(x is not None for x in y) for y in v)
        out.append({'p':str(p),'H':225,'m':128,'K':352,'Q':17,'arc_subqueries':idx.arcs,
                    'RMQ_tree_node_reads':idx.R.reads,'outputs':2176,'all_exact':True})
    return out

def long():
    p,q,m,H=262204504569236716045286,10**24,5,100003
    K=m+H-1
    ks=[K,0,K//2,10,100,10000,K//3,K-1,50000,25000,K,1]
    idx,v=evaluate(p,q,m,H,ks,False)
    assert len(v)==12 and all(len(y)==m for y in v)
    return {'m':m,'H':H,'K':K,'Q':len(v),'outputs':60,'arc_subqueries':idx.arcs,
            'RMQ_tree_node_reads':idx.R.reads,'all_exact':True}

def main():
    result={'pin':PIN,'small':small(),'frozen':frozen(),'large':long(),
            'evidence':'exact rational integer direct oracle; independent grouped updates for small/frozen',
            'status':'AUTHOR_CHECKED_UNREVIEWED'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
