#!/usr/bin/env python3
"""R5 exact mean-optimal and same-minimax-radius checkpoint placement.
Run on the stacked R5 branch; imports the original immutable pinned rational fixture
from VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED, independently checks counts.

This file is a publication for clean-checkout replication; publish != execution.
All mathematical objective arithmetic and comparisons use Python integers/Fraction.
"""
import sys, json, itertools, random
from pathlib import Path
from bisect import bisect_left, bisect_right
from array import array
from fractions import Fraction

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "brc_r5_offline_fenwick_20261112"))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as P

N, M, pairs, walls, lohi = P.N, P.M, P.pairs, P.walls, P.lohi
assert (N,M,len(walls)) == (2880,1065,953)
wallid={w:i for i,w in enumerate(walls)}
codes=[wallid[(1-Fraction(36*q,n))/23] for q,n in pairs]
freq=[0]*len(walls)
for code in codes: freq[code]+=1
E=[0]
for z in freq: E.append(E[-1]+z)
assert len(E)==954 and E[-1]==M and all(a<b for a,b in zip(E,E[1:]))
x=E
n=len(x)
PREF=[0]
for v in x:PREF.append(PREF[-1]+v)
INF=10**30

def segment(i,j,s=None):
    if s is None:s=(i+j)//2
    v=x[s]
    return (v*(s-i+1)-(PREF[s+1]-PREF[i])+
            (PREF[j+1]-PREF[s+1])-v*(j-s))

def unconstrained(K):
    # Standard exact K-median recurrence, accelerated via Monge monotone argmins.
    prev=[0]+[INF]*n
    row_choices=[]
    for k in range(1,K+1):
        cur=[INF]*(n+1)
        choices=array('H',[0])*(n+1)
        def dc(jlo,jhi,ilo,ihi):
            if jlo>jhi:return
            j=(jlo+jhi)//2
            best=(INF,-1)
            for i in range(max(k-1,ilo),min(j-1,ihi)+1):
                val=prev[i]+segment(i,j-1)
                if val<best[0]:best=(val,i)
            assert best[1]>=0
            cur[j]=best[0];choices[j]=best[1]
            dc(jlo,j-1,ilo,best[1])
            dc(j+1,jhi,best[1],ihi)
        dc(k,n,k-1,n-1)
        prev=cur;row_choices.append(choices)
    out=[];j=n
    for k in range(K,0,-1):
        i=row_choices[k-1][j]
        out.append((i,j-1,(i+j-1)//2))
        j=i
    assert j==0
    out.reverse()
    assert sum(segment(a,b,s) for a,b,s in out)==prev[n]
    return prev[n],[s for a,b,s in out]

def greedy(R):
    centers=[];i=0
    while i<n:
        j=bisect_right(x,x[i]+R)-1
        centers.append(j)
        i=bisect_right(x,x[j]+R)
    return centers

def minimax(K):
    a,b=0,M
    while a<b:
        mid=(a+b)//2
        if len(greedy(mid))<=K:b=mid
        else:a=mid+1
    return a,greedy(a)

def bounded_cost(i,j,R):
    if x[j]-x[i]>2*R:return INF,None
    lo=bisect_left(x,x[j]-R,i,j+1)
    hi=bisect_right(x,x[i]+R,i,j+1)-1
    if lo>hi:return INF,None
    s=max(lo,min(hi,(i+j)//2))
    return segment(i,j,s),s

def same_radius(K,R):
    # Independent finite full DP; no Monge acceleration and no heuristic.
    prev=[0]+[INF]*n
    rows=[]
    for k in range(1,K+1):
        cur=[INF]*(n+1)
        arg=array('H',[0])*(n+1)
        for j in range(k,n+1):
            best=INF;bi=0
            for i in range(j-1,k-2,-1):
                if x[j-1]-x[i]>2*R:break
                c,_=bounded_cost(i,j-1,R)
                y=prev[i]+c
                if y<best:best=y;bi=i
            cur[j]=best;arg[j]=bi
        rows.append(arg);prev=cur
    assert prev[n]<INF
    cells=[];j=n
    for k in range(K,0,-1):
        i=rows[k-1][j]
        c,s=bounded_cost(i,j-1,R)
        assert c<INF
        cells.append((i,j-1,s));j=i
    assert j==0
    cells.reverse()
    centers=[s for _,_,s in cells]
    assert sum(segment(i,j,s) for i,j,s in cells)==prev[n]
    return prev[n],centers

def metrics(centers):
    d=[min(abs(v-x[s]) for s in centers) for v in x]
    return {'total':sum(d),'max':max(d),'zero':d.count(0)}

# Exhaustive independent cross-check for the DP recurrence on 32 small exact inputs.
for trial in range(32):
    y=sorted(random.Random(987312+trial).sample(range(100),8))
    for k in range(1,5):
        brute=min(sum(min(abs(v-y[s]) for s in S) for v in y)
                  for S in itertools.combinations(range(8),k))
        dp=[0]+[INF]*8
        for kk in range(1,k+1):
            cur=[INF]*9
            for j in range(kk,9):
                for i in range(kk-1,j):
                    m=(i+j-1)//2
                    c=sum(abs(y[t]-y[m]) for t in range(i,j))
                    cur[j]=min(cur[j],dp[i]+c)
            dp=cur
        assert brute==dp[-1]

order=sorted(range(M),key=lambda t:(codes[t],t))
checks=0
results={}
for K in (15,57,213):
    R,g= minimax(K)
    uncon_cost,u=unconstrained(K)
    fixed_cost,f=same_radius(K,R)
    a,b,c=metrics(g),metrics(f),metrics(u)
    assert (a['max'],b['max'])==(R,R)
    assert (b['total'],c['total'])==(fixed_cost,uncon_cost)
    assert c['total']<=b['total']<=a['total']
    # Test the actual signed-correction data carrier for both new center sets.
    for centers in (u,f):
        ys=[x[s] for s in centers]
        masks=[];mask=0;ptr=0
        for z in ys:
            while ptr<z:
                mask|=1<<order[ptr]
                ptr+=1
            masks.append(mask)
        def count(v,r):
            rank=bisect_right(walls,r);target=x[rank]
            t=bisect_left(ys,target)
            if t==0:z=0
            elif t==len(ys):z=t-1
            else:z=t if ys[t]-target<target-ys[t-1] else t-1
            l,h=lohi[v]
            if l==h:return 0
            y=ys[z]
            value=((masks[z]>>l)&((1<<(h-l))-1)).bit_count()
            if y<target:
                for j in range(y,target):value+=int(l<=order[j]<h)
            elif y>target:
                for j in range(target,y):value-=int(l<=order[j]<h)
            return value
        for r in P.prev.samples:
            for v in range(N):
                assert count(v,r)==P.prev.pinned.count(v,r)
                checks+=1
        for boundary in range(len(E)):
            r=walls[boundary-1] if boundary else walls[0]-1
            active=[int(code<boundary) for code in codes]
            prefix=[0]
            for bit in active:prefix.append(prefix[-1]+bit)
            for v in range(0,N,23):
                l,h=lohi[v]
                assert count(v,r)==prefix[h]-prefix[l]
                checks+=1
    results[str(K)]={'minimax_radius':R,'greedy_centers_used':len(g),
                     'greedy_total':a['total'],
                     'same_radius_total':b['total'],
                     'same_radius_max':b['max'],
                     'unconstrained_total':c['total'],
                     'unconstrained_max':c['max'],
                     'same_radius_centers':f,
                     'unconstrained_centers':u}
assert checks==1066824
out={'science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'nodes':N,'certificates':M,'distinct_walls':len(walls),
     'uniform_query_boundaries':len(E),
     'tiny_exhaustive_checks':128,'signed_query_comparisons':checks,
     'results':results}
print(json.dumps(out,ensure_ascii=False,indent=2))
