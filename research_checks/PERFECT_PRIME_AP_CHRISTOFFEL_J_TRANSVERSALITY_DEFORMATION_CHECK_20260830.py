#!/usr/bin/env python3
"""Exact regression for the Perfect Prime AP Christoffel deformation boundary.

All arithmetic is rational and uses only the Python standard library.
The checker verifies finite symbolic certificates used by the research return:
  * exact m=2 quotient determinant formula on the genuine positive deformation;
  * exact nonmonotonicity of the normalized m=2 quotient determinant;
  * signed self-adjointness/crossing-form symmetry regressions;
  * exact m=3 indefiniteness of the naive definite crossing form;
  * exact tangent-Christoffel tree-cofactor factorizations for m=2,3,4;
  * exact m=4 tangent recrossing at t=49/51 with nonzero normalizers and
    Laplacian nullity exactly 2.

Finite checks support, but do not replace, the all-m algebraic statements in
research_returns/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_RETURN_20260830.md.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pneg(a):
    return trim([-x for x in a])


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pscale(a, c):
    return trim([c * x for x in a])


def peval(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def pder(a):
    if len(a) <= 1:
        return (F(0),)
    return trim([F(i) * a[i] for i in range(1, len(a))])


def plin(c0, c1=F(0)):
    return trim((F(c0), F(c1)))


def pfactor(*factors):
    out = (F(1),)
    for f in factors:
        out = pmul(out, f)
    return out


class Rat:
    def __init__(self, n=(F(0),), d=(F(1),)):
        self.n = trim(tuple(F(x) for x in n))
        self.d = trim(tuple(F(x) for x in d))
        if self.d == (F(0),):
            raise ZeroDivisionError

    @staticmethod
    def const(x):
        return Rat((F(x),), (F(1),))

    @staticmethod
    def poly(p):
        return Rat(p, (F(1),))

    def __add__(self, other):
        other = other if isinstance(other, Rat) else Rat.const(other)
        return Rat(padd(pmul(self.n, other.d), pmul(other.n, self.d)), pmul(self.d, other.d))

    __radd__ = __add__

    def __neg__(self):
        return Rat(pneg(self.n), self.d)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Rat) else -Rat.const(other))

    def __rsub__(self, other):
        return Rat.const(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Rat) else Rat.const(other)
        return Rat(pmul(self.n, other.n), pmul(self.d, other.d))

    __rmul__ = __mul__

    def inv(self):
        if self.n == (F(0),):
            raise ZeroDivisionError
        return Rat(self.d, self.n)

    def __truediv__(self, other):
        other = other if isinstance(other, Rat) else Rat.const(other)
        return self * other.inv()

    def __eq__(self, other):
        other = other if isinstance(other, Rat) else Rat.const(other)
        return trim(pmul(self.n, other.d)) == trim(pmul(other.n, self.d))

    def eval(self, x):
        return peval(self.n, x) / peval(self.d, x)


def mmul(a, b):
    zero = Rat.const(0) if isinstance(a[0][0], Rat) else F(0)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), zero)
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return [list(row) for row in zip(*a)]


def diag(v):
    return [[v[i] if i == j else (Rat.const(0) if isinstance(v[i], Rat) else F(0))
             for j in range(len(v))] for i in range(len(v))]


def eye(n, rat=False):
    one = Rat.const(1) if rat else F(1)
    zero = Rat.const(0) if rat else F(0)
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mscale(a, c):
    return [[c * x for x in row] for row in a]


def det_fraction(a):
    n = len(a)
    x = [row[:] for row in a]
    out = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if x[r][c]), None)
        if p is None:
            return F(0)
        if p != c:
            x[c], x[p] = x[p], x[c]
            out = -out
        pivot = x[c][c]
        out *= pivot
        for r in range(c + 1, n):
            if x[r][c] == 0:
                continue
            q = x[r][c] / pivot
            for j in range(c + 1, n):
                x[r][j] -= q * x[c][j]
            x[r][c] = F(0)
    return out


def rank_fraction(a):
    x = [row[:] for row in a]
    nr, nc = len(x), len(x[0])
    r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if x[i][c]), None)
        if p is None:
            continue
        x[r], x[p] = x[p], x[r]
        pivot = x[r][c]
        for j in range(c, nc):
            x[r][j] /= pivot
        for i in range(nr):
            if i == r or x[i][c] == 0:
                continue
            q = x[i][c]
            for j in range(c, nc):
                x[i][j] -= q * x[r][j]
        r += 1
        if r == nr:
            break
    return r


def poly_perm_det(a):
    n = len(a)
    out = (F(0),)
    for p in permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        term = (F(-1 if inv & 1 else 1),)
        for i in range(n):
            term = pmul(term, a[i][p[i]])
        out = padd(out, term)
    return trim(out)


def r_matrix(m):
    return [[F(((-1) ** j) * comb(i, j)) if j <= i else F(0)
             for j in range(m)] for i in range(m)]


def route_m2_rat():
    m, n, M = 2, 1, 4
    w = [F(((-1) ** i) * comb(n, i)) for i in range(m)]
    H = [[Rat.poly(plin(F(1, i + m*j + 1), -F(1, i + m*j + 1 + M)))
          for j in range(m)] for i in range(m)]
    W = diag([Rat.const(x) for x in w])
    e = [sum((H[i][j] * w[j] for j in range(m)), Rat.const(0)) for i in range(m)]
    d = [sum((H[i][j] * w[i] for i in range(m)), Rat.const(0)) for j in range(m)]
    A = mmul(mmul(diag([x.inv() for x in e]), H), W)
    B = mmul(mmul(diag([x.inv() for x in d]), trans(H)), W)
    K = mmul(B, A)
    R = [[Rat.const(x) for x in row] for row in r_matrix(m)]
    T = mmul(mmul(R, K), R)
    return Rat.const(1) - T[1][1]


def exact_m2_formula_check():
    D = route_m2_rat()
    expected_num = pscale(pfactor(plin(0, 1), plin(-13, 5), plin(-350, 13)), F(6))
    expected_den = pfactor(plin(-15, 1), plin(-6, 1), plin(-35, 3), plin(-14, 3))
    expected = Rat(expected_num, expected_den)
    if D != expected:
        raise AssertionError("m=2 genuine deformation determinant formula mismatch")

    g_num = pscale(pfactor(plin(-13, 5), plin(-350, 13)), F(6))
    g_den = expected_den
    g0 = peval(g_num, F(0)) / peval(g_den, F(0))
    g1 = peval(g_num, F(1)) / peval(g_den, F(1))
    gp_num = psub(pmul(pder(g_num), g_den), pmul(g_num, pder(g_den)))
    gp_den = pmul(g_den, g_den)
    gp0 = peval(gp_num, F(0)) / peval(gp_den, F(0))
    gp1 = peval(gp_num, F(1)) / peval(gp_den, F(1))
    if (g0, g1, gp0, gp1) != (F(13,21), F(1011,1540), F(1523,22050), -F(319731,18972800)):
        raise AssertionError("m=2 normalized determinant endpoint data mismatch")
    if not (gp0 > 0 and gp1 < 0):
        raise AssertionError("m=2 normalized determinant should be nonmonotone")
    for x in (F(1,10), F(1,2), F(1)):
        if D.eval(x) <= 0:
            raise AssertionError("m=2 determinant must stay positive on exact regression points")
    print("m=2 genuine AP-Christoffel path: exact determinant formula + normalized nonmonotonicity PASS")


def route_fraction(m, tv):
    n, M = m - 1, m * m
    def h(q):
        return sum((F(((-1) ** r) * comb(n, r)) * (tv ** r) / F(q + 1 + r * M)
                    for r in range(n + 1)), F(0))
    H = [[h(i + m*j) for j in range(m)] for i in range(m)]
    w = [F(((-1) ** i) * comb(n, i)) for i in range(m)]
    W = diag(w)
    e = [sum((H[i][j] * w[j] for j in range(m)), F(0)) for i in range(m)]
    d = [sum((H[i][j] * w[i] for i in range(m)), F(0)) for j in range(m)]
    A = mmul(mmul(diag([1/x for x in e]), H), W)
    B = mmul(mmul(diag([1/x for x in d]), trans(H)), W)
    K = mmul(B, A)
    return H, w, e, d, K


def signed_self_adjoint_regression():
    for m in range(2, 6):
        for tv in (F(0), F(1,3), F(1)):
            H, w, e, d, K = route_fraction(m, tv)
            G = diag([w[i] * d[i] for i in range(m)])
            GK = mmul(G, K)
            if GK != trans(GK):
                raise AssertionError(f"m={m}, t={tv}: signed self-adjointness failed")
    print("signed metric self-adjointness exact regression m=2..5, t in {0,1/3,1}: PASS")


def crossing_at_zero(m):
    n, M = m - 1, m*m
    w = [F(((-1) ** i) * comb(n, i)) for i in range(m)]
    W = diag(w)
    H0 = [[F(1, i + m*j + 1) for j in range(m)] for i in range(m)]
    H1 = [[-F(n, i + m*j + 1 + M) for j in range(m)] for i in range(m)]
    e0 = [sum((H0[i][j] * w[j] for j in range(m)), F(0)) for i in range(m)]
    e1 = [sum((H1[i][j] * w[j] for j in range(m)), F(0)) for i in range(m)]
    d0 = [sum((H0[i][j] * w[i] for i in range(m)), F(0)) for j in range(m)]
    d1 = [sum((H1[i][j] * w[i] for i in range(m)), F(0)) for j in range(m)]
    E0i = diag([1/x for x in e0])
    D0i = diag([1/x for x in d0])
    A0 = mmul(mmul(E0i, H0), W)
    B0 = mmul(mmul(D0i, trans(H0)), W)
    if mmul(B0, A0) != eye(m):
        raise AssertionError(f"m={m}: Cauchy K0 != I")
    Eder = diag(e1)
    Dder = diag(d1)
    A1 = madd(mmul(mmul(mscale(mmul(mmul(E0i, Eder), E0i), F(-1)), H0), W),
              mmul(mmul(E0i, H1), W))
    B1 = madd(mmul(mmul(mscale(mmul(mmul(D0i, Dder), D0i), F(-1)), trans(H0)), W),
              mmul(mmul(D0i, trans(H1)), W))
    K1 = madd(mmul(B1, A0), mmul(B0, A1))
    G0 = diag([w[i] * d0[i] for i in range(m)])
    S = mscale(mmul(G0, K1), F(-1))
    return w, d0, K1, S


def crossing_regression():
    for m in range(2, 7):
        w, d0, K1, S = crossing_at_zero(m)
        if S != trans(S):
            raise AssertionError(f"m={m}: crossing form not symmetric")
        if any(sum(row, F(0)) != 0 for row in K1):
            raise AssertionError(f"m={m}: K'(0) row sum not zero")
    _, _, _, S3 = crossing_at_zero(3)
    if S3[0][0] != -F(47,15470) or S3[1][1] != F(17879,680680):
        raise AssertionError("m=3 crossing-form exact diagonal certificate mismatch")
    if not (S3[0][0] < 0 < S3[1][1]):
        raise AssertionError("m=3 crossing form should be indefinite")
    print("crossing form: symmetry m=2..6 + exact m=3 indefiniteness PASS")


def tangent_laplacian_poly(m):
    n, M = m - 1, m*m
    w = [F(((-1) ** i) * comb(n, i)) for i in range(m)]
    H = [[plin(F(1, i + m*j + 1), -F(n, i + m*j + 1 + M))
          for j in range(m)] for i in range(m)]
    C = [[pscale(H[i][j], w[i] * w[j]) for j in range(m)] for i in range(m)]
    rows = []
    cols = []
    for i in range(m):
        s = (F(0),)
        for j in range(m): s = padd(s, C[i][j])
        rows.append(s)
    for j in range(m):
        s = (F(0),)
        for i in range(m): s = padd(s, C[i][j])
        cols.append(s)
    z = (F(0),)
    L = [[z for _ in range(2*m)] for __ in range(2*m)]
    for i in range(m):
        L[i][i] = rows[i]
        for j in range(m):
            L[i][m+j] = pneg(C[i][j])
            L[m+j][i] = pneg(C[i][j])
    for j in range(m):
        L[m+j][m+j] = cols[j]
    return H, L


def tangent_tree_checks():
    expected = {
        2: pscale(pfactor(plin(0,1), plin(-13,5)), -F(1,1260)),
        3: pscale(pfactor(pfactor(plin(0,1), plin(0,1)), plin(-7,5)), -F(243,476476000)),
        4: pscale(pfactor(pfactor(pfactor(plin(0,1), plin(0,1)), plin(0,1)), plin(-49,51)),
                  -F(3145728,25617946563506171875)),
    }
    for m in (2,3,4):
        H, L = tangent_laplacian_poly(m)
        cof = [row[:-1] for row in L[:-1]]
        got = poly_perm_det(cof)
        if got != expected[m]:
            raise AssertionError(f"m={m}: tangent tree polynomial mismatch\n{got}\n{expected[m]}")
        print(f"m={m} tangent tree-cofactor exact factorization PASS")

    root = F(49,51)
    H, L = tangent_laplacian_poly(4)
    w = [F(((-1) ** i) * comb(3, i)) for i in range(4)]
    e = [sum((peval(H[i][j], root) * w[j] for j in range(4)), F(0)) for i in range(4)]
    d = [sum((peval(H[i][j], root) * w[i] for i in range(4)), F(0)) for j in range(4)]
    if any(x == 0 for x in e + d):
        raise AssertionError("m=4 tangent recrossing must not be a normalizer pole")
    Lr = [[peval(x, root) for x in row] for row in L]
    if rank_fraction(Lr) != 6:
        raise AssertionError("m=4 tangent Laplacian should have rank 6 at t=49/51")
    print("m=4 tangent recrossing: t=49/51, all normalizers nonzero, Laplacian nullity=2 PASS")


def main():
    exact_m2_formula_check()
    signed_self_adjoint_regression()
    crossing_regression()
    tangent_tree_checks()
    print("AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_EXACT_CHECK_PASS")


if __name__ == "__main__":
    main()
