#!/usr/bin/env python3
"""R762KG: exact parity counterexample for three disjoint inactive Ports."""
from itertools import combinations,product
from math import comb
A=range(6)
P0=list(combinations(A,2));S=list(combinations(A,3))
D={(0,1),(2,3),(4,5)}
P=[p for p in P0 if p not in D];idx={p:i for i,p in enumerate(P)}
E={s:list(combinations([idx[p] for p in combinations(s,2) if p in idx],2)) for s in S}
F=[s for s in S if len(E[s])==1]
C=[s for s in S if len(E[s])==3]
assert (len(P),len(F),len(C))==(12,12,8)
bit=lambda uv:(1<<uv[0])^(1<<uv[1])
# Exactly four of twelve forced colors have multiplicity two; all other colors one.
FORCED_DOUBLED={(0,1,3),(0,1,5),(2,4,5),(3,4,5)}
counts={s:(2 if s in FORCED_DOUBLED else 1) for s in S}
assert sum(counts.values())==24 and sum(counts[s]==1 for s in C)==8
forced_boundary=0
for s in F:
 if counts[s]&1:forced_boundary^=bit(E[s][0])
assert forced_boundary==4010
# Complete 3^8 enumeration: no eight-singleton flexible edge choice matches.
solutions=0; image=set()
for digits in product(range(3),repeat=len(C)):
 x=0
 for s,j in zip(C,digits):x^=bit(E[s][j])
 image.add(x)
 if x==forced_boundary:solutions+=1
assert (len(image),solutions)==(1881,0)

classes={"pairwise_disjoint":0,"intersecting":0}
for missing in combinations(P0,3):
 disjoint=all(not(set(a)&set(b)) for a,b in combinations(missing,2))
 classes["pairwise_disjoint" if disjoint else "intersecting"]+=1
 if not disjoint:
  a,b=next((a,b) for a,b in combinations(missing,2) if set(a)&set(b))
  triad=tuple(sorted(set(a)|set(b)))
  assert len([p for p in combinations(triad,2) if p not in missing])<=1
assert classes=={"pairwise_disjoint":15,"intersecting":440}

def connected(edges):
 parent=list(range(len(P)))
 def r(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for a,b in edges:parent[r(a)]=r(b)
 return len({r(i) for i in range(len(P))})==1

# Feasible positive comparison: choose connected base, double every selected edge.
digits=(0,0,0,0,0,0,0,1)
selected=[E[s][0] for s in F]+[E[s][j] for s,j in zip(C,digits)]
assert connected(selected)
positive_even_events=selected*2
assert len(positive_even_events)==40
deg=[0]*len(P)
for a,b in positive_even_events:deg[a]+=1;deg[b]+=1
assert all(x>0 and x%2==0 for x in deg)
print({'inactive_pair_patterns':comb(15,3),'intersecting_zero_event_patterns':440,
       'disjoint_matching_patterns':15,'representative_inactive':['01','23','45'],
       'counterexample_total_events':24,'forced_doubled':['013','015','245','345'],
       'forced_boundary':forced_boundary,'flexible_edge_assignments_exhausted':3**8,
       'reachable_flexible_parities':len(image),'matching_assignments':solutions,
       'positive_feasible_all_double_events':40,'failures':0})
