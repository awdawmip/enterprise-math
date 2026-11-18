#!/usr/bin/env python3
"""Exact Fraction checker for R284W; only auxiliary nonnegative rational Port matrices."""
from fractions import Fraction as Q
import itertools
import json
import random


def determinant(M):
    n = len(M)
    if n == 0:
        return Q(1)
    a = [[Q(v) for v in row] for row in M]
    out = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            out = -out
        v = a[k][k]
        out *= v
        for i in range(k + 1, n):
            scale = a[i][k] / v
            for j in range(k + 1, n):
                a[i][j] -= scale * a[k][j]
            a[i][k] = Q(0)
    return out


def rank(M, ncols=None):
    rows = len(M)
    cols = len(M[0]) if rows else (0 if ncols is None else ncols)
    if not cols or not rows:
        return 0
    a = [[Q(v) for v in row] for row in M]
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][c]
        for i in range(r + 1, rows):
            w = a[i][c] / v
            for j in range(c, cols):
                a[i][j] -= w * a[r][j]
        r += 1
        if r == rows:
            break
    return r


def M_at(W, edits, values):
    n = len(W)
    a = [[Q(i == j) - W[i][j] for j in range(n)] for i in range(n)]
    for (u, v), x in zip(edits, values):
        a[u][v] -= x
    return a


def cofactor_ab(M, a, b):
    sub = [[M[r][c] for c in range(len(M)) if c != a]
           for r in range(len(M)) if r != b]
    return (-1)**(a + b) * determinant(sub)


def certificate(M0, a, b, edit, other_edits):
    n = len(M0)
    u, v = edit
    if u == b or v == a:
        return {"endpoint_excluded": True, "right": True, "left": True,
                "matching": None}
    rows = [i for i in range(n) if i not in (b, u)]
    cols = [i for i in range(n) if i not in (a, v)]
    A = [[M0[r][c] for c in cols] for r in rows]
    touched_cols = {e_v for e_u, e_v in other_edits if e_u in rows and e_v in cols}
    touched_rows = {e_u for e_u, e_v in other_edits if e_u in rows and e_v in cols}
    available_cols = [i for i in range(len(cols)) if cols[i] not in touched_cols]
    available_rows = [i for i in range(len(rows)) if rows[i] not in touched_rows]
    right = bool(available_cols) and rank([[row[j] for j in available_cols] for row in A],
                                          len(available_cols)) < len(available_cols)
    left = bool(available_rows) and rank([[A[i][j] for i in available_rows] for j in range(len(cols))],
                                         len(available_rows)) < len(available_rows)
    # Deliberately compute matching independently of arithmetic rank.
    adj = [[j for j, value in enumerate(row) if value] for row in A]
    def match(i, used):
        if i == len(adj):
            return True
        for j in adj[i]:
            if j not in used and match(i+1, used | {j}):
                return True
        return False
    return {"endpoint_excluded": False, "right": bool(right), "left": bool(left),
            "matching": bool(match(0, set()))}


def canonical(v):
    if isinstance(v, Q):
        return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"
    if isinstance(v, dict):
        return {k: canonical(z) for k, z in v.items()}
    if isinstance(v, list):
        return [canonical(z) for z in v]
    return v


def four_port(t, c, delta=Q(0)):
    W = [[Q(0) for _ in range(4)] for _ in range(4)]
    W[0][1], W[0][2] = t, t + delta
    W[3][1] = W[3][2] = c
    return W


def main():
    t1, c1 = Q(1, 8), Q(1, 7)
    t2, c2 = Q(1, 10), Q(1, 9)
    delta = Q(1, 40)
    base = [four_port(t1, c1), four_port(t2, c2)]
    broken = [base[0], four_port(t2, c2, delta)]
    xs = [Q(0), Q(1, 8), Q(1, 4)]
    ys = [Q(0), Q(1, 8), Q(1, 4)]
    edits = [(2, 3), (1, 0)]
    special_tests = 0
    for pair, broken_flag in [(base, False), (broken, True)]:
        for x, y in itertools.product(xs, ys):
            Ns, Ds = [], []
            for h, W in enumerate(pair):
                t, c = [(t1, c1), (t2, c2)][h]
                d = delta if broken_flag and h == 1 else Q(0)
                M = M_at(W, edits, [x, y])
                N, D = cofactor_ab(M, 0, 1), determinant(M)
                assert N == t + c * d * x
                assert D == 1 - c*x - t*y - c*d*x*y
                assert D > 0
                Ns.append(N)
                Ds.append(D)
                special_tests += 1
            P = Ns[0]*Ds[1] - Ns[1]*Ds[0]
            if broken_flag:
                assert P == Q(1,40) - x/Q(420) + x*x/Q(2520)
            else:
                assert P == Q(1,40) + x/Q(2520)
        A = M_at(pair[1], [], [])
        cert = certificate(A, 0, 1, (2, 3), [(1, 0)])
        assert cert['matching'] is True
        assert cert['right'] == (not broken_flag)
        if not broken_flag:
            assert cert['left'] is True
    # Deterministic independent finite checks of the sufficient condition.
    gen = random.Random(28423)
    samples = 0
    checks = 0
    certified = 0
    hall_present_certified = 0
    for n in (4, 5, 6):
        for _ in range(160):
            W = [[Q(gen.randrange(3), 32*n) for j in range(n)] for i in range(n)]
            a, b = gen.randrange(n), gen.randrange(n)
            edit = (gen.randrange(n), gen.randrange(n))
            others = [(gen.randrange(n), gen.randrange(n)) for _ in range(2)]
            M0 = M_at(W, [], [])
            cert = certificate(M0, a, b, edit, others)
            samples += 1
            if cert['right'] or cert['left']:
                certified += 1
                if cert['matching'] is True:
                    hall_present_certified += 1
                for z in itertools.product((Q(0),Q(1,16)), repeat=2):
                    old = cofactor_ab(M_at(W, [edit]+others, [Q(0)]+list(z)), a,b)
                    new = cofactor_ab(M_at(W, [edit]+others, [Q(1,16)]+list(z)), a,b)
                    assert old == new, (n,a,b,edit,others,z)
                    checks += 1
    assert samples == 480
    return canonical({
        "schema":"EM_R284W_EXACT_CERTIFICATE_V1",
        "status":"PASS",
        "arithmetic":"Python Fraction, exact Gaussian elimination; seeded finite checker",
        "seed":28423,
        "witness_observation":"F_01=(I-W)^-1[0,1]",
        "witness_edits":{"x":"2->3","y":"1->0"},
        "symmetric_pair":{"model1":{"t":t1,"c":c1},"model2":{"t":t2,"c":c2},
                          "N1":"1/8", "D1":"1-x/7-y/8", "N2":"1/10", "D2":"1-x/9-y/10",
                          "P":"1/40+x/2520"},
        "broken_symmetry":{"delta":delta,"N2":"1/10+x/360",
                           "D2":"1-x/9-y/10-xy/360", "P":"1/40-x/420+x^2/2520"},
        "cofactor_support":"two rows x two columns, all 4 entries nonzero, so perfect matching",
        "right_nullvector":"(1,-1) in symmetric pair",
        "tested_xy_nodes_per_pair":9,
        "exact_determinant_cofactor_node_checks":special_tests,
        "random_matrix_cases":samples,
        "random_matrix_certificate_cases":certified,
        "hall_present_certificate_cases":hall_present_certified,
        "random_exact_observation_pair_comparisons":checks,
        "scope":"Deterministic tested finite instances; general theorem proved separately"
    })


if __name__ == '__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
