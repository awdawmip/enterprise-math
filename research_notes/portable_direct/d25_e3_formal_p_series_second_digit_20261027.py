#!/usr/bin/env python3
"""Original E3 formal-group p-series coefficient: author-side, not H0/B0."""
from math import comb


def witness(p):
    assert p > 3 and p % 24 in (13, 19)
    modulus = p**3
    zero, one = (0, 0), (1, 0)

    def add(a, b):
        return ((a[0] + b[0]) % modulus, (a[1] + b[1]) % modulus)

    def mul(a, b):
        return ((a[0]*b[0] + 2*a[1]*b[1]) % modulus,
                (a[0]*b[1] + a[1]*b[0]) % modulus)

    def scale(k, a):
        return ((k*a[0]) % modulus, (k*a[1]) % modulus)

    c = scale(pow(108, -1, modulus), (2, -1))
    powers = [one]
    for _ in range((p-1)//3):
        powers.append(mul(powers[-1], c))

    # Path A: exact original E3 hypergeometric coefficients.
    a = []
    for n in range(p):
        coefficient = zero
        for j in range(n//3 + 1):
            coefficient = add(coefficient,
                              scale(comb(2*j, j)*comb(n-j, 2*j), powers[j]))
        a.append(coefficient)

    # Path B: independently solve 2*D*H' + D'*H = 0.
    d = [one, (-2 % modulus, 0), one, scale(-4, c)]
    h = [zero] * p
    h[0] = one
    for n in range(1, p):
        raw = zero
        for j in range(1, min(3, n)+1):
            raw = add(raw, scale(2*n-j, mul(d[j], h[n-j])))
        h[n] = scale(-pow(2*n, -1, modulus), raw)
    assert a == h
    assert a[0] == a[1] == one
    assert a[p-1][0] % p == a[p-1][1] % p == 0

    # The p-local logarithm has lambda_j = a_{j-1}/j;
    # j < p are units and lambda_p is integral since a_{p-1} is p-divisible.
    lam = [zero]
    for j in range(1, p):
        lam.append(scale(pow(j, -1, modulus), a[j-1]))

    # Coefficient [x^p] L(x)^2 mod p, preserving both T-branches.
    cp = zero
    for j in range(1, p):
        cp = add(cp, mul(lam[j], lam[p-j]))
    cp = (cp[0] % p, cp[1] % p)

    # Independent symmetry identity: 1/(j*(p-j)) = -1/j^2 modulo p.
    cp_other = zero
    for j in range(1, p):
        cp_other = add(cp_other,
                       scale(-pow(j, -2, p), mul(a[j-1], a[p-j-1])))
    assert cp == (cp_other[0] % p, cp_other[1] % p)

    # [x^p][p]_E = a_{p-1} - p^2*C_p/2 mod p^3.
    correction = scale(p*p * pow(2, -1, modulus), cp)
    coefficient = add(a[p-1], scale(-1, correction))
    assert coefficient[0] % p == coefficient[1] % p == 0
    return p, a[p-1], cp, correction, coefficient


if __name__ == '__main__':
    for prime in (13, 19, 37, 43, 61, 67, 211, 373):
        print(witness(prime))
    p, a, c, correction, coeff = witness(373)
    assert a == (46042747, 33130606)
    assert c == (46, 350)
    assert correction == (3199967, 24347575)
    assert coeff == (42842780, 8783031)
    assert (23*23-2*175*175) % 373 == 78  # nonzero norm of C/2
    print('D25_ORIGINAL_E3_FORMAL_P_SERIES_SECOND_DIGIT_PASS')
