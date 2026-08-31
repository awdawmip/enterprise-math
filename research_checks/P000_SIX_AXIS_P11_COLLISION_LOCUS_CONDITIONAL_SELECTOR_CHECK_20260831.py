#!/usr/bin/env python3
"""Exact task-local checker for P000 P11 collision locus / conditional selector.

Standard-library only. It verifies:
* exact S3 collision classification, including repeated marginals;
* the symmetric Gram/Vandermonde quadratic resolvents for P21 and P12;
* same/opposite binary-root ordering on the two collision classes;
* root-box minimal pairable witnesses (B<=6);
* scaled infinite-family regression;
* no three-state P11 fibre on an exhaustive bounded control domain.
"""
from collections import defaultdict
from itertools import combinations, combinations_with_replacement, permutations

PERMS = tuple(permutations(range(3)))
C1_PAIR = ((0, 2, 1), (1, 0, 2))  # 132 vs 213
C2_PAIR = ((1, 2, 0), (2, 0, 1))  # 231 vs 312


def canonical_K(H, T, perm):
    return tuple(sorted((H[i], T[perm[i]]) for i in range(3)))


def distinct_matchings(H, T):
    seen = {}
    for perm in PERMS:
        K = canonical_K(H, T, perm)
        seen.setdefault(K, perm)
    return [(perm, K) for K, perm in seen.items()]


def moment(H, T, perm, r, s):
    return sum((H[i] ** r) * (T[perm[i]] ** s) for i in range(3))


def fibres(H, T):
    out = defaultdict(list)
    for perm, K in distinct_matchings(H, T):
        out[moment(H, T, perm, 1, 1)].append((perm, K))
    return out


def collision_classes(H, T):
    if len(set(H)) < 3 or len(set(T)) < 3:
        return set()
    A = H[1] - H[0]
    B = H[2] - H[1]
    C = T[1] - T[0]
    D = T[2] - T[1]
    ans = set()
    if A * C == B * D:
        ans.add("C1")
    if A * D == B * C:
        ans.add("C2")
    return ans


def power_sums(X):
    return [3, sum(X), sum(z * z for z in X),
            sum(z ** 3 for z in X), sum(z ** 4 for z in X)]


def gram3(X):
    r = power_sums(X)
    return [[r[0], r[1], r[2]],
            [r[1], r[2], r[3]],
            [r[2], r[3], r[4]]]


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def adj3(M):
    return [
        [
            M[1][1] * M[2][2] - M[1][2] * M[2][1],
            -(M[0][1] * M[2][2] - M[0][2] * M[2][1]),
            M[0][1] * M[1][2] - M[0][2] * M[1][1],
        ],
        [
            -(M[1][0] * M[2][2] - M[1][2] * M[2][0]),
            M[0][0] * M[2][2] - M[0][2] * M[2][0],
            -(M[0][0] * M[1][2] - M[0][2] * M[1][0]),
        ],
        [
            M[1][0] * M[2][1] - M[1][1] * M[2][0],
            -(M[0][0] * M[2][1] - M[0][1] * M[2][0]),
            M[0][0] * M[1][1] - M[0][1] * M[1][0],
        ],
    ]


def quadratic_coefficients(nodes, mass_sum, mixed_first, mass_square_sum):
    G = gram3(nodes)
    A = adj3(G)
    Delta = det3(G)
    qa = A[2][2]
    qb = 2 * (A[0][2] * mass_sum + A[1][2] * mixed_first)
    qc = (
        A[0][0] * mass_sum * mass_sum
        + 2 * A[0][1] * mass_sum * mixed_first
        + A[1][1] * mixed_first * mixed_first
        - Delta * mass_square_sum
    )
    return qa, qb, qc, Delta


def q21_coeffs(H, T, p11):
    return quadratic_coefficients(H, sum(T), p11, sum(t * t for t in T))


def q12_coeffs(H, T, p11):
    return quadratic_coefficients(T, sum(H), p11, sum(h * h for h in H))


def relation_states(B):
    R = set()
    roots = {}
    for a in range(-B, B + 1):
        for b in range(a, B + 1):
            key = (a + b, a * b)
            R.add(key)
            roots.setdefault(key, []).append((a, b))
    return R, roots


def class_pair(cls):
    return C1_PAIR if cls == "C1" else C2_PAIR


def class_witnesses_at_B(B, cls):
    R, roots = relation_states(B)
    Hvals = sorted({h for h, _ in R})
    Tvals = sorted({t for _, t in R})
    pair = class_pair(cls)
    out = []
    for H in combinations(Hvals, 3):
        A = H[1] - H[0]
        Bgap = H[2] - H[1]
        for T in combinations(Tvals, 3):
            C = T[1] - T[0]
            D = T[2] - T[1]
            collision = (A * C == Bgap * D) if cls == "C1" else (A * D == Bgap * C)
            if not collision:
                continue
            if all((H[i], T[perm[i]]) in R for perm in pair for i in range(3)):
                out.append((H, T))
    return out, roots


def pairable(h, t):
    disc = h * h - 4 * t
    if disc < 0:
        return False
    d = int(disc ** 0.5)
    while (d + 1) * (d + 1) <= disc:
        d += 1
    while d * d > disc:
        d -= 1
    return d * d == disc and (d - h) % 2 == 0


def main():
    checks = 0

    control_values = range(-3, 4)
    global_max = 0
    for H in combinations_with_replacement(control_values, 3):
        for T in combinations_with_replacement(control_values, 3):
            F = fibres(H, T)
            fibre_max = max(len(v) for v in F.values())
            global_max = max(global_max, fibre_max)
            assert fibre_max <= 2
            has_double = any(len(v) == 2 for v in F.values())
            classes = collision_classes(H, T)
            assert has_double == bool(classes)
            if len(set(H)) < 3 or len(set(T)) < 3:
                assert not has_double
            checks += 1
    assert global_max == 2
    collision_checks = checks

    resolvent_checks = 0
    for H in combinations(control_values, 3):
        for T in combinations(control_values, 3):
            for p11, entries in fibres(H, T).items():
                for perm, _ in entries:
                    p21 = moment(H, T, perm, 2, 1)
                    a, b, c, DeltaH = q21_coeffs(H, T, p11)
                    assert DeltaH > 0 and a > 0
                    assert a * p21 * p21 + b * p21 + c == 0

                    p12 = moment(H, T, perm, 1, 2)
                    a2, b2, c2, DeltaT = q12_coeffs(H, T, p11)
                    assert DeltaT > 0 and a2 > 0
                    assert a2 * p12 * p12 + b2 * p12 + c2 == 0
                    resolvent_checks += 2

                if len(entries) == 2:
                    xroots = sorted(moment(H, T, e[0], 2, 1) for e in entries)
                    a, b, c, _ = q21_coeffs(H, T, p11)
                    assert xroots[0] != xroots[1]
                    assert b == -a * sum(xroots)
                    assert c == a * xroots[0] * xroots[1]

                    yroots = sorted(moment(H, T, e[0], 1, 2) for e in entries)
                    a2, b2, c2, _ = q12_coeffs(H, T, p11)
                    assert yroots[0] != yroots[1]
                    assert b2 == -a2 * sum(yroots)
                    assert c2 == a2 * yroots[0] * yroots[1]
                    resolvent_checks += 4

    branch_checks = 0
    for A in range(1, 9):
        for Bgap in range(1, 9):
            for C in range(1, 9):
                for D in range(1, 9):
                    H = (0, A, A + Bgap)
                    T = (0, C, C + D)
                    if A * C == Bgap * D:
                        left, right = C1_PAIR
                        assert moment(H, T, left, 1, 1) == moment(H, T, right, 1, 1)
                        dx = moment(H, T, left, 2, 1) - moment(H, T, right, 2, 1)
                        dy = moment(H, T, left, 1, 2) - moment(H, T, right, 1, 2)
                        assert dx < 0 and dy < 0
                        branch_checks += 1
                    if A * D == Bgap * C:
                        left, right = C2_PAIR
                        assert moment(H, T, left, 1, 1) == moment(H, T, right, 1, 1)
                        dx = moment(H, T, left, 2, 1) - moment(H, T, right, 2, 1)
                        dy = moment(H, T, left, 1, 2) - moment(H, T, right, 1, 2)
                        assert dx < 0 and dy > 0
                        branch_checks += 1
    assert branch_checks == 320

    nested_counts = {"C1": [], "C2": []}
    rootbox_witnesses = {}
    for B in range(1, 7):
        for cls in ("C1", "C2"):
            W, roots = class_witnesses_at_B(B, cls)
            nested_counts[cls].append(len(W))
            if B == 6:
                assert len(W) == 1
                rootbox_witnesses[cls] = (W[0], roots)
            else:
                assert not W
    assert nested_counts == {"C1": [0, 0, 0, 0, 0, 1], "C2": [0, 0, 0, 0, 0, 1]}
    assert rootbox_witnesses["C1"][0] == ((-1, 1, 4), (-30, -12, 0))
    assert rootbox_witnesses["C2"][0] == ((-4, -1, 1), (-30, -12, 0))

    scale_checks = 0
    base = {
        "C1": ((-1, 1, 4), (-30, -12, 0)),
        "C2": ((-4, -1, 1), (-30, -12, 0)),
    }
    for cls, (H0, T0) in base.items():
        for m in range(1, 13):
            H = tuple(m * h for h in H0)
            T = tuple(m * m * t for t in T0)
            assert cls in collision_classes(H, T)
            left, right = class_pair(cls)
            assert moment(H, T, left, 1, 1) == moment(H, T, right, 1, 1)
            for perm in (left, right):
                for i in range(3):
                    assert pairable(H[i], T[perm[i]])
                    scale_checks += 1

    double_controls = 0
    for A in range(1, 9):
        for C in range(1, 9):
            H = (0, A, 2 * A)
            T = (0, C, 2 * C)
            F = fibres(H, T)
            assert sorted(len(v) for v in F.values()) == [1, 1, 2, 2]
            double_levels = sorted(p for p, v in F.items() if len(v) == 2)
            assert double_levels[1] - double_levels[0] == 2 * A * C
            double_controls += 1

    total = collision_checks + resolvent_checks + branch_checks + scale_checks + double_controls
    print(
        "PASS P000_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR "
        f"checks={total} collision={collision_checks} resolvent={resolvent_checks} "
        f"branch={branch_checks} scale={scale_checks} double_controls={double_controls} "
        "rootbox=C1:0,0,0,0,0,1|C2:0,0,0,0,0,1 "
        "fibre_max=2 selector_bits=0_or_1"
    )


if __name__ == "__main__":
    main()
