#!/usr/bin/env python3
from itertools import combinations, permutations, product

V = ("A", "B", "C", "D")
E = tuple("".join(p) for p in combinations(V, 2))
STARS = {v: frozenset(e for e in E if v in e) for v in V}

# Frozen carrier relabeling:
# L_AB=L1, L_AC=L3, L_AD=L6, L_BC=L5, L_BD=L4, L_CD=L2.
BETA = {1: "AB", 2: "AC", 3: "AD", 4: "BC", 5: "BD", 6: "CD"}
I_A = frozenset((1, 2, 3))
I_B = frozenset((4, 5, 6))
J = {
    "A": frozenset((1, 2, 3)),
    "B": frozenset((1, 4, 5)),
    "C": frozenset((2, 4, 6)),
    "D": frozenset((3, 5, 6)),
}

# Convenient oriented representatives of the six frozen unoriented FCC lines.
R = {
    "AB": (1, 1, 0),
    "AC": (1, 0, 1),
    "AD": (0, 1, -1),
    "BC": (0, 1, 1),
    "BD": (1, 0, -1),
    "CD": (1, -1, 0),
}

# One local zero-sum 120-degree orientation section on each carrier star.
S = {
    "A": {"AB": -1, "AC": 1, "AD": 1},
    "B": {"AB": 1, "BC": -1, "BD": -1},
    "C": {"AC": -1, "BC": 1, "CD": 1},
    "D": {"AD": 1, "BD": -1, "CD": 1},
}


def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))


def scale(a, v):
    return tuple(a * x for x in v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def canon_edge(a, b):
    return "".join(sorted((a, b)))


def induced_edge_perm(p):
    d = dict(zip(V, p))
    return {e: canon_edge(d[e[0]], d[e[1]]) for e in E}


def atlas_from_beta(native_atlas):
    return {k: frozenset(BETA[i] for i in t) for k, t in native_atlas.items()}


# 1. K4 star incidence.
assert len(E) == 6
assert all(len(STARS[v]) == 3 for v in V)
assert all(len(STARS[a] & STARS[b]) == 1 for a, b in combinations(V, 2))
assert all(sum(e in STARS[v] for v in V) == 2 for e in E)
assert all((frozenset(E) - STARS[v]) not in set(STARS.values()) for v in V)

# 2. The chosen native star atlas is exactly the FCC star atlas under beta.
assert atlas_from_beta(J) == STARS
assert frozenset(BETA[i] for i in I_A) == STARS["A"]
COMP_A = frozenset(BETA[i] for i in I_B)
assert COMP_A == frozenset(("BC", "BD", "CD"))
assert COMP_A == frozenset(E) - STARS["A"]
assert COMP_A not in set(STARS.values())

# Count K4-star designs on six labeled native axes.  This is the finite
# symmetry ambiguity that P000's bare six labels do not remove.
U6 = set(range(1, 7))
trips = list(combinations(range(1, 7), 3))
designs = set()
for four in combinations(trips, 4):
    blocks = [frozenset(t) for t in four]
    if set().union(*blocks) != U6:
        continue
    if not all(sum(i in b for b in blocks) == 2 for i in U6):
        continue
    if not all(len(a & b) == 1 for a, b in combinations(blocks, 2)):
        continue
    designs.add(tuple(sorted(tuple(sorted(b)) for b in blocks)))
assert len(designs) == 30
assert sum(tuple(sorted(I_A)) in d for d in designs) == 6

# 3. Carrier S4 action preserves the star family.  Consequently no physical
# carrier-atlas rotation sends a 120-degree star to its complementary triangle.
seen = set()
for p in permutations(V):
    ep = induced_edge_perm(p)
    image_a = frozenset(ep[e] for e in STARS["A"])
    assert image_a in set(STARS.values())
    assert image_a != COMP_A
    seen.add(tuple(ep[e] for e in E))
assert len(seen) == 24

# Therefore the minimal clone-product rho: I_A <-> I_B cannot intertwine with
# any carrier S4 atlas rotation once I_A is read as S_A.  This is pure incidence.

# 4. Each local chart orientation is an exact 120-degree zero-sum triple and is
# unique up to one common sign.
for c, star in STARS.items():
    local = []
    es = tuple(sorted(star))
    for signs in product((-1, 1), repeat=3):
        vs = [scale(signs[k], R[e]) for k, e in enumerate(es)]
        if add(*vs) == (0, 0, 0) and all(
            dot(vs[i], vs[j]) == -1 for i, j in combinations(range(3), 2)
        ):
            local.append(dict(zip(es, signs)))
    assert len(local) == 2
    assert any(all(x[e] == S[c][e] for e in star) for x in local)

# 5. No single global signed representative of the six line families makes all
# four star charts simultaneously zero-sum 120-degree triples.
global_good = []
for signs in product((-1, 1), repeat=6):
    g = dict(zip(E, signs))
    ok = True
    for star in STARS.values():
        es = tuple(sorted(star))
        vs = [scale(g[e], R[e]) for e in es]
        if not (
            add(*vs) == (0, 0, 0)
            and all(dot(vs[i], vs[j]) == -1 for i, j in combinations(range(3), 2))
        ):
            ok = False
            break
    if ok:
        global_good.append(g)
assert global_good == []

# 6. Z2 chart-transition holonomy.  Local common-sign gauge changes cannot
# remove it: every triangular chart loop has holonomy -1.
Q = {}
for a, b in combinations(V, 2):
    e = next(iter(STARS[a] & STARS[b]))
    Q[(a, b)] = Q[(b, a)] = S[b][e] * S[a][e]
tri_hol = {}
for a, b, c in combinations(V, 3):
    h = Q[(a, b)] * Q[(b, c)] * Q[(c, a)]
    tri_hol[a + b + c] = h
assert set(tri_hol.values()) == {-1}

for flips in product((-1, 1), repeat=4):
    t = dict(zip(V, flips))
    qg = {
        (a, b): t[b] * Q[(a, b)] * t[a]
        for a in V
        for b in V
        if a != b
    }
    for a, b, c in combinations(V, 3):
        assert qg[(a, b)] * qg[(b, c)] * qg[(c, a)] == -1

# 7. HCP regression, reusing the exact integer shell coordinates from the
# accepted first-shell checker.  FCC has six antipodal pairs; HCP has only three.
R0 = [
    (2, 0, 0),
    (1, 3, 0),
    (-1, 3, 0),
    (-2, 0, 0),
    (-1, -3, 0),
    (1, -3, 0),
]
U = [(1, 1, 1), (-1, 1, 1), (0, -2, 1)]
FCC = R0 + U + [(0, 2, -1), (-1, -1, -1), (1, -1, -1)]
HCP = R0 + U + [(1, 1, -1), (-1, 1, -1), (0, -2, -1)]


def antipodal_pairs(points):
    pts = set(points)
    out = set()
    for p in points:
        n = tuple(-x for x in p)
        if n in pts:
            out.add(tuple(sorted((p, n))))
    return out


assert len(FCC) == 12 and len(HCP) == 12
assert len(antipodal_pairs(FCC)) == 6
assert len(antipodal_pairs(HCP)) == 3

print("PASS")
print("native_beta=", BETA)
print("native_factor_A_to_carrier=", sorted(STARS["A"]))
print("native_factor_B_to_carrier_complement=", sorted(COMP_A))
print("k4_star_designs_on_six_labeled_axes=", len(designs))
print("designs_containing_visible_I_A=", sum(tuple(sorted(I_A)) in d for d in designs))
print("carrier_S4_edge_actions=", len(seen))
print("global_120_orientation_sections=", len(global_good))
print("triangle_Z2_holonomy=", tri_hol)
print("FCC_antipodal_pairs=", len(antipodal_pairs(FCC)))
print("HCP_antipodal_pairs=", len(antipodal_pairs(HCP)))
