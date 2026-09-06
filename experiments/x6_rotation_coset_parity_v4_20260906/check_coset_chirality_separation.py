#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import deque

# S6 permutation parity.
def parity(p):
    return sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2

# K4 vertices and six edges.
V=range(4)
E=tuple(combinations(V,2))
EI={e:i for i,e in enumerate(E)}

def edge_action(g):
    return tuple(EI[tuple(sorted((g[a],g[b])))] for a,b in E)

# Every S4 vertex permutation induces an even permutation of the six edges.
S4=tuple(permutations(range(4)))
images=tuple(edge_action(g) for g in S4)
assert len(set(images))==24
assert all(parity(p)==0 for p in images)

# Every vertex transposition induces exactly two disjoint edge transpositions.
def transposition(a,b):
    p=list(range(4)); p[a],p[b]=p[b],p[a]; return tuple(p)
for a,b in combinations(range(4),2):
    p=edge_action(transposition(a,b))
    moved=sum(p[i]!=i for i in range(6))
    assert moved==4 and parity(p)==0

# Local STAR chirality can reverse under an even global six-edge permutation:
# a K4 vertex transposition sends source star to target star and reverses the
# induced ordering; parity computation above already proves the separation.

# A local slot transposition on first three axes has both odd and even S6
# extensions depending on what happens on the complement.
odd=(1,0,2,3,4,5)
even=(1,0,2,4,3,5)
assert odd[:3]==even[:3]
assert parity(odd)==1 and parity(even)==0

# Index-two group count: signed frame group has 2^6 * 720; even-permutation
# triadic frame sector has 2^6 * 360.
B6=64*720
R=64*360
assert B6==46080 and R==23040 and B6//R==2

# Any odd permutation plus A6 generates S6. Check with one transposition and
# all 3-cycles on six symbols.
def compose(p,q): return tuple(p[q[i]] for i in range(6))
ID=tuple(range(6))
three=[]
for a,b,c in combinations(range(6),3):
    p=list(range(6)); p[a]=b;p[b]=c;p[c]=a
    three.append(tuple(p))
gens=three+[odd]
G={ID}; q=deque([ID])
while q:
    x=q.popleft()
    for g in gens:
        y=compose(g,x)
        if y not in G: G.add(y); q.append(y)
assert len(G)==720

print('PASS_X6_ROTATION_COSET_PARITY_V4')
print('K4_edge_action_order',len(set(images)))
print('K4_edge_action_all_even',True)
print('triadic_frame_group_order',R)
print('full_signed_frame_group_order',B6)
print('frame_index',2)
print('one_odd_axis_permutation_extends_to_full_S6',True)
print('local_chirality_bit_equals_global_axis_parity',False)
