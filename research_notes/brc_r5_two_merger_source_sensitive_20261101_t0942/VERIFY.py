#!/usr/bin/env python3
"""Exact independent Fraction checks for the R5 double-merger source-sensitive cube.

All four terminal W probabilities are rational in the finite regression grid.
The all-real cube theorem is proved algebraically in RESEARCH.md, not by sampling.
"""
from fractions import Fraction as F
from itertools import product

SOURCES = ("A", "B")
Q_U = {"A": F(1, 4), "B": F(1, 2)}
P_U = {"A": F(1, 8), "B": F(1, 4)}
LR_KEYS = ("c", "l", "hA", "hB")
FULL_KEYS = ("cA", "cB", "lA", "hA", "lB", "hB")
CENTER = (F(3, 4), F(1, 4), F(1, 4), F(3, 4))
EPS = F(1, 32)


def observed(policy, terminal, lr):
    pA, pB, qA, qB = terminal
    pw = {"A": pA, "B": pB}
    qw = {"A": qA, "B": qB}
    # P(error) := P(final response is 1); Q(error) := Q(response is 0).
    eP, eQ, TP, TQ = F(0), F(1), F(1), F(1)
    for s in SOURCES:
        c = policy["c"] if lr else policy["c" + s]
        if not c:
            continue
        TP += F(1, 2) * 2
        TQ += F(1, 2) * 2
        for low in (True, False):
            pm = F(1, 2) * (P_U[s] if low else 1 - P_U[s])
            qm = F(1, 2) * (Q_U[s] if low else 1 - Q_U[s])
            a = policy["l" if low else "h" + s] if lr else policy[("l" if low else "h") + s]
            if a:
                eP += pm * pw[s]
                eQ -= qm * qw[s]
                TP += pm
                TQ += qm
    return (eP, eQ, TP, TQ)


def det4(matrix):
    m = [[F(x) for x in row] for row in matrix]
    value = F(1)
    for j in range(4):
        pivot = next((i for i in range(j, 4) if m[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            value = -value
        p = m[j][j]
        value *= p
        for i in range(j + 1, 4):
            factor = m[i][j] / p
            for k in range(j + 1, 4):
                m[i][k] -= factor * m[j][k]
            m[i][j] = F(0)
    return value


def rank_minor(terminal):
    # Four linearly independent differences from the first LR vertex.
    keys = ((0, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 1),
            (1, 0, 1, 0), (1, 1, 0, 0))
    vertices = [observed(dict(zip(LR_KEYS, v)), terminal, True) for v in keys]
    return det4([[a - b for a, b in zip(vertex, vertices[0])]
                 for vertex in vertices[1:]])


def contrast(terminal):
    pA, pB, qA, qB = terminal
    return (F(1, 16)*pA - F(1, 8)*qA,
            F(7, 16)*pA - F(3, 8)*qA,
            F(1, 8)*pB - F(1, 4)*qB,
            F(3, 8)*pB - F(1, 4)*qB)


def sign_and_formula(terminal):
    la, ha, lb, hb = contrast(terminal)
    assert la >= F(5, 512) and ha >= F(107, 512)
    assert lb <= -F(37, 256) and hb <= -F(19, 256)
    assert la + lb <= -F(63, 512)
    det = rank_minor(terminal)
    pA, pB, qA, qB = terminal
    symbolic_det = (pA*qA + 9*pA*qB - 9*pB*qA - pB*qB) / 128
    assert det == symbolic_det and det >= F(63, 2048)
    return la, ha, det


def run():
    # Both P and Q measures assign positive masses to each preterminal path.
    for src in SOURCES:
        assert 0 < Q_U[src] < 1 and 0 < P_U[src] < 1
    assert sum(F(1, 2) * x for s in SOURCES for x in (P_U[s], 1-P_U[s])) == 1
    assert sum(F(1, 2) * x for s in SOURCES for x in (Q_U[s], 1-Q_U[s])) == 1
    assert P_U["A"]/Q_U["A"] == P_U["B"]/Q_U["B"] == F(1, 2)
    assert (1-P_U["A"])/(1-Q_U["A"]) == F(7, 6)
    assert (1-P_U["B"])/(1-Q_U["B"]) == F(3, 2)

    count = 0
    for displacements in product((-EPS, F(0), EPS), repeat=4):
        terminal = tuple(x + y for x, y in zip(CENTER, displacements))
        assert all(0 < p < 1 for p in terminal)
        la, ha, d = sign_and_formula(terminal)
        lr = [observed(dict(zip(LR_KEYS, bits)), terminal, True)
              for bits in product((0, 1), repeat=4)]
        full = [observed(dict(zip(FULL_KEYS, bits)), terminal, False)
                for bits in product((0, 1), repeat=6)]
        jlr = max(x[0] + x[1] for x in lr)
        jfull = max(x[0] + x[1] for x in full)
        assert jlr == 1 + ha and jfull == 1 + ha + la
        assert jfull - jlr == la >= F(5, 512)
        count += len(lr) + len(full)

    assert rank_minor(CENTER) == F(9, 256)
    assert rank_minor((F(23,32), F(9,32), F(9,32), F(23,32))) == F(63,2048)
    lr_best = observed(dict(zip(LR_KEYS, (1, 0, 1, 0))), CENTER, True)
    full_best = observed(dict(zip(FULL_KEYS, (1, 0, 1, 1, 0, 0))), CENTER, False)
    assert lr_best == (F(21,64), F(29,32), F(55,16), F(27,8))
    assert full_best == (F(3,8), F(7,8), F(5,2), F(5,2))
    assert lr_best[0]+lr_best[1] == F(79,64)
    assert full_best[0]+full_best[1] == F(5,4)
    print("INPUT_TWO_MERGER_TRUE_LR_KEYS: t1={1}, t3.low={1/2}, t3.highA={7/6}, t3.highB={3/2}")
    print("FINITE_REGRESSION: 81 terminal P/Q kernel choices, 16 LR + 64 FULL deterministic policies each")
    print("EXACT_POLICY_OBSERVATIONS_CHECKED:", count)
    print("CENTER_LR_MAX_J=79/64 FULL_MAX_J=5/4 GAP=1/64")
    print("CENTER_FULL_WITNESS=(3/8,7/8,5/2,5/2)")
    print("RANK4_MINOR_CENTER=9/256; ALL_REAL_CUBE_MINOR_LOWER_BOUND=63/2048")
    print("ALL_REAL_CUBE_GAP_LOWER_BOUND=5/512 (analytic proof, not sampled extrapolation)")
    print("PASS_EXACT_R5_TWO_GENUINE_MERGERS_SOURCE_SENSITIVE_CUBE_NO_GO")


if __name__ == "__main__":
    run()
