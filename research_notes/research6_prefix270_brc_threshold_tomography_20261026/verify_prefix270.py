#!/usr/bin/env python3
"""PREFIX-270 exact rational verification of the WBRC-T31 port-feedback theorem.

Standalone semantic checker: mirrors the Source finite positive recurrent BRC
star/potential semantics. It does NOT import/execute the Enterprise Math package,
and it does not implement a physical heartbeat Phi or signed amplitudes.
"""
from fractions import Fraction as F
from itertools import product
import json


def inv(a):
    n = len(a)
    v = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = next((i for i in range(k, n) if v[i][k]), None)
        if p is None:
            return None
        v[k], v[p] = v[p], v[k]
        factor = v[k][k]
        v[k] = [x / factor for x in v[k]]
        for i in range(n):
            if i != k:
                factor = v[i][k]
                v[i] = [x - factor * y for x, y in zip(v[i], v[k])]
    return tuple(tuple(row[n:]) for row in v)


def star(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    assert all(value >= 0 for row in a for value in row)
    r = inv([[F(i == j) - a[i][j] for j in range(n)] for i in range(n)])
    if r is None:
        return None
    h = [sum(row) for row in r]
    if any(x <= 0 for x in h):
        return None
    assert all(x >= 0 for row in r for x in row)
    assert all(sum(a[i][j] * h[j] for j in range(n)) == h[i] - 1 for i in range(n))
    return r


def add_probe(a, i, j, t):
    b = [list(row) for row in a]
    b[i][j] += t
    return tuple(tuple(row) for row in b)


def feedback_thresholds(a):
    r = star(a)
    assert r is not None
    n = len(a)
    return tuple(tuple((1 / r[j][i]) if r[j][i] else None for j in range(n))
                 for i in range(n))


def exact_string(x):
    if x is None:
        return "INFINITY"
    return f"{x.numerator}/{x.denominator}"


def test_one(a):
    n = len(a)
    r = star(a)
    assert r is not None
    thresholds = feedback_thresholds(a)
    r_rec = tuple(tuple(F(0) if thresholds[j][i] is None else 1 / thresholds[j][i]
                        for j in range(n)) for i in range(n))
    assert r_rec == r
    r_inv = inv(r_rec)
    assert r_inv is not None
    recovered = tuple(tuple(F(i == j) - r_inv[i][j] for j in range(n))
                      for i in range(n))
    assert recovered == a
    checks = 0
    for i in range(n):
        for j in range(n):
            t_star = thresholds[i][j]
            if t_star is None:
                samples = ((F(0), True), (F(1), True), (F(100), True))
            else:
                samples = ((F(0), True), (t_star / 2, True), (t_star, False), (t_star * 2, False))
            for t, expected in samples:
                observed = star(add_probe(a, i, j, t)) is not None
                assert observed == expected, (a, i, j, t, observed, expected)
                checks += 1
                if expected:
                    # Exact rank-one feedback BRC star identity.
                    b = star(add_probe(a, i, j, t))
                    den = 1 - t * r[j][i]
                    assert den > 0
                    rhs = tuple(tuple(r[x][y] + t * r[x][i] * r[j][y] / den
                                      for y in range(n)) for x in range(n))
                    assert b == rhs
    return checks


def run():
    cases = checks = 0
    counts = {}
    for n in (1, 2, 3):
        seen = set()
        count = 0
        for bits in product((0, 1), repeat=n*n):
            a = tuple(tuple(F(bits[i*n+j], 4) for j in range(n)) for i in range(n))
            # n<=3 gives each row sum <=3/4 and hence baseline stability.
            assert star(a) is not None
            checks += test_one(a)
            sig = feedback_thresholds(a)
            assert sig not in seen, (n, a)
            seen.add(sig)
            cases += 1
            count += 1
        counts[str(n)] = count
    a = ((F(0), F(1, 4)), (F(0), F(0)))
    b = ((F(1, 4), F(0)), (F(0), F(0)))
    ra, rb = star(a), star(b)
    ta, tb = feedback_thresholds(a), feedback_thresholds(b)
    assert ra == ((F(1), F(1, 4)), (F(0), F(1)))
    assert rb == ((F(4, 3), F(0)), (F(0), F(1)))
    assert ta == ((F(1), None), (F(4), F(1)))
    assert tb == ((F(3, 4), None), (None, F(1)))
    assert star(add_probe(a, 1, 0, F(4))) is None
    assert star(add_probe(b, 1, 0, F(4))) == ((F(4, 3), F(0)), (F(16, 3), F(1)))
    out = {
        "schema": "PREFIX270_EXACT_BRC_THRESHOLD_VERIFICATION_V1",
        "mode": "standalone_exact_source_semantics_mirror_not_Source_import",
        "status": "PASS",
        "finite_test_family": "all n x n entries in {0,1/4}, n in {1,2,3}",
        "baseline_matrices_checked": cases,
        "by_size": counts,
        "exact_probe_stability_checks": checks,
        "full_symbolic_quantifier_covered_by": "paper algebraic BRC feedback proof, not finite tests",
        "example_A": {
            "W": [["0", "1/4"], ["0", "0"]],
            "R": [["1", "1/4"], ["0", "1"]],
            "T_i_j": [[exact_string(x) for x in row] for row in ta]
        },
        "example_B": {
            "W": [["1/4", "0"], ["0", "0"]],
            "R": [["4/3", "0"], ["0", "1"]],
            "T_i_j": [[exact_string(x) for x in row] for row in tb]
        },
        "baseline_context_K_2_1_4": {
            "A": "UNSTABLE",
            "B": "STABLE",
            "B_star": [["4/3", "0"], ["16/3", "1"]]
        },
        "native_heartbeat_import": "NOT_EXECUTED",
        "canonical_source_import": "NOT_EXECUTED"
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run()
