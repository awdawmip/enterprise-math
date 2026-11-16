#!/usr/bin/env python3
"""Exact modular certificate: 8 readings separate every q != p in [6, 1000].

This program uses only Python 3 integer arithmetic. No floating point,
probabilistic testing, numerical root finding, or trust in modular inverses as
substitutes for integer statements. Nonzero reduction modulo a prime proves
that the original integer determinant is nonzero.
"""
import hashlib
import json
from math import factorial

Q_MIN, Q_MAX, OBS, PRIME = 6, 1000, 8, 1_000_000_007
MAX_ARG = Q_MAX + 6 * (OBS - 1)
WEIGHTS = (1, 1, 2, 3, 6)


def counts(max_q):
    # Four labeled source coordinates k2,k3,k4,k5 with weights (1,2,3,6).
    # Each is a genuine multiplicity-bearing nonnegative integer coordinate.
    base = [0] * max_q
    base[0] = 1
    for w in WEIGHTS[1:]:
        for n in range(w, max_q):
            base[n] += base[n - w]
    c, t = [0] * (max_q + 1), [0] * (max_q + 1)
    prefix_count = prefix_weight = 0
    for q in range(1, max_q + 1):
        n = q - 1
        prefix_count += base[n]
        prefix_weight += n * base[n]
        c[q] = c[q - 1] + prefix_count
        t[q] = t[q - 1] + n * prefix_count - prefix_weight
    return c, t


def S(n):
    return 18 * n**4 + 54 * n**3 - 345 * n**2 + 2070 * n - 16315


def lifted_row(q, p, j, c, t, cube, s):
    a, b = q + 6 * j, p + 6 * j
    ca, ta, cb, tb = c[a], t[a], c[b], t[b]
    ds = s[a] - s[b]  # S(a)-S(b): no division, as matrix is scaled by 108.
    aa, bb = cube[a], cube[b]
    # Monomials [1, e, d, E, D, e*D, E*d, d*D].
    return (
        108 * (aa * ta * cb - bb * tb * ca) - ds * ca * cb,
        108 * aa * cb,
        -108 * bb * tb - ds * cb,
        -108 * bb * ca,
        108 * aa * ta - ds * ca,
        108 * aa,
        -108 * bb,
        -ds,
    )


def determinant_mod(rows, prime):
    a = [[x % prime for x in row] for row in rows]
    det = 1
    n = len(a)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        z = a[k][k]
        det = (det * z) % prime
        zi = pow(z, -1, prime)
        for i in range(k + 1, n):
            f = a[i][k] * zi % prime
            if f:
                a[i][k] = 0
                for j in range(k + 1, n):
                    a[i][j] = (a[i][j] - f * a[k][j]) % prime
    return det % prime


def main():
    C, T = counts(MAX_ARG)
    assert (C[6], T[6], C[12], T[12]) == (41, 50, 380, 881)
    cubes = [i**3 for i in range(MAX_ARG + 1)]
    ss = [S(i) for i in range(MAX_ARG + 1)]
    digest = hashlib.sha256()
    min_residue, max_residue = PRIME, 0
    checked = 0
    # Entire finite domain, not a sample. Ordered q<p, since swapping
    # q and p does not change whether their lifted matrix is singular.
    for q in range(Q_MIN, Q_MAX):
        for p in range(q + 1, Q_MAX + 1):
            rows = [lifted_row(q, p, j, C, T, cubes, ss)
                    for j in range(OBS)]
            v = determinant_mod(rows, PRIME)
            if v == 0:
                raise AssertionError(f"zero modular determinant for ({q},{p})")
            digest.update(v.to_bytes(4, "big"))
            min_residue = min(min_residue, v)
            max_residue = max(max_residue, v)
            checked += 1
    assert checked == (Q_MAX - Q_MIN + 1) * (Q_MAX - Q_MIN) // 2

    # Simple fully explicit universal entry bound; intentionally conservative.
    A = MAX_ARG
    B = 18*A**4 + 54*A**3 + 345*A**2 + 2070*A + 16315
    Ds = 2 * B
    R = A**3
    Cm, Tm = C[MAX_ARG], T[MAX_ARG]
    M = 216*R*Tm*Cm + Ds*Cm**2 + 108*R*(Tm+Cm+1) + Ds*(Cm+1)
    # Every entry of every integer lifted matrix is bounded in modulus by M.
    # |det A|>=1; each 7x7 cofactor <= 7! M^7. Since z_0=1,
    # 1 <= 8*7! M^7 * 108*(Cm+2)^2 * ||Y_q-Y_p||_infinity.
    gap_denominator = 108 * OBS * factorial(OBS-1) * (Cm + 2)**2 * M**(OBS-1)

    result = {
        "status": "PASS",
        "id": "R749SSX",
        "scope": "auxiliary five-labeled-source scalar observer, q,p integers in [6,1000], q!=p; continuous common errors within each candidate [-2,2]^2",
        "weights": WEIGHTS,
        "frozen_scientific_input": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "observations": OBS,
        "six_step_spacing": 6,
        "candidate_range_inclusive": [Q_MIN, Q_MAX],
        "unordered_pairs_exhaustively_checked": checked,
        "determinant_prime": PRIME,
        "zero_mod_prime_count": 0,
        "determinant_residue_stream_sha256": digest.hexdigest(),
        "min_nonzero_residue": min_residue,
        "max_nonzero_residue": max_residue,
        "source_count_witness": {"C6": C[6], "T6": T[6], "C12": C[12], "T12": T[12]},
        "max_observation_argument": MAX_ARG,
        "max_C": str(Cm),
        "max_T": str(Tm),
        "entry_absolute_bound_M": str(M),
        "uniform_pair_gap_lower_bound_strict_or_equal": f"1/{gap_denominator}",
        "gap_denominator_decimal_digits": len(str(gap_denominator)),
        "strict_noise_per_observation_sufficient": f"epsilon < 1/{2*gap_denominator}",
        "certificate": "nonzero integer 8x8 determinant from exact matrix, proved by nonzero modular reduction for every pair; adjugate and integer determinant bound",
        "not_claimed": "unbounded-cutoff eight-read theorem; sharp gap; native X6/BRC identification",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
