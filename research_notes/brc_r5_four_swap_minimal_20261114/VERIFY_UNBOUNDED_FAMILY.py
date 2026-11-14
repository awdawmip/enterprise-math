#!/usr/bin/env python3
"""Exact integer DP and direct combinatorial checks for an unbounded one-gap optimizer-recourse family."""
from itertools import combinations
import json

def family(k):
    assert k >= 2
    n = 3*k-2
    x = (0, 3) + tuple(range(5, n+3))
    y = tuple(v - (i > 0) for i,v in enumerate(x))
    old = (0,) + tuple(range(2,n,3))
    new = (1,) + tuple(range(3,n,3))
    return x,y,old,new

def score(x,s):
    d = [min(abs(x[i]-x[j]) for j in s) for i in range(len(x))]
    return max(d),sum(d)

def optimal_dp(x,k,reference=()):
    n=len(x); chosen=set(reference)
    inf=10**15
    costs=[inf]*n; ways=[0]*n; overlap=[-10**9]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            costs[j]=sum(x[j]-x[t] for t in range(j))
            ways[j]=1
            overlap[j]=int(j in chosen)
    for ct in range(2,k+1):
        nxt=[inf]*n; nways=[0]*n; noverlap=[-10**9]*n
        for j in range(n):
            for i in range(j-1,-1,-1):
                if x[j]-x[i]>7:break
                if costs[i]==inf:continue
                d=[min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)]
                if any(z>2 for z in d):continue
                cand=costs[i]+sum(d)
                if cand<nxt[j]:
                    nxt[j]=cand;nways[j]=ways[i];noverlap[j]=overlap[i]+int(j in chosen)
                elif cand==nxt[j]:
                    nways[j]+=ways[i]
                    noverlap[j]=max(noverlap[j],overlap[i]+int(j in chosen))
        costs,ways,overlap=nxt,nways,noverlap
    best=inf;num=0;maxoverlap=-10**9
    for j in range(n):
        if costs[j]==inf or x[-1]-x[j]>2:continue
        cand=costs[j]+sum(x[t]-x[j] for t in range(j+1,n))
        if cand<best:
            best,num,maxoverlap=cand,ways[j],overlap[j]
        elif cand==best:
            num+=ways[j];maxoverlap=max(maxoverlap,overlap[j])
    return (best,num,maxoverlap)

def brute(x,k):
    cost=None;opts=[]
    for s in combinations(range(len(x)),k):
        r,c=score(x,s)
        if r>2:continue
        if cost is None or c<cost:cost,opts=c,[s]
        elif c==cost:opts.append(s)
    return cost,opts

def main():
    rows=[]
    for k in range(2,51):
        x,y,t,s=family(k)
        assert len(x)==3*k-2 and len(t)==len(s)==k and not(set(t)&set(s))
        assert x[1]-x[0]==3 and y[1]-y[0]==2
        assert all(x[i+1]-x[i] in (1,2,3) for i in range(len(x)-1))
        assert score(x,t)==(2,2*k-1) and score(y,s)==(2,2*k-1)
        a=optimal_dp(x,k,s);b=optimal_dp(y,k)
        assert a==(2*k-1,1,0),(k,a)
        assert b[0]==2*k-1,(k,b)
        if k<=6:
            ca,A=brute(x,k);cb,B=brute(y,k)
            assert ca==cb==2*k-1 and A==[t] and s in B
        rows.append({'k':k,'n':len(x),'old_cost':a[0],'new_cost':b[0],
                     'old_optimum_count':a[1],'max_old_overlap_with_new_S':a[2],
                     'replacements':k,'new_optimum_count':b[1]})
    return {'status':'PASS_EXACT_UNBOUNDED_SINGLE_GAP_RECOURSE_K2_TO_K50',
            'verified_range':'2<=K<=50 (checks only; general theorem has symbolic proof)',
            'single_closed_gap':'index 0, length 3 to 2',
            'family':'n=3K-2, x=(0,3,5,6,...,n+2), y=(0,2,4,5,...,n+1)',
            'old_optimum':'T=(0,2,5,8,...,3K-4) unique',
            'new_optimum_witness':'S=(1,3,6,9,...,3K-3)',
            'both_optimal_cost':'2K-1',
            'minimum_replacements':'K',
            'brute_force_k':[2,3,4,5,6],
            'dp_k':[2,50],
            'nonscoped_954_event_conclusion':False,
            'independent_review':'NOT_REVIEWED',
            'results':rows}

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
