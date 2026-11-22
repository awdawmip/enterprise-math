#!/usr/bin/env python3
"""Exact-integer certificate checks for low-triple 45-event Port-Euler histograms.

Usage:
  python R762JK_PORT_EULER_45_CHECK.py --t 7 --z 1
  python R762JK_PORT_EULER_45_CHECK.py --t 7 --z 0 --start 0 --end 25

Requires NumPy and SciPy/HiGHS. Solver outputs are proposed allocations;
each accepted 43-event witness is checked using exact integer constraints.
"""
import argparse
from itertools import combinations, permutations
from collections import Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

P=list(combinations(range(6),2)); S=list(combinations(range(6),3))
port_index={p:i for i,p in enumerate(P)}
support_index={s:i for i,s in enumerate(S)}
T=[tuple(port_index[p] for p in combinations(s,2)) for s in S]
E=[list(combinations(t,2)) for t in T]
PERM=[tuple(support_index[tuple(sorted(q[a] for a in s))] for s in S)
      for q in permutations(range(6))]
MATCHINGS=[m for k in range(4) for m in combinations(range(15),k)
           if len({a for i in m for a in P[i]})==2*k]
assert len(MATCHINGS)==76
A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for k,(u,v) in enumerate(E[s]):
        A[s,3*s+k]=1; A[20+u,3*s+k]=1; A[20+v,3*s+k]=1
for u in range(15): A[20+u,60+u]=-2
A=A.tocsr()

def ncomponents(tri):
    parent=list(range(15))
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    for s in tri:
        u,v,w=T[s]
        parent[root(v)]=root(u);parent[root(w)]=root(u)
    return len({root(v) for v in range(15)})

def all_essential_orbits(t):
    essential=set()
    for tri in combinations(range(20),t):
        c=ncomponents(tri)
        if all(ncomponents(tri[:i]+tri[i+1:])>c for i in range(t)):
            essential.add(sum(1<<s for s in tri))
    remaining=set(essential);reps=[]
    while remaining:
        m=min(remaining)
        orbit={sum(1<<q[s] for s in range(20) if m>>s&1) for q in PERM}
        assert orbit<=essential
        reps.append((m,len(orbit)));remaining-=orbit
    return len(essential),reps

def connected_components(alloc,active):
    graph={v:set() for v in active}
    for s in range(20):
        for k,(u,v) in enumerate(E[s]):
            if alloc[3*s+k]:
                assert u in active and v in active
                graph[u].add(v);graph[v].add(u)
    unseen=set(active);parts=[]
    while unseen:
        part={min(unseen)};todo=list(part);unseen-=part
        for v in todo:
            for w in graph[v] & unseen:
                unseen.remove(w);part.add(w);todo.append(w)
        parts.append(part)
    return parts

def verify(alloc,count,inactive):
    assert len(alloc)==60 and all(type(v)==int and 0<=v<=3 for v in alloc)
    assert sum(alloc)==43
    degree=[0]*15
    for s in range(20):
        assert sum(alloc[3*s:3*s+3])==count[s]
        for k,(u,v) in enumerate(E[s]):
            degree[u]+=alloc[3*s+k];degree[v]+=alloc[3*s+k]
    active=set(range(15))-set(inactive)
    assert all(degree[v]>=2 and degree[v]%2==0 for v in active)
    assert all(degree[v]==0 for v in inactive)
    assert len(connected_components(alloc,active))==1

def propose(count,inactive):
    active=set(range(15))-set(inactive)
    upper=[count[s] if u in active and v in active else 0
           for s in range(20) for u,v in E[s]]
    upper += [0 if u in inactive else 22 for u in range(15)]
    lower=[0]*60 + [0 if u in inactive else 1 for u in range(15)]
    equations=LinearConstraint(A,count+[0]*15,count+[0]*15)
    cuts=[]
    for round_no in range(15):
        r=milp(np.zeros(75),integrality=np.ones(75),bounds=Bounds(lower,upper),
               constraints=[equations]+cuts,options={'time_limit':2})
        if r.x is None:return None,r.status
        alloc=[int(round(float(v))) for v in r.x[:60]]
        parts=connected_components(alloc,active)
        if len(parts)==1:
            verify(alloc,count,inactive)
            return alloc,round_no
        for part in parts:
            cut=np.zeros(75)
            for s in range(20):
                for k,(u,v) in enumerate(E[s]):
                    if (u in part)!=(v in part):cut[3*s+k]=1
            cuts.append(LinearConstraint(cut,1,np.inf))
    return None,98

def run_case(t,z,start,end):
    singles=t-5-2*z; doubles=25-2*t+z
    assert t in range(5,11) and z>=0 and singles>=0 and doubles>=0
    assert t+doubles+singles+z==20 and 3*t+2*doubles+singles==45
    total,reps=all_essential_orbits(t)
    tested=labelled=locally_impossible=0
    inactive_hist=Counter();cut_hist=Counter()
    for i,(mask,orbit) in enumerate(reps):
        if not (start<=i<end):continue
        tri=[s for s in range(20) if mask>>s&1]
        covered={v for s in tri for v in T[s]}
        unused=sorted(set(range(15))-covered)
        other=[s for s in range(20) if s not in tri]
        if z==0:
            absent_port_sets=[m for m in MATCHINGS if set(m).isdisjoint(covered)]
        else:
            absent_port_sets=[m for k in range(len(unused)+1)
                              for m in combinations(unused,k)]
        for absent in combinations(other,z):
            remaining=[s for s in other if s not in absent]
            for once in combinations(remaining,singles):
                count=[3 if s in tri else 0 if s in absent
                       else 1 if s in once else 2 for s in range(20)]
                for inactive in absent_port_sets:
                    active=set(range(15))-set(inactive)
                    if any(sum(v in active for v in T[s])<2
                           for s in range(20) if count[s]):
                        locally_impossible+=1;continue
                    for j in tri:
                        reduced=count.copy();reduced[j]=1
                        alloc,rounds=propose(reduced,inactive)
                        if alloc is not None:break
                    assert alloc is not None,(t,z,i,tri,absent,once,inactive,rounds)
                    verify(alloc,reduced,inactive)
                    tested+=1;labelled+=orbit
                    inactive_hist[len(inactive)]+=1;cut_hist[rounds]+=1
    return dict(histogram=[t,doubles,singles,z],essential=total,orbits=len(reps),
                representative_checks=tested,labelled_configs=labelled,
                locally_impossible=locally_impossible,inactive=dict(inactive_hist),
                cuts=dict(cut_hist),range=[start,end])

def main():
    import json
    a=argparse.ArgumentParser();a.add_argument('--t',type=int,required=True)
    a.add_argument('--z',type=int,required=True)
    a.add_argument('--start',type=int,default=0)
    a.add_argument('--end',type=int,default=999)
    args=a.parse_args()
    print(json.dumps(run_case(args.t,args.z,args.start,args.end),sort_keys=True))

if __name__=='__main__':main()
