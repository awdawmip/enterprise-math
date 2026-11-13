#!/usr/bin/env python3
"""Exact Fraction audit for R5 symmetric-upstream two-terminal-split no-go.
Only finite auxiliary stopping models are tested; no native X6 dynamics are computed.
"""
from fractions import Fraction as F
from itertools import product, permutations

T = F(1, 4)
A1, D1 = F(2, 5), F(1, 2)


def stream(p1, p2, q1, q2, qb, r, a2, d2):
    """Each row is (origin, label, stopping time, answer, P mass, Q mass)."""
    out = []
    for origin, p, q, a, d in (("A1", p1, q1, A1, D1), ("A2", p2, q2, a2, d2)):
        out.extend([
            (origin, "I_stop", 1, "P", F(1, 8)*p, F(1, 8)*p),
            (origin, "high", 2, "Q", F(1, 8)*(1-p)*(1-2*T), F(1, 8)*(1-p)*(1-T)),
            (origin, "J_stop", 2, "P", F(1, 8)*(1-p)*2*T*q, F(1, 8)*(1-p)*T*q),
            (origin, "tail_P", 3, "P", F(1, 8)*(1-p)*2*T*(1-q)*a, F(1, 8)*(1-p)*T*(1-q)*(1-d)),
            (origin, "tail_Q", 3, "Q", F(1, 8)*(1-p)*2*T*(1-q)*(1-a), F(1, 8)*(1-p)*T*(1-q)*d),
        ])
    out.extend([
        ("B", "J_stop", 2, "P", F(1, 4)*qb, F(1, 8)*qb),
        ("B", "tail_P", 3, "P", F(1, 4)*(1-qb), F(1, 8)*(1-qb)),
        ("C", "early_Q", 1, "Q", F(1, 2)*r, F(5, 8)*r),
        ("C", "late_P", 3, "P", F(1, 2)*(1-r), F(5, 8)*(1-r)),
    ])
    assert sum(x[4] for x in out) == sum(x[5] for x in out) == 1
    assert all(x[4] >= 0 and x[5] >= 0 for x in out)
    return out


def observation(*args):
    rows = stream(*args)
    return (
        sum(x[4] for x in rows if x[3] == "P"),
        sum(x[5] for x in rows if x[3] == "Q"),
        sum(x[2]*x[4] for x in rows),
        sum(x[2]*x[5] for x in rows),
    )


def lr(p, q, r, a, d):
    return observation(p, p, q, q, q, r, a, d)


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k*x for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def determinant(cols):
    mat = [[cols[j][i] for j in range(4)] for i in range(4)]
    total = F(0)
    for perm in permutations(range(4)):
        parity = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = F(-1 if parity % 2 else 1)
        for i in range(4):
            term *= mat[i][perm[i]]
        total += term
    return total


def chart(a, d):
    o = lr(0, 0, 0, a, d)
    b = sub(lr(1, 0, 0, a, d), o)
    c = sub(lr(0, 1, 0, a, d), o)
    f = sub(sub(sub(lr(1, 1, 0, a, d), o), b), c)
    e = sub(lr(0, 0, 1, a, d), o)
    return o, b, c, f, e


def s_row(a, d):
    den = 140*a+50*d-199
    return (
        80*(2*d+43)/den,
        -32*(10*a-91)/den,
        -20*(40*a+14*d-63)/den,
        32*(15*a+5*d-29)/den,
    )


def audit(a, d):
    o, b, c, f, e = chart(a, d)
    det = determinant((b, c, f, e))
    assert det == (199-140*a-50*d)/40960 > 0
    row = s_row(a, d)
    assert (dot(row, b), dot(row, c), dot(row, f), dot(row, e)) == (0, 0, 1, 0)
    for p, q, r in product((F(0), F(1, 2), F(1)), repeat=3):
        observed = lr(p, q, r, a, d)
        expected = add(o, add(scale(p, b), add(scale(q, c), add(scale(p*q, f), scale(r, e)))))
        assert observed == expected
        assert dot(row, sub(observed, o)) == p*q
    for p, q, r in product((0, 1), repeat=3):
        assert dot(row, sub(lr(p, q, r, a, d), o)) == p*q
    w = observation(0, 0, 1, 0, 0, 1, a, d)
    assert w == ((a+5)/16, d/32+F(13, 16), F(29, 16), F(49, 32))
    target = (160*a+74*d+135)/(4*(140*a+50*d-199))
    assert dot(row, sub(w, o)) == target < 0
    assert sum(abs(z) for z in row) == (8540-1600*a-280*d)/(199-140*a-50*d)
    lower = (160*a+74*d+135)/(4*(8540-1600*a-280*d))
    assert lower >= F(27, 6832)
    return det, w, target, lower


def main():
    grid = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))
    for a, d in product(grid, repeat=2):
        audit(a, d)
    a, d = F(1, 3), F(1, 4)
    det, witness, s, distance = audit(a, d)
    assert det == F(839, 245760)
    assert witness == (F(1, 3), F(105, 128), F(29, 16), F(49, 32))
    assert s == -F(1241, 3356)
    assert distance == F(1241, 190480)
    # At this strict-positive sample every same-(time,LR) terminal key has one answer.
    terminal_keys = [
        (1, F(1), "P"), (1, F(4, 5), "Q"),
        (2, F(2), "P"), (2, F(2, 3), "Q"),
        (3, F(8, 5), "P"), (3, F(12, 5), "Q"),
        (3, F(8, 9), "P"), (3, F(16, 3), "Q"),
        (3, F(2), "P"), (3, F(4, 5), "P"),
    ]
    for i, x in enumerate(terminal_keys):
        for y in terminal_keys[i+1:]:
            assert (x[0], x[1]) != (y[0], y[1]) or x[2] == y[2]
    print("frozen_nature_t=1/4 A1=(alpha=2/5,delta=1/2)")
    print("exact_grid_pairs=25; LR_ternary_checks=675; P_Q_normalization=PASS")
    print("symbolic_formulas=IN_RESEARCH_MD; finite_grid_not_universal_proof")
    print("admissible_example_alpha2=1/3 delta2=1/4")
    print("rank_det=", det, "FULL_witness=", witness)
    print("s_FULL_witness=", s, "s_LR=pq>=0")
    print("Linf_distance_bound_sample=", distance, "uniform_all_parameter_bound=", F(27, 6832))
    print("PASS_EXACT_R5_SECOND_SOURCE_TAIL_SPLIT_ALL_PARAMETER_NO_GO")


if __name__ == "__main__":
    main()
