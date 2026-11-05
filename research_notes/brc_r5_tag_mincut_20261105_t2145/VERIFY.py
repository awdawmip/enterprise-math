#!/usr/bin/env python3
"""Exact Fraction verification of the R5 finite-tag deficit/min-cut theorem."""
from collections import deque
from fractions import Fraction as F
from itertools import product
from random import Random

def pos(x): return max(F(0),x)

def brute(w,A,u,T):
    k=len(T[0])
    full=sum(w[i]*max(F(0),A[i],A[i]+u[i]) for i in range(len(w)))
    tag=max(sum(w[i]*pos(A[i]+u[i]*sum(T[i][y]*z[y] for y in range(k)))
                for i in range(len(w))) for z in product([0,1],repeat=k))
    return full-tag

def bound(w,A,u,T):
    neg=[i for i in range(len(w)) if A[i]>0 and u[i]<0]
    plus=[i for i in range(len(w)) if A[i]+u[i]>0 and u[i]>0]
    return sum(min(sum(w[i]*min(A[i],-u[i])*T[i][y] for i in neg),
                   sum(w[j]*min(A[j]+u[j],u[j])*T[j][y] for j in plus))
               for y in range(len(T[0])))

def flowcut(w,A,u,T):
    m,k=len(w),len(T[0])
    neg=[i for i in range(m) if A[i]>0 and u[i]<0]
    plus=[i for i in range(m) if A[i]+u[i]>0 and u[i]>0]
    s=0; nb=1; yb=nb+len(neg); pb=yb+k; t=pb+len(plus)
    adj=[set() for _ in range(t+1)]
    cap=[{} for _ in range(t+1)]
    res=[{} for _ in range(t+1)]
    def add(v,q,c):
        assert c>=0
        if not c:return
        adj[v].add(q);adj[q].add(v)
        cap[v][q]=cap[v].get(q,F(0))+c
        res[v][q]=res[v].get(q,F(0))+c
        res[q].setdefault(v,F(0))
    for j,i in enumerate(neg):
        a=nb+j
        add(s,a,w[i]*A[i])
        for y in range(k): add(a,yb+y,w[i]*(-u[i])*T[i][y])
    for j,i in enumerate(plus):
        a=pb+j
        add(a,t,w[i]*(A[i]+u[i]))
        for y in range(k): add(yb+y,a,w[i]*u[i]*T[i][y])
    flow=F(0)
    while True:
        parent={s:-1};Q=deque([s])
        while Q and t not in parent:
            v=Q.popleft()
            for q in sorted(adj[v]):
                if q not in parent and res[v].get(q,F(0))>0:
                    parent[q]=v;Q.append(q)
                    if q==t:break
        if t not in parent:break
        path=[];q=t
        while q!=s:
            v=parent[q];path.append((v,q));q=v
        d=min(res[v][q] for v,q in path)
        for v,q in path:
            res[v][q]-=d;res[q][v]=res[q].get(v,F(0))+d
        flow+=d
    reach={s};Q=deque([s])
    while Q:
        v=Q.popleft()
        for q in sorted(adj[v]):
            if q not in reach and res[v].get(q,F(0))>0:
                reach.add(q);Q.append(q)
    cut=sum(c for v in reach for q,c in cap[v].items() if q not in reach)
    assert cut==flow
    z=tuple(int(yb+y not in reach) for y in range(k))
    return cut,z,t+1,sum(len(x) for x in cap)

def check(w,A,u,T):
    assert len(w)==len(A)==len(u)==len(T)
    assert all(x>0 for x in w)
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in T)
    D=brute(w,A,u,T); mc,z,n,e=flowcut(w,A,u,T); B=bound(w,A,u,T)
    assert D==mc and 0<=B<=D
    return D,B,z,n,e

def main():
    w=[F(1,2),F(1,2)];A=[F(1,200),-F(47,400)];u=[-F(9,500),F(49,400)]
    print("MODEL S (inherited Bellman coefficients; not new tree execution)")
    for eta in [F(0),F(1,100),F(10,281),F(1,20),F(1,2)]:
        D,B,z,n,e=check(w,A,u,[[1-eta,eta],[eta,1-eta]])
        assert D==min(F(281)*eta/4000,F(1,400)) and B==eta/200
        print("eta=%s D=%s B=%s optimal_z=%s nodes=%s arcs=%s"%(eta,D,B,z,n,e))
    w=[F(1,3),F(1,2),F(1,6)]
    A=[F(1,7),-F(1,5),F(1,9)];u=[-F(1,3),F(3,10),F(0)]
    T=[[F(1,2),F(1,3),F(1,6)],[F(1,6),F(1,2),F(1,3)],[F(1,4),F(1,4),F(1,2)]]
    D,B,z,n,e=check(w,A,u,T)
    assert (D,B)==(F(1,21),F(9,280))
    print("THREE_HISTORY D=%s B=%s optimal_z=%s nodes=%s arcs=%s"%(D,B,z,n,e))
    rng=Random(202611052140);cnt=0
    for trial in range(512):
        m=rng.randrange(1,7);k=rng.randrange(1,7)
        a=[rng.randrange(1,8) for _ in range(m)]
        w=[F(t,sum(a)) for t in a]
        A=[F(rng.randrange(-8,9),rng.randrange(1,8)) for _ in range(m)]
        u=[F(rng.randrange(-8,9),rng.randrange(1,8)) for _ in range(m)]
        T=[]
        for _ in range(m):
            a=[rng.randrange(0,8) for _ in range(k)]
            if sum(a)==0:a[0]=1
            T.append([F(t,sum(a)) for t in a])
        D,B,z,n,e=check(w,A,u,T)
        neg={y for i in range(m) if A[i]>0 and u[i]<0 for y in range(k) if T[i][y]>0}
        plus={y for i in range(m) if A[i]+u[i]>0 and u[i]>0 for y in range(k) if T[i][y]>0}
        assert (D>0)==bool(neg&plus)
        cnt+=int(D>0)
    print("RANDOM_EXACT_CASES=512 conflicts=%s positive_deficits=%s"%(cnt,cnt))
    print("PASS_EXACT_R5_TAG_MINCUT_REDUCTION")
if __name__=="__main__":main()
