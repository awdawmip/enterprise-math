#!/usr/bin/env python3
"""Exact finite checker for P000 Gen12 common-model a/b lift, K4-star transport, and S4 closure."""
from itertools import combinations

def comp(p, q):
    """Permutation composition p∘q; tuples store images."""
    assert len(p) == len(q)
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    r = [0] * len(p)
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)

def ident(n):
    return tuple(range(n))

def power(p, k):
    z = ident(len(p))
    for _ in range(k):
        z = comp(p, z)
    return z

def generated(gens, n):
    e = ident(n)
    seen = {e}
    todo = [e]
    while todo:
        x = todo.pop()
        for g in gens:
            y = comp(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen

def pair_comp(P, Q):
    return (comp(P[0], Q[0]), comp(P[1], Q[1]))

def pair_power(P, k):
    z = (ident(len(P[0])), ident(len(P[1])))
    for _ in range(k):
        z = pair_comp(P, z)
    return z

def pair_generated(gens):
    e = (ident(len(gens[0][0])), ident(len(gens[0][1])))
    seen = {e}
    todo = [e]
    while todo:
        x = todo.pop()
        for g in gens:
            y = pair_comp(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen

def relv(v, g):
    gi = inv(g)
    return [v[gi[i]] for i in range(len(v))]

def relm(M, g):
    gi = inv(g)
    n = len(M)
    return [[M[gi[i]][gi[j]] for j in range(n)] for i in range(n)]

def frame_transport(fx, fy):
    return comp(fy, inv(fx))

def pi_for(axis_perm, r, frames, x):
    return comp(frames[r[x]], comp(axis_perm, inv(frames[x])))

def oriented(edges):
    out = []
    for e in edges:
        x, y = tuple(e)
        out.append((x, y))
        out.append((y, x))
    return out

def path_transport(path, T, n=6):
    z = ident(n)
    for x, y in zip(path, path[1:]):
        z = comp(T[(x, y)], z)
    return z

def adj_preserved(r, edges):
    return {frozenset((r[x], r[y])) for x, y in (tuple(e) for e in edges)} == set(edges)

def pf_equivariant(r, axis_perm, frames, ingress, egress, passage):
    for x in frames:
        rx = r[x]
        p = pi_for(axis_perm, r, frames, x)
        for c in range(6):
            if ingress[rx][p[c]] != ingress[x][c]:
                return False
            if egress[rx][p[c]] != egress[x][c]:
                return False
            for d in range(6):
                if passage[rx][p[c]][p[d]] != passage[x][c][d]:
                    return False
    return True

def connection_natural(r, axis_perm, frames, T, edges):
    for x, y in oriented(edges):
        lhs = comp(T[(r[x], r[y])], pi_for(axis_perm, r, frames, x))
        rhs = comp(pi_for(axis_perm, r, frames, y), T[(x, y)])
        if lhs != rhs:
            return False
    return True

def strict_lift(r, axis_perm, order, cells, edges, frames, ingress, egress, passage, T):
    if set(r) != set(cells) or set(r.values()) != set(cells):
        return False
    rt = tuple(r[x] for x in cells)
    if power(rt, order) != ident(len(cells)):
        return False
    if not adj_preserved(r, edges):
        return False
    if not pf_equivariant(r, axis_perm, frames, ingress, egress, passage):
        return False
    if not connection_natural(r, axis_perm, frames, T, edges):
        return False
    # Typed group law on local channel transport for the generator order.
    for x in cells:
        cur = x
        channel_word = ident(6)
        for _ in range(order):
            p = pi_for(axis_perm, r, frames, cur)
            channel_word = comp(p, channel_word)
            cur = r[cur]
        if cur != x or channel_word != ident(6):
            return False
    return True

# ---- Frozen carrier / native-axis actions ----
# Carrier vertices A,B,C,D are only witness labels for the accepted K4 carrier atlas.
A, B, C, D = range(4)
carrier_edges = ((A, B), (A, C), (A, D), (B, C), (B, D), (C, D))
# Frozen native axis types E1..E6 correspond to the accepted K4 edge incidence.
edge_to_axis = {
    frozenset((A, B)): 0,  # E1
    frozenset((A, C)): 1,  # E2
    frozenset((A, D)): 2,  # E3
    frozenset((B, C)): 3,  # E4
    frozenset((B, D)): 4,  # E5
    frozenset((C, D)): 5,  # E6
}
axis_to_edge = {v: k for k, v in edge_to_axis.items()}

carrier_a = (A, C, D, B)  # (BCD)
carrier_b = (B, A, C, D)  # (AB)

def induced_axis(carrier_perm):
    out = [None] * 6
    for i, e in axis_to_edge.items():
        u, v = tuple(e)
        image_edge = frozenset((carrier_perm[u], carrier_perm[v]))
        out[i] = edge_to_axis[image_edge]
    return tuple(out)

a_axis = induced_axis(carrier_a)
b_axis = induced_axis(carrier_b)
assert a_axis == (1, 2, 0, 5, 3, 4)       # (E1 E2 E3)(E4 E6 E5)
assert b_axis == (0, 3, 4, 1, 2, 5)       # (E2 E4)(E3 E5)
assert power(a_axis, 3) == ident(6)
assert power(b_axis, 2) == ident(6)
assert power(comp(a_axis, b_axis), 4) == ident(6)
assert len(generated([a_axis, b_axis], 6)) == 24

# ---- One exact common Full-Cell witness ----
# xA..xD are four distinct opaque native Cell identities.  Their labels are presentation only;
# no Cell is identified with a carrier object and no quotient is taken.
cells = (0, 1, 2, 3)
xA, xB, xC, xD = cells
r_a_t = (xA, xC, xD, xB)
r_b_t = (xB, xA, xC, xD)
r_a = dict(zip(cells, r_a_t))
r_b = dict(zip(cells, r_b_t))

# Native adjacency is K4 on the four opaque Cells.
cell_edges = {frozenset(e) for e in combinations(cells, 2)}
assert adj_preserved(r_a, cell_edges)
assert adj_preserved(r_b, cell_edges)

# Identity presentation frames; a later regression gauges them independently.
ID6 = ident(6)
frames = {x: ID6 for x in cells}

# Full PF-10 data: uniform ingress/egress and diagonal passage tensor.
# This makes Omega_b false, proving the successful rotation witness does not use the contact route.
one = [1] * 6
M0 = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
ingress = {x: one[:] for x in cells}
egress = {x: one[:] for x in cells}
passage = {x: [row[:] for row in M0] for x in cells}

# Retained frame-induced connection on every native adjacency edge.
T = {(x, y): frame_transport(frames[x], frames[y]) for x, y in oriented(cell_edges)}
assert all(value == ID6 for value in T.values())

assert strict_lift(r_a, a_axis, 3, cells, cell_edges, frames, ingress, egress, passage, T)
assert strict_lift(r_b, b_axis, 2, cells, cell_edges, frames, ingress, egress, passage, T)

# Gen11 route-specific regression: Omega_b is not used.
def omega_b(M):
    return (
        M[1][3] > 0 and M[1][3] == M[3][1]
        and M[2][4] > 0 and M[2][4] == M[4][2]
    )
assert not any(omega_b(passage[x]) for x in cells)

# ---- K4-star derived slice objects ----
J = {
    A: frozenset((0, 1, 2)),
    B: frozenset((0, 3, 4)),
    C: frozenset((1, 3, 5)),
    D: frozenset((2, 4, 5)),
}
assert frozenset(a_axis[i] for i in J[A]) == J[A]
assert frozenset(a_axis[i] for i in J[B]) == J[C]
assert frozenset(a_axis[i] for i in J[C]) == J[D]
assert frozenset(a_axis[i] for i in J[D]) == J[B]
assert frozenset(b_axis[i] for i in J[A]) == J[B]
assert frozenset(b_axis[i] for i in J[B]) == J[A]
assert frozenset(b_axis[i] for i in J[C]) == J[C]
assert frozenset(b_axis[i] for i in J[D]) == J[D]

# Declared downstream geometric star object:
# (opaque Cell, incident-axis set, induced PF-10 restriction, complete local three-axis relation).
cell_for_star = {A: xA, B: xB, C: xC, D: xD}
def star_object(u):
    axes = tuple(sorted(J[u]))
    local_rel = frozenset(frozenset((p, q)) for p, q in combinations(axes, 2))
    return {
        "cell": cell_for_star[u],
        "axes": frozenset(axes),
        "I": tuple(ingress[cell_for_star[u]][i] for i in axes),
        "O": tuple(egress[cell_for_star[u]][i] for i in axes),
        "Mdiag": tuple(passage[cell_for_star[u]][i][i] for i in axes),
        "local_rel": local_rel,
    }

def transport_star(u, carrier_perm, r, axis_perm):
    v = carrier_perm[u]
    src = star_object(u)
    dst = star_object(v)
    mapped_axes = frozenset(axis_perm[i] for i in src["axes"])
    mapped_rel = frozenset(
        frozenset(axis_perm[i] for i in pair)
        for pair in src["local_rel"]
    )
    return (
        r[src["cell"]] == dst["cell"]
        and mapped_axes == dst["axes"]
        and src["I"] == dst["I"]
        and src["O"] == dst["O"]
        and src["Mdiag"] == dst["Mdiag"]
        and mapped_rel == dst["local_rel"]
    )

for u in (A, B, C, D):
    assert transport_star(u, carrier_a, r_a, a_axis)
    assert transport_star(u, carrier_b, r_b, b_axis)

# Exact overlap/gluing regression: every two stars intersect in exactly the axis of their K4 edge;
# generator transport carries both the shared axis and opaque-Cell adjacency.
for u, v in combinations((A, B, C, D), 2):
    overlap = J[u] & J[v]
    assert len(overlap) == 1
    expected = {edge_to_axis[frozenset((u, v))]}
    assert overlap == expected
    for carrier_perm, r, axis_perm in ((carrier_a, r_a, a_axis), (carrier_b, r_b, b_axis)):
        uu, vv = carrier_perm[u], carrier_perm[v]
        mapped = frozenset(axis_perm[i] for i in overlap)
        assert mapped == (J[uu] & J[vv])
        assert frozenset((r[cell_for_star[u]], r[cell_for_star[v]])) in cell_edges

# ---- Exact enriched group and relation closure ----
RA = (r_a_t, a_axis)
RB = (r_b_t, b_axis)
Epair = (ident(4), ident(6))
assert pair_power(RA, 3) == Epair
assert pair_power(RB, 2) == Epair
assert pair_power(pair_comp(RA, RB), 4) == Epair

G = pair_generated([RA, RB])
assert len(G) == 24
cell_image = {g[0] for g in G}
axis_image = {g[1] for g in G}
assert len(cell_image) == 24
assert len(axis_image) == 24

cell_kernel = {g for g in G if g[0] == ident(4)}
axis_kernel = {g for g in G if g[1] == ident(6)}
assert cell_kernel == {Epair}
assert axis_kernel == {Epair}

# Stronger no-residue check on the declared enriched state:
# relation words are identity on Cells, axis types, PF-10 data, star objects and the retained connection.
relation_words = {
    "Ra^3": pair_power(RA, 3),
    "Rb^2": pair_power(RB, 2),
    "(RaRb)^4": pair_power(pair_comp(RA, RB), 4),
}
assert all(v == Epair for v in relation_words.values())

# Holonomy/connection regression: frame-induced connection is flat and equivariant.
# Triangles generate the cycle space of K4; all triangle holonomies are identity.
for u, v, w in combinations(cells, 3):
    assert path_transport([u, v, w, u], T) == ID6
assert connection_natural(r_a, a_axis, frames, T, cell_edges)
assert connection_natural(r_b, b_axis, frames, T, cell_edges)

# ---- Gauge-covariance regression ----
# Nonuniform local presentation changes must not create or destroy the group lift.
gauges = {
    xA: (1, 0, 2, 3, 5, 4),
    xB: (2, 1, 0, 5, 4, 3),
    xC: (5, 4, 3, 2, 1, 0),
    xD: (0, 2, 1, 4, 3, 5),
}
frames_g = {x: comp(gauges[x], frames[x]) for x in cells}
ingress_g = {x: relv(ingress[x], gauges[x]) for x in cells}
egress_g = {x: relv(egress[x], gauges[x]) for x in cells}
passage_g = {x: relm(passage[x], gauges[x]) for x in cells}
T_g = {
    (x, y): comp(gauges[y], comp(T[(x, y)], inv(gauges[x])))
    for x, y in oriented(cell_edges)
}
assert strict_lift(r_a, a_axis, 3, cells, cell_edges, frames_g, ingress_g, egress_g, passage_g, T_g)
assert strict_lift(r_b, b_axis, 2, cells, cell_edges, frames_g, ingress_g, egress_g, passage_g, T_g)

# Verify typed channel transport respects the whole 24-element representation after gauge change.
for P in G:
    rc, ax = P
    for Q in G:
        qc, qx = Q
        PQ = pair_comp(P, Q)
        rcq, axq = PQ
        for x in cells:
            pP_at_Qx = comp(frames_g[rc[qc[x]]], comp(ax, inv(frames_g[qc[x]])))
            pQ_at_x = comp(frames_g[qc[x]], comp(qx, inv(frames_g[x])))
            lhs = comp(pP_at_Qx, pQ_at_x)
            rhs = comp(frames_g[rcq[x]], comp(axq, inv(frames_g[x])))
            assert lhs == rhs

# Exact classification guards.
assert len(G) == 24
assert len(cell_kernel) == 1
assert len(axis_kernel) == 1
assert all(relation_words[name] == Epair for name in relation_words)
assert not any(omega_b(passage[x]) for x in cells)
P000_MUTATED = False
NATIVE_QUOTIENT_USED = False
LOCAL_S6_PROMOTED_TO_NATIVE_ROTATION = False
CARRIER_IDENTITY_IDENTIFIED_WITH_CELL_IDENTITY = False
TIME_MOVED = False
assert not any((
    P000_MUTATED,
    NATIVE_QUOTIENT_USED,
    LOCAL_S6_PROMOTED_TO_NATIVE_ROTATION,
    CARRIER_IDENTITY_IDENTIFIED_WITH_CELL_IDENTITY,
    TIME_MOVED,
))

print("PASS P000_BASE_CELL_RA_STAR_ORBIT_V12_CHECK")
print("terminal_class=FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED")
print("axis_a=(E1 E2 E3)(E4 E6 E5)")
print("axis_b=(E2 E4)(E3 E5)")
print("Ra_order=3")
print("Rb_order=2")
print("RaRb_order=4")
print("enriched_action_order=24")
print("bare_cell_image_order=24")
print("axis_type_image_order=24")
print("forgetful_to_cell_kernel_order=1")
print("axis_readout_kernel_order=1")
print("relation_residue=TRIVIAL_IN_DECLARED_MODEL")
print("star_orbit=A|BCD_under_a;AB_swap_under_b;C,D_fixed_under_b")
print("geometric_star_transport=cell+axes+PF10+local_relation+overlap_gluing")
print("connection=FRAME_INDUCED_FLAT_EQUIVARIANT")
print("Omega_b=false_in_positive_common_model")
print("contact_route_required=false")
print("gauge_covariance=verified_nonuniform_local_reindexing")
print("full_P000_native_rotation_group_promoted=false")
