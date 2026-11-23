#!/usr/bin/env python3
"""Directed exact checks for the arbitrary-skeleton shallow-tree proof.

Universal claims are proved in the accompanying Markdown, not inferred here.
Only already supplied original coordinates and original q values are used.
"""
from bisect import bisect_left
from collections import Counter
from fractions import Fraction as R
from itertools import product
import hashlib
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent


def interp_pair(xs, ys, n):
    l, r = xs
    return (ys[0] * (r - n) + ys[1] * (n - l)) / (r - l)


def interp(xs, ys):
    out = {}
    for k in range(len(xs) - 1):
        for n in range(xs[k], xs[k + 1] + 1):
            z = interp_pair(xs[k:k + 2], ys[k:k + 2], n)
            assert n not in out or out[n] == z
            out[n] = z
    return out


def energy(vals):
    return sum((max(R(0), z) ** 2 / n ** 2 for n, z in vals.items()), R(0))


def baseline(xs, ys):
    fine = interp(xs, ys)
    j = {n: interp_pair((xs[0], xs[-1]), (ys[0], ys[-1]), n) for n in fine}
    return fine, j, {n: max(fine[n], j[n]) for n in fine}


def tree_geometry(splits, last):
    edges, leaves = [], []

    def walk(i, j):
        edges.append((i, j))
        if (i, j) not in splits:
            leaves.append((i, j))
            return 0
        k = splits[(i, j)]
        assert i < k < j
        return 1 + max(walk(i, k), walk(k, j))

    return walk(0, last), edges, leaves


def envelope(xs, ys, edges):
    out = {}
    for i, j in edges:
        for n in range(xs[i], xs[j] + 1):
            z = interp_pair((xs[i], xs[j]), (ys[i], ys[j]), n)
            if n not in out or z > out[n]:
                out[n] = z
    return out


def safe_prefix(xs, ys):
    """Positive-safe prefix, reversing only index order when necessary."""
    last = len(xs) - 1
    levels = len({y for y in ys if y > 0})
    splits, records = {}, []
    if ys[0] * ys[-1] >= 0:
        return splits, {"record_count": 0, "chain_count": 0, "positive_levels": levels}
    negative_on_left = ys[0] < 0
    order = list(range(last + 1)) if negative_on_left else list(range(last, -1, -1))
    pos = last
    while ys[order[pos]] > 0:
        pos = max(k for k in range(pos) if ys[order[k]] < ys[order[pos]])
        if order[pos] not in (0, last):
            records.append(order[pos])
    assert len(records) <= levels
    anchors = sorted([0, *records, last])
    residuals = {
        k: ys[k] - interp_pair((xs[0], xs[-1]), (ys[0], ys[-1]), xs[k])
        for k in records
    }

    def coarse(i, j, candidates):
        if not candidates:
            return
        low = min(residuals[k] for k in candidates)
        ties = [k for k in candidates if residuals[k] == low]
        k = ties[len(ties) // 2]
        splits[(i, j)] = k
        coarse(i, k, [v for v in candidates if v < k])
        coarse(k, j, [v for v in candidates if v > k])

    coarse(0, last, sorted(records))
    chain_count, chain_levels = 0, []
    cross = [(i, j) for i, j in zip(anchors, anchors[1:]) if ys[i] * ys[j] < 0]
    assert len(cross) <= 1
    if cross:
        i, j = cross[0]
        while j - i > 1:
            p = ys[j] if ys[i] < 0 else ys[i]
            assert p > 0 and all(ys[k] >= p for k in range(i + 1, j))
            v = min(ys[i + 1:j])
            ties = [k for k in range(i + 1, j) if ys[k] == v]
            k = ties[0] if ys[i] < 0 else ties[-1]
            if chain_levels:
                assert v > chain_levels[-1]
            chain_levels.append(v)
            splits[(i, j)] = k
            chain_count += 1
            if ys[i] < 0:
                j = k
            else:
                i = k
    assert chain_count <= levels
    depth, edges, leaves = tree_geometry(splits, last)
    assert depth <= 2 * levels
    assert all(j - i == 1 or ys[i] * ys[j] >= 0 for i, j in leaves)
    level_ranks = {value: rank + 1 for rank, value in enumerate(sorted({y for y in ys if y > 0}))}
    return splits, {"record_count": len(records), "chain_count": chain_count,
                    "positive_levels": levels, "depth": depth,
                    "records_original_indices": records,
                    "chain_positive_height_ranks": [level_ranks[v] for v in chain_levels]}


def check_prefix(xs, ys):
    splits, info = safe_prefix(xs, ys)
    depth, edges, leaves = tree_geometry(splits, len(xs) - 1)
    fine, j, m = baseline(xs, ys)
    p = envelope(xs, ys, edges)
    assert all(max(p[n], R(0)) <= max(m[n], R(0)) for n in fine)
    assert all(p[n] >= j[n] for n in fine)
    assert p[xs[0]] == ys[0] and p[xs[-1]] == ys[-1]
    info["signed_violation_points"] = [n for n in fine if p[n] > m[n]]
    return splits, info


def choose_threshold(eps, q2, w, divisor):
    upper2 = eps ** 2 * q2 / (divisor ** 2 * w)
    t = R(1)
    while t ** 2 > upper2:
        t /= 2
    while 4 * t ** 2 <= upper2:
        t *= 2
    assert upper2 / 4 <= t ** 2 <= upper2
    return t


def quantize_positive(ys, alpha, tau):
    heights = [tau]
    while heights[-1] < max(ys):
        heights.append(heights[-1] * alpha)
    out = [y if y <= 0 else heights[bisect_left(heights, y)] for y in ys]
    for y, z in zip(ys, out):
        assert y <= z <= (alpha * y if y > 0 else y) + tau
        assert (y > 0) == (z > 0)
    return out


def complete_same_sign(xs, ys, splits, eta, tau):
    alpha = 1 + eta / 16
    _, _, leaves = tree_geometry(splits, len(xs) - 1)
    max_added_bound = 0
    for i, j in leaves:
        if j - i == 1:
            continue
        assert ys[i] * ys[j] >= 0
        positive_j = min(ys[i], ys[j]) >= 0
        scaled = {}
        for k in range(i, j + 1):
            a = tau + (interp_pair((xs[i], xs[j]), (ys[i], ys[j]), xs[k]) if positive_j else 0)
            scaled[k] = ys[k] / a
        powers = [R(1)]
        while powers[-1] < max(R(1), *scaled.values()):
            powers.append(powers[-1] * alpha)
        labels = {k: 0 if z <= 1 else bisect_left(powers, z) for k, z in scaled.items()}
        counts = Counter(labels[k] for k in range(i + 1, j))
        max_added_bound = max(max_added_bound, sum(c.bit_length() for c in counts.values()))

        def make(a, b):
            if b - a == 1:
                return
            low = min(labels[k] for k in range(a + 1, b))
            ties = [k for k in range(a + 1, b) if labels[k] == low]
            k = ties[len(ties) // 2]
            splits[(a, b)] = k
            make(a, k)
            make(k, b)

        make(i, j)
    return max_added_bound


def full_case(xs, ys, delta):
    fine, j, m = baseline(xs, ys)
    q2 = energy(m)
    assert q2 > 0
    w = sum((R(1, n ** 2) for n in fine), R(0))
    alpha, eta = 1 + delta / 64, delta / 3
    tau = choose_threshold(delta, q2, w, 4)
    hat = quantize_positive(ys, alpha, tau)
    fh, jh, mh = baseline(xs, hat)
    qh2 = energy(mh)
    assert alpha ** 10 <= 1 + delta / 4
    ya = [alpha * y if y > 0 else y for y in ys]
    fa, ja, ma = baseline(xs, ya)
    stage1 = {n: max(j[n], fa[n], R(0)) for n in fine}
    assert energy(stage1) <= alpha ** 10 * q2
    assert energy(ma) <= alpha ** 10 * energy(stage1)
    assert qh2 <= (1 + delta / 2) ** 2 * q2
    splits, info = check_prefix(xs, hat)
    prefix_depth = tree_geometry(splits, len(xs) - 1)[0]
    tau2 = choose_threshold(eta, qh2, w, 2)
    add_bound = complete_same_sign(xs, hat, splits, eta, tau2)
    depth, edges, leaves = tree_geometry(splits, len(xs) - 1)
    assert all(j - i == 1 for i, j in leaves)
    assert depth <= prefix_depth + add_bound
    actual = envelope(xs, ys, edges)
    comparison = envelope(xs, hat, edges)
    assert all(actual[n] <= comparison[n] for n in fine)
    assert all(m[n] <= actual[n] for n in fine)
    assert actual[xs[0]] == ys[0] and actual[xs[-1]] == ys[-1]
    assert energy(comparison) <= (1 + eta) ** 2 * qh2
    assert energy(actual) <= (1 + delta) ** 2 * q2
    return {"nodes": xs, "true_values": [str(y) for y in ys], "delta": str(delta),
            "prefix": info, "tree_depth": depth, "positive_levels_after_rounding": len({y for y in hat if y > 0}),
            "true_squared_energy_ratio": str(energy(actual) / q2),
            "true_squared_energy_ratio_for_reading": float(energy(actual) / q2),
            "true_endpoints_unchanged": True}


def main():
    assert 4 * 65 ** 10 < 5 * 64 ** 10
    prefix_count, max_prefix_depth, signed_violations = 0, 0, 0
    for values in product((-2, 0, 1, 2), repeat=3):
        ys = list(map(R, (-3, *values, 2)))
        for trial in (ys, list(reversed(ys))):
            _, info = check_prefix([5, 6, 7, 9, 10], trial)
            prefix_count += 1
            max_prefix_depth = max(max_prefix_depth, info.get("depth", 0))
            signed_violations += bool(info["signed_violation_points"])
    for q in (-1000, -2, 0, 1, 2, 1000):
        for ys in ([R(-3), R(q), R(2)], [R(2), R(q), R(-3)]):
            check_prefix([5, 7, 10], ys)
            prefix_count += 1
    for ys in ([R(-3), R(2)], [R(2), R(-3)], [R(0), R(2)], [R(-3), R(0)]):
        check_prefix([5, 10], ys)
        prefix_count += 1
    witness_x = [10, 11, 12, 20]
    witness_y = list(map(R, [-1000, -900, -1, 1]))
    witness_splits, witness_info = check_prefix(witness_x, witness_y)
    _, _, witness_m = baseline(witness_x, witness_y)
    witness_p = envelope(witness_x, witness_y, tree_geometry(witness_splits, 3)[1])
    assert witness_p[11] == R(-1001, 2) and witness_m[11] == R(-8999, 10)
    assert witness_p[11] > witness_m[11] and max(witness_p[11], 0) == max(witness_m[11], 0) == 0
    prefix_count += 1
    fixtures = [
        ([10, 11, 12, 20], [-1000, -900, -1, 1]),
        ([8, 9, 10, 11, 12, 14, 16], [-10**50, 1, 1, 1, 1, 1, 2]),
        ([8, 9, 10, 11, 12, 14, 16], [-1, 100, 10, 1, R(1, 100), R(1, 10**50), 1]),
        ([6, 7, 8, 9, 10, 11, 12], [-100, 1, 3, 1, 0, 3, 2]),
        ([5, 7, 10], [-3, 1000, 2]),
        ([5, 7, 10], [-3, -1000, 2]),
        ([5, 10], [-3, 2]),
        ([5, 7, 10], [0, -1000, 2]),
        ([5, 7, 10], [-3, 1000, 0]),
        ([5, 6, 8, 10], [1, -1000, 2, 3]),
    ]
    cases = []
    for xs, values in fixtures:
        ys = list(map(R, values))
        for trial in (ys, list(reversed(ys))):
            for delta in (R(1), R(1, 4), R(1, 10)):
                cases.append(full_case(xs, trial, delta))
    rng = random.Random(2026112302)
    for k in range(36):
        x = rng.randrange(4, 16)
        xs = [x] + [n for n in range(x + 1, 2 * x) if rng.randrange(3) == 0] + [2 * x]
        ys = [R(-rng.randrange(1, 10))]
        ys += [R(rng.randrange(-10, 11), rng.randrange(1, 5)) for n in xs[1:-1]]
        ys += [R(rng.randrange(1, 10))]
        if k % 2:
            ys.reverse()
        cases.append(full_case(xs, ys, (R(1), R(1, 4), R(1, 10))[k % 3]))
    result = {
        "status": "Author exact rational checks; not an independent Project Review",
        "scientific_semantics": "Unchanged native X6 scalar observations, original coordinates and true endpoint values",
        "data_cost": "All values are supplied original nodes; quantization selects a tree and is not a physical q correction or a new query",
        "prefix_cases": prefix_count,
        "maximum_prefix_depth_in_exhaustive_small_family": max_prefix_depth,
        "positive_safe_but_not_signed_safe_cases_in_exhaustive_family": signed_violations,
        "explicit_positive_safety_witness": {"nodes": witness_x, "values": [str(y) for y in witness_y],
            "point": 11, "prefix_value": str(witness_p[11]), "M_value": str(witness_m[11]),
            "positive_parts_both_zero": True, "prefix": witness_info},
        "full_construction_cases": len(cases),
        "maximum_full_depth": max(c["tree_depth"] for c in cases),
        "maximum_observed_true_squared_energy_ratio": max(c["true_squared_energy_ratio_for_reading"] for c in cases),
        "all_small_closed_window_integers_checked": True,
        "all_actual_and_comparison_tree_edges_checked": True,
        "cases": cases,
    }
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    proof = ROOT / "GENERAL_WEIGHTED_ENERGY_SHALLOW_TREES.md"
    result["proof_sha256_at_run"] = hashlib.sha256(proof.read_bytes()).hexdigest()
    path = ROOT / "general_weighted_tree_certificate.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"certificate": str(path), "prefix_cases": prefix_count,
                      "full_construction_cases": len(cases),
                      "maximum_full_depth": result["maximum_full_depth"],
                      "maximum_observed_true_squared_energy_ratio": result["maximum_observed_true_squared_energy_ratio"]}))


if __name__ == "__main__":
    main()
