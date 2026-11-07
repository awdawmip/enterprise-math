#!/usr/bin/env python3
"""D25 original-E3 Proposition-16 quartic-twist bridge.

Exact finite-field checks only. The all-prime coefficient identity is proved
in the companion note from the d=3 supersingular Proposition 16 and the exact
original-E3 CM eigenbasis. This script does not execute native H0/B0 or [X]U.
"""
from math import comb


def pair_add(x, y, q):
    return ((x[0] + y[0]) % q, (x[1] + y[1]) % q)


def pair_mul(x, y, q):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % q,
            (x[0] * y[1] + x[1] * y[0]) % q)


def pair_inv(x, p):
    norm = (x[0] * x[0] - 2 * x[1] * x[1]) % p
    ni = pow(norm, -1, p)
    return (x[0] * ni % p, -x[1] * ni % p)


def e3_coefficients(p):
    """Original E3 identity-branch a_(p-1), regular eta coefficient b_(p-1)."""
    q = p ** 3
    n = p - 1
    c = (2 * pow(108, -1, q) % q, -pow(108, -1, q) % q)
    powers = [(1, 0)]
    for _ in range(1, (n + 2) // 3 + 1):
        powers.append(pair_mul(powers[-1], c, q))

    a = (0, 0)
    b = (0, 0)
    for j in range(n // 3 + 1):
        coeff = comb(2 * j, j) * comb(n - j, 2 * j)
        a = pair_add(a, ((coeff * powers[j][0]) % q,
                         (coeff * powers[j][1]) % q), q)
    for j in range(1, (n + 2) // 3 + 1):
        coeff = (comb(2 * j, j) * comb(n - j + 1, 2 * j - 1)
                 * pow(2, -1, q))
        b = pair_add(b, ((coeff * powers[j][0]) % q,
                         (coeff * powers[j][1]) % q), q)

    assert a[0] % p == 0 and a[1] % p == 0
    A = ((a[0] // p) % p, (a[1] // p) % p)
    B_plain = (b[0] % p, b[1] % p)
    beta = (4 * pow(72, -1, p) % p, -pow(72, -1, p) % p)
    B_CM = pair_mul(pair_inv(beta, p), B_plain, p)

    assert pair_mul(A, B_plain, p) == beta
    assert pair_mul(A, B_CM, p) == (1, 0)
    assert pow(2, (p - 1) // 2, p) == p - 1  # (2/p) = -1
    return A, B_plain, beta, B_CM


def harmonic(n, p, order=1):
    return sum(pow(k, -order, p) for k in range(1, n + 1)) % p


def phi_xx_mod_p(p):
    """Second x-derivative of Phi_m(x,1/2) at x=m, exact modulo p."""
    m = (p - 1) // 6
    A = [1, 0, 0]  # coefficients in t for (-m-t)_k
    B = [1, 0, 0]  # coefficients in t for (-2m-2t)_k
    inv_fact_sq = 1
    inv_two_pow = 1
    total_t2 = 0

    for k in range(p):
        t2 = (A[2] * B[0] + A[1] * B[1] + A[0] * B[2]) % p
        scale = inv_fact_sq * inv_two_pow % p
        total_t2 = (total_t2 + t2 * scale) % p

        aa, bb = k - m, k - 2 * m
        A = [(aa * A[0]) % p,
             (aa * A[1] - A[0]) % p,
             (aa * A[2] - A[1]) % p]
        B = [(bb * B[0]) % p,
             (bb * B[1] - 2 * B[0]) % p,
             (bb * B[2] - 2 * B[1]) % p]
        if k + 1 < p:
            inv_fact_sq = inv_fact_sq * pow(k + 1, -2, p) % p
        inv_two_pow = inv_two_pow * pow(2, -1, p) % p

    return 2 * total_t2 % p


def low_and_high_second_jet(p):
    """L2_low and V_(4m) from the exact three-band decomposition."""
    m = (p - 1) // 6
    q, e, j2 = [], [], []
    Hm, H2m = harmonic(m, p), harmonic(2 * m, p)
    Hm2, H2m2 = harmonic(m, p, 2), harmonic(2 * m, p, 2)

    for n in range(m + 1):
        qn = comb(m, n) * comb(2 * m, n) * pow(2, -n, p) % p
        en = (-(Hm - harmonic(m - n, p)) * pow(6, -1, p)
              -(H2m - harmonic(2 * m - n, p)) * pow(3, -1, p)) % p
        jn = (-(Hm2 - harmonic(m - n, p, 2)) * pow(36, -1, p)
              -(H2m2 - harmonic(2 * m - n, p, 2)) * pow(9, -1, p)) % p
        q.append(qn)
        e.append(en)
        j2.append(jn)

    L2_low = sum(q[n] * (e[n] * e[n] + j2[n]) * pow(2, -1, p)
                 for n in range(m + 1)) % p

    c = [None] * (4 * m + 1)
    c[1] = pow(10, -1, p)
    for a in range(1, 4 * m):
        c[a + 1] = (c[a] * 36 * a * a
                    * pow((6 * a + 5) * (3 * a + 2), -1, p)) % p
    V = [0] * (4 * m + 1)
    for a in range(1, 4 * m + 1):
        V[a] = (V[a - 1] + c[a]) % p
    return L2_low, V[4 * m]


def middle_dual_observer(p):
    """Same u_(m+r) carrier, observed by the Phi_xx and cutoff ports."""
    m = (p - 1) // 6
    c = [None] * (2 * m + 1)
    c[1] = pow(10, -1, p)
    for a in range(1, 2 * m):
        c[a + 1] = (c[a] * 36 * a * a
                    * pow((6 * a + 5) * (3 * a + 2), -1, p)) % p

    H = [0] * (2 * m + 1)
    for i in range(1, 2 * m + 1):
        H[i] = sum((1 + 6 * (i - a)) * c[a]
                   for a in range(1, i + 1)) % p

    q_m = comb(2 * m, m) * pow(2, -m, p) % p
    K = [None] * (m + 1)
    K[1] = 1
    f = [0] * (m + 1)
    u = [0] * (m + 1)

    for r in range(1, m + 1):
        if r > 1:
            s = r - 1
            K[r] = (K[r - 1] * 3 * s * (6 * s + 1)
                    * pow((6 * s + 5) ** 2, -1, p)) % p
        f[r] = ((harmonic(r - 1, p) - harmonic(m, p)) * pow(6, -1, p)
                -(harmonic(2 * m, p) - harmonic(m - r, p))
                * pow(3, -1, p)) % p
        u[r] = q_m * pow(50, -1, p) * K[r] % p

    L2_mid = sum(u[r] * f[r] for r in range(1, m + 1)) % p
    S_mid = 2 * sum(u[r] * H[m + r] for r in range(1, m + 1)) % p
    KH_sigma = sum(K[r] * H[m + r] for r in range(1, m + 1)) % p
    assert S_mid == q_m * pow(25, -1, p) * KH_sigma % p
    return q_m, KH_sigma, L2_mid, S_mid


def verify(p):
    A, B_plain, beta, B_CM = e3_coefficients(p)
    phi2 = phi_xx_mod_p(p)
    L2_low, V4m = low_and_high_second_jet(p)
    q_m, KH_sigma, L2_mid, S_mid = middle_dual_observer(p)

    assert (phi2 * pow(72, -1, p)) % p == (L2_low + L2_mid + V4m) % p
    return {
        "p": p,
        "A": A,
        "B_plain": B_plain,
        "beta": beta,
        "B_CM": B_CM,
        "A_times_B_plain": beta,
        "A_times_B_CM": (1, 0),
        "quartic_product_factor": p - 1,
        "Phi_xx": phi2,
        "Phi_xx_over_72": phi2 * pow(72, -1, p) % p,
        "L2_low": L2_low,
        "L2_mid": L2_mid,
        "V4m": V4m,
        "q_m": q_m,
        "KH_sigma": KH_sigma,
        "S_mid": S_mid,
    }


def main():
    for p in (13, 19, 37, 43, 61, 67, 211, 373):
        e3_coefficients(p)
    for p in (19, 373):
        print(verify(p))
    print("PASS_D25_E3_PROP16_QUARTIC_TWIST_BRIDGE")


if __name__ == "__main__":
    main()
