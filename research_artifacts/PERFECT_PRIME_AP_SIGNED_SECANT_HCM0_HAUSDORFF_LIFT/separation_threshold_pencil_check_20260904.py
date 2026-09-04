#!/usr/bin/env python3
"""Exact checker for SEPARATION_THRESHOLD_PENCIL_CHECKPOINT_20260904.md.

No floating-point value is used for coefficient-sign certificates.
"""

from fractions import Fraction as F
from math import comb, factorial


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(row) for row in zip(*A)]


def det(A):
    A = [[F(x) for x in row] for row in A]
    n = len(A)
    out = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c]), None)
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            out = -out
        piv = A[c][c]
        out *= piv
        for j in range(c + 1, n):
            A[c][j] /= piv
        for r in range(c + 1, n):
            q = A[r][c]
            if q:
                for j in range(c + 1, n):
                    A[r][j] -= q * A[c][j]
    return out


def mu(m, r):
    n = m - 1
    den = 1
    for a in range(1, m + 1):
        den *= m * r + a
    return F(factorial(n), den)


def pascal(m):
    return [[F(comb(i, k)) if k <= i else F(0)
             for k in range(m)] for i in range(m)]


def Hlead(m, r):
    n = m - 1
    P = pascal(m)
    D = [[F(0) for _ in range(m)] for _ in range(m)]
    for j in range(m):
        D[j][j] = F((-1) ** j * comb(n, j)) * mu(m, r + j)
    H = mm(tr(P), mm(D, P))
    return [row[:n] for row in H[:n]]


def Tbin(m, M):
    n = m - 1
    return [[F(comb(M, a - k)) if k < a else F(0)
             for a in range(1, n + 1)] for k in range(n)]


def Q(m, r0, r):
    assert r > r0
    T = Tbin(m, r - r0)
    return mm(tr(T), mm(Hlead(m, r), T))


def polynomial_coefficients(A, B):
    """Return coefficients c_k of det(A+tB)=sum c_k t^k exactly."""
    n = len(A)
    vals = []
    for x in range(n + 1):
        vals.append(det([[A[i][j] + F(x) * B[i][j]
                          for j in range(n)] for i in range(n)]))

    # Newton forward interpolation followed by multiplication in Q[t].
    diffs = []
    cur = vals[:]
    diffs.append(cur[0])
    for _ in range(1, n + 1):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        diffs.append(cur[0])

    # polys are coefficient lists in ascending monomial degree.
    ans = [F(0)] * (n + 1)
    fall = [F(1)]
    fact = 1
    for j, dj in enumerate(diffs):
        if j:
            # multiply current falling factorial by (t-(j-1))
            a = F(j - 1)
            nxt = [F(0)] * (len(fall) + 1)
            for k, ck in enumerate(fall):
                nxt[k] -= a * ck
                nxt[k + 1] += ck
            fall = nxt
            fact *= j
        for k, ck in enumerate(fall):
            ans[k] += dj * ck / fact
    return ans


def signs(cs):
    return tuple(1 if c > 0 else -1 if c < 0 else 0 for c in cs)


def same_strict_sign(cs):
    s = signs(cs)
    return 0 not in s and len(set(s)) == 1


def check_exact_integer_counterexample():
    m = 10
    cs = polynomial_coefficients(Q(m, 0, 1), Q(m, 0, 5))
    expected = F(
        -10612824961174951202027648577503279651182772104969959464262239715,
        1779190353785266854363656648348425662886396623357055484212781139453940884444359455084001552607701836246656138519424941793415894301254772509798569513296767514860060672,
    )
    assert cs[8] == expected
    assert cs[8] < 0
    assert all(c > 0 for k, c in enumerate(cs) if k != 8)
    return cs


def check_all_actual_m10():
    m = 10
    count = 0
    for se in range(m - 2):
        for sd in range(se + 1, m - 1):
            A = Q(m, m * se, m * sd)
            for sf in range(sd + 1, m):
                B = Q(m, m * se, m * sf)
                cs = polynomial_coefficients(A, B)
                assert same_strict_sign(cs), (se, sd, sf, signs(cs))
                count += 1
    assert count == comb(10, 3) == 120
    return count


def check_large_gap_grid(m):
    """100 exact near-threshold pencils used in the checkpoint."""
    count = 0
    for r0 in range(4):
        for M in range(m, m + 5):
            r = r0 + M
            for N in range(M + 1, m + 8):
                s = r0 + N
                cs = polynomial_coefficients(Q(m, r0, r), Q(m, r0, s))
                assert same_strict_sign(cs), (m, r0, M, N, signs(cs))
                count += 1
    assert count == 100
    return count


def main():
    cs = check_exact_integer_counterexample()
    print("m10 integer counterexample signs:", signs(cs))
    print("m10 exact negative t^8 coefficient:", cs[8])

    count = check_all_actual_m10()
    print("m10 actual triples strict common-sign:", count, "/", count)

    total = 0
    for m in range(3, 11):
        c = check_large_gap_grid(m)
        total += c
        print("large-gap exact grid m=", m, ":", c, "/", c)
    print("large-gap exact total:", total, "/", total)


if __name__ == "__main__":
    main()
