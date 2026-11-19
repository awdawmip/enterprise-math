"""Exact total variation costs for the exposed PFSSV address block. Python >=3.10."""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import comb, prod
from pathlib import Path


SOURCE = Path("research_artifacts/PFSSV_REVISION_20260908/cell_profiles.jsonl")
SOURCE_LINE = "fcfc138fbbddacd089c228b4cb3783e55064b9c9879d84f5de642911ebc860a0"


def read_geometry(path):
    with path.open("rb") as stream:
        first = stream.readline()
    assert sha256(first).hexdigest() == SOURCE_LINE
    cell = json.loads(first)
    assert (cell["X"], cell["upper"]) == (100000, 101000)
    address_rows = {}
    residue_occurrences = 0
    for row in cell["rows"]:
        p = row["p"]
        assert (row["qlo"], row["qhi"]) == (max(p, 100000 // p + 1), 101000 // p)
        for q in range(row["qlo"], row["qhi"] + 1):
            address_rows.setdefault(q, []).append(p)
        residue_occurrences += row["q_mod_30_counts"][29]
    target = {q: rows for q, rows in address_rows.items() if q % 30 == 29}
    shared = {q: rows for q, rows in target.items() if len(rows) > 1}
    assert shared == {419: [239, 241]} and all(419 % d for d in range(2, 21))
    n = len(target)
    occupied = residue_occurrences - 1
    r = sum(2 in rows for rows in target.values())
    assert (len(address_rows), n, occupied, r) == (2016, 69, 29, 17)
    assert (len(cell["rows"]), cell["zero_prime_count_rows"]) == (66, 15)
    assert (cell["totals"]["diagonal"], cell["totals"]["overflow"]) == (1, 1)
    return n, occupied, r


def basis_values(x, t):
    """Integer Newton basis on 1,...,r, also evaluated at the external node 0."""
    if x == 0:
        return [(-1) ** j for j in range(t + 1)]
    return [comb(x - 1, j) for j in range(t + 1)]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def simplex(constraints, objective):
    """Maximize from the initial slack basis; Bland's rule uses exact rationals."""
    m = len(constraints)
    n = len(objective)
    basis = list(range(n, n + m))
    rows = []
    for i, (coefficients, rhs) in enumerate(constraints):
        assert rhs >= 0
        slack = [int(i == j) for j in range(m)]
        rows.append(list(map(Fraction, coefficients + slack + [rhs])))
    bottom = list(map(Fraction, [-v for v in objective] + [0] * (m + 1)))
    while True:
        entering = next((j for j in range(n + m) if bottom[j] < 0), None)
        if entering is None:
            break
        choices = [(row[-1] / row[entering], basis[i], i)
                   for i, row in enumerate(rows) if row[entering] > 0]
        if not choices:
            raise ValueError("Unbounded dual for the specified change")
        leaving = min(choices)[2]
        divisor = rows[leaving][entering]
        pivot = [v / divisor for v in rows[leaving]]
        rows[leaving] = pivot
        nonzero = [(j, v) for j, v in enumerate(pivot) if v]
        for i, row in enumerate(rows + [bottom]):
            if i != leaving and row[entering]:
                multiplier = row[entering]
                for j, value in nonzero:
                    row[j] -= multiplier * value
        basis[leaving] = entering
    optimum = [Fraction(0)] * (n + m)
    for row, j in zip(rows, basis):
        optimum[j] = row[-1]
    return bottom[-1], optimum[:n], bottom[n:-1]


def cost_line(weights, t, direction, size):
    """Return an attained supporting line, after checking a measure and a polynomial."""
    r = len(weights) - 1
    delta = direction * size
    constraints = []
    for i in range(1, r + 1):
        values = basis_values(i, t)
        coeff = values + [-v for v in values] + [0] * r
        constraints.append((coeff, 1))
        below = [-v for v in coeff]
        below[2 * (t + 1) + i - 1] = -1
        constraints.append((below, 0))
    zero = [delta * v for v in basis_values(0, t)]
    objective = zero + [-v for v in zero] + [-w for w in weights[1:]]
    value, primal, dual = simplex(constraints, objective)
    coeff = [primal[i] - primal[t + 1 + i] for i in range(t + 1)]
    polynomial = [dot(coeff, basis_values(x, t)) for x in range(r + 1)]
    edit = [-delta] + [dual[2 * i] - dual[2 * i + 1] for i in range(r)]
    updated = [w + e for w, e in zip(weights, edit)]
    assert min(updated) >= 0 and sum(updated) == 1
    for j in range(t + 1):
        assert sum(e * comb(i, j) for i, e in enumerate(edit)) == 0
    assert max(polynomial[1:]) <= 1
    slope = direction * polynomial[0] + int(direction < 0)
    intercept = sum(w * min(v, 0) for w, v in zip(weights[1:], polynomial[1:]))
    tv = sum(abs(e) for e in edit) / 2
    assert slope * size + intercept == tv == value + max(0, -delta)
    return (slope, intercept), edit, polynomial


def feasible_range(weights, t):
    """Extremal polynomials for the point indicator, also checked by endpoint edits."""
    r = len(weights) - 1
    if t == r:
        return weights[0], weights[0]
    lower, upper = Fraction(0), Fraction(1)
    for nodes in combinations(range(1, r + 1), t):
        gaps = [x for x in range(1, r + 1) if x not in nodes]
        signs = {sum(j < x for j in nodes) % 2 for x in gaps}
        if len(signs) != 1:
            continue
        den = prod(nodes)
        bound = weights[0] + sum(weights[x] * Fraction(prod(j - x for j in nodes), den)
                                 for x in gaps)
        if signs == {0}:
            upper = min(upper, bound)
        else:
            lower = max(lower, bound)
    return lower, upper


def budget_frontier(weights, t, direction, limit):
    """Intersect supporting lines. A matching primal interpolation fills each interval."""
    if not limit:
        return [], None
    r = len(weights) - 1
    near = min(weights) / r ** (r + 1)
    assert 0 < near < limit
    first, edit, polynomial = cost_line(weights, t, direction, near)
    assert first[1] == 0 and min(polynomial[1:]) >= 0
    stencil = [i for i in range(1, r + 1) if edit[i]]
    signed = [str(edit[i] / (direction * near)) for i in stencil]
    last = cost_line(weights, t, direction, limit)[0]

    def between(left, right, a, b):
        if a == b:
            return [(left, right, *a)]
        cross = (a[1] - b[1]) / (b[0] - a[0])
        assert left <= cross <= right
        if cross == left:
            return [(left, right, *b)]
        if cross == right:
            return [(left, right, *a)]
        mid = cost_line(weights, t, direction, cross)[0]
        if mid[0] * cross + mid[1] == a[0] * cross + a[1]:
            return [(left, cross, *a), (cross, right, *b)]
        return between(left, cross, a, mid) + between(cross, right, mid, b)

    pieces = []
    for seg in between(Fraction(0), limit, first, last):
        if pieces and pieces[-1][2:] == seg[2:]:
            pieces[-1] = (pieces[-1][0], seg[1], *seg[2:])
        else:
            pieces.append(seg)
    assert pieces[0][0] == 0 and pieces[-1][1] == limit
    for a, b in zip(pieces, pieces[1:]):
        assert a[1] == b[0] and a[2] < b[2]
        assert a[2] * a[1] + a[3] == b[2] * b[0] + b[3]
    corners = [(str(left), str(slope * left + origin))
               for left, _, slope, origin in pieces]
    corners.append((str(limit), str(last[0] * limit + last[1])))
    return corners, {"nodes": stencil, "interpolation_weights": signed,
                     "sensitivity": str(1 / first[0])}


def complement_test(r, ell):
    """Independent binomial, low-degree L1 minimization for the opposite end of the table."""
    weights = [comb(r, j) for j in range(r + 1)]
    best = None
    best_nodes = []
    for missing in combinations(range(1, r + 1), ell):
        numerator = sum(w * abs(prod(m - j for m in missing)) for j, w in enumerate(weights))
        value = Fraction(numerator, prod(missing))
        if best is None or value < best:
            best, best_nodes = value, [missing]
        elif value == best:
            best_nodes.append(missing)
    return best, best_nodes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default = SOURCE if SOURCE.is_file() else Path("/workspace/enterprise-math") / SOURCE
    parser.add_argument("--source", type=Path, default=default)
    n, k, r = read_geometry(parser.parse_args().source)
    weights = [Fraction(comb(r, i) * comb(n - r, k - i), comb(n, k)) for i in range(r + 1)]
    assert sum(weights) == 1
    profiles = []
    for t in range(r + 1):
        lo, hi = feasible_range(weights, t)
        down, stencil = budget_frontier(weights, t, 1, weights[0] - lo)
        up, opposite = budget_frontier(weights, t, -1, hi - weights[0])
        if t < r:
            assert stencil["sensitivity"] == opposite["sensitivity"]
        profiles.append({"order": t, "empty_range": [str(lo), str(hi)],
                         "local": stencil, "decrease_corners": down, "increase_corners": up})
    assert [t for t, row in enumerate(profiles) if row["empty_range"][0] == "0"] == list(range(15))
    assert profiles[2]["local"]["sensitivity"] == "64/81"
    assert profiles[14]["decrease_corners"][-1][1] == "1846443070/9700057191"
    for size in range(2, 37):
        assert complement_test(size, 0)[0] == 2 ** size
        val, nodes = complement_test(size, 1)
        assert val == comb(size, size // 2)
        assert nodes == ([(size // 2 + 1,)] if size % 2 else [(size // 2,), (size // 2 + 1,)])
    gaussian_checks = []
    for size in (8, 16, 17, 32, 64):
        value, roots = complement_test(size, 2)
        gaussian_checks.append({"r": size, "optimal_omitted_pairs": roots,
                                "binomial_normalization": str(size * value / 2 ** size)})
        if size == r:
            assert 2 / value == Fraction(profiles[r - 3]["local"]["sensitivity"])
    output = {"source_first_line_sha256": SOURCE_LINE, "layer": [n, k, r],
              "baseline_empty": str(weights[0]), "profiles": profiles,
              "two_missing_node_tests": gaussian_checks}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
