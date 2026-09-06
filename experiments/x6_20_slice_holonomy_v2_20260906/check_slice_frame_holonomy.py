#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations

AX=tuple(range(6))
CHARTS=tuple(frozenset(s) for s in combinations(AX,3))

def adjacent(S,T): return len(S&T)==2

def trans(S,T):
    if not adjacent(S,T): raise ValueError('need adjacent charts')
    K=S&T
    a=next(iter(S-K)); b=next(iter(T-K))
    out={x:x for x in K}; out[a]=b
    return out

def transport_loop(path):
    S0=path[0]
    current={x:x for x in S0}
    for S,T in zip(path,path[1:]):
        r=trans(S,T)
        current={x:r[current[x]] for x in S0}
    return current

def cycletype(m):
    seen=set(); lens=[]
    for x in m:
        if x in seen: continue
        y=x; n=0
        while y not in seen:
            seen.add(y); n+=1; y=m[y]
        lens.append(n)
    return tuple(sorted(lens,reverse=True))

triangles=[]
for tri in combinations(CHARTS,3):
    if all(adjacent(a,b) for a,b in combinations(tri,2)):
        union=len(set().union(*tri))
        inter=len(set.intersection(*map(set,tri)))
        h=transport_loop((tri[0],tri[1],tri[2],tri[0]))
        triangles.append(((union,inter),cycletype(h)))
counts=Counter(triangles)
assert sum(counts.values())==120
assert counts[((5,2),(1,1,1))]==60
assert counts[((4,1),(2,1))]==60

# Base-chart loop holonomy generates all S3 permutations.
base=frozenset((0,1,2))
hgens=[]
for tri in combinations(CHARTS,3):
    if base not in tri or not all(adjacent(a,b) for a,b in combinations(tri,2)):
        continue
    union=len(set().union(*tri)); inter=len(set.intersection(*map(set,tri)))
    if (union,inter)!=(4,1): continue
    others=[x for x in tri if x!=base]
    for order in (others,others[::-1]):
        h=transport_loop((base,order[0],order[1],base))
        hgens.append(tuple(h[x] for x in sorted(base)))
transpositions=set(hgens)
assert len(transpositions)==3

def compose(p,q):
    # permutations as image tuples on 0,1,2
    return tuple(p[q[i]] for i in range(3))
ID=(0,1,2)
G={ID}; Q=deque([ID])
while Q:
    x=Q.popleft()
    for g in transpositions:
        y=compose(g,x)
        if y not in G:
            G.add(y); Q.append(y)
assert len(G)==6

# One adjacent chart switch needs exactly the entering-axis coordinate in
# addition to the old raw 3-coordinate observation.
S=frozenset((0,1,2)); T=frozenset((0,1,3))
z=(7,-2,5,11,100,-4)
obsS=tuple(z[i] for i in sorted(S))
obsT=tuple(z[i] for i in sorted(T))
repair=z[3]
reconstructed=(obsS[0],obsS[1],repair)
assert reconstructed==obsT
z2=(7,-2,5,99,100,-4)
assert tuple(z2[i] for i in sorted(S))==obsS
assert tuple(z2[i] for i in sorted(T))!=obsT

print('PASS_X6_20_SLICE_FRAME_HOLONOMY_V2')
print('charts',len(CHARTS))
print('Johnson_triangles',120)
print('flat_common_pair_triangles',60)
print('curved_four_axis_triangles',60)
print('base_holonomy_generators',len(transpositions))
print('holonomy_group_order',len(G))
print('holonomy_group','S3')
print('adjacent_raw_chart_repair_coordinates',1)
