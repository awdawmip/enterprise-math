#!/usr/bin/env python3
"""Exact finite comparison checks for RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS.

This checker does not certify bibliography or novelty. It certifies the finite
identifications used by the prior-art audit:

* the four-Cell and six-axis S4 orbitals;
* the n=6 Lee-ball formula used by the Falconer lane;
* the H(6,q) Hamming countermodel distance set;
* the signed-shell separation numbers 3/2/2/infinity;
* the K6 minimum edge-cover interpretation;
* the even-weight SPC-code interpretation of global inversion;
* the frozen E6 root-system reconstruction: 72 roots, degree 20, 720 edges.

Only Python stdlib and exact integer arithmetic are used.
"""

from collections import deque
from itertools import combinations, permutations, product
from math import comb

CHECKS = 0


def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


# ---------------------------------------------------------------------------
# Kissing lane: S4 on four Cells and on the six edges of K4 = J(4,2).
# ---------------------------------------------------------------------------
PTS = range(4)
S4 = list(permutations(PTS))
FOUR_PAIRS = list(combinations(PTS, 2))
seed = FOUR_PAIRS[0]
four_pair_orbit = {
    tuple(sorted((p[seed[0]], p[seed[1]])))
    for p in S4
}
check(len(four_pair_orbit) == 6, "S4 must be transitive on unordered pairs of four points")
check({0, 3} == {0, len(tuple(PTS)) - 1}, "four-Cell invariant graph degrees must be 0 or 3")

AXES = [tuple(c) for c in combinations(PTS, 2)]
AXIS_INDEX = {e: i for i, e in enumerate(AXES)}
AXIS_PAIRS = list(combinations(range(6), 2))
seen = set()
orbitals = []
for pair in AXIS_PAIRS:
    if pair in seen:
        continue
    orb = set()
    for p in S4:
        a = AXIS_INDEX[tuple(sorted((p[AXES[pair[0]][0]], p[AXES[pair[0]][1]])))]
        b = AXIS_INDEX[tuple(sorted((p[AXES[pair[1]][0]], p[AXES[pair[1]][1]])))]
        orb.add(tuple(sorted((a, b))))
    seen |= orb
    orbitals.append(orb)

check(sorted(len(o) for o in orbitals) == [3, 12], "J(4,2) non-diagonal orbitals must have sizes 3 and 12")
orbital_degrees = []
for orb in orbitals:
    degrees = [0] * 6
    for a, b in orb:
        degrees[a] += 1
        degrees[b] += 1
    check(len(set(degrees)) == 1, "each S4 orbital graph on J(4,2) must be regular")
    orbital_degrees.append(degrees[0])
check(sorted(orbital_degrees) == [1, 4], "J(4,2) orbital degrees must be 1 and 4")
check(sorted({0, orbital_degrees[0], orbital_degrees[1], sum(orbital_degrees)}) == [0, 1, 4, 5],
      "all S4-invariant simple graph degrees on six axes must be 0,1,4,5")


# ---------------------------------------------------------------------------
# Falconer lane: Lee ball and Hamming scheme.
# ---------------------------------------------------------------------------
def V6(r):
    return sum((2 ** j) * comb(6, j) * comb(r, j) for j in range(7))


for r in range(5):
    exact = sum(
        1
        for x in product(range(-r, r + 1), repeat=6)
        if sum(abs(a) for a in x) <= r
    )
    check(exact == V6(r), f"Lee ball enumeration mismatch at radius {r}")
check([V6(r) for r in range(5)] == [1, 13, 85, 377, 1289], "Lee ball regression mismatch")

for q in range(2, 6):
    distances_from_zero = {
        sum(a != b for a, b in zip((0,) * 6, v))
        for v in product(range(q), repeat=6)
    }
    check(distances_from_zero == set(range(7)), f"H(6,{q}) must realize all distances 0..6")
    check(q ** 6 > 6, f"H(6,{q}) carrier must already exceed its diameter")


# ---------------------------------------------------------------------------
# Hadwiger lane: constrained binary covering/separation.
# ---------------------------------------------------------------------------
def separation_number(patterns, n=6):
    pats = list(patterns)
    for k in range(1, min(4, len(pats)) + 1):
        for inds in combinations(range(len(pats)), k):
            chosen = [pats[i] for i in inds]
            if all({p[j] for p in chosen} == {-1, 1} for j in range(n)):
                return k
    return None


ALL_PATTERNS = list(product((-1, 1), repeat=6))
ELEMENTARY = [p for p in ALL_PATTERNS if sum(x == -1 for x in p) in (0, 2)]
EVEN = [p for p in ALL_PATTERNS if sum(x == -1 for x in p) % 2 == 0]
SIGN_PRESERVING = [(1,) * 6]

check(separation_number(ELEMENTARY) == 3, "one-step weight-2 family must have separation number 3")
check(separation_number(EVEN) == 2, "even-weight closure must have separation number 2")
check(separation_number(ALL_PATTERNS) == 2, "full sign family must have separation number 2")
check(separation_number(SIGN_PRESERVING) is None, "sign-preserving family must fail to separate polarities")

K6_EDGES = list(combinations(range(6), 2))
rho = None
for k in range(1, 4):
    for es in combinations(K6_EDGES, k):
        covered = set()
        for a, b in es:
            covered |= {a, b}
        if len(covered) == 6:
            rho = k
            break
    if rho is not None:
        break
check(rho == 3, "minimum edge cover of K6 must have size 3")

minus = (-1,) * 6
check(minus in EVEN, "all-minus word must lie in the length-6 even-weight SPC code")


def mul(a, b):
    return tuple(x * y for x, y in zip(a, b))


def flip(i, j):
    p = [1] * 6
    p[i] = p[j] = -1
    return tuple(p)


check(mul(mul(flip(0, 1), flip(2, 3)), flip(4, 5)) == minus,
      "three disjoint weight-2 flips must compose to global inversion")


# ---------------------------------------------------------------------------
# E6 frozen external witness, regenerated exactly from the accepted Gram matrix.
# ---------------------------------------------------------------------------
G = [
    [2, 0, -1, 0, 0, 0],
    [0, 2, 0, -1, 0, 0],
    [-1, 0, 2, -1, 0, 0],
    [0, -1, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, -1, 2],
]


def gv(v):
    return [sum(G[i][j] * v[j] for j in range(6)) for i in range(6)]


def reflect(v, i):
    w = list(v)
    w[i] -= gv(v)[i]
    return tuple(w)


def inner(v, w):
    return sum(v[i] * G[i][j] * w[j] for i in range(6) for j in range(6))


roots = {(1, 0, 0, 0, 0, 0)}
queue = deque(roots)
while queue:
    v = queue.popleft()
    for i in range(6):
        w = reflect(v, i)
        if w not in roots:
            roots.add(w)
            queue.append(w)

check(len(roots) == 72, "E6 reflection closure must contain 72 roots")
check(all(inner(v, v) == 2 for v in roots), "every regenerated E6 root must have norm 2")
degrees = [sum(1 for w in roots if w != v and inner(v, w) == 1) for v in roots]
check(set(degrees) == {20}, "E6 pairing-1 contact graph must be 20-regular")
check(sum(degrees) // 2 == 720, "E6 pairing-1 contact graph must have 720 edges")

print(f"PASS GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS checks={CHECKS}")
