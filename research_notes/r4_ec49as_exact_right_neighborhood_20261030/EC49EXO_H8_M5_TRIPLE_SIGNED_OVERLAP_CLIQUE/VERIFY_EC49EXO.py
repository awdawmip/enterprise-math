#!/usr/bin/env python3
"""EC49EXO: rigorously safe, all-123147 schedule native-X6 trie edge lower bound.
Pure integer arithmetic, standard-library only. Scientific pins preserved from EC49EXM.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
import json
import time

HS=tuple(range(2,9))
FROZEN={'global':'773d538180bfb49e24cffeb35c3ee75eb0628e2e',
        'enterprise_math':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'}


def eligible(h):
    output={}
    for w in range(1,(h+1)//2+1):
        for u in range(2*h+3):
            for v in range(h+2):
                r=u+v-h-1
                f=h+1-v-2*w
                g=h+1-u
                if min(r,f,g)>=0 and (r>=1 or (r==0 and f>=1 and g>=1)):
                    output[(u,v,w)]=4 if r>=1 else 2
    return output

S={h:eligible(h) for h in HS}
assert [len(S[h]) for h in HS]==[1,4,9,17,28,43,62]


def signed_overlap(a,b):
    """Maximum common signed-symbol count of *any* two permutations of the two histograms."""
    return 2*sum(min(a[i],b[i]) for i in range(3))-2


def clique_bound_for_schedule(assign):
    """Construct five key groups, one for a triple and four for singletons.

    At primitive depth d each key K requires at least q_K(d) distinct trie nodes.
    A collection of keys pairwise satisfying signed_overlap(K,K')<d
    needs the sum of their q_K(d) nodes. We take the maximum clique weight.
    """
    groups={}
    for h,K in assign.items():
        if K not in groups:groups[K]=[0,0,2*(sum(K)-1)]
        groups[K][0]+=1 # horizon count for shared key
        groups[K][1]+=S[h][K] # mandatory distinct rank-observation signatures
    assert len(groups)==5
    ks=list(groups)
    L=[groups[k][2] for k in ks]
    n=[groups[k][0] for k in ks]
    m=[groups[k][1] for k in ks]
    cap={(i,j):signed_overlap(ks[i],ks[j]) for i in range(5) for j in range(i+1,5)}
    total=0
    for d in range(1,max(L)+1):
        q=[0 if d>li else mi if d>=li-1 else ni if d==li-2 else 1
           for li,ni,mi in zip(L,n,m)]
        best=max(q)
        # Small-graph direct clique enumeration, early pruning.
        for i in range(5):
            if not q[i]: continue
            for j in range(i+1,5):
                if not q[j] or cap[i,j]>=d:continue
                best=max(best,q[i]+q[j])
                for k in range(j+1,5):
                    if not q[k] or cap[i,k]>=d or cap[j,k]>=d:continue
                    best=max(best,q[i]+q[j]+q[k])
                    for m_ in range(k+1,5):
                        if not q[m_] or any(cap[t,m_]>=d for t in (i,j,k)):continue
                        best=max(best,q[i]+q[j]+q[k]+q[m_])
                        for z in range(m_+1,5):
                            if q[z] and all(cap[t,z]<d for t in (i,j,k,m_)):
                                best=max(best,q[i]+q[j]+q[k]+q[m_]+q[z])
        total+=best
    return total


def compute():
    tic=time.monotonic()
    overall=Counter();per_triple=[]
    sample={}
    for triple in combinations(HS,3):
        singles=tuple(h for h in HS if h not in triple)
        common=set.intersection(*(set(S[h]) for h in triple))
        if not common:continue
        c=Counter()
        for k3 in sorted(common):
            assign={h:k3 for h in triple}
            def rec(i,used):
                if i==len(singles):
                    b=clique_bound_for_schedule(assign)
                    c[b]+=1
                    if b not in sample:
                        sample[b]={'triple_windows':list(triple),'key_by_h':
                                    {str(h):list(assign[h]) for h in HS}}
                    return
                h=singles[i]
                for k in S[h]:
                    if k not in used:
                        assign[h]=k
                        rec(i+1,used|{k})
                assign.pop(h,None)
            rec(0,{k3})
        if c:
            overall.update(c)
            per_triple.append({'windows':list(triple),'schedules':sum(c.values()),
                               'lower_bound_min':min(c),'lower_bound_max':max(c),
                               'E_lt_80_excluded':sum(cnt for b,cnt in c.items() if b>=80),
                               'E_le_80_excluded':sum(cnt for b,cnt in c.items() if b>80)})
    assert sum(overall.values())==123147
    assert [x['schedules'] for x in per_triple]==[71799,23502,4983,2905,10158,3015,1917,4868]
    return {'status':'PASS', 'scope':'native signed-X6, H=2..8, exact M=5, S<=6, triple-key-collision skeletons',
            'frozen_scientific_pins':FROZEN,
            'lower_bound_method':'depthwise maximum-weight incompatibility clique; native signed histogram overlap + same-key divergent-window and signature suffix bounds',
            'eligible_key_counts':{str(h):len(S[h]) for h in HS},
            'schedules':sum(overall.values()),
            'lb_histogram':dict(sorted(overall.items())),
            'min_lb':min(overall),'max_lb':max(overall),
            'E_lt_80_excluded':sum(cnt for b,cnt in overall.items() if b>=80),
            'E_lt_80_survivors':sum(cnt for b,cnt in overall.items() if b<80),
            'E_le_80_excluded':sum(cnt for b,cnt in overall.items() if b>80),
            'per_triple':per_triple,
            'example_lb90':sample.get(90),
            'elapsed_seconds':round(time.monotonic()-tic,3)}

if __name__=='__main__':
    print(json.dumps(compute(),indent=2,ensure_ascii=False))