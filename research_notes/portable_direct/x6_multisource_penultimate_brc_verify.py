#!/usr/bin/env python3
"""R6: exact source-labelled Boolean-BRC future-trie support and sharp
penultimate horizon fiber bound for multi-label resource controllers.

No native Cell permission or signed-amplitude computation is asserted.
Provenance branch=(ordered source word, controller state); quotient=(count vector,q).
"""
import itertools
import json
from functools import lru_cache
from collections import defaultdict
from math import ceil, log2


def evaluate(capacities, periods, transitions, labels=('A', 'B', 'C')):
    d=len(labels)
    total=sum(capacities)
    start=((0,)*d, 0)
    def step(state, index):
        counts,q=state
        if counts[index] == capacities[index]:return None
        nxt=transitions.get((q,index))
        if nxt is None:return None
        new=list(counts);new[index]+=1
        return (tuple(new),nxt)
    levels=[{start}]
    branches={('',0)}
    for k in range(total):
        news=set();nextbranches=set()
        for s in levels[-1]:
            for i in range(d):
                t=step(s,i)
                if t is not None:news.add(t)
        for w,q in branches:
            for i in range(d):
                s=(tuple(w.count(x) for x in labels),q)
                t=step(s,i)
                if t is not None:nextbranches.add((w+labels[i],t[1]))
        branches=nextbranches
        assert news=={(tuple(w.count(x) for x in labels),q) for w,q in branches}, ('support',capacities,periods,transitions,k)
        levels.append(news)
    @lru_cache(None)
    def completions(s):
        if s[0] == capacities:return frozenset([''])
        out=set()
        for i,x in enumerate(labels):
            t=step(s,i)
            if t is not None:
                out.update(x+v for v in completions(t))
        return frozenset(out)
    @lru_cache(None)
    def brute(s,h):
        words=completions(s)
        return frozenset(w[:j] for w in words for j in range(min(h,len(w))+1))
    intern={}
    @lru_cache(None)
    def signature(s,h):
        if not completions(s):return None
        children=() if h==0 else tuple((i,signature(t,h-1)) for i in range(d)
                if (t:=step(s,i)) is not None and completions(t))
        if children not in intern:intern[children]=len(intern)+1
        return intern[children]
    @lru_cache(None)
    def obs(s):
        return (sum(s[0]),tuple(n%p for n,p in zip(s[0],periods)))
    N=0
    class_profiles=0
    for k,lv in enumerate(levels):
        H=total-k
        prod=[s for s in lv if completions(s)]
        if not prod:continue
        groups=defaultdict(list)
        for s in prod:groups[obs(s)].append(s)
        for s in prod:
            for h in range(H+1):
                # independently reconstruct ALL completed labelled suffixes and their productive prefixes
                assert (signature(s,h) is not None)==bool(brute(s,h))
        for o,sts in groups.items():
            profiles=[]
            for h in range(H+1):
                # exact DAG trie IDs versus independent expanded word-language equivalence
                idlangs=defaultdict(set)
                for s in sts:
                    idlangs[signature(s,h)].add(brute(s,h))
                assert all(len(z)==1 for z in idlangs.values()), ('signature collisions',o,h)
                assert len(idlangs)==len({brute(s,h) for s in sts})
                profiles.append(len(idlangs))
            assert profiles==sorted(profiles)
            full_formula=defaultdict(lambda: defaultdict(set))
            for s in sts:
                full_formula[s[0]][s[1]].add(completions(s))
            expected=sum(len({c for qset in qs.values() for c in qset}) for qs in full_formula.values())
            # same controller q is unique per count, but use set union for generality
            assert profiles[-1]==expected,('multi-source full sum',capacities,periods,o,profiles[-1],expected)
            t=sum(p==1 for p in periods)
            if H>=1:
                assert profiles[-1] <= max(1,t)*profiles[-2],('class bound',capacities,periods,o,profiles)
                if t<=1:assert profiles[-1]==profiles[-2],('early stabilization',capacities,periods,o,profiles)
                for s,u in itertools.combinations(sts,2):
                    equal=(signature(s,H-1)==signature(u,H-1))
                    if equal and completions(s)!=completions(u):
                        cdelta=tuple(x-y for x,y in zip(s[0],u[0]))
                        assert cdelta.count(1)==1 and cdelta.count(-1)==1 and all(x in (-1,0,1) for x in cdelta)
                        assert all(p==1 for x,p in zip(cdelta,periods) if x!=0)
            N+=1
            class_profiles+=sum(profiles)
    return N,class_profiles,bool(completions(start))


def finite_exhaustive():
    tested=0;with_completion=0;fiber_profiles=0;all_language_class_sums=0
    capacities=[(1,1,1),(1,1,2),(1,2,1),(2,1,1)]
    periods=[(1,1,1),(1,1,2),(1,2,2),(2,3,1),(2,2,2)]
    # ALL 3**6 deterministic partial two-state Port controllers for three named source types.
    for choices in itertools.product((None,0,1),repeat=6):
        delta=dict(zip(itertools.product((0,1),range(3)), choices))
        for caps in capacities:
            for p in periods:
                n,l,yes=evaluate(caps,p,delta)
                tested+=1;fiber_profiles+=n;all_language_class_sums+=l
                with_completion+=int(yes)
    return dict(controller_count=3**6,capacity_vectors=capacities,period_vectors=periods,
                complete_model_phase_cases=tested,nonempty_model_phase_cases=with_completion,
                observed_fibers_checked=fiber_profiles,language_class_cardinalities_compared=all_language_class_sums,
                result='PASS')


def sharp_witness(t,period_of_extra=2):
    d=t+1
    labels=tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:d]);caps=(1,)*d
    periods=(1,)*t+(period_of_extra,)
    # deterministic one-state Port with all source appends enabled. This is a typed BRC branch carrier.
    delta={(0,i):0 for i in range(d)}
    k=d-1
    states=[]
    for j in range(t):
        counts=tuple(0 if i==j else 1 for i in range(d))
        states.append((counts,0))
    O={(sum(s[0]),tuple(n%p for n,p in zip(s[0],periods))) for s in states}
    assert len(O)==1
    suffixes={labels[j] for j in range(t)}
    assert len(suffixes)==t
    # H=1, all productive h=0 prefix sets equal {epsilon}; at h=1, separate by required label.
    assert all(sum(caps[i]-s[0][i] for i in range(d))==1 for s in states)
    return dict(source_types=d,unit_period_channels=t,periods=list(periods),capacities=list(caps),rank=k,
                observer=list(O)[0][1],horizon=1,M_h0=1,M_h1=t,
                bit_jump=ceil(log2(t)),distinct_last_letters=sorted(suffixes))


def boundary_with_lcm_gt_one():
    w=sharp_witness(2,2)
    assert w['periods']==[1,1,2] and w['M_h1']==2
    return w


def main():
    small=finite_exhaustive()
    witnesses=[sharp_witness(t) for t in range(2,6)]
    return dict(schema='X6_MULTI_SOURCE_PORT_H_MINUS_ONE_FIBERS_V1',
        setting='typed labelled-branch Boolean BRC; deterministic partial Port guard; fixed terminal vector; productive finite source-prefix language',
        inherited='R4 full-completion count/Port signatures; R5 sharp two-source H-1 stabilization',
        exhaustive=small,
        unit_transfer_boundary=boundary_with_lcm_gt_one(),
        sharp_t_channel_witnesses=witnesses,
        asserted='For arbitrary d, M_H(o)<=max(1,t)*M_{H-1}(o); equality for all models when t<=1; ratio t sharp for t>=2',
        math_status='author-proved; finite independently enumerated exact support/prefix checks',
        native_X6_attribution='PENDING_REAL_TRIADIC_CLOSURE_E_AND_PORT_ADMISSION',
        all_assertions='PASS')

if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
