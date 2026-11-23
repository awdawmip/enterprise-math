#!/usr/bin/env python3
"""Exact rational checks for WEIGHTED_ENERGY_SHALLOW_TREES.md.

The proof, not these finite cases, carries all universal quantifiers.
No full-road or q sampling is changed, and no remote state is touched.
"""
from __future__ import annotations

from bisect import bisect_left
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent


def serialize_fraction(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal_for_reading": float(x)}


def linear(x, y, n):
    a, b = x
    qa, qb = y
    return (qa * (b - n) + qb * (n - a)) / (b - a)


def interpolate(nodes, values):
    out = {}
    for a in range(len(nodes) - 1):
        for n in range(nodes[a], nodes[a + 1] + 1):
            v = linear(nodes[a:a + 2], values[a:a + 2], n)
            assert n not in out or out[n] == v
            out[n] = v
    return out


def positive_energy(values):
    return sum((max(v, F(0)) ** 2 / n ** 2 for n, v in values.items()), F(0))


def choose_tau(delta, q2, weight_sum):
    upper2 = delta ** 2 * q2 / (4 * weight_sum)
    tau = F(1)
    while tau ** 2 > upper2:
        tau /= 2
    while 4 * tau ** 2 <= upper2:
        tau *= 2
    assert upper2 / 4 <= tau ** 2 <= upper2
    return tau


def bucket_tree(nodes, values, delta, tau):
    alpha = 1 + delta / 16
    jl, jr = values[0], values[-1]
    assert min(jl, jr) >= 0 or max(jl, jr) <= 0
    positive_j = min(jl, jr) >= 0
    scale_values = [
        (linear((nodes[0], nodes[-1]), (jl, jr), n) if positive_j else F(0)) + tau
        for n in nodes
    ]
    normalized = [q / a for q, a in zip(values, scale_values)]
    powers = [F(1)]
    while powers[-1] < max(F(1), *normalized):
        powers.append(powers[-1] * alpha)
    labels = [0 if u <= 1 else bisect_left(powers, u) for u in normalized]
    edges, insertion_order = [], []

    def construct(i, j):
        edges.append((i, j))
        if j - i == 1:
            return 0
        first = min(labels[i + 1:j])
        candidates = [k for k in range(i + 1, j) if labels[k] == first]
        k = candidates[len(candidates) // 2]
        insertion_order.append(k)
        return 1 + max(construct(i, k), construct(k, j))

    depth = construct(0, len(nodes) - 1)
    counts = Counter(labels[1:-1])
    per_bucket_depth_bound = sum(count.bit_length() for count in counts.values())
    assert depth <= per_bucket_depth_bound
    return dict(alpha=alpha, scale_values=scale_values, labels=labels,
                edges=edges, depth=depth, insertion_order=insertion_order,
                per_bucket_depth_bound=per_bucket_depth_bound,
                counts=counts)


def envelope(nodes, values, edges):
    out = {}
    for i, j in edges:
        for n in range(nodes[i], nodes[j] + 1):
            v = linear((nodes[i], nodes[j]), (values[i], values[j]), n)
            if n not in out or out[n] < v:
                out[n] = v
    return out


def check_inflation_cells():
    alphas = [F(17, 16), F(9, 8), F(3, 2), F(2)]
    endpoints = [F(-100), F(-3), F(-1), F(0), F(1), F(3), F(100)]
    cases = 0
    worst_ratio = F(1)
    witness = None
    for x, h in [(2, 1), (2, 2), (3, 2), (4, 4), (7, 5), (9, 9)]:
        ns = list(range(x, x + h + 1))
        weights = [F(1, n * n * (2 if j in (0, h) else 1))
                   for j, n in enumerate(ns)]
        floors = [[F(0) for n in ns], [F(1) for n in ns],
                  [F(3 * j, h) for j in range(h + 1)],
                  [F((3 * n + n * n) % 7, 2) for n in ns]]
        for ql in endpoints:
            for qr in endpoints:
                base = [linear((x, x + h), (ql, qr), n) for n in ns]
                for alpha in alphas:
                    yl = alpha * ql if ql > 0 else ql
                    yr = alpha * qr if qr > 0 else qr
                    inflated = [linear((x, x + h), (yl, yr), n) for n in ns]
                    for floor in floors:
                        e0 = sum((w * max(b, z, F(0)) ** 2
                                  for w, b, z in zip(weights, floor, base)), F(0))
                        e1 = sum((w * max(b, z, F(0)) ** 2
                                  for w, b, z in zip(weights, floor, inflated)), F(0))
                        assert e1 <= alpha ** 10 * e0
                        cases += 1
                        if e0 and e1 / e0 > worst_ratio:
                            worst_ratio = e1 / e0
                            witness = [x, h, str(ql), str(qr), str(alpha)]
    # The false pointwise claim must actually fail on an integer point.
    x, h, alpha = 4, 4, F(3, 2)
    midpoint_base = linear((x, x + h), (F(-100), F(100)), x + h // 2)
    midpoint_new = linear((x, x + h), (F(-100), F(150)), x + h // 2)
    assert midpoint_base == 0 and midpoint_new == 25
    return {"exact_case_count": cases, "endpoint_scheme": "half weights at both cell ends",
            "worst_observed_energy_ratio": serialize_fraction(worst_ratio),
            "worst_witness_x_h_left_right_alpha": witness,
            "false_pointwise_claim_counterexample": {
                "nodes": [4, 8], "old_values": [-100, 100], "new_values": [-100, 150],
                "integer_midpoint": 6, "old_value": 0, "new_value": 25}}


def check_one_tree(nodes, values, delta):
    final = interpolate(nodes, values)
    skeleton = {n: linear((nodes[0], nodes[-1]), (values[0], values[-1]), n)
                for n in final}
    optimum = {n: max(final[n], skeleton[n]) for n in final}
    q2 = positive_energy(optimum)
    if not q2:
        assert all(q <= 0 for q in values)
        tree = bucket_tree(nodes, values, delta, F(1))
        env = envelope(nodes, values, tree["edges"])
        assert positive_energy(env) == 0
        assert all(optimum[n] <= env[n] for n in final)
        assert env[nodes[0]] == values[0] and env[nodes[-1]] == values[-1]
        return {"zero": True, "depth": tree["depth"], "ratio": F(1)}
    weight_sum = sum((F(1, n ** 2) for n in final), F(0))
    tau = choose_tau(delta, q2, weight_sum)
    tree = bucket_tree(nodes, values, delta, tau)
    env = envelope(nodes, values, tree["edges"])
    inflated = interpolate(nodes, [tree["alpha"] * q if q > 0 else q for q in values])
    scale = interpolate(nodes, tree["scale_values"])
    assert set(env) == set(final)
    for n in final:
        assert optimum[n] <= env[n] <= max(scale[n], inflated[n])
    inflated_floor = {n: max(skeleton[n], F(0), inflated[n]) for n in final}
    assert positive_energy(inflated_floor) <= tree["alpha"] ** 10 * q2
    energy = positive_energy(env)
    assert energy <= (1 + delta) ** 2 * q2
    assert env[nodes[0]] == values[0] and env[nodes[-1]] == values[-1]
    return {"zero": False, "depth": tree["depth"], "ratio": energy / q2,
            "tau": str(tau), "delta": str(delta),
            "occupied_buckets": len(tree["counts"]),
            "per_bucket_depth_bound": tree["per_bucket_depth_bound"],
            "nodes": nodes, "values": [str(q) for q in values]}


def check_general_trees():
    rng = random.Random(2026112301)
    cases = []
    fixtures = [
        ([4, 5, 6, 7, 8], [0, -100, 100, -3, 0]),
        ([10, 11, 13, 16, 20], [100, -1000, 3, -100, 1]),
        ([10, 12, 14, 17, 20], [-100, 1, -2, 100, -3]),
        ([3, 4, 5, 6], [-100, -3, -1, 0]),
        ([6, 7, 8, 9, 10, 11, 12], [0, F(1, 10**40), 1, -100, 2, F(1, 10**50), 0]),
    ]
    for nodes, values in fixtures:
        for delta in (F(1), F(1, 2), F(1, 10)):
            cases.append(check_one_tree(nodes, list(map(F, values)), delta))
    for k in range(300):
        x = rng.randint(4, 24)
        y = rng.randint(x + 2, 2 * x)
        interior = [n for n in range(x + 1, y) if rng.randrange(3)]
        nodes = [x] + interior + [y]
        sign = 1 if k % 2 == 0 else -1
        values = [F(sign * rng.randrange(0, 10), rng.randint(1, 5))]
        for n in interior:
            exponent = rng.randrange(0, 20) if k % 11 == 0 else 0
            values.append(F(rng.randint(-40, 40), rng.randint(1, 5) * 10 ** exponent))
        values.append(F(sign * rng.randrange(0, 10), rng.randint(1, 5)))
        delta = (F(1), F(1, 2), F(1, 10))[k % 3]
        cases.append(check_one_tree(nodes, values, delta))
    nonzero = [c for c in cases if not c["zero"]]
    worst = max(nonzero, key=lambda c: c["ratio"])
    worst = dict(worst)
    worst["ratio"] = serialize_fraction(worst["ratio"])
    return {"exact_case_count": len(cases),
            "zero_positive_energy_cases": len(cases) - len(nonzero),
            "positive_and_negative_skeleton_cases_included": True,
            "all_closed_window_integers_scanned": True,
            "all_actual_chord_edges_checked": True,
            "maximum_observed_depth": max(c["depth"] for c in cases),
            "worst_observed_squared_energy_ratio_case": worst}


def check_prior_obstruction_family():
    result = []
    delta = F(1, 10)
    pointwise_factor = F(11, 10)
    for s in [8, 16, 32, 64, 128, 256, 512, 1024, 4096]:
        x, h, m = s ** 4, s ** 3, s // 2
        k = (2 * pointwise_factor * s).__floor__() + 1
        assert F(k) > 2 * pointwise_factor * s
        nodes = [x + j * h for j in range(s + 1)]
        values = [F(0)] + [F(s ** 2, k ** (m - j)) for j in range(1, m)]
        values += [F(s ** 2)] * (s - m) + [F(0)]
        assert len(nodes) == len(values)
        tau = delta * s ** 2 / 16
        tree = bucket_tree(nodes, values, delta, tau)
        if s >= 128:
            assert k >= 160
            assert tree["counts"][0] == m - 1
            assert sorted(tree["counts"].values()) == [m - 1, m]
            assert len(tree["counts"]) == 2
            assert tree["depth"] == 2 * (s.bit_length() - 1) - 1
        result.append({"s": s, "X": x, "h": h, "K": k,
                       "number_of_internal_nodes": s - 1,
                       "previous_pointwise_required_depth_at_R_11_over_10": m - 1,
                       "new_actual_tree_depth": tree["depth"],
                       "per_bucket_depth_bound": tree["per_bucket_depth_bound"],
                       "occupied_bucket_counts": {str(label): count for label, count in sorted(tree["counts"].items())},
                       "relative_root_energy_guarantee": "11/10, by analytic theorem",
                       "exact_depth_formula_for_s_at_least_128": "2 log2(s) - 1, by the two occupied bucket proof",
                       "all_integer_energy_direct_scan": False})
    return result


def main():
    results = {
        "status": "Author exact rational finite checks; not an independent Project Review",
        "scope": "Fixed-sign affine true skeleton, unchanged original nodes and endpoints",
        "proof_file": "WEIGHTED_ENERGY_SHALLOW_TREES.md",
        "source_scientific_freeze": "9fc068244e4f1117f1e75df5eb0285c6697d21d7",
        "observation_semantics": "Scalar interpolation construction on the native X6 road; no scalar replacement of X6",
        "data_cost": "Q squared and tau are computed from already supplied true nodes; the theorem gives no free acquisition or certification of arithmetic q values",
        "inflation_cells": check_inflation_cells(),
        "fixed_sign_tree_cases": check_general_trees(),
        "prior_pointwise_obstruction_family": check_prior_obstruction_family(),
    }
    results["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    results["proof_sha256_at_run"] = hashlib.sha256((ROOT / results["proof_file"]).read_bytes()).hexdigest()
    path = ROOT / "weighted_energy_tree_certificate.json"
    path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"certificate": str(path),
                      "cell_cases": results["inflation_cells"]["exact_case_count"],
                      "tree_cases": results["fixed_sign_tree_cases"]["exact_case_count"],
                      "family_depths": [(r["s"], r["new_actual_tree_depth"], r["previous_pointwise_required_depth_at_R_11_over_10"])
                                        for r in results["prior_pointwise_obstruction_family"]]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
