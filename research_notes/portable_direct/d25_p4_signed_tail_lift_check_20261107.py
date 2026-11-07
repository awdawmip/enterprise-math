"""Exact p^4 source-labelled tail lift for the 216 / 2304 sums.
Only stdlib; independently evaluates full and half sums from integer binomials.
Author-side research check; not a native Source benchmark or admission.
"""
from math import comb, factorial


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n ** .5) + 1):
        if sieve[d]:
            sieve[d * d::d] = b'\x00' * len(sieve[d * d::d])
    return [i for i in range(5, n + 1) if sieve[i]]


def check(p):
    m2, m4, h = p * p, p ** 4, (p - 1) // 2
    fac = [1] * p
    harmonic = [0] * p
    for j in range(1, p):
        fac[j] = fac[j - 1] * j % m2
        harmonic[j] = (harmonic[j - 1] + pow(j, -1, p)) % p
    wilson = ((factorial(p - 1) + 1) // p) % p
    a0 = a_h = a3 = b0 = b_h = b3 = 0
    for k in range(h + 1, p):
        if 3 * k < 2 * p:  # v_p((2k)!(3k)!) = 2
            r2, r3 = 2 * k - p, 3 * k - p
            base = (6 * k + 1) * fac[r2] * fac[r3]
            base *= pow(216, -k, m2) * pow(fac[k], -5, m2)
            base %= m2
            a0 = (a0 + base) % m2
            a_h = (a_h + (base % p) * (harmonic[r2] + harmonic[r3])) % p
        else:  # valuation 3, normalized unit only modulo p
            r2, r3 = 2 * k - p, 3 * k - 2 * p
            term = -2 * (6 * k + 1) * fac[r2] * fac[r3]
            term *= pow(216, -k, p) * pow(fac[k], -5, p)
            a3 = (a3 + term) % p
        if 4 * k < 3 * p:  # valuation 2 for the 2304 port
            r4 = 4 * k - 2 * p
            base = 2 * (8 * k + 1) * fac[r4]
            base *= pow(2304, -k, m2) * pow(fac[k], -4, m2)
            base %= m2
            b0 = (b0 + base) % m2
            b_h = (b_h + 2 * (base % p) * harmonic[r4]) % p
        else:  # valuation 3
            r4 = 4 * k - 3 * p
            term = -6 * (8 * k + 1) * fac[r4]
            term *= pow(2304, -k, p) * pow(fac[k], -4, p)
            b3 = (b3 + term) % p
    assert b0 % p == 0, (p, '2304 tail divisibility')
    ja = (a_h + a3) % p
    kb = (b0 // p + b_h + b3) % p
    # Full and low sums are evaluated independently from integral binomial coefficients.
    w_low = v_low = w_full = v_full = 0
    inv216, inv2304 = pow(216, -1, m4), pow(2304, -1, m4)
    q216 = q2304 = 1
    for k in range(p):
        w = (6 * k + 1) * comb(2 * k, k) ** 2 * comb(3 * k, k)
        v = (8 * k + 1) * comb(2 * k, k) ** 2 * comb(4 * k, 2 * k)
        w = w * q216 % m4
        v = v * q2304 % m4
        w_full = (w_full + w) % m4
        v_full = (v_full + v) % m4
        if k <= h:
            w_low = (w_low + w) % m4
            v_low = (v_low + v) % m4
        q216 = q216 * inv216 % m4
        q2304 = q2304 * inv2304 % m4
    wa = (p * p * a0 + p ** 3 * (ja - 2 * wilson * (a0 % p))) % m4
    vb = (p ** 3 * kb) % m4
    assert (w_full - w_low) % m4 == wa, (p, '216 p4-tail')
    assert (v_full - v_low) % m4 == vb, (p, '2304 p4-tail')
    chi = 1 if p % 3 == 1 else -1
    low_bridge = (2 * v_low - w_low - p * chi) % m4
    predicted_bridge = (low_bridge - p * p * a0 + p ** 3 * (2 * kb - ja + 2 * wilson * (a0 % p))) % m4
    exact_bridge = (2 * v_full - w_full - p * chi) % m4
    assert predicted_bridge == exact_bridge, (p, 'signed-bridge formula')
    return (p, a0 % p, ja, kb, wilson, low_bridge, exact_bridge)


if __name__ == '__main__':
    cases = [check(p) for p in primes_upto(401)]
    assert len(cases) == 77
    assert all(row[-1] == 0 for row in cases)  # finite H, NOT a universal proof
    print('PASS 77/77 primes (5<=p<=401); independent factorial/binomial paths; p^4')
    for p in (7, 11, 13, 19, 373):
        print('p,A0_mod_p,J_A,K_B,w,low_bridge,H=', next(row for row in cases if row[0] == p))
