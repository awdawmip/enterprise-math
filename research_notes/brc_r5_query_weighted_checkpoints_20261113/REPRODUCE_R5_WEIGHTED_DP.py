#!/usr/bin/env python3
"""Reproduce the exact R5 1D weighted k-median checkpoint experiment.
Provide the frozen offline-Fenwick fixture path as the first CLI argument.
Frozen scientific input commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from pathlib import Path
from fractions import Fraction
import bisect, json, sys

BASE = Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/em_r5_offline_20261112/VERIFY_R5_OFFLINE_FENWICK.py')
source = BASE.read_text()
d = {'__name__':'frozen_r5_query_weights'}
exec(compile(source[:source.index('# Compare 2 independent exact implementations at every prefix/sample.')],str(BASE),'exec'),d)
N,M,wall,pairs = d['N'],d['M'],d['walls'],d['pair2']
W=len(wall)
assert (N,M,W)==(2880,1065,953)
wi={v:i for i,v in enumerate(wall)}
f=[0]*W
for q,n in pairs:f[wi[(1-Fraction(36*q,n))/23]]+=1
E=[0]
for h in f:E.append(E[-1]+h)
assert E[-1]==M

def optimize(weights,K):
    n=len(E);P=[0];Q=[0]
    for x,w in zip(E,weights):
        P.append(P[-1]+w)
        Q.append(Q[-1]+x*w)
    cost=[];med=[]
    for i in range(n):
        a=[];b=[];mid=i
        for j in range(i,n):
            total=P[j+1]-P[i]
            while mid<j and 2*(P[mid+1]-P[i])<total:mid+=1
            lw=P[mid+1]-P[i]
            rw=P[j+1]-P[mid+1]
            v=E[mid]*lw-(Q[mid+1]-Q[i])+(Q[j+1]-Q[mid+1])-E[mid]*rw
            a.append(v);b.append(mid)
        cost.append(a);med.append(b)
    dp=cost[0][:]
    back=[None,None]
    for k in range(2,K+1):
        nxt=[10**30]*n
        choice=[None]*n
        for j in range(k-1,n):
            for t in range(k-2,j):
                v=dp[t]+cost[t+1][j-t-1]
                if v<nxt[j]:
                    nxt[j]=v
                    choice[j]=t
        dp=nxt;back.append(choice)
    j=n-1;centers=[]
    for k in range(K,1,-1):
        t=back[k][j]
        centers.append(med[t+1][j-t-1])
        j=t
    centers.append(med[0][j])
    centers.reverse()
    obj=sum(w*min(abs(E[b]-E[c]) for c in centers) for b,w in enumerate(weights))
    assert obj==dp[-1]
    return centers,obj

def minimax(K):
    def greedy(R):
        centers=[];b=0
        while b<=W:
            s=bisect.bisect_right(E,E[b]+R)-1
            centers.append(s)
            b=bisect.bisect_right(E,E[s]+R)
        return centers
    lo,hi=0,M
    while lo<hi:
        mid=(lo+hi)//2
        if len(greedy(mid))<=K:hi=mid
        else:lo=mid+1
    return greedy(lo)

def avg(w,C):
    return sum(t*min(abs(E[b]-E[c]) for c in C) for b,t in enumerate(w))/sum(w)

weights={
 'uniform':[1]*(W+1),
 'three_hotspots':[2+300*max(0,22-abs(b-W//7))//22+
                   280*max(0,30-abs(b-W//2))//30+
                   260*max(0,18-abs(b-7*W//8))//18 for b in range(W+1)]
}
summary={}
for name,w in weights.items():
    for k in (15,30):
        C,obj=optimize(w,k)
        C0=minimax(k)
        assert obj<=sum(t*min(abs(E[b]-E[c]) for c in C0) for b,t in enumerate(w))
        summary[f'{name}_K{k}']={
          'optimal_centers':C,'optimal_total':obj,
          'optimal_mean_event_edits':round(avg(w,C),5),
          'minimax_count':len(C0),
          'minimax_mean_event_edits':round(avg(w,C0),5)
        }
print(json.dumps({
 'status':'PASS_EXACT_WEIGHTED_MEDIAN_DP',
 'pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
 'summary':summary
},ensure_ascii=False,indent=2))
