#!/usr/bin/env python3
"""R722 exact integer verifier; observation changes, not force closure."""
import itertools, json
from collections import Counter
N=6
T=tuple(itertools.combinations(range(N),3))
P=tuple(itertools.combinations(range(N),2))
PID={p:i for i,p in enumerate(P)}
TP=tuple(tuple(PID[p] for p in itertools.combinations(t,2)) for t in T)
def can(x):
    m=min(x); return tuple(y-m for y in x)
def sup(v):
    return tuple(int(len({v[i] for i in t})>1) for t in T)
def exact(z,v):
    return tuple(int(can([z[i] for i in t])!=can([z[i]+v[i] for i in t])) for t in T)
def degree(h):
    d=[0]*len(P)
    for flag,es in zip(h,TP):
        if flag:
            for i in es:d[i]+=1
    return tuple(d)
def expected(v):
    ct=Counter(v)
    return tuple(N-2 if v[i]!=v[j] else N-ct[v[i]] for i,j in P)
def restore(d):
    return tuple(int(any(d[e]==N-2 for e in es)) for es in TP)
def main():
    anchors=((0,)*6,(7,-5,0,11,-10,2),(-2,-2,3,3,5,0))
    imgs={}
    for v in itertools.product((-1,0,1,2),repeat=N):
        h=sup(v); d=degree(h)
        assert d==expected(v) and h==restore(d)
        assert sum(h)==20-sum(m*(m-1)*(m-2)//6 for m in Counter(v).values())
        for z in anchors:assert exact(z,v)==h
        imgs.setdefault(h,v)
    hist=dict(sorted(Counter(sum(h) for h in imgs).items()))
    assert hist=={0:1,10:6,16:15,18:10,19:20,20:1}
    assert len(imgs)==53
    assert len({sup(v) for v in itertools.product(range(3),repeat=N)})==53
    tid={t:i for i,t in enumerate(T)}
    for perm in itertools.permutations(range(N)):
        for h,v in imgs.items():
            pv=[0]*N
            for i,p in enumerate(perm):pv[p]=v[i]
            ph=sup(pv)
            for t,flag in zip(T,h):
                assert ph[tid[tuple(sorted(perm[i] for i in t))]]==flag
    targets={degree(h):0 for h in imgs}; d=[0]*len(P); prev=0
    for k in range(1<<20):
        g=k^(k>>1)
        if k:
            bit=(prev^g).bit_length()-1
            for e in TP[bit]:d[e]+=1 if g&(1<<bit) else -1
        x=tuple(d)
        if x in targets:targets[x]+=1
        prev=g
    assert set(targets.values())=={1}
    v=(1,0,0,0,0,0); w=(2,0,0,0,0,0); q=(-1,0,0,0,0,0)
    assert sup(v)==sup(w)
    assert sup(tuple(x+y for x,y in zip(v,q)))!=sup(tuple(x+y for x,y in zip(w,q)))
    print(json.dumps({"status":"R722_X6_OBSERVER_CHANGE_SUPPORT_EXACT_PASS","increments":4096,"anchors":3,"anchor_cases":12288,"supports":53,"histogram":hist,"S6_checks":38160,"all_boolean_states":1048576,"singleton_targets":53,"counterexample":{"v":v,"w":w,"q":q}}))
if __name__=="__main__":main()
