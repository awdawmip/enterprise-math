#!/usr/bin/env python3
"""Exact coefficient-ring checks for original E3_v/Hesse conjugate isomorphism.

Mathematical proof: research_returns/D25_E3_NATIVE_GM_SIGNED_HESSE_GAUGE_20261111.md
This is author checking of integral de Rham/curve geometry, not native
H0/B0 divided-power or p-adic Frobenius [X]U validation.
"""


def add(a, b, q):
    return ((a[0] + b[0]) % q, (a[1] + b[1]) % q)


def neg(a, q):
    return (-a[0] % q, -a[1] % q)


def sub(a, b, q):
    return add(a, neg(b, q), q)


def scale(k, a, q):
    return (k * a[0] % q, k * a[1] % q)


def mul(a, b, q):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % q,
            (a[0] * b[1] + a[1] * b[0]) % q)


def power(a, e, q):
    out = (1, 0)
    while e:
        if e & 1:
            out = mul(out, a, q)
        a = mul(a, a, q)
        e >>= 1
    return out


def inverse(a, q):
    norm = (a[0] ** 2 - 2 * a[1] ** 2) % q
    return scale(pow(norm, -1, q), (a[0], -a[1]), q)


def cube_root_t(p, t):
    """Small p only; use a pinned large-p witness for p=373."""
    q = p * p
    for x in range(p):
        for y in range(p):
            a0 = (x, y)
            if power(a0, 3, p) != (t[0] % p, t[1] % p):
                continue
            diff = sub(t, power(a0, 3, q), q)
            assert all(c % p == 0 for c in diff)
            f = (diff[0] // p, diff[1] // p)
            deriv = scale(3, power(a0, 2, p), p)
            delta = mul(f, inverse(deriv, p), p)
            root = ((x + p * delta[0]) % q, (y + p * delta[1]) % q)
            assert power(root, 3, q) == t
            return root
    raise ValueError('no cube root of target t')


def sqrt_minus_three(p):
    q = p * p
    x = next(x for x in range(p) if (x * x + 3) % p == 0)
    delta = ((-3 - x*x) // p) * pow(2*x, -1, p) % p
    r = (x + p * delta) % q
    assert (r*r + 3) % q == 0
    return r


def check(p):
    assert p % 24 in (13, 19)
    q = p * p
    v = scale(pow(4, -1, q), (2, -1), q)
    conj = scale(pow(4, -1, q), (2, 1), q)
    assert add(v, conj, q) == (1, 0)
    assert mul(v, conj, q) == (pow(8, -1, q), 0)
    t = (4, -2 % q)  # 1/(1-v), original signed E3 j-port.
    assert mul(t, conj, q) == (1, 0)
    if p == 373:
        a = (91441, (-93269) % q)
    else:
        a = cube_root_t(p, t)
    assert power(a, 3, q) == t
    r = sqrt_minus_three(p)
    s = scale(r, a, q)
    assert power(s, 2, q) == scale(-3, power(a, 2, q), q)
    A_E = sub(scale(24, v, q), (27, 0), q)
    B_E = add(sub(scale(16, power(v, 2, q), q), scale(72, v, q), q), (54, 0), q)
    assert A_E == ((-15) % q, (-6) % q)
    assert B_E == (24 % q, 14 % q)
    A_H = scale(-27, mul(a, add(t, (8, 0), q), q), q)
    B_H = scale(54, sub(sub(power(t, 2, q), scale(20, t, q), q), (8, 0), q), q)
    assert mul(power(s, 4, q), A_E, q) == A_H
    assert mul(power(s, 6, q), B_E, q) == B_H
    d = sub(t, (1, 0), q)
    assert (d[0]**2-2*d[1]**2) % q == 1

    # Independently compute GM via I0,I1,I2 exact-differential reductions.
    D = add(scale(4, power(A_E, 3, q), q), scale(27, power(B_E, 2, q), q), q)
    Dinv = inverse(D, q)
    A_prime = (24, 0)
    B_prime = sub(scale(32, v, q), (72, 0), q)
    inv2 = pow(2, -1, q)
    m11 = mul(neg(add(mul(A_prime, power(A_E, 2, q), q),
                       scale(9*inv2, mul(B_prime, B_E, q), q), q), q), Dinv, q)
    m21 = mul(sub(scale(9*inv2, mul(A_prime, B_E, q), q),
                  scale(3, mul(B_prime, A_E, q), q), q), Dinv, q)
    m12 = mul(sub(scale(3*inv2, mul(mul(A_prime, A_E, q), B_E, q), q),
                  mul(B_prime, power(A_E, 2, q), q), q), Dinv, q)
    f = 2 * pow(3, -1, q) % q
    assert m11 == scale(f, (-1, -1), q)
    assert m12 == scale(f, (-5, -2), q)
    assert m21 == (f, 0)
    assert neg(m11, q) == scale(f, (1, 1), q)
    Q = (((6, 0), (-4 % q, -4 % q)), ((0, 0), (4, 0)))
    assert scale(6, m11, q) == Q[0][1]
    assert scale(6, m21, q) == Q[1][1]
    assert (Q[0][0][0]*Q[1][1][0]) % q == 24
    target_port = add(Q[0][0], scale(6, Q[0][1], q), q), scale(6, Q[1][1], q)
    assert target_port == ((-18 % q, -24 % q), (24 % q, 0))
    if p == 373:
        assert r == 89697
        assert a == (91441, 45860)
        assert s == (50569, 16406)
        assert A_H == (90958, 96462)
        assert B_H == (135673, 1296)
    return {'p': p, 'r': r, 'a': a, 's': s, 'AH': A_H, 'BH': B_H,
            'M_v': (m11, m12, m21, neg(m11, q)), 'Qdet': 24}


def main():
    for p in (13, 19, 37, 43, 373):
        r = check(p)
        print('PASS p=%s: r=%s a=%s s=%s (A_H,B_H)=(%s,%s); detQ=%s'
              % (p, r['r'], r['a'], r['s'], r['AH'], r['BH'], r['Qdet']))
    print('PASS: original E3 signed-port Hesse isomorphism; direct rank-two Gauss-Manin and cyclic basis')
    print('NOT_RUN: source-fixed native divided-power H0/B0 [X]U and kappa/Delta-R validation')


if __name__ == '__main__':
    main()
