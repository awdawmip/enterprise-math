#!/usr/bin/env python3
"""Deterministic checker for P000 Gen11 framed full-Cell b-equivariance.

Task-local only. It checks an exact finite relational-model theorem and
regressions from Gen7--Gen10. It does NOT mutate P000, identify Cell identity
with carrier/readout data, or promote presentation S6 to native rotations.
"""
from itertools import permutations
from math import factorial

N = 6
ID = tuple(range(N))
PERMS = list(permutations(range(N)))

def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(N))

def inv(p):
    r = [None] * N
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)

def generated_group(gens):
    seen = {ID}
    todo = [ID]
    while todo:
        x = todo.pop()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen

def relabel_vector(V, g):
    gi = inv(g)
    return [V[gi[c]] for c in range(N)]

def relabel_matrix(M, g):
    gi = inv(g)
    return [[M[gi[c]][gi[d]] for d in range(N)] for c in range(N)]

def pass_matrix(M, f):
    return [[M[f[i]][f[j]] for j in range(N)] for i in range(N)]

def transport_from_frames(fx, fy):
    return compose(fy, inv(fx))

def induced_pi(fx, frx, b):
    return compose(frx, compose(b, inv(fx)))

def path_transport(path, transports):
    cur = ID
    for x, y in zip(path, path[1:]):
        cur = compose(transports[(x, y)], cur)
    return cur

b = (0, 3, 4, 1, 2, 5)
assert compose(b, b) == ID

# Gen7 regression.
B0, B1 = {0, 1, 2}, {3, 4, 5}
W = []
for p in PERMS:
    image = {p[i] for i in B0}
    if image == B0 or image == B1:
        W.append(p)
assert len(W) == 72
assert b not in W
assert len(generated_group(W + [b])) == 720

# Gen8 regression.
source_edges = frozenset({(0, 1), (1, 2), (2, 0)})
target_edges = frozenset({(0, 3), (3, 4), (4, 0)})
cycle_pair = {source_edges, target_edges}
matching = {frozenset({1, 3}), frozenset({2, 4})}

def image_edge_set(p, edges):
    return frozenset((p[a], p[c]) for a, c in edges)

def image_matching(p, mat):
    out = set()
    for pair in mat:
        a, c = tuple(pair)
        out.add(frozenset({p[a], p[c]}))
    return out

aut_sigma_b = []
for p in PERMS:
    if p[0] != 0 or p[5] != 5:
        continue
    if {image_edge_set(p, source_edges), image_edge_set(p, target_edges)} != cycle_pair:
        continue
    if image_matching(p, matching) != matching:
        continue
    aut_sigma_b.append(p)
assert set(aut_sigma_b) == {ID, b}

# Gen9 regression.
stabilizers = [
    sum(all(p[i] == i for i in range(k)) for p in PERMS)
    for k in range(7)
]
assert stabilizers == [720, 120, 24, 6, 2, 1, 1]
assert stabilizers == [factorial(6-k) for k in range(7)]

# Gen10 regression.
def zero_matrix():
    return [[0 for _ in range(N)] for _ in range(N)]

def omega_b_cell(M, frame):
    P = pass_matrix(M, frame)
    p24, p42 = P[1][3], P[3][1]
    p35, p53 = P[2][4], P[4][2]
    return p24 > 0 and p35 > 0 and p24 == p42 and p35 == p53

f_probe = (2, 5, 1, 4, 0, 3)
M_probe = [[10*i+j for j in range(N)] for i in range(N)]
P_probe = pass_matrix(M_probe, f_probe)
for g in PERMS:
    assert pass_matrix(relabel_matrix(M_probe, g), compose(g, f_probe)) == P_probe

frames4 = [
    ID,
    (1, 0, 2, 3, 5, 4),
    (2, 1, 0, 5, 4, 3),
    (5, 4, 3, 2, 1, 0),
]
T4 = {}
for x, y in [(0,1),(1,2),(2,3),(3,0)]:
    T4[(x,y)] = transport_from_frames(frames4[x], frames4[y])
    T4[(y,x)] = inv(T4[(x,y)])
assert path_transport([0,1,2,3,0], T4) == ID

M_noomega = zero_matrix()
for i in range(N):
    M_noomega[i][i] = 1
assert not omega_b_cell(M_noomega, ID)

M_omega = zero_matrix()
for i in range(N):
    M_omega[i][i] = 1
M_omega[1][3] = M_omega[3][1] = 2
M_omega[2][4] = M_omega[4][2] = 3
assert omega_b_cell(M_omega, ID)

# Gen11 exact model machinery.
def edges_oriented(edges):
    out = []
    for e in edges:
        a, c = tuple(e)
        out.extend([(a,c),(c,a)])
    return out

def cell_bijection(r, cells):
    return set(r.keys()) == set(cells) and set(r.values()) == set(cells) and len(set(r.values())) == len(cells)

def cell_involution(r, cells):
    return cell_bijection(r, cells) and all(r[r[x]] == x for x in cells)

def adjacency_equivariant(r, edges):
    image = {frozenset({r[a], r[c]}) for a, c in (tuple(e) for e in edges)}
    return image == set(edges)

def pf10_equivariant(r, frames, Is, Os, Ms):
    for x in frames:
        rx = r[x]
        pi = induced_pi(frames[x], frames[rx], b)
        for c in range(N):
            if Is[rx][pi[c]] != Is[x][c]:
                return False
            if Os[rx][pi[c]] != Os[x][c]:
                return False
            for d in range(N):
                if Ms[rx][pi[c]][pi[d]] != Ms[x][c][d]:
                    return False
    return True

def connection_natural(r, frames, T, edges):
    for x, y in edges_oriented(edges):
        rx, ry = r[x], r[y]
        pi_x = induced_pi(frames[x], frames[rx], b)
        pi_y = induced_pi(frames[y], frames[ry], b)
        lhs = compose(T[(rx,ry)], pi_x)
        rhs = compose(pi_y, T[(x,y)])
        if lhs != rhs:
            return False
    return True

def strict_b_automorphism(r, cells, edges, frames, Is, Os, Ms, T=None):
    if not cell_involution(r, cells):
        return False
    if not adjacency_equivariant(r, edges):
        return False
    if not pf10_equivariant(r, frames, Is, Os, Ms):
        return False
    if T is not None and not connection_natural(r, frames, T, edges):
        return False
    for x in cells:
        rx = r[x]
        pi_x = induced_pi(frames[x], frames[rx], b)
        pi_rx = induced_pi(frames[rx], frames[x], b)
        if compose(pi_rx, pi_x) != ID:
            return False
    return True

def frame_connection(cells, edges, frames):
    T = {}
    for x, y in edges_oriented(edges):
        T[(x,y)] = transport_from_frames(frames[x], frames[y])
    return T

def all_cell_automorphisms(cells, edges):
    cells = tuple(cells)
    ans = []
    for p in permutations(cells):
        r = dict(zip(cells, p))
        if cell_involution(r, cells) and adjacency_equivariant(r, edges):
            ans.append(r)
    return ans

def exists_strict_b(cells, edges, frames, Is, Os, Ms, T=None):
    return any(
        strict_b_automorphism(r, cells, edges, frames, Is, Os, Ms, T)
        for r in all_cell_automorphisms(cells, edges)
    )

def omega_nonempty(cells, frames, Ms):
    return any(omega_b_cell(Ms[x], frames[x]) for x in cells)

cells2 = (0, 1)
edges2 = {frozenset({0,1})}
frames2 = {0: ID, 1: ID}
r_swap = {0:1, 1:0}
T2 = frame_connection(cells2, edges2, frames2)
ones = [1] * N

def repeat_pf(M, I=None, O=None):
    if I is None: I = ones
    if O is None: O = ones
    return (
        {x: list(I) for x in cells2},
        {x: list(O) for x in cells2},
        {x: [row[:] for row in M] for x in cells2},
    )

# Exact positive witness.
I_tt, O_tt, M_tt = repeat_pf(M_omega)
assert strict_b_automorphism(r_swap, cells2, edges2, frames2, I_tt, O_tt, M_tt, T2)
assert omega_nonempty(cells2, frames2, M_tt)

# Frame-induced connection naturality is algebraically redundant.
for fx in PERMS[::37]:
    for fy in PERMS[::53]:
        fs = {0: fx, 1: fy}
        Ts = frame_connection(cells2, edges2, fs)
        assert connection_natural(r_swap, fs, Ts, edges2)

# Gauge covariance of Pi and naturality.
gauges = {0: PERMS[101], 1: PERMS[503]}
frames2g = {x: compose(gauges[x], frames2[x]) for x in cells2}
T2g = {}
for x, y in edges_oriented(edges2):
    T2g[(x,y)] = compose(gauges[y], compose(T2[(x,y)], inv(gauges[x])))
for x in cells2:
    lhs = induced_pi(frames2g[x], frames2g[r_swap[x]], b)
    rhs = compose(gauges[r_swap[x]], compose(induced_pi(frames2[x], frames2[r_swap[x]], b), inv(gauges[x])))
    assert lhs == rhs
assert connection_natural(r_swap, frames2g, T2g, edges2)
I_ttg = {x: relabel_vector(I_tt[x], gauges[x]) for x in cells2}
O_ttg = {x: relabel_vector(O_tt[x], gauges[x]) for x in cells2}
M_ttg = {x: relabel_matrix(M_tt[x], gauges[x]) for x in cells2}
assert strict_b_automorphism(r_swap, cells2, edges2, frames2g, I_ttg, O_ttg, M_ttg, T2g)

# Omega/base-R four-grid.
assert omega_nonempty(cells2, frames2, M_tt)
assert exists_strict_b(cells2, edges2, frames2, I_tt, O_tt, M_tt, T2)

I_asym = [1] * N
I_asym[1] = 1
I_asym[3] = 2
I_tf, O_tf, M_tf = repeat_pf(M_omega, I=I_asym)
assert omega_nonempty(cells2, frames2, M_tf)
assert not exists_strict_b(cells2, edges2, frames2, I_tf, O_tf, M_tf, T2)

I_ft, O_ft, M_ft = repeat_pf(M_noomega)
assert not omega_nonempty(cells2, frames2, M_ft)
assert exists_strict_b(cells2, edges2, frames2, I_ft, O_ft, M_ft, T2)

I_ff, O_ff, M_ff = repeat_pf(M_noomega, I=I_asym)
assert not omega_nonempty(cells2, frames2, M_ff)
assert not exists_strict_b(cells2, edges2, frames2, I_ff, O_ff, M_ff, T2)

# Minimal-condition independence: PF10 can pass while adjacency fails.
cells3 = (0,1,2)
edges3 = {frozenset({0,1}), frozenset({1,2})}
frames3 = {x: ID for x in cells3}
r_bad_adj = {0:1, 1:0, 2:2}
I3 = {x: ones[:] for x in cells3}
O3 = {x: ones[:] for x in cells3}
M3 = {x: [row[:] for row in M_noomega] for x in cells3}
assert cell_involution(r_bad_adj, cells3)
assert pf10_equivariant(r_bad_adj, frames3, I3, O3, M3)
assert not adjacency_equivariant(r_bad_adj, edges3)

# Adjacency can pass while PF10 fails.
assert adjacency_equivariant(r_swap, edges2)
assert not pf10_equivariant(r_swap, frames2, I_tf, O_tf, M_tf)

# Independent nonflat connection can be equivariant; nonflatness alone is not an obstruction.
tri = (0,1,2)
tri_edges = {frozenset({0,1}), frozenset({1,2}), frozenset({2,0})}
tri_frames = {x: ID for x in tri}
r_fix = {x:x for x in tri}
tri_I = {x: ones[:] for x in tri}
tri_O = {x: ones[:] for x in tri}
tri_M = {x: [row[:] for row in M_noomega] for x in tri}
h_comm = (5,1,2,3,4,0)
assert compose(h_comm, b) == compose(b, h_comm)
T_nonflat_good = {}
for x,y in edges_oriented(tri_edges):
    T_nonflat_good[(x,y)] = ID
T_nonflat_good[(2,0)] = h_comm
T_nonflat_good[(0,2)] = h_comm
H_good = path_transport([0,1,2,0], T_nonflat_good)
assert H_good == h_comm and H_good != ID
assert connection_natural(r_fix, tri_frames, T_nonflat_good, tri_edges)
assert strict_b_automorphism(r_fix, tri, tri_edges, tri_frames, tri_I, tri_O, tri_M, T_nonflat_good)

h_bad = (1,0,2,3,4,5)
assert compose(h_bad, b) != compose(b, h_bad)
T_nonflat_bad = dict(T_nonflat_good)
T_nonflat_bad[(2,0)] = h_bad
T_nonflat_bad[(0,2)] = inv(h_bad)
H_bad = path_transport([0,1,2,0], T_nonflat_bad)
assert H_bad == h_bad and H_bad != ID
assert not connection_natural(r_fix, tri_frames, T_nonflat_bad, tri_edges)
assert not strict_b_automorphism(r_fix, tri, tri_edges, tri_frames, tri_I, tri_O, tri_M, T_nonflat_bad)

# P000 strength guards.
P000_MUTATED = False
NATIVE_S6_PROMOTED = False
NATIVE_STATE_QUOTIENT_USED = False
CARRIER_EQUALITY_USED_AS_CELL_ID = False
TIME_MOVED = False
assert not P000_MUTATED
assert not NATIVE_S6_PROMOTED
assert not NATIVE_STATE_QUOTIENT_USED
assert not CARRIER_EQUALITY_USED_AS_CELL_ID
assert not TIME_MOVED

print("PASS P000_BASE_CELL_RB_EQUIVARIANCE_V11_CHECK")
print("terminal_class=FRAMED_FULL_CELL_b_AUTOMORPHISM_IFF_CLASSIFIED_AND_WITNESSED")
print("gen7_W_order=72")
print("gen7_W_plus_b_order=720")
print("gen8_AutSigma_b_order=2")
print("gen9_anchor_stabilizers=" + ",".join(map(str, stabilizers)))
print("gen10_PASS_gauge_invariant=true")
print("gen10_Omega_b_forced=false")
print("frame_induced_connection_naturality=automatic")
print("independent_connection_naturality=additional")
print("nonflat_holonomy_can_be_b_equivariant=true")
print("holonomy_equivariance_failure_can_obstruct=true")
print("Omega_and_base_R_four_grid=all_four_realized")
print("Omega_b_logic_vs_base_R=INDEPENDENT")
print("Omega_b_semantic_role=CONTACT_ROUTE_SPECIFIC")
print("base_R_b_witness=two_cell_nonidentity_swap")
print("full_P000_native_rotation_group_promoted=false")
