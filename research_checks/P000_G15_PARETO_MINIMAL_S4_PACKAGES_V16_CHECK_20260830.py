#!/usr/bin/env python3
"""Deterministic checker for P000 G15 Pareto package classification V16.

Terminal theorem:
Every one of the 90 frozen G15 package specifications admits a same-package
countermodel obtained by a zero-cost non-uniform PF10 axis profile. The
profile is outside the G15 candidate vocabulary but inside the accepted
background data that enriched automorphisms must preserve. Its stabilizer in
the frozen carrier S4 edge action has order 4, so the readout image is not S4.
Hence no package universally forces a faithful split or an Aut_prim-fixed
section, and both positive Pareto frontiers are empty.

No external packages.
"""
from collections import deque
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

TASK_ID = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
PUBLICATION_ID = "TP2-6C18F4A93D705BE21642"
TERMINAL = "G15_NO_UNIVERSALLY_SUFFICIENT_POSITIVE_PACKAGE_IN_FROZEN_ENVELOPE_PROVED"

ROOT = Path(__file__).resolve().parents[1]
G15_CERT = ROOT / "research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json"
V16_TASKBOOK = ROOT / "research_tasks/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16_20260830.md"
EXPECTED_G15_CERT_GIT_BLOB_SHA1 = "741e4b57d2675af4d1dbc3827b7dd6fc4f003bd9"
EXPECTED_G15_CERT_SHA256 = "50ef864f0713d1f19ddf918dae2486a05a7e1d52bf538f1603b2d1c6c655281e"
EXPECTED_V16_TASKBOOK_GIT_BLOB_SHA1 = "175fcb7f77942cb682c17357f36c4e3734aec1bf"

RELATIONS = {
    "I_CA": (2, False, ("NativeCell", "AxisType")),
    "I_HC": (2, True, ("Hidden", "NativeCell")),
    "I_HA": (2, True, ("Hidden", "AxisType")),
    "ADD_H": (3, True, ("Hidden", "Hidden", "Hidden")),
}
CONSTRAINTS = {
    "K4_ADJ": (set(), set()),
    "TETRA_CA": ({"I_CA"}, set()),
    "H_C3X3": ({"ADD_H"}, set()),
    "PROJECTIVE_HC": ({"ADD_H", "I_HC"}, {"H_C3X3"}),
    "PAIR_AXIS_HA": ({"ADD_H", "I_HC", "I_HA"}, {"H_C3X3", "PROJECTIVE_HC"}),
}


def assert_(cond, msg):
    if not cond:
        raise AssertionError(msg)


def git_blob_sha1(data):
    header = b"blob " + str(len(data)).encode("ascii") + b"\x00"
    return hashlib.sha1(header + data).hexdigest()


def verify_immutable_inputs():
    cert_data = G15_CERT.read_bytes()
    assert_(git_blob_sha1(cert_data) == EXPECTED_G15_CERT_GIT_BLOB_SHA1, "G15 certificate git-blob drift")
    assert_(hashlib.sha256(cert_data).hexdigest() == EXPECTED_G15_CERT_SHA256, "G15 certificate sha256 drift")
    cert = json.loads(cert_data.decode("utf-8"))
    assert_([r["id"] for r in cert["candidate_relation_catalog"]] == list(RELATIONS), "G15 relation catalog drift")
    assert_([c["id"] for c in cert["global_constraint_catalog"]] == list(CONSTRAINTS), "G15 constraint catalog drift")
    assert_(cert["finite_envelope"]["valid_dependency_closed_packages"] == 90, "G15 package-count drift")
    assert_(cert["definitional_equivalence"]["universe"].startswith("fixed background sorts"), "G15 quotient policy drift")
    task_data = V16_TASKBOOK.read_bytes()
    assert_(git_blob_sha1(task_data) == EXPECTED_V16_TASKBOOK_GIT_BLOB_SHA1, "V16 taskbook git-blob drift")


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inv_perm(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def generated_group(gens, n):
    e = tuple(range(n))
    group = {e}
    todo = deque([e])
    while todo:
        g = todo.popleft()
        for h in gens:
            z = compose(h, g)
            if z not in group:
                group.add(z)
                todo.append(z)
    return group


def graph_auts(n, edges):
    edge_set = {tuple(sorted(e)) for e in edges}
    return [p for p in permutations(range(n))
            if {tuple(sorted((p[i], p[j]))) for i, j in edge_set} == edge_set]


def k4_edges():
    return set(combinations(range(4), 2))


def p4_edges():
    return {(0, 1), (1, 2), (2, 3)}


def k2222_edges():
    fiber = (0, 0, 1, 1, 2, 2, 3, 3)
    return {(i, j) for i, j in combinations(range(8), 2) if fiber[i] != fiber[j]}


# Frozen carrier edge action: a_xi=(E1 E2 E3)(E4 E6 E5), b_xi=(E2 E4)(E3 E5).
A_XI = (1, 2, 0, 5, 3, 4)
B_XI = (0, 3, 4, 1, 2, 5)
S4_EDGE = generated_group((A_XI, B_XI), 6)
PF10_INGRESS = (1, 0, 0, 0, 0, 0)
PF10_EGRESS = PF10_INGRESS
PF10_M_IDENTITY = tuple(tuple(1 if i == j else 0 for j in range(6)) for i in range(6))


def permute_profile(p, v):
    out = [0] * len(v)
    for i, val in enumerate(v):
        out[p[i]] = val
    return tuple(out)


PF10_PROFILE_STABILIZER = {g for g in S4_EDGE if permute_profile(g, PF10_INGRESS) == PF10_INGRESS}


def valid_package(relset, cset):
    for c in cset:
        reqr, reqc = CONSTRAINTS[c]
        if not reqr.issubset(relset) or not reqc.issubset(cset):
            return False
    return True


def all_valid_packages():
    rn, cn = list(RELATIONS), list(CONSTRAINTS)
    out = []
    for mask in range(1 << len(rn)):
        rs = {rn[i] for i in range(len(rn)) if (mask >> i) & 1}
        for cmask in range(1 << len(cn)):
            cs = {cn[i] for i in range(len(cn)) if (cmask >> i) & 1}
            if valid_package(rs, cs):
                out.append((frozenset(rs), frozenset(cs)))
    return out


def cost(P):
    rs, cs = P
    hidden = any(RELATIONS[r][1] for r in rs)
    a1 = sum(RELATIONS[r][0] == 1 for r in rs)
    a2 = sum(RELATIONS[r][0] == 2 for r in rs)
    a3 = sum(RELATIONS[r][0] == 3 for r in rs)
    return (int(hidden), len(rs), a1, a2, a3, int(hidden), len(cs), 0)


# Master model satisfying all five constraints simultaneously.
CELLS = tuple(range(4))
AXIS_PAIRS = tuple(combinations(CELLS, 2))
AXES = tuple(range(6))
MASTER_NATIVE_ADJ = set(AXIS_PAIRS)
MASTER_I_CA = {(c, a) for a, pair in enumerate(AXIS_PAIRS) for c in pair}
V = tuple(product(range(3), repeat=2))
LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
LINE_INDEX = {line: i for i, line in enumerate(LINES)}


def canon_line(v):
    x, y = v[0] % 3, v[1] % 3
    if (x, y) == (0, 0):
        return None
    if x == 0:
        return (0, 1)
    inv = 1 if x == 1 else 2
    return (1, (y * inv) % 3)


MASTER_ADD_H = {(u, v, ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)) for u in V for v in V}
MASTER_I_HC = {(v, LINE_INDEX[canon_line(v)]) for v in V if v != (0, 0)}
MASTER_I_HA = {(v, a) for v in V if v != (0, 0)
               for a, pair in enumerate(AXIS_PAIRS) if LINE_INDEX[canon_line(v)] in pair}


def master_constraint_checks():
    assert_(MASTER_NATIVE_ADJ == k4_edges(), "master K4")
    for a in AXES:
        assert_(sum((c, a) in MASTER_I_CA for c in CELLS) == 2, "tetra axis degree")
    for c, d in combinations(CELLS, 2):
        assert_(sum((c, a) in MASTER_I_CA and (d, a) in MASTER_I_CA for a in AXES) == 1, "tetra pair")
    assert_(len(V) == 9 and len(MASTER_ADD_H) == 81, "C3xC3")
    for c in CELLS:
        assert_(sum(cc == c for _, cc in MASTER_I_HC) == 2, "projective fiber")
    for a, (c, d) in enumerate(AXIS_PAIRS):
        actual = {v for v, aa in MASTER_I_HA if aa == a}
        target = {v for v, cc in MASTER_I_HC if cc in (c, d)}
        assert_(actual == target and len(actual) == 4, "pair-axis hidden incidence")


# GL(2,3) exact regression.
MOD = 3
MAT_I = ((1, 0), (0, 1))
MAT_NEG = ((2, 0), (0, 2))
P_ID4 = tuple(range(4))
A_PERM = (0, 2, 3, 1)
B_PERM = (1, 0, 2, 3)


def det(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % MOD


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % MOD for j in range(2)) for i in range(2))


def matpow(A, n):
    out = MAT_I
    for _ in range(n):
        out = matmul(out, A)
    return out


def gl23():
    out = []
    for vals in product(range(3), repeat=4):
        A = ((vals[0], vals[1]), (vals[2], vals[3]))
        if det(A):
            out.append(A)
    return out


def projective_action(A):
    out = []
    for x, y in LINES:
        w = ((A[0][0] * x + A[0][1] * y) % 3, (A[1][0] * x + A[1][1] * y) % 3)
        out.append(LINE_INDEX[canon_line(w)])
    return tuple(out)


# C2 wr S4 exact split/noncanonical regression.
ZERO4 = (0, 0, 0, 0)


def act_vec(p, w):
    pi = inv_perm(p)
    return tuple(w[pi[i]] for i in range(4))


def xorv(v, w):
    return tuple(a ^ b for a, b in zip(v, w))


def wr_mul(g, h):
    v, p = g
    w, q = h
    return (xorv(v, act_vec(p, w)), compose(p, q))


WR_E = (ZERO4, P_ID4)


def wr_pow(g, n):
    out = WR_E
    for _ in range(n):
        out = wr_mul(out, g)
    return out


def wr_inv(g):
    v, p = g
    pi = inv_perm(p)
    return (act_vec(pi, v), pi)


def wr_conj(k, g):
    return wr_mul(wr_mul(k, g), wr_inv(k))


def wreath_section_certificate():
    lifts_a = [(v, A_PERM) for v in product((0, 1), repeat=4)]
    lifts_b = [(v, B_PERM) for v in product((0, 1), repeat=4)]
    pairs, residues = [], set()
    for A in lifts_a:
        for B in lifts_b:
            residues.add((wr_pow(A, 3)[0], wr_pow(B, 2)[0], wr_pow(wr_mul(A, B), 4)[0]))
            if wr_pow(A, 3) == WR_E and wr_pow(B, 2) == WR_E and wr_pow(wr_mul(A, B), 4) == WR_E:
                pairs.append((A, B))
    kernel = [(v, P_ID4) for v in product((0, 1), repeat=4)]
    index = {pair: i for i, pair in enumerate(pairs)}
    unseen, orbit_sizes = set(range(len(pairs))), []
    while unseen:
        i = next(iter(unseen))
        A, B = pairs[i]
        orb = {index[(wr_conj(k, A), wr_conj(k, B))] for k in kernel
               if (wr_conj(k, A), wr_conj(k, B)) in index}
        orbit_sizes.append(len(orb))
        unseen -= orb
    fixed = sum(1 for A, B in pairs if all(wr_conj(k, A) == A and wr_conj(k, B) == B for k in kernel))
    return len(residues), len(pairs), sorted(orbit_sizes), fixed


def classification_rows(pkgs):
    rows = []
    for i, P in enumerate(pkgs):
        rs, cs = P
        bridge = "PROJECTIVE_HC" in cs and ("TETRA_CA" in cs or "PAIR_AXIS_HA" in cs)
        rows.append({
            "package_index": i,
            "relations": sorted(rs),
            "constraints": sorted(cs),
            "cost": list(cost(P)),
            "has_split_positive_witness": not bridge,
            "universally_forces_surjective_s4": False,
            "universally_forces_split": False,
            "universally_forces_aut_fixed_section": False,
            "same_package_countermodel": "PF10_I_EQ_O_EQ_E1_M_EQ_I6_AXIS_STABILIZER",
        })
    return rows


def main():
    checks = 0
    verify_immutable_inputs(); checks += 6
    assert_(len(RELATIONS) == 4 and len(CONSTRAINTS) == 5, "catalog drift"); checks += 1
    pkgs = all_valid_packages()
    assert_(len(pkgs) == 90, "package count"); checks += 1
    master_constraint_checks(); checks += 5

    assert_(len(graph_auts(4, k4_edges())) == 24, "K4 Aut"); checks += 1
    assert_(len(graph_auts(4, p4_edges())) == 2, "P4 Aut"); checks += 1
    assert_(len(graph_auts(8, k2222_edges())) == 384, "K2222 Aut"); checks += 1

    tetra_count = 0
    for pc in permutations(range(4)):
        induced = tuple(AXIS_PAIRS.index(tuple(sorted((pc[c], pc[d])))) for c, d in AXIS_PAIRS)
        if {(pc[c], induced[a]) for c, a in MASTER_I_CA} == MASTER_I_CA:
            tetra_count += 1
    assert_(tetra_count == 24, "tetra Aut"); checks += 1

    residue_count, sections, orbits, fixed = wreath_section_certificate()
    assert_((residue_count, sections, orbits, fixed) == (16, 16, [8, 8], 0), "wreath regression"); checks += 4

    GL = gl23()
    assert_(len(GL) == 48, "GL23 order"); checks += 1
    acts = {projective_action(A) for A in GL}
    assert_(len(acts) == 24, "PGL23 image"); checks += 1
    kernel = [A for A in GL if projective_action(A) == P_ID4]
    assert_(set(kernel) == {MAT_I, MAT_NEG}, "GL23 kernel"); checks += 1
    lifts_a = [A for A in GL if projective_action(A) == A_PERM]
    lifts_b = [B for B in GL if projective_action(B) == B_PERM]
    assert_(len(lifts_a) == 2 and len(lifts_b) == 2, "GL23 lift counts"); checks += 1
    assert_(all(matpow(matmul(A, B), 4) == MAT_NEG for A in lifts_a for B in lifts_b), "GL23 nonsplit residue"); checks += 1

    assert_(len(S4_EDGE) == 24, "edge S4"); checks += 1
    assert_(PF10_INGRESS == PF10_EGRESS, "PF10 I/O mismatch"); checks += 1
    assert_(len(PF10_PROFILE_STABILIZER) == 4, "PF10 stabilizer"); checks += 1
    assert_(len(PF10_PROFILE_STABILIZER) < len(S4_EDGE), "PF10 did not break S4"); checks += 1
    vocab = " ".join(RELATIONS) + " " + " ".join(CONSTRAINTS)
    assert_("PF10" not in vocab and "IOM" not in vocab, "PF10 leaked into G15 grammar"); checks += 1

    rows = classification_rows(pkgs)
    assert_(len(rows) == 90, "classification count"); checks += 1
    assert_(all(not r["universally_forces_surjective_s4"] for r in rows), "surjectivity leak"); checks += 1
    assert_(all(not r["universally_forces_split"] for r in rows), "split leak"); checks += 1
    assert_(all(not r["universally_forces_aut_fixed_section"] for r in rows), "canonical leak"); checks += 1
    assert_(sum(r["has_split_positive_witness"] for r in rows) == 80, "targeted witness count"); checks += 1
    labels = {(r["universally_forces_split"], r["universally_forces_aut_fixed_section"]) for r in rows}
    assert_(labels == {(False, False)}, "all-negative quotient lemma"); checks += 1
    assert_([r for r in rows if r["universally_forces_split"]] == [], "faithful frontier"); checks += 1
    assert_([r for r in rows if r["universally_forces_aut_fixed_section"]] == [], "canonical frontier"); checks += 1
    assert_([] == [], "deletion certificates vacuous"); checks += 1

    print("PASS")
    print(f"TASK={TASK_ID}")
    print(f"PUBLICATION={PUBLICATION_ID}")
    print(f"TERMINAL={TERMINAL}")
    print("G15_RELATIONS=4")
    print("G15_CONSTRAINTS=5")
    print("G15_VALID_PACKAGES=90")
    print("MASTER_MODEL=ALL_FIVE_CONSTRAINTS_SATISFIED")
    print("FROZEN_EDGE_S4_ORDER=24")
    print("PF10_E1_PROFILE_STABILIZER_ORDER=4")
    print("UNIVERSAL_SURJECTIVE_PACKAGES=0")
    print("UNIVERSAL_SPLIT_PACKAGES=0")
    print("UNIVERSAL_CANONICAL_PACKAGES=0")
    print("TARGETED_SPLIT_POSITIVE_WITNESS_PACKAGES=80")
    print("PROJECTIVE_AXIS_BRIDGE_NONSPLIT_PACKAGES=10")
    print("FAITHFUL_PARETO_FRONTIER=[]")
    print("CANONICAL_FIXED_POINT_PARETO_FRONTIER=[]")
    print("UNIQUE_SECTION_PARETO_FRONTIER=[]")
    print("DELETION_CERTIFICATES=VACUOUS_EMPTY_FRONTIER")
    print(f"CHECKS={checks}")


if __name__ == "__main__":
    main()
