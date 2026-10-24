#!/usr/bin/env python3
"""R257 author-side exact positive BRC edge-label lift test.
This is an independent finite interpreter, NOT an import of the native enterprise_math package.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import product
from random import Random
from math import comb
import json
from pathlib import Path

DFA=((1,0),(2,0),(2,2))  # 'contains 00'; 2 is accepting
# Edge: (source,target,selector,weight,linear_sign,first_axis_offset,multiplicity)
GRAPH_R256=tuple((q, dst, a, Fraction(1), eps, offset, 1)
  for q,row in enumerate((
    ((2,-1,-1),(2,1,-1)),
    ((0,-1,-1),(0,1,-1)),
    ((1,1,1),(2,1,-1))))
  for a,(dst,eps,offset) in enumerate(row))


def advance(effect,edge):
    # Source Affine.then: later o earlier, (eta*eps, eta*k+b).
    q,r,w,eps,k=effect
    src,tgt,a,v,eta,b,c=edge
    assert src==q and v>0 and c>0
    return (tgt,DFA[r][a],w*v,eta*eps,eta*k+b)


def step(states,edges,include_query=True):
    edges_by_q={}
    for e in edges:edges_by_q.setdefault(e[0],[]).append(e)
    new=defaultdict(int)
    for (q,r,w,eps,k),mult in states.items():
        for e in edges_by_q.get(q,()):
            dst,dr,v,eta,b=advance((q,r,w,eps,k),e)
            key=(dst,dr if include_query else 0,v,eta,b)
            new[key]+=mult*e[6]
    return dict(new)


def projected(states):
    out=defaultdict(int)
    for (q,r,w,eps,k),c in states.items():
        out[(q,w,eps,k)]+=c
    return dict(out)


def brute(word,edges):
    # Deterministic selector graph used only for R256; each source has one edge per selector.
    by={(e[0],e[2]):e for e in edges}
    st=(0,0,Fraction(1),1,0)
    for a in word:
        st=advance(st,by[(st[0],a)])
    return st


def get_query_mass(states):
    return sum(c for (q,r,w,eps,k),c in states.items() if r==2)


def no_go():
    I=(0,0,0,Fraction(1),1,0,1)
    J=(0,0,1,Fraction(1),1,0,1)
    A=(I,J)
    B=(I,I)  # two distinct source edges both labelled 0
    def forget(one):
        result=defaultdict(int)
        for s,t,a,w,e,k,c in one:result[(s,t,w,e,k)]+=c
        return dict(result)
    assert forget(A)==forget(B)=={(0,0,Fraction(1),1,0):2}
    result={}
    for name,edges in [('different_labels',A),('both_zero',B)]:
        states={(0,0,Fraction(1),1,0):1}
        seq=[]
        for m in range(7):
            seq.append({'m':m,'paths':sum(states.values()),'contains_00':get_query_mass(states)})
            if m<6:states=step(states,edges)
        result[name]=seq
    assert result['different_labels'][2]['contains_00']==1
    assert result['both_zero'][2]['contains_00']==4
    assert all(result['different_labels'][m]['paths']==result['both_zero'][m]['paths']==2**m for m in range(7))
    # A: 00 avoidance Fibonacci. B: every nonempty selector is '0', every length >=2 accepts.
    return result


def test_r256():
    states={(0,0,Fraction(1),1,0):1}; aggregate=[]; brute_paths=0
    for m in range(25):
        unlabeled={(q,0,w,e,k):c for (q,w,e,k),c in projected(states).items()}
        # Forgotten-label source with same 6-axis affine transitions and exact positive weights.
        alt={(0,0,Fraction(1),1,0):1}
        for _ in range(m):alt=step(alt,GRAPH_R256,include_query=False)
        assert states and projected(states)==projected(alt)
        assert sum(states.values())==2**m
        if m<=10:
            direct=defaultdict(int)
            for word in product((0,1),repeat=m):
                direct[brute(word,GRAPH_R256)]+=1
                brute_paths+=1
            assert dict(direct)==states
        if m in (0,2,3,7,12,24):aggregate.append((m,len(states),len(projected(states)),get_query_mass(states)))
        if m<24:states=step(states,GRAPH_R256)
    assert brute((0,0,0),GRAPH_R256)[:1]+brute((0,0,0),GRAPH_R256)[3:]==(0,1,-1)
    assert brute((1,0,1),GRAPH_R256)[:1]+brute((1,0,1),GRAPH_R256)[3:]==(0,1,-1)
    return {'all_words_checked_through_depth':10,'word_cases_checked':brute_paths,'selected':aggregate}


def random_cases(n=24,depth=10):
    rng=Random(2572401)
    checked=0
    for i in range(n):
        edges=[]
        for q in range(2):
            for a in (0,1):
                edges.append((q,rng.randrange(2),a,rng.choice([Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2)]),rng.choice([-1,1]),rng.choice([-1,0,1]),rng.choice([1,2])))
        marked={(0,0,Fraction(1),1,0):1}
        unmarked={(0,0,Fraction(1),1,0):1}
        for m in range(depth+1):
            assert projected(marked)==projected(unmarked),(i,m)
            checked+=1
            if m<depth:
                marked=step(marked,edges,True)
                unmarked=step(unmarked,edges,False)
    return checked


def main():
    no_go_result=no_go()
    r256=test_r256()
    random_count=random_cases()
    report={
      'schema':'EM_R257_AUTHOR_AUXILIARY_EXACT_V1',
      'result':'PASS',
      'claim_scope':'formal positive rational labelled-edge BRC with finite DFA state; no native module executed',
      'source_pin':'awdawmip/enterprise-math@9a1659352c5c5959e82c87924c4c2939c77c0b1b',
      'native_interface_readback_blobs':{'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1','brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8'},
      'native_implemented_package_executed':False,
      'actual_R193_token_grammar_verified':False,
      'nonfactorization_witness_depth2':{'A_query_yes':no_go_result['different_labels'][2]['contains_00'],'B_query_yes':no_go_result['both_zero'][2]['contains_00'],'both_unlabelled_path_count':4},
      'finite_cross_check_r256':r256,
      'random_seed':2572401,'random_weighted_branch_models':24,'random_depth':10,'random_model_depth_observations':random_count,
      'scope_of_infinite_claim':'inductive proof in accompanying note, NOT extrapolation of tests'
    }
    with Path(__file__).with_name('R257_AUXILIARY_REPORT.json').open('w',encoding='utf8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
