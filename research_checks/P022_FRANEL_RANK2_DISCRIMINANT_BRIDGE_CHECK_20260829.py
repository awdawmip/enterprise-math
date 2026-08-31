#!/usr/bin/env python3
"""Exact replay for RS-P022-FRANEL-RANK2-DISCRIMINANT-BRIDGE.

Pure-Python checker.  Finite scans are regression/falsification controls only;
the theorem-level identities are proved algebraically in the return packet.
"""

from fractions import Fraction
from math import comb


def det2(A, mod=None):
    x = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return x if mod is None else x % mod


def mm(A, B, p):
    return [[sum(A[i][r] * B[r][j] for r in range(2)) % p
             for j in range(2)] for i in range(2)]


def mv(A, v, p):
    return [sum(A[i][r] * v[r] for r in range(2)) % p for i in range(2)]


def scalar_matrix(c, A, p):
    return [[c * A[i][j] % p for j in range(2)] for i in range(2)]


def franel_direct(n):
    return sum(comb(n, r) ** 3 for r in range(n + 1))


def franel_integer_table(N):
    F = [0] * (N + 1)
    F[0] = 1
    if N:
        F[1] = 2
    for n in range(1, N):
        num = (7 * n * (n + 1) + 2) * F[n] + 8 * n * n * F[n - 1]
        den = (n + 1) ** 2
        assert num % den == 0
        F[n + 1] = num // den
    return F


def franel_mod(k, p):
    if k == 0:
        return 1
    fm1, f = 1, 2
    if k == 1:
        return f
    for n in range(1, k):
        numerator = ((7 * n * (n + 1) + 2) * f + 8 * n * n * fm1) % p
        denominator = ((n + 1) * (n + 1)) % p
        fp = numerator * pow(denominator, -1, p) % p
        fm1, f = f, fp
    return f


def S(j, p):
    inv = pow(((j + 1) * (j + 1)) % p, -1, p)
    return [
        [0, 1],
        [8 * j * j * inv % p, (7 * j * (j + 1) + 2) * inv % p],
    ]


def K(k, p):
    out = [[1, 0], [0, 1]]
    for j in range(1, k):
        out = mm(S(j, p), out, p)
    return out


def cusp_connection(p):
    assert p % 6 == 5
    k = (p + 1) // 3
    assert k % 2 == 0 and k < p

    Kk = K(k, p)
    A0 = [[-1 % p, 0], [1, 9 * pow(8, -1, p) % p]]
    vc = [-1 % p, 8 * pow(3, -1, p) % p]
    v0 = [1, 2]
    assert mv(A0, vc, p) == v0

    # nu^2 = det(K_k A_0)
    nu = 3 * pow((-8) % p, k // 2, p) * pow((8 * k) % p, -1, p) % p
    J = scalar_matrix(pow(nu, -1, p), mm(Kk, A0, p), p)

    state_K = mv(Kk, v0, p)
    state_J = mv(J, vc, p)
    return k, Kk, J, state_K, state_J, nu


def legendre_minus_two(p):
    x = pow((-2) % p, (p - 1) // 2, p)
    return -1 if x == p - 1 else x


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Deterministic for 64-bit inputs.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def hahn_M(s):
    s = Fraction(s)
    A = (s - Fraction(1, 3)) * (s + Fraction(2, 3))
    B = Fraction(1, 3) - 2 * s * s
    C = (s - Fraction(1, 2)) * (s + Fraction(1, 6))
    return [[-B / A, -C / A], [Fraction(1), Fraction(0)]]


def mmQ(A, B):
    return [[sum(A[i][r] * B[r][j] for r in range(2))
             for j in range(2)] for i in range(2)]


def hahn_block(t):
    return mmQ(hahn_M(3 * t + 2), mmQ(hahn_M(3 * t + 1), hahn_M(3 * t)))


def hahn_block_det_formula(t):
    t = Fraction(t)
    return (
        (t + Fraction(1, 2))
        * (t - Fraction(1, 6))
        * (t + Fraction(1, 6))
        * (t + Fraction(1, 18))
        * (t + Fraction(7, 18))
        * (t + Fraction(13, 18))
        / (
            (t - Fraction(1, 9))
            * (t + Fraction(2, 9)) ** 2
            * (t + Fraction(5, 9)) ** 2
            * (t + Fraction(8, 9))
        )
    )


def main():
    # 1. Coefficient recurrence from the frozen rank-two Franel ODE.
    F = franel_integer_table(15)
    for n in range(16):
        assert F[n] == franel_direct(n)

    # 2. Exact rational three-step Hahn determinant / conductor-18 factorization.
    for t in range(0, 9):
        B = hahn_block(t)
        assert det2(B) == hahn_block_det_formula(t)

    # 3. Rank-two coefficient transfer, determinant match and SL2 normalization.
    for p in (17, 29, 41, 53, 89, 107, 149, 173, 197):
        if not is_prime(p) or p % 6 != 5:
            continue
        k, Kk, J, state_K, state_J, nu = cusp_connection(p)
        assert state_K[1] == franel_mod(k, p)
        assert state_J == [x * pow(nu, -1, p) % p for x in state_K]
        assert det2(Kk, p) == pow(-8, k - 1, p) * pow(k * k, -1, p) % p
        assert det2(J, p) == 1
        # Both coefficient transfer and cusp transfer carry the same square class.
        dK = det2(Kk, p)
        dA = (-9 * pow(8, -1, p)) % p
        assert pow(dK * pow(dA, -1, p) % p, (p - 1) // 2, p) == 1

    # Known unrestricted boundary zero: p=149, k=50.
    k, _, J149, _, state149, _ = cusp_connection(149)
    assert k == 50 and franel_mod(k, 149) == 0
    assert state149[1] == 0 and state149[0] != 0
    assert det2(J149, 149) == 1

    # 4. Task-local admissible regression, not a proof.
    admissible = []
    for m in range(1, 5001):
        q = 18 * m - 1
        if is_prime(q) and is_prime(12 * m - 1) and is_prime(12 * m + 1):
            residue = franel_mod(6 * m, q)
            admissible.append((m, q, legendre_minus_two(q), residue))
    assert len(admissible) == 137
    assert sum(1 for _, _, chi, _ in admissible if chi == 1) == 72
    assert sum(1 for _, _, chi, _ in admissible if chi == -1) == 65
    assert all(residue != 0 for _, _, _, residue in admissible)

    print("PASS")
    print("exact Franel transfer + SL2 cusp normalization verified")
    print("exact Hahn three-step conductor-18 determinant verified")
    print("admissible regression: 137 triples through m<=5000, 0 boundary zeros")


if __name__ == "__main__":
    main()
