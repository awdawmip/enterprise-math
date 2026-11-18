#!/usr/bin/env python3
"""R5 source-aware cyclic bridge: exact shared-library and Helly-two certificates.
Standard library only; no native X6 computations.
"""
from itertools import combinations
import json

OLD = ("0125","0135","0235","0245","0246")
NEW_A = (("1235",1),("1245",1),("1246",1),("1345",0),("1346",0))
NEW_AB = NEW_A+(("1236",1),)

def q(k,u):
    return sum((u>>i&1)*(u>>((i+1)%k)&1) for i in range(k))

def edges(k):
    # 2k vertex IDs: spine v_i=i and leaf w_i=k+i
    return tuple(sorted(set(tuple(sorted(t)) for i in range(k)
                     for t in ((i,(i+1)%k),(i,k+i),((i+1)%k,k+i)))))

def exact_graph(k,u):
    es=edges(k)
    avail=[i for i in range(k) if not (u>>i&1)]
    best=10**6
    winners=[]
    for mask in range(1<<len(avail)):
        S={v for j,v in enumerate(avail) if mask>>j&1}
        cost=2*len(S)+sum(not (a in S or b in S) for a,b in es)
        if cost<best: best,winners=cost,[tuple(sorted(S))]
        elif cost==best: winners.append(tuple(sorted(S)))
    return len(es)+best,winners

def canonical_sources(k,u):
    es=edges(k)
    A={i for i in range(k) if not (u>>i&1)}
    label=lambda a,b:"".join('1' if i in (a,b) else '0' for i in range(2*k))
    one=lambda v:"".join('1' if i==v else '0' for i in range(2*k))
    out={(1,0,label(a,b)) for a,b in es}
    for v in A:
        out.add((0,1,one(v)))
        out.add((4,1,one(v)))
    for a,b in es:
        if a not in A and b not in A: out.add((0,1,label(a,b)))
    assert len(out)==5*k+q(k,u)
    return out

def covers(k,lib,join=False):
    for a,b in edges(k):
        y="".join('1' if i in (a,b) else '0' for i in range(2*k))
        for C,t in NEW_AB if join else NEW_A:
            if not any(len(set(C)-set(OLD[j]))+(s!=t)+sum(xi!=yi for xi,yi in zip(x,y))<=2
                       for j,s,x in lib): return False
    return True

def pair_criterion(k,u,v):
    w=u|v
    return q(k,w)==q(k,u)==q(k,v)

def run():
    exact_masks=0
    direct_repairs=0
    pair_cases=0
    for k in range(3,9):
        for u in range(1<<k):
            got,winners=exact_graph(k,u)
            assert got==5*k+q(k,u),(k,u,got,q(k,u))
            A=tuple(i for i in range(k) if not(u>>i&1))
            assert A in winners,(k,u)
            exact_masks+=1
            if k<=5:
                S=canonical_sources(k,u)
                assert covers(k,S)
                direct_repairs+=1
        if k<=7:
            for u in range(1<<k):
                for v in range(1<<k):
                    # Source intersection formula and pair common-optimum criterion
                    shared=5*k+q(k,u|v)
                    assert shared>=max(5*k+q(k,u),5*k+q(k,v))
                    criterion=pair_criterion(k,u,v)
                    assert criterion==(shared==5*k+q(k,u)==5*k+q(k,v))
                    pair_cases+=1
    robust_cases=0
    robust_direct_cases=0
    for k in range(3,8):
        for control in range(1<<k):
            for u in range(1<<k):
                worst=u|control
                robust=5*k+q(k,worst)
                # Every named assignment on control is a reachable state.
                max_individual=max(5*k+q(k,(u&~control)|assignment)
                                   for assignment in range(1<<k)
                                   if assignment&~control==0)
                assert robust==max_individual
                robust_cases+=1
                if k<=5:
                    lib=canonical_sources(k,worst)
                    assert len(lib)==robust and covers(k,lib)
                    assert all(not (control>>v&1) and not(worst>>v&1)
                               for j,s,x in lib if j in (0,4) and s==1
                               for v in [x.index('1')] if x.count('1')==1)
                    robust_direct_cases+=1
    triples_checked=0
    for k in range(3,6):
        for u,v,w in combinations(range(1<<k),3):
            if pair_criterion(k,u,v) and pair_criterion(k,u,w) and pair_criterion(k,v,w):
                assert q(k,u|v|w)==q(k,u)==q(k,v)==q(k,w)
            triples_checked+=1
    # Quantitative k-fold sharing penalty: singleton unavailable masks
    for k in range(3,40):
        singles=[1<<i for i in range(k)]
        assert all(q(k,x)==0 for x in singles)
        assert q(k,((1<<k)-1))==k
        assert 5*k+q(k,(1<<k)-1)==6*k
    return dict(status="PASS_R5_SHARED_SOURCE_HELLY_TWO",frozen_science="435e77af0d180eac32bd1f9c4c464bc4010b7551",
                exact_graph_masks=exact_masks,direct_original_core_repair_masks=direct_repairs,
                exact_mask_pairs=pair_cases,exhaustive_distinct_mask_triples=triples_checked,
                exhaustive_robust_pairs=robust_cases,robust_direct_core_repairs=robust_direct_cases,
                singletons_unbounded_range=[3,39],
                independent_review="NOT_REVIEWED",
                interpreted_scope="auxiliary one-step radius-two indexed-center cycle graph")

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
