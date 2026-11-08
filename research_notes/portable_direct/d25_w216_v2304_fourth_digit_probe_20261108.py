#!/usr/bin/env python3
"""Author-side exact integer probe; no native H0/B0 operation or Source write.

Data: original W216 and V2304 with full n=0,...,p-1 truncations.
The finite p^4 conjecture is tested, not asserted as a universal theorem.
"""
import math


def primes_through(limit: int):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q:limit + 1:q] = b'\x00' * ((limit - q * q) // q + 1)
    return [p for p in range(5, limit + 1) if sieve[p]]


def original_recurrence(p: int, exponent: int):
    """Exact modular hypergeometric coefficient recurrence, all denominators units."""
    mod = p ** exponent
    a = b = 1
    W = V = 0
    W_grade = [0] * exponent
    V_grade = [0] * exponent
    inv216, inv2304 = pow(216, -1, mod), pow(2304, -1, mod)
    for n in range(p):
        wn, vn = (6 * n + 1) * a % mod, (8 * n + 1) * b % mod
        W = (W + wn) % mod
        V = (V + vn) % mod
        gw = (2*n)//p + (3*n)//p
        gv = (4*n)//p
        if gw < exponent:
            W_grade[gw] = (W_grade[gw] + wn) % mod
        if gv < exponent:
            V_grade[gv] = (V_grade[gv] + vn) % mod
        if n + 1 < p:
            inv = pow(n + 1, -1, mod)
            a = a * (2*n + 1) * (2*n + 2) * (3*n + 1) * (3*n + 2) * (3*n + 3) % mod
            a = a * pow(inv, 5, mod) * inv216 % mod
            b = b * (4*n + 1) * (4*n + 2) * (4*n + 3) * (4*n + 4) % mod
            b = b * pow(inv, 4, mod) * inv2304 % mod
    assert sum(W_grade) % mod == W
    assert sum(V_grade) % mod == V
    return W, V, W_grade, V_grade


def factorial_tail_kernels(p: int):
    """Theorem: exact third-grade / p^3 readout modulo p for both models."""
    fac = [1] * p
    for i in range(1, p):
        fac[i] = fac[i-1] * i % p
    T_W = T_V = 0
    for r in range((p-3)//3 + 1):
        den = fac[2*r + 1] * fac[3*r + 2] % p
        t = 2 * (6*r + 5) * pow(fac[r], 5, p) * pow(216, r, p) % p
        T_W = (T_W + t * pow(den, -1, p)) % p
    for r in range((p-4)//4 + 1):
        t = 6 * (8*r + 7) * pow(fac[r], 4, p) * pow(2304, r, p) % p
        T_V = (T_V + t * pow(fac[4*r + 3], -1, p)) % p
    return T_W, T_V


def direct_binomial(p: int, exponent: int):
    """Independent path from original integer binomial coefficients, not recurrence."""
    mod = p ** exponent
    W = V = 0
    for n in range(p):
        wa = (6*n + 1) * math.comb(2*n, n)**2 * math.comb(3*n, n)
        va = (8*n + 1) * math.factorial(4*n) // math.factorial(n)**4
        W = (W + wa * pow(216, -n, mod)) % mod
        V = (V + va * pow(2304, -n, mod)) % mod
    return W, V


def run():
    tested = primes_through(10000)
    for p in tested:
        w, v, _, _ = original_recurrence(p, 4)
        chi = 1 if p % 3 == 1 else -1
        assert (w - 2*v + p*chi) % p**4 == 0, ('fourth-digit counterexample', p)
    print('W-2V+p*(-3/p) mod p^4: exact PASS', len(tested), 'primes 5..10000')

    for p in primes_through(2000):
        w, v, wg, vg = original_recurrence(p, 4)
        tw, tv = factorial_tail_kernels(p)
        assert wg[3] == (p**3) * tw, ('W grade-3 mismatch', p)
        assert vg[3] == (p**3) * tv, ('V grade-3 mismatch', p)
    print('Grade-3 factorial kernels: exact PASS 301 primes 5..2000, 602 ports')

    for p in [13, 19, 373]:
        w4, v4, wg, vg = original_recurrence(p, 4)
        assert (w4, v4) == direct_binomial(p, 4)
        w5, v5, _, _ = original_recurrence(p, 5)
        assert (w5, v5) == direct_binomial(p, 5)
        chi = 1 if p % 3 == 1 else -1
        obstruction = ((w5 - 2*v5 + p*chi) % p**5) // p**4
        print('p=', p, 'W4=', w4, 'V4=', v4, 'third-grade/p^3=', (wg[3]//p**3,vg[3]//p**3),
              'p5 obstruction digit=', obstruction)
        assert obstruction != 0
    print('INFERENCE: finite p^4 congruence candidate; uniform proof OPEN; p^5 extension false at p=13,19,373')


if __name__ == '__main__':
    run()
