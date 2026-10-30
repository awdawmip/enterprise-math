#!/usr/bin/env python3
"""Exact checks for D25 GH-141/142 (author-side portable research only).

Quadratic-fibre character sums over F_(p^2), exhaustive t / selected B,
plus an independent Hasse-coefficient check of the p=3347 odd-moment
orientation witness. No native Enterprise Math experiment is attempted.
"""
from collections import Counter


class Fp2:
    def __init__(self, p):
        self.p = p
        self.d = next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)
        self.z, self.one = (0, 0), (1, 0)

    def a(self, x, y):
        p = self.p
        return ( (x[0] + y[0]) % p, (x[1] + y[1]) % p )

    def neg(self, x):
        p = self.p
        return (-x[0] % p, -x[1] % p)

    def sub(self, x, y):
        return self.a(x, self.neg(y))

    def m(self, x, y):
        p, d = self.p, self.d
        return ((x[0] * y[0] + d * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def power(self, x, n):
        assert n >= 0
        acc = self.one
        while n:
            if n & 1:
                acc = self.m(acc, x)
            x = self.m(x, x)
            n >>= 1
        return acc

    def inv(self, x):
        assert x != self.z
        return self.power(x, self.p * self.p - 2)

    def chi(self, x):
        if x == self.z:
            return 0
        y = self.power(x, (self.p * self.p - 1) // 2)
        assert y in (self.one, self.neg(self.one))
        return 1 if y == self.one else -1

    def elems(self):
        return ((a, b) for a in range(self.p) for b in range(self.p))

    def scale(self, x, z):
        return ((x[0] * z) % self.p, (x[1] * z) % self.p)


def direct_fibers(K):
    f = {}
    for x in K.elems():
        t = K.neg(K.a(K.m(x, x), x))
        f[t] = f.get(t, 0) + K.chi(x)
    return f


def direct_moment_sequence(K, B, upto):
    """Original f=xg character moment, without using fibre reflection."""
    p = K.p
    result = [K.z for _ in range(upto + 1)]
    for x in K.elems():
        if x == K.z:
            continue
        g = K.a(K.a(K.m(x, x), x), B)
        if g == K.z:
            continue
        f = K.m(x, g)
        ch = K.chi(f)
        v = K.inv(g)  # exactly x/f
        z = K.one
        for r in range(upto + 1):
            result[r] = K.a(result[r], K.scale(z, ch))
            z = K.m(z, v)
    return result


def pair_witness_p3347():
    p = 3347
    K = Fp2(p)
    assert K.d == 2
    rho = (0, 1)
    B = K.scale(K.a(K.one, K.scale(rho, 2 * pow(3, -1, p))), pow(8, -1, p))
    N = (p - 1) // 2
    factorial = [1] * (N + 1)
    for i in range(1, N + 1):
        factorial[i] = factorial[i - 1] * i % p
    invfact = [pow(z, -1, p) for z in factorial]
    H = K.z
    Hp = K.z
    x_power = K.one
    x_prev = K.one
    for u in range(N // 2 + 1):
        coeff = factorial[N] * invfact[u] * invfact[u] * invfact[N - 2 * u] % p
        H = K.a(H, K.scale(x_power, coeff))
        if u:
            Hp = K.a(Hp, K.scale(x_prev, (u * coeff) % p))
        x_prev, x_power = x_power, K.m(x_power, B)
    S1 = K.scale(K.m(Hp, K.power(H, p)), 2)
    expected = (0, 362)
    assert H == (783, 0), (H, Hp)
    assert Hp == (0, 1351), (H, Hp)
    assert S1 == expected, S1
    reflected = K.sub((pow(4, -1, p), 0), B)
    assert reflected == K.power(B, p)
    return B, H, Hp, S1, K.power(S1, p)


def main():
    checked_fibres = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 59, 83):
        K = Fp2(p)
        f = direct_fibers(K)
        c = (pow(4, -1, p), 0)
        assert len(f) <= p * p
        hist = Counter(f.get(t, 0) for t in K.elems())
        q = p * p
        expected = {2: (q - 9) // 8, -2: (q - 1) // 8,
                    1: 2, 0: 3 * (q - 1) // 4}
        assert hist == Counter(expected), (p, hist, expected)
        assert f.get(K.z) == 1 and f.get(c) == 1
        for t in K.elems():
            reflected = K.sub(c, t)
            assert f.get(t, 0) == f.get(reflected, 0), (p, t, reflected)
            checked_fibres += 1
        print('FIBER', p, 'q', q, 'hist', dict(hist), 'PASS')
    print('PASS_GH141_FULL_FIBER_REFLECTION', checked_fibres)

    checked_moments = 0
    examples = []
    for p in (11, 19, 43):
        K = Fp2(p)
        assert K.d == 2
        c = (pow(4, -1, p), 0)
        B0 = K.scale(K.a(K.one, K.scale((0, 1), 2 * pow(3, -1, p))), pow(8, -1, p))
        B_choices = [B0, (0, 0), (1, 0), (3, 5), c]
        limit = p * p - 2 if p <= 19 else 50
        for B in B_choices:
            reflected = K.sub(c, B)
            s = direct_moment_sequence(K, B, limit)
            t = direct_moment_sequence(K, reflected, limit)
            for r, (v, w) in enumerate(zip(s, t)):
                assert w == (K.neg(v) if r & 1 else v), (p, B, r, v, w)
                checked_moments += 1
            if B == B0:
                assert K.power(B, p) == reflected
                for r, v in enumerate(s):
                    assert K.power(v, p) == (K.neg(v) if r & 1 else v)
                examples.append((p, s[0], s[1], s[(p - 1) // 2 + 1], s[(p * p - 1) // 2] if (p * p - 1) // 2 <= limit else None))
        print('MOMENT', p, 'B_choices', len(B_choices), 'r0_to', limit, 'PASS')
    print('PASS_GH141_ALL_R_CHARACTER_MOMENT_DUALITY', checked_moments)
    print('ORIGINAL_MARK_EXAMPLES', examples)

    B, H, Hp, S1, S1p = pair_witness_p3347()
    print('P3347_ORIENTATION', 'B', B, 'H', H, 'Hp', Hp,
          'S1', S1, 'Frobenius', S1p)
    print('PASS_GH142_P3347_NONZERO_ODD_OBSERVER_AND_HISTOGRAM')
    print('PASS_GH141_GH142_ALL_EXACT')


if __name__ == '__main__':
    main()
