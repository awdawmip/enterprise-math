#!/usr/bin/env python3
"""R762CL exact integer N-BRC: K4 six-token triad partitions and swap graph."""
from itertools import combinations, permutations
from math import factorial
import json
V=tuple(range(4))
E=tuple(combinations(V,2))
ES=frozenset(E)
def canon(A):
    A=frozenset(A)
    B=ES-A
    return tuple(sorted((tuple(sorted(A)),tuple(sorted(B)))))
S=tuple(sorted({canon(A) for A in combinations(E,3)}))
assert len(S)==10
def kind(T):
    d=tuple(sorted(sum(v in e for e in T) for v in V))
    return {(1,1,1,3):'star',(0,2,2,2):'face',(1,1,2,2):'path'}[d]
def tag(s):
    a,b=sorted(kind(T) for T in s)
    return 'SF' if (a,b)==('face','star') else 'PP' if (a,b)==('path','path') else None
tags={s:tag(s) for s in S}
assert sorted(tags.values())==['PP']*6+['SF']*4
G={}
for s in S:
    A,B=map(set,s)
    nxt={canon((A-{a})|{b}) for a in A for b in B}
    assert nxt==set(S)-{s}
    G[s]=nxt
perms=list(permutations(V))
def act(s,p):
    return canon([tuple(sorted((p[u],p[v]))) for u,v in s[0]])
remaining=set(S)
orbits=[]
while remaining:
    o={act(min(remaining),p) for p in perms}
    remaining-=o
    orbits.append(o)
assert sorted(map(len,orbits))==[4,6]
M={'SF':{'SF':3,'PP':6},'PP':{'SF':4,'PP':5}}
for s in S:
    assert {k:sum(tags[v]==k for v in G[s]) for k in ('SF','PP')}==M[tags[s]]
    for p in perms:
        assert {act(v,p) for v in G[s]}==G[act(s,p)]
walks={s:{s:1} for s in S}
checks=0
for t in range(13):
    for s in S:
        total=sum(walks[s].values())
        sf=sum(c for x,c in walks[s].items() if tags[x]=='SF')
        assert total==9**t
        assert 10*sf==4*9**t+(6 if tags[s]=='SF' else -4)*(-1)**t
        checks+=1
    walks={s:{u:sum(walks[s].get(v,0) for v in G[u]) for u in S} for s in S}
n=lambda m:factorial(3*m)//(6**m*factorial(m))
assert [n(m) for m in range(1,5)]==[1,10,280,15400]
print(json.dumps({'schema':'R762CL_BRC_EVIDENCE_V1','states':10,
'orbits':{'SF':4,'PP':6},'swap_graph':'K10','degree':9,
'count_transfer':M,'s4_group_actions':len(perms),'s4_graph_covariance_checks':len(perms)*len(S),
'depth_range':[0,12],'start_depth_checks':checks,
'walk_counts_t0_to_t12':[9**t for t in range(13)],
'general_3m_partition_counts':[1,10,280,15400],
'author_execution':'PASS','native_triadic_event_permission':'UNVERIFIED',
'independent_review':'NOT_REVIEWED'},indent=2))
