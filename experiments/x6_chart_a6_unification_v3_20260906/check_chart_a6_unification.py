#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations

AX=set(range(6))
CHARTS=tuple(frozenset(s) for s in combinations(range(6),3))
ID=tuple(range(6))

def compose(p,q): return tuple(p[q[i]] for i in range(6))
def parity(p): return sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2

def adjacent(S,T): return len(S&T)==2

def transposition(a,b):
    p=list(range(6)); p[a],p[b]=p[b],p[a]; return tuple(p)

def even_lift(S,T):
    if not adjacent(S,T): raise ValueError
    K=S&T; a=next(iter(S-K)); b=next(iter(T-K)); rest=tuple(sorted(AX-(S|T)))
    p=list(range(6))
    p[a],p[b]=p[b],p[a]
    c,d=rest; p[c],p[d]=p[d],p[c]
    return tuple(p)

def odd_lift(S,T):
    K=S&T; a=next(iter(S-K)); b=next(iter(T-K))
    return transposition(a,b)

# Every adjacent chart edge has one odd and one even natural lift.
edges=[]
for S,T in combinations(CHARTS,2):
    if adjacent(S,T):
        o=odd_lift(S,T); e=even_lift(S,T)
        assert parity(o)==1 and parity(e)==0
        # both fix shared axes and exchange removed/entering axes
        K=S&T
        assert all(o[k]==k and e[k]==k for k in K)
        edges.append((S,T,e))
# Johnson J(6,3): 20 vertices degree 9 -> 90 edges.
assert len(edges)==90

# Distinct even lifts are exactly the 45 double transpositions.
lifts={e for _,_,e in edges}
assert len(lifts)==45
for p in lifts:
    moved=[i for i in range(6) if p[i]!=i]
    assert len(moved)==4 and parity(p)==0
    assert compose(p,p)==ID

# Generate A6 from the 45 lifts.
G={ID}; q=deque([ID])
while q:
    x=q.popleft()
    for g in lifts:
        y=compose(g,x)
        if y not in G:
            G.add(y); q.append(y)
assert len(G)==360 and all(parity(p)==0 for p in G)

# Triangle holonomy classification.
def loop(path):
    out=ID
    for S,T in zip(path,path[1:]):
        out=compose(even_lift(S,T),out)
    return out

def cycle_type(p):
    seen=set(); lens=[]
    for i in range(6):
        if i in seen: continue
        x=i;n=0
        while x not in seen:
            seen.add(x);n+=1;x=p[x]
        if n>1:lens.append(n)
    return tuple(sorted(lens,reverse=True))

tri=Counter()
for S,T,U in combinations(CHARTS,3):
    if adjacent(S,T) and adjacent(T,U) and adjacent(U,S):
        union=len(S|T|U); inter=len(S&T&U)
        h=loop((S,T,U,S))
        tri[(union,inter,cycle_type(h))]+=1
assert sum(tri.values())==120
assert tri[(5,2,())]==60
assert tri[(4,1,(2,2))]==60

# Local restriction of four-axis holonomy is one transposition; hidden complement
# is the second transposition. Verify on every curved triangle based at each first chart.
for S,T,U in combinations(CHARTS,3):
    if not (adjacent(S,T) and adjacent(T,U) and adjacent(U,S)): continue
    if len(S|T|U)!=4: continue
    h=loop((S,T,U,S))
    moved_inside=sum(h[i]!=i for i in S)
    outside=AX-(S|T|U)
    moved_out=sum(h[i]!=i for i in outside)
    assert moved_inside==2 and moved_out==2

# Example decomposition of a double transposition into two 3-cycles.
def cycle3(a,b,c):
    p=list(range(6));p[a]=b;p[b]=c;p[c]=a;return tuple(p)
target=transposition(0,1)
target=compose(transposition(2,3),target) # (23)(01), disjoint so order irrelevant
assert compose(cycle3(0,3,2),cycle3(0,1,2))==target

print('PASS_X6_CHART_A6_UNIFICATION_V3')
print('charts',len(CHARTS))
print('Johnson_edges',len(edges))
print('distinct_even_chart_lifts',len(lifts))
print('even_chart_lift_generated_group_order',len(G))
print('flat_triangles',tri[(5,2,())])
print('double_transposition_holonomy_triangles',tri[(4,1,(2,2))])
print('common_group','A6')
