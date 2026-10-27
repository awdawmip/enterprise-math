#!/usr/bin/env python3
"""D25 author-side exact finite-field Gauss–Legendre certificate.

This verifies a proved conditional-on-accepted-CM0 scalar theorem, not native H0/B0.
Only built-in Python integer arithmetic is used.
"""
from math import comb


def multiply(a, b, modulus):
    result = [0] * (len(a) + len(b) - 1)
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            result[j + k] = (result[j + k] + aj * bk) % modulus
    return result


def integrate_even(poly, p):
    # poly[j] is coefficient of x^(2j); 2*j+1 < p.
    assert 2 * len(poly) - 1 < p
    return sum(c * pow(2 * j + 1, -1, p) for j, c in enumerate(poly)) % p


def polynomial_even_legendre(p):
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    n = 2 * m
    den = pow(2, -n, p)
    return [(-1) ** (m - j) * comb(n, m - j) * comb(n + 2*j, n) * den % p
            for j in range(m + 1)]


def cm0_gauss_check(p):
    # Only p=13,19 mod24 is within the frozen target.
    assert p % 24 in (13, 19)
    m, n = (p - 1)//6, (p - 1)//3
    P = polynomial_even_legendre(p)
    inv2 = pow(2, -1, p)
    R = [0] * m
    R[m-1] = P[m] * inv2 % p
    for j in range(m-1, 0, -1):
        R[j-1] = (P[j] + R[j])*inv2 % p
    cm0_rem = (P[0] + R[0]) % p
    assert cm0_rem == 0, (p, 'CM0 P divisible by 2x²-1 failed')
    V = [2*j*P[j] % p for j in range(1, m + 1)]  # P'(x)/x
    PR = multiply(P, R, p)
    RV = multiply(R, V, p)
    H = [(RV[j] if j < len(RV) else 0)
         - (RV[j-1] if j >= 1 else 0) for j in range(len(RV) + 1)]
    H = [c % p for c in H]
    assert integrate_even(PR, p) == 0, ('Legendre orthogonality', p)
    assert integrate_even(H, p) == 1, ('two-node Gauss quadrature', p)
    Q = [(-PR[j] + 6*H[j]) % p for j in range(len(PR))]
    assert integrate_even(Q, p) == 6, ('final integral', p)
    # Independent original signed (k,s) moment, no use of P, R or quadrature.
    A = [comb(m,j)*comb(2*m,j)*pow(2, -j, p) % p for j in range(m+1)]
    t = multiply(A, A, p)
    f = [(6*k+1)*v % p for k,v in enumerate(t)]
    assert sum(f) % p == 0, ('F(1) source',p)
    u, usum, nested = 1, 0, 0
    for k, fk in enumerate(f):
        nested = (nested + fk * usum) % p
        if k < n-1:
            usum = (usum + u) % p
            u = u * (4*(k+1)) * pow(2*k+3, -1, p) % p
    # The sum over s<k at k=n needs u_{n-1} but not u_n.
    # Above loop adds u only until k=n-2, so recompute direct for clarity.
    U, acc, nested2 = [], 0, 0
    u = 1
    for s in range(n):
        U.append(u)
        u = u * (4*(s+1)) * pow(2*s+3,-1,p) % p
    for k, fk in enumerate(f):
        nested2 = (nested2 + fk*acc) % p
        if k < n: acc = (acc + U[k]) % p
    assert nested2 == 6, ('source weighted nested moment',p,nested2)
    return {'p':p,'degree_P':n,'CM0_division_remainder':cm0_rem,
            'integral_P_times_R':integrate_even(PR,p),
            'integral_Gauss_two_root_support':integrate_even(H,p),
            'T_direct':nested2,'T_integral':integrate_even(Q,p)}


def split_control(p):
    assert p % 24 in (1,7)
    m = (p-1)//6
    P = polynomial_even_legendre(p)
    r = [0]*m
    r[-1] = P[-1]*pow(2,-1,p) % p
    for j in range(m-1,0,-1):
        r[j-1] = (P[j]+r[j])*pow(2,-1,p)%p
    return {'p':p,'non_CM0_division_remainder':(P[0]+r[0])%p}


if __name__ == '__main__':
    for p in (13,19,37,43,61,67,211,373):
        print(cm0_gauss_check(p))
    for p in (7,31):
        print(split_control(p))
    print('PASS_D25_CM0_GAUSS_TWO_NODE_FULL_TARGET_CLASS_PROOF_GUARD')
