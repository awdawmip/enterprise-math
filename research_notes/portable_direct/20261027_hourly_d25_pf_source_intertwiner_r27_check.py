"""Exact finite-field author check for the R27 W/S truncated source intertwiner."""
from fractions import Fraction
from math import isqrt

def primes_upto(bound):
    for n in range(7, bound):
        if n % 6 != 1:
            continue
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n

def modq(q, p):
    q = Fraction(q)
    d = q.denominator % p
    if d == 0:
        raise ZeroDivisionError((q, p))
    return (q.numerator % p) * pow(d, -1, p) % p

def check_prime(p):
    m = (p - 1) // 6
    one3, one6, one12 = (modq(Fraction(1, i), p) for i in (3, 6, 12))
    a = [1]
    b = [1]
    h = [1]
    for r in range(1, m):
        aw_den = r * (r + one6) * (r + one3) % p
        bs_den = (r - one12) * (r + one6) * (r + 5 * one12) % p
        hh_den = (r - one12) * (r + 5 * one12) % p
        if 0 in (aw_den, bs_den, hh_den):
            raise AssertionError(('singular before cutoff', p, r))
        a.append(a[-1] * pow((r - one3) % p, 3, p) * pow(aw_den, -1, p) % p)
        b.append(b[-1] * pow((r - one3) % p, 3, p) * pow(bs_den, -1, p) % p)
        h.append(h[-1] * r * (r + one3) * pow(hh_den, -1, p) % p)
        assert b[-1] == (h[-1] * a[-1]) % p
    assert all(h) and all(a) and all(b)

    def lw(f, r):
        cur = f[r] if r < m else 0
        return (r * (r + one6) * (r + one3) * cur
                - pow((r - one3) % p, 3, p) * f[r - 1]) % p

    def ls(g, r):
        cur = g[r] if r < m else 0
        return (r * (r - one12) * (r + one6) * (r + 5 * one12) * cur
                - r * pow((r - one3) % p, 3, p) * g[r - 1]) % p

    for f in (a, [1] + [(7 + 3*r*r) % p for r in range(1, m)],
              [(11 + 13*r + 17*r*r) % p for r in range(m)]):
        g = [(h[r] * f[r]) % p for r in range(m)]
        for r in range(1, m+1):
            k_r = r * h[r - 1] % p
            assert k_r != 0
            assert ls(g, r) == k_r * lw(f, r) % p, (p, r)
    for r in range(1, m):
        assert lw(a, r) == 0 and ls(b, r) == 0
    w_end = lw(a, m)
    s_end = ls(b, m)
    assert w_end == a[-1] * pow(8, -1, p) % p
    assert s_end == -b[-1] * pow(48, -1, p) % p
    assert s_end == m * h[-1] * w_end % p
    return p, m, h[-1], m * h[-1] % p, w_end, s_end

if __name__ == '__main__':
    records = [check_prime(p) for p in primes_upto(2000)]
    assert len(records) == 148, len(records)
    assert all(r[4] != 0 and r[5] != 0 for r in records)
    sample = [r for r in records if r[0] in (7, 13, 19, 37, 61, 181, 373, 733, 997)]
    print('PASS', len(records), 'primes, all r=1..m, 3 distinct polynomial inputs each, and two nonzero endpoints')
    print('p m h_(m-1) transfer_factor W_boundary S_boundary')
    for r in sample:
        print(*r)
