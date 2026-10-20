#!/usr/bin/env python3
"""Exact finite certificate for the P000 FCC native-coordinate bridge/rotation atlas.

This checker certifies only the task-local discrete model and the finite carrier
incidence/action statements.  It does not promote FCC to native ontology.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

TASK_ID = "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS"
PUBLICATION_ID = "TP2-0B7E6C14F3A95D208E61"
RESEARCHER_ID = "EM-P000FCC-7B4D2A"
CLAIM_ID = "chatgpt-p000fcc-20260829-2118-7b4d2a"
BASE_MAIN_SHA = "65d1cae115e648f5154a898cd3ba83a2a2b27223"

LINES = (
    (1, 1, 0),
    (1, -1, 0),
    (1, 0, 1),
    (1, 0, -1),
    (0, 1, 1),
    (0, 1, -1),
)
LINE_NAMES = tuple(f"L{i}" for i in range(1, 7))

# E1->L1, E2->L3, E3->L6, E4->L4, E5->L5, E6->L2.
AXIS_TO_LINE = (0, 2, 5, 3, 4, 1)
AXIS_NAMES = tuple(f"E{i}" for i in range(1, 7))

CARRIER_SLICES = {
    "A": (0, 2, 5),
    "B": (0, 3, 4),
    "C": (1, 2, 4),
    "D": (1, 3, 5),
}
NATIVE_SLICES = {
    "A": (0, 1, 2),
    "B": (0, 3, 4),
    "C": (1, 4, 5),
    "D": (2, 3, 5),
}
ORIENT = {
    "A": {0: +1, 2: -1, 5: -1},
    "B": {0: +1, 3: -1, 4: -1},
    "C": {1: +1, 2: -1, 4: +1},
    "D": {1: +1, 3: -1, 5: +1},
}

W = tuple(LINES[j] for j in AXIS_TO_LINE)
A_MATRIX = tuple(tuple(W[c][r] for c in range(6)) for r in range(3))

K_A = (1, -1, -1, 0, 0, 0)
K_B = (1, 0, 0, -1, -1, 0)
K_C = (0, -1, 0, 0, 1, 1)
K_D = (0, 0, 1, -1, 0, 1)
KERNEL_BASIS = (K_A, K_B, K_C)

HCP_SHELL = (
    (2, 0, 0), (1, 3, 0), (-1, 3, 0), (-2, 0, 0),
    (-1, -3, 0), (1, -3, 0),
    (1, 1, 1), (-1, 1, 1), (0, -2, 1),
    (1, 1, -1), (-1, 1, -1), (0, -2, -1),
)

SOURCE_PINS = {
    "research_tasks/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_SYNTHESIZED_V3_20260829.md":
        "2a36121fe32bc002268ab5a9e4b4ef34a5694a04",
    "p000_reality_foundation.json":
        "2eb853aa6bd2ff7e9f19b5eb4f231cec00a31900",
    "research_returns/P000_FIRST_SHELL_POLYHEDRON_CLASSIFICATION_RETURN_20260829.md":
        "ebdba3056bbd7cd7e0391577b7426b9f0733d2e8",
    "driver_reviews/P000_FIRST_SHELL_POLYHEDRON_DRIVER_REVIEW_AND_COORDINATE_SELECTION_20260829.md":
        "ed000e9a00bbd99db4761c44e8afbdefbb2715a9",
    "research_review_syntheses/RR-73C4AC1CB16F08C64FC4/RVS-0333BA126C92B3726D41.json":
        "6d5956c3afc94a61734350a22231d27b2ed42a37",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vec_add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(len(vs[0])))


def vec_scale(s, v):
    return tuple(s * x for x in v)


def mat_vec(M, v):
    return tuple(sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M)))


def mat_mul(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(len(B)))
              for j in range(len(B[0])))
        for i in range(len(A))
    )


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1, +1), repeat=3):
            if perm_sign(p) * signs[0] * signs[1] * signs[2] != 1:
                continue
            M = tuple(
                tuple(signs[r] if c == p[r] else 0 for c in range(3))
                for r in range(3)
            )
            out.append(M)
    assert len(out) == len(set(out)) == 24
    return tuple(out)


def line_match(w):
    for j, v in enumerate(LINES):
        if w == v:
            return j, +1
        if w == tuple(-x for x in v):
            return j, -1
    raise AssertionError(("not an FCC line representative up to sign", w))


def lift6(line_perm, line_sign):
    """Frame-conjugated signed lift on the task-local Z^6 address lattice."""
    inv_frame = {line: axis for axis, line in enumerate(AXIS_TO_LINE)}
    M = [[0] * 6 for _ in range(6)]
    for axis, line in enumerate(AXIS_TO_LINE):
        image_line = line_perm[line]
        image_axis = inv_frame[image_line]
        M[image_axis][axis] = line_sign[line]
    return tuple(tuple(row) for row in M)


def build_actions():
    slice_sets = {s: frozenset(v) for s, v in CARRIER_SLICES.items()}
    out = []
    for R in rotations():
        lp = []
        ls = []
        for v in LINES:
            j, eps = line_match(mat_vec(R, v))
            lp.append(j)
            ls.append(eps)

        smap = {}
        tau = {}
        for s, inds in CARRIER_SLICES.items():
            image = frozenset(lp[i] for i in inds)
            targets = [t for t, z in slice_sets.items() if z == image]
            assert len(targets) == 1
            t = targets[0]
            smap[s] = t
            vals = []
            for i in inds:
                vals.append(ORIENT[s][i] * ls[i] * ORIENT[t][lp[i]])
            assert len(set(vals)) == 1
            tau[s] = vals[0]
        out.append((R, tuple(lp), tuple(ls), smap, tau))
    return tuple(out)


def check_sources(root: Path):
    for rel, expected in SOURCE_PINS.items():
        path = root / rel
        assert path.exists(), rel
        actual = git_blob_sha1(path)
        assert actual == expected, (rel, actual, expected)


def check_frame_and_slices():
    assert len(set(AXIS_TO_LINE)) == 6
    for s in CARRIER_SLICES:
        mapped = frozenset(AXIS_TO_LINE[i] for i in NATIVE_SLICES[s])
        assert mapped == frozenset(CARRIER_SLICES[s])

    for line in range(6):
        assert sum(line in CARRIER_SLICES[s] for s in CARRIER_SLICES) == 2
    for axis in range(6):
        assert sum(axis in NATIVE_SLICES[s] for s in NATIVE_SLICES) == 2
    for s, t in itertools.combinations("ABCD", 2):
        assert len(set(CARRIER_SLICES[s]) & set(CARRIER_SLICES[t])) == 1
        assert len(set(NATIVE_SLICES[s]) & set(NATIVE_SLICES[t])) == 1

    for s, inds in CARRIER_SLICES.items():
        oriented = [vec_scale(ORIENT[s][i], LINES[i]) for i in inds]
        assert vec_add(*oriented) == (0, 0, 0)
        assert all(dot(v, v) == 2 for v in oriented)
        assert all(dot(oriented[i], oriented[j]) == -1
                   for i in range(3) for j in range(i + 1, 3))


def check_readout_and_kernel():
    rays = []
    for w in W:
        rays.append(w)
        rays.append(tuple(-x for x in w))
    assert len(set(rays)) == 12

    for k in (K_A, K_B, K_C, K_D):
        assert mat_vec(A_MATRIX, k) == (0, 0, 0)
    assert tuple(K_A[i] - K_B[i] - K_C[i] + K_D[i] for i in range(6)) == (0,) * 6

    # Aq=0 iff, with q2,q3,q4 free,
    # q=(-q3-q4,q2,q3,q4,-q2+q3+q4,q3-q2).
    for q2, q3, q4 in itertools.product(range(-3, 4), repeat=3):
        q = (-q3 - q4, q2, q3, q4, -q2 + q3 + q4, q3 - q2)
        assert mat_vec(A_MATRIX, q) == (0, 0, 0)
        rhs = tuple(
            -q3 * K_A[i] - q4 * K_B[i] + (q3 - q2) * K_C[i]
            for i in range(6)
        )
        assert q == rhs

    # D3 surjectivity: (x,y,z)=a*v1+b*v3+c*v5.
    for x, y, z in itertools.product(range(-8, 9), repeat=3):
        if (x + y + z) % 2:
            continue
        a = (x + y - z) // 2
        b = (x + z - y) // 2
        c = (y + z - x) // 2
        q = (a, b, 0, 0, c, 0)
        assert mat_vec(A_MATRIX, q) == (x, y, z)

    for q in itertools.product(range(-2, 3), repeat=6):
        x, y, z = mat_vec(A_MATRIX, q)
        assert (x + y + z) % 2 == 0


def check_frame_torsor():
    frames = tuple(itertools.permutations(range(6)))
    assert len(frames) == 720

    JA = frozenset(NATIVE_SLICES["A"])
    JB = frozenset(NATIVE_SLICES["B"])
    SA = frozenset(CARRIER_SLICES["A"])
    SB = frozenset(CARRIER_SLICES["B"])
    ja_frames = [f for f in frames if frozenset(f[i] for i in JA) == SA]
    jab_frames = [f for f in ja_frames if frozenset(f[i] for i in JB) == SB]
    assert len(ja_frames) == 36
    assert len(jab_frames) == 4
    assert AXIS_TO_LINE in jab_frames

    stabilizers = []
    for k in range(7):
        stabilizers.append(sum(all(f[i] == AXIS_TO_LINE[i] for i in range(k)) for f in frames))
    assert stabilizers == [720, 120, 24, 6, 2, 1, 1]
    return stabilizers


def check_rotation_atlas():
    actions = build_actions()
    by_R = {a[0]: a for a in actions}
    assert len(by_R) == 24
    assert len({a[1] for a in actions}) == 24
    assert len({tuple(a[3][s] for s in "ABCD") for a in actions}) == 24

    line_stabilizers = [sum(a[1][i] == i for a in actions) for i in range(6)]
    slice_stabilizers = {s: sum(a[3][s] == s for a in actions) for s in "ABCD"}
    assert line_stabilizers == [4] * 6
    assert slice_stabilizers == {s: 6 for s in "ABCD"}

    tau_counts = {+1: 0, -1: 0}
    for a in actions:
        for s in "ABCD":
            tau_counts[a[4][s]] += 1
    assert tau_counts == {+1: 48, -1: 48}

    lifts = {}
    for R, lp, ls, smap, tau in actions:
        L = lift6(lp, ls)
        lifts[R] = L
        assert mat_mul(A_MATRIX, L) == mat_mul(R, A_MATRIX)
        for k in KERNEL_BASIS:
            assert mat_vec(A_MATRIX, mat_vec(L, k)) == (0, 0, 0)

    lift_composition_checks = 0
    chart_cocycle_checks = 0
    for a1 in actions:
        for a2 in actions:
            R12 = mat_mul(a2[0], a1[0])
            a12 = by_R[R12]
            assert mat_mul(lifts[a2[0]], lifts[a1[0]]) == lifts[R12]
            lift_composition_checks += 1
            for s in "ABCD":
                assert a12[4][s] == a2[4][a1[3][s]] * a1[4][s]
                chart_cocycle_checks += 1

    assert lift_composition_checks == 576
    assert chart_cocycle_checks == 2304

    return {
        "group_order": 24,
        "distinct_line_permutations": 24,
        "distinct_slice_permutations": 24,
        "line_stabilizer_order": 4,
        "slice_stabilizer_order": 6,
        "frame_conditioned_lift_composition_checks": 576,
        "chart_transport_checks": 96,
        "chart_cocycle_checks": 2304,
        "chart_transport_tau_counts": {"+1": 48, "-1": 48},
    }


def check_hcp_regression():
    pts = set(HCP_SHELL)
    missing = []
    for p in HCP_SHELL:
        n = tuple(-x for x in p)
        if n not in pts:
            missing.append((p, n))
    assert missing
    assert ((1, 1, 1), (-1, -1, -1)) in missing
    return len(missing)


def build_certificate():
    frame_stabilizers = check_frame_torsor()
    rotation = check_rotation_atlas()
    hcp_missing = check_hcp_regression()
    check_frame_and_slices()
    check_readout_and_kernel()

    overlap = {}
    for s, t in itertools.combinations("ABCD", 2):
        i = next(iter(set(CARRIER_SLICES[s]) & set(CARRIER_SLICES[t])))
        overlap[s + t] = {
            "line": LINE_NAMES[i],
            "orientation_transition": ORIENT[t][i] * ORIENT[s][i],
        }

    return {
        "schema": "P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_CERTIFICATE_V1",
        "task_id": TASK_ID,
        "publication_id": PUBLICATION_ID,
        "researcher_id": RESEARCHER_ID,
        "claim_id": CLAIM_ID,
        "execution_base_main": BASE_MAIN_SHA,
        "terminal_class": "STRICT_PARTIAL_OR_GROUPOID_ATLAS_PROVED",
        "native_model": {
            "address_group": "Z^6",
            "adjacency": "q~q+/-e_i for i=1..6",
            "l1_degree": 12,
            "axis_to_carrier_line_frame": {
                AXIS_NAMES[i]: LINE_NAMES[AXIS_TO_LINE[i]] for i in range(6)
            },
            "native_slice_charts": {
                s: [AXIS_NAMES[i] for i in NATIVE_SLICES[s]] for s in "ABCD"
            },
        },
        "carrier": {
            "image_lattice": "D3={(x,y,z) in Z^3: x+y+z even}",
            "six_lines": {LINE_NAMES[i]: list(LINES[i]) for i in range(6)},
            "slices": {s: [LINE_NAMES[i] for i in CARRIER_SLICES[s]] for s in "ABCD"},
            "overlap_transitions": overlap,
        },
        "readout": {
            "matrix_columns_by_native_axis": [list(v) for v in W],
            "local_l1_map_bijective": True,
            "global_map_injective": False,
            "global_map_surjective_onto_D3": True,
            "regular_covering": True,
            "deck_group": "ker(A) ~= Z^3",
            "kernel_basis": [list(k) for k in KERNEL_BASIS],
            "dependent_chart_kernel": list(K_D),
            "kernel_relation": "K_A-K_B-K_C+K_D=0",
        },
        "frame_groupoid": {
            "unframed_axis_line_bijections": 720,
            "frames_after_JA_to_SA_set_constraint": 36,
            "frames_after_JA_to_SA_and_JB_to_SB_set_constraints": 4,
            "pointwise_anchor_stabilizers_k0_to_k6": frame_stabilizers,
            "canonical_unframed_bridge": False,
        },
        "rotation": rotation,
        "hcp_regression": {
            "centrally_symmetric": False,
            "explicit_missing_antipode": [[1, 1, 1], [-1, -1, -1]],
            "shell_points_missing_antipodes_count": hcp_missing,
        },
        "promotion_guards": {
            "fcc_rank_reduces_native_dimension": False,
            "carrier_antipode_creates_native_axis_equivalence": False,
            "carrier_kernel_creates_native_equality": False,
            "continuous_SO3_or_SO6_imported_as_native_truth": False,
            "hcp_dropped": False,
            "foundation_or_working_truth_promoted": False,
        },
        "source_pins_git_blob_sha1": SOURCE_PINS,
    }


def main():
    root = Path(__file__).resolve().parents[1]
    check_sources(root)
    cert = build_certificate()

    cert_path = root / "research_artifacts/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS/exact_certificate_20260829.json"
    if cert_path.exists():
        frozen = json.loads(cert_path.read_text(encoding="utf-8"))
        assert frozen == cert

    print(
        "P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_CHECK=PASS "
        "rotations=24 line_perms=24 slice_perms=24 lift_compositions=576 "
        "chart_transports=96 chart_cocycles=2304 frame_torsor=720 "
        "kernel_rank=3 hcp_central_symmetry=false"
    )


if __name__ == "__main__":
    main()
