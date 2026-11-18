#!/usr/bin/env python3
"""R281 exact rational tests of BRC labeled-Port multioutput and 13-adic visibility."""
from collections import deque
from fractions import Fraction as Q
from itertools import product
from math import factorial
import json


def invert(a):
    n = len(a)
    b = [[Q(a[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        t = next(i for i in range(k, n) if b[i][k] != 0)
        b[k], b[t] = b[t], b[k]
        pivot = b[k][k]
        b[k] = [v / pivot for v in b[k]]
        for i in range(n):
            if i != k:
                scale = b[i][k]
                b[i] = [x - scale*y for x, y in zip(b[i], b[k])]
    return [row[n:] for row in b]


def green(w):
    n = len(w)
    assert all(v >= 0 for row in w for v in row)
    assert all(sum(row) < 1 for row in w)
    return invert([[Q(i == j) - w[i][j] for j in range(n)] for i in range(n)])


def bfs(starts, arcs):
    d = dict.fromkeys(starts, 0)
    q = deque(starts)
    while q:
        i = q.popleft()
        for j in arcs[i]:
            if j not in d:
                d[j] = d[i]+1
                q.append(j)
    return d


def multi_degrees(s, edits, outputs):
    m = len(edits)
    arcs = [[j for j, (u, _) in enumerate(edits) if s[edits[i][1]][u] > 0] for i in range(m)]
    rev = [[i for i in range(m) if j in arcs[i]] for j in range(m)]
    by_output = []
    for a, b in outputs:
        sources = [i for i, (u, v) in enumerate(edits) if s[a][u] > 0]
        sinks = [i for i, (u, v) in enumerate(edits) if s[v][b] > 0]
        dl = bfs(sources, arcs)
        dr = bfs(sinks, rev)
        depths = [dl[i]+1+dr[i] if i in dl and i in dr else None for i in range(m)]
        by_output.append({"output": [a, b],
                          "first_any": min((v for v in depths if v is not None), default=None),
                          "first_by_label": depths})
    return by_output


def coefficient(s, edits, a, b, word):
    if not word:
        return s[a][b]
    t = s[a][edits[word[0]][0]]
    for i, j in zip(word, word[1:]):
        t *= s[edits[i][1]][edits[j][0]]
    return t*s[edits[word[-1]][1]][b]


def exact_model(w, edits, outputs, max_degree=5):
    s = green(w)
    by_output = multi_degrees(s, edits, outputs)
    inspected = 0
    for info in by_output:
        a, b = info["output"]
        measured = [None]*len(edits)
        first = None
        for degree in range(1, max_degree+1):
            for word in product(range(len(edits)), repeat=degree):
                inspected += 1
                c = coefficient(s, edits, a, b, word)
                if c > 0:
                    first = degree if first is None else first
                    for i in set(word):
                        if measured[i] is None:
                            measured[i] = degree
        assert measured == info["first_by_label"], (measured, info)
        assert first == info["first_any"], (first, info)
    return {"outputs": by_output, "ordered_word_output_checks": inspected}


def val_p(q, p):
    q = Q(q)
    if q == 0:
        return None
    a, b, v = abs(q.numerator), q.denominator, 0
    while a % p == 0:
        v += 1
        a //= p
    while b % p == 0:
        v -= 1
        b //= p
    return v


def residue_unit(q, p):
    v = val_p(q, p)
    if v is None:
        return 0
    q = q / Q(p**v) if v >= 0 else q * Q(p**(-v))
    assert q.denominator % p != 0
    return (q.numerator * pow(q.denominator, -1, p)) % p


# Multi-output extension of R280's five-Port sharpness example.
w5 = [[Q(0) for _ in range(5)] for _ in range(5)]
for u, v in [(0, 1), (2, 0), (2, 3), (4, 1)]:
    w5[u][v] = Q(1, 8)
mult = exact_model(w5, [(1, 2), (3, 4)], [(0, 0), (0, 3), (4, 0)])
assert mult["outputs"][0]["first_by_label"] == [1, 3]

# Observers (0,0) and (3,3) protect disjoint edit labels.
w_multi = [[Q(0) for _ in range(4)] for _ in range(4)]
w_multi[0][1] = w_multi[2][0] = Q(1, 4)
scoped = exact_model(w_multi, [(1, 2), (3, 3)], [(0, 0), (3, 3)])
assert scoped["outputs"][0]["first_by_label"] == [1, None]
assert scoped["outputs"][1]["first_by_label"] == [None, 1]

# Two positive baseline paths: each is a 13-adic unit; their sum is not.
w3 = [[Q(0), Q(1, 16), Q(7, 8)], [Q(0)]*3,
      [Q(0), Q(6, 7), Q(0)]]
s = green(w3)
path1 = Q(1, 16)
path2 = Q(7, 8) * Q(6, 7)
assert path1 + path2 == s[0][1] == Q(13, 16)
assert val_p(path1, 13) == val_p(path2, 13) == 0
assert (residue_unit(path1, 13) + residue_unit(path2, 13)) % 13 == 0
assert val_p(s[0][1], 13) == 1
w3_updated = [row[:] for row in w3]
w3_updated[1][0] = Q(1, 4)
assert green(w3_updated)[0][0] == Q(64, 51)
assert green(w3_updated)[0][0] == 1 / (1 - Q(13, 16)*Q(1, 4))

# First real edit degree 1, but first degree mod 13 is 2.
w4 = [[Q(0) for _ in range(4)] for _ in range(4)]
w4[0][1] = Q(13, 16)
e4 = [(1, 0), (0, 2), (2, 0)]
s4 = green(w4)
jet = exact_model(w4, e4, [(0, 0), (0, 1)])
assert jet["outputs"][0]["first_any"] == 1
assert coefficient(s4, e4, 0, 0, (0,)) == Q(13, 16)
assert coefficient(s4, e4, 0, 0, (1, 2)) == 1
assert val_p(coefficient(s4, e4, 0, 0, (0,)), 13) == 1
assert val_p(coefficient(s4, e4, 0, 0, (1, 2)), 13) == 0
updated = [row[:] for row in w4]
for u, v in e4:
    updated[u][v] += Q(1, 16)
assert green(updated)[0][0] == Q(128, 121)
a_only = [row[:] for row in w4]
a_only[1][0] = Q(1, 16)
assert green(a_only)[0][0] == Q(256, 243)
assert residue_unit(green(updated)[0][0], 13) == 6
assert residue_unit(green(a_only)[0][0], 13) == 1

# On a single Port with 13 distinct self-edge labels, [x_1...x_13]F=13!.
assert val_p(Q(factorial(13)), 13) == 1
assert factorial(13) % 13 == 0

result = {
    "status": "PASS",
    "models": 3,
    "multi_output_word_checks": (
        mult["ordered_word_output_checks"] +
        scoped["ordered_word_output_checks"] +
        jet["ordered_word_output_checks"]),
    "multi_output": mult,
    "scoped_union": scoped,
    "mixed_jet": jet,
    "baseline_path_terms": [str(path1), str(path2)],
    "baseline_sum": str(s[0][1]),
    "baseline_sum_v13": 1,
    "baseline_edit_value": "64/51",
    "single_edge_linear_coefficient": "13/16",
    "mixed_edge_quadratic_coefficient": "1",
    "mod13_response_all_three": 6,
    "mod13_response_A_only": 1,
    "factorial_labeled_monomial_coefficient": str(factorial(13)),
    "factorial_v13": 1,
    "scientific_scope": "finite exact rational witnesses; universal formulas justified separately by symbolic proof",
    "frozen_science_pin": "43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    "prior_frontier": "R280@33fcdc666acd935b276e3b0f50789c2f3301193f"
}
print(json.dumps(result, ensure_ascii=False, indent=2))
