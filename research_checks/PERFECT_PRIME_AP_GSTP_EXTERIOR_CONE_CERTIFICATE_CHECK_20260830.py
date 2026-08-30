#!/usr/bin/env python3
"""Exact regression/counterexample checker for the AP GSTP exterior-cone task.

Pure stdlib / Fraction arithmetic.  The decisive certificate is the actual AP
operator at m=10: after removing the known eigenvalue 1, its degree-9 quotient
characteristic polynomial has exactly seven real roots, all in (0,1), and no
real roots on (-inf,0) or (1,inf).  Hence the remaining two roots are a
non-real conjugate pair.  The same exact quotient is nonzero at lambda=1, so
the parent fixed-point exclusion survives at m=10.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math


EXPECTED_T10_SHA256 = "80110c201bd8d08de474484f4caa4fe2207e523aca3dfd5c664896287634f617"
EXPECTED_Q10_CHARPOLY_SHA256 = "2c1e58b54a999a84bc9a89b0fadf090dd2e836eaa42c4a803415370382350fae"
EXPECTED_Q10_AT_ONE_SHA256 = "a8dd130f9c473546c667b5215d6ef291d35dde20b1ec8912e20d3ea8b3ea6f5b"

EXPECTED_ROOT_COUNTS = {
    2: (0, 1, 0),
    3: (0, 2, 0),
    4: (0, 3, 0),
    5: (0, 4, 0),
    6: (0, 5, 0),
    7: (0, 6, 0),
    8: (0, 7, 0),
    9: (0, 8, 0),
    10: (0, 7, 0),
}


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def eye(n: int):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(a, b):
    n, p, q = len(a), len(b), len(b[0])
    assert len(a[0]) == p
    return [
        [sum(a[i][k] * b[k][j] for k in range(p)) for j in range(q)]
        for i in range(n)
    ]


def add_scalar_identity(a, c: Fraction):
    n = len(a)
    return [
        [a[i][j] + (c if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def build_operator(m: int, cauchy: bool = False):
    n = m - 1
    if cauchy:
        h = [[Fraction(1, i + m * j + 1) for j in range(m)] for i in range(m)]
    else:
        h = []
        for i in range(m):
            row = []
            for j in range(m):
                q = i + m * j
                den = 1
                for ell in range(m):
                    den *= q + 1 + ell * m * m
                row.append(Fraction(1, den))
            h.append(row)

    w = [Fraction(((-1) ** i) * math.comb(n, i)) for i in range(m)]
    e = [sum(h[i][j] * w[j] for j in range(m)) for i in range(m)]
    d = [sum(h[i][j] * w[i] for i in range(m)) for j in range(m)]
    assert all(x > 0 for x in e + d)

    a = [[h[i][j] * w[j] / e[i] for j in range(m)] for i in range(m)]
    b = [[h[j][i] * w[j] / d[i] for j in range(m)] for i in range(m)]
    r = [
        [
            Fraction(((-1) ** j) * math.comb(i, j)) if j <= i else Fraction(0)
            for j in range(m)
        ]
        for i in range(m)
    ]

    k = matmul(b, a)
    t = matmul(matmul(r, k), r)
    ones = [Fraction(1) for _ in range(m)]
    assert matvec(a, ones) == ones
    assert matvec(b, ones) == ones
    assert matvec(t, [Fraction(1)] + [Fraction(0)] * (m - 1)) == (
        [Fraction(1)] + [Fraction(0)] * (m - 1)
    )
    return t


def charpoly_desc(a):
    """Faddeev-LeVerrier: [1,c1,...,cn] for det(lambda I-A)."""
    n = len(a)
    b = eye(n)
    coeff = [Fraction(1)]
    for k in range(1, n + 1):
        ab = matmul(a, b)
        ck = -trace(ab) / k
        coeff.append(ck)
        b = add_scalar_identity(ab, ck)
    return coeff


def poly_eval_desc(p, x: Fraction):
    y = Fraction(0)
    for c in p:
        y = y * x + c
    return y


def divide_by_lambda_minus_one(desc):
    q = [desc[0]]
    for c in desc[1:-1]:
        q.append(c + q[-1])
    rem = desc[-1] + q[-1]
    return q, rem


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def derivative(p):
    if len(p) <= 1:
        return [Fraction(0)]
    return trim([p[i] * i for i in range(1, len(p))])


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [Fraction(0)], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1] / b[-1]
        q[shift] = c
        for j in range(len(b)):
            a[j + shift] -= c * b[j]
        a = trim(a)
    return trim(q), trim(a)


def sturm_sequence(p_asc):
    p = trim(p_asc)
    seq = [p, derivative(p)]
    while seq[-1] != [0]:
        _, rem = divmod_poly(seq[-2], seq[-1])
        if rem == [0]:
            break
        seq.append([-x for x in rem])
    return seq


def poly_eval_asc(p, x: Fraction):
    y = Fraction(0)
    for c in reversed(p):
        y = y * x + c
    return y


def sign_variations(values):
    signs = []
    for v in values:
        if v > 0:
            signs.append(1)
        elif v < 0:
            signs.append(-1)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def variations_at(seq, x: Fraction):
    return sign_variations([poly_eval_asc(p, x) for p in seq])


def variations_at_infinity(seq, positive: bool):
    signs = []
    for p in seq:
        s = 1 if p[-1] > 0 else -1
        if not positive and (len(p) - 1) % 2:
            s = -s
        signs.append(s)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def root_counts(q_desc):
    q_asc = list(reversed(q_desc))
    assert poly_eval_asc(q_asc, Fraction(0)) != 0
    assert poly_eval_asc(q_asc, Fraction(1)) != 0
    seq = sturm_sequence(q_asc)
    v_neg_inf = variations_at_infinity(seq, positive=False)
    v_0 = variations_at(seq, Fraction(0))
    v_1 = variations_at(seq, Fraction(1))
    v_pos_inf = variations_at_infinity(seq, positive=True)
    return {
        "negative": v_neg_inf - v_0,
        "unit_interval": v_0 - v_1,
        "above_one": v_1 - v_pos_inf,
        "sturm_variations": [v_neg_inf, v_0, v_1, v_pos_inf],
        "squarefree": len(seq[-1]) == 1 and seq[-1][0] != 0,
    }


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    rows = []
    for m in range(2, 11):
        t = build_operator(m)
        cp = charpoly_desc(t)
        q_desc, rem = divide_by_lambda_minus_one(cp)
        assert rem == 0, (m, "known fixed root lambda=1 missing")
        q_at_one = poly_eval_desc(q_desc, Fraction(1))
        assert q_at_one != 0, (m, "parent quotient determinant vanished")
        counts = root_counts(q_desc)
        triple = (
            counts["negative"],
            counts["unit_interval"],
            counts["above_one"],
        )
        assert triple == EXPECTED_ROOT_COUNTS[m], (m, triple)
        rows.append({
            "m": m,
            "degree": len(q_desc) - 1,
            "roots_negative": triple[0],
            "roots_0_1": triple[1],
            "roots_gt_1": triple[2],
            "nonreal_roots": (len(q_desc) - 1) - sum(triple),
            "q_at_one_positive": q_at_one > 0,
            "squarefree": counts["squarefree"],
            "sturm_variations": counts["sturm_variations"],
        })

        # The comparison endpoint retained from the accepted predecessor.
        if m <= 8:
            t0 = build_operator(m, cauchy=True)
            assert t0 == eye(m), (m, "Cauchy endpoint is not identity")

        if m == 10:
            canonical_t = json.dumps(
                [[fstr(x) for x in row] for row in t],
                separators=(",", ":"),
                ensure_ascii=False,
            )
            canonical_q = json.dumps(
                [fstr(x) for x in q_desc],
                separators=(",", ":"),
                ensure_ascii=False,
            )
            canonical_q1 = fstr(q_at_one)
            assert sha256_text(canonical_t) == EXPECTED_T10_SHA256
            assert sha256_text(canonical_q) == EXPECTED_Q10_CHARPOLY_SHA256
            assert sha256_text(canonical_q1) == EXPECTED_Q10_AT_ONE_SHA256
            assert counts["squarefree"]
            assert triple == (0, 7, 0)
            assert len(q_desc) - 1 == 9
            assert q_at_one > 0
            assert len(str(abs(q_at_one.numerator))) == 1865
            assert len(str(q_at_one.denominator)) == 1888

            # Structural identification q(1)=det(I-Q_10), using the lower-right
            # block Q_10 of the frozen upper-triangular splitting.
            q_block = [row[1:] for row in t[1:]]
            q_block_cp = charpoly_desc(q_block)
            det_i_minus_q = poly_eval_desc(q_block_cp, Fraction(1))
            assert det_i_minus_q == q_at_one

    # Fully explicit m=2 anchor from the actual AP operator.
    t2 = build_operator(2)
    assert t2 == [
        [Fraction(1), Fraction(3, 28)],
        [Fraction(0), Fraction(529, 1540)],
    ]

    out = {
        "status": "PASS",
        "terminal_certificate": "ACTUAL_AP_M10_HAS_ONE_NONREAL_CONJUGATE_EIGENPAIR_SO_GSTP_FAILS",
        "parent_m10": "det(I-Q_10)>0 EXACT",
        "m10_t_sha256": EXPECTED_T10_SHA256,
        "m10_quotient_charpoly_sha256": EXPECTED_Q10_CHARPOLY_SHA256,
        "m10_q_at_one_sha256": EXPECTED_Q10_AT_ONE_SHA256,
        "rows": rows,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
