#!/usr/bin/env python3
"""Exact symbolic certificate for R762CS. Requires SymPy; no floating arithmetic."""
import itertools
import json
from collections import Counter
import sympy as sp

EDGES = ("01", "02", "03", "12", "13", "23")
FULL = 63
TRIADS = sorted({min(sum(1 << a for a in t), FULL ^ sum(1 << a for a in t))
                 for t in itertools.combinations(range(6), 3)})
INDEX = {m: i for i, m in enumerate(TRIADS)}
STAR = {min(sum(1 << a for a, e in enumerate(EDGES) if str(v) in e),
            FULL ^ sum(1 << a for a, e in enumerate(EDGES) if str(v) in e))
        for v in range(4)}
F = [int(m in STAR) for m in TRIADS]
P = [1 - x for x in F]


def partitions():
    def rec(a, maximum):
        if len(a) == 6:
            yield a
        else:
            for j in range(maximum + 2):
                yield from rec(a + (j,), max(maximum, j))
    return list(rec((0,), 0))


def normalize(labels):
    renamed = {}
    return tuple(renamed.setdefault(t, len(renamed)) for t in labels)


def edge_actions():
    actions = []
    for v in itertools.permutations(range(4)):
        actions.append(tuple(EDGES.index("".join(map(str, sorted((v[int(e[0])], v[int(e[1])])))))
                             for e in EDGES))
    return actions


def transform_partition(partition, action):
    transformed = [None] * 6
    for old, new in enumerate(action):
        transformed[new] = partition[old]
    return normalize(transformed)


def adjacency(partition):
    rows = []
    for mask in TRIADS:
        row = []
        for x in range(6):
            if mask & (1 << x):
                for y in range(6):
                    if not mask & (1 << y) and partition[x] == partition[y]:
                        next_mask = mask ^ (1 << x) ^ (1 << y)
                        row.append((INDEX[min(next_mask, FULL ^ next_mask)], partition[x]))
        rows.append(row)
    return rows


def observations(rows, weights, depth):
    f, p = [sp.Integer(x) for x in F], [sp.Integer(x) for x in P]
    out = [(f, p)]
    for _ in range(depth):
        f = [sp.expand(sum(weights[j] * f[k] for k, j in row)) for row in rows]
        p = [sp.expand(sum(weights[j] * p[k] for k, j in row)) for row in rows]
        out.append((f, p))
    return out


def impossible_positive_linear(poly, variables):
    # A nonzero homogeneous linear equation with all coefficients of one sign
    # has no solution when every source weight is strictly positive.
    q = sp.Poly(poly, *variables)
    if q.total_degree() != 1 or q.coeff_monomial(1) != 0:
        return False
    coeffs = [q.coeff_monomial(x) for x in variables]
    return (all(c >= 0 for c in coeffs) and any(c > 0 for c in coeffs)) or (all(c <= 0 for c in coeffs) and any(c < 0 for c in coeffs))


def exact_symbolic_certificate():
    pats = partitions()
    assert len(pats) == 203 and len(TRIADS) == 10 and sum(F) == 4
    actions = edge_actions()
    reps = sorted({min(transform_partition(p, a) for a in actions) for p in pats})
    assert len(actions) == 24 and len(reps) == 25
    checks = Counter()
    for part in reps:
        variables = sp.symbols("w0:" + str(max(part) + 1))
        obs = observations(adjacency(part), variables, 8)
        for i, j in itertools.combinations(range(10), 2):
            if F[i] != F[j]:
                continue
            checks["pairs"] += 1
            differences = [sp.expand(obs[h][c][i] - obs[h][c][j])
                           for h in (1, 2) for c in (0, 1)]
            if all(q == 0 for q in differences):
                assert all(obs[h][c][i] == obs[h][c][j]
                           for h in range(3, 9) for c in (0, 1))
                checks["identical_polynomials"] += 1
            elif any(impossible_positive_linear(q, variables)
                     for q in differences[:2] if q != 0):
                checks["positive_infeasible"] += 1
            else:
                basis = sp.groebner([q for q in differences if q != 0],
                                    *variables, order="grlex")
                for h in range(3, 9):
                    for c in (0, 1):
                        delta = sp.expand(obs[h][c][i] - obs[h][c][j])
                        assert basis.reduce(delta)[1] == 0, (part, i, j, h, c)
                checks["ideal_certified"] += 1
    assert dict(checks) == {"pairs": 525, "identical_polynomials": 235,
                            "positive_infeasible": 244, "ideal_certified": 46}
    return ["".join(map(str, p)) for p in reps], dict(checks)


def numeric_audit(max_weight=5):
    counts = Counter()
    total = 0
    for part in partitions():
        rows = adjacency(part)
        for weights in itertools.product(range(1, max_weight + 1),
                                         repeat=max(part) + 1):
            v = observations_numeric(rows, weights)
            classes = [len({tuple(v[i][:depth + 1]) for i in range(10)})
                       for depth in range(3)]
            needed = next(h for h in range(3) if classes[h] == classes[2])
            counts[needed] += 1
            total += 1
    assert total == 115155 and dict(counts) == {0: 15635, 1: 99280, 2: 240}
    return total, dict(counts)


def observations_numeric(rows, weights):
    f, p = F[:], P[:]
    out = [[(f[i], p[i])] for i in range(10)]
    for _ in range(2):
        f = [sum(weights[j] * f[t] for t, j in row) for row in rows]
        p = [sum(weights[j] * p[t] for t, j in row) for row in rows]
        for i in range(10):
            out[i].append((f[i], p[i]))
    return out


def witness():
    part, weights = (0, 0, 1, 1, 1, 2), (2, 1, 1)
    z = observations_numeric(adjacency(part), weights)
    assert z[2][0] == z[6][0]
    assert z[2][1] == z[6][1] == (2, 2)
    assert z[2][2] == (2, 14) and z[6][2] == (4, 12)
    return {"partition": "001112", "weights": list(weights),
            "state_indices": [2, 6], "state_masks": [TRIADS[2], TRIADS[6]],
            "O1": list(z[2][1]), "O2": [list(z[2][2]), list(z[6][2])]}


if __name__ == "__main__":
    representatives, proof_counts = exact_symbolic_certificate()
    total, depth = numeric_audit()
    print(json.dumps({
        "schema": "EM_R762CS_TWO_STEP_ALL_POSITIVE_BRC_CERTIFICATE_V1",
        "proposition": "O2 equality is equivalent to all-future F/P equality for every positive real source class weight on any partition of six named K4 edges",
        "scope": "conditional source-matched cross-triad swaps; weighted positive N-BRC, not native signed TRIADIC_CLOSURE_E licence",
        "theoretical_horizon": 8,
        "partition_orbits_under_vertex_S4": len(representatives),
        "canonical_partition_representatives": representatives,
        "exact_symbolic_pair_checks": proof_counts,
        "finite_integer_audit": {"weights_per_class": "1..5", "assignments": total,
                                 "minimal_observation_depth_histogram": depth},
        "sharpness_witness": witness(),
        "arithmetic": "exact SymPy rational polynomial ideals and Python integers; no floating-point",
        "independent_review": "NOT_REVIEWED"
    }, ensure_ascii=False, indent=2))
