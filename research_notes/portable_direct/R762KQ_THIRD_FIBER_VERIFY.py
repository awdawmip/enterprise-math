#!/usr/bin/env python3
"""R762KQ: exact third connected source fiber in unsigned M3 Port--Euler.

All operations are integer or rational. No numerical optimization or floating point.
"""
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb

PORTS = [p for p in combinations(range(6), 2) if p not in {(0, 1), (2, 3), (4, 5)}]
BITS = {p: 1 << i for i, p in enumerate(PORTS)}
EDGES = []
for i, j, k in product(range(2), repeat=3):
    a, b, c = (i, 2 + j), (i, 4 + k), (2 + j, 4 + k)
    EDGES.append((BITS[a] ^ BITS[b], BITS[a] ^ BITS[c], BITS[b] ^ BITS[c]))

F = {0}
for tri in combinations(range(6), 3):
    pairs = [p for p in combinations(tri, 2) if p in BITS]
    if len(pairs) == 2:
        e = BITS[pairs[0]] ^ BITS[pairs[1]]
        F |= {v ^ e for v in tuple(F)}
assert len(PORTS) == 12 and len(EDGES) == 8 and len(F) == 512

# P[b][i] = coefficient t^i of the eight-factor GF(2) group-algebra product.
P = {0: (1,)}
for edges in EDGES:
    nxt = defaultdict(lambda: [0] * 9)
    for mask, coefficients in P.items():
        for i, v in enumerate(coefficients):
            if not v:
                continue
            if i < 8:
                nxt[mask][i + 1] += v
            for edge in edges:
                nxt[mask ^ edge][i] += v
    P = {k: tuple(v) for k, v in nxt.items()}
classes = defaultdict(list)
for boundary in sorted(F):
    classes[P.get(boundary, (0,) * 9)].append(boundary)
assert len(P) == 2048 and len(classes) == 19
by_rep = {min(bs): (p, bs) for p, bs in classes.items()}
assert by_rep[0][0] == (9, 0, 16, 0, 6, 0, 0, 0, 1)
assert by_rep[3][0] == (6, 8, 6, 8, 2, 0, 2, 0, 0)
assert by_rep[15][0] == (4, 8, 10, 8, 0, 0, 2, 0, 0)
assert by_rep[18][0] == (4, 12, 8, 0, 4, 4, 0, 0, 0)
assert by_rep[51][0] == (8, 0, 16, 0, 8, 0, 0, 0, 0)
assert by_rep[15][1] == [15, 240, 785, 1348, 2696, 3106]
assert by_rep[18][1] == [18, 33, 72, 132, 1536, 2304]
assert by_rep[51][1] == [51, 204, 3840]


def divided_square(d):
    """Integer exact quotient d(t)/(t-1)^2; verifies reconstruction."""
    q = []
    for i in range(7):
        q.append(d[i] + (2 * q[-1] if q else 0) - (q[-2] if len(q) > 1 else 0))
    rebuilt = [0] * 9
    for i, v in enumerate(q):
        rebuilt[i] += v
        rebuilt[i + 1] -= 2 * v
        rebuilt[i + 2] += v
    assert tuple(rebuilt) == tuple(d)
    return q


def bernstein(coeff, lo, hi):
    """Degree-six Bernstein coefficients of polynomial on rational [lo,hi]."""
    n = len(coeff) - 1
    power = [Fraction(0) for _ in range(n + 1)]
    for i, v in enumerate(coeff):
        for k in range(i + 1):
            power[k] += v * comb(i, k) * lo ** (i - k) * (hi - lo) ** k
    return [sum((power[i] * Fraction(comb(j, i), comb(n, i))
                 for i in range(j + 1)), Fraction(0))
            for j in range(n + 1)]

# Candidate dominance over every other nonzero class besides the known runner p_3.
regimes = [(18, Fraction(3, 5), Fraction(1), None),
           (18, Fraction(1), Fraction(2), 15),
           (15, Fraction(2), Fraction(3), 18)]
certificates = []
for winner, left, right, edge_tie in regimes:
    for rep, (p, bs) in sorted(by_rep.items()):
        if rep in (0, 3, winner):
            continue
        d = [a - b for a, b in zip(by_rep[winner][0], p)]
        quotient = divided_square(d)
        values = bernstein(quotient, left, right)
        assert min(values) >= 0, (winner, rep, left, right, values)
        if rep != edge_tie:
            assert min(values) > 0, (winner, rep, values)
        else:
            # p18-p15=-2*t*(t-2)*(t-1)^2*(t+1)^2.
            # The analogous opposite sign applies for p15-p18.
            assert min(values) == 0
        certificates.append({"winner": winner, "competitor": rep,
                             "interval": [str(left), str(right)],
                             "quotient_coefficients_low_to_high": quotient,
                             "min_bernstein": str(min(values))})
assert len(certificates) == 48


def exact(m, b):
    r = m // 2
    A, B = (((r + 1) * (r + 2) // 2, r * (r + 1) // 2) if m % 2 == 0 else
            (r * (r + 1) // 2, (r + 1) * (r + 2) // 2))
    return sum(v * A ** i * B ** (8 - i) for i, v in enumerate(P.get(b, (0,) * 9))) - (3 if b == 0 else 0)


def third(m):
    class_values = [(exact(m, rep), rep) for rep in by_rep]
    all_values = sorted({v for v, rep in class_values}, reverse=True)
    assert len(all_values) >= 3
    value = all_values[2]
    winners = sorted(b for b in F if exact(m, b) == value)
    return (value, winners)

# Isolated ratios: m=2 t=3; m=3 t=1/3; m=4 t=2; m=5 t=1/2.
expected = {2: (1792, by_rep[15][1]),
            3: (63360, by_rep[3][1]),
            4: (1653372, sorted(by_rep[15][1] + by_rep[18][1])),
            5: (20995200, by_rep[51][1])}
for m, target in expected.items():
    assert third(m) == target, (m, third(m), target)
for m in range(6, 101):
    val, boundaries = third(m)
    assert boundaries == by_rep[18][1], (m, boundaries)

result = {
    "name": "R762KQ third-distinct connected source fiber",
    "scope": "unsigned auxiliary M3 three inactive Ports 01,23,45; eight uniform flexible multiplicities m>=2; unordered edge-type multisets",
    "parent": "R762KP@07e3f06b98d15197249c1afd7c6fe7949bad7d9b",
    "forced_boundaries": len(F), "polynomial_classes": len(classes),
    "certificate_count": len(certificates), "certificate_intervals": [["3/5", "1"], ["1", "2"], ["2", "3"]],
    "isolated": {str(m): {"third_distinct_value": third(m)[0], "boundaries": third(m)[1]}
                 for m in (2, 3, 4, 5)},
    "all_m_ge_6_third_boundaries": by_rep[18][1],
    "class_polynomials": {str(rep): {"multiplicity": len(bs), "coefficients": list(p)}
                          for rep, (p, bs) in sorted(by_rep.items())},
    "certificates": certificates,
    "finite_regressions_m": [2, 100], "status": "EXACT_PASS",
    "review": "NOT_REVIEWED", "native_lift": "UNPROVED"
}
with open("R762KQ_THIRD_FIBER_EVIDENCE.json", "w", encoding="utf8") as fp:
    json.dump(result, fp, ensure_ascii=False, indent=2)
print("PASS", "boundary=", len(F), "classes=", len(classes), "certificate=", len(certificates))
print("isolated=", result["isolated"])
print("m>=6 third boundaries=", by_rep[18][1])
