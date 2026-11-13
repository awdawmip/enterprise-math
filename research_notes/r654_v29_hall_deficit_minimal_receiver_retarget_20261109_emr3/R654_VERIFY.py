#!/usr/bin/env python3
"""Exact finite verification of R654 terminal V29 TRANSFER margin retargeting.
Combinatorial typed event-count observer only; no physical propagation simulation.
"""
from itertools import product
import json

def neighbors(edges,na,nb):
    return [tuple(j for j in range(nb) if (i,j) in edges) for i in range(na)]

def reachable_receivers(s,adj,nb):
    seen={(0,)*nb}
    for m,opts in zip(s,adj):
        if m and not opts:
            return set()
        candidates=[]
        if not m:
            candidates=[(0,)*nb]
        else:
            for dest in product(opts,repeat=m):
                v=[0]*nb
                for j in dest: v[j]+=1
                candidates.append(tuple(v))
        seen={tuple(u+v for u,v in zip(q,p)) for q in seen for p in candidates}
    return seen

def deficit(s,t,adj):
    best=0; arg=()
    for mask in range(1<<len(s)):
        U=tuple(i for i in range(len(s)) if mask & (1<<i))
        N={b for i in U for b in adj[i]}
        d=sum(s[i] for i in U)-sum(t[j] for j in N)
        if d>best:
            best,arg=d,U
    return best,arg

def cost(t,z):
    assert sum(t)==sum(z)
    return sum(abs(a-b) for a,b in zip(t,z))//2

def check(edges,na,nb,limit,stats):
    adj=neighbors(edges,na,nb)
    dual=neighbors({(j,i) for i,j in edges},nb,na)
    for s in product(range(limit+1),repeat=na):
        poss=reachable_receivers(s,adj,nb)
        for t in product(range(limit+1),repeat=nb):
            if sum(s)!=sum(t): continue
            stats['balanced_tested']+=1
            d,U=deficit(s,t,adj)
            if any(s[i]>0 and not adj[i] for i in range(na)):
                assert not poss
                stats['isolated_sender_infeasible']+=1
                continue
            assert poss
            actual=min(cost(t,z) for z in poss)
            assert actual==d,(edges,s,t,d,U,actual)
            stats['deficit_equals_min_retarget']+=1
            if d: stats['positive_deficit']+=1
            if not d: assert t in poss
            if all(not t[j] or dual[j] for j in range(nb)):
                dualposs=reachable_receivers(t,dual,na)
                d2,_=deficit(t,s,dual)
                assert d2==d==min(cost(s,z) for z in dualposs)
                stats['symmetric_retarget_checks']+=1
            optimum=min(poss,key=lambda z:(cost(t,z),z))
            changes=[z-b for z,b in zip(optimum,t)]
            assert sum(changes)==0
            assert sum(abs(x) for x in changes)==2*d
            stats['signed_delta_checks']+=1

def main():
    stats={k:0 for k in (
      'graphs_checked','balanced_tested','isolated_sender_infeasible',
      'deficit_equals_min_retarget','positive_deficit',
      'symmetric_retarget_checks','signed_delta_checks')}
    e22=list(product(range(2),repeat=2))
    for mask in range(1,1<<4):
        E={edge for k,edge in enumerate(e22) if mask & (1<<k)}
        check(E,2,2,3,stats);stats['graphs_checked']+=1
    samples=[
      {(0,0),(1,1),(2,2)},
      {(0,0),(0,1),(1,1),(1,2),(2,2)},
      {(0,0),(0,1),(1,0),(1,2),(2,1),(2,2)},
      {(0,0),(0,2),(1,1),(1,2),(2,0),(2,1)},
      set(product(range(3),repeat=2))]
    for E in samples:
        check(E,3,3,2,stats);stats['graphs_checked']+=1
    E={(i,j) for i in range(4) for j in range(4) if abs(i-j)==1}
    s=(1,0,0,0);t=(0,0,0,1)
    adj=neighbors(E,4,4)
    d,U=deficit(s,t,adj)
    zs=reachable_receivers(s,adj,4)
    assert (d,U,zs)==(1,(0,),{(0,1,0,0)})
    t2=(0,1,0,0)
    assert cost(t,t2)==1
    u0=tuple(t[i]-s[i] for i in range(4))
    u1=tuple(t2[i]-s[i] for i in range(4))
    assert u0==(-1,0,0,1) and u1==(-1,1,0,0)
    assert tuple(u1[i]-u0[i] for i in range(4))==(0,1,0,-1)
    print(json.dumps(dict(
      marker='R654_MINIMAL_TRANSFER_RETARGET_HALL_DEFICIT_EXACT_PASS',
      domain='All nonempty 2x2 licensed graphs s,t in 0..3; five 3x3 graphs s,t in 0..2',
      **stats,
      x6_path=dict(s=s,t=t,Hall_witness_U=U,deficit=d,
                  repaired_t=t2,retarget_moves=1,
                  signed_observer_delta=(0,1,0,-1))),indent=2))

if __name__=='__main__':
    main()
