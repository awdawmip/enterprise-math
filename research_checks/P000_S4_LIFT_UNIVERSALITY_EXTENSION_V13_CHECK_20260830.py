#!/usr/bin/env python3
"""Exact standard-library checker for P000 S4 lift universality/extension V13."""

from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product

TERMINAL_CLASS = (
    "NONTRIVIAL_FULL_CELL_RELATION_EXTENSION_OF_S4_EXACTLY_CLASSIFIED"
    " / BARE_P000_UNIVERSAL_OR_CANONICAL_S4_LIFT_EXACTLY_OBSTRUCTED_WITH_MODEL_CLASS_BOUNDARY"
)

# ---------- finite permutations ----------
def pcomp(p, q):
    """p*q = p o q: apply q first."""
    return tuple(p[q[i]] for i in range(len(p)))

def pinv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def ppow(p, n):
    out = tuple(range(len(p)))
    for _ in range(n):
        out = pcomp(p, out)
    return out

def cycle(n, entries):
    p = list(range(n))
    for i, x in enumerate(entries):
        p[x] = entries[(i + 1) % len(entries)]
    return tuple(p)

def generated_perm_group(gens):
    ident = tuple(range(len(gens[0])))
    seen = {ident}
    queue = deque([ident])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = pcomp(g, x)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen

ID4 = tuple(range(4))
A4 = cycle(4, (1, 2, 3))      # (BCD), A fixed
B4 = cycle(4, (0, 1))         # (AB)
AB4 = pcomp(A4, B4)
S4 = generated_perm_group([A4, B4])
assert len(S4) == 24
assert ppow(A4, 3) == ID4
assert ppow(B4, 2) == ID4
assert ppow(AB4, 4) == ID4

# ---------- Gen12 tagged-sort regression ----------
CARRIER_VERTICES = tuple(("CarrierVertex", x) for x in "ABCD")
GEN12_NATIVE_CELLS = tuple(("NativeCell", "Gen12", x) for x in "ABCD")
assert set(CARRIER_VERTICES).isdisjoint(GEN12_NATIVE_CELLS)

EDGE_LABEL = {
    frozenset((0, 1)): "E1",
    frozenset((0, 2)): "E2",
    frozenset((0, 3)): "E3",
    frozenset((1, 2)): "E4",
    frozenset((1, 3)): "E5",
    frozenset((2, 3)): "E6",
}
EDGE_ORDER = ("E1", "E2", "E3", "E4", "E5", "E6")
EDGE_INDEX = {e: i for i, e in enumerate(EDGE_ORDER)}

def edge_action(sigma):
    out = [None] * 6
    for pair, label in EDGE_LABEL.items():
        i, j = tuple(pair)
        image_label = EDGE_LABEL[frozenset((sigma[i], sigma[j]))]
        out[EDGE_INDEX[label]] = EDGE_INDEX[image_label]
    return tuple(out)

AXIS_A = edge_action(A4)
AXIS_B = edge_action(B4)
EXPECTED_AXIS_A = cycle(6, (0, 1, 2))
EXPECTED_AXIS_A = pcomp(cycle(6, (3, 5, 4)), EXPECTED_AXIS_A)
EXPECTED_AXIS_B = pcomp(cycle(6, (1, 3)), cycle(6, (2, 4)))
assert AXIS_A == EXPECTED_AXIS_A
assert AXIS_B == EXPECTED_AXIS_B
AXIS_GROUP = generated_perm_group([AXIS_A, AXIS_B])
assert len(AXIS_GROUP) == 24
assert len({edge_action(g) for g in S4}) == 24
GEN12_KERNEL = [g for g in S4 if edge_action(g) == tuple(range(6))]
assert GEN12_KERNEL == [ID4]

# ---------- split nontrivial-kernel Full-Cell model: C2 wr S4 ----------
ZERO4 = (0, 0, 0, 0)
K4_BITS = tuple(product((0, 1), repeat=4))

def vadd(u, v):
    return tuple(x ^ y for x, y in zip(u, v))

def permute_bits(sigma, v):
    inv = pinv(sigma)
    return tuple(v[inv[i]] for i in range(4))

def wmul(x, y):
    u, sigma = x
    v, tau = y
    return (vadd(u, permute_bits(sigma, v)), pcomp(sigma, tau))

def winv(x):
    u, sigma = x
    sigma_inv = pinv(sigma)
    return (permute_bits(sigma_inv, u), sigma_inv)

def wpow(x, n):
    out = (ZERO4, ID4)
    for _ in range(n):
        out = wmul(x, out)
    return out

def wq(x):
    return x[1]

WREATH = tuple((v, s) for v in K4_BITS for s in S4)
WREATH_K = tuple((v, ID4) for v in K4_BITS)
assert len(WREATH) == 384
assert len(WREATH_K) == 16
assert len({wq(g) for g in WREATH}) == 24
for x in WREATH:
    for y in WREATH:
        assert wq(wmul(x, y)) == pcomp(wq(x), wq(y))

# Native semantic realization: four un-oriented 2-Cell fibers.
WREATH_CELLS = tuple(
    ("NativeCell", "Wreath", i, bit) for i in range(4) for bit in range(2)
)
assert set(CARRIER_VERTICES).isdisjoint(WREATH_CELLS)

def wreath_cell_action(g, cell):
    _, model, i, bit = cell
    assert model == "Wreath"
    v, sigma = g
    j = sigma[i]
    return ("NativeCell", "Wreath", j, bit ^ v[j])

def fiber_index(cell):
    return cell[2]

def native_adj_wreath(x, y):
    # Complete 4-partite K_{2,2,2,2}: the un-oriented fiber partition is native.
    return fiber_index(x) != fiber_index(y)

for g in WREATH:
    images = [wreath_cell_action(g, x) for x in WREATH_CELLS]
    assert len(set(images)) == 8
    for x, y in combinations(WREATH_CELLS, 2):
        assert native_adj_wreath(x, y) == native_adj_wreath(
            wreath_cell_action(g, x), wreath_cell_action(g, y)
        )

# Kernel is actual independent within-fiber Cell swapping, not an inert label.
for v in K4_BITS:
    g = (v, ID4)
    moved = sum(wreath_cell_action(g, x) != x for x in WREATH_CELLS)
    assert moved == 2 * sum(v)
    assert wq(g) == ID4

WA0 = (ZERO4, A4)
WB0 = (ZERO4, B4)
assert wpow(WA0, 3) == (ZERO4, ID4)
assert wpow(WB0, 2) == (ZERO4, ID4)
assert wpow(wmul(WA0, WB0), 4) == (ZERO4, ID4)

def generated_wreath_group(gens):
    ident = (ZERO4, ID4)
    seen = {ident}
    queue = deque([ident])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = wmul(g, x)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen

assert len(generated_wreath_group([WA0, WB0])) == 24

# Exhaust all 16*16 choices of generator lifts and freeze residue behavior.
residue_triples = Counter()
exact_section_pairs = []
for u in K4_BITS:
    for v in K4_BITS:
        A = (u, A4)
        B = (v, B4)
        za = wpow(A, 3)
        zb = wpow(B, 2)
        zab = wpow(wmul(A, B), 4)
        assert za in WREATH_K and zb in WREATH_K and zab in WREATH_K
        residue_triples[(za[0], zb[0], zab[0])] += 1
        if za[0] == ZERO4 and zb[0] == ZERO4 and zab[0] == ZERO4:
            H = generated_wreath_group([A, B])
            assert len(H) == 24 and len({wq(h) for h in H}) == 24
            exact_section_pairs.append((A, B))

assert len(residue_triples) == 16
assert len(exact_section_pairs) == 16
assert {t[0] for t in residue_triples} == {
    (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 1, 1), (1, 1, 1, 1)
}
assert {t[1] for t in residue_triples} == {
    (0, 0, 0, 0), (1, 1, 0, 0)
}
assert {t[2] for t in residue_triples} == {
    (0, 0, 0, 0), (1, 1, 1, 1)
}

def wconj(h, x):
    return wmul(wmul(h, x), winv(h))

def section_pair_conj(k, pair):
    kk = (k, ID4)
    return (wconj(kk, pair[0]), wconj(kk, pair[1]))

# All 16 homomorphic sections split into exactly two K-conjugacy orbits of size 8.
unseen = set(exact_section_pairs)
section_orbit_sizes = []
while unseen:
    seed = next(iter(unseen))
    orbit = {section_pair_conj(k, seed) for k in K4_BITS}
    orbit &= set(exact_section_pairs)
    section_orbit_sizes.append(len(orbit))
    unseen -= orbit
assert sorted(section_orbit_sizes) == [8, 8]

# Canonicality obstruction: a K-conjugation-invariant section would centralize K.
centralizer_K = []
for g in WREATH:
    if all(wmul(g, k) == wmul(k, g) for k in WREATH_K):
        centralizer_K.append(g)
assert set(centralizer_K) == set(WREATH_K)
assert {wq(g) for g in centralizer_K} == {ID4}
# Hence no section S4 -> WREATH can be fixed pointwise by all primitive-preserving K conjugations.

# ---------- nonsplit central semantic extension: GL(2,3) -> PGL(2,3) ~= S4 ----------
MOD = 3
MI = (1, 0, 0, 1)
MMINUS_I = (2, 0, 0, 2)

def mmul(A, B):
    return tuple(
        sum(A[2 * i + k] * B[2 * k + j] for k in range(2)) % MOD
        for i in range(2) for j in range(2)
    )

def mpow(A, n):
    out = MI
    for _ in range(n):
        out = mmul(A, out)
    return out

def mdet(A):
    return (A[0] * A[3] - A[1] * A[2]) % MOD

def mvec(A, v):
    return (
        (A[0] * v[0] + A[1] * v[1]) % MOD,
        (A[2] * v[0] + A[3] * v[1]) % MOD,
    )

GL23 = tuple(A for A in product(range(3), repeat=4) if mdet(A) != 0)
assert len(GL23) == 48

P1_REPS = ((1, 0), (0, 1), (1, 1), (1, 2))
P1_INDEX = {v: i for i, v in enumerate(P1_REPS)}

def line_canon(v):
    if v[0]:
        inv = 1 if v[0] == 1 else 2
        return (1, (v[1] * inv) % 3)
    return (0, 1)

def pgl_readout(A):
    return tuple(P1_INDEX[line_canon(mvec(A, v))] for v in P1_REPS)

PGL_IMAGE = {pgl_readout(A) for A in GL23}
assert PGL_IMAGE == set(S4)
GL_KERNEL = [A for A in GL23 if pgl_readout(A) == ID4]
assert set(GL_KERNEL) == {MI, MMINUS_I}

for X in GL23:
    for Y in GL23:
        assert pgl_readout(mmul(X, Y)) == pcomp(pgl_readout(X), pgl_readout(Y))

# Semantic hidden relation: V=F3^2 with addition, with four native Cell-line anchors.
V23 = tuple(product(range(3), repeat=2))
GL_CELLS = tuple(("NativeCellLine", i) for i in range(4))
GL_HIDDEN = tuple(("HiddenVector",) + v for v in V23)
assert set(CARRIER_VERTICES).isdisjoint(GL_CELLS)
assert set(CARRIER_VERTICES).isdisjoint(GL_HIDDEN)
assert set(GL_CELLS).isdisjoint(GL_HIDDEN)

def v23add(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)

def incidence(v, line_i):
    if v == (0, 0):
        return False
    return line_canon(v) == P1_REPS[line_i]

for A in GL23:
    # linear/addition relation preservation
    for x in V23:
        for y in V23:
            assert mvec(A, v23add(x, y)) == v23add(mvec(A, x), mvec(A, y))
    # projective Cell-line incidence preservation
    sigma = pgl_readout(A)
    for v in V23:
        for i in range(4):
            assert incidence(v, i) == incidence(mvec(A, v), sigma[i])

# -I is a genuine hidden-state symmetry: invisible to Cell-line/axis readout, nontrivial on V.
assert pgl_readout(MMINUS_I) == ID4
assert any(mvec(MMINUS_I, v) != v for v in V23)

GL_LIFTS_A = [A for A in GL23 if pgl_readout(A) == A4]
GL_LIFTS_B = [B for B in GL23 if pgl_readout(B) == B4]
assert len(GL_LIFTS_A) == len(GL_LIFTS_B) == 2

def generated_matrix_group(gens):
    seen = {MI}
    queue = deque([MI])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = mmul(g, x)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen

gl_residue_rows = []
for A in GL_LIFTS_A:
    for B in GL_LIFTS_B:
        za = mpow(A, 3)
        zb = mpow(B, 2)
        zab = mpow(mmul(A, B), 4)
        assert za in GL_KERNEL and zb in GL_KERNEL and zab in GL_KERNEL
        assert zb == MI
        assert zab == MMINUS_I       # invariant under all four lift choices
        H = generated_matrix_group([A, B])
        assert len(H) == 48
        gl_residue_rows.append((za, zb, zab))
assert len(gl_residue_rows) == 4
assert {row[0] for row in gl_residue_rows} == {MI, MMINUS_I}
assert {row[2] for row in gl_residue_rows} == {MMINUS_I}
# Since every possible A,B lift has (AB)^4=-I, no homomorphic S4 section exists.

# ---------- exact no-lift countermodel: native P4 adjacency ----------
P4_CELLS = tuple(("NativeCell", "P4", i) for i in range(4))
assert set(CARRIER_VERTICES).isdisjoint(P4_CELLS)
P4_EDGES = {frozenset((0, 1)), frozenset((1, 2)), frozenset((2, 3))}

def preserves_p4(sigma):
    image = {frozenset((sigma[i], sigma[j])) for i, j in (tuple(e) for e in P4_EDGES)}
    return image == P4_EDGES

P4_AUT = [p for p in permutations(range(4)) if preserves_p4(p)]
assert len(P4_AUT) == 2
assert A4 not in P4_AUT
assert B4 not in P4_AUT
# Uniform PF-10 and frame-induced identity transport can be chosen, so adjacency alone blocks the lift.

# ---------- structural classification assertions ----------
# Split iff a homomorphic section exists: witnessed by WREATH. Nonsplit: GL23.
# Non-surjective/no-generator-preimage: P4. Gen12 supplies K=1 split faithful regression.
assert len(GEN12_KERNEL) == 1
assert len(WREATH_K) == 16
assert len(GL_KERNEL) == 2
assert len(P4_AUT) < 24

print("PASS P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_CHECK")
print(f"terminal_class={TERMINAL_CLASS}")
print("gen12_split_faithful_K_order=1")
print("tagged_carrier_native_cell_disjoint=true")
print("frozen_axis_image_order=24")
print("wreath_group_order=384")
print("wreath_kernel_order=16")
print("wreath_axis_image_order=24")
print("wreath_generator_lift_pairs=256")
print(f"wreath_distinct_residue_triples={len(residue_triples)}")
print(f"wreath_exact_homomorphic_sections={len(exact_section_pairs)}")
print("wreath_section_K_conjugacy_orbits=2")
print("wreath_section_orbit_sizes=8,8")
print("wreath_centralizer_of_kernel_order=16")
print("wreath_canonical_section_fixed_by_kernel=false")
print("gl23_group_order=48")
print("gl23_kernel_order=2")
print("gl23_axis_image_order=24")
print("gl23_generator_lift_pairs=4")
print("gl23_all_product_relation_residue=-I")
print("gl23_homomorphic_section_exists=false")
print("p4_native_adjacency_aut_order=2")
print("p4_frozen_a_lift_exists=false")
print("universal_bare_p000_s4_lift_not_derivable=true")
print("full_native_rotation_group_promoted=false")
print("carrier_kernel_quotiented_to_manufacture_s4=false")
print("time_rotated=false")
