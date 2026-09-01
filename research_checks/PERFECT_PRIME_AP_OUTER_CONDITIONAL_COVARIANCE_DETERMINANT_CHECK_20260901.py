#!/usr/bin/env python3
"""Exact obstruction checker for the Perfect Prime outer covariance task.

All arithmetic is fractions.Fraction. This checker proves a finite exact
counterexample to the canonical monomial-flag / one-by-one Sylvester-LDL
sign-regularity mechanism at m=15, t=4/5. It does NOT refute the full
determinant nonvanishing target or the conjectured inertia.
"""
from __future__ import annotations

import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
from fractions import Fraction as F
from math import comb, factorial


def det(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a)
    if n == 0:
        return F(1)
    out = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out
        q = a[c][c]
        out *= q
        for j in range(c, n):
            a[c][j] /= q
        for r in range(c + 1, n):
            q = a[r][c]
            if q:
                for j in range(c, n):
                    a[r][j] -= q * a[c][j]
    return out


def c_js(m, j, s):
    n = m - 1
    z = m * j + m * m * s
    den = 1
    for r in range(1, m + 1):
        den *= z + r
    return F(factorial(n), den)


def inner_covariance(m, j, t):
    n = m - 1
    b = m * m
    y = m * j
    lam = [
        F((-1) ** s * comb(n, s)) * t ** s * c_js(m, j, s)
        for s in range(n + 1)
    ]
    D = sum(lam)
    assert D > 0
    moments = [
        sum(lam[s] * F((y + b * s) ** r) for s in range(n + 1))
        for r in range(2 * n + 1)
    ]
    C = [
        [
            moments[r + q] - moments[r] * moments[q] / D
            for q in range(1, n + 1)
        ]
        for r in range(1, n + 1)
    ]
    return C


def outer_covariance(m, t):
    n = m - 1
    S = [[F(0) for _ in range(n)] for __ in range(n)]
    for j in range(n + 1):
        C = inner_covariance(m, j, t)
        w = F((-1) ** j * comb(n, j))
        for r in range(n):
            for q in range(n):
                S[r][q] += w * C[r][q]
    return S


def frac_sha256(q):
    text = f"{q.numerator}/{q.denominator}".encode("ascii")
    return "sha256:" + hashlib.sha256(text).hexdigest()


def sign(q):
    return 1 if q > 0 else -1 if q < 0 else 0


def expected_flag_sign(k):
    return -1 if ((k + 1) // 2) % 2 else 1


def leading_minors(m, t):
    S = outer_covariance(m, t)
    return [det([row[:k] for row in S[:k]]) for k in range(1, m)]


def main():
    m = 15
    target_t = F(4, 5)
    ds = leading_minors(m, target_t)
    signs = [sign(d) for d in ds]
    expected = [expected_flag_sign(k) for k in range(1, m)]
    assert all(s != 0 for s in signs)

    # Exact obstruction: the canonical flag sign theorem fails only at k=12
    # for this witness.
    mismatches = [k for k in range(1, m) if signs[k - 1] != expected[k - 1]]
    assert mismatches == [12]
    assert ds[10] > 0   # Delta_11
    assert ds[11] < 0   # Delta_12, expected positive under the rejected theorem
    assert ds[12] < 0   # Delta_13
    assert ds[13] < 0   # full det S_15(4/5) is nonzero

    # One-by-one LDL pivots are Delta_k/Delta_{k-1}.  The 12th/13th pivot
    # signs swap relative to strict alternation, while the total inertia count
    # remains 7 positive and 7 negative.
    pivot_signs = [sign(ds[0])]
    for k in range(1, len(ds)):
        pivot_signs.append(sign(ds[k] / ds[k - 1]))
    assert pivot_signs.count(1) == 7
    assert pivot_signs.count(-1) == 7
    assert pivot_signs[11] == -1
    assert pivot_signs[12] == 1

    # Exact sign reversal on either side proves at least two interior zeros of
    # the 12th leading principal minor by continuity; all D_j(t)>0 on [0,1].
    S_34 = outer_covariance(m, F(3, 4))
    S_1 = outer_covariance(m, F(1))
    d12_34 = det([row[:12] for row in S_34[:12]])
    d12_45 = ds[11]
    d12_1 = det([row[:12] for row in S_1[:12]])
    assert d12_34 > 0
    assert d12_45 < 0
    assert d12_1 > 0

    payload = {
        "schema": "PERFECT_PRIME_AP_OUTER_COVARIANCE_FLAG_OBSTRUCTION_CERT_V1",
        "arithmetic": "exact Python fractions.Fraction",
        "task_id": "RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT",
        "witness": {"m": 15, "t": "4/5", "basis": "canonical quotient monomials X,...,X^14"},
        "leading_minor_signs_k1_to_k14": signs,
        "rejected_universal_flag_pattern_k1_to_k14": expected,
        "mismatch_orders": mismatches,
        "ldl_pivot_signs_k1_to_k14": pivot_signs,
        "inertia_from_nonzero_ldl_pivots": {"positive": 7, "negative": 7, "zero": 0},
        "full_outer_determinant": {
            "sign": sign(ds[-1]),
            "nonzero": ds[-1] != 0,
            "canonical_fraction_sha256": frac_sha256(ds[-1]),
            "numerator_bits": abs(ds[-1].numerator).bit_length(),
            "denominator_bits": ds[-1].denominator.bit_length(),
        },
        "delta_12": {
            "at_3/4": {"sign": sign(d12_34), "canonical_fraction_sha256": frac_sha256(d12_34)},
            "at_4/5": {"sign": sign(d12_45), "canonical_fraction_sha256": frac_sha256(d12_45)},
            "at_1": {"sign": sign(d12_1), "canonical_fraction_sha256": frac_sha256(d12_1)},
            "continuity_consequence": "at least one zero in (3/4,4/5) and at least one zero in (4/5,1)",
        },
        "delta_11_at_4/5_sha256": frac_sha256(ds[10]),
        "delta_13_at_4/5_sha256": frac_sha256(ds[12]),
        "classification": "EXACT_CANONICAL_FLAG_SIGN_REGULARITY_OBSTRUCTION",
        "scope": (
            "Refutes the universal canonical-monomial-flag / strict alternating "
            "one-by-one LDL pivot mechanism. Does not refute det S_m(t)!=0 or the "
            "7+7 inertia at the witness."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
