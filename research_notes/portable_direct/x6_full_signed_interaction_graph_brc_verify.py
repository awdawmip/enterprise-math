#!/usr/bin/env python3
"""Exact typed Boolean-BRC labelled-future checks; conditional X6 vacancy-only model."""
import json
from itertools import permutations, product
from math import comb
from collections import defaultdict
D=6
ZERO=(0,)*D
DIRS=tuple((i,s) for i in range(D) for s in (-1,1))
ACTIONS=tuple((a,i,s) for a in range(3) for i,s in DIRS)
def point(x,y=0): return (x,y,0,0,0,0)
def move(p,i,s):
    a=list(p);a[i]+=s;return tuple(a)
def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
def step(ps,event):
    a,i,s=event
    target=move(ps[a],i,s)
    if target in ps:return None
    out=list(ps);out[a]=target;return tuple(out)
def language(ps,h):
    words={()};front=[(ps,())]
    for _ in range(h):
        nex=[]
        for state,w in front:
            for event in ACTIONS[:12*len(ps)]:
                nxt=step(state,event)
                if nxt is not None:
                    u=w+(event,);words.add(u);nex.append((nxt,u))
        front=nex
    return frozenset(words)
def signature(ps,h):
    n=len(ps);adj={i:set() for i in range(n)}
    for i in range(n):
        for j in range(i+1,n):
            if dist(ps[i],ps[j])<=h:
                adj[i].add(j);adj[j].add(i)
    unseen=set(range(n));comps=[]
    while unseen:
        root=min(unseen);todo=[root];unseen.remove(root);ids=set()
        while todo:
            i=todo.pop();ids.add(i)
            for j in adj[i]&unseen:
                unseen.remove(j);todo.append(j)
        ids=tuple(sorted(ids));anchor=ps[ids[0]]
        diffs=tuple(tuple(ps[i][k]-anchor[k] for k in range(6)) for i in ids)
        comps.append((ids,diffs))
    return tuple(sorted(comps))
def ball(h):
    return sum(2**j*comb(6,j)*comb(h,j) for j in range(min(6,h)+1))
def run():
    positions=[point(x,y) for x,y in product(range(-2,3),repeat=2) if (x,y)!=(0,0)]+[point(9,9)]
    pair_results=[];pair_words=0
    for h in range(4):
        by=defaultdict(list)
        for b in positions:
            L=language((ZERO,b),h);pair_words+=len(L)
            key=b if dist(ZERO,b)<=h else "FAR"
            by[key].append(L)
        assert all(len(set(a))==1 for a in by.values())
        assert len({a[0] for a in by.values()})==len(by)
        pair_results.append(dict(h=h,sample_states=len(positions),sample_equivalence_classes=len(by),
                                 theoretical_all_X6_classes=ball(h),theoretical_min_bits=(ball(h)-1).bit_length()))
    points=[point(*v) for v in ((-1,0),(0,0),(1,0),(0,1),(1,1),(-1,1))]
    states=list(permutations(points,3));three=[];three_words=0;three_moves=0
    for h in range(3):
        by=defaultdict(list)
        for ps in states:
            L=language(ps,h);three_words+=len(L);by[signature(ps,h)].append((ps,L))
        assert all(len({L for _,L in a})==1 for a in by.values())
        if h:
            for a in by.values():
                ref=a[0][0]
                for ps,_ in a:
                    for event in ACTIONS:
                        x=step(ps,event);y=step(ref,event)
                        assert (x is None)==(y is None)
                        if x is not None:
                            assert signature(x,h-1)==signature(y,h-1);three_moves+=1
        three.append(dict(h=h,configurations=len(states),signature_classes=len(by),
                          observed_language_classes=len({L for a in by.values() for _,L in a})))
    two_moves=0
    for h in range(1,4):
        by=defaultdict(list)
        for b in positions:
            ps=(ZERO,b);by[signature(ps,h)].append(ps)
        for states in by.values():
            rep=states[0]
            for ps in states:
                for event in ACTIONS[:24]:
                    x=step(ps,event);y=step(rep,event)
                    assert (x is None)==(y is None)
                    if x is not None:
                        assert signature(x,h-1)==signature(y,h-1);two_moves+=1
    result={
        "result":"PASS",
        "scope":"conditional occupancy-only six signed native-coordinate unit-step event system; complete source/axis/direction labelled Boolean future-word support; not TRIADIC_CLOSURE_E native admission",
        "pair_tests":pair_results,"pair_sample_total_word_observations":pair_words,
        "three_source_tests":three,"three_source_total_word_observations":three_words,
        "three_source_graded_transitions":three_moves,"two_source_graded_transitions":two_moves,
        "pair_global_class_formula":"sum_{j=0}^min(6,h) 2^j * C(6,j) * C(h,j) = |{z in Z^6: ||z||_1 <= h}|",
        "algorithm":"enumerate all source-labelled legal event words, test equality of Boolean supports for same signature; independently check horizon-graded signature update on all legal typed moves in sampled configurations",
        "validation_limit":"full pair sample: b=(x,y,0,0,0,0), x,y=-2..2 excluding origin plus b=(9,9,0,0,0,0), horizon 0..3; all 120 ordered distinct 3-source configurations from 6 fixed points, horizon 0..2; symbolic proof handles arbitrary n and unbounded X6 displacements"}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=="__main__":run()
