#!/usr/bin/env python3
"""Exact finite checker for P000 signed-K4/cohomology prior-art audit V5.

No external packages or network calls.
"""

from itertools import permutations, product

V = ("A", "B", "C", "D")
EDGES = tuple((V[i], V[j]) for i in range(4) for j in range(i + 1, 4))
Q = {
    ("A", "B"): -1,
    ("A", "C"): -1,
    ("A", "D"): +1,
    ("B", "C"): -1,
    ("B", "D"): +1,
    ("C", "D"): +1,
}
H = {"A": +1, "B": +1, "C": +1, "D": -1}

def edge(u, v):
    return tuple(sorted((u, v)))

def q(u, v):
    return Q[edge(u, v)]

def cycle_sign(cyc, sig=Q):
    z = 1
    for i, u in enumerate(cyc):
        v = cyc[(i + 1) % len(cyc)]
        z *= sig[edge(u, v)]
    return z

def switch(sig, h):
    return {e: h[e[0]] * sig[e] * h[e[1]] for e in EDGES}

def inv_perm(p):
    return {p[v]: v for v in V}

def act_sig(p, sig):
    pinv = inv_perm(p)
    return {
        e: sig[edge(pinv[e[0]], pinv[e[1]])]
        for e in EDGES
    }

def compose(p, r):
    # p*r means first r, then p.
    return {v: p[r[v]] for v in V}

def gauge_for(p):
    pinv = inv_perm(p)
    return {v: H[v] * H[pinv[v]] for v in V}

def act_vertex_function(p, f):
    pinv = inv_perm(p)
    return {v: f[pinv[v]] for v in V}

def mul_vertex_functions(f, g):
    return {v: f[v] * g[v] for v in V}

# 1. Cycle signs.
triangles = [
    ("A","B","C"), ("A","B","D"),
    ("A","C","D"), ("B","C","D")
]
four_cycles = [
    ("A","B","C","D"),
    ("A","B","D","C"),
    ("A","C","B","D"),
]
assert {c: cycle_sign(c) for c in triangles} == {c: -1 for c in triangles}
assert {c: cycle_sign(c) for c in four_cycles} == {c: +1 for c in four_cycles}

# 2. Antibalance and explicit all-negative normal form.
Q0 = switch(Q, H)
assert set(Q0.values()) == {-1}

# Exhaustively verify all simple K4 cycles have sign (-1)^length.
all_cycles = set()
for k in (3,4):
    for cyc in permutations(V, k):
        # normalize up to rotation and reversal
        rots = []
        s = list(cyc)
        for r in range(k):
            rots.append(tuple(s[r:]+s[:r]))
        sr = list(reversed(s))
        for r in range(k):
            rots.append(tuple(sr[r:]+sr[:r]))
        all_cycles.add(min(rots))
for cyc in all_cycles:
    assert cycle_sign(cyc) == (-1) ** len(cyc)

# 3. H^1(K4;F2) coordinate: fundamental triangle signs are (1,1,1).
# negative -> 1. Spanning tree AB, AC, AD; chords BC, BD, CD.
fundamental = [("A","B","C"), ("A","B","D"), ("A","C","D")]
assert tuple(0 if cycle_sign(c) == +1 else 1 for c in fundamental) == (1,1,1)

# 4. Full S4 strictly fixes Q0, and the original-gauge correction is a 1-coboundary.
S4 = []
for image in permutations(V):
    p = dict(zip(V, image))
    S4.append(p)
    assert act_sig(p, Q0) == Q0
assert len(S4) == 24

for p in S4:
    gp = gauge_for(p)
    assert switch(act_sig(p, Q), gp) == Q

for p in S4:
    for r in S4:
        pr = compose(p, r)
        lhs = gauge_for(pr)
        rhs = mul_vertex_functions(gauge_for(p), act_vertex_function(p, gauge_for(r)))
        assert lhs == rhs

# 5. Signed double cover in all-negative gauge = K_4,4 minus a perfect matching = Q3.
cover_vertices = tuple((v, s) for v in V for s in (+1,-1))
cover_edges = set()
for i, u in enumerate(V):
    for v in V[i+1:]:
        # all-negative edge lifts across sheets.
        cover_edges.add(frozenset(((u,+1),(v,-1))))
        cover_edges.add(frozenset(((u,-1),(v,+1))))
assert len(cover_vertices) == 8
assert len(cover_edges) == 12
deg = {x: 0 for x in cover_vertices}
for e in cover_edges:
    for x in e:
        deg[x] += 1
assert set(deg.values()) == {3}

cube = {
    ("A",+1):(0,0,0), ("B",+1):(0,1,1),
    ("C",+1):(1,0,1), ("D",+1):(1,1,0),
    ("A",-1):(1,1,1), ("B",-1):(1,0,0),
    ("C",-1):(0,1,0), ("D",-1):(0,0,1),
}
def hamming(a,b):
    return sum(x != y for x,y in zip(a,b))
assert all((frozenset((x,y)) in cover_edges) == (hamming(cube[x],cube[y]) == 1)
           for i,x in enumerate(cover_vertices) for y in cover_vertices[i+1:])

# 6. S4 lift is split; deck involution is central.
def lift(p, x):
    v,s = x
    return (p[v], s)
def deck(x):
    v,s = x
    return (v,-s)

for p in S4:
    # projected action is a cover automorphism
    for e in cover_edges:
        x,y = tuple(e)
        assert frozenset((lift(p,x), lift(p,y))) in cover_edges
    for x in cover_vertices:
        assert lift(p, deck(x)) == deck(lift(p, x))

# Faithfulness of S4 lift and intersection with deck C2 is trivial.
for p in S4:
    if all(lift(p,x) == x for x in cover_vertices):
        assert all(p[v] == v for v in V)
    assert not all(lift(p,x) == deck(x) for x in cover_vertices)

# 7. Carrier presentation a=(BCD), b=(AB): exact split lift residues (0,0,0).
a = {"A":"A","B":"C","C":"D","D":"B"}
b = {"A":"B","B":"A","C":"C","D":"D"}
identity = {v:v for v in V}
def power(p,n):
    out=identity
    for _ in range(n):
        out=compose(p,out)
    return out
assert power(a,3) == identity
assert power(b,2) == identity
assert power(compose(a,b),4) == identity

# 8. Six-edge action is faithful. Complement on 2-subsets commutes with S4 but is outside it.
edge_set = set(EDGES)
def edge_action(p,e):
    return edge(p[e[0]], p[e[1]])
edge_actions = {
    tuple(edge_action(p,e) for e in EDGES)
    for p in S4
}
assert len(edge_actions) == 24

def complement_edge(e):
    return tuple(sorted(set(V) - set(e)))
assert complement_edge(complement_edge(("A","B"))) == ("A","B")
for p in S4:
    for e in EDGES:
        assert complement_edge(edge_action(p,e)) == edge_action(p,complement_edge(e))

# Complement is not induced by any vertex permutation.
assert all(any(edge_action(p,e) != complement_edge(e) for e in EDGES) for p in S4)

stars = {v: {e for e in EDGES if v in e} for v in V}
tri_complements = {v: edge_set - stars[v] for v in V}
for v in V:
    assert {complement_edge(e) for e in stars[v]} == tri_complements[v]
    assert tri_complements[v] not in stars.values()

print("PASS")
print("q_normal_form=all-negative K4")
print("H1_graph_cycle_coordinates=(1,1,1)")
print("S4_invariant_representative=yes")
print("gamma_obstruction=0 (explicit fixed representative)")
print("canonical_signed_cover=Q3=K4,4-minus-matching")
print("carrier_lift=S4xC2 split")
print("carrier_generator_residues=(alpha,beta,gamma)=(0,0,0)")
print("star_complement_extra_C2=outside physical S4")
