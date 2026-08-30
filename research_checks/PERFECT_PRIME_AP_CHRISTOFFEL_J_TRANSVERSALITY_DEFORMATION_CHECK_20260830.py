#!/usr/bin/env python3
"""Exact regression/certificate for the AP Christoffel J-transversality deformation task.

This checker is pure Python stdlib + Fraction arithmetic. It proves no all-m
statement by finite enumeration. Decisive exact counter-certificates:
  * at m=3 the natural symmetric Schur crossing is indefinite on the quotient complement of w;
  * at m=10 the first quotient derivative Q'(0) is invertible and squarefree,
    but has exactly seven real negative roots and one non-real conjugate pair.
Thus a global real-spectral / definite-inertia deformation engine is obstructed
without producing a parent counterexample.

It also freezes finite exact discovery evidence for the half-Pascal pencil
D_*(t)=C_*(t)-A_*(t), which is a candidate rank certificate not requiring real
spectrum.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import hashlib
import json

EXPECTED_Q1_ROWS = {
    2: (1, 0, 0),
    3: (2, 0, 0),
    4: (3, 0, 0),
    5: (4, 0, 0),
    6: (5, 0, 0),
    7: (6, 0, 0),
    8: (7, 0, 0),
    9: (8, 0, 0),
    10: (7, 0, 2),
}
EXPECTED_M10_Q1_CHARPOLY_SHA256 = "0cf9c194b264d2e22123f3faeaf86ab4f63e1c08026201a1bdd159ffd61f1377"
EXPECTED_M10_DET_MINUS_Q1_SHA256 = "0ecb55da55153338b3d6f05c0ca31df73bca3f267b7f5dc57a0dfcedeca79ad0"
EXPECTED_M10_AP_DET_I_MINUS_Q_SHA256 = "a8dd130f9c473546c667b5215d6ef291d35dde20b1ec8912e20d3ea8b3ea6f5b"
EXPECTED_M3_CROSSING_GRAM = [
    [Fraction(2177, 388960), Fraction(1201, 38896)],
    [Fraction(1201, 38896), Fraction(-5617, 680680)],
]
EXPECTED_M3_CROSSING_DET = Fraction(-243, 243100)
GRID_T = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
EXPECTED_PROPER_MINOR_COUNTS = {2: 4, 3: 18, 4: 68, 5: 250, 6: 922}


def zeros(n, m=None):
    if m is None:
        m = n
    return [[Fraction(0) for _ in range(m)] for __ in range(n)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def diag(v):
    out = zeros(len(v))
    for i, x in enumerate(v):
        out[i][i] = Fraction(x)
    return out


def matmul(a, b):
    n, p, q = len(a), len(b), len(b[0])
    assert len(a[0]) == p
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(p)), Fraction(0))
            for j in range(q)
        ]
        for i in range(n)
    ]


def matadd(a, b):
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matsub(a, b):
    return [
        [a[i][j] - b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matscale(a, c):
    return [[c * x for x in row] for row in a]


def inverse(a):
    n = len(a)
    aug = [a[i][:] + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        if pivot is None:
            raise AssertionError("singular matrix where inverse expected")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            if f:
                aug[r] = [
                    aug[r][c] - f * aug[col][c] for c in range(2 * n)
                ]
    return [row[n:] for row in aug]


def det(a):
    n = len(a)
    if n == 0:
        return Fraction(1)
    x = [row[:] for row in a]
    out = Fraction(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if x[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            x[col], x[pivot] = x[pivot], x[col]
            sign *= -1
        p = x[col][col]
        out *= p
        for r in range(col + 1, n):
            if x[r][col]:
                f = x[r][col] / p
                for c in range(col + 1, n):
                    x[r][c] -= f * x[col][c]
                x[r][col] = Fraction(0)
    return out * sign


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def add_scalar_identity(a, c):
    n = len(a)
    return [
        [a[i][j] + (c if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


def fstr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def pascal_t(m, t):
    return [
        [
            Fraction(comb(i, j)) * t ** (i - j) if j <= i else Fraction(0)
            for j in range(m)
        ]
        for i in range(m)
    ]


def route_t(m, t):
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]
    h = zeros(m)
    for i in range(m):
        for j in range(m):
            q = i + m * j
            h[i][j] = sum(
                (
                    Fraction(((-1) ** r) * comb(n, r), q + 1 + r * m * m)
                    * t ** r
                    for r in range(n + 1)
                ),
                Fraction(0),
            )
    e = [
        sum((h[i][j] * w[j] for j in range(m)), Fraction(0))
        for i in range(m)
    ]
    d = [
        sum((h[i][j] * w[i] for i in range(m)), Fraction(0))
        for j in range(m)
    ]
    assert all(x > 0 for x in e + d)
    wdiag = diag(w)
    a = matmul(matmul(diag([1 / x for x in e]), h), wdiag)
    b = matmul(matmul(diag([1 / x for x in d]), transpose(h)), wdiag)
    rmat = [
        [
            Fraction(((-1) ** j) * comb(i, j)) if j <= i else Fraction(0)
            for j in range(m)
        ]
        for i in range(m)
    ]
    k = matmul(b, a)
    tmat = matmul(matmul(rmat, k), rmat)
    fixed = [Fraction(1)] + [Fraction(0)] * (m - 1)
    assert [sum(tmat[i][j] * fixed[j] for j in range(m)) for i in range(m)] == fixed
    return h, e, d, a, b, rmat, k, tmat


def derivative_t0(m):
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]
    h0, h1 = zeros(m), zeros(m)
    for i in range(m):
        for j in range(m):
            q = i + m * j
            h0[i][j] = Fraction(1, q + 1)
            h1[i][j] = Fraction(-n, q + 1 + m * m)
    e0 = [
        sum((h0[i][j] * w[j] for j in range(m)), Fraction(0))
        for i in range(m)
    ]
    e1 = [
        sum((h1[i][j] * w[j] for j in range(m)), Fraction(0))
        for i in range(m)
    ]
    d0 = [
        sum((h0[i][j] * w[i] for i in range(m)), Fraction(0))
        for j in range(m)
    ]
    d1 = [
        sum((h1[i][j] * w[i] for i in range(m)), Fraction(0))
        for j in range(m)
    ]
    wdiag = diag(w)
    e0i = diag([1 / x for x in e0])
    d0i = diag([1 / x for x in d0])
    a0 = matmul(matmul(e0i, h0), wdiag)
    b0 = matmul(matmul(d0i, transpose(h0)), wdiag)
    a1 = matsub(
        matmul(matmul(e0i, h1), wdiag),
        matmul(matmul(e0i, diag(e1)), a0),
    )
    b1 = matsub(
        matmul(matmul(d0i, transpose(h1)), wdiag),
        matmul(matmul(d0i, diag(d1)), b0),
    )
    rmat = [
        [
            Fraction(((-1) ** j) * comb(i, j)) if j <= i else Fraction(0)
            for j in range(m)
        ]
        for i in range(m)
    ]
    k1 = matadd(matmul(b1, a0), matmul(b0, a1))
    t1 = matmul(matmul(rmat, k1), rmat)
    return h0, h1, e0, e1, d0, d1, a0, a1, b0, b1, rmat, t1


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


def poly_eval_desc(p, x):
    y = Fraction(0)
    for c in p:
        y = y * x + c
    return y


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def derivative_poly(p):
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
    seq = [p, derivative_poly(p)]
    while seq[-1] != [0]:
        _, rem = divmod_poly(seq[-2], seq[-1])
        if rem == [0]:
            break
        seq.append([-x for x in rem])
    return seq


def poly_eval_asc(p, x):
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


def variations_at(seq, x):
    return sign_variations([poly_eval_asc(p, x) for p in seq])


def variations_at_infinity(seq, positive):
    signs = []
    for p in seq:
        s = 1 if p[-1] > 0 else -1
        if not positive and (len(p) - 1) % 2:
            s = -s
        signs.append(s)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def real_root_counts_about_zero(desc):
    seq = sturm_sequence(list(reversed(desc)))
    v_neg_inf = variations_at_infinity(seq, False)
    v_0 = variations_at(seq, Fraction(0))
    v_pos_inf = variations_at_infinity(seq, True)
    return {
        "negative": v_neg_inf - v_0,
        "positive": v_0 - v_pos_inf,
        "squarefree": len(seq[-1]) == 1 and seq[-1][0] != 0,
    }


def symmetric_schur_derivative(m):
    h0, h1, e0, e1, d0, d1, *_ = derivative_t0(m)
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]
    wdiag = diag(w)
    winv = diag([1 / x for x in w])
    e0i = diag([1 / x for x in e0])
    term1 = matmul(diag(d1), winv)
    term2 = matmul(matmul(matmul(transpose(h1), wdiag), e0i), h0)
    term3 = matmul(matmul(matmul(transpose(h0), wdiag), e0i), h1)
    term4 = matmul(
        matmul(
            matmul(
                matmul(matmul(transpose(h0), wdiag), e0i),
                diag(e1),
            ),
            e0i,
        ),
        h0,
    )
    return matsub(matadd(term1, term4), matadd(term2, term3))


def bilinear(a, v, w):
    return sum(
        (v[i] * a[i][j] * w[j] for i in range(len(v)) for j in range(len(w))),
        Fraction(0),
    )


def derivative_dstar0(m):
    h0, h1, e0, e1, d0, d1, a0, a1, b0, b1, rmat, _ = derivative_t0(m)
    ah0, ah1 = matmul(a0, rmat), matmul(a1, rmat)
    bh0, bh1 = matmul(b0, rmat), matmul(b1, rmat)
    s = pascal_t(m, Fraction(1, 2))
    sinv = pascal_t(m, Fraction(-1, 2))
    jmat = diag([Fraction((-1) ** i) for i in range(m)])
    astar1 = matmul(matmul(sinv, ah1), s)
    bstar0 = matmul(matmul(sinv, bh0), s)
    bstar1 = matmul(matmul(sinv, bh1), s)
    bstar0i = inverse(bstar0)
    cstar1 = matscale(
        matmul(matmul(matmul(matmul(jmat, bstar0i), bstar1), bstar0i), jmat),
        Fraction(-1),
    )
    return matsub(cstar1, astar1)


def dstar_at(m, t):
    _, _, _, a, b, rmat, _, tmat = route_t(m, t)
    ahat = matmul(a, rmat)
    bhat = matmul(b, rmat)
    s = pascal_t(m, Fraction(1, 2))
    sinv = pascal_t(m, Fraction(-1, 2))
    jmat = diag([Fraction((-1) ** i) for i in range(m)])
    assert matmul(matmul(sinv, rmat), s) == jmat
    astar = matmul(matmul(sinv, ahat), s)
    bstar = matmul(matmul(sinv, bhat), s)
    cstar = matmul(matmul(jmat, inverse(bstar)), jmat)
    tstar = matmul(matmul(sinv, tmat), s)
    assert tstar == matmul(inverse(cstar), astar)
    return matsub(cstar, astar)


def all_proper_minors_positive(a):
    n = len(a)
    count = 0
    for q in range(1, n):
        for rows in combinations(range(n), q):
            for cols in combinations(range(n), q):
                value = det([[a[i][j] for j in cols] for i in rows])
                count += 1
                if value <= 0:
                    return False, count, (q, rows, cols, value)
    return True, count, None


def main():
    # Mandatory Cauchy endpoint and first derivative quotient census.
    q1_rows = []
    m10_cp = None
    m10_det_minus = None
    for m in range(2, 11):
        *_, t1 = derivative_t0(m)
        q1 = [row[1:] for row in t1[1:]]
        cp = charpoly_desc(q1)
        counts = real_root_counts_about_zero(cp)
        degree = m - 1
        nonreal = degree - counts["negative"] - counts["positive"]
        assert (counts["negative"], counts["positive"], nonreal) == EXPECTED_Q1_ROWS[m]
        assert counts["squarefree"]
        det_minus = det(matscale(q1, Fraction(-1)))
        assert det_minus > 0
        q1_rows.append({
            "m": m,
            "degree": degree,
            "negative_real": counts["negative"],
            "positive_real": counts["positive"],
            "nonreal": nonreal,
            "squarefree": True,
            "det_minus_q1_positive": True,
        })
        if m == 10:
            m10_cp = cp
            m10_det_minus = det_minus

    canonical_cp = json.dumps([fstr(x) for x in m10_cp], separators=(",", ":"))
    assert sha256_text(canonical_cp) == EXPECTED_M10_Q1_CHARPOLY_SHA256
    assert sha256_text(fstr(m10_det_minus)) == EXPECTED_M10_DET_MINUS_Q1_SHA256

    # At actual AP t=1 the parent quotient determinant still survives exactly.
    t10 = route_t(10, Fraction(1))[-1]
    q10 = [row[1:] for row in t10[1:]]
    det_i_minus_q10 = det(matsub(eye(9), q10))
    assert det_i_minus_q10 > 0
    assert sha256_text(fstr(det_i_minus_q10)) == EXPECTED_M10_AP_DET_I_MINUS_Q_SHA256

    # Natural symmetric Schur crossing form is already indefinite at m=3.
    sigma1 = symmetric_schur_derivative(3)
    w = [Fraction(1), Fraction(-2), Fraction(1)]
    assert [sum(sigma1[i][j] * w[j] for j in range(3)) for i in range(3)] == [0, 0, 0]
    v1 = [Fraction(2), Fraction(1), Fraction(0)]
    v2 = [Fraction(-1), Fraction(0), Fraction(1)]
    gram = [
        [bilinear(sigma1, v1, v1), bilinear(sigma1, v1, v2)],
        [bilinear(sigma1, v2, v1), bilinear(sigma1, v2, v2)],
    ]
    assert gram == EXPECTED_M3_CROSSING_GRAM
    assert det(gram) == EXPECTED_M3_CROSSING_DET < 0

    # Half-Pascal rank-certificate frontier: finite exact evidence only.
    half_pascal_rows = []
    for m in range(2, 7):
        d1 = derivative_dstar0(m)
        ok, count, witness = all_proper_minors_positive(d1)
        assert ok, witness
        assert count == EXPECTED_PROPER_MINOR_COUNTS[m]
        assert det(d1) == 0
        z = [Fraction(-1, 2) ** i for i in range(m)]
        assert [sum(d1[i][j] * z[j] for j in range(m)) for i in range(m)] == [0] * m

        trows = []
        for t in GRID_T:
            dmat = dstar_at(m, t)
            ok, count, witness = all_proper_minors_positive(dmat)
            assert ok, (m, t, witness)
            assert count == EXPECTED_PROPER_MINOR_COUNTS[m]
            assert det(dmat) == 0
            assert [sum(dmat[i][j] * z[j] for j in range(m)) for i in range(m)] == [0] * m
            trows.append({"t": fstr(t), "proper_minor_count": count})
        half_pascal_rows.append({
            "m": m,
            "derivative_proper_minor_count": EXPECTED_PROPER_MINOR_COUNTS[m],
            "grid": trows,
        })

    out = {
        "status": "PASS",
        "terminal_certificate": "M10_FIRST_ORDER_REAL_SPECTRAL_INERTIA_OBSTRUCTED_PARENT_SURVIVES",
        "q1_rows": q1_rows,
        "m10_q1_charpoly_sha256": EXPECTED_M10_Q1_CHARPOLY_SHA256,
        "m10_det_minus_q1_sha256": EXPECTED_M10_DET_MINUS_Q1_SHA256,
        "m10_ap_det_i_minus_q_sha256": EXPECTED_M10_AP_DET_I_MINUS_Q_SHA256,
        "m3_symmetric_crossing_gram_det": fstr(EXPECTED_M3_CROSSING_DET),
        "half_pascal_rows": half_pascal_rows,
        "note": "finite m/grid evidence is regression/discovery only, not an all-m proof",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
