#!/usr/bin/env python3
"""Exact six-edge, four-STAR triad BRC group and mixing certificate."""
from collections import Counter, deque
from itertools import combinations, permutations
from fractions import Fraction
import json

V=range(4)
edges=list(combinations(V,2))
assert len(edges)==6
ID=tuple(range(6))

def compose(p,q):return tuple(p[q[i]] for i in range(6))
def invert(p):return tuple(p.index(i) for i in range(6))
def oriented_cycle(triple,reverse=False):
    a,b,c=triple;p=list(ID)
    if reverse:p[a],p[b],p[c]=c,a,b
    else:p[a],p[b],p[c]=b,c,a
    return tuple(p)

stars=[tuple(i for i,e in enumerate(edges) if v in e) for v in V]
assert all(len(t)==3 for t in stars)
C=[oriented_cycle(t,reverse) for t in stars for reverse in (False,True)]
assert len(set(C))==8

ALL=list(permutations(range(6)))
EVEN={p for p in ALL if sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2==0}
assert len(EVEN)==360 and set(C)<=EVEN

# Complete BFS: every edge is a left multiplication by one allowed branch.
levels={ID:0};q=deque([ID])
while q:
    p=q.popleft()
    for c in C:
        r=compose(c,p)
        if r not in levels:
            levels[r]=levels[p]+1;q.append(r)
assert set(levels)==EVEN
layer_counts=dict(sorted(Counter(levels.values()).items()))
assert layer_counts=={0:1,1:8,2:48,3:182,4:112,5:9}

S4=[tuple(edges.index(tuple(sorted((perm[a],perm[b])))) for a,b in edges) for perm in permutations(V)]
assert len(set(S4))==24
assert all({compose(compose(s,c),invert(s)) for c in C}==set(C) for s in S4)

# Independently generate 360 states; derive full S4 conjugacy orbits.
left=set(EVEN);orbits=[]
while left:
    p=next(iter(left))
    orb={compose(compose(s,p),invert(s)) for s in S4}
    assert orb<=EVEN
    left-=orb;orbits.append(orb)
assert len(orbits)==22

horizon=[];counts={ID:1}
for h in range(1,7):
    nxt=Counter()
    for p,k in counts.items():
        for g in C:nxt[compose(g,p)]+=k
    counts=nxt
    assert sum(counts.values())==8**h
    assert set(counts)=={p for p,d in levels.items() if d<=h} - ({ID} if h==1 else set())
    assert all(len({counts.get(p,0) for p in orb})==1 for orb in orbits)
    tv=sum(abs(Fraction(counts.get(p,0),8**h)-Fraction(1,360)) for p in EVEN)/2
    horizon.append(dict(depth=h,support=len(counts),min_path_count=min(counts.values()),max_path_count=max(counts.values()),tv=str(tv)))
assert horizon[3]['support']==351 and horizon[4]['support']==360
assert horizon[4]['min_path_count']==44 and horizon[4]['max_path_count']==326
assert horizon[4]['tv']=='28619/184320'
# Every five-step transition is at least 44/8^5 = (495/1024)/360.
assert Fraction(44*360,8**5)==Fraction(495,1024)
print(json.dumps(dict(research_id='R762FX',method='exact BFS + integer convolution + S4 orbit check',edges=edges,stars=stars,branches=8,group_size=len(levels),minimal_word_length_counts=layer_counts,diameter=5,S4_conjugacy_orbits=len(orbits),horizons=horizon,five_step_minorization='495/1024',five_step_TV_contraction='529/1024',status='PASS',review='NOT_REVIEWED'),indent=2))
