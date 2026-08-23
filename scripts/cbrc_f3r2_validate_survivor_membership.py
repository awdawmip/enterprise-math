#!/usr/bin/env python3
"""Deterministic validator for CBRC F3R2 survivor membership predicate.

Exact integer / finite-field / Fraction arithmetic only.
Bounded GL(2,Z) enumeration is regression evidence; completeness comes from
the theorem proved in the accompanying F3R2 report.
"""
from fractions import Fraction
from math import gcd
import hashlib
import itertools
import json

P = ((0, 1), (1, 0))
I2 = ((1, 0), (0, 1))
A0 = ((2, 3), (3, 4))

def det2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def mmul(A, B):
    return (
        (A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        (A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    )

def mvec(A, v):
    return (
        A[0][0]*v[0] + A[0][1]*v[1],
        A[1][0]*v[0] + A[1][1]*v[1],
    )

def inv2(A):
    d = det2(A)
    assert d in (1, -1)
    return (
        (A[1][1]//d, -A[0][1]//d),
        (-A[1][0]//d, A[0][0]//d),
    )

def diag(s, t):
    return ((s, 0), (0, t))

SIGNS = [diag(s, t) for s in (1, -1) for t in (1, -1)]

def physical_free_orbit(A):
    seen = set()
    stack = [A]
    while stack:
        X = stack.pop()
        if X in seen:
            continue
        seen.add(X)
        for L in SIGNS:
            for R in SIGNS:
                stack.append(mmul(mmul(L, X), R))
        stack.append(mmul(mmul(P, X), P))
        stack.append(inv2(X))
    return seen

def free_canonical(A):
    return min(tuple(z for row in X for z in row) for X in physical_free_orbit(A))

def pair_gcds(A):
    a, b = A[0]
    c, d = A[1]
    return gcd(abs(a), abs(d)), gcd(abs(b), abs(c))

def survivor_free_predicate(A):
    if det2(A) not in (1, -1):
        return False
    g, h = pair_gcds(A)
    return g > 1 and h > 1

def full_membership_predicate(A, B, D):
    return survivor_free_predicate(A) and det2(D) % 3 != 0

def prime_factors(n):
    n = abs(n)
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out

def perm_type_mod(A, p):
    a, b = A[0][0] % p, A[0][1] % p
    c, d = A[1][0] % p, A[1][1] % p
    if a and d and not b and not c:
        return 0  # diagonal
    if b and c and not a and not d:
        return 1  # anti-diagonal
    return None

def in_support_stratum(A, p, r):
    tp = perm_type_mod(A, p)
    tr = perm_type_mod(A, r)
    return tp is not None and tr is not None and tp != tr

def union_support_predicate(A):
    if det2(A) not in (1, -1):
        return False
    g, h = pair_gcds(A)
    for p in prime_factors(g):
        for r in prime_factors(h):
            if p != r and in_support_stratum(A, p, r):
                return True
    return False

def q_pr(n, p, r):
    return Fraction((0 if n % p == 0 else 1) + (0 if n % r == 0 else 1), 2)

def check_q_pr_conservation(A, p, r):
    N = p*r
    for x, y in itertools.product(range(N), repeat=2):
        u, v = mvec(A, (x, y))
        assert q_pr(u, p, r) + q_pr(v, p, r) == q_pr(x, p, r) + q_pr(y, p, r)
    a, _ = A[0]
    c, _ = A[1]
    assert q_pr(0, p, r) == 0
    assert q_pr(1, p, r) == 1
    assert q_pr(a, p, r) == q_pr(c, p, r) == Fraction(1, 2)

def xgcd(a, b):
    if b == 0:
        return abs(a), 1 if a > 0 else -1, 0
    g, x1, y1 = xgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def invmod(a, m):
    g, x, _ = xgcd(a, m)
    assert g == 1
    return x % m

def crt2(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + ((b-a)*invmod(m, n) % n)*m) % (m*n)

def bezout_completion(a, c, eps):
    g, x, y = xgcd(a, c)
    assert g == 1
    # a*x + c*y = 1
    d0 = eps*x
    b0 = -eps*y
    assert a*d0 - c*b0 == eps
    return b0, d0

def completion_membership_by_crt(a, c, eps, k):
    b0, d0 = bezout_completion(a, c, eps)
    b, d = b0 + k*a, d0 + k*c
    A = ((a, b), (c, d))
    assert det2(A) == eps
    direct = survivor_free_predicate(A)
    by_union = False
    for p in prime_factors(a):
        kp = (-d0 * invmod(c, p)) % p
        if k % p != kp:
            continue
        for r in prime_factors(c):
            kr = (-b0 * invmod(a, r)) % r
            if k % r == kr:
                by_union = True
                break
        if by_union:
            break
    return direct, by_union, A

def all_gl2_f3():
    out = []
    for vals in itertools.product(range(3), repeat=4):
        M = ((vals[0], vals[1]), (vals[2], vals[3]))
        if det2(M) % 3:
            out.append(M)
    return out

def all_b_f3():
    return [((a,b),(c,d)) for a,b,c,d in itertools.product(range(3), repeat=4)]

GL3 = all_gl2_f3()
BS = all_b_f3()

def apply_affine_torsion(B, D, free_residue, torsion_pair):
    r1, r2 = free_residue
    t1, t2 = torsion_pair
    return (
        (B[0][0]*r1 + B[0][1]*r2 + D[0][0]*t1 + D[0][1]*t2) % 3,
        (B[1][0]*r1 + B[1][1]*r2 + D[1][0]*t1 + D[1][1]*t2) % 3,
    )

def check_torsion_affine_bijections():
    target = set(itertools.product(range(3), repeat=2))
    checks = 0
    for B in BS:
        for D in GL3:
            for r in itertools.product(range(3), repeat=2):
                images = {
                    apply_affine_torsion(B, D, r, t)
                    for t in itertools.product(range(3), repeat=2)
                }
                assert images == target
                checks += 1
    return checks

def bounded_gl2_regression(bound=9):
    tested = 0
    survivors = 0
    admissible_first_but_fail = 0
    mismatches = 0
    examples_outside = []
    for a,b,c,d in itertools.product(range(-bound, bound+1), repeat=4):
        A = ((a,b),(c,d))
        if det2(A) not in (1,-1):
            continue
        tested += 1
        pred = survivor_free_predicate(A)
        support = union_support_predicate(A)
        if pred:
            survivors += 1
            g,h = pair_gcds(A)
            p = prime_factors(g)[0]
            r = prime_factors(h)[0]
            assert in_support_stratum(A,p,r)
            check_q_pr_conservation(A,p,r)
        else:
            if abs(a)>=2 and abs(c)>=2:
                admissible_first_but_fail += 1
                if len(examples_outside) < 8:
                    examples_outside.append(A)
        if pred != support:
            mismatches += 1
    assert mismatches == 0
    return {
        "bound": bound,
        "tested_unimodular": tested,
        "predicted_survivors": survivors,
        "admissible_first_but_fail": admissible_first_but_fail,
        "support_union_mismatches": mismatches,
        "outside_examples": examples_outside,
    }

def check_completion_parameterization():
    checked = 0
    mismatches = 0
    for a,c in itertools.product(range(-12,13), repeat=2):
        if abs(a)<2 or abs(c)<2 or gcd(abs(a),abs(c)) != 1:
            continue
        for eps in (1,-1):
            for k in range(-30,31):
                direct, by_union, A = completion_membership_by_crt(a,c,eps,k)
                checked += 1
                if direct != by_union:
                    mismatches += 1
    assert mismatches == 0
    return {"checked": checked, "mismatches": mismatches}

def check_physical_invariance():
    samples = [
        A0,
        ((2, 9), (3, 14)),   # det 1, g=2,h=3
        ((2, 1), (3, 1)),    # smallest direct no-go
        ((2, 5), (3, 7)),    # outside all S
        ((3, 14), (5, 23)),  # det -1? checked below if used
    ]
    checked = 0
    for A in samples:
        if det2(A) not in (1,-1):
            continue
        g,h = pair_gcds(A)
        pred = survivor_free_predicate(A)
        for X in physical_free_orbit(A):
            assert pair_gcds(X) == (g,h)
            assert survivor_free_predicate(X) == pred
            checked += 1
    return checked

def check_known_and_outside_examples():
    assert survivor_free_predicate(A0)
    assert pair_gcds(A0) == (2,3)
    for t in range(-20,21):
        A = ((2,12*t+3),(3,18*t+4))
        assert det2(A) == -1
        assert survivor_free_predicate(A)
        assert in_support_stratum(A,2,3)
    bad = {
        "smallest_axis_certificate": ((2,1),(3,1)),
        "both_pair_gcds_one": ((2,5),(3,7)),
        "g_one_h_three": ((2,3),(3,5)),
        "g_two_h_one": ((2,1),(3,2)),
    }
    for A in bad.values():
        assert det2(A) in (1,-1)
        assert abs(A[0][0])>=2 and abs(A[1][0])>=2
        assert not survivor_free_predicate(A)
        assert not union_support_predicate(A)
    # Explicit smallest certificate for [[2,1],[3,1]]:
    # input (0,e) -> free outputs (e,e), so q(e)+q(e)=q(0)+q(e), i.e. 2=1.
    A = bad["smallest_axis_certificate"]
    assert mvec(A,(0,1)) == (1,1)
    return bad

def check_lift_counts():
    assert len(BS) == 81
    assert len(GL3) == 48
    good = A0
    bad = ((2,5),(3,7))
    good_count = sum(full_membership_predicate(good,B,D) for B in BS for D in GL3)
    bad_count = sum(full_membership_predicate(bad,B,D) for B in BS for D in GL3)
    assert good_count == 3888
    assert bad_count == 0
    return {"good_lifts": good_count, "bad_lifts": bad_count}

def main():
    assert det2(A0) == -1
    assert pair_gcds(A0) == (2,3)

    bad_examples = check_known_and_outside_examples()
    regression = bounded_gl2_regression()
    completion = check_completion_parameterization()
    lift_counts = check_lift_counts()
    torsion_bijection_checks = check_torsion_affine_bijections()
    physical_checks = check_physical_invariance()

    payload = {
        "schema": "CBRC_F3R2_MEMBERSHIP_CHECK_V1",
        "primary_predicate": "det(A)=+-1 and gcd(|a|,|d|)>1 and gcd(|b|,|c|)>1; B arbitrary; D in GL(2,F3)",
        "support_union_identity": "SurvivorFree = union_{p!=r} S_{p,r}",
        "outside_support_survivors_exist": False,
        "all_lifts_of_free_survivor": True,
        "torsion_sensitive_only_lifts_exist": False,
        "canonical_A0_pair_gcds": list(pair_gcds(A0)),
        "known_outside_examples": {k:[list(v[0]),list(v[1])] for k,v in bad_examples.items()},
        "bounded_regression": regression,
        "completion_parameterization": completion,
        "lift_counts": lift_counts,
        "torsion_affine_bijection_checks": torsion_bijection_checks,
        "physical_equivalence_checks": physical_checks,
        "theorem_enumeration_mismatches": 0,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",",":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps({"deterministic_digest": digest, "payload": payload}, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
