#!/usr/bin/env python3
"""Exact original-Gauss truncated-tail Hensel-root transport for D25/LIFT.

AUTHOR-SIDE verification only: not the native H0/B0 divided-power experiment.
All divisions are inverses of p-units modulo p**3; no floating point.
"""
from math import factorial


def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[0:2] = b'\x00\x00'
    for q in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q:limit:q] = b'\x00' * len(sieve[q * q:limit:q])
    return [q for q in range(13, limit) if sieve[q] and q % 24 in (13, 19)]


def evaluate(coefs, final_index, point, mod):
    """Evaluate G(x) and G'(x), coefs[n]=[(1/6)_n(1/3)_n/(n!)**2]*2**(-n)."""
    w = (2 * point) % mod
    value = derivative_w = 0
    for n in range(final_index, -1, -1):
        derivative_w = (derivative_w * w + value) % mod
        value = (value * w + coefs[n]) % mod
    return value, (2 * derivative_w) % mod


def root(coefs, final_index, p):
    """Unique Hensel zero mod p**3 above x=1/2 mod p."""
    mod = p**3
    x = pow(2, -1, p)
    assert evaluate(coefs, final_index, x, mod)[0] % p == 0
    for k in (1, 2):
        value, deriv = evaluate(coefs, final_index, x, mod)
        assert value % p**k == 0 and deriv % p
        digit = (-value // p**k * pow(deriv % p, -1, p)) % p
        x += digit * p**k
    x %= mod
    assert evaluate(coefs, final_index, x, mod)[0] == 0
    return x


def factorial_tail(p, m):
    """Independent factorial description for F_p, computed in F_p."""
    f = [1] * p
    for k in range(1, p):
        f[k] = f[k-1] * k % p
    pref = (-1 if m & 1 else 1) * f[m] * f[2*m] * pow(18, -1, p)
    inv2 = pow(2, -1, p)
    acc = 0
    for n in range(2*m + 1, p):
        numer = f[n-m-1] * f[n-2*m-1] % p
        denom = pow(f[n]*f[n] % p, -1, p)
        acc = (acc + numer * denom * pow(inv2, n, p)) % p
    return pref * acc % p


def check(p):
    assert p % 24 in (13, 19)
    m = (p - 1)//6
    mod = p**3
    coefs = [1]
    # c_n/2**n is an original Gauss coefficient at z=1/2.
    # All denominators are p-units for 0<=n<p.
    for n in range(p-1):
        unit_denom = 36 * (n+1)**2
        coefs.append(coefs[-1]*(6*n+1)*(3*n+1)*pow(unit_denom, -1, mod) % mod)
    assert all(v % p**2 == 0 for v in coefs[2*m+1:])
    tail = sum(coefs[2*m+1:]) % mod
    assert tail % p**2 == 0
    F = tail // p**2
    assert F == factorial_tail(p, m), (p, F, factorial_tail(p,m))
    z0 = pow(2, -1, mod)
    _, g_full = evaluate(coefs, p-1, z0, mod)
    _, g_low = evaluate(coefs, 2*m, z0, mod)
    g = g_full % p
    assert g and g == g_low % p
    zeta_low = root(coefs, 2*m, p)
    zeta_full = root(coefs, p-1, p)
    shift = (zeta_full - zeta_low) % mod
    assert shift % p**2 == 0
    shift_digit = shift // p**2
    assert shift_digit == (-F * pow(g, -1, p)) % p
    # Signed-root-observer correction: 6*g**2*((d_full-d_low)/p) = 6*g*F.
    observer_correction = 6 * g * F % p
    d_full = (z0 - zeta_full) % mod
    d_low = (z0 - zeta_low) % mod
    assert d_full % p == d_low % p == 0
    assert ((d_full-d_low) % mod)//p**2 == F*pow(g,-1,p)%p
    return p, F, g, zeta_low, zeta_full, shift_digit, observer_correction


def main():
    target = primes_below(5000)
    outputs = [check(p) for p in target]
    exceptions = [x[0] for x in outputs if x[1] == 0]
    for row in outputs:
        if row[0] in (13, 19, 37, 43, 211, 373):
            print('exact_certificate p,F,g,zeta_low,zeta_full,full_minus_low_over_p2,signed_observer_port', *row)
    print('target_primes', len(target), 'in_13_19_mod_24_below_5000')
    print('F_zero_target_primes_below_5000', exceptions)
    print('PASS_D25_EXACT_GAUSS_TAIL_HENSEL_ROOT_TRANSPORT')


if __name__ == '__main__':
    main()