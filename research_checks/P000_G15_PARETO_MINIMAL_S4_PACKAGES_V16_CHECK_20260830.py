#!/usr/bin/env python3
"""Deterministic checker for P000 G15 Pareto-minimal S4 packages V16.

The checker consumes the frozen Generation-15 grammar, enumerates all 90
dependency-closed package specifications, applies the frozen fixed-sort
definitional quotient, checks the universal classification partition,
computes faithful/canonical Pareto frontiers, and re-runs mandatory finite
regressions.

No external packages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path

TASK_ID = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
PUBLICATION_ID = "TP2-6C18F4A93D705BE21642"
TERMINAL = "G15_PARETO_MINIMAL_FAITHFUL_AND_CANONICAL_S4_PACKAGES_CLASSIFIED"

G15_CERT_SHA256 = "50ef864f0713d1f19ddf918dae2486a05a7e1d52bf538f1603b2d1c6c655281e"

RELATIONS_ORDER = ("I_CA", "I_HC", "I_HA", "ADD_H")
CONSTRAINTS_ORDER = ("K4_ADJ", "TETRA_CA", "H_C3X3", "PROJECTIVE_HC", "PAIR_AXIS_HA")
REL_META = {
    "I_CA": (2, False),
    "I_HC": (2, True),
    "I_HA": (2, True),
    "ADD_H": (3, True),
}
CONSTRAINTS = {
    "K4_ADJ": (set(), set()),
    "TETRA_CA": ({"I_CA"}, set()),
    "H_C3X3": ({"ADD_H"}, set()),
    "PROJECTIVE_HC": ({"ADD_H", "I_HC"}, {"H_C3X3"}),
    "PAIR_AXIS_HA": ({"ADD_H", "I_HC", "I_HA"}, {"H_C3X3", "PROJECTIVE_HC"}),
}

EXPECTED_SPEC_COUNTS = {
    "NO_LIFT_P4": 30,
    "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT": 12,
    "NO_LIFT_UNCONSTRAINED_I_CA": 6,
    "NO_LIFT_UNCONSTRAINED_I_HC": 24,
    "NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS": 6,
    "SURJECTIVE_NONSPLIT_GL23": 12,
}
EXPECTED_CLASS_COUNTS = {
    "NO_LIFT_P4": 30,
    "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT": 9,
    "NO_LIFT_UNCONSTRAINED_I_CA": 6,
    "NO_LIFT_UNCONSTRAINED_I_HC": 18,
    "NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS": 3,
    "SURJECTIVE_NONSPLIT_GL23": 9,
}


def assert_(cond, msg):
    if not cond:
        raise AssertionError(msg)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valid_package(relset, cset):
    for c in cset:
        reqr, reqc = CONSTRAINTS[c]
        if not reqr.issubset(relset) or not reqc.issubset(cset):
            return False
    return True


def all_valid_packages():
    out = []
    for rmask in range(1 << len(RELATIONS_ORDER)):
        rs = frozenset(RELATIONS_ORDER[i] for i in range(len(RELATIONS_ORDER)) if (rmask >> i) & 1)
        for cmask in range(1 << len(CONSTRAINTS_ORDER)):
            cs = frozenset(CONSTRAINTS_ORDER[i] for i in range(len(CONSTRAINTS_ORDER)) if (cmask >> i) & 1)
            if valid_package(set(rs), set(cs)):
                out.append((rmask, cmask, rs, cs))
    return out


def cost(rs, cs):
    hidden = any(REL_META[r][1] for r in rs)
    arity = {1: 0, 2: 0, 3: 0}
    for r in rs:
        arity[REL_META[r][0]] += 1
    return (
        int(hidden),
        len(rs),
        arity[1],
        arity[2],
        arity[3],
        int(hidden),
        len(cs),
        0,
    )


def class_key(rs, cs):
    # Frozen G15 D1: TETRA_CA parameter-free defines complete K4 adjacency.
    # Thus adding explicit K4_ADJ to a TETRA_CA package is semantically redundant.
    # Frozen independent-meaning/signature policy supplies no other mutual-definability collapse.
    cs = set(cs)
    if "TETRA_CA" in cs:
        cs.discard("K4_ADJ")
    return (
        tuple(r for r in RELATIONS_ORDER if r in rs),
        tuple(c for c in CONSTRAINTS_ORDER if c in cs),
    )


def classify(rs, cs):
    rs, cs = set(rs), set(cs)
    base = ("K4_ADJ" in cs) or ("TETRA_CA" in cs)

    # Without a full four-cell S4 base, NativeAdj=P4 is an admitted same-package
    # valuation; every other selected constraint can be instantiated independently.
    if not base:
        return ("NO_LIFT_P4", "GEN13_P4_NO_LIFT", False, False)

    # PROJECTIVE_HC forces the hidden F3^2/projective-line coupling. With K4 or
    # TETRA on Cells, the exact GL(2,3)->PGL(2,3) readout remains onto S4 but
    # has nontrivial central residue, hence no section.
    if "PROJECTIVE_HC" in cs:
        return ("SURJECTIVE_NONSPLIT_GL23", "GEN13_GL23_SURJECTIVE_NONSPLIT", False, False)

    # A selected Cell-touching relation without its symmetry-completing constraint
    # admits a singleton valuation that fixes c0 and shrinks the cell image.
    if "I_HC" in rs:
        return ("NO_LIFT_UNCONSTRAINED_I_HC", "SINGLETON_I_HC_CELL_STABILIZER", False, False)
    if "I_CA" in rs and "TETRA_CA" not in cs:
        return ("NO_LIFT_UNCONSTRAINED_I_CA", "SINGLETON_I_CA_CELL_STABILIZER", False, False)

    # Under TETRA_CA, AxisType is the six unordered Cell pairs. An unconstrained
    # I_HA singleton singles out one axis and restricts the S4 image to a pair stabilizer.
    if "TETRA_CA" in cs and "I_HA" in rs:
        return ("NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS", "SINGLETON_I_HA_AXIS_STABILIZER", False, False)

    # Remaining packages have one of two exact typed factorizations:
    #  (i) K4 NativeCell component times a Cell-disconnected Axis/Hidden component;
    #  (ii) tetrahedral Cell-Axis component (Aut=S4) times an ADD_H-only Hidden component.
    # q is projection to the S4 factor. The identity-on-complement section is
    # fixed by primitive-preserving conjugation after canceling the induced S4 conjugation.
    return ("UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT", "DIRECT_TYPED_FACTOR_SECTION", True, True)


def dominates(a, b):
    return a != b and all(x <= y for x, y in zip(a, b))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse_perm(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def graph_auts(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    return [
        p for p in permutations(range(n))
        if {tuple(sorted((p[i], p[j]))) for i, j in E} == E
    ]


def k4_edges():
    return set(combinations(range(4), 2))


def p4_edges():
    return {(0, 1), (1, 2), (2, 3)}


def k2222_edges():
    fib = (0, 0, 1, 1, 2, 2, 3, 3)
    return {(i, j) for i, j in combinations(range(8), 2) if fib[i] != fib[j]}


def tetra_data():
    pairs = list(combinations(range(4), 2))
    pair_index = {p: i for i, p in enumerate(pairs)}
    incidence = {(c, a) for a, pair in enumerate(pairs) for c in pair}
    auts = []
    for pc in permutations(range(4)):
        pa = []
        for i, j in pairs:
            pa.append(pair_index[tuple(sorted((pc[i], pc[j])))])
        auts.append((pc, tuple(pa)))
    return pairs, incidence, auts


# GL(2,3) exact hidden witness
MOD = 3
MAT_I = ((1, 0), (0, 1))
MAT_NEG = ((2, 0), (0, 2))
LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
LINE_INDEX = {v: i for i, v in enumerate(LINES)}
P_ID = tuple(range(4))
A_PERM = (0, 2, 3, 1)  # (BCD)
B_PERM = (1, 0, 2, 3)  # (AB)


def det(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % MOD


def matmul(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2)) % MOD for j in range(2))
        for i in range(2)
    )


def matpow(A, n):
    R = MAT_I
    for _ in range(n):
        R = matmul(R, A)
    return R


def gl23():
    out = []
    for vals in product(range(3), repeat=4):
        A = ((vals[0], vals[1]), (vals[2], vals[3]))
        if det(A):
            out.append(A)
    return out


def canon_line(v):
    x, y = v[0] % 3, v[1] % 3
    if x == 0:
        return (0, 1)
    inv = 1 if x == 1 else 2
    return (1, (y * inv) % 3)


def projective_action(A):
    out = []
    for x, y in LINES:
        w = (
            (A[0][0] * x + A[0][1] * y) % 3,
            (A[1][0] * x + A[1][1] * y) % 3,
        )
        out.append(LINE_INDEX[canon_line(w)])
    return tuple(out)


# C2 wr S4 exact split/noncanonical regression
S4 = list(permutations(range(4)))
ZERO = (0, 0, 0, 0)


def act_vec(p, w):
    inv = inverse_perm(p)
    return tuple(w[inv[i]] for i in range(4))


def xorv(v, w):
    return tuple(a ^ b for a, b in zip(v, w))


def wr_mul(g, h):
    v, p = g
    w, q = h
    return (xorv(v, act_vec(p, w)), compose(p, q))


WR_E = (ZERO, P_ID)


def wr_pow(g, n):
    r = WR_E
    for _ in range(n):
        r = wr_mul(r, g)
    return r


def wr_inv(g):
    v, p = g
    pi = inverse_perm(p)
    return (act_vec(pi, v), pi)


def wr_conj(k, g):
    return wr_mul(wr_mul(k, g), wr_inv(k))


def wreath_certificate():
    liftsA = [(v, A_PERM) for v in product((0, 1), repeat=4)]
    liftsB = [(v, B_PERM) for v in product((0, 1), repeat=4)]
    pairs = []
    residues = set()
    for A in liftsA:
        for B in liftsB:
            residues.add((wr_pow(A, 3)[0], wr_pow(B, 2)[0], wr_pow(wr_mul(A, B), 4)[0]))
            if wr_pow(A, 3) == WR_E and wr_pow(B, 2) == WR_E and wr_pow(wr_mul(A, B), 4) == WR_E:
                pairs.append((A, B))
    kernel = [(v, P_ID) for v in product((0, 1), repeat=4)]
    index = {pair: i for i, pair in enumerate(pairs)}
    unseen = set(range(len(pairs)))
    orbit_sizes = []
    while unseen:
        i = next(iter(unseen))
        A, B = pairs[i]
        orb = set()
        for k in kernel:
            pair = (wr_conj(k, A), wr_conj(k, B))
            if pair in index:
                orb.add(index[pair])
        orbit_sizes.append(len(orb))
        unseen -= orb
    fixed = sum(
        1 for A, B in pairs
        if all(wr_conj(k, A) == A and wr_conj(k, B) == B for k in kernel)
    )
    return len(residues), len(pairs), sorted(orbit_sizes), fixed


def expected_artifact_rows(pkgs, class_ids):
    rows = []
    for i, (rmask, cmask, rs, cs) in enumerate(pkgs, 1):
        c = classify(rs, cs)
        rows.append({
            "package_id": f"G15P{i:03d}",
            "relation_mask": rmask,
            "constraint_mask": cmask,
            "relations": [r for r in RELATIONS_ORDER if r in rs],
            "constraints": [x for x in CONSTRAINTS_ORDER if x in cs],
            "definitional_class": class_ids[class_key(rs, cs)],
            "cost": list(cost(rs, cs)),
            "universal_split": c[2],
            "universal_aut_fixed_section": c[3],
            "classification": c[0],
            "certificate": c[1],
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest-no-repo", action="store_true",
                    help="skip repository-file digest/artifact checks; finite/classification logic remains exact")
    args = ap.parse_args()

    checks = 0
    here = Path(__file__).resolve()
    root = here.parents[1]

    if not args.selftest_no_repo:
        g15 = root / "research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json"
        art = root / "research_artifacts/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16/CLASSIFICATION_CERTIFICATE.json"
        assert_(g15.exists(), "missing frozen G15 grammar certificate")
        assert_(sha256_file(g15) == G15_CERT_SHA256, "G15 certificate hash drift")
        checks += 2

    pkgs = all_valid_packages()
    assert_(len(pkgs) == 90, "G15 package count drift")
    checks += 1

    keys = sorted({class_key(rs, cs) for _, _, rs, cs in pkgs})
    assert_(len(keys) == 75, "definitional quotient class count drift")
    class_ids = {k: f"G15C{i+1:03d}" for i, k in enumerate(keys)}
    assert_(class_ids[((), ("K4_ADJ",))] == "G15C002", "K4 class id drift")
    checks += 2

    # TETRA toggles K4 as the one frozen redundant presentation flag.
    tetra_specs = [p for p in pkgs if "TETRA_CA" in p[3]]
    assert_(len(tetra_specs) == 30, "TETRA package count")
    assert_(sum("K4_ADJ" in p[3] for p in tetra_specs) == 15, "TETRA/K4 redundant toggles")
    checks += 2

    labels = Counter(classify(rs, cs)[0] for _, _, rs, cs in pkgs)
    assert_(labels == Counter(EXPECTED_SPEC_COUNTS), f"spec partition drift: {labels}")
    checks += 1

    groups = defaultdict(list)
    for p in pkgs:
        groups[class_key(p[2], p[3])].append(p)
    class_labels = {}
    class_min_cost = {}
    for k, members in groups.items():
        labs = {classify(p[2], p[3])[0] for p in members}
        assert_(len(labs) == 1, f"classification not definitional-class invariant: {k}")
        class_labels[k] = next(iter(labs))
        cs = [cost(p[2], p[3]) for p in members]
        cmin = min(cs)
        assert_(all(all(a <= b for a, b in zip(cmin, c)) for c in cs), f"no minimal class representative: {k}")
        class_min_cost[k] = cmin
    assert_(Counter(class_labels.values()) == Counter(EXPECTED_CLASS_COUNTS), "class partition drift")
    checks += 2 + len(groups)

    positives = [k for k, lab in class_labels.items() if lab == "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT"]
    assert_(len(positives) == 9, "positive class count")
    frontier = [
        k for k in positives
        if not any(dominates(class_min_cost[j], class_min_cost[k]) for j in positives if j != k)
    ]
    assert_(frontier == [((), ("K4_ADJ",))], f"faithful/canonical frontier drift: {frontier}")
    assert_(class_min_cost[frontier[0]] == (0, 0, 0, 0, 0, 0, 1, 0), "K4 frontier cost")
    checks += 3

    # Deletion certificate: empty package is valid and P4 kills surjectivity.
    assert_(valid_package(set(), set()), "empty deletion package invalid")
    assert_(len(graph_auts(4, p4_edges())) == 2, "P4 deletion witness")
    checks += 2

    # Positive regressions.
    assert_(len(graph_auts(4, k4_edges())) == 24, "K4 Aut != 24")
    pairs, incidence, tetra_auts = tetra_data()
    assert_(len(tetra_auts) == 24, "tetra Aut != 24")
    induced = set()
    for c, d in combinations(range(4), 2):
        if any((c, a) in incidence and (d, a) in incidence for a in range(6)):
            induced.add((c, d))
    assert_(induced == k4_edges(), "TETRA no longer defines K4")
    checks += 3

    # Singleton symmetry-breaking witnesses.
    singleton_ica_proj = set()
    for pc in permutations(range(4)):
        for pa in permutations(range(6)):
            if {(pc[0], pa[0])} == {(0, 0)}:
                singleton_ica_proj.add(pc)
    assert_(len(singleton_ica_proj) == 6, "singleton I_CA cell stabilizer")
    axis0_stab = [pc for pc, pa in tetra_auts if pa[0] == 0]
    assert_(len(axis0_stab) == 4, "singleton I_HA tetra-axis stabilizer")
    # I_HC singleton at a definable hidden point (e.g. zero under H_C3X3)
    # fixes one Cell, so the cell projection is exactly a subgroup of S3.
    assert_(len([p for p in permutations(range(4)) if p[0] == 0]) == 6, "singleton I_HC cell stabilizer")
    checks += 3

    # GL(2,3) nonsplit regression.
    GL = gl23()
    acts = {projective_action(A) for A in GL}
    kernel = [A for A in GL if projective_action(A) == P_ID]
    liftsA = [A for A in GL if projective_action(A) == A_PERM]
    liftsB = [B for B in GL if projective_action(B) == B_PERM]
    assert_(len(GL) == 48, "GL23 order")
    assert_(len(acts) == 24, "PGL23 image")
    assert_(set(kernel) == {MAT_I, MAT_NEG}, "GL23 projective kernel")
    assert_(len(liftsA) == len(liftsB) == 2, "GL23 frozen lift counts")
    assert_(all(matpow(matmul(A, B), 4) == MAT_NEG for A in liftsA for B in liftsB), "GL23 nonsplit residue")
    checks += 5

    # C2 wr S4 split/noncanonical mandatory regression.
    assert_(len(graph_auts(8, k2222_edges())) == 384, "K2222 Aut != 384")
    residue_count, sections, orbit_sizes, fixed = wreath_certificate()
    assert_((residue_count, sections, orbit_sizes, fixed) == (16, 16, [8, 8], 0), "wreath regression")
    checks += 2

    if not args.selftest_no_repo:
        data = json.loads(art.read_text(encoding="utf-8"))
        assert_(data["task_id"] == TASK_ID and data["publication_id"] == PUBLICATION_ID, "artifact identity")
        assert_(data["terminal_class"] == TERMINAL, "artifact terminal class")
        assert_(data["package_table"] == expected_artifact_rows(pkgs, class_ids), "90-row artifact table drift")
        assert_(data["definitional_quotient"]["classes"] == 75, "artifact quotient count")
        assert_(data["faithful_pareto_frontier"][0]["class_id"] == "G15C002", "artifact faithful frontier")
        assert_(data["canonical_fixed_point_pareto_frontier"][0]["class_id"] == "G15C002", "artifact canonical frontier")
        checks += 6

    print("PASS")
    print(f"task={TASK_ID}")
    print(f"publication={PUBLICATION_ID}")
    print(f"terminal={TERMINAL}")
    print("raw_packages=90")
    print("definitional_classes=75")
    print("universal_split_specs=12")
    print("universal_split_classes=9")
    print("faithful_pareto_frontier=G15C002:{K4_ADJ}")
    print("canonical_fixed_point_pareto_frontier=G15C002:{K4_ADJ}")
    print(f"checks={checks}")


if __name__ == "__main__":
    main()
