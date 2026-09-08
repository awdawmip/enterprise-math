#!/usr/bin/env python3
"""Task-local exact audit for P000 FCC native-coordinate bridge / rotation atlas.

This checker re-audits the frozen theorem and sharpens only the residual
frame-selection obstruction. It is not a general-purpose Enterprise tool and
does not promote FCC carrier equality to native P000 identity.
"""
from __future__ import annotations

import itertools
import json

TASK_ID = "RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS"
PUBLICATION_ID = "TP2-0B7E6C14F3A95D208E61"
RESEARCHER_ID = "EM-P000FCC-7C4F1A"
CLAIM_ID = "chatgpt-p000fcc-atlas-review-synthesis-v3-20260906-1454-7c4f1a"
PRIOR_RESULT_ID = "RR-BF4BC89ACAC51D2E16C5"

LINES = (
    (1, 1, 0),
    (1, -1, 0),
    (1, 0, 1),
    (1, 0, -1),
    (0, 1, 1),
    (0, 1, -1),
)

# Frame used only as a supplied witness: E1..E6 -> L1,L3,L6,L4,L5,L2.
AXIS_TO_LINE = (0, 2, 5, 3, 4, 1)

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
TASK_KERNEL_BASIS = (K_A, K_B, K_C)

# Exact integral parametrization of all solutions Aq=0:
# q = a*N1+b*N2+c*N3 = (-a-b+c, a-c, a, b-c, b, c).
N1 = (-1, 1, 1, 0, 0, 0)
N2 = (-1, 0, 0, 1, 1, 0)
N3 = (1, -1, 0, -1, 0, 1)
PARAM_KERNEL_BASIS = (N1, N2, N3)

HCP_SHELL = (
    (2, 0, 0), (1, 3, 0), (-1, 3, 0), (-2, 0, 0),
    (-1, -3, 0), (1, -3, 0),
    (1, 1, 1), (-1, 1, 1), (0, -2, 1),
    (1, 1, -1), (-1, 1, -1), (0, -2, -1),
)


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


def det3_matrix(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def det3_cols(cols):
    return det3_matrix(tuple(tuple(A_MATRIX[r][c] for c in cols) for r in range(3)))


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1, +1), repeat=3):
            if perm_sign(p) * signs[0] * signs[1] * signs[2] != 1:
                continue
            out.append(tuple(
                tuple(signs[r] if c == p[r] else 0 for c in range(3))
                for r in range(3)
            ))
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
        lp, ls = [], []
        for v in LINES:
            j, eps = line_match(mat_vec(R, v))
            lp.append(j)
            ls.append(eps)
        smap, tau = {}, {}
        for s, inds in CARRIER_SLICES.items():
            image = frozenset(lp[i] for i in inds)
            targets = [t for t, z in slice_sets.items() if z == image]
            assert len(targets) == 1
            t = targets[0]
            smap[s] = t
            vals = [
                ORIENT[s][i] * ls[i] * ORIENT[t][lp[i]]
                for i in inds
            ]
            assert len(set(vals)) == 1
            tau[s] = vals[0]
        out.append((R, tuple(lp), tuple(ls), smap, tau))
    return tuple(out)


def check_charts():
    for s, inds in CARRIER_SLICES.items():
        oriented = [vec_scale(ORIENT[s][i], LINES[i]) for i in inds]
        assert vec_add(*oriented) == (0, 0, 0)
        assert all(dot(v, v) == 2 for v in oriented)
        assert all(
            dot(oriented[i], oriented[j]) == -1
            for i in range(3) for j in range(i + 1, 3)
        )
    for s, t in itertools.combinations("ABCD", 2):
        assert len(set(CARRIER_SLICES[s]) & set(CARRIER_SLICES[t])) == 1
        assert len(set(NATIVE_SLICES[s]) & set(NATIVE_SLICES[t])) == 1


def check_readout():
    minors = {
        cols: det3_cols(cols)
        for cols in itertools.combinations(range(6), 3)
    }
    nonzero = {cols: d for cols, d in minors.items() if d}
    assert len(nonzero) == 16
    assert {abs(d) for d in nonzero.values()} == {2}

    # Every column has even coordinate sum, so im(A) lies in D3.
    assert all(sum(w) % 2 == 0 for w in W)

    # Conversely, every (x,y,z) in D3 has the exact reconstruction
    # a=(x+y-z)/2, b=(x+z-y)/2, c=(y+z-x)/2 via L1,L3,L5.
    for x, y, z in itertools.product(range(-5, 6), repeat=3):
        if (x + y + z) % 2:
            continue
        a = (x + y - z) // 2
        b = (x + z - y) // 2
        c = (y + z - x) // 2
        q = (a, b, 0, 0, c, 0)
        assert mat_vec(A_MATRIX, q) == (x, y, z)

    for k in TASK_KERNEL_BASIS + PARAM_KERNEL_BASIS:
        assert mat_vec(A_MATRIX, k) == (0, 0, 0)

    # The task kernel basis and the exact-parametrization basis differ by the
    # unimodular coefficient matrix with columns (-1,0,0),(0,-1,0),(0,1,1).
    transform = ((-1, 0, 0), (0, -1, 1), (0, 0, 1))
    assert abs(det3_matrix(transform)) == 1
    for j, n in enumerate(PARAM_KERNEL_BASIS):
        reconstructed = tuple(
            sum(TASK_KERNEL_BASIS[k][i] * transform[k][j] for k in range(3))
            for i in range(6)
        )
        assert reconstructed == n

    # Verify the closed-form parametrization over a finite exact box.
    for a, b, c in itertools.product(range(-4, 5), repeat=3):
        q = (-a - b + c, a - c, a, b - c, b, c)
        assert mat_vec(A_MATRIX, q) == (0, 0, 0)
        rhs = tuple(a * N1[i] + b * N2[i] + c * N3[i] for i in range(6))
        assert q == rhs

    rays = {w for v in W for w in (v, tuple(-x for x in v))}
    assert len(rays) == 12

    return {
        "rank": 3,
        "nonzero_3x3_minors": 16,
        "nonzero_minor_abs_value": 2,
        "image": "D3_even_coordinate_sum",
        "kernel_rank": 3,
        "kernel_basis_saturated": True,
        "local_directed_rays": 12,
    }


def check_frame_anchor_hierarchy():
    frames = tuple(itertools.permutations(range(6)))
    carrier_sets = {s: frozenset(v) for s, v in CARRIER_SLICES.items()}

    def image_support(f, s):
        return frozenset(f[i] for i in NATIVE_SLICES[s])

    exact_counts = {}
    for k in range(5):
        rows = {}
        for charts in itertools.combinations("ABCD", k):
            count = sum(
                all(image_support(f, s) == carrier_sets[s] for s in charts)
                for f in frames
            )
            rows["".join(charts) or "NONE"] = count
        exact_counts[str(k)] = rows

    assert exact_counts["0"] == {"NONE": 720}
    assert set(exact_counts["1"].values()) == {36}
    assert set(exact_counts["2"].values()) == {4}
    assert set(exact_counts["3"].values()) == {1}
    assert exact_counts["4"] == {"ABCD": 1}

    carrier_family = set(carrier_sets.values())
    unordered_family_count = sum(
        {image_support(f, s) for s in "ABCD"} == carrier_family
        for f in frames
    )
    assert unordered_family_count == 24

    # The supplied witness is the unique frame once any three named chart
    # correspondences are imposed.
    for charts in itertools.combinations("ABCD", 3):
        survivors = [
            f for f in frames
            if all(image_support(f, s) == carrier_sets[s] for s in charts)
        ]
        assert survivors == [AXIS_TO_LINE]

    return {
        "all_frames": 720,
        "one_named_slice_each": exact_counts["1"],
        "two_named_slices_each": exact_counts["2"],
        "three_named_slices_each": exact_counts["3"],
        "four_named_slices": 1,
        "unordered_k4_family_isomorphisms": 24,
        "minimal_named_slice_count_for_unique_frame": 3,
    }


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
    lifts = {}
    for R, lp, ls, smap, tau in actions:
        for s in "ABCD":
            tau_counts[tau[s]] += 1
        L = lift6(lp, ls)
        lifts[R] = L
        assert mat_mul(A_MATRIX, L) == mat_mul(R, A_MATRIX)
        for k in TASK_KERNEL_BASIS:
            assert mat_vec(A_MATRIX, mat_vec(L, k)) == (0, 0, 0)

    assert tau_counts == {+1: 48, -1: 48}

    lift_compositions = 0
    cocycles = 0
    for a1 in actions:
        for a2 in actions:
            R12 = mat_mul(a2[0], a1[0])
            a12 = by_R[R12]
            assert mat_mul(lifts[a2[0]], lifts[a1[0]]) == lifts[R12]
            lift_compositions += 1
            for s in "ABCD":
                assert a12[4][s] == a2[4][a1[3][s]] * a1[4][s]
                cocycles += 1

    assert lift_compositions == 576
    assert cocycles == 2304
    return {
        "group_order": 24,
        "distinct_line_actions": 24,
        "distinct_slice_actions": 24,
        "line_stabilizer_order": 4,
        "slice_stabilizer_order": 6,
        "lift_composition_checks": 576,
        "chart_transport_checks": 96,
        "chart_cocycle_checks": 2304,
        "tau_positive": 48,
        "tau_negative": 48,
    }


def check_hcp():
    pts = set(HCP_SHELL)
    missing = [(p, tuple(-x for x in p)) for p in HCP_SHELL
               if tuple(-x for x in p) not in pts]
    assert len(missing) == 6
    assert ((1, 1, 1), (-1, -1, -1)) in missing
    return {"missing_antipodes": len(missing), "centrally_symmetric": False}


def main():
    check_charts()
    result = {
        "schema": "ENTERPRISE_MATH_TASK_LOCAL_FCC_ATLAS_AUDIT_CERTIFICATE_V1",
        "task_id": TASK_ID,
        "publication_id": PUBLICATION_ID,
        "researcher_id": RESEARCHER_ID,
        "claim_id": CLAIM_ID,
        "prior_result_id": PRIOR_RESULT_ID,
        "terminal_class": "STRICT_PARTIAL_OR_GROUPOID_ATLAS_PROVED",
        "readout": check_readout(),
        "charts": {
            "count": 4,
            "incidence": "K4_edges",
            "exact_120_degree": True,
        },
        "frame_anchor_hierarchy": check_frame_anchor_hierarchy(),
        "rotation": check_rotation_atlas(),
        "hcp_regression": check_hcp(),
        "new_residue_theorem": (
            "Within named slice-incidence data, any two named native-to-carrier "
            "slice correspondences leave four frames, while any three determine "
            "the unique axis-line frame; an unordered K4 atlas still leaves 24 "
            "incidence isomorphisms."
        ),
        "native_identity_firewall": (
            "Carrier readout equality modulo ker(A) is not native P000 equality."
        ),
        "tool_payload": "NO_TOOL_PAYLOAD_TASK_LOCAL_CHECKER",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
