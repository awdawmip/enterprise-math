"""R49: exact Sylvester resultant and exceptional rank-2 observer certificate.

Pure Python stdlib, exact integers and finite-field arithmetic only.
The observations concern arbitrary source amplitudes, not a native H0/B0 run.
"""
from math import isqrt

P = (2688, 6160, 4456, 1166, 85)  # descending x^4 ... x^0


def eval_poly(coeff, x):
    value = 0
    for c in coeff:
        value = value * x + c
    return value


def shift_one(coeff):
    # ascending input and output, P(x+1) by synthetic Taylor transform
    from math import comb
    src = list(reversed(coeff))
    out = [sum(src[j] * comb(j, i) for j in range(i, 5)) for i in range(5)]
    return tuple(reversed(out))


def bareiss_det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def resultant_degree_four(f, g):
    assert len(f) == len(g) == 5
    rows = []
    for p in (f, g):
        for i in range(4):
            rows.append([0] * i + list(p) + [0] * (3 - i))
    return bareiss_det(rows)


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def clean(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mod_poly_gcd_desc(f, g, p):
    a = clean([v % p for v in reversed(f)])
    b = clean([v % p for v in reversed(g)])
    while any(b):
        r = a[:]
        while len(r) >= len(b) and any(r):
            c = r[-1] * pow(b[-1], -1, p) % p
            pos = len(r) - len(b)
            for i, z in enumerate(b):
                r[pos + i] = (r[pos + i] - c * z) % p
            clean(r)
        a, b = b, r
    lead = pow(a[-1], -1, p)
    return tuple((v * lead) % p for v in a)  # ascending, monic


def ratio_a(t, p):
    n = (6*t+7)*(2*t+1)*(3*t+1)*(3*t+2)
    d = 36*(6*t+1)*(t+1)**3
    assert d % p != 0
    return n * pow(d, -1, p) % p


def ratio_b(t, p):
    n = (8*t+9)*(2*t+1)*(4*t+1)*(4*t+3)
    d = 288*(8*t+1)*(t+1)**3
    assert d % p != 0
    return n * pow(d, -1, p) % p


def main():
    q = shift_one(P)
    assert q == (2688, 16912, 39064, 39310, 14555)
    res = resultant_degree_four(P, q)
    claimed = -(2**31)*(3**2)*5*(7**3)*79411*18558017
    assert res == claimed, (res, claimed)
    assert prime(79411) and prime(18558017)
    assert 79411 % 6 == 1 and 18558017 % 6 == 5
    assert mod_poly_gcd_desc(P, q, 7) == (1,)
    assert mod_poly_gcd_desc(P, q, 79411) == (74017, 1)
    assert mod_poly_gcd_desc(P, q, 18558017) == (18558017 - 1156500, 1)
    p, k = 79411, 5394
    assert eval_poly(P, k) % p == eval_poly(P, k+1) % p == 0
    assert eval_poly(P, k+2) % p == 22144
    a = [ratio_a(k+j, p) for j in range(3)]
    b = [ratio_b(k+j, p) for j in range(3)]
    assert a == [63693, 63793, 2920], a
    assert b == [63693, 63793, 61628], b
    for j in range(3):
        assert a[j] != 0 and b[j] != 0
    A, B = 1, 1
    observer_rows = []
    for j in range(4):
        observer_rows.append((A, (-B) % p))
        if j < 3:
            A = A * a[j] % p
            B = B * b[j] % p
    determinants = [(r[0] + r[1]) % p for r in observer_rows[1:]]
    assert determinants == [0, 0, 13918], determinants
    observed_first_state = [r[0] for r in observer_rows]
    observed_second_state = [(-r[1]) % p for r in observer_rows]
    assert observed_first_state[:3] == observed_second_state[:3] == [1,63693,24323]
    assert (observed_first_state[3],observed_second_state[3]) == (29726,15808)
    print('PASS: exact 8x8 Sylvester determinant =',res)
    print('PASS: factorization = -2^31 * 3^2 * 5 * 7^3 * 79411 * 18558017')
    print('PASS: modulo-7 gcd=1; modulo-79411 gcd=x-5394; p=18558017 class=5 mod 6')
    print('PASS: p=79411, k=5394: 2-step alias; 3-step determinant=13918')
    print('PASS: two source states share (1,63693,24323), split at fourth (29726,15808)')


if __name__ == '__main__':
    main()
