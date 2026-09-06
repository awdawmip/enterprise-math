#!/usr/bin/env python3
"""Exact checks for X6 upper V34 relation-time -> transfer-chirality bridge."""
from itertools import combinations, permutations

TRIADS=tuple(combinations(range(6),3))
NEIGH={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}

def is_triangle(A,B,C):
    return B in NEIGH[A] and C in NEIGH[A] and C in NEIGH[B]

def orientation_from_previous(A,B,C,prev):
    # Current Cell carries A; B,C are the other two triangle states.
    assert is_triangle(A,B,C)
    assert prev in (B,C)
    nxt=C if prev==B else B
    # oriented active-state cycle is prev -> A -> nxt -> prev
    return (prev,A,nxt)

def transfer_seed(cell_of,oriented_cycle):
    # To move state cur -> next, the Cell carrying next sends one context token
    # to the Cell currently carrying cur.
    prev,A,nxt=oriented_cycle
    cyc=(A,nxt,prev)  # current A then next then third
    edges=[]
    for i,cur in enumerate(cyc):
        next_state=cyc[(i+1)%3]
        edges.append((cell_of[next_state],cell_of[cur]))
    return tuple(edges)

def contexts_from_edges(edges):
    incoming={}
    for src,dst in edges:
        assert dst not in incoming
        incoming[dst]=src
    return incoming

CURVED=((0,1,2),(0,1,3),(0,2,3))
FLAT=((0,1,2),(0,1,3),(0,1,4))
for tri in (CURVED,FLAT):
    A,B,C=tri
    cell_of={A:'xA',B:'xB',C:'xC'}
    o1=orientation_from_previous(A,B,C,C)
    o2=orientation_from_previous(A,B,C,B)
    assert o1==(C,A,B)
    assert o2==(B,A,C)
    e1=transfer_seed(cell_of,o1)
    e2=transfer_seed(cell_of,o2)
    assert set(e1)=={('xB','xA'),('xC','xB'),('xA','xC')}
    assert set(e2)=={(b,a) for a,b in e1}
    c1=contexts_from_edges(e1)
    assert c1=={'xA':'xB','xB':'xC','xC':'xA'}

# Every J(6,3) triangle and every choice of current vertex has exactly two
# ordered previous-edge seeds, mapped to opposite transfer-ring orientations.
triangles=[]
for A,B,C in combinations(TRIADS,3):
    if is_triangle(A,B,C): triangles.append((A,B,C))
assert len(triangles)==120
cases=0
for tri in triangles:
    for current in tri:
        others=[x for x in tri if x!=current]
        cell_of={tri[i]:i for i in range(3)}
        seeds=[]
        for prev in others:
            A=current; B,C=others
            orient=orientation_from_previous(A,B,C,prev)
            edges=set(transfer_seed(cell_of,orient))
            seeds.append(edges); cases+=1
        assert seeds[1]=={(b,a) for a,b in seeds[0]}

# Joint Cell relabeling covariance of the edge set.
base=CURVED
cell_of={base[i]:i for i in range(3)}
orient=orientation_from_previous(base[0],base[1],base[2],base[2])
base_edges=set(transfer_seed(cell_of,orient))
for p in permutations(range(3)):
    relabeled={(p[a],p[b]) for a,b in base_edges}
    assert len(relabeled)==3
    assert all(a!=b for a,b in relabeled)
    assert {a for a,b in relabeled}=={0,1,2}
    assert {b for a,b in relabeled}=={0,1,2}

print('PASS_X6_RELATION_TIME_SEED_V34')
print('J633_triangles',len(triangles))
print('ordered_previous_edge_seed_cases',cases)
print('seed_fiber_per_current_triangle_vertex',2)
print('opposite_previous_edges_give_reverse_transfer_ring',True)
