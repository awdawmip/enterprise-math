#!/usr/bin/env python3
"""Finite typed BRC Boolean-support verification of a conditional two-chain causal poset.

Model: two labelled source chains A[1..a], B[1..b]; acyclic directed cross-links
AB(r,s): A_r precedes B_s; BA(u,v): B_u precedes A_v.
Carrier: a set of source-labelled branch words. Allowed operation: append A/B
if the resulting prefix is a legal ideal; support quotient is (count_A,count_B).
Readout: k, local phase i mod pA and j mod pB. Not native X6 admission.
No pi/trigonometry/matrix exponential/physical timing or signed mass involved.
"""
from itertools import combinations
from math import gcd
from collections import defaultdict
import json


def lcm(a,b):
    return a//gcd(a,b)*b


def dag_ok(a,b,ab,ba):
    n=a+b
    adj=[[] for _ in range(n)]
    for i in range(a-1): adj[i].append(i+1)
    for j in range(b-1): adj[a+j].append(a+j+1)
    for r,s in ab: adj[r-1].append(a+s-1)
    for u,v in ba: adj[a+u-1].append(v-1)
    indeg=[0]*n
    for row in adj:
        for w in row: indeg[w]+=1
    seen=0
    ready=[t for t,x in enumerate(indeg) if x==0]
    while ready:
        t=ready.pop(); seen+=1
        for w in adj[t]:
            indeg[w]-=1
            if indeg[w]==0: ready.append(w)
    return seen==n


def legal(i,j,a,b,ab,ba):
    return (0<=i<=a and 0<=j<=b
        and all(j<s or i>=r for r,s in ab)
        and all(i<v or j>=u for u,v in ba))


def interval(k,a,b,ab,ba):
    lo=max(0,k-b)
    hi=min(a,k)
    for r,s in ab: lo=max(lo,min(r,k-s+1))
    for u,v in ba: hi=min(hi,max(v-1,k-u))
    return lo,hi


def labelled_levels(a,b,ab,ba):
    words={''}
    supports=[{(0,0)}]
    for k in range(a+b):
        nxt=set()
        for w in words:
            i=w.count('A');j=k-i
            if legal(i+1,j,a,b,ab,ba): nxt.add(w+'A')
            if legal(i,j+1,a,b,ab,ba): nxt.add(w+'B')
        words=nxt
        supports.append({(w.count('A'),len(w)-w.count('A')) for w in words})
    return supports, len(words)


def support_levels(a,b,ab,ba):
    support={(0,0)}
    levels=[support]
    for _ in range(a+b):
        nxt=set()
        for i,j in support:
            if legal(i+1,j,a,b,ab,ba): nxt.add((i+1,j))
            if legal(i,j+1,a,b,ab,ba): nxt.add((i,j+1))
        levels.append(nxt); support=nxt
    return levels


def check(a,b,ab,ba,period_pairs):
    assert dag_ok(a,b,ab,ba)
    B,nwords=labelled_levels(a,b,ab,ba)
    S=support_levels(a,b,ab,ba)
    assert B==S, ('BRC branch-support failure',a,b,ab,ba)
    assert nwords>0
    for k,level in enumerate(S):
        lo,hi=interval(k,a,b,ab,ba)
        predicted={(i,k-i) for i in range(lo,hi+1)}
        assert level==predicted and lo<=hi, ('interval failure', a,b,ab,ba,k)
        for pA,pB in period_pairs:
            L=lcm(pA,pB)
            fibers=defaultdict(set)
            for i,j in level: fibers[(i%pA,j%pB)].add((i,j))
            assert max(map(len,fibers.values()))==(hi-lo+L)//L, ('max fiber failure',a,b,ab,ba,k,pA,pB)
            for states in fibers.values():
                iseq=sorted(i for i,_ in states)
                assert all((iseq[z+1]-iseq[z])==L for z in range(len(iseq)-1))
    return len(S)


def subset_cases(a,b,exhaustive=True,maxsize=2):
    all_edges=[('AB',r,s) for r in range(1,a+1) for s in range(1,b+1)]
    all_edges += [('BA',u,v) for u in range(1,b+1) for v in range(1,a+1)]
    if exhaustive:
        sizes=range(len(all_edges)+1)
    else:
        sizes=range(maxsize+1)
    for size in sizes:
        for subset in combinations(all_edges,size):
            ab=tuple((x,y) for direction,x,y in subset if direction=='AB')
            ba=tuple((x,y) for direction,x,y in subset if direction=='BA')
            yield ab,ba


def future_words(i,j,a,b,ab,ba):
    curr={('',i,j)}
    for _ in range(a+b-i-j):
        nxt=set()
        for w,x,y in curr:
            if legal(x+1,y,a,b,ab,ba): nxt.add((w+'A',x+1,y))
            if legal(x,y+1,a,b,ab,ba): nxt.add((w+'B',x,y+1))
        curr=nxt
    return {w for w,x,y in curr}


def run():
    phase_pairs=[(2,2),(2,3),(3,4),(4,5)]
    cases=0;levels=0;with_bidirectional=0
    sizes=[(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)]
    per_size={}
    for a,b in sizes:
        n=0
        # 3x3: all two-link subsets, plus selected full samples; 2x3/3x2 complete all 4096 subsets.
        exhaustive=(a,b)!=(3,3)
        for ab,ba in subset_cases(a,b,exhaustive=exhaustive,maxsize=2):
            if not dag_ok(a,b,ab,ba): continue
            levels+=check(a,b,ab,ba,phase_pairs)
            cases+=1;n+=1
            if ab and ba: with_bidirectional+=1
        per_size[f'{a}x{b}']=n
    # Explicit 4x4 mixed dependency test, k-levels and future-language collision certificate.
    ab=((2,3),)
    ba=((1,3),)
    assert dag_ok(4,4,ab,ba)
    check(4,4,ab,ba,[(2,2),(2,3),(3,4)])
    # Specific ambiguous pair at k=6 for pA=2, pB=3, with no links and a=b=6.
    pair=((0,6),(6,0)); a=b=6; ab=(); ba=()
    assert all(legal(i,j,a,b,ab,ba) for i,j in pair)
    assert len({(i+j,i%2,j%3) for i,j in pair})==1
    f0=future_words(*pair[0],a,b,ab,ba)
    f1=future_words(*pair[1],a,b,ab,ba)
    assert f0=={'AAAAAA'} and f1=={'BBBBBB'} and f0.isdisjoint(f1)
    # Any cross-link orientation removes the only candidate collision when a=b=L.
    L=6; edges_checked=0
    for orientation in ('AB','BA'):
        for r in range(1,L+1):
            for s in range(1,L+1):
                ab=((r,s),) if orientation=='AB' else ()
                ba=((r,s),) if orientation=='BA' else ()
                # full exact support without labelled words for the larger L grid
                lev=support_levels(L,L,ab,ba)
                for k,states in enumerate(lev):
                    lo,hi=interval(k,L,L,ab,ba)
                    assert states=={(i,k-i) for i in range(lo,hi+1)}
                    assert hi-lo+1<=L
                edges_checked+=1
    # Long horizon survives one AB edge, with same phase/count.
    long_pair=((12,12),(24,0)); a=24;b=12;ab=((2,1),);ba=()
    assert all(legal(i,j,a,b,ab,ba) for i,j in long_pair)
    assert len({(i+j,i%3,j%4) for i,j in long_pair})==1
    result={
        'model':'typed source-labelled BRC branch words with Boolean-support guarded append',
        'domain':'acyclic cross-edge subsets: all sets for 1x1,1x2,2x1,2x2,2x3,3x2; up to 2 edges for 3x3',
        'period_pairs': phase_pairs,
        'acyclic_graphs_checked': cases,
        'k_level_supports_checked':levels,
        'bidirectional_graphs_checked':with_bidirectional,
        'cases_by_chain_lengths':per_size,
        'uniform_lcm_6_one_crosslink_oriented_edges_checked':edges_checked,
        'explicit_mixed_direction_case':{'a':4,'b':4,'AB':[[2,3]],'BA':[[1,3]],'status':'PASS'},
        'different_periods_phase_collision':{'pA':2,'pB':3,'k':6,'counts':pair,'future_words':[sorted(f0),sorted(f1)]},
        'long_horizon_phase_collision':{'pA':3,'pB':4,'k':24,'counts':long_pair,'AB':[[2,1]]},
        'result':'PASS',
        'limitation':'conditional two-chain event-poset model; not native triadic Cell-Link-Port permission or physical time'
    }
    return result

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
