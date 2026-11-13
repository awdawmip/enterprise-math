"""Exact rational one-parameter adversarial separator for any fixed BRC-S23 decoder bank.

For a fixed 1D policy edge, represent each label's maximum TV as the max of
row/sign affine forms and the bank's best-label risk as the min of those maxima.
Enumerate every pairwise crossing of ALL forms and the interval endpoints.
Nothing relies on a floating-point optimizer or preselected active constraints.
"""
from fractions import Fraction as F
from itertools import product, combinations

M20 = [
    [10, 10, 0, 0, 0, 0],
    [9, 11, 0, 0, 0, 0],
    [0, 0, 20, 0, 0, 0],
    [0, 0, 0, 10, 10, 0],
    [0, 0, 0, 2, 18, 0],
    [0, 0, 0, 0, 0, 20],
]
BOXES = [
    "34 24 34 24", "34 23 34 34", "34 34 34 23",
    "24 24 12 12", "12 12 24 34", "12 13 23 24",
    "23 34 12 13", "24 34 12 14", "13 12 13 13",
    "12 12 14 12",
]
GROUP = [0, 0, 1, 2, 2, 3]


def prepared_at(t):
    """Six input rows, four time values, lawful one-coin A edge."""
    source = [
        [t, 0, 1 - t, 0],
        [t, 0, 0, 1 - t],
        [t, 0, 1 - t, 0],
        [F(1), 0, 0, 0],
        [F(1), 0, 0, 0],
        [F(1), 0, 0, 0],
    ]
    return [
        [sum(F(M20[i][x], 20) * source[x][a] for x in range(6)) for a in range(4)]
        for i in range(6)
    ]


def decoder(label):
    pairs = [[int(v) - 1 for v in s] for s in BOXES[label].split()]
    return [
        [F(1, 2) if a in pairs[GROUP[i]] else F(0) for a in range(4)]
        for i in range(6)
    ]


def all_lines():
    p0, p1 = prepared_at(F(0)), prepared_at(F(1))
    label_lines = []
    for label in range(10):
        q = decoder(label)
        these = set()
        for i in range(6):
            c = [p0[i][t] - q[i][t] for t in range(4)]
            d = [p1[i][t] - p0[i][t] for t in range(4)]
            for signs in product((-1, 1), repeat=4):
                # TV(p(t),q) = max_signs (1/2) * sum(sign_t * (p_t(t)-q_t))
                slope = sum(signs[t] * d[t] for t in range(4)) / 2
                intercept = sum(signs[t] * c[t] for t in range(4)) / 2
                these.add((F(slope), F(intercept)))
        label_lines.append(tuple(sorted(these)))
    return label_lines


def exact_score(t, label_lines):
    return min(max(a*t + b for a, b in lines) for lines in label_lines)


def main():
    label_lines = all_lines()
    total_with_label = sum(map(len, label_lines))
    global_lines = sorted(set().union(*map(set, label_lines)))
    candidates = {F(0), F(1)}
    for (a, b), (c, d) in combinations(global_lines, 2):
        if a != c:
            x = F(d - b, a - c)
            if 0 <= x <= 1:
                candidates.add(x)
    results = {x: exact_score(x, label_lines) for x in candidates}
    largest = max(results.values())
    maximizers = sorted(x for x, v in results.items() if v == largest)
    assert len(label_lines) == 10
    assert len(global_lines) == 29, len(global_lines)
    assert len(candidates) == 18, len(candidates)
    assert largest == F(2, 3), largest
    assert maximizers == [F(1, 3)], maximizers
    assert exact_score(F(0), label_lines) == F(1, 2)
    assert exact_score(F(1, 2), label_lines) == F(1, 2)
    assert exact_score(F(1), label_lines) == F(1, 2)
    print("PASS_EXACT_ONE_DIMENSIONAL_AFFINE_SEPARATOR")
    print("distinct_label_affine_form_pairs", total_with_label)
    print("global_distinct_affine_forms", len(global_lines))
    print("candidate_breakpoints", len(candidates))
    print("candidate_set", ",".join(map(str, sorted(candidates))))
    print("exact_global_max_TV", largest, "maximizers", ",".join(map(str,maximizers)))
    print("ternary_edge_scores", [str(exact_score(t, label_lines)) for t in (F(0),F(1,2),F(1))])


if __name__ == "__main__":
    main()
