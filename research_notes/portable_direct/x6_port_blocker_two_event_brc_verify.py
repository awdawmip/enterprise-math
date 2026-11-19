#!/usr/bin/env python3
"""Exact finite labelled Boolean-BRC verification for X6 two-event blocker tomography.

All positions are 6-tuples of signed native-axis relative integers. 12 primitive
moves (six axes, both signs); only vacancy guards. No amplitude or physical-force
calculation is asserted. Tests are independent finite checks of the paper's proof.
"""
from itertools import permutations
from collections import defaultdict
import json

D = tuple(tuple(sign if i==j else 0 for i in range(6))
          for j in range(6) for sign in (-1,1))
N = (0,)*6

def plus(p,v): return tuple(x+y for x,y in zip(p,v))

def next_state(P,s,v):
    q=plus(P[s],v)
    if q in P: return None
    out=list(P);out[s]=q
    return tuple(out)

def languages(P):
    L1=set();L2=set()
    for s in range(len(P)):
        for idx,v in enumerate(D):
            S=next_state(P,s,v)
            if S is None: continue
            L1.add((s,idx))
            for t in range(len(P)):
                for j,w in enumerate(D):
                    if next_state(S,t,w) is not None:
                        L2.add(((s,idx),(t,j)))
    return L1,L2

def true_blockers(P):
    lookup={pos:s for s,pos in enumerate(P)}
    return {(s,j):lookup[plus(P[s],v)]
            for s in range(len(P)) for j,v in enumerate(D)
            if plus(P[s],v) in lookup}

def reconstruct_blockers(P,L1,L2):
    out={}
    for s in range(len(P)):
        for j in range(len(D)):
            if (s,j) in L1:continue
            candidates=[]
            for t in range(len(P)):
                if t==s: continue
                if any((t,i) in L1 and ((t,i),(s,j)) in L2 for i in range(len(D))):
                    candidates.append(t)
            out[s,j]=candidates
    return out

def is_connected(P, blocker):
    g={i:set() for i in range(len(P))}
    for (s,_),t in blocker.items():g[s].add(t);g[t].add(s)
    seen={0};todo=[0]
    while todo:
        for x in g[todo.pop()]:
            if x not in seen:seen.add(x);todo.append(x)
    return len(seen)==len(P)

def invariant(P):
    b=true_blockers(P)
    # A complete signed-axis labelled directed adjacency graph is translation invariant.
    return tuple(sorted((s,j,t) for (s,j),t in b.items()))

def check(P, counters):
    assert len(set(P))==len(P)
    L1,L2=languages(P)
    b=true_blockers(P)
    calc=reconstruct_blockers(P,L1,L2)
    assert all((s,j) in calc for (s,j) in b)
    can_move=all(any(src==s for src,_ in L1) for s in range(len(P)))
    if can_move:
        assert all(v==[b[k]] for k,v in calc.items()), (P,b,calc)
        counters['fully_mobile_cases']+=1
        if is_connected(P,b):
            counters['connected_mobile_cases']+=1
            key=(len(P),frozenset(L1),frozenset(L2))
            old=language_class.get(key)
            if old is not None:
                assert old==invariant(P),('bad L2 reconstruction',P)
            else: language_class[key]=invariant(P)
    else:
        assert all(not v or v==[b[k]] for k,v in calc.items())
        counters['nonmobile_cases']+=1
    counters['configs']+=1
    counters['legal_first_words']+=len(L1)
    counters['legal_second_words']+=len(L2)
    counters['blocked_directed_edges']+=len(b)
    counters['decoded_edges']+=sum(len(v)==1 for v in calc.values())

language_class={}

def run():
    from math import factorial
    count=defaultdict(int)
    base=[]
    # Exact enumeration on an embedded 3x3 patch. All 6 signed axes are offered.
    patch=[(x,y,0,0,0,0) for x in range(3) for y in range(3)]
    for n in (2,3):
        for P in permutations(patch,n):
            check(P,count)
    # Exhaustive permutations of labelled connected 4-particle line and square.
    line=tuple((x,0,0,0,0,0) for x in range(4))
    square=tuple((x,y,0,0,0,0) for x in range(2) for y in range(2))
    for cells in (line,square):
        for P in permutations(cells):check(P,count)
    # Entire 5-source factorial family -- 5! different labelled configurations.
    line5=tuple((x,0,0,0,0,0) for x in range(5))
    signatures1=set(); signatures2=set()
    for inside in permutations((1,2,3)):
        P=(line5[0],)+(tuple(line5[i] for i in inside))+(line5[-1],)
        check(P,count)
        l1,l2=languages(P)
        signatures1.add(frozenset(l1));signatures2.add(frozenset(l2))
    assert len(signatures1)==1 and len(signatures2)==6
    count['five_source_perm_L1_classes']=len(signatures1)
    count['five_source_perm_L2_classes']=len(signatures2)
    # Sharp 4-source instance: two interior labels swapped.
    P=(line[0],line[1],line[2],line[3]); Q=(line[0],line[2],line[1],line[3])
    assert languages(P)[0]==languages(Q)[0]
    assert languages(P)[1]!=languages(Q)[1]
    count['four_source_L1_equal_L2_different']=True
    # Immobile shell center: all signed unit neighbors occupied. Guard cannot decode center.
    shell=(N,)+D
    l1,l2=languages(shell)
    b=true_blockers(shell);c=reconstruct_blockers(shell,l1,l2)
    assert all(s!=0 for s,_ in l1)
    assert c[(1,next(i for i,d in enumerate(D) if plus(D[0],d)==N))]==[]
    count['enclosed_center_immobile']=True
    count['source_model']='Vacancy-only full signed six-axis, ordered labelled Boolean-BRC language up to 2 moves'
    count['result']='PASS'
    return dict(count)

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2,sort_keys=True))
