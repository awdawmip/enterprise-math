#!/usr/bin/env python3
"""Exact unit-weight N-BRC signed-port incidence, not physical force dynamics."""
import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

AXES = range(6)
SIGNS = (-1, 1)
PORTS = [(i, s) for i in AXES for s in SIGNS]

def port_triples():
    return [tuple(sorted((a, s) for a, s in zip(ax, signs)))
            for ax in itertools.combinations(AXES, 3)
            for signs in itertools.product(SIGNS, repeat=3)]

def permute(p, permutation):
    return (permutation[p[0]], p[1])

def parity3(items, basis):
    v = [basis.index(p) for p in items]
    inversions = sum(v[i] > v[j] for i in range(3) for j in range(i+1, 3))
    return -1 if inversions % 2 else 1

def orientations(t):
    a, b, c = t
    return ((a, b, c), (a, c, b))

def transport(t, chi, permutation):
    image = tuple(permute(p, permutation) for p in orientations(t)[chi])
    target = tuple(sorted(image))
    return target, 0 if parity3(image, target) == 1 else 1

triads = port_triples()
assert len(triads) == 160 and len(set(triads)) == 160
oriented = {(t, chi) for t in triads for chi in (0, 1)}
assert len(oriented) == 320

lifts = defaultdict(list)
for t, chi in oriented:
    for hidden in t:
        visible = tuple(sorted(p for p in t if p != hidden))
        lifts[visible].append((t, chi, hidden))
assert len(lifts) == 60
assert {len(v) for v in lifts.values()} == {16}
assert sum(map(len, lifts.values())) == 960
assert len({x for v in lifts.values() for x in v}) == 960

unsigned_orbits = Counter(sum(sign == -1 for _, sign in t) for t in triads)
assert unsigned_orbits == {0: 20, 1: 60, 2: 60, 3: 20}
oriented_orbits = {k: 2 * n for k, n in unsigned_orbits.items()}

# Each signed triple has a stabilizing transposition reversing chirality.
for t in triads:
    a, b = next((a, b) for a, b in itertools.combinations(t, 2)
                if a[1] == b[1])
    pi = list(AXES)
    pi[a[0]], pi[b[0]] = pi[b[0]], pi[a[0]]
    assert transport(t, 0, pi) == (t, 1)
    assert transport(t, 1, pi) == (t, 0)

permutations = list(itertools.permutations(AXES))
assert len(permutations) == 720
checks = 0
for pi in permutations:
    for t in triads:
        t2 = tuple(sorted(permute(p, pi) for p in t))
        assert (t2, 0) in oriented
        for chi in (0, 1):
            image_t, image_chi = transport(t, chi, pi)
            assert image_t == t2 and (image_t, image_chi) in oriented
            for hidden in t:
                visible = tuple(sorted(p for p in t if p != hidden))
                visible2 = tuple(sorted(permute(p, pi) for p in visible))
                assert (t2, image_chi, permute(hidden, pi)) in lifts[visible2]
                checks += 1
assert checks == 691200

for visible, members in lifts.items():
    hidden_count = Counter(m[2] for m in members)
    assert len(hidden_count) == 8 and set(hidden_count.values()) == {2}
    rest = [i for i in AXES if i not in {visible[0][0], visible[1][0]}]
    assert len(rest) == 4
    for hidden in [p for p in PORTS if p[0] in rest]:
        other = next(a for a in rest if a != hidden[0])
        pi = list(AXES)
        pi[hidden[0]], pi[other] = pi[other], pi[hidden[0]]
        assert {permute(v, pi) for v in visible} == set(visible)
        assert permute(hidden, pi) != hidden

stabs = {k: math.factorial(k) * math.factorial(3-k) * 6
         for k in range(4)}
assert [stabs[k] for k in range(4)] == [36, 12, 12, 36]
evidence = {
    "schema": "R762K_SIGNED_X6_TRIAD_INCIDENCE_V1",
    "axisCount": 6,
    "scope": "exact N-BRC unit-weight branch incidences only, not an admitted physical force event",
    "signedPortCount": len(PORTS),
    "unsignedAxisTripleCount": 20,
    "signedUnorderedTriads": len(triads),
    "cyclicallyOrientedSignedTriads": len(oriented),
    "visibleUnorderedSignedPairs": len(lifts),
    "thirdSignedPortLiftsPerVisiblePair": 8,
    "orientedLiftsPerVisiblePair": 16,
    "minimumFixedWidthRepairBits": {"thirdPort": 3, "thirdPortAndOrientation": 4},
    "incidenceTotal": sum(map(len, lifts.values())),
    "triadOrbitsByNegativePortCount": {k: unsigned_orbits[k] for k in range(4)},
    "orientedTriadOrbitsByNegativePortCount": {k: oriented_orbits[k] for k in range(4)},
    "unorientedStabilizersByNegativePortCount": stabs,
    "orientedStabilizersByNegativePortCount": {k: stabs[k]//2 for k in range(4)},
    "S6Size": len(permutations),
    "stabilizerParityObstructionCheckedForAll160": True,
    "fullS6ProjectionEquivarianceChecks": checks,
    "allChecks": "PASS",
}
print(json.dumps(evidence, indent=2, ensure_ascii=False))
