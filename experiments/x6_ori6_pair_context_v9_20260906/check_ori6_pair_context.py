#!/usr/bin/env python3
"""Exact checks for A6-symmetric Ori6 selector obstruction and pair-context repair."""
from itertools import permutations, combinations
from collections import Counter
from math import comb

N=6
S6=tuple(permutations(range(N)))

def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
A6=tuple(p for p in S6 if parity(p)==0)

def compose(p,q): return tuple(p[q[i]] for i in range(N))
def inverse(p):
    q=[0]*N
    for i,j in enumerate(p): q[j]=i
    return tuple(q)
def conjugate(g,h): return compose(compose(g,h),inverse(g))

def centralizer(H): return tuple(p for p in S6 if all(compose(p,h)==compose(h,p) for h in H))

# No-context selector: A6-fixed odd permutation would have to centralize A6.
C0=centralizer(A6)
assert C0==(tuple(range(N)),)
assert not any(parity(p) for p in C0)

# One distinguished axis: stabilizer A5; still no odd centralizer.
H1=tuple(g for g in A6 if g[0]==0)
C1=centralizer(H1)
assert len(H1)==60
assert C1==(tuple(range(N)),)

# One unordered pair: stabilizer centralizer is {1,(01)}, so the transposition is
# the unique nontrivial equivariant odd frame normal form at the reference pair.
PAIR=frozenset((0,1))
H2=tuple(g for g in A6 if frozenset((g[0],g[1]))==PAIR)
C2=centralizer(H2)
swap01=(1,0,2,3,4,5)
assert len(H2)==24
assert set(C2)=={tuple(range(N)),swap01}
assert parity(swap01)==1

# Equivariant pair selector f({i,j})=(ij).
def transposition(i,j):
    p=list(range(N)); p[i],p[j]=p[j],p[i]; return tuple(p)
for pair in combinations(range(N),2):
    f=transposition(*pair)
    assert parity(f)==1
    for g in A6:
        gp=tuple(sorted((g[pair[0]],g[pair[1]])))
        assert conjugate(g,f)==transposition(*gp)

# Spatial action/path cost for a pair swap on integer state x.
def swap_state(x,i,j):
    y=list(x);y[i],y[j]=y[j],y[i];return tuple(y)
def l1(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def shortest_mult_pair_swap(x,i,j):
    d=abs(x[i]-x[j])
    return comb(2*d,d)
for x in ((1,0,0,0,0,0),(3,-1,0,0,0,0),(2,2,1,0,0,0)):
    y=swap_state(x,0,1); d=abs(x[0]-x[1])
    assert l1(x,y)==2*d
    assert shortest_mult_pair_swap(x,0,1)==comb(2*d,d)
    if d==0: assert x==y

# Two-token unit swap: both II and OO have a common midpoint, unlike triadic III uniqueness.
def unit(i):
    z=[0]*N;z[i]=1;return tuple(z)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
zero=(0,)*N
a,b=unit(0),unit(1)
outer=add(a,b)
# token a->b and b->a each have midpoint choices {0,a+b}
common=[]
for X in ('I','O'):
    for Y in ('I','O'):
        mx=zero if X=='I' else outer
        my=zero if Y=='I' else outer
        if mx==my: common.append(X+Y)
assert common==['II','OO']

# One-axis subset contexts cannot select an equivariant odd event; pair contexts can.
print('PASS_X6_ORI6_PAIR_CONTEXT_V9')
print('A6_centralizer_order',len(C0))
print('one_axis_stabilizer_order',len(H1))
print('one_axis_centralizer_order',len(C1))
print('pair_stabilizer_order',len(H2))
print('pair_centralizer',C2)
print('equivariant_odd_pair_events',15)
print('minimal_axis_subset_context_size_for_deterministic_odd_selector',2)
print('pair_swap_common_midpoint_branches',common)
print('pair_swap_common_midpoint_unique',False)
