#!/usr/bin/env python3
"""Exact nesting classification of all 741 frozen R5 radius-2 budget transitions.
Uses the companion self-contained VERIFY_R5_ALLOCATION_EDIT.py.
"""
from collections import Counter
from functools import lru_cache
from bisect import bisect_left
from VERIFY_R5_ALLOCATION_EDIT import frozen_blocks, local_dp, minimum_removed, optimal_language

X,B=frozen_blocks()
D=[local_dp(z) for z in B]
M=[min(d[0]) for d in D]
G=[]
for i,d in enumerate(D):
    gains=[d[0][k][0]-d[0][k+1][0] for k in range(M[i],len(B[i]))]
    assert all(gains[t]>=gains[t+1] for t in range(len(gains)-1))
    G.append(gains)
all_gains=sorted((v for gg in G for v in gg),reverse=True)
assert len(all_gains)==741 and sum(M)==213
assert Counter(all_gains)=={1:603,2:36,3:23,4:70,5:8,6:1}

@lru_cache(None)
def local_nested(i,extra):
    return minimum_removed(B[i],D[i],M[i]+extra,M[i]+extra+1,0)

def some_optimal(x,s,k):
    graph=optimal_language(x,s,k)
    out=[];cur=-1
    for t in range(k):
        cur=graph[(t,cur)][0]
        out.append(cur)
    return tuple(out)

def direct_global_check(centers,K,expected):
    assert len(centers)==K and centers==tuple(sorted(set(centers)))
    cost=0
    for value in X:
        j=bisect_left(centers,value)
        distance=min(abs(value-centers[t]) for t in (j-1,j) if 0<=t<len(centers))
        assert distance<=2
        cost+=distance
    assert cost==expected,(K,cost,expected)

rows=[];complete_witnesses=0
for u,g in enumerate(all_gains):
    k=213+u
    if g==1:
        rows.append((k,g,True,None,None))
        continue  # universal unit-gain nesting theorem
    if g>=4:
        rows.append((k,g,False,None,None))
        continue  # radius-2 single addition saves at most 3
    strict=[sum(v>g for v in gg) for gg in G]
    ties=[sum(v==g for v in gg) for gg in G]
    r=u-sum(strict)
    assert 0<=r<sum(ties)
    selected=None
    for i in range(len(B)):
        for t in range(ties[i]):
            if 0<=r-t<=sum(ties)-ties[i] and local_nested(i,strict[i]+t):
                selected=(i,t)
                break
        if selected:break
    if selected is None:
        rows.append((k,g,False,None,None))
        continue
    i,t=selected
    # Construct a globally optimal allocation whose only change is +1 in block i.
    used=[0]*len(B)
    used[i]=t
    todo=r-t
    for j in range(len(B)):
        if j==i:continue
        add=min(todo,ties[j]);used[j]=add;todo-=add
    assert todo==0
    allocation=[M[j]+strict[j]+used[j] for j in range(len(B))]
    assert sum(allocation)==k
    old=[];new=[]
    for j in range(len(B)):
        if j==i:
            z=local_nested(i,strict[i]+t)
            a,b=z[1:]
            assert z[0]==0
        else:
            a=some_optimal(B[j],D[j],allocation[j]);b=a
        old += [B[j][c] for c in a]
        new += [B[j][c] for c in b]
    old=tuple(old);new=tuple(new)
    assert set(old)<=set(new) and len(new)==k+1
    target=lambda K: 1070-sum(all_gains[:K-213])
    direct_global_check(old,k,target(k))
    direct_global_check(new,k+1,target(k+1))
    complete_witnesses+=1
    rows.append((k,g,True,i,strict[i]+t))

assert len(rows)==741
assert sum(y[2] for y in rows)==662
assert sum(not y[2] for y in rows)==79
assert complete_witnesses==59
print({'status':'PASS_EXACT_GLOBAL','input_boundaries':len(X),'block_count':len(B),
       'gain_histogram':dict(sorted(Counter(all_gains).items())),
       'nested_transitions':662,'forced_nonnested':79,
       'direct_global_old_new_witnesses_gain2_or_3':complete_witnesses,
       'nonnested_range':[213,291],'nested_range':[292,953],
       'local_pair_checks_cached':local_nested.cache_info().currsize})
