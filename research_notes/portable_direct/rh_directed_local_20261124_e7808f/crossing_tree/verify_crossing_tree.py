#!/usr/bin/env python3
"""Exact rational checks of the crossing-skeleton construction.

The all-parameter theorem is proved in PROOF.md. This checker exercises
its prefix, comparison-data transfer, and complete-integer energy claims.
Only Python's standard library is used.
"""
from fractions import Fraction as F
from pathlib import Path
from random import Random
import json


def line(xa, ya, xb, yb, x):
    return ya + (yb - ya) * F(x - xa, xb - xa)


def interp(xs, ys, x):
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            return line(xs[i], ys[i], xs[i + 1], ys[i + 1], x)
    raise ValueError("point outside node range")


def log2_ceiling_integer(n):
    return (n - 1).bit_length()


def geom_bin(value, alpha):
    if value <= 1:
        return 0
    power = F(1)
    k = 0
    while power < value:
        power *= alpha
        k += 1
    return k


def critical_points(xs, ys):
    """Breakpoints of max(J,F,0), sufficient for affine comparisons."""
    points = set(map(F, xs))
    for a, b in zip(range(len(xs) - 1), range(1, len(xs))):
        ja = line(xs[0], ys[0], xs[-1], ys[-1], xs[a])
        jb = line(xs[0], ys[0], xs[-1], ys[-1], xs[b])
        pairs = [(ys[a], ys[b]), (ja, jb), (ys[a] - ja, ys[b] - jb)]
        for va, vb in pairs:
            if va * vb < 0:
                points.add(F(xs[a]) - va * F(xs[b] - xs[a], 1) / (vb - va))
    return sorted(points)


def envelope(xs, ys, edges, x):
    return max(line(xs[i], ys[i], xs[j], ys[j], x)
               for i, j in edges if xs[i] <= x <= xs[j])


def prefix(xs, ys):
    """Return safe prefix, same-sign leaves, edges, and descent trace."""
    edges = [(0, len(xs) - 1)]
    leaves = []
    trace = []

    def visit(i, j, ascending=False, depth=0):
        if j == i + 1 or ys[i] * ys[j] >= 0:
            leaves.append((i, j, depth))
            return None
        ordered = list(range(i, j + 1)) if ys[i] < 0 else list(range(j, i - 1, -1))
        neg, pos = ordered[0], ordered[-1]
        inner = ordered[1:-1]
        p = ys[pos]
        nonpositive = [k for k in inner if ys[k] <= 0]
        reason = ""
        if nonpositive:
            assert not ascending
            z = nonpositive[-1]
            suffix = inner[inner.index(z) + 1:]
            sz = (p - ys[z]) / abs(xs[pos] - xs[z])
            if suffix:
                slopes = {k: (p - ys[k]) / abs(xs[pos] - xs[k]) for k in suffix}
                maximum = max(slopes.values())
            else:
                maximum = None
            if not suffix or maximum <= sz:
                k = z
                reason = "last_nonpositive"
            else:
                tied = [k for k in suffix if slopes[k] == maximum]
                k = tied[len(tied) // 2]
                reason = "strict_positive_descent"
                assert 0 < ys[k] < p
        else:
            assert all(ys[k] > 0 for k in inner)
            slopes = {k: (p - ys[k]) / abs(xs[pos] - xs[k]) for k in inner}
            maximum = max(slopes.values())
            if not ascending and maximum > 0:
                tied = [k for k in inner if slopes[k] == maximum]
                k = tied[len(tied) // 2]
                reason = "strict_positive_descent"
                assert 0 < ys[k] < p
            else:
                ascending = True
                c = min(ys[k] for k in inner)
                assert c >= p
                tied = [k for k in inner if ys[k] == c]
                k = tied[len(tied) // 2]
                reason = "minimum_height_median"
        edges.extend([(i, k), (k, j)])
        trace.append({"interval": [i, j], "root": k, "reason": reason,
                      "old_positive_approx": float(p), "root_value_approx": float(ys[k])})
        left = visit(i, k, ascending, depth + 1)
        right = visit(k, j, ascending, depth + 1)
        return (k, left, right)

    tree = visit(0, len(xs) - 1)
    return tree, leaves, edges, trace


def complete(xs, ys, tau, alpha, prefix_tree, leaves, prefix_edges):
    edges = list(prefix_edges)
    replacements = {}
    bins_used = []

    for i, j, prior_depth in leaves:
        if j == i + 1:
            replacements[(i, j)] = None
            continue
        assert ys[i] * ys[j] >= 0
        positive_skeleton = ys[i] >= 0 and ys[j] >= 0
        bins = {}
        for k in range(i + 1, j):
            a = tau
            if positive_skeleton:
                a += line(xs[i], ys[i], xs[j], ys[j], xs[k])
            bins[k] = geom_bin(ys[k] / a, alpha)
        bins_used.append(len(set(bins.values())))

        def build(a, b):
            if b == a + 1:
                return None
            low = min(bins[k] for k in range(a + 1, b))
            tied = [k for k in range(a + 1, b) if bins[k] == low]
            k = tied[len(tied) // 2]
            edges.extend([(a, k), (k, b)])
            return (k, build(a, k), build(k, b))

        replacements[(i, j)] = build(i, j)

    def splice(tree, i, j):
        if tree is None:
            return replacements[(i, j)]
        k, left, right = tree
        return (k, splice(left, i, k), splice(right, k, j))

    return splice(prefix_tree, 0, len(xs) - 1), edges, bins_used


def depth(tree):
    if tree is None:
        return 0
    return 1 + max(depth(tree[1]), depth(tree[2]))


def energy(xs, ys, edges=None):
    out = F(0)
    for n in range(xs[0], xs[-1] + 1):
        if edges is None:
            value = max(F(0), interp(xs, ys, n),
                        line(xs[0], ys[0], xs[-1], ys[-1], n))
        else:
            value = max(F(0), envelope(xs, ys, edges, n))
        out += value * value / (n * n)
    return out


def case_check(xs, ys, delta):
    q2 = energy(xs, ys)
    assert q2 > 0
    w = sum((F(1, n * n) for n in range(xs[0], xs[-1] + 1)), F(0))
    low_tau2 = delta * delta * q2 / (256 * w)
    high_tau2 = delta * delta * q2 / (64 * w)
    tau = F(1)
    while tau * tau < low_tau2:
        tau *= 2
    while tau * tau > high_tau2:
        tau /= 2
    assert low_tau2 <= tau * tau <= high_tau2
    alpha = 1 + delta / 32
    rounded = list(ys)
    for i in range(1, len(xs) - 1):
        if ys[i] > 0:
            power = tau
            while power < ys[i]:
                power *= alpha
            rounded[i] = power
        assert ys[i] <= rounded[i] <= max(ys[i], alpha * ys[i]) + tau

    p_tree, leaves, p_edges, trace = prefix(xs, rounded)
    critical = critical_points(xs, rounded)
    for x in critical:
        target = max(F(0), interp(xs, rounded, x),
                     line(xs[0], ys[0], xs[-1], ys[-1], x))
        assert max(F(0), envelope(xs, rounded, p_edges, x)) <= target

    k_heights = len(set(y for y in rounded if y > 0))
    ln = log2_ceiling_integer(len(xs) - 1)
    assert depth(p_tree) <= k_heights * (1 + ln) + 1
    assert sum(t["reason"] == "last_nonpositive" for t in trace) <= 1

    tree, edges, bins_used = complete(xs, rounded, tau, alpha, p_tree, leaves, p_edges)
    assert len(edges) == 1 + 2 * (len(xs) - 2)
    assert {k for i, j in edges for k in (i, j)} == set(range(len(xs)))
    result2 = energy(xs, ys, edges)
    comparison2 = energy(xs, rounded, edges)
    rounded2 = energy(xs, rounded)
    assert q2 <= result2 <= comparison2
    assert result2 <= (1 + delta) ** 2 * q2
    for n in range(xs[0], xs[-1] + 1):
        assert envelope(xs, ys, edges, n) <= envelope(xs, rounded, edges, n)
    ratio = result2 / q2
    decimal_scale = 10**12
    lo = ratio.numerator * decimal_scale // ratio.denominator
    hi = -((-ratio.numerator * decimal_scale) // ratio.denominator)
    return {"nodes": len(xs), "delta": str(delta), "depth": depth(tree),
            "prefix_depth": depth(p_tree), "positive_heights": k_heights,
            "prefix_breakpoints_checked": len(critical),
            "integer_points_checked": xs[-1] - xs[0] + 1,
            "energy_ratio_squared_enclosure": [str(F(lo, decimal_scale)), str(F(hi, decimal_scale))],
            "energy_ratio_squared_decimal": float(result2 / q2),
            "rounding_ratio_squared_decimal": float(rounded2 / q2),
            "prefix_reasons": [t["reason"] for t in trace],
            "same_sign_gaps": len(leaves), "max_completion_occupied_bins": max(bins_used, default=0)}


def main():
    rng = Random(20261124)
    results = []
    cases = []
    values = [F(-10**20), F(-100), F(-3), F(-1), F(-1, 10**25), F(0),
              F(1, 10**30), F(1, 100), F(1), F(2), F(3), F(100), F(10**20)]
    for count in range(3, 17):
        for trial in range(20):
            span = 2 * count + 5
            x = span + rng.randrange(1, 20)
            xs = [x] + sorted(rng.sample(range(x + 1, x + span), count - 2)) + [x + span]
            ys = [rng.choice(values) for _ in xs]
            ys[0] = -abs(rng.choice([v for v in values if v]))
            ys[-1] = abs(rng.choice([v for v in values if v]))
            if trial % 2:
                ys.reverse()
            delta = rng.choice([F(1), F(1, 2), F(1, 4), F(1, 10)])
            cases.append((xs, ys, delta))
    # Repeated positive levels, zeros, all-positive interior and large cancellation.
    for count in [5, 9, 17, 33]:
        xs = list(range(2 * count, 3 * count))
        patterns = [
            [F(-10**25)] + [F(1)] * (count - 2) + [F(10**10)],
            [F(-1)] + [F(1, 10**30)] * (count - 2) + [F(10**10)],
            [F(-1)] + [F(2**k) for k in range(count - 2)] + [F(2**count)],
            [F(-1)] + [F(0) if k % 3 == 0 else F(k % 4 + 1) for k in range(count - 2)] + [F(10)],
        ]
        for ys in patterns:
            for reverse in [False, True]:
                cases.append((xs, list(reversed(ys)) if reverse else ys, F(1, 10)))
    fixture = Path(__file__).with_name("fixed_inputs.json")
    if fixture.exists():
        frozen = json.loads(fixture.read_text())
        cases = [(row["xs"], list(map(F, row["ys"])), F(row["delta"]))
                 for row in frozen["cases"]]
    else:
        fixture.write_text(json.dumps({
            "seed_used_only_for_initial_generation": 20261124,
            "cases": [{"xs": xs, "ys": list(map(str, ys)), "delta": str(delta)}
                      for xs, ys, delta in cases],
        }, indent=2) + "\n")
    for xs, ys, delta in cases:
        results.append(case_check(xs, ys, delta))
    summary = {
        "status": "all exact rational assertions passed",
        "scope": "author finite checks of the proved general crossing-skeleton theorem; not independent Review",
        "seed": 20261124,
        "fixed_inputs": "fixed_inputs.json",
        "cases": len(results),
        "continuous_breakpoints_checked": sum(r["prefix_breakpoints_checked"] for r in results),
        "closed_integer_energy_points": sum(r["integer_points_checked"] for r in results),
        "maximum_observed_prefix_depth": max(r["prefix_depth"] for r in results),
        "maximum_observed_total_depth": max(r["depth"] for r in results),
        "maximum_observed_energy_ratio_squared": max(r["energy_ratio_squared_decimal"] for r in results),
        "reused_lemma": "previous full-integer nonnegative-floor amplification exponent 10",
        "results": results,
    }
    out = Path(__file__).with_name("crossing_tree_certificate.json")
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
