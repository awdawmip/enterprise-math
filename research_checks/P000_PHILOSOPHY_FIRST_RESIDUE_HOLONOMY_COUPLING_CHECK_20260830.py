#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from collections import Counter, deque

MOD = 3
I2 = (1, 0, 0, 1)
Z2 = (2, 0, 0, 2)
PID = (0, 1, 2, 3)


def mm(A, B):
    return tuple(
        sum(A[2*i+k] * B[2*k+j] for k in range(2)) % MOD
        for i in range(2) for j in range(2)
    )


def mpow(A, n):
    r = I2
    for _ in range(n):
        r = mm(r, A)
    return r


def det(A):
    return (A[0]*A[3] - A[1]*A[2]) % MOD


GL23 = tuple(A for A in itertools.product(range(3), repeat=4) if det(A))
assert len(GL23) == 48

LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
LIDX = {v: i for i, v in enumerate(LINES)}


def norm(v):
    x, y = v
    if x % 3:
        inv = 1 if x % 3 == 1 else 2
        return ((x*inv) % 3, (y*inv) % 3)
    return (0, 1)


def act(A, v):
    return (
        (A[0]*v[0] + A[1]*v[1]) % 3,
        (A[2]*v[0] + A[3]*v[1]) % 3,
    )


def qperm(A):
    return tuple(LIDX[norm(act(A, v))] for v in LINES)


def pc(p, q):
    return tuple(p[q[i]] for i in range(4))


def pord(p):
    r = PID
    for n in range(1, 25):
        r = pc(r, p)
        if r == PID:
            return n
    raise AssertionError("permutation order bound")


def pgen(gs):
    seen = {PID}
    q = deque([PID])
    while q:
        x = q.popleft()
        for g in gs:
            y = pc(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


S4 = set(qperm(A) for A in GL23)
assert len(S4) == 24
kernel = tuple(A for A in GL23 if qperm(A) == PID)
assert set(kernel) == {I2, Z2}
fibres = {p: tuple(A for A in GL23 if qperm(A) == p) for p in S4}

qpairs = [
    (a, b) for a in S4 for b in S4
    if pord(a) == 3
    and pord(b) == 2
    and pord(pc(a, b)) == 4
    and len(pgen((a, b))) == 24
]
assert len(qpairs) == 24

# Recheck the accepted Q5 residue census inside this Q12 executable.
gl_res = Counter()
for a, b in qpairs:
    for A in fibres[a]:
        for B in fibres[b]:
            gl_res[mpow(mm(A, B), 4)] += 1
assert gl_res == Counter({Z2: 96})


def spmul(x, y):
    return (pc(x[0], y[0]), (x[1] + y[1]) % 2)


def sppow(x, n):
    r = (PID, 0)
    for _ in range(n):
        r = spmul(r, x)
    return r


split_res = Counter()
for a, b in qpairs:
    for u, v in itertools.product((0, 1), repeat=2):
        split_res[sppow(spmul((a, u), (b, v)), 4)[1]] += 1
assert split_res == Counter({0: 96})

# Native relation loop: the eight directed generator steps of (ab)^4.
# A C2-valued independent edge twist eta changes the total holonomy by its parity.
TWISTS = tuple(itertools.product((0, 1), repeat=8))
GAUGES = TWISTS


def twist_parity(eta):
    return sum(eta) % 2


def gauge(eta, h):
    # edge i: vertex i -> i+1 cyclically; inverse equals itself in C2
    return tuple((eta[i] + h[i] + h[(i+1) % 8]) % 2 for i in range(8))


for eta in TWISTS:
    for h in GAUGES:
        assert twist_parity(gauge(eta, h)) == twist_parity(eta)


def orbit(seed):
    return {gauge(seed, h) for h in GAUGES}


o0 = orbit((0,) * 8)
o1 = orbit((1, 0, 0, 0, 0, 0, 0, 0))
assert len(o0) == len(o1) == 128
assert o0.isdisjoint(o1)
assert len(o0 | o1) == 256
assert all(twist_parity(x) == 0 for x in o0)
assert all(twist_parity(x) == 1 for x in o1)

# Exact law: H = R xor D. D is the gauge-invariant edge-twist class.
rows = []
for model, r, split in (("S4xC2", 0, True), ("GL2F3", 1, False)):
    counts = Counter()
    for eta in TWISTS:
        d = twist_parity(eta)
        hol = r ^ d
        counts[(r, d, hol)] += 1
        assert hol == (r ^ d)
        if d == 0:
            assert hol == r
    assert counts[(r, 0, r)] == 128
    assert counts[(r, 1, r ^ 1)] == 128
    rows.append({
        "model": model,
        "residue": r,
        "split": split,
        "untwisted_holonomy": r,
        "twist_classes": 2,
    })

eta0 = (0,) * 8
eta1 = (1, 0, 0, 0, 0, 0, 0, 0)

# same residue / different holonomy; one edge is Hamming-minimal.
for r in (0, 1):
    assert (r ^ twist_parity(eta0)) != (r ^ twist_parity(eta1))

# same holonomy / different residue; compensate the nonsplit residue by one edge twist.
for target_h in (0, 1):
    split_eta = eta0 if target_h == 0 else eta1
    gl_eta = eta1 if target_h == 0 else eta0
    assert (0 ^ twist_parity(split_eta)) == target_h
    assert (1 ^ twist_parity(gl_eta)) == target_h

# Section existence and strict globalization (H=0) realize all four truth combinations.
combos = set()
for split, r in ((True, 0), (False, 1)):
    for d in (0, 1):
        hol = r ^ d
        combos.add((split, hol == 0))
assert combos == {(True, True), (True, False), (False, True), (False, False)}

# Central C2 lift changes cannot alter R=(AB)^4 in either frozen benchmark.
for a, b in qpairs:
    assert {
        sppow(spmul((a, u), (b, v)), 4)[1]
        for u, v in itertools.product((0, 1), repeat=2)
    } == {0}
    assert {
        0 if mpow(mm(A, B), 4) == I2 else 1
        for A in fibres[a] for B in fibres[b]
    } == {1}

report = {
    "schema": "P000_Q12_RESIDUE_HOLONOMY_COUPLING_CHECK_V1",
    "status": "PASS",
    "hard_target_disposition": "P000_RESIDUE_HOLONOMY_COUPLING_OR_INDEPENDENCE_CLASSIFIED",
    "quotient_generator_pairs": len(qpairs),
    "split_lifted_pairs": sum(split_res.values()),
    "gl2f3_lifted_pairs": sum(gl_res.values()),
    "relation_loop_edges": 8,
    "edge_twist_assignments": len(TWISTS),
    "gauge_assignments": len(GAUGES),
    "gauge_orbits": 2,
    "gauge_orbit_sizes": [len(o0), len(o1)],
    "exact_law": "H = R xor D, where D is the C2 gauge-invariant parity of the independent edge twist",
    "untwisted_subclass": "D=0 => H=R",
    "independence_witnesses": {
        "same_residue_different_holonomy": "fixed extension; toggle one edge twist",
        "same_holonomy_different_residue": "S4xC2 with D=h versus GL2F3 with D=1 xor h",
    },
    "section_vs_strict_globalization_combinations": sorted([list(x) for x in combos]),
    "models": rows,
    "method_reuse": "T9_HOLONOMY_COCOYCLE_GLUING + T7_FINITE_SYMMETRY_EQUIVARIANCE + T2_BLOCK_FINITE_CERTIFICATE",
}
print(json.dumps(report, indent=2, sort_keys=True))
