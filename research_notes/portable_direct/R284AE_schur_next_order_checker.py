#!/usr/bin/env python3
"""R284AE exact first-two-graded-parts checker: SymPy, fixed seed, no floats."""
import json
from pathlib import Path
from random import Random
from itertools import combinations
import sympy as s

rng = Random(284020)


def change(A):
    n = A.rows
    r = A.rank()
    d = n - r
    for rs in combinations(range(n), r):
        for cs in combinations(range(n), r):
            if A.extract(rs, cs).det() != 0:
                break
        else:
            continue
        break
    rows = tuple(rs) + tuple(i for i in range(n) if i not in rs)
    cols = tuple(cs) + tuple(i for i in range(n) if i not in cs)
    P = s.eye(n).extract(rows, tuple(range(n)))
    Q = s.eye(n).extract(tuple(range(n)), cols)
    T = P * A * Q
    B = T[:r, :r]
    D, E = T[r:, :r], T[:r, r:]
    left = s.BlockMatrix([
        [s.eye(r), s.zeros(r, d)],
        [-D * B.inv(), s.eye(d)]
    ]).as_explicit() * P
    right = Q * s.BlockMatrix([
        [s.eye(r), -B.inv() * E],
        [s.zeros(d, r), s.eye(d)]
    ]).as_explicit()
    assert left * A * right == s.diag(B, s.zeros(d, d))
    return left, right, B, P.det() * Q.det() * B.det()


def homog(expr, symbols, degree):
    poly = s.Poly(s.expand(expr), *symbols)
    return s.expand(sum(
        coef * s.prod(x ** e for x, e in zip(symbols, mon))
        for mon, coef in poly.terms() if sum(mon) == degree
    ))


def trial(n, r, rep):
    while True:
        base = (s.Matrix(n, r, lambda i, j: rng.randint(1, 4)) *
                s.Matrix(r, n, lambda i, j: rng.randint(1, 4)))
        if base.rank() == r:
            break
    m = min(n + 1, 4)
    all_edges = [(i, j) for i in range(n) for j in range(n)]
    rng.shuffle(all_edges)
    edges = all_edges[:m]
    t = s.symbols("t0:" + str(m))
    left, right, B, gamma = change(base)
    d = n - r
    X = s.zeros(r)
    Y = s.zeros(r, d)
    Z = s.zeros(d, r)
    M = s.zeros(d)
    real = base.copy()
    for v, (i, j) in zip(t, edges):
        real[i, j] += v
        u = left[:, i]
        w = right[j, :]
        term = v * u * w
        X += term[:r, :r]
        Y += term[:r, r:]
        Z += term[r:, :r]
        M += term[r:, r:]
    true = real.det(method="bareiss")
    one = gamma * M.det()
    next_ = gamma * (s.trace(B.inv() * X) * M.det() -
                     s.trace(M.adjugate() * Z * B.inv() * Y))
    assert s.expand(homog(true, t, d) - one) == 0, (n, r, rep, "leading")
    assert s.expand(homog(true, t, d + 1) - next_) == 0, (n, r, rep, "next")
    for expr in (one, next_):
        poly = s.Poly(expr, *t)
        assert all(all(power <= 1 for power in mon)
                   for mon, _ in poly.terms())
    return bool(s.expand(next_)), bool(s.expand(one))


def run():
    counts = {
        "rank_pairs": 0,
        "generated_cases": 0,
        "leading_degree_checked": 0,
        "next_degree_checked": 0,
        "multi_affinity_checks": 0,
        "nonzero_next_degree_cases": 0,
        "no_leading_but_nonzero_next_cases": 0,
    }
    for n in range(2, 6):
        for r in range(1, n):
            counts["rank_pairs"] += 1
            for rep in range(4):
                hasnext, hasleading = trial(n, r, rep)
                counts["generated_cases"] += 1
                counts["leading_degree_checked"] += 1
                counts["next_degree_checked"] += 1
                counts["multi_affinity_checks"] += 2
                counts["nonzero_next_degree_cases"] += int(hasnext)
                counts["no_leading_but_nonzero_next_cases"] += int(hasnext and not hasleading)
    c = s.Rational(1, 192)
    C0 = c * s.Matrix([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    L, R, B, gamma = change(C0)
    t, u = s.symbols("t u")
    d, r = 1, 2
    X = s.zeros(r)
    Y = s.zeros(r, d)
    Z = s.zeros(d, r)
    M = s.zeros(d)
    for value, (i, j) in zip((t, u), [(1, 0), (0, 1)]):
        term = value * L[:, i] * R[j, :]
        X += term[:r, :r]
        Y += term[:r, r:]
        Z += term[r:, :r]
        M += term[r:, r:]
    assert M == s.zeros(1)
    q2 = s.expand(-gamma * s.trace(Z * B.inv() * Y))
    assert s.expand(q2 + c * t * u) == 0
    return {
        "schema": "R284AE_SCHUR_NEXT_GRADED_COEFFICIENT_V1",
        "status": "PASS",
        "seed": 284020,
        "exact_arithmetic": "SymPy Rational, no floating point",
        "domain": "n=2..5, r=1..n-1, 4 seeded positive rank-r matrix factorizations each, m=min(n+1,4) distinct named edits",
        "counts": counts,
        "positive_port_corank_one_quadratic": "-t*u/192",
        "physical_native_BRC_experiment": False,
        "independent_review": False,
    }


if __name__ == "__main__":
    data = run()
    Path(__file__).with_name("R284AE_schur_next_order_verification.json").write_text(
        json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8")
    print(json.dumps(data, sort_keys=True))
