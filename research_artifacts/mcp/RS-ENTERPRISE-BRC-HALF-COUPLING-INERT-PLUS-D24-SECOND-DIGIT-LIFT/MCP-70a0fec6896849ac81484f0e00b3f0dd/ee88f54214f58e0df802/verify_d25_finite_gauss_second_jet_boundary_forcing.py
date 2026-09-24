#!/usr/bin/env python3

# Deterministic falsifier for the D25 finite-Gauss second-jet terminal forcing.
# No finite scan is used as proof.

from math import factorial


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def inv(a, p):
    return pow(a % p, p - 2, p)

def fact_mod(n, p):
    x = 1
    for k in range(1, n + 1):
        x = (x * k) % p
    return x

def mul_jet(u, v, p):
    # tuples are (value, first derivative, second derivative) at a=0
    u0, u1, u2 = u
    v0, v1, v2 = v
    return (
        u0 * v0 % p,
        (u1 * v0 + u0 * v1) % p,
        (u2 * v0 + 2 * u1 * v1 + u0 * v2) % p,
    )

def terminal_jet(m, p):
    n = 6 * m
    f = (1, 0, 0)
    g = (1, 0, 0)
    for j in range(n):
        # (-m+a+j), derivative 1, second derivative 0
        f = mul_jet(f, ((j - m) % p, 1, 0), p)
        # (-2m+2a+j), derivative 2, second derivative 0
        g = mul_jet(g, ((j - 2 * m) % p, 2, 0), p)
    fg = mul_jet(f, g, p)
    den = fact_mod(n, p)
    den2inv = inv(den * den, p)
    return tuple(x * den2inv % p for x in fg)

def closed_c2(m, p):
    num = 4
    if m % 2:
        num = -num
    for n in (m, 2 * m, 4 * m - 1, 5 * m - 1):
        num = num * fact_mod(n, p) % p
    den = fact_mod(6 * m, p)
    return num % p * inv(den * den, p) % p

def boundary_at_half(m, p, c2):
    # B_m(1/2) = -20 m^2 c_N''(0) 2^{-p}.
    return (-20 * m * m * c2 * inv(pow(2, p, p), p)) % p

def main():
    targets = [p for p in range(5, 5000) if is_prime(p) and p % 24 in (13, 19)]
    by_class = {13: 0, 19: 0}
    failures = []
    for p in targets:
        by_class[p % 24] += 1
        m = (p - 1) // 6
        j0, j1, j2 = terminal_jet(m, p)
        c2 = closed_c2(m, p)
        b = boundary_at_half(m, p, c2)
        if j0 != 0 or j1 != 0 or j2 != c2 or b != (-2) % p:
            failures.append({
                'p': p, 'm': m, 'jet': (j0, j1, j2),
                'closed_c2': c2, 'boundary': b, 'expected_boundary': (-2) % p,
            })
    print('target_primes', len(targets))
    print('class_counts', by_class)
    print('failures', failures)
    if failures:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
