#!/usr/bin/env python3
"""D25 portable prime-field check of the A216 resonant endpoint transport.

Author-side research regression; not a Source-native benchmark or theorem acceptance.
All p-adic divisions are performed before finite-field reduction.
"""
from math import factorial


def primes_below(bound):
    for p in range(7, bound):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            yield p


def inv(value, p):
    return pow(value % p, -1, p)


def check_prime(p):
    assert p % 6 == 1
    m = (p - 1) // 6
    f = [1] * p
    for n in range(1, p):
        f[n] = f[n - 1] * n % p
    C = 3 * pow(216, 2 * m, p) * pow(f[2 * m], 5, p) * inv(f[4 * m + 1], p) % p
    h = 1
    for s in range(m - 1):
        numerator = 4 * (2 * s + 3) * pow(3 * s + 2, 3, p)
        denominator = 3 * (2 * s + 1) * (6 * s + 7) * (3 * s + 4) * (s + 1)
        assert denominator % p
        h = h * numerator * inv(denominator, p) % p
    # This last step is NOT an ordinary continuation: it uses p*h_m.
    boundary_num = 4 * (2 * m + 1) * pow(3 * m - 1, 3, p)
    boundary_den = 3 * (2 * m - 1) * (3 * m + 1) * m
    assert boundary_den % p
    p_hm = h * boundary_num * inv(boundary_den, p) % p
    transported_kernel = C * p_hm % p

    # Reflection extension at s=m-1 is singular, but p*g_m is well-defined.
    g_last = ((18 * m - 1) * pow(216, 3 * m - 1, p)
              * pow(f[3 * m - 1], 5, p)
              * inv(f[6 * m - 1] * f[3 * m - 2], p)) % p
    p_gm = ((18 * m + 5) * pow(216, 3 * m, p)
            * pow(f[3 * m], 5, p)
            * inv(f[6 * m] * f[3 * m + 1], p)) % p

    # Independent factorial-unit arithmetic for w_{3m}/p.
    N = 3 * m
    a_endpoint_over_p = (f[6 * m] * (-f[N - 1])
                         * inv(pow(f[N], 5, p) * pow(216, N, p), p)) % p
    w_endpoint_over_p = (6 * N + 1) * a_endpoint_over_p % p
    chi = pow(6, (p - 1) // 2, p)
    assert chi in (1, p - 1)
    assert C * h % p == g_last, (p, 'interior-last')
    assert p_gm == -9 * g_last % p, (p, 'g pole')
    assert transported_kernel == -27 * g_last % p, (p, 'h pole')
    assert transported_kernel == 3 * p_gm % p, (p, 'factor 3')
    assert w_endpoint_over_p == 9 * g_last % p, (p, 'low endpoint')
    assert p_gm == -4 * chi % p, (p, 'legendre g')
    assert w_endpoint_over_p == 4 * chi % p, (p, 'legendre low')
    assert transported_kernel == -12 * chi % p, (p, 'legendre pole')
    assert (transported_kernel + 3 * w_endpoint_over_p) % p == 0
    if p in (7, 13, 19, 31, 37, 373):
        numerator = ((6 * N + 1) * factorial(2 * N) * (factorial(3 * N) // p))
        denominator = factorial(N)**5 * 216**N
        raw = numerator * inv(denominator, p) % p
        assert raw == w_endpoint_over_p, (p, 'raw-binomial')
    return C, h, p_hm, g_last, p_gm, w_endpoint_over_p, transported_kernel, (chi if chi == 1 else -1)


def regularized_endpoint_probe(p):
    """Calculate the finite part of C*h_m+3*w_(3m)/p^2 exactly modulo p.

    In F_p use the parent p-adic numerator modulo p^2 before division.
    This probes (but does not prove) the residual low/middle port matching.
    """
    m = (p - 1) // 6
    N = 3 * m
    modulus = p * p
    f = [1] * p
    for n in range(1, p):
        f[n] = f[n - 1] * n % modulus
    C = 3 * pow(216, 2 * m, modulus) * pow(f[2 * m], 5, modulus) * inv(f[4 * m + 1], modulus) % modulus
    h = 1
    H = 1
    for s in range(m - 1):
        h = (h * 4 * (2 * s + 3) * pow(3 * s + 2, 3, modulus) *
             inv(3 * (2 * s + 1) * (6 * s + 7) * (3 * s + 4) * (s + 1), modulus)) % modulus
        H = (H + h) % modulus
    p_hm = (h * 4 * (2 * m + 1) * pow(3 * m - 1, 3, modulus) *
            inv(3 * (2 * m - 1) * (3 * m + 1) * m, modulus)) % modulus
    factorial_3N_without_p = 1
    for n in range(1, 3 * N + 1):
        if n % p:
            factorial_3N_without_p = factorial_3N_without_p * n % modulus
    wN_over_p = ((6 * N + 1) * f[2 * N] * factorial_3N_without_p *
                 inv(pow(f[N], 5, modulus) * pow(216, N, modulus), modulus)) % modulus
    combined_numerator = (C * p_hm + 3 * wN_over_p) % modulus
    assert combined_numerator % p == 0
    regularized = combined_numerator // p

    # Original A216 lower window, full signed coefficients modulo p^3.
    modulus3 = p ** 3
    a = 1
    A_low = 0
    for n in range(N + 1):
        A_low = (A_low + (6 * n + 1) * a) % modulus3
        if n < N:
            a = (a * (2 * n + 2) * (2 * n + 1) *
                 (3 * n + 3) * (3 * n + 2) * (3 * n + 1) *
                 inv(216 * (n + 1)**5, modulus3)) % modulus3
    assert (A_low - p) % (p * p) == 0
    J = ((A_low - p) // (p * p)) % p
    Q = C * H % p
    assert (J + Q) % p == 0
    return regularized, J, Q


def main():
    tests = 0
    target = 0
    for p in primes_below(1500):
        if p % 6 != 1:
            continue
        values = check_prime(p)
        tests += 1
        target += p % 24 in (13, 19)
        if p in (7, 13, 19, 31, 37, 373):
            print('CERT', p, 'C,h,p*h_m,g_last,p*g_m,wN/p,C*p*h_m,chi=', *values)
    for p in (13, 19, 373):
        R, J, Q = regularized_endpoint_probe(p)
        print('FIRST_JET', p, 'regularized_boundary', R, 'original_low_port', J, 'middle_port', Q, 'boundary_not_full_port', R != Q)
    print('PASS_RESONANT_BOUNDARY_FACTOR_3', tests, 'prime inputs; target primes', target)
    print('PROVED_FORMULAS: C_m*p*h_m == 3*p*g_m == -3*w_(3m)/p == -12*(6/p) mod p')
    print('NATIVE_H0_B0_NOT_EXECUTED; UNREVIEWED_NOT_ADMITTED')


if __name__ == '__main__':
    main()
