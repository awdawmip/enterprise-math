#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def F(x: int | Fraction, y: int | None = None) -> Fraction:
    return Fraction(x) if y is None else Fraction(x, y)


def eye(n: int):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def diag(values):
    n = len(values)
    return [[F(values[i]) if i == j else F(0) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def det(A):
    A = [row[:] for row in A]
    n = len(A)
    out = F(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if A[r][c] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            A[c], A[pivot] = A[pivot], A[c]
            out = -out
        pv = A[c][c]
        out *= pv
        for j in range(c, n):
            A[c][j] /= pv
        for r in range(c + 1, n):
            factor = A[r][c]
            if factor:
                for j in range(c, n):
                    A[r][j] -= factor * A[c][j]
    return out


def inverse(A):
    n = len(A)
    aug = [A[i][:] + eye(n)[i] for i in range(n)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if aug[r][c] != 0), None)
        if pivot is None:
            raise AssertionError("matrix unexpectedly singular")
        if pivot != c:
            aug[c], aug[pivot] = aug[pivot], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(n):
            if r == c:
                continue
            factor = aug[r][c]
            if factor:
                aug[r] = [aug[r][j] - factor * aug[c][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def rank(A):
    A = [row[:] for row in A]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                factor = A[i][c]
                A[i] = [A[i][j] - factor * A[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def frac_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def actual_h(m: int, q: int) -> Fraction:
    return F(1, math.prod(1 + q + ell * m * m for ell in range(m)))


def cauchy_h(m: int, i: int, j: int) -> Fraction:
    return F(1, 1 + i + m * j)


def build(m: int, actual: bool):
    n = m - 1
    w = [F(((-1) ** i) * math.comb(n, i)) for i in range(m)]
    if actual:
        H = [[actual_h(m, i + m * j) for j in range(m)] for i in range(m)]
    else:
        H = [[cauchy_h(m, i, j) for j in range(m)] for i in range(m)]
    e = [sum(H[i][j] * w[j] for j in range(m)) for i in range(m)]
    d = [sum(w[i] * H[i][j] for i in range(m)) for j in range(m)]
    if not all(x > 0 for x in e + d):
        raise AssertionError("normalizers must be positive")
    A = [[H[i][j] * w[j] / e[i] for j in range(m)] for i in range(m)]
    B = [[H[i][j] * w[i] / d[j] for i in range(m)] for j in range(m)]
    K = matmul(B, A)
    return H, w, e, d, A, B, K


def mobius_R(m: int):
    n = m - 1
    return [
        [F(((-1) ** k) * math.comb(j, k)) if k <= j else F(0) for k in range(m)]
        for j in range(m)
    ]


def lagrange_value(nodes, index: int, value: Fraction) -> Fraction:
    num = F(1)
    den = F(1)
    for r, node in enumerate(nodes):
        if r == index:
            continue
        num *= value - node
        den *= nodes[index] - node
    return num / den


def check_cauchy_baseline(m: int):
    H, w, e, d, A, B, K = build(m, actual=False)
    n = m - 1
    xs = [F(1 + i) for i in range(m)]
    ys = [F(m * j) for j in range(m)]
    expected_e = [F(math.factorial(n) * (m**n), math.prod(int(x) + m * r for r in range(m))) for x in xs]
    expected_d = [F(math.factorial(n), math.prod(int(y) + 1 + r for r in range(m))) for y in ys]
    if e != expected_e or d != expected_d:
        raise AssertionError("closed Cauchy normalizers failed")
    for i in range(m):
        for j in range(m):
            if A[i][j] != lagrange_value(ys, j, -xs[i]):
                raise AssertionError("A is not the Cauchy/Lagrange evaluation map")
            neg_xs = [-x for x in xs]
            if B[j][i] != lagrange_value(neg_xs, i, ys[j]):
                raise AssertionError("B is not inverse Lagrange evaluation")
    if K != eye(m):
        raise AssertionError("unweighted Cauchy baseline must satisfy BA=I")
    return True


def check_finite_difference_identity(m: int):
    n = m - 1
    for i in range(m):
        for j in range(m):
            q = i + m * j
            left = sum(
                F(((-1) ** ell) * math.comb(n, ell), q + 1 + ell * m * m)
                for ell in range(m)
            )
            right = F(math.factorial(n) * (m * m) ** n) * actual_h(m, q)
            if left != right:
                raise AssertionError("AP Christoffel/finite-difference identity failed")
    return True


def check_krein_structure(m: int):
    H, w, e, d, A, B, K = build(m, actual=True)
    n = m - 1
    lam = [F(math.comb(n, i)) for i in range(m)]
    J = diag([F(((-1) ** i)) for i in range(m)])
    W = diag(w)
    E = diag(e)
    D = diag(d)
    Lam = diag(lam)
    P = matmul(E, Lam)
    Q = matmul(D, Lam)
    X = matmul(A, J)
    Y = matmul(B, J)
    if matmul(Q, Y) != matmul(transpose(X), P):
        raise AssertionError("positive-metric adjoint relation QY=X^T P failed")
    if K != matmul(matmul(matmul(Y, J), X), J):
        raise AssertionError("K=Y J X J failed")
    lhs = matmul(matmul(D, W), K)
    rhs = matmul(matmul(transpose(A), E), matmul(W, A))
    if lhs != rhs:
        raise AssertionError("Krein self-adjoint identity DWK=A^T EWA failed")
    if lhs != transpose(lhs):
        raise AssertionError("DWK must be symmetric")
    ones = [F(1) for _ in range(m)]
    if matvec(K, ones) != ones:
        raise AssertionError("distinguished fixed vector failed")
    if rank(matsub(eye(m), K)) != m - 1:
        raise AssertionError("finite regression: fixed point not simple")
    R = mobius_R(m)
    if matmul(R, R) != eye(m):
        raise AssertionError("R involution failed")
    T = matmul(matmul(R, K), R)
    e0 = [F(1)] + [F(0)] * (m - 1)
    if matvec(T, e0) != e0:
        raise AssertionError("T e0=e0 failed")
    Qm = [row[1:] for row in T[1:]]
    quotient_det = det(matsub(eye(m - 1), Qm))
    if quotient_det == 0:
        raise AssertionError("finite regression: quotient determinant vanished")
    signed_norm = sum(w[j] * d[j] for j in range(m))
    if signed_norm <= 0:
        raise AssertionError("distinguished J-norm must be positive")
    return quotient_det, signed_norm


def check_principal_angle_mismatch():
    m = 2
    H, w, e, d, A, B, K = build(m, actual=True)
    Gv = [[actual_h(m, i + j) for j in range(m)] for i in range(m)]
    Gw = [[actual_h(m, m * (i + j)) for j in range(m)] for i in range(m)]
    C = matmul(matmul(matmul(inverse(Gw), transpose(H)), inverse(Gv)), H)
    k_nontrivial = det(K)
    c_nontrivial = det(C)
    if k_nontrivial != F(529, 1540):
        raise AssertionError("unexpected m=2 K eigenvalue regression")
    if c_nontrivial != F(18515, 19968):
        raise AssertionError("unexpected m=2 principal-angle eigenvalue regression")
    if k_nontrivial == c_nontrivial:
        raise AssertionError("ordinary principal angles unexpectedly encode K")
    return k_nontrivial, c_nontrivial


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=6)
    parser.add_argument("--baseline-max-m", type=int, default=8)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    if args.max_m < 2 or args.baseline_max_m < 2:
        raise SystemExit("m bounds must be >=2")

    quotient = {}
    signed_norms = {}
    for m in range(2, args.max_m + 1):
        check_finite_difference_identity(m)
        qdet, snorm = check_krein_structure(m)
        quotient[str(m)] = frac_text(qdet)
        signed_norms[str(m)] = frac_text(snorm)
    for m in range(2, args.baseline_max_m + 1):
        check_cauchy_baseline(m)
    k2, c2 = check_principal_angle_mismatch()

    certificate = {
        "schema": "PERFECT_PRIME_BETA_BERNSTEIN_PRINCIPAL_ANGLE_EXTERIOR_POWER_CERTIFICATE_V1",
        "status": "PASS",
        "actual_regression_max_m": args.max_m,
        "cauchy_baseline_exact_max_m": args.baseline_max_m,
        "all_m_symbolic_claims_replayed_finitely": [
            "AP finite-difference/Christoffel moment identity",
            "positive-metric adjointization after stripping J",
            "K=Y J X J and DWK=A^T EWA",
            "unweighted Cauchy barycentric maps A/B are inverse"
        ],
        "finite_actual_quotient_determinants": quotient,
        "finite_actual_distinguished_J_norms": signed_norms,
        "m2_actual_K_nontrivial_eigenvalue": frac_text(k2),
        "m2_actual_ordinary_principal_angle_squared": frac_text(c2),
        "principal_angle_spectral_mismatch": True,
        "unweighted_cauchy_baseline_K_identity": True,
        "note": "Finite m checks are regression only; all-m statements are proved symbolically in the research return."
    }
    text = json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        args.certificate.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
