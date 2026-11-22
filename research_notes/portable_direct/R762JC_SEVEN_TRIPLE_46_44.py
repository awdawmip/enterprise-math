#!/usr/bin/env python3
"""R762JC reproducible finite proof search for (7,12,1,0): 46 -> 44.
Requires Python, NumPy, SciPy (milp/HiGHS); solver proposes witnesses.
Each witness is independently verified with integer degree, support and BFS tests.
"""
from itertools import combinations, permutations
from collections import Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

P = list(combinations(range(6),2)); S = list(combinations(range(6),3))
pi={p:i for i,p in enumerate(P)}; si={s:i for i,s in enumerate(S)}
T=[tuple(pi[p] for p in combinations(s,2)) for s in S]
E=[tuple(combinations(t,2)) for t in T]
M=[m for k in range(4) for m in combinations(range(15),k)
   if len({a for i in m for a in P[i]})==2*k]
perms=[tuple(si[tuple(sorted(q[a] for a in s))] for s in S)
       for q in permutations(range(6))]
assert len(M)==76
A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for e,(u,v) in enumerate(E[s]):
        A[s,3*s+e]=1
        A[20+u,3*s+e]=1; A[20+v,3*s+e]=1
for u in range(15): A[20+u,60+u]=-2
A=A.tocsr()

def triangle_components(t):
    par=list(range(15))
    def f(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for s in t:
        a,b,c=T[s]
        par[f(b)]=f(a);par[f(c)]=f(a)
    return len({f(i) for i in range(15)})

def essential_reps():
    ess=[]
    for t in combinations(range(20),7):
        c=triangle_components(t)
        if all(triangle_components(t[:j]+t[j+1:])>c for j in range(7)):
            ess.append(sum(1<<s for s in t))
    assert len(ess)==23700
    left=set(ess); out=[]
    while left:
        m=min(left)
        orbit={sum(1<<q[s] for s in range(20) if m>>s&1) for q in perms}
        assert orbit<=set(ess)
        out.append((m,len(orbit)));left-=orbit
    assert len(out)==55 and sum(z for _,z in out)==23700
    return out

def exact_components(x,active):
    g={u:set() for u in active}
    for s in range(20):
        for e,(u,v) in enumerate(E[s]):
            if x[3*s+e]>0:
                assert u in active and v in active
                g[u].add(v);g[v].add(u)
    unseen=set(active);out=[]
    while unseen:
        c={next(iter(unseen))};q=list(c);unseen-=c
        for u in q:
            for v in g[u]:
                if v in unseen:unseen.remove(v);c.add(v);q.append(v)
        out.append(c)
    return out

def verify_exact(x, counts, inactive):
    assert x is not None and len(x)==60 and all(isinstance(v,int) and 0<=v<=3 for v in x)
    assert sum(x)==44
    active=set(range(15))-set(inactive)
    degrees=[0]*15
    for s in range(20):
        assert sum(x[3*s:3*s+3])==counts[s]
        for e,(u,v) in enumerate(E[s]):
            k=x[3*s+e]
            degrees[u]+=k;degrees[v]+=k
    assert all(degrees[u]>0 and degrees[u]%2==0 for u in active)
    assert all(degrees[u]==0 for u in inactive)
    assert len(exact_components(x,active))==1

def solve(counts,inactive):
    active=set(range(15))-set(inactive)
    upper=[counts[s] if u in active and v in active else 0
           for s in range(20) for u,v in E[s]]
    upper += [0 if u in inactive else 22 for u in range(15)]
    lower=[0]*60+[0 if u in inactive else 1 for u in range(15)]
    eq=LinearConstraint(A,counts+[0]*15,counts+[0]*15)
    cuts=[]
    for trial in range(10):
        r=milp(np.zeros(75),integrality=np.ones(75),bounds=Bounds(lower,upper),
               constraints=[eq]+cuts,options={'time_limit':5})
        if r.x is None:raise AssertionError(('no integer candidate',r.status,r.message))
        x=list(map(int,np.rint(r.x[:60])))
        parts=exact_components(x,active)
        if len(parts)==1:
            verify_exact(x,counts,inactive)
            return x,trial
        for comp in parts:
            row=np.zeros(75)
            for s in range(20):
                for e,(u,v) in enumerate(E[s]):
                    if (u in comp)!=(v in comp):row[3*s+e]=1
            cuts.append(LinearConstraint(row,1,np.inf))
    raise AssertionError('connectivity cuts exhausted')

def main():
    reps=essential_reps()
    n=0;labelled=0;by_inactive=Counter();cuts=Counter()
    for mask,os in reps:
        t=[s for s in range(20) if mask>>s&1]
        covered={u for s in t for u in T[s]}
        for inactive in M:
            if not set(inactive).isdisjoint(covered):continue
            for singleton in range(20):
                if singleton in t:continue
                counts=[3 if s in t else 1 if s==singleton else 2 for s in range(20)]
                counts[t[0]]=1
                x,rounds=solve(counts,inactive)
                verify_exact(x,counts,inactive)
                n+=1;labelled+=os;by_inactive[len(inactive)]+=1;cuts[rounds]+=1
    assert n==1755 and labelled==741780
    assert by_inactive=={0:715,1:962,2:78}
    print('PASS R762JC: 77,520 subsets, 23,700 all-essential, 55 S6 orbits')
    print('1755/1755 exact integer witnesses; labelled cases:',labelled)
    print('inactive cases:',dict(sorted(by_inactive.items())))
    print('connectivity cut rounds:',dict(sorted(cuts.items())))
if __name__=='__main__': main()
