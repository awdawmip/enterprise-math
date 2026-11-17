#!/usr/bin/env python3
"""Exact finite checker for X6 conditional two-chain opposing links.
This is a mathematical dependency test, NOT native physical Cell/Link/Port approval.
"""
from collections import Counter
from itertools import combinations
import json

def acyclic(r,s,t,u):
    return (r<u or t<s)

def polynomial_hist(a,b,r,s,t,u):
    assert acyclic(r,s,t,u)
    legal=Counter()
    for i in range(a+1):
        for j in range(b+1):
            if (j<s or i>=r) and (i<u or j>=t):
                legal[i+j]+=1
    count=(a+1)*(b+1)-r*(b-s+1)-(a-u+1)*t
    assert sum(legal.values())==count
    return [legal[k] for k in range(a+b+1)]

def dp_extensions(a,b,r,s,t,u):
    # Independent count of legal grid paths / full linear extensions
    prev={(0,0):1}
    for _ in range(a+b):
        cur=Counter()
        for (i,j),m in prev.items():
            for ni,nj in ((i+1,j),(i,j+1)):
                if ni<=a and nj<=b and (nj<s or ni>=r) and (ni<u or nj>=t):
                    cur[ni,nj]+=m
        prev=dict(cur)
    return prev.get((a,b),0)

def brute(a,b,r,s,t,u):
    # Directly enumerate every binom(a+b,a) event serialization
    n=0
    reachable=set()
    for places in combinations(range(a+b),a):
        pos=set(places)
        word=['A' if k in pos else 'B' for k in range(a+b)]
        alpha=[k for k,c in enumerate(word) if c=='A']
        beta=[k for k,c in enumerate(word) if c=='B']
        if not(alpha[r-1] < beta[s-1] and beta[t-1] < alpha[u-1]):
            continue
        n+=1
        i=j=0
        reachable.add((i,j))
        for c in word:
            if c=='A':i+=1
            else:j+=1
            reachable.add((i,j))
    counts=Counter(i+j for i,j in reachable)
    return n,[counts[k] for k in range(a+b+1)]

def check():
    tested=valid=cyclic=0
    examples=[]
    requested={(2,2,1,2,1,2),(3,3,2,2,3,3),(4,4,1,3,2,4)}
    for a in range(1,5):
        for b in range(1,5):
            for r in range(1,a+1):
                for u in range(1,a+1):
                    for s in range(1,b+1):
                        for t in range(1,b+1):
                            tested+=1
                            n,h=brute(a,b,r,s,t,u)
                            if not acyclic(r,s,t,u):
                                cyclic+=1
                                assert n==0,(a,b,r,s,t,u,'cyclic')
                            else:
                                valid+=1
                                predicted=polynomial_hist(a,b,r,s,t,u)
                                assert predicted==h,(a,b,r,s,t,u,predicted,h)
                                assert dp_extensions(a,b,r,s,t,u)==n and n>0
                                if (a,b,r,s,t,u) in requested:
                                    examples.append({'parameters':[a,b,r,s,t,u],
                                                     'cut_histogram':h,
                                                     'total_ideals':sum(h),
                                                     'linear_extensions':n})
    assert tested==900 and valid==500 and cyclic==400
    return {'scope':'two conditional V1R local event chains, opposing hypothetical crosslinks',
            'admitted_native_event':False, 'cases':tested,
            'acyclic_verified':valid,'cyclic_zero_linear_extension_verified':cyclic,
            'proof_comparison':'enumerated words/prefix ideals vs rectangle polynomial and DP',
            'examples':examples}

if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
