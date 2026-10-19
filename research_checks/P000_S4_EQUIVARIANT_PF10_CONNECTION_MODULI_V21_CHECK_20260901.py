from __future__ import annotations
import itertools
from collections import Counter

V = ("A", "B", "C", "D")
EDGES = (("A","B"), ("A","C"), ("A","D"), ("B","C"), ("B","D"), ("C","D"))
ENAME = ("E1","E2","E3","E4","E5","E6")
EDGE_IDX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
ID6 = tuple(range(6))

def vperm(images):
    return dict(zip(V, images))

def compose_v(p, q):
    return {x: p[q[x]] for x in V}

def eperm(p):
    return tuple(EDGE_IDX[tuple(sorted((p[u], p[v])))] for u, v in EDGES)

def comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def conj(p, h):
    return comp(comp(p, h), inv(p))

def push_vec(act, vec):
    out = [None] * len(vec)
    for i, value in enumerate(vec):
        out[act[i]] = value
    return tuple(out)

def push_mat(act, mat):
    out = [[None] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            out[act[i]][act[j]] = mat[i][j]
    return tuple(tuple(row) for row in out)

def swap6(i, j):
    p = list(ID6)
    p[i], p[j] = p[j], p[i]
    return tuple(p)

def pindex(target):
    for i, p in enumerate(S4):
        if all(p[k] == value for k, value in target.items()):
            return i
    raise AssertionError(target)

def orbit_partition(points, acts, action):
    unseen = set(points)
    parts = []
    while unseen:
        seed = min(unseen)
        orb = {action(g, seed) for g in acts}
        changed = True
        while changed:
            changed = False
            for x in tuple(orb):
                for g in acts:
                    y = action(g, x)
                    if y not in orb:
                        orb.add(y)
                        changed = True
        parts.append(tuple(sorted(orb)))
        unseen -= orb
    return tuple(sorted(parts))

def subgroup_closure(gens):
    out = {ID6}
    front = [ID6]
    gens = tuple(gens)
    while front:
        x = front.pop()
        for g in gens:
            for y in (comp(g, x), comp(x, g), comp(inv(g), x)):
                if y not in out:
                    out.add(y)
                    front.append(y)
    return out

def perm_cycles(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = p[j]
        if len(cyc) > 1:
            out.append(tuple(cyc))
    return tuple(out)

def cycle_type(p):
    moving = [len(c) for c in perm_cycles(p)]
    fixed = len(p) - sum(moving)
    return tuple(sorted(moving + [1] * fixed, reverse=True))

def conn_nat(T, pidx):
    pv, pe = S4[pidx], EA[pidx]
    return all(T[(pv[x], pv[y])] == conj(pe, T[(x, y)]) for x, y in ORIENTED)

def inverse_consistent(T):
    return all(T[(y, x)] == inv(T[(x, y)]) for x, y in ORIENTED)

def path_transport(T, path):
    r = ID6
    for x, y in zip(path, path[1:]):
        r = comp(T[(x, y)], r)
    return r

S4 = [vperm(images) for images in itertools.permutations(V)]
EA = [eperm(p) for p in S4]
S6 = list(itertools.permutations(range(6)))
ORIENTED = [(x, y) for x in V for y in V if x != y]

# ---------------------------------------------------------------------------
# 1. Frozen carrier and PF10 orbit parameterization
# ---------------------------------------------------------------------------
assert len(S4) == 24
assert len(set(EA)) == 24

a_idx = pindex({"A":"A","B":"C","C":"D","D":"B"})   # (BCD)
b_idx = pindex({"A":"B","B":"A","C":"C","D":"D"})   # (AB)
aE, bE = EA[a_idx], EA[b_idx]
assert len(subgroup_closure((aE, bE))) == 24

H_A_idx = [i for i, p in enumerate(S4) if p["A"] == "A"]
H_A = [EA[i] for i in H_A_idx]
full_vector_orbits = orbit_partition(range(6), EA, lambda g, i: g[i])
full_pair_orbits = orbit_partition([(i,j) for i in range(6) for j in range(6)], EA, lambda g, ij: (g[ij[0]], g[ij[1]]))
base_vector_orbits = orbit_partition(range(6), H_A, lambda g, i: g[i])
base_pair_orbits = orbit_partition([(i,j) for i in range(6) for j in range(6)], H_A, lambda g, ij: (g[ij[0]], g[ij[1]]))

assert len(full_vector_orbits) == 1
assert len(full_pair_orbits) == 3
assert len(base_vector_orbits) == 2
assert len(base_pair_orbits) == 8
assert set(base_vector_orbits) == {tuple(sorted((0,1,2))), tuple(sorted((3,4,5)))}

# Symbolic 12-parameter base profile: 2 I + 2 O + 8 M.
I_A = tuple(next(f"I{o}" for o, orb in enumerate(base_vector_orbits) if i in orb) for i in range(6))
O_A = tuple(next(f"O{o}" for o, orb in enumerate(base_vector_orbits) if i in orb) for i in range(6))
M_A = tuple(tuple(next(f"M{o}" for o, orb in enumerate(base_pair_orbits) if (i,j) in orb) for j in range(6)) for i in range(6))
assert all(push_vec(h, I_A) == I_A for h in H_A)
assert all(push_vec(h, O_A) == O_A for h in H_A)
assert all(push_mat(h, M_A) == M_A for h in H_A)

def reconstruct_pf(base):
    I0, O0, M0 = base
    out = {}
    for x in V:
        reps = [i for i, p in enumerate(S4) if p["A"] == x]
        candidates = {(push_vec(EA[i], I0), push_vec(EA[i], O0), push_mat(EA[i], M0)) for i in reps}
        assert len(candidates) == 1
        out[x] = next(iter(candidates))
    return out

PF_SYMBOLIC = reconstruct_pf((I_A, O_A, M_A))
assert PF_SYMBOLIC["A"] == (I_A, O_A, M_A)
for gi, g in enumerate(S4):
    e = EA[gi]
    for x in V:
        lhs = PF_SYMBOLIC[g[x]]
        rhs = (push_vec(e, PF_SYMBOLIC[x][0]), push_vec(e, PF_SYMBOLIC[x][1]), push_mat(e, PF_SYMBOLIC[x][2]))
        assert lhs == rhs

# Explicit raw Cell-to-Cell nonconstant equivariant PF10 family.
def star_vec(x):
    return tuple(1 if x in edge else 0 for edge in EDGES)
def comp_vec(v):
    return tuple(1-z for z in v)
IDMAT = tuple(tuple(1 if i == j else 0 for j in range(6)) for i in range(6))
PF_WIT = {x: (star_vec(x), comp_vec(star_vec(x)), IDMAT) for x in V}
assert len({PF_WIT[x][0] for x in V}) == 4
for gi, g in enumerate(S4):
    e = EA[gi]
    for x in V:
        I, O, M = PF_WIT[x]
        assert PF_WIT[g[x]] == (push_vec(e, I), push_vec(e, O), push_mat(e, M))

# ---------------------------------------------------------------------------
# 2. Exact connection seed classification in typed value group Sym(E)=S6
# ---------------------------------------------------------------------------
k_idx = pindex({"A":"A","B":"B","C":"D","D":"C"})    # (CD), oriented-edge stabilizer
kappa = EA[k_idx]                                      # (E2 E3)(E4 E5)
lam = bE                                                # (E2 E4)(E3 E5)
assert comp(kappa, lam) == comp(lam, kappa)

centralizer = [t for t in S6 if comp(t, kappa) == comp(kappa, t)]
assert len(centralizer) == 16
centralizer_involutions = [s for s in centralizer if comp(s, s) == ID6]
assert len(centralizer_involutions) == 12

Z = [t for t in S6 if comp(t, kappa) == comp(kappa, t) and conj(lam, t) == inv(t)]
assert len(Z) == 12
# Twisted-involution theorem: t <-> s=lambda*t gives exactly involutions in C_S6(kappa).
assert {comp(lam, t) for t in Z} == set(centralizer_involutions)

REP = {}
for x, y in ORIENTED:
    REP[(x,y)] = next(i for i, p in enumerate(S4) if p["A"] == x and p["B"] == y)

def conn_from_seed(t):
    return {(x,y): conj(EA[REP[(x,y)]], t) for x,y in ORIENTED}

CONNS = [conn_from_seed(t) for t in Z]
for T in CONNS:
    assert inverse_consistent(T)
    assert all(conn_nat(T, gi) for gi in range(24))

assert sum(t == ID6 for t in Z) == 1
assert sum(t != ID6 for t in Z) == 11

# K4 rank-3 triangle cycle basis.
CYCLE_BASIS = [
    ("A","B","C","A"),
    ("A","B","D","A"),
    ("A","C","D","A"),
]
HOLS = [tuple(path_transport(T, c) for c in CYCLE_BASIS) for T in CONNS]
flat_raw = [i for i, hs in enumerate(HOLS) if all(h == ID6 for h in hs)]
assert flat_raw == [0, 5]
assert len(flat_raw) == 2
assert len(Z) - len(flat_raw) == 10

# Verify holonomy S4 conjugacy law on every triangle and every structural permutation.
TRIANGLES = []
for base in V:
    others = [x for x in V if x != base]
    for y,z in itertools.combinations(others, 2):
        TRIANGLES.append((base,y,z,base))
for T in CONNS:
    for gi, g in enumerate(S4):
        e = EA[gi]
        for cyc in TRIANGLES:
            moved = tuple(g[x] for x in cyc)
            assert path_transport(T, moved) == conj(e, path_transport(T, cyc))

# ---------------------------------------------------------------------------
# 3. Accepted Gen10 local-S6 gauge quotient
# ---------------------------------------------------------------------------
TREE = (("A","B"), ("A","C"), ("A","D"))
NONTREE = (("B","C"), ("B","D"), ("C","D"))

def tree_gauge(T, root_g=ID6):
    gauges = {"A": root_g}
    for y in ("B","C","D"):
        gauges[y] = comp(root_g, inv(T[("A", y)]))
    Tg = {(x,y): comp(comp(gauges[y], T[(x,y)]), inv(gauges[x])) for x,y in ORIENTED}
    assert all(Tg[e] == ID6 for e in TREE)
    return Tg, gauges

CANON = []
for T in CONNS:
    Tg, _ = tree_gauge(T)
    CANON.append(tuple(Tg[e] for e in NONTREE))

def simultaneous_conjugate(tr1, tr2):
    return any(all(conj(g, a) == b for a,b in zip(tr1,tr2)) for g in S6)

classes = []
unused = set(range(len(Z)))
while unused:
    i = min(unused)
    block = sorted(j for j in unused if simultaneous_conjugate(CANON[i], CANON[j]))
    for j in block:
        unused.remove(j)
    classes.append(block)

assert classes == [[0,5], [1], [2], [3,4], [6,11], [7], [8], [9,10]]
assert len(classes) == 8
flat_gauge_classes = sum(any(i in flat_raw for i in block) for block in classes)
assert flat_gauge_classes == 1
assert len(classes) - flat_gauge_classes == 7

# Exact holonomy fingerprints for gauge-class representatives.
def holonomy_group_size(hs):
    return len(subgroup_closure(hs))

class_reps = [block[0] for block in classes]
fingerprints = [(cycle_type(HOLS[i][0]), holonomy_group_size(HOLS[i])) for i in class_reps]
assert fingerprints == [
    ((1,1,1,1,1,1), 1),
    ((4,2), 24),
    ((2,2,1,1), 6),
    ((2,1,1,1,1), 6),
    ((2,2,2), 2),
    ((2,2,2), 6),
    ((4,1,1), 24),
    ((5,1), 60),
]
# S4 symmetry forces the three basis triangles into one conjugacy type per class.
for i in class_reps:
    assert len({cycle_type(h) for h in HOLS[i]}) == 1

# ---------------------------------------------------------------------------
# 4. Same-model nonconstant PF10 + Gen18 nonflat connection witness
# ---------------------------------------------------------------------------
t_gen18 = swap6(0, 5)  # seed on AB = (E1 E6)
gen18_index = Z.index(t_gen18)
assert gen18_index == 6
T_COMMON = CONNS[gen18_index]

opp = {}
for i, (u,v) in enumerate(EDGES):
    rest = [x for x in V if x not in (u,v)]
    opp[i] = EDGE_IDX[tuple(sorted(rest))]
for x,y in ORIENTED:
    i = EDGE_IDX[tuple(sorted((x,y)))]
    assert T_COMMON[(x,y)] == swap6(i, opp[i])

assert any(h != ID6 for h in HOLS[gen18_index])
assert all(conn_nat(T_COMMON, gi) for gi in range(24))
assert len({PF_WIT[x][0] for x in V}) > 1

# Frozen visible common model uses the faithful carrier S4 itself as G0; no kernel is
# quotiented or ignored, so full lift fibers of a,b are singletons in this witness.
assert len(subgroup_closure((aE,bE))) == 24

def perm_power(p, n):
    r = ID6
    for _ in range(n):
        r = comp(p, r)
    return r

abE = comp(aE, bE)
assert perm_power(aE, 3) == ID6
assert perm_power(bE, 2) == ID6
assert perm_power(abE, 4) == ID6

# The enriched data are fixed by the generating structural action, hence by the relations.
for gi in (a_idx, b_idx):
    assert all(conn_nat(T_COMMON, gi) for _ in (0,))
    g = S4[gi]
    e = EA[gi]
    for x in V:
        I,O,M = PF_WIT[x]
        assert PF_WIT[g[x]] == (push_vec(e,I), push_vec(e,O), push_mat(e,M))

# P000/Gen17/Gen18 guards: checked as frozen scope declarations, not mutated axioms.
NO_KERNEL_QUOTIENT = True
TIME_FIXED = True
CARRIER_S4_IS_COMPLETE_NATIVE_P000_ROTATION_GROUP = False
LOCAL_S6_IS_NATIVE_SPATIAL_ROTATION_GROUP = False
assert NO_KERNEL_QUOTIENT and TIME_FIXED
assert not CARRIER_S4_IS_COMPLETE_NATIVE_P000_ROTATION_GROUP
assert not LOCAL_S6_IS_NATIVE_SPATIAL_ROTATION_GROUP

print("PASS P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V21_CHECK")
print("carrier_s4_order=24")
print("full_local_vector_orbits=1")
print("full_local_ordered_pair_orbits=3")
print("base_cell_stabilizer_vector_orbits=2")
print("base_cell_stabilizer_ordered_pair_orbits=8")
print("pf10_raw_parameter_slots=12")
print("pf10_nonconstant_equivariant_witness=true")
print("connection_value_group=S6_order_720")
print("oriented_edge_stabilizer_centralizer_order=16")
print("equivariant_inverse_consistent_connection_seeds=12")
print("raw_identity_connections=1")
print("raw_nonidentity_connections=11")
print("raw_flat_connections=2")
print("raw_nonflat_connections=10")
print("gauge_classes=8")
print("flat_gauge_classes=1")
print("nonflat_gauge_classes=7")
print("holonomy_fingerprints=" + repr(fingerprints))
print("gen18_edge_to_opposite_nonflat_regression=true")
print("common_nonconstant_pf10_nonflat_connection_model=true")
print("enriched_relations_a3_b2_ab4=true")
print("terminal_class=NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED")
