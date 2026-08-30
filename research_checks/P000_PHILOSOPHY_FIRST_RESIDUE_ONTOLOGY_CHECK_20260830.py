#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from collections import Counter

MOD = 3
I2 = (1, 0, 0, 1)
NEG_I2 = (2, 0, 0, 2)


def mm(A, B):
    return tuple(
        sum(A[2*i+k] * B[2*k+j] for k in range(2)) % MOD
        for i in range(2) for j in range(2)
    )


def mpow(A, n):
    R = I2
    for _ in range(n):
        R = mm(R, A)
    return R


def mdet(A):
    return (A[0]*A[3] - A[1]*A[2]) % MOD


def mord(A, limit=96):
    R = I2
    for n in range(1, limit + 1):
        R = mm(R, A)
        if R == I2:
            return n
    raise AssertionError("matrix order limit exceeded")


GL23 = tuple(A for A in itertools.product(range(3), repeat=4) if mdet(A) != 0)
assert len(GL23) == 48

PROJECTIVE_LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
LINE_INDEX = {v: i for i, v in enumerate(PROJECTIVE_LINES)}


def norm_line(v):
    x, y = v
    if x % MOD:
        inv = 1 if x % MOD == 1 else 2
        return ((x * inv) % MOD, (y * inv) % MOD)
    assert y % MOD
    return (0, 1)


def act_vec(A, v):
    return (
        (A[0]*v[0] + A[1]*v[1]) % MOD,
        (A[2]*v[0] + A[3]*v[1]) % MOD,
    )


def projective_perm(A):
    return tuple(LINE_INDEX[norm_line(act_vec(A, v))] for v in PROJECTIVE_LINES)


# Permutation helpers; p*q means p after q.
PID = (0, 1, 2, 3)


def pc(p, q):
    return tuple(p[q[i]] for i in range(4))


def ppow(p, n):
    r = PID
    for _ in range(n):
        r = pc(r, p)
    return r


def pord(p):
    r = PID
    for n in range(1, 25):
        r = pc(r, p)
        if r == PID:
            return n
    raise AssertionError("permutation order limit exceeded")


def pgen(gens):
    S = {PID}
    changed = True
    while changed:
        changed = False
        for x in tuple(S):
            for g in gens:
                y = pc(x, g)
                if y not in S:
                    S.add(y)
                    changed = True
    return S


S4 = set(projective_perm(A) for A in GL23)
assert len(S4) == 24
kernel = tuple(A for A in GL23 if projective_perm(A) == PID)
assert set(kernel) == {I2, NEG_I2}
assert all(mm(NEG_I2, A) == mm(A, NEG_I2) for A in GL23)

# All quotient generator pairs with presentation type (3,2,4) and full image.
quotient_pairs = [
    (a, b)
    for a in S4 for b in S4
    if pord(a) == 3
    and pord(b) == 2
    and pord(pc(a, b)) == 4
    and len(pgen((a, b))) == 24
]
assert len(quotient_pairs) == 24

fibres = {p: tuple(A for A in GL23 if projective_perm(A) == p) for p in S4}
assert all(len(f) == 2 for f in fibres.values())

# GL(2,3): exhaust every lift of every frozen-presentation generator pair.
gl_signatures = Counter()
gl_lift_orders = Counter()
for qa, qb in quotient_pairs:
    for A in fibres[qa]:
        for B in fibres[qb]:
            za = mpow(A, 3)
            zb = mpow(B, 2)
            zab = mpow(mm(A, B), 4)
            assert za in kernel and zb in kernel and zab in kernel
            gl_signatures[(za, zb, zab)] += 1
            gl_lift_orders[(mord(A), mord(B), mord(mm(A, B)))] += 1

assert sum(gl_signatures.values()) == 96
assert gl_signatures == Counter({
    (I2, I2, NEG_I2): 48,
    (NEG_I2, I2, NEG_I2): 48,
})
assert gl_lift_orders == Counter({(3, 2, 8): 48, (6, 2, 8): 48})

# One explicit clean witness: A^3=B^2=I but (AB)^4=-I.
A0 = (0, 1, 2, 2)
B0 = (1, 0, 0, 2)
assert A0 in GL23 and B0 in GL23
assert mpow(A0, 3) == I2
assert mpow(B0, 2) == I2
assert mpow(mm(A0, B0), 4) == NEG_I2
assert mord(A0) == 3 and mord(B0) == 2 and mord(mm(A0, B0)) == 8
assert pord(projective_perm(A0)) == 3
assert pord(projective_perm(B0)) == 2
assert pord(pc(projective_perm(A0), projective_perm(B0))) == 4
assert len(pgen((projective_perm(A0), projective_perm(B0)))) == 24

# Exact 4-cycle lift profile is a quotient-free enriched invariant.
gl_fourcycle_profiles = Counter(
    tuple(sorted(mord(A) for A in fibres[p]))
    for p in S4 if pord(p) == 4
)
assert gl_fourcycle_profiles == Counter({(8, 8): 6})

# Split comparison E=S4 x C2.  Multiplication is componentwise.
def split_mul(x, y):
    return (pc(x[0], y[0]), (x[1] + y[1]) % 2)


def split_pow(x, n):
    r = (PID, 0)
    for _ in range(n):
        r = split_mul(r, x)
    return r


def split_ord(x):
    r = (PID, 0)
    for n in range(1, 49):
        r = split_mul(r, x)
        if r == (PID, 0):
            return n
    raise AssertionError("split order limit exceeded")

split_signatures = Counter()
split_lift_orders = Counter()
for qa, qb in quotient_pairs:
    for ea in (0, 1):
        for eb in (0, 1):
            A = (qa, ea)
            B = (qb, eb)
            za = split_pow(A, 3)
            zb = split_pow(B, 2)
            zab = split_pow(split_mul(A, B), 4)
            split_signatures[(za[1], zb[1], zab[1])] += 1
            split_lift_orders[(split_ord(A), split_ord(B), split_ord(split_mul(A, B)))] += 1

assert split_signatures == Counter({(0, 0, 0): 48, (1, 0, 0): 48})
assert split_lift_orders == Counter({(3, 2, 4): 48, (6, 2, 4): 48})

split_fourcycle_profiles = Counter(
    tuple(sorted(split_ord((p, eps)) for eps in (0, 1)))
    for p in S4 if pord(p) == 4
)
assert split_fourcycle_profiles == Counter({(4, 4): 6})

# Minimal-order statement: any nontrivial kernel over |S4|=24 has order >=48.
assert len(GL23) == 48
assert 24 * 2 == 48

report = {
    "schema": "P000_Q5_RESIDUE_ONTOLOGY_CHECK_V1",
    "status": "PASS",
    "base_readout": {
        "projective_line_count": len(PROJECTIVE_LINES),
        "projective_image_order": len(S4),
        "kernel": [list(I2), list(NEG_I2)],
        "kernel_order": len(kernel),
        "presentation_generator_pairs": len(quotient_pairs),
    },
    "split_S4xC2": {
        "order": 48,
        "lifted_pair_count": sum(split_signatures.values()),
        "residue_signatures_C2_bits": {
            str(k): v for k, v in sorted(split_signatures.items(), key=lambda kv: str(kv[0]))
        },
        "lift_order_signatures": {
            str(k): v for k, v in sorted(split_lift_orders.items())
        },
        "four_cycle_lift_profiles": {
            str(k): v for k, v in split_fourcycle_profiles.items()
        },
        "classification": "NONZERO_ZA_CAN_BE_PRESENTATION_ARTIFACT; SPLIT_SECTION_EXISTS",
    },
    "GL2F3": {
        "order": len(GL23),
        "projective_quotient": "S4 via action on P^1(F3)",
        "lifted_pair_count": sum(gl_signatures.values()),
        "residue_signatures": {
            str(k): v for k, v in sorted(gl_signatures.items(), key=lambda kv: str(kv[0]))
        },
        "lift_order_signatures": {
            str(k): v for k, v in sorted(gl_lift_orders.items())
        },
        "four_cycle_lift_profiles": {
            str(k): v for k, v in gl_fourcycle_profiles.items()
        },
        "explicit_witness": {
            "A": list(A0),
            "B": list(B0),
            "A3": list(mpow(A0, 3)),
            "B2": list(mpow(B0, 2)),
            "AB4": list(mpow(mm(A0, B0), 4)),
            "ord_A": mord(A0),
            "ord_B": mord(B0),
            "ord_AB": mord(mm(A0, B0)),
        },
        "classification": "ZAB=-I FOR EVERY ALLOWED LIFT; ENRICHED_INVARIANT_AND_NO_SECTION_OBSTRUCTION",
    },
    "minimality": "Both nontrivial-kernel benchmarks have order 48 = 24*2, the minimum possible over S4.",
    "hard_target_disposition": "NONTRIVIAL_RESIDUE_INVARIANT_CLASSIFIED_ON_MINIMAL_CENTRAL_C2_EXTENSION_BENCHMARKS",
}
print(json.dumps(report, indent=2, sort_keys=True))
