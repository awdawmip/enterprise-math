#!/usr/bin/env python3
"""R020 P021 dynamic-completeness focused finite oracle.

Standalone research evidence only. No repository/canonical semantics are modified.
All searches are bounded and exact over finite simple relations/functions.
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

def all_relations(n: int):
    edges = tuple((i, j) for i in range(n) for j in range(n))
    return [
        frozenset(edge for k, edge in enumerate(edges) if (mask >> k) & 1)
        for mask in range(1 << (n * n))
    ]

def compose(R, S):
    return frozenset((x, z) for x, y in R for y2, z in S if y == y2)

def path_count(R, S):
    return sum(1 for x, y in R for y2, z in S if y == y2)

def rel_json(R):
    return [list(edge) for edge in sorted(R)]

def find_min_equal_cardinality_diff_composed_support(max_n=2):
    for n in range(1, max_n + 1):
        rels = all_relations(n)
        systems = [(R, S, (len(R), len(S)), bool(compose(R, S))) for R in rels for S in rels]
        by_counts = {}
        for R, S, counts, support in systems:
            key = counts
            if key in by_counts and by_counts[key][2] != support:
                R0, S0, support0 = by_counts[key]
                return {
                    "minimum_states": n,
                    "system_a": {"R": rel_json(R0), "S": rel_json(S0), "counts": list(counts),
                                 "composed_support": rel_json(compose(R0, S0))},
                    "system_b": {"R": rel_json(R), "S": rel_json(S), "counts": list(counts),
                                 "composed_support": rel_json(compose(R, S))},
                    "one_state_failure_absent": n > 1,
                }
            by_counts.setdefault(key, (R, S, support))
    return None

def find_min_same_counts_same_fine_support_diff_paths(max_n=3):
    for n in range(1, max_n + 1):
        rels = all_relations(n)
        seen = {}
        for R in rels:
            for S in rels:
                C = compose(R, S)
                if not C:
                    continue
                key = (len(R), len(S), C)
                pc = path_count(R, S)
                if key in seen and seen[key][2] != pc:
                    R0, S0, pc0 = seen[key]
                    return {
                        "minimum_states": n,
                        "counts": [len(R), len(S)],
                        "identical_fine_composed_support": rel_json(C),
                        "system_a": {"R": rel_json(R0), "S": rel_json(S0), "path_count": pc0},
                        "system_b": {"R": rel_json(R), "S": rel_json(S), "path_count": pc},
                    }
                seen[key] = (R, S, pc)
    return None

def outdegree(R, n):
    return tuple(sum((i, j) in R for j in range(n)) for i in range(n))

def find_min_uniform_one_step_support_loses_uniformity(max_n=3):
    for n in range(1, max_n + 1):
        rels = []
        for R in all_relations(n):
            deg = outdegree(R, n)
            if deg and deg[0] > 0 and len(set(deg)) == 1:
                rels.append(R)
        for R in rels:
            for S in rels:
                C = compose(R, S)
                if len(set(outdegree(C, n))) > 1:
                    return {
                        "minimum_states": n,
                        "R": rel_json(R),
                        "R_outsupport_sizes": list(outdegree(R, n)),
                        "S": rel_json(S),
                        "S_outsupport_sizes": list(outdegree(S, n)),
                        "composite": rel_json(C),
                        "composite_outsupport_sizes": list(outdegree(C, n)),
                    }
    return None

def canonical_partitions(n):
    out = []
    def rec(i, arr, mx):
        if i == n:
            out.append(tuple(arr))
            return
        for v in range(mx + 2):
            rec(i + 1, arr + [v], max(mx, v))
    if n:
        rec(1, [0], 0)
    return out

def horizon_constant(q, f, o, h):
    n = len(q)
    for i in range(n):
        for j in range(n):
            if q[i] != q[j]:
                continue
            xi, xj = i, j
            for _t in range(h + 1):
                if o[xi] != o[xj]:
                    return False
                xi, xj = f[xi], f[xj]
    return True

def find_min_future_language_separation(max_n=4):
    for n in range(1, max_n + 1):
        for q in canonical_partitions(n):
            if len(set(q)) == n:
                continue
            for f in product(range(n), repeat=n):
                for o in product(range(2), repeat=n):
                    if horizon_constant(q, f, o, 1) and not horizon_constant(q, f, o, 2):
                        return {
                            "minimum_states": n,
                            "q": list(q),
                            "f": list(f),
                            "observable": list(o),
                            "exact_for_horizon": 1,
                            "fails_at_horizon": 2,
                        }
    return None

def surjective_labelings(n):
    for k in range(1, n + 1):
        for q in product(range(k), repeat=n):
            if set(q) == set(range(k)):
                yield k, q

def fibre(q, a):
    return frozenset(i for i, x in enumerate(q) if x == a)

def fine_img(A, f):
    return frozenset(f[x] for x in A)

def coarse_support(A, q):
    return frozenset(q[x] for x in A)

def qrel_row(q, f, a):
    return coarse_support(fine_img(fibre(q, a), f), q)

def exact_two(q, f, a):
    return coarse_support(fine_img(fine_img(fibre(q, a), f), f), q)

def naive_two(q, f, a):
    result = set()
    for b in qrel_row(q, f, a):
        result |= set(qrel_row(q, f, b))
    return frozenset(result)

def quotient_saturation_stats(max_n=3):
    by_n = []
    first = None
    total_trials = total_failures = 0
    for n in range(1, max_n + 1):
        trials = failures = 0
        for k, q in surjective_labelings(n):
            for f in product(range(n), repeat=n):
                for a in range(k):
                    trials += 1
                    exact = exact_two(q, f, a)
                    naive = naive_two(q, f, a)
                    if exact != naive:
                        failures += 1
                        if first is None:
                            first = {
                                "n": n, "k": k, "q": list(q), "f": list(f), "start_label": a,
                                "one_step": sorted(qrel_row(q, f, a)),
                                "exact_two_step": sorted(exact),
                                "naive_two_step": sorted(naive),
                            }
        by_n.append({"n": n, "trials": trials, "failures": failures})
        total_trials += trials
        total_failures += failures
    return {
        "by_n": by_n,
        "total_trials": total_trials,
        "total_failures": total_failures,
        "first_failure": first,
    }

def dot(l, r):
    return sum(a * b for a, b in zip(l, r))

def delta(l, r):
    return len(l) * dot(l, r) - sum(l) * sum(r)

def pair_delta(l, r):
    return sum(
        (l[i] - l[j]) * (r[i] - r[j])
        for i in range(len(l)) for j in range(i + 1, len(l))
    )

def uniform(v):
    return len(set(v)) == 1

def profile_stats(max_m=4, max_entry=3):
    rows = []
    nonuniform_example = None
    for m in range(1, max_m + 1):
        profiles = list(product(range(max_entry + 1), repeat=m))
        total = identity_fail = uniform_cases = uniform_fail = nonuniform_zero = 0
        for l in profiles:
            for r in profiles:
                total += 1
                if delta(l, r) != pair_delta(l, r):
                    identity_fail += 1
                if uniform(l) or uniform(r):
                    uniform_cases += 1
                    if delta(l, r) != 0:
                        uniform_fail += 1
                elif delta(l, r) == 0:
                    nonuniform_zero += 1
                    if nonuniform_example is None:
                        nonuniform_example = {
                            "l": list(l), "r": list(r), "m": m,
                            "L": sum(l), "R": sum(r), "N": dot(l, r), "Delta": 0,
                        }
        rows.append({
            "m": m, "profile_pairs": total, "delta_identity_failures": identity_fail,
            "uniform_side_cases": uniform_cases, "uniform_side_delta_nonzero": uniform_fail,
            "both_nonuniform_delta_zero": nonuniform_zero,
        })
    return {"by_m": rows, "first_both_nonuniform_delta_zero": nonuniform_example}

def matmul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def block_sig(A, part, i):
    return tuple(sum(A[i][j] for j in cell) for cell in part)

def equitable(A, part):
    return all(len({block_sig(A, part, i) for i in cell}) == 1 for cell in part)

def quotient(A, part):
    return tuple(block_sig(A, part, cell[0]) for cell in part)

def equitable_product_check():
    part = ((0, 1), (2,))
    mats = []
    for vals in product(range(2), repeat=9):
        A = tuple(tuple(vals[3*i+j] for j in range(3)) for i in range(3))
        if equitable(A, part):
            mats.append(A)
    failures = 0
    for A in mats:
        QA = quotient(A, part)
        for B in mats:
            QB = quotient(B, part)
            AB = matmul(A, B)
            if not equitable(AB, part) or quotient(AB, part) != matmul(QA, QB):
                failures += 1
                return {"equitable_matrices": len(mats), "matrix_pairs": len(mats) ** 2, "failures": failures}
    return {"equitable_matrices": len(mats), "matrix_pairs": len(mats) ** 2, "failures": 0}

def support(A):
    return tuple(tuple(v > 0 for v in row) for row in A)

def bool_product(A, B):
    n = len(A)
    return tuple(tuple(any(A[i][k] and B[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def positive_support_product_check():
    mats = []
    for vals in product(range(3), repeat=4):
        mats.append((vals[:2], vals[2:]))
    failures = 0
    for A in mats:
        for B in mats:
            if support(matmul(A, B)) != bool_product(support(A), support(B)):
                failures += 1
                return {"matrix_pairs": len(mats) ** 2, "failures": failures}
    return {"matrix_pairs": len(mats) ** 2, "failures": 0}

def main():
    result = {
        "equal_cardinality_different_composed_support": find_min_equal_cardinality_diff_composed_support(),
        "same_counts_same_fine_support_different_paths": find_min_same_counts_same_fine_support_diff_paths(),
        "uniform_one_step_support_loses_uniformity": find_min_uniform_one_step_support_loses_uniformity(),
        "future_language_horizon_separation": find_min_future_language_separation(),
        "quotient_saturation_composition": quotient_saturation_stats(),
        "coupling_defect_profiles": profile_stats(),
        "equitable_count_quotient": equitable_product_check(),
        "positive_support_semiring_shadow": positive_support_product_check(),
    }
    out = Path(__file__).with_name("r020_p021_dynamic_completeness_results.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
